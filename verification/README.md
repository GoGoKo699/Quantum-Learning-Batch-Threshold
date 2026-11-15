# Reproduce the finite scientific checks

The general result follows from the written [finite converse](../science/collective_converse.md), [attaining protocol](../science/attaining_measurements.md), and [phase-boundary argument](../science/phase_boundary.md). This suite checks load-bearing finite algebra and probability calculations independently of those prose derivations.

## Run

From the repository root, with Python 3.10 or newer:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/check_science.py --output /tmp/batch-threshold-checks.json
```

Only NumPy and the Python standard library are used. The seed is fixed at `20261115`. A passing run exits zero and prints a compact JSON summary; a failed diagnostic exits nonzero. The full report identifies every case, residual, bound, software version, input SHA-256 and observation time. It uses explicit runtime checks that remain active under optimized Python.

The [saved report](results.json) contains the observed run for the committed science inputs. Its own file is excluded from input hashes to avoid self-reference. Running to `/tmp` leaves the repository unchanged.

## Navigation and shared learning checks

From the repository root:

```bash
python3 verification/check_repository.py --output /tmp/batch-threshold-repository-checks.json
```

The [repository checker](check_repository.py) uses only Python's standard library. It checks relative file links and heading fragments, the single canonical M01–M30 map and its two phases, backward milestone dependencies, the selected Watrous (2018) source identity, explicit private-coaching boundary patterns, and the saved scientific report's hashes against the current science inputs. A stale report fails this check; rerun the scientific suite after changing those inputs.

These structural checks support navigation and reproducibility. Scientific meaning, educational coherence, and the actual hosted mathematical presentation require their separate reviews; a structural pass does not establish them.

## What is checked

| Check | Finite scope | Independent construction |
|---|---|---|
| GHZ coverage count | 1–12 unresolved sites | Enumerate binary symplectic stabilizer generator products, then compare full-support counts and coverage inequalities |
| GHZ operator and decoder signs | 1–6 unresolved sites; covered and uncovered words; signed local Clifford frames | Build the GHZ circuit as raw matrices, compare measured Pauli eigenvalues and Born probabilities with the decoder, including $`Y`$ on the first site and even all-$`Z`$ words |
| Exact marker-averaged coverage | 240 rational parameter cases, including negative third-base cases | Sum the binomial mixture with `Fraction` arithmetic and compare the closed form and half-$`\beta^n`$ bound |
| Odd tensor Pauli representation | Odd copy counts 1, 3 and 5 | Construct tensor Pauli matrices and an independent parity/complement basis; compare each logical generator and its $`Y`$ sign |
| Odd-subset response and signed known-site reduction | Listed small block effects and an explicit signed reduction | Evaluate raw matrix expectations, including a reduction with eigenvalues $`-1/2,+1/2`$, rather than assuming it is positive |
| Finite-contrast joint-POVM bound | 10 block configurations, two nonzero contrasts each, Hilbert dimension at most 64 | Normalize random general joint POVMs independently, evaluate tensor-density Born laws, enumerate unresolved axes, and compare KL, chi-squared divergence and the analytical block bound |

The observed suite has **508 finite cases in six groups**. The numerical tolerance is $`3\times10^{-11}`$. Binary enumeration and rational identities are exact within their finite ranges; floating-point matrix tests are diagnostics. The maximum GHZ operator residual in the saved run is reported in its test group.

## Limits

The suite does not enumerate all collective POVMs, establish the arbitrary-size or asymptotic theorem by testing, certify literature priority, or constitute independent expert review. Random matrices use a reproducible seed and exercise only the recorded finite cases. No hardware experiment, noisy-device guarantee or end-to-end learning-runtime benchmark is presented. Decoded Bernoulli laws are checked directly using matrix Born probabilities; no experiment-level Monte Carlo claim is made.

The [two-qubit example](../science/worked_example.md) gives a complete exact source/measurement/filtering calculation. It illustrates the protocol without supplying the large-size theorem or an optimal finite sample count.
