# Scientific account

A specimen carries a signed scalar in a Pauli correlation. Its classical markers give local clues about the hidden Pauli word. Feedback uses early clues to choose later settings. A preplanned batch can use only its own markers for that decision.

For known finite classical marker laws, let e_b be the minimax error of ruling out one local axis after b observations. The [noisy-marker theorem](noisy-markers.md) gives a finite converse against arbitrary collective block POVMs and a GHZ measurement achieving the same exponential base with one payload per signal block. Three distinct laws permit polynomial specimen cost exactly when ne_b is of logarithmic order or smaller. Goldar et al.'s commuting noisy qubit markers give an explicit threshold and a sharp fixed-accuracy single-copy base.

With erasure probability 1−q, the error of ruling out one axis is (1−q)^b/3. The [erasure account](phase_boundary.md) works through that case, including its detailed coverage calculation and feedback comparison.

## One connected argument

1. [Model](model.md): source, symmetric signed-contrast task, allowed controls and charged specimens.
2. [Collective converse](collective_converse.md): odd tensor powers retain a logical Pauli algebra; conditioning on erased markers and summing KL across preplanned blocks gives a finite fixed-contrast minimax bound.
3. [Attaining measurements](attaining_measurements.md): GHZ stabilizer coverage, unconditional filtering, exact coverage probability and finite sample budget; the adaptive local comparison is included.
4. [Phase boundary](phase_boundary.md): matching fixed-block exponential base and the growing-cap polynomial-feasibility criterion.
5. [Noisy markers](noisy-markers.md): the posterior-weighted converse, two-axis GHZ measurement, and the threshold for the original noisy-qubit source.
6. [Resources and interpretation](resources.md): specimen count, implementation and classical costs, control restrictions and what the batch parameter means.

A [complete two-qubit example](worked_example.md) shows the source probabilities, three marker cases, Bell-basis signs and final filtering.

The input states are fully separable. Known-axis measurement would be a Bernoulli-mean problem, and source preparation takes linear work for the source holding the hidden word. The obstruction concerns allocating measurement information before that word is known; it does not come from a hard-to-prepare input or a small trace-distance signal.

## Attribution and evidence

The marked-Pauli adaptivity mechanism and earlier one-copy and two-copy separations are inherited. The batch protocol, finite-contrast converse, and minimax marker-exclusion law determine the boundary for this source and control model. [Related work](../references/RELATED_WORK.md) compares the closest statements and [the bibliography](../references/references.bib) gives their versions.

[Verification](../verification/README.md) separates exact stabilizer and probability identities, finite matrix checks and protocol simulations from the general analytical proof. The result is an information-theoretic law for the specified source and control structure, not an implementation or priority certificate.
