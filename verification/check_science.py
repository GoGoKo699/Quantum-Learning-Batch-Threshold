#!/usr/bin/env python3
"""Finite scientific diagnostics for the marked-Pauli batch account.

Only NumPy and Python's standard library are used. Matrix checks are numerical
checks of explicitly constructed operators, not exact-arithmetic proof.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import numpy as np

SEED = 20261115
TOL = 3e-11
PAULI = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.diag([1, -1]).astype(complex),
}
AXES = ("X", "Y", "Z")
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
S_GATE = np.diag([1, 1j]).astype(complex)


class CheckFailure(RuntimeError):
    """A finite diagnostic failed."""


def require(condition, message):
    if not bool(condition):
        raise CheckFailure(message)


def kron_all(matrices):
    out = np.ones((1, 1), dtype=complex)
    for matrix in matrices:
        out = np.kron(out, matrix)
    return out


def word_matrix(word):
    return kron_all(PAULI[axis] for axis in word)


def tensor_power(matrix, copies):
    return kron_all(matrix for _ in range(copies))


def max_abs(matrix):
    return float(np.max(np.abs(matrix))) if np.size(matrix) else 0.0


def bits(index, count):
    return tuple((index >> (count - 1 - j)) & 1 for j in range(count))


def ghz_group_binary(k):
    """Enumerate star-generator products as binary symplectic pairs."""
    all_sites = (1 << k) - 1
    generators = [(all_sites, 0)]
    generators += [(0, (1 << (k - 1)) | (1 << (k - 1 - j)))
                   for j in range(1, k)]
    group = set()
    for choices in itertools.product((0, 1), repeat=k):
        x = z = 0
        for choice, (gx, gz) in zip(choices, generators):
            if choice:
                x ^= gx
                z ^= gz
        group.add((x, z))
    return group


def ghz_circuit(k):
    """Build H on site zero followed by each controlled-X, as raw matrices."""
    dim = 1 << k
    unitary = np.kron(H, np.eye(1 << (k - 1)))
    for target in range(1, k):
        permutation = np.zeros((dim, dim), dtype=complex)
        for column in range(dim):
            row = column
            if column & (1 << (k - 1)):
                row ^= 1 << (k - 1 - target)
            permutation[row, column] = 1
        unitary = permutation @ unitary
    return unitary


def ghz_covered(word):
    if not word:
        return True
    return ((all(axis in ("X", "Y") for axis in word)
             and word.count("Y") % 2 == 0)
            or (all(axis == "Z" for axis in word) and len(word) % 2 == 0))


def ghz_decoder(word):
    """Return the formula's eigenvalue for every raw GHZ-circuit outcome."""
    k = len(word)
    require(ghz_covered(word), "Decoder called on an uncovered word")
    out = []
    for outcome in range(1 << k):
        z = [(-1) ** bit for bit in bits(outcome, k)]
        if all(axis == "Z" for axis in word):
            value = math.prod(z[1:])
        else:
            y_sites = [j for j, axis in enumerate(word) if axis == "Y"]
            value = (-1) ** (len(y_sites) // 2) * z[0]
            value *= math.prod(z[j] for j in y_sites if j != 0)
        out.append(value)
    return np.asarray(out, dtype=float)


def single_qubit_cliffords():
    """Generate signed Pauli actions independently from H and S matrices."""
    pending = [np.eye(2, dtype=complex)]
    found = {}
    while pending:
        unitary = pending.pop()
        action = []
        for axis in AXES:
            transformed = unitary @ PAULI[axis] @ unitary.conj().T
            overlaps = [float(np.trace(PAULI[a] @ transformed).real / 2)
                        for a in AXES]
            j = int(np.argmax(np.abs(overlaps)))
            require(abs(abs(overlaps[j]) - 1) < TOL, "Invalid Clifford action")
            action.append((AXES[j], 1 if overlaps[j] > 0 else -1))
        key = tuple(action)
        if key in found:
            continue
        found[key] = unitary
        pending.extend([H @ unitary, S_GATE @ unitary])
    require(len(found) == 24, "H/S generation did not produce 24 Clifford actions")
    return [(unitary, action) for action, unitary in found.items()]


def check_binary_counts(_rng):
    counts = {}
    for k in range(1, 13):
        group = ghz_group_binary(k)
        require(len(group) == 2 ** k, f"GHZ generator dependence at k={k}")
        count = sum((x | z) == (1 << k) - 1 for x, z in group)
        formula = 2 ** (k - 1) + int(k % 2 == 0)
        require(count == formula, f"GHZ full-support count mismatch at k={k}")
        counts[k] = count
    return {"cases": 12, "counts": counts,
            "method": "Independent binary symplectic enumeration of star-generator products"}


def check_ghz_operators(rng):
    cliffords = single_qubit_cliffords()
    max_residual = 0.0
    checked_covered = checked_uncovered = y_first = all_z = local_cases = 0
    for k in range(1, 7):
        dim = 1 << k
        unitary = ghz_circuit(k)
        residual = max_abs(unitary.conj().T @ unitary - np.eye(dim))
        max_residual = max(max_residual, residual)
        require(residual < TOL, f"GHZ circuit not unitary at k={k}")
        covered_words = []
        uncovered_words = []
        for word in itertools.product(AXES, repeat=k):
            if ghz_covered(word):
                covered_words.append(word)
            else:
                uncovered_words.append(word)
        require(len(covered_words) == 2 ** (k - 1) + int(k % 2 == 0),
                "Word membership and independent group count disagree")
        for word in covered_words:
            raw = word_matrix(word)
            transformed = unitary.conj().T @ raw @ unitary
            decoded = ghz_decoder(word)
            residual = max_abs(transformed - np.diag(decoded))
            max_residual = max(max_residual, residual)
            require(residual < TOL, f"Raw GHZ decoder mismatch: {word}")
            checked_covered += 1
            y_first += int(word[0] == "Y")
            all_z += int(all(axis == "Z" for axis in word))
            for contrast in (-0.6, 0.0, 0.45, 1.0):
                state = (np.eye(dim) + contrast * raw) / dim
                born = np.diag(unitary.conj().T @ state @ unitary).real
                require(float(np.min(born)) > -TOL, "Negative Born probability")
                mean = float(born @ decoded)
                residual = abs(mean - contrast)
                max_residual = max(max_residual, residual)
                require(residual < TOL, "Decoded Born-law mean is incorrect")
                plus_probability = float(np.sum(born[decoded == 1]))
                require(abs(plus_probability - (1 + contrast) / 2) < TOL,
                        "Decoded full Bernoulli law is incorrect")
        # A deterministic selection of genuinely uncovered raw operators.
        for word in uncovered_words[:12]:
            diagonal = np.diag(unitary.conj().T @ word_matrix(word) @ unitary)
            residual = max_abs(diagonal)
            max_residual = max(max_residual, residual)
            require(residual < TOL, f"Uncovered word has nonzero diagonal: {word}")
            checked_uncovered += 1
        # Include signed local-Clifford conjugation in the raw operator check.
        selected = covered_words[:3] + covered_words[-3:]
        for word in selected:
            choices = [cliffords[int(rng.integers(len(cliffords)))] for _ in range(k)]
            local = kron_all(choice[0] for choice in choices)
            actual_word = []
            sign = 1
            for axis, (_matrix, action) in zip(word, choices):
                new_axis, new_sign = action[AXES.index(axis)]
                actual_word.append(new_axis)
                sign *= new_sign
            measured_basis = local @ unitary
            transformed = (measured_basis.conj().T @ word_matrix(actual_word)
                           @ measured_basis)
            target = sign * ghz_decoder(word)
            residual = max_abs(transformed - np.diag(target))
            max_residual = max(max_residual, residual)
            require(residual < TOL, "Local-Clifford sign decoder mismatch")
            local_cases += 1
    require(y_first > 0 and all_z == 3, "Requested decoder edge cases were not tested")
    return {"cases": checked_covered + checked_uncovered + local_cases,
            "covered_raw_operator_cases": checked_covered,
            "uncovered_diagonal_cases": checked_uncovered,
            "local_clifford_cases": local_cases, "y_at_first_site_cases": y_first,
            "even_all_z_cases": all_z, "sizes": list(range(1, 7)),
            "max_absolute_residual": max_residual,
            "method": "Raw H/CNOT circuit and Kronecker Pauli matrices versus parity decoder; direct Born probabilities"}


def fraction_h(k, counts):
    return Fraction(1) if k == 0 else Fraction(counts[k], 3 ** k)


def check_fraction_coverage(_rng):
    counts = {k: sum((x | z) == (1 << k) - 1
                    for x, z in ghz_group_binary(k))
              for k in range(1, 13)}
    cases = 0
    negative_third_base = 0
    for n, q, batch in itertools.product(
            range(1, 13), (Fraction(1, 5), Fraction(1, 2),
                           Fraction(3, 4), Fraction(5, 6)), (1, 2, 3, 5, 7)):
        t = (1 - q) ** batch
        direct = sum(Fraction(math.comb(n, k)) * t ** k * (1 - t) ** (n - k)
                     * fraction_h(k, counts) for k in range(n + 1))
        closed = ((1 - t / 3) ** n + (1 - 2 * t / 3) ** n
                  + (1 - 4 * t / 3) ** n - (1 - t) ** n) / 2
        beta_power = (1 - t / 3) ** n
        require(direct == closed, "Exact binomial closed form mismatch")
        require(beta_power / 2 <= direct <= beta_power,
                "Exact half-beta coverage bound failed")
        negative_third_base += int(1 - 4 * t / 3 < 0)
        cases += 1
    require(negative_third_base > 0, "Negative third-base edge case was omitted")
    return {"cases": cases, "arithmetic": "fractions.Fraction exact rational",
            "n_values": list(range(1, 13)),
            "q_values": ["1/5", "1/2", "3/4", "5/6"], "batch_values": [1, 2, 3, 5, 7],
            "negative_third_base_cases": negative_third_base,
            "method": "Binomial average of independently enumerated stabilizer counts versus generating-function closed form"}


def check_odd_representation(_rng):
    rows = []
    for copies in (1, 3, 5):
        dim = 1 << copies
        even_parity = [j for j in range(dim) if j.bit_count() % 2 == 0]
        columns = even_parity + [(dim - 1) ^ j for j in even_parity]
        change = np.eye(dim)[:, columns]
        multiplicity = np.eye(dim // 2)
        residuals = {}
        for axis in AXES:
            actual = change.conj().T @ tensor_power(PAULI[axis], copies) @ change
            sign = (-1) ** ((copies - 1) // 2) if axis == "Y" else 1
            target = sign * np.kron(PAULI[axis], multiplicity)
            residual = max_abs(actual - target)
            require(residual < TOL, f"Odd-copy Pauli representation failed: {copies},{axis}")
            residuals[axis] = residual
        rows.append({"odd_copies": copies, "multiplicity": dim // 2,
                     "residuals": residuals})
    return {"cases": 9, "rows": rows,
            "method": "Raw tensor Pauli operators in an independently constructed parity/complement basis"}


def full_payload_word(n, unknown_sites, unknown_axes):
    word = [AXES[(2 * j + 1) % 3] for j in range(n)]
    for site, axis in zip(unknown_sites, unknown_axes):
        word[site] = axis
    return tuple(word)


def q_subset(pauli_word, block_size, subset):
    dim = pauli_word.shape[0]
    return kron_all(pauli_word if j in subset else np.eye(dim)
                    for j in range(block_size))


def check_pauli_response(rng):
    cases = [(1, 1, ()), (1, 1, (0,)), (2, 1, (0,)), (2, 1, (0, 1)),
             (2, 3, ()), (2, 3, (0,)), (2, 3, (0, 1)), (3, 2, (0, 2))]
    evaluations = 0
    max_ratio = 0.0
    for n, batch, unknown_sites in cases:
        dim = 1 << (n * batch)
        k = len(unknown_sites)
        bound = (2 / 3) ** k
        states = []
        for _ in range(4):
            vector = rng.normal(size=dim) + 1j * rng.normal(size=dim)
            vector /= np.linalg.norm(vector)
            states.append(vector)
        for size in range(1, batch + 1, 2):
            for subset in itertools.combinations(range(batch), size):
                operators = [q_subset(word_matrix(full_payload_word(n, unknown_sites, axes)),
                                      batch, subset)
                             for axes in itertools.product(AXES, repeat=k)]
                for vector in states:
                    response = sum(float(np.vdot(vector, op @ vector).real) ** 2
                                   for op in operators) / (3 ** k)
                    require(response <= bound + TOL, "Odd-subset response bound failed")
                    max_ratio = max(max_ratio, response / bound)
                    evaluations += 1
    # A known-site reduction that is genuinely signed, not a density operator.
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    omega = np.outer(bell, bell.conj())
    weighted = np.kron(PAULI["I"], PAULI["Z"]) @ omega
    reduced = np.trace(weighted.reshape(2, 2, 2, 2), axis1=1, axis2=3)
    eigenvalues = np.linalg.eigvalsh(reduced)
    require(eigenvalues[0] < -0.49 and eigenvalues[1] > 0.49,
            "Known-site reduction did not exercise a negative eigenvalue")
    require(np.sum(np.abs(eigenvalues)) <= 1 + TOL, "Signed reduction trace norm failed")
    response_sum = sum(float(np.trace(reduced @ PAULI[axis]).real) ** 2
                       for axis in AXES)
    require(abs(response_sum - 1) < TOL, "Signed known-site Pauli coefficient check failed")
    return {"cases": evaluations + 1, "configurations": [
                {"n": n, "block_size": batch, "unknown_sites": list(sites)}
                for n, batch, sites in cases],
            "max_response_to_bound_ratio": max_ratio,
            "signed_reduction_eigenvalues": [float(x) for x in eigenvalues],
            "method": "Raw subset-Pauli expectations of random complex pure block effects; explicit Bell-state signed known-site reduction"}


def random_joint_povm(rng, dim, outcomes=5):
    raw = []
    for _ in range(outcomes):
        matrix = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
        raw.append(matrix.conj().T @ matrix)
    total = sum(raw)
    values, vectors = np.linalg.eigh(total)
    require(float(np.min(values)) > 0, "POVM normalization matrix not positive")
    inverse_root = (vectors * (values ** -0.5)) @ vectors.conj().T
    effects = [inverse_root @ matrix @ inverse_root for matrix in raw]
    require(max_abs(sum(effects) - np.eye(dim)) < TOL, "POVM effects do not sum to identity")
    for effect in effects:
        require(float(np.linalg.eigvalsh(effect)[0]) > -TOL, "Nonpositive POVM effect")
    return effects


def finite_a(batch, contrast):
    return ((1 + contrast) ** batch - (1 - contrast) ** batch) ** 2 / (1 - contrast) ** batch


def check_joint_kl(rng):
    configurations = [(1, 3, ()), (1, 3, (0,)),
                      (2, 2, ()), (2, 2, (0,)), (2, 2, (0, 1)),
                      (2, 3, ()), (2, 3, (0,)), (2, 3, (0, 1)),
                      (3, 2, (1,)), (3, 2, (0, 1, 2))]
    rows = []
    for n, batch, unknown_sites in configurations:
        payload_dim = 1 << n
        block_dim = payload_dim ** batch
        effects = random_joint_povm(rng, block_dim)
        k = len(unknown_sites)
        for contrast in (0.25, 0.65):
            kl = chi = 0.0
            max_probability_residual = 0.0
            for axes in itertools.product(AXES, repeat=k):
                pword = word_matrix(full_payload_word(n, unknown_sites, axes))
                plus = tensor_power((np.eye(payload_dim) + contrast * pword) / payload_dim, batch)
                minus = tensor_power((np.eye(payload_dim) - contrast * pword) / payload_dim, batch)
                pplus = np.array([np.trace(effect @ plus).real for effect in effects])
                pminus = np.array([np.trace(effect @ minus).real for effect in effects])
                require(np.min(pplus) > 0 and np.min(pminus) > 0,
                        "Nonpositive finite-contrast outcome probability")
                residual = max(abs(float(np.sum(pplus)) - 1),
                               abs(float(np.sum(pminus)) - 1))
                max_probability_residual = max(max_probability_residual, residual)
                require(residual < TOL, "Born outcome law not normalized")
                kl += float(np.sum(pplus * np.log(pplus / pminus))) / (3 ** k)
                chi += float(np.sum((pplus - pminus) ** 2 / pminus)) / (3 ** k)
            bound = finite_a(batch, contrast) * (2 / 3) ** k
            require(kl <= chi + TOL, "KL exceeds chi-squared")
            require(chi <= bound + TOL, "Conditional finite-contrast block bound failed")
            rows.append({"n": n, "block_size": batch, "unknown_sites": list(unknown_sites),
                         "contrast": contrast, "averaged_kl": kl, "averaged_chi_squared": chi,
                         "analytic_bound": bound, "chi_to_bound_ratio": chi / bound,
                         "max_probability_normalization_residual": max_probability_residual})
    return {"cases": len(rows), "povm_configurations": len(configurations),
            "outcomes_per_povm": 5, "max_block_hilbert_dimension": 64,
            "max_chi_to_bound_ratio": max(row["chi_to_bound_ratio"] for row in rows),
            "rows": rows,
            "method": "Direct tensor density matrices and independently normalized random general joint POVMs; enumerate unresolved axes at finite +/- contrast"}


def input_hashes(repo):
    paths = sorted((repo / "science").glob("*.md"))
    require(bool(paths), "No science files found for input hashing")
    paths.append(Path(__file__).resolve())
    return {str(path.relative_to(repo)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the complete JSON report to this path")
    args = parser.parse_args()
    started = time.perf_counter()
    repo = Path(__file__).resolve().parents[1]
    rng = np.random.default_rng(SEED)
    tests = []
    for name, function in (
        ("binary_symplectic_ghz_counts", check_binary_counts),
        ("raw_ghz_operators_and_sign_decoder", check_ghz_operators),
        ("exact_rational_binomial_coverage", check_fraction_coverage),
        ("odd_tensor_pauli_representation", check_odd_representation),
        ("odd_subset_response_and_signed_reduction", check_pauli_response),
        ("finite_contrast_general_joint_povm_kl", check_joint_kl),
    ):
        test_started = time.perf_counter()
        try:
            result = function(rng)
            tests.append({"name": name, "passed": True, **result,
                          "duration_seconds": time.perf_counter() - test_started})
        except Exception as error:
            tests.append({"name": name, "passed": False,
                          "error_type": type(error).__name__, "error": str(error),
                          "duration_seconds": time.perf_counter() - test_started})
    passed = all(test["passed"] for test in tests)
    report = {
        "schema_version": 1,
        "passed": passed,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "duration_seconds": time.perf_counter() - started,
        "deterministic_seed": SEED,
        "software": {"python": platform.python_version(), "numpy": np.__version__,
                     "platform": platform.platform()},
        "diagnostic_scope": {
            "exact": "Binary stabilizer enumeration and rational binomial identities at the listed sizes",
            "numerical": "Explicit raw matrix/operator, Born-law, odd-Pauli and joint-POVM checks at the listed small dimensions",
            "absolute_tolerance": TOL,
            "not_established": [
                "Universal or asymptotic theorem validity by testing",
                "Literature priority or independent expert verification",
                "Physical hardware behavior, noise tolerance or full learning runtime",
                "Arbitrary-size collective POVM enumeration",
            ],
            "sampling_note": "Random matrices use a fixed seed. No end-to-end experiment Monte Carlo is presented; decoded Bernoulli laws are checked directly from explicit Born probabilities.",
        },
        "input_sha256": input_hashes(repo),
        "tests": tests,
    }
    output = None
    if args.output:
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    summary = {"passed": passed, "test_groups": len(tests),
               "finite_cases": sum(test.get("cases", 0) for test in tests),
               "duration_seconds": round(report["duration_seconds"], 3),
               "output": str(output) if output else None,
               "failed_groups": [test["name"] for test in tests if not test["passed"]]}
    print(json.dumps(summary, separators=(",", ":")))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

