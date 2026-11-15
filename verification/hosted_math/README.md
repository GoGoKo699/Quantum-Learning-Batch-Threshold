# Actual GitHub mathematics checks

These three unmodified helpers come from `GoGoKo699/Guinevere` at commit `5731b136156e426c2adf10fb5b09fdbccc8c9de4`, under `plugins/merlin-arthur-research/skills/merlin-arthur-research/scripts/`.

| Helper | SHA256 |
|---|---|
| `capture_hosted_math.cjs` | `c96f5c769ef62711137fc4d75e110cfb40c0db149c87590cdfb463b69a648b54` |
| `probe_hosted_math.cjs` | `cf2374791bef13f29ce254179ea00aa1c38943272fc1881ec8c188876c22f631` |
| `check_rendered_math.py` | `edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe` |

The [workflow](../../.github/workflows/hosted-math.yml) checks out the exact same-repository pull-request head with read-only repository permissions. It uses a fresh anonymous browser to inspect real commit-pinned GitHub pages at both required widths. No source replacement, rendered-content injection, sign-in, or certificate-ignore setting is used.

The representative README probe runs first. A successful probe is followed by the collector's full default Markdown inventory, including this page. The workflow retains the diagnostic and full reports, HTML, and screenshots even when a later step fails. A failed probe prevents the full capture from running; its failed evidence remains available. Workflow artifacts expire after 14 days and are not permanent preservation.

The [local runtime adapter](run_hosted_math.cjs) uses the collector's supported runtime hook while leaving those three helpers unchanged. Before screenshots it returns to the page top and lets the sticky toolbar settle. It also saves ordinary viewport screenshots at the top and after a 500-pixel scroll, so a reviewer can inspect text covered by the toolbar in a full-page screenshot. Their separate `visual-supplements.json` records the source, URLs, viewports, times and file hashes. The adapter changes no page content, style, compiler or comparison rule. Its SHA256 is `c6b0d86968b3415376cf921c63e6d57f08a979fca7c37999c70913281002fff6`.

For a permitted local browser environment, install Playwright 1.56.1 and MathJax 3.2.1 outside the scientific source, install the matching Chromium browser, and set `NODE_PATH` to that dependency directory. Run:

```bash
node verification/hosted_math/run_hosted_math.cjs probe \
  --root /absolute/checkout --repository GoGoKo699/Quantum-Learning-Batch-Threshold \
  --revision FULL_COMMIT_SHA --page README.md --output /absolute/new-probe-directory

node verification/hosted_math/run_hosted_math.cjs capture \
  --root /absolute/checkout --repository GoGoKo699/Quantum-Learning-Batch-Threshold \
  --revision FULL_COMMIT_SHA --output /absolute/new-full-directory
```

Use an actual full commit ID and a new empty output directory for every attempt. A structural pass does not replace visual inspection, scientific review, or final source-bound completion checks. The repository's existing scientific and navigation checkers run separately from hosted comparison.
