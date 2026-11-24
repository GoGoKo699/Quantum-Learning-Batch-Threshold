# Quantum Learning Batch Threshold

**How many specimens must a preplanned experiment pool to replace feedback during quantum learning?** A source encodes a signed scalar in a hidden Pauli string. Each site's classical markers are noisy instructions about which Pauli axis to measure. The learner may read a block's own markers before measuring its payload, and an arbitrary joint measurement is allowed inside each block. Measurements in different blocks are fixed independently of earlier outcomes. The decoder can combine all classical records at the end.

Let n be the number of payload qubits and b the block cap. At each site, let e_b be the smallest worst-case probability of mistakenly ruling out the true axis after reading b markers. For three distinct marker laws and fixed accuracy and confidence,

```math
\text{polynomial specimen cost}
\quad\Longleftrightarrow\quad
ne_b=O(\log n).
```

| Marker model | What the batch law gives |
|---|---|
| Finite classical markers | At fixed b with positive omission error, the optimal specimen count has matching exponential order with base $`1/(1-e_b)`$ per payload qubit. |
| Goldar et al.'s noisy-qubit markers | For fixed strength u, the logarithmic transition has coefficient $`1/C_u`$, where $`C_u=-\tfrac12\log(1-u^2)`$. The lower edge for polynomial cost is shifted by $`-\tfrac32\log\log n`$ in $`C_u b`$. The single-copy base is $`(3-u)/2`$. |
| Erasure markers revealing the axis with probability q | The omission error is $`(1-q)^b/3`$, recovering the erasure threshold. |

An attaining experiment rules out one axis per site, then measures one payload in a randomized GHZ stabilizer basis adapted to the two remaining axes. Final decoding identifies the true word and extracts its signed parity from compatible records. The resource count includes every marker copy, discarded payload and rejected record. With one round of feedback, separate marker localization followed by local Pauli measurements uses logarithmically many specimens at fixed accuracy.

## Read the science

Start with the [scientific overview](science/README.md).

| Question | Authoritative account |
|---|---|
| What is supplied, what must be learned, and which feedback is allowed? | [Model](science/model.md) |
| How do noisy markers set the batch threshold? | [Marker exclusion theorem and Goldar example](science/noisy-markers.md) |
| Why can arbitrary collective block measurements not avoid the lower bound? | [Finite converse](science/collective_converse.md) |
| How do GHZ stabilizers attain the exponential coverage factor? | [Attaining measurements](science/attaining_measurements.md) |
| Where is the logarithmic batch threshold, including its transition scale? | [Phase boundary](science/phase_boundary.md) |
| How does one complete two-qubit experiment work? | [Worked example](science/worked_example.md) |
| What do preparation, gates, records and final decoding cost? | [Resources](science/resources.md) |
| Which ingredients and earlier separations are inherited? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib) |

Goldar and coauthors established the original [single-copy separation](https://arxiv.org/abs/2610.38922v1) and asked what changes when multicopy measurements are allowed. The [noisy-marker theorem](science/noisy-markers.md) gives the finite-accuracy batch boundary for their source. The [comparison with earlier work](references/RELATED_WORK.md) credits the inherited Pauli and classical hypothesis-exclusion tools.

## Learn the argument

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source-to-project bridge](learning/WATROUS_BRIDGE.md) identifies the needed sections, translates notation and logarithm conventions, and supplies the steps from textbook distinguishability to this batch theorem.

The [30-milestone map](learning/MILESTONES.md) has 11 background milestones and 19 narrative milestones. It connects single-qubit measurements and classical instructions to the collective converse, the GHZ construction and the complete resource boundary. Start with the [learning guide](learning/README.md); the [two-qubit experiment](science/worked_example.md) provides a concrete source, measurement and decoding example.

## Reproduce the finite checks

From this directory:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/check_science.py --output /tmp/batch-threshold-checks.json
```

The [verification guide](verification/README.md) identifies exact stabilizer and probability checks, finite matrix tests of arbitrary joint effects, classical record sampling and their limits. The analytical proofs establish the general theorem; numerical checks do not certify asymptotics or priority. [llms.txt](llms.txt) maps targeted scientific questions to their proof sources.

## Scope

The source supplies IID specimens with one fixed hidden word and independent markers in a known common basis. The result concerns signed contrast and ideal receiver operations. The batch cap counts specimens assigned to one experiment. Minimum coherent width, storage time, noncommuting markers, and hardware-dependent costs remain open.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
