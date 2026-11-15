# Quantum Learning Batch Threshold

**How large must a joint measurement batch be to replace feedback during quantum learning?** For a source with a hidden Pauli signal and independently erased classical measurement instructions, this project determines when preplanned block measurements have polynomial specimen cost.

Let $`n`$ be the payload qubit count, $`q\in(0,1)`$ the fixed probability that a local marker reveals its axis, and $`b`$ the maximum specimens in a preplanned joint experiment. For fixed accuracy and confidence in the signed-contrast task,

```math
\text{polynomial specimen cost}
\quad\Longleftrightarrow\quad
n(1-q)^b=O(\log n).
```

The nonadaptive learner may use **any collective POVM inside each block**, including control based on that block's own markers. No earlier block outcome controls another block, and no coherent carrier connects the blocks. All records may be decoded jointly at the end.

| Regime | Supported specimen law |
|---|---|
| Every fixed batch cap $`b`$ | Matching exponential order $`\Theta_{b,q,c_0}(\beta_b^{-n})`$, where $`\beta_b=1-(1-q)^b/3`$ |
| Growing cap | Polynomial exactly when the residual instructions $`n(1-q)^b`$ are at most logarithmic |
| One classical feedback round | Local single-copy measurements use $`O_q(\log n)`$ specimens at fixed accuracy |

The source states are fully separable. The attaining block protocol reads its own markers, measures one payload in a randomized GHZ stabilizer basis, and filters classical records after the full marker transcript identifies the hidden word. It matches the converse's exponential base without entangling different payload specimens. Every unused payload, erasure and rejected record is charged.

The batch cap counts inputs in a preplanned experiment. It does not establish a minimum coherent width or holding time: the implementation can discard early payloads and measure the final one after collecting the block's markers. The learning domain includes both positive and negative contrasts; the sign converse does not assert the same boundary for a positive-only task.

## Read the science

Start with the [scientific overview](science/README.md).

| Question | Authoritative account |
|---|---|
| What is supplied, what must be learned, and which feedback is allowed? | [Model](science/model.md) |
| Why can arbitrary collective block measurements not avoid the lower bound? | [Finite converse](science/collective_converse.md) |
| How do GHZ stabilizers attain the exponential coverage factor? | [Attaining measurements](science/attaining_measurements.md) |
| Where is the logarithmic batch threshold, including its transition scale? | [Phase boundary](science/phase_boundary.md) |
| How does one complete two-qubit experiment work? | [Worked example](science/worked_example.md) |
| What do preparation, gates, records and final decoding cost? | [Resources](science/resources.md) |
| Which ingredients and earlier separations are inherited? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib) |

Goldar and coauthors' [marked single-copy separation](https://arxiv.org/abs/2610.38922v1) is the immediate antecedent. Chen, Gong and Zhang's [two-copy separation](https://arxiv.org/abs/2412.19022v1) supplies closely related signed-Pauli information bounds. This project's addition is the growing-batch finite-contrast frontier and matching coverage construction. It does not establish the erasure-marker law for a different noisy-marker channel.

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

The source is IID with one fixed hidden word, independent orthogonal erasure markers and fixed known reveal probability. Receiver operations are ideal. The result charges specimens and gives an explicit attaining implementation under all-to-all connectivity. General marker channels, optimal finite constants, the precise polynomial degree at the transition, architecture-dependent depth, source drift and receiver noise require their own analysis. No end-to-end training-runtime advantage is asserted.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
