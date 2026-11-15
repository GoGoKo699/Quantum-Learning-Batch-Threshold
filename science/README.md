# Scientific account

A quantum specimen can contain a simple scalar correlation whose useful measurement basis is initially unknown. Classical markers gradually reveal that basis. Feedback lets a learner use the early instructions to choose later measurements. Without feedback between independent experiments, a larger joint measurement block is one way to collect instructions before choosing its payload measurement.

This project determines the batch threshold for a marked-Pauli source with independent erasures. For fixed marker reveal probability and fixed signed-contrast accuracy, arbitrary preplanned blocks of at most $`b`$ specimens admit polynomial specimen cost exactly when

```math
n(1-q)^b=O(\log n).
```

For every fixed block size, the exponential base is matched:

```math
N_{\min}
=\Theta_{b,q,c_0}\left[
\left(1-\frac{(1-q)^b}{3}\right)^{-n}
\right].
```

The converse permits arbitrary collective block POVMs. The attaining measurement uses each block's markers and a randomized GHZ stabilizer basis on one payload; it does not entangle different payload specimens. Adaptive local measurements with one feedback round need only $`O(\log n)`$ specimens at fixed accuracy.

## One connected argument

1. [Model](model.md): source, symmetric signed-contrast task, allowed controls and charged specimens.
2. [Collective converse](collective_converse.md): odd tensor powers retain a logical Pauli algebra; conditioning on erased markers and summing KL across preplanned blocks gives a finite fixed-contrast minimax bound.
3. [Attaining measurements](attaining_measurements.md): GHZ stabilizer coverage, unconditional filtering, exact coverage probability and finite sample budget; the adaptive local comparison is included.
4. [Phase boundary](phase_boundary.md): matching fixed-block exponential base and the growing-cap polynomial-feasibility criterion.
5. [Resources and interpretation](resources.md): specimen count, implementation and classical costs, control restrictions and what the batch parameter means.

A [complete two-qubit example](worked_example.md) shows the source probabilities, three marker cases, Bell-basis signs and final filtering.

The input states are fully separable. Known-axis measurement would be a Bernoulli-mean problem, and source preparation takes linear work for the source holding the hidden word. The obstruction concerns allocating measurement information before that word is known; it does not come from a hard-to-prepare input or a small trace-distance signal.

## Attribution and evidence

The marked-Pauli adaptivity mechanism and earlier one-copy and two-copy separations are inherited. The addition is the growing-batch finite-contrast frontier and its matching coverage construction. [Related work](../references/RELATED_WORK.md) compares the closest statements and [the bibliography](../references/references.bib) gives their versions.

[Verification](../verification/README.md) separates exact stabilizer and probability identities, finite matrix checks and protocol simulations from the general analytical proof. The result is an information-theoretic law for the specified source and control structure, not an implementation or priority certificate.
