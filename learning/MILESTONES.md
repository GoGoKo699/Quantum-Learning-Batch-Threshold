# The 30-milestone understanding map

[Repository](../README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific overview](../science/README.md) · [Worked experiment](../science/worked_example.md)

The story begins with a correlation whose measurement instructions are partly erased. It ends with a precise answer to how many specimens a preplanned experiment must pool when previous experiments cannot supply feedback. The batch cap counts source copies participating in an experiment; it is not a lower bound on quantum memory width, holding time or inter-copy entanglement.

The map has **11 background/preliminary milestones and 19 narrative/innovation milestones**. The first phase builds the local objects and joins them into the full statistical experiment. The second has seven milestones for the converse, seven for an attaining experiment, and five for the combined resource law and its meaning. This allocation reflects the need to understand both sides of a matched threshold, rather than treating an achievable protocol as a universal lower bound.

The one educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). Source abbreviations below refer to its chapters: **W1**, Mathematical preliminaries; **W2**, Basic notions of quantum information; **W3**, Similarity and distance among states and channels; **W5**, Quantum entropy and source coding. The [bridge](WATROUS_BRIDGE.md) identifies the relevant sections and translates the book's base-two entropy convention to the project's natural logarithms. The anchor supplies foundations, including probability and concentration. The project supplies the marked source, the odd-subset argument, GHZ coverage, its finite sampling calculation and the batch frontier. The map is an understanding route, not a requirement to read those chapters in full, and it does not attempt to cover every technical detail.

The asymptotic laws hold as the payload size grows with reveal probability, accuracy and confidence fixed. The converse uses a fixed interior sign pair and an accuracy smaller than its contrast. The two signs, the independent erasure law and the ban on marker feedback between blocks are part of the result.

## Phase I — Background and preliminaries, local to global

### M01 — One qubit, three possible measurement axes

**Central question.** What changes when a qubit is measured along $`X`$, $`Y`$ or $`Z`$?

**Understanding target.** Explain a Pauli axis as a two-outcome measurement with signs $`\pm1`$, and distinguish a known measurement basis from an unknown state.

**Dependencies and story role.** Entry point; supplies the local physical object used at every payload site.

**Conceptual connection.** The hidden word will select one of these axes at each site; it does not select the outcome itself.

