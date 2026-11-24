# Learning the batch threshold

The single educational anchor is **Watrous, *The Theory of Quantum Information* (2018)**. Its [author page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the source. Selected sections cover states, measurements, norms, probability, and distinguishability. The bridge translates their notation and supplies the local Pauli/GHZ calculations.

The common starting route is:

1. [Watrous bridge](WATROUS_BRIDGE.md): the source-and-marker story, precise textbook sections, and additional proof steps.
2. [Complete two-qubit example](../science/worked_example.md): preparation probabilities, Bell-basis signs, filtering, and charged failures.
3. [Thirty milestones](MILESTONES.md): the project's understanding targets and dependencies.
4. [Scientific account](../science/README.md): the full model, finite proofs, batch boundary, and resources.

Choose the route that matches what you want to understand.

| Reading goal | Route through the material | Scientific destination |
|---|---|---|
| Understand the experiment | Bridge's source story → two-qubit example → background milestones | [Model](../science/model.md) and [attaining measurements](../science/attaining_measurements.md) |
| Understand the complete result | Full bridge → example → the whole milestone map | [Overview](../science/README.md), [phase boundary](../science/phase_boundary.md), and [resources](../science/resources.md) |
| Reconstruct the proof | Bridge's notation and proof connections → example → milestone dependencies | [Finite converse](../science/collective_converse.md) followed by [achievability](../science/attaining_measurements.md) |

A batch can choose its measurement using its own markers. The final decoder can use the full record. Keep these two times separate while reading the [erasure example](../science/worked_example.md) and then the [noisy-marker proof](../science/noisy-markers.md). In the latter, compare the probability of eliminating the true axis with the separate cost of identifying the entire word. The batch threshold measures how much information must arrive before measurement.

The [verification guide](../verification/README.md) separates finite calculations from the analytical proof. [Research references](../references/RELATED_WORK.md) provide attribution and comparisons, while Watrous remains the sole educational anchor.

