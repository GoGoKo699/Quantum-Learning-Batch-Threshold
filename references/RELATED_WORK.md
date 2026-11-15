# Relation to earlier work

[Scientific model](../science/model.md) · [Collective converse](../science/collective_converse.md) · [Attaining measurements](../science/attaining_measurements.md) · [Phase boundary](../science/phase_boundary.md) · [Bibliography](references.bib)

## What this account adds

The question is how many source copies a preplanned experiment may pool before its payload measurement, when earlier experiments cannot supply feedback. The source has a fixed hidden Pauli word, an interior signed contrast, and independent erasure markers. Measurements may be arbitrary within a block of at most $`b`$ source copies; no outcome from another block may change that block's measurement.

For fixed marker reveal probability $`q\in(0,1)`$, define

```math
t_b=(1-q)^b,\qquad \beta_b=1-\frac{t_b}{3}.
```

The finite fixed-sign converse controls arbitrary global block POVMs through an odd-subset logical-Pauli reduction. A marker-conditioned GHZ-basis measurement attains the same $`\beta_b^n`$ coverage scale up to the stated prefactors. Together they establish that polynomial copy complexity is possible exactly when $`n(1-q)^b=O(\log n)`$. One classical feedback round instead permits local single-copy learning with logarithmically many source copies. These conclusions concern this source and measurement model; they do not establish a general training speedup or an optimal memory width.

## Marker information and single-copy feedback

Goldar, Qin, Zhu, Gong and Wakin, [arXiv:2610.38922v1](https://arxiv.org/abs/2610.38922v1), already construct a ternary hidden-Pauli marker–signal family with a scalar parameter, separable inputs, a one-round adaptive local protocol, and an exponential separation from nonadaptive arbitrary global **single-copy** measurements. Their Theorems V.1 and V.10 distinguish the local-asymptotic and finite-accuracy statements. Section II-B excludes measurements joining different copies; Section VIII-C explicitly raises the multicopy question.

That is the immediate scientific antecedent. This repository inherits the marker-directed incompatibility mechanism and changes the marker channel to exact classical erasures. Its addition is the growing-block finite-contrast converse, matching coverage construction, and resulting polynomial-learnability boundary. It does not prove that boundary for the original paper's noisy-qubit marker channel.

## Signed Pauli information and two-copy adaptation

Chen, Gong and Zhang, [arXiv:2412.19022v1](https://arxiv.org/abs/2412.19022v1), Theorem 1.2, prove that nonadaptive two-copy measurements require $`\Omega(2^{n/2})`$ copies for signed Pauli shadow tomography, whereas adaptive two-copy measurements suffice with $`O(n)`$ copies at constant accuracy. Their proof compares the hidden families $`(I+P_a)/2^n`$ and $`(I-P_a)/2^n`$ through a measurement-information budget.

Thus failure to recover Pauli signs with a fixed two-copy primitive is already known. Our result concerns a different scalar task with explicit marker information, a block cap growing with system size, and the point at which nonadaptive learning becomes polynomial. The Pauli information-allocation method is shared prior machinery.

Chen, Gong and Ye, [arXiv:2404.19105](https://arxiv.org/abs/2404.19105), provide the broader measurement/memory taxonomy and optimal Pauli-estimation tradeoffs. Their adaptive signed-observable protocols are also relevant context; a memory-width tradeoff is a different resource statement from the batch-size theorem proved here.

## Conjugate-state access is a different resource

King, Wan and McClean, [arXiv:2403.03469v1](https://arxiv.org/abs/2403.03469v1), published in [PRX Quantum 5, 040301 (2024)](https://doi.org/10.1103/PRXQuantum.5.040301), study displacement-amplitude learning. Theorem 1 gives a prime-dimension lower bound for measurements on $`K`$ ordinary copies under $`K\leq1/(12\varepsilon)`$. Theorems 2 and 5 instead exploit supplied conjugate states $`\rho^*`$, with Theorem 5 also resolving signs through a hypothesis-dependent procedure.

We assume neither conjugate-state preparation nor a controlled unknown-state oracle. Their result already shows that the type of quantum access can matter more than a small copy-count overhead. Our marker-conditioned block threshold neither supplies nor simulates that access.

## Existing multicopy hierarchies

Nöller, Tran, Gachechiladze and Kueng, [arXiv:2510.08070v2](https://arxiv.org/abs/2510.08070v2), establish an infinite hierarchy of multicopy learning tasks. The current full text's Result 4, Theorem 9 and Corollary 12 cover each local dimension $`d\geq2`$ not divisible by four: Weyl–Heisenberg amplitude estimation is hard for **adaptive** measurements on fewer than $`d`$ copies and efficient with $`d`$ copies, at fixed nontrivial accuracy. The local dimension and observable family change with the degree. These are amplitudes of linear expectation values; “degree” denotes the required number of simultaneous copies, not the polynomial degree of a state functional.

This is prior art for sharp multicopy thresholds. Our distinction is a fixed qubit signal with classical erasure markers, one signed parameter, and a feedback-versus-batch-size boundary: feedback already makes the single-copy experiment efficient. The hierarchy's adaptive lower bound therefore does not transfer to this marked source. The full v2 statement is broader than the prime/square-free summary still visible on some abstract pages.

## Foundations used without a novelty claim

Premeasurement versus postmeasurement side information and its connection to incompatibility are established themes; see Carmeli, Heinosaari and Toigo, [Physical Review A 98, 012126 (2018)](https://doi.org/10.1103/PhysRevA.98.012126). Gill and Massar's [information-budget analysis](https://doi.org/10.1103/PhysRevA.61.042312) is related background for the single-copy antecedent. Pauli orthogonality, purity bounds, trace-norm duality, classical relative-entropy bounds and binary testing reductions are standard tools.

The GHZ state, its stabilizers and its preparation/measurement circuits are also standard; see [Greenberger–Horne–Zeilinger (1989)](https://doi.org/10.1007/978-94-017-0849-4_10) and [Nielsen–Chuang](https://doi.org/10.1017/CBO9780511976667). The project-specific calculation is their use to attain marker-averaged signed-observable coverage. Entanglement in this measurement construction does not make the input source entangled, and the theorem gives no necessity claim for that particular attaining measurement.

The comparisons above identify inspected versions and controlling statements. They credit inherited mechanisms and delimit the supported difference; they are not an exhaustive priority claim.
