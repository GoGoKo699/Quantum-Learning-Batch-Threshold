#!/usr/bin/env python3
"""Check repository navigation, shared learning structure, and report freshness.

These checks do not establish scientific correctness, educational quality, or
hosted mathematical rendering. They use only Python's standard library.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit


class CheckFailure(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


def unfenced(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token[0]
            elif token[0] == fence:
                fence = None
            lines.append("")
        elif fence is None:
            lines.append(line)
        else:
            lines.append("")
    return "\n".join(lines)


def heading_ids(text):
    """GitHub-style slugs for ordinary Markdown headings used in this repo."""
    ids = set(re.findall(r'<a\s+[^>]*(?:id|name)=["\']([^"\']+)["\']', text,
                         flags=re.I))
    seen = {}
    for line in unfenced(text).splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        label = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match.group(1))
        label = re.sub(r"<[^>]+>", "", label)
        label = html.unescape(label).lower().strip()
        slug = re.sub(r"[^\w\- ]", "", label).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        ids.add(slug if count == 0 else f"{slug}-{count}")
    return ids


def link_targets(text):
    text = unfenced(text)
    # Markdown destinations in this repository use unspaced paths. Titles, if
    # present, are ignored. External URLs need not be decoded or contacted.
    inline = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))")
    for match in inline.finditer(text):
        yield match.group(1) or match.group(2)
    reference = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", re.M)
    for match in reference.finditer(text):
        yield match.group(1) or match.group(2)
    for match in re.finditer(r"<(?:a|img)\s+[^>]*(?:href|src)=[\"']([^\"']+)[\"']",
                             text, re.I):
        yield match.group(1)


def check_links(repo, markdown):
    errors = []
    checked = 0
    anchor_cache = {}
    for source in markdown:
        for target in link_targets(source.read_text()):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or parts.path.startswith("/"):
                continue
            checked += 1
            destination = (source.parent / unquote(parts.path)).resolve() if parts.path else source
            try:
                destination.relative_to(repo)
            except ValueError:
                errors.append(f"{source.relative_to(repo)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{source.relative_to(repo)}: missing destination: {target}")
                continue
            if parts.fragment and destination.suffix.lower() in {".md", ".txt"}:
                if destination not in anchor_cache:
                    anchor_cache[destination] = heading_ids(destination.read_text())
                if unquote(parts.fragment) not in anchor_cache[destination]:
                    errors.append(f"{source.relative_to(repo)}: missing heading fragment: {target}")
    require(not errors, "\n".join(errors))
    return {"relative_links_checked": checked, "markdown_files": len(markdown),
            "fragment_documents": len(anchor_cache)}


def check_milestones(repo):
    candidates = []
    for path in (repo / "learning").glob("*.md"):
        entries = re.findall(r"(?m)^#{1,6}\s+M(\d{2})(?:\b|\s|[—–:-])", unfenced(path.read_text()))
        if entries:
            candidates.append((path, entries))
    require(len(candidates) == 1,
            f"Expected one canonical milestone-heading map, found {len(candidates)}")
    path, entries = candidates[0]
    require(entries == [f"{i:02d}" for i in range(1, 31)],
            "Canonical headings must be exactly M01 through M30 in order")
    current_phase = None
    phases = []
    milestones = []
    current = None
    for line in unfenced(path.read_text()).splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            title = heading.group(2)
            milestone = re.match(r"M(\d{2})(?:\b|\s|[—–:-])", title)
            if milestone:
                current = {"id": int(milestone.group(1)), "phase": current_phase, "body": []}
                milestones.append(current)
            else:
                low = title.lower()
                category = ("background" if "background" in low or "preliminar" in low
                            else "narrative" if "narrative" in low or "innovation" in low else None)
                if category and ("phase" in low or len(heading.group(1)) <= 2):
                    current_phase = category
                    phases.append(category)
                    current = None
        elif current is not None:
            current["body"].append(line)
    require(phases == ["background", "narrative"],
            "The canonical map must have background/preliminaries then narrative/innovation phases")
    dependencies = 0
    allocation = {name: 0 for name in phases}
    for item in milestones:
        require(item["phase"] in allocation, f"M{item['id']:02d} has no declared phase")
        allocation[item["phase"]] += 1
        dependency_lines = []
        for line in item["body"]:
            plain = line.replace("**", "").strip().lstrip("-* ")
            if re.match(r"(?i)^dependenc(?:y|ies)(?:\s+and\s+story\s+role)?\s*[:.]", plain):
                dependency_lines.append(plain)
        require(len(dependency_lines) == 1,
                f"M{item['id']:02d} needs one explicit dependency field")
        for value in re.findall(r"\bM(\d{2})\b", dependency_lines[0]):
            previous = int(value)
            require(1 <= previous < item["id"],
                    f"M{item['id']:02d} has a missing, current, or forward dependency M{value}")
            dependencies += 1
    require(all(allocation.values()), "Each phase must contain understanding targets")
    return {"canonical_map": str(path.relative_to(repo)), "milestones": len(milestones),
            "phase_allocation": allocation, "dependency_references": dependencies}


def check_anchor_and_private_material(repo, markdown):
    learning = repo / "learning"
    bridges = [path for path in learning.glob("*.md") if "bridge" in path.stem.lower()]
    require(len(bridges) == 1, "Expected exactly one educational source bridge")
    overview = learning / "README.md"
    require(overview.is_file(), "Missing common learning overview")
    for path in [overview, bridges[0]]:
        text = path.read_text()
        require("Watrous" in text and "2018" in text and "Theory of Quantum Information" in text,
                f"Selected Watrous2018 identity is incomplete in {path.relative_to(repo)}")
    forbidden_names = {"coaching.md", "learner_state.json", "learner_progress.json", "tutor_state.json"}
    bad_files = [str(path.relative_to(repo)) for path in repo.rglob("*")
                 if path.is_file() and ".git" not in path.parts and path.name.lower() in forbidden_names]
    require(not bad_files, "Private coaching files in scientific repository: " + ", ".join(bad_files))
    rules = [r"Revise\s*(?:→|->|–|—)\s*Learn\s*(?:→|->|–|—)\s*Test",
             r"failed challenge", r"next challenge size", r"learning-test errors?",
             r"current learner progress"]
    leaked = []
    for path in markdown:
        text = path.read_text()
        for rule in rules:
            if re.search(rule, text, flags=re.I):
                leaked.append(f"{path.relative_to(repo)}: {rule}")
    require(not leaked, "Personal coaching instructions found: " + "; ".join(leaked))
    return {"selected_anchor": "John Watrous, The Theory of Quantum Information (2018)",
            "bridge": str(bridges[0].relative_to(repo)),
            "private_file_names_checked": sorted(forbidden_names),
            "limits": "Source identity and explicit private-rule patterns only; semantic educational review is separate"}


def check_science_report(repo):
    report_path = repo / "verification" / "results.json"
    require(report_path.is_file(), "Missing saved scientific report")
    report = json.loads(report_path.read_text())
    require(report.get("passed") is True, "Saved scientific report did not pass")
    require(report.get("tests") and all(test.get("passed") is True for test in report["tests"]),
            "Saved scientific report has a missing or failed test group")
    expected = {str(path.relative_to(repo)) for path in (repo / "science").glob("*.md")}
    expected.add("verification/check_science.py")
    recorded = report.get("input_sha256", {})
    require(set(recorded) == expected,
            "Saved scientific report's input set differs from current science files/checker")
    stale = [name for name, digest in recorded.items()
             if hashlib.sha256((repo / name).read_bytes()).hexdigest() != digest]
    require(not stale, "Saved scientific report is stale for: " + ", ".join(stale))
    return {"report": str(report_path.relative_to(repo)), "matched_inputs": len(expected),
            "checked_at_utc": report.get("checked_at_utc"),
            "limits": "Checks report scope and hashes, not the report's scientific truth"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional complete JSON report path")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    markdown = sorted(path for path in repo.rglob("*.md") if ".git" not in path.parts)
    checks = []
    for name, function in [
        ("relative_navigation", lambda: check_links(repo, markdown)),
        ("canonical_learning_map", lambda: check_milestones(repo)),
        ("selected_anchor_and_private_boundary", lambda: check_anchor_and_private_material(repo, markdown)),
        ("scientific_report_freshness", lambda: check_science_report(repo)),
    ]:
        try:
            checks.append({"name": name, "passed": True, **function()})
        except (CheckFailure, OSError, ValueError, KeyError) as error:
            checks.append({"name": name, "passed": False, "error": str(error)})
    passed = all(check["passed"] for check in checks)
    inputs = markdown + [Path(__file__).resolve(), repo / "verification" / "results.json"]
    report = {"schema_version": 1, "passed": passed,
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "checks": checks,
              "input_sha256": {str(path.relative_to(repo)): hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in inputs if path.is_file()},
              "limits": "Structural navigation, shared-map, explicit boundary and report-freshness checks only; no theorem, educational-quality, or hosted-rendering certification"}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"passed": passed, "checks": len(checks),
                      "failed": [check for check in checks if not check["passed"]],
                      "output": str(args.output) if args.output else None}, separators=(",", ":")))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