**Sources.** Watrous W1–W2; [source specimens](../science/model.md#source-specimens); [two-qubit experiment](../science/worked_example.md).

### M02 — A global correlation with uninformative local parts

**Central question.** How can a payload carry information that no proper subset of its qubits reveals?

**Understanding target.** Explain the full Pauli word $`P_a`$, the contrast $`c`$, and why proper payload marginals are maximally mixed for $`n\ge2`$.

**Dependencies and story role.** Uses M01; joins local axes into the source's global observable.

**Conceptual connection.** A missing local measurement instruction can spoil access to a genuine many-site correlation without making the correlation itself exponentially small.

**Sources.** Watrous W2, tensor products and reduced states; [source specimens](../science/model.md#source-specimens); [simple input and measurement difficulty](../science/model.md#why-the-input-is-simple-but-the-measurement-problem-is-not).

### M03 — A sign to learn, rather than a magnitude alone

**Central question.** Why does distinguishing positive from negative contrast matter?

**Understanding target.** Relate a matched Pauli parity to a coin of mean $`c`$, and distinguish signed estimation from estimating $`|c|`$ or $`c^2`$.

**Dependencies and story role.** Uses M01–M02; identifies the observable output and the load-bearing signed task.

**Conceptual connection.** The converse compares fixed interior alternatives $`\pm c_0`$; magnitude information alone cannot settle their sign.

**Sources.** Watrous W2–W3, measurement statistics and distinguishability; [learning task](../science/model.md#the-learning-task); [worked payload probabilities](../science/worked_example.md).

### M04 — A classical instruction that may be erased

**Central question.** What exactly does one marker reveal, and what does an erasure leave unknown?

**Understanding target.** Describe the orthogonal alphabet $`\{\bot,X,Y,Z\}`$, fixed reveal probability $`q`$, and independence across sites and specimens conditional on the fixed word.

**Dependencies and story role.** Uses M01–M03; adds the local side information that makes feedback useful.

**Conceptual connection.** Reading a marker is ordinary classical readout. It supplies a measurement instruction rather than a copy of the payload's random outcome.

**Sources.** Watrous W2, classical registers as diagonal quantum states; [source specimens](../science/model.md#source-specimens).

### M05 — What an unrestricted measurement permits

**Central question.** What does allowing an arbitrary joint POVM actually give a learner?

**Understanding target.** Explain positive measurement effects, outcome probabilities, ancillas and internal conditional operations; distinguish a global POVM from a product Pauli setting.

**Dependencies and story role.** Uses M01–M04; establishes the strong measurement benchmark against which the converse must work.

**Conceptual connection.** The lower bound must limit every allowed block measurement, including one that reads markers before choosing how to inspect payloads.

**Sources.** Watrous W2, measurements and channels; [predetermined block experiments](../science/model.md#predetermined-block-experiments); [reading markers first](../science/collective_converse.md#2-reading-a-blocks-markers-loses-no-generality).

### M06 — Internal control and feedback between experiments

**Central question.** Which use of earlier information changes the measurement model?

**Understanding target.** Distinguish a block's use of its own markers, forbidden use of a previous block's markers, and unrestricted final classical decoding.

**Dependencies and story role.** Uses M04–M05; turns individual measurement operations into a control architecture.

**Conceptual connection.** The experiment may pool at most $`b`$ specimens internally. The cap is cardinality, not minimum simultaneous quantum storage or elapsed coherence time.

**Sources.** Watrous W2, composition of operations; [predetermined blocks](../science/model.md#predetermined-block-experiments); [block cardinality](../science/resources.md#block-cardinality-is-not-simultaneous-coherent-width).

### M07 — Accuracy, confidence and the full specimen budget

**Central question.** What must an estimator guarantee, and which specimens count toward its cost?

**Understanding target.** Explain uniform absolute error, failure probability and a hard maximum budget; include discarded payloads, erasures and rejected records in the charge.

**Dependencies and story role.** Uses M03–M06; specifies the score by which experiments will be compared.

**Conceptual connection.** A useful parity record is only part of an experiment's input cost. Conditional success cannot silently remove unsuccessful specimens from the denominator.

**Sources.** Watrous W1–W2, probabilities and measured data; [learning task](../science/model.md#the-learning-task); [charged specimens](../science/resources.md#supplied-information-and-charged-specimens).

### M08 — From distinguishable records to a statistical lower bound

**Central question.** How can two close outcome distributions rule out accurate estimation?

**Understanding target.** Connect binary testing error, total variation, relative entropy and the $`\chi^2`$ comparison used here; distinguish a finite testing guarantee from local sensitivity.

**Dependencies and story role.** Uses M05–M07; supplies the statistical bridge needed by the universal converse.

**Conceptual connection.** The project bounds the records of two actual nonzero contrasts, rather than inferring fixed-error difficulty from Fisher information at zero.

**Sources.** Watrous W3 and W5, distinguishability and relative entropy; [finite sign comparison](../science/collective_converse.md#4-one-block-at-finite-contrast); [minimax error](../science/collective_converse.md#6-from-divergence-to-minimax-error).

### M09 — An information budget over many Pauli directions

**Central question.** Why can one normalized measurement effect not be highly informative about every unknown Pauli word?

**Understanding target.** Use Pauli orthogonality and a purity bound to explain a sum-of-squared-expectations budget, without assuming that the effect is a product state.

**Dependencies and story role.** Uses M01, M02 and M05; introduces the quantum ingredient behind the lower bound.

**Conceptual connection.** Averaging many incompatible candidate directions differs from measuring one known observable repeatedly.

**Sources.** Watrous W1–W2, operator inner products and density operators; [odd-subset lemma](../science/collective_converse.md#3-odd-tensor-powers-retain-a-pauli-algebra).

### M10 — Pooling independent erased instructions

**Central question.** How does a block's size determine its remaining number of unknown axes?

**Understanding target.** Explain $`t_r=(1-q)^r`$, the binomial unresolved count $`K`$, and why averaging $`(2/3)^K`$ produces $`\beta_r^n`$.

**Dependencies and story role.** Uses M04 and M09; joins the local marker law to a system-wide statistical factor.

**Conceptual connection.** The same binomial generating function will connect the collective information budget and an attaining measurement's coverage.

**Sources.** Watrous W1, probability foundations; [batch parameter](../science/model.md#the-batch-parameter); [marker-conditioned count](../science/collective_converse.md#2-reading-a-blocks-markers-loses-no-generality).

### M11 — Assemble the full learning experiment

**Central question.** What precise comparison does the project ask us to understand?

**Understanding target.** State the source, unknowns, output, fixed-parameter limit, allowed controls and specimen charge together; explain why the separable source is easy to generate but its measurement instructions matter.

**Dependencies and story role.** Synthesizes M01–M10 and completes the background phase.

**Conceptual connection.** The forthcoming upper and lower bounds must refer to the same signed task and the same absence of feedback between blocks.

**Sources.** Watrous W1–W3 as the common formal framework; [complete model](../science/model.md); [resources](../science/resources.md); [scientific overview](../science/README.md).

## Phase II — Narrative and innovation, local to global

### M12 — Reduce a block to its unresolved axes

**Central question.** Why may the converse read all orthogonal markers before analyzing the payload measurement?

**Understanding target.** Explain the block-diagonal reduction and the remaining independent uniform axes under the proof's hidden-word prior.

**Dependencies and story role.** Uses M04–M06, M10–M11; begins the converse with the exact information supplied inside one block.

**Conceptual connection.** Strong marker-conditioned measurements are included, not excluded to make the lower bound easier.

**Sources.** Watrous W2, measurements on classical registers; [marker reduction](../science/collective_converse.md#2-reading-a-blocks-markers-loses-no-generality).

### M13 — The sign difference selects odd subsets

**Central question.** Which terms survive when the two block states at $`+c_0`$ and $`-c_0`$ are subtracted?

**Understanding target.** Explain why only odd subsets of payload copies contribute, and why even-copy magnitude information does not resolve the fixed sign pair.

**Dependencies and story role.** Uses M02–M03, M08 and M12; identifies the algebra the converse must control.

**Conceptual connection.** Signed estimation makes odd tensor powers, rather than arbitrary tensor powers, the decisive measurement directions.

**Sources.** Watrous W1–W2, tensor products and linear measurement probabilities; [odd tensor powers](../science/collective_converse.md#3-odd-tensor-powers-retain-a-pauli-algebra); [finite divergence](../science/collective_converse.md#4-one-block-at-finite-contrast).

### M14 — Many physical copies retain one logical Pauli algebra

**Central question.** Why do odd tensor powers still obey a qubit's incompatibility relations?

**Understanding target.** Explain pairwise anticommutation, the possible sign convention for the logical $`Y`$, and the irrelevant multiplicity space.

**Dependencies and story role.** Uses M01, M09 and M13; supplies the central algebraic reduction for arbitrary collective measurements.

**Conceptual connection.** More copies do not automatically make the sign-bearing alternatives jointly accessible. Their odd-subset representation still has a Pauli information budget.

**Sources.** Watrous W1–W2, operator representations and tensor products; [logical-Pauli proof](../science/collective_converse.md#3-odd-tensor-powers-retain-a-pauli-algebra).

### M15 — Preserve the budget after contracting known directions

**Central question.** Can the known axes, multiplicities or an entangled measurement effect defeat the unresolved-axis bound?

**Understanding target.** Explain why the contracted logical operator has trace norm at most one, even when it need not be a density operator, and how its squared Pauli coefficients remain bounded.

**Dependencies and story role.** Uses M09, M12 and M14; completes the lemma's unrestricted-measurement meaning.

**Conceptual connection.** Trace-norm duality prevents a positive-effect proof from silently assuming away correlations with the known part of a block.

**Sources.** Watrous W1 and W3, operator norms and duality; [odd-subset lemma and contraction](../science/collective_converse.md#3-odd-tensor-powers-retain-a-pauli-algebra).

### M16 — Obtain a finite nonzero-contrast block bound

**Central question.** How does the odd-subset budget limit the entire outcome distribution at fixed $`c_0`$?

**Understanding target.** Connect the full-rank denominator, the weighted sum of odd subsets, $`A_r(c_0)`$, and the marker average $`\beta_r^n`$.

**Dependencies and story role.** Uses M08, M10 and M13–M15; converts the algebraic lemma into a statistical bound for one arbitrary block.

**Conceptual connection.** Keeping the contrast-dependent prefactor explicit is what permits a valid growing-batch asymptotic argument later.

**Sources.** Watrous W3 and W5, distinguishability and entropy foundations; [fixed-sign divergence budget](../science/collective_converse.md#4-one-block-at-finite-contrast).

### M17 — One hidden word connects all records

**Central question.** Why cannot the proof multiply block laws after averaging away the unknown word?

**Understanding target.** Distinguish conditional independence from unconditional correlation; explain final revelation of the word as a proof device that cannot retroactively choose measurements.

**Dependencies and story role.** Uses M06, M08 and M16; extends the single-block argument to the actual experiment.

**Conceptual connection.** The decoder receives all final classical information, while only premeasurement control is restricted.

**Sources.** Watrous W2 and W5, classical registers and conditional information; [shared hidden word](../science/collective_converse.md#5-one-hidden-word-across-every-block).

### M18 — A universal specimen converse

**Central question.** How does a block information bound become a minimax lower bound under one specimen budget?

**Understanding target.** Explain unequal preplanned block sizes, the monotonic per-specimen budget, independent shared randomness and the final testing reduction.

**Dependencies and story role.** Uses M07–M08 and M16–M17; synthesizes the converse before turning to an attaining experiment.

**Conceptual connection.** The theorem excludes every allowed joint block POVM and final decoder, not merely a particular unsuccessful measurement design.

**Sources.** Watrous W3 and W5; [finite theorem](../science/collective_converse.md#1-finite-theorem); [budget aggregation](../science/collective_converse.md#5-one-hidden-word-across-every-block); [minimax error](../science/collective_converse.md#6-from-divergence-to-minimax-error).

### M19 — Use a block's markers and one payload

**Central question.** How can an attaining experiment use internal marker information without using feedback from other blocks?

**Understanding target.** Describe reading early markers, discarding their payloads and measuring the final payload under the same preplanned block rule; charge every specimen.

**Dependencies and story role.** Uses M04–M07 and M10–M11; begins the constructive side with its actual implementation.

**Conceptual connection.** A block cap can permit internal classical control without requiring a quantum carrier between arrivals or entanglement between copies.

**Sources.** Watrous W2, measurement composition; [one-payload experiment](../science/attaining_measurements.md#read-the-blocks-markers-then-measure-one-payload); [cardinality and width](../science/resources.md#block-cardinality-is-not-simultaneous-coherent-width).

### M20 — A GHZ basis covers many full-support words

**Central question.** Which unknown Pauli observables can one GHZ stabilizer-basis record determine?

**Understanding target.** Explain the commuting generators, the full-support $`X/Y`$ words, and the extra all-$`Z`$ word at even unresolved count.

**Dependencies and story role.** Uses M01–M02, M05 and M19; constructs a measurement with many useful directions on one payload.

**Conceptual connection.** Standard stabilizer algebra supplies coverage; the source itself remains separable.

**Sources.** Watrous W1–W2 for operator and measurement foundations; [GHZ coverage derivation supplied here](../science/attaining_measurements.md#the-ghz-coverage-calculation); [two-qubit Bell example](../science/worked_example.md).

### M21 — Random frames distribute that coverage fairly

**Central question.** How does a fixed unknown word obtain a uniform chance of being covered?

**Understanding target.** Explain independent local Clifford randomization, the coverage probability $`h_k`$, its special $`k=0`$ case and its bounds by constant multiples of $`(2/3)^k`$.

**Dependencies and story role.** Uses M09–M10 and M20; turns a particular stabilizer basis into a uniform measurement design.

**Conceptual connection.** This is the attaining counterpart of the converse's unresolved-axis information budget.

**Sources.** Watrous W1–W2, basis changes and measurement probabilities; [randomized GHZ coverage](../science/attaining_measurements.md#the-ghz-coverage-calculation).

### M22 — Decode the correct signed parity offline

**Central question.** How can a recorded basis become useful only after later markers reveal the word?

**Understanding target.** Explain final coverage filtering, stabilizer and Clifford phase signs, and why every accepted record has the same mean $`c`$.

**Dependencies and story role.** Uses M03, M06 and M20–M21; connects a measurement record to the actual prediction task.

**Conceptual connection.** Learning the word at final decoding is permitted; using it to remeasure an already consumed payload is not.

**Sources.** Watrous W2–W3, classical measurement records and distinguishability; [offline filtering and signs](../science/attaining_measurements.md#offline-filtering-and-the-exact-acceptance-probability); [Bell sign example](../science/worked_example.md).

### M23 — The coverage factor matches the converse

**Central question.** What is the useful-record probability after averaging the erasure pattern?

**Understanding target.** Relate $`p_r=\mathbb E[h_K]`$ to its exact binomial expression and the bounds $`\beta_r^n/2\le p_r\le\beta_r^n`$.

**Dependencies and story role.** Uses M10, M16 and M21–M22; joins the constructive mechanism to the converse's governing factor.

**Conceptual connection.** Matching an exponential base requires more than an upper protocol that merely becomes exponential.

**Sources.** Watrous W1, probability foundations; [exact acceptance calculation](../science/attaining_measurements.md#offline-filtering-and-the-exact-acceptance-probability); [finite pair of bounds](../science/phase_boundary.md#one-finite-pair-of-bounds).

### M24 — Pay for every failure event

**Central question.** Why does accepted-record accuracy not by itself prove a finite specimen guarantee?

**Understanding target.** Separate failure to recover the word, too few accepted records and inaccurate averaging; explain the ideal decoder comparison without assuming independence after global marker success.

**Dependencies and story role.** Uses M07–M08, M17 and M22–M23; completes the constructive statistical guarantee.

**Conceptual connection.** The deterministic budget includes failed coverage and unused payloads; selection does not create free samples.

**Sources.** Watrous W1–W3 for probability and measurement foundations; [finite sample guarantee supplied here](../science/attaining_measurements.md#a-finite-sample-guarantee); [complete specimen cost](../science/resources.md#complete-finite-specimen-cost).

### M25 — Separate a sharper base from the feasibility threshold

**Central question.** Which conclusions require GHZ measurements, and which already follow from local product measurements and feedback?

**Understanding target.** Compare randomized GHZ coverage, random product-axis guesses and the one-feedback-round protocol; distinguish intra-payload entangling gates from inter-copy entanglement and from the source's separability.

**Dependencies and story role.** Uses M06, M19 and M23–M24; synthesizes the constructive implementations and their resource meanings.

**Conceptual connection.** GHZ improves the fixed-block exponential base. Neither the polynomial boundary nor the explicit upper requires entanglement between different source specimens.

**Sources.** Watrous W2 for measurements and circuit composition; [product alternative](../science/attaining_measurements.md#a-product-measurement-alternative); [adaptive local comparison](../science/attaining_measurements.md#one-feedback-round-with-local-single-copy-measurements); [resource table](../science/resources.md#operations-in-the-attaining-block-protocol).

### M26 — Fixed batches have a matching exponential base

**Central question.** What does the combined result establish when the batch cap stays fixed?

**Understanding target.** Explain $`\Theta_{b,q,c_0}(\beta_b^{-n})`$, which parameters are held fixed, and what remains unspecified by that notation.

**Dependencies and story role.** Uses M18 and M23–M25; begins the global synthesis by comparing upper and lower bounds in their simplest common regime.

**Conceptual connection.** Matching an exponential rate is distinct from identifying exact finite constants, processing time or a hardware crossover.

**Sources.** Watrous W3 for the testing interpretation; [fixed-block law](../science/phase_boundary.md#fixed-blocks-the-exponential-base-matches); [resources](../science/resources.md).

### M27 — Prove polynomial feasibility without filling a large cap

**Central question.** Why is $`n(1-q)^b=O(\log n)`$ enough for polynomial specimen cost?

**Understanding target.** Explain the inverse-coverage exponent, a working block no larger than order $`\log n`$, and why an allowed cap need not be used in full.

**Dependencies and story role.** Uses M10, M23–M24 and M26; derives the sufficient half of the growing-batch criterion.

**Conceptual connection.** An asymptotic resource allowance should not force the attaining implementation to acquire unnecessary inputs.

**Sources.** Watrous W1, logarithms and probability foundations; [large-cap truncation](../science/attaining_measurements.md#a-large-cap-need-not-increase-the-cost); [growing-block sufficiency](../science/phase_boundary.md#growing-blocks-an-if-and-only-if-criterion).

### M28 — Prove necessity along every cap sequence

**Central question.** Why can no uniform polynomial budget work when residual instruction uncertainty exceeds logarithmic order?

**Understanding target.** Track the $`b`$-dependent contrast prefactor, the difficult subsequence and the uniform meaning of a polynomial budget; explain the $`\log\log n`$ correction to the boundary.

**Dependencies and story role.** Uses M16–M18 and M27; completes the if-and-only-if result without assuming that cap sequences have a limiting exponent.

**Conceptual connection.** A fixed-batch bound cannot simply be relabelled as a growing-batch theorem; its prefactor must remain controlled in the relevant regime.

**Sources.** Watrous W3 and W5 as testing foundations; [converse frontier](../science/collective_converse.md#7-consequences-for-the-batch-frontier); [uniform criterion and boundary](../science/phase_boundary.md#growing-blocks-an-if-and-only-if-criterion).

### M29 — Read the three regimes as one resource law

**Central question.** How do fixed, below-threshold logarithmic and near-threshold batches fit the same mechanism?

**Understanding target.** Explain exponential, stretched-exponential and polynomial specimen costs from the residual unknown-axis count; retain fixed $`q`$, fixed signed contrast and integer-rounding qualifications.

**Dependencies and story role.** Uses M26–M28; turns the formal criterion into an intelligible comparative picture.

**Conceptual connection.** The same factor links a small worked experiment to large-system regimes, while finite examples remain illustrations rather than proofs of an asymptotic law.

**Sources.** Watrous W1–W3 as the common framework; [three regimes](../science/phase_boundary.md#three-regimes); [worked experiment](../science/worked_example.md); [verification extent](../verification/README.md).

### M30 — State the discovery and its boundary together

**Central question.** After crediting earlier work and all restrictions, what has been established?

**Understanding target.** State the matched fixed-batch base and growing-batch polynomial criterion, explain the feedback comparison, and recover the erasure formula from the minimax omission error. State the signed domain and which operations may use the final marker record.

**Dependencies and story role.** Synthesizes M11–M29 and closes the narrative phase with the whole scientific account.

**Conceptual connection.** The inherited marker–signal separation and Pauli information budget support a new finite-sign batch frontier; marker exclusion gives the same mechanism for erasure and noisy markers, with no feedback between blocks.

**Sources.** Watrous W1–W3 and W5 as the one foundational anchor; [scientific overview](../science/README.md); [phase boundary](../science/phase_boundary.md); [noisy-marker theorem](../science/noisy-markers.md); [resource interpretation](../science/resources.md); [precise prior-work comparison](../references/RELATED_WORK.md).
