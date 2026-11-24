# From Watrous to the batch threshold

The educational anchor is John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies this edition and its section structure; the [publisher record](https://doi.org/10.1017/9781316848142) identifies the published book.

The route into this project is a small experiment: a source produces a correlation, and classical markers gradually tell the learner which measurement reveals it. The question is how many source specimens an experiment must group together when earlier experiments cannot control later ones. Start with the story below, then follow the [complete two-qubit example](../science/worked_example.md). The book supplies mathematical tools as they become useful; reading it cover to cover is unnecessary.

## 1. The parts of the book that do work here

These are 2018 book section numbers. Pages refer to printed pagination.

| When it becomes useful | Watrous location | What it supplies here |
|---|---|---|
| Read vectors, matrices, and tensor products | Sections 1.1.1–1.1.2, beginning pp. 1 and 8 | The spaces and operators describing one payload and several independent payloads |
| Understand an operator's size | Section 1.1.3, beginning p. 24; operator norms on pp. 32–33 | Spectral decompositions, trace and Frobenius norms, and norm inequalities |
| Read marker probabilities and a mean-estimation guarantee | Section 1.2.2, beginning p. 47; Hoeffding's inequality, Theorem 1.16, p. 51 | Independent random variables and empirical means |
| Distinguish a readable flag from an unknown quantum state | Sections 2.1.1–2.1.2, beginning pp. 58 and 61 | Classical registers and quantum density operators |
| Remove registers while retaining the right operator | Section 2.1.3, beginning p. 67 | Partial traces; the signed extension in the converse is supplied locally |
| Allow the most general block measurement | Sections 2.3.1–2.3.2, beginning pp. 100 and 105 | POVMs and their outcome probabilities |
| Relate a statistical difference to a final decision | Section 3.1.1, beginning p. 125; Holevo–Helstrom theorem, Theorem 3.4 | Binary discrimination and trace distance |
| Convert a record-information bound into decision error | Sections 5.1.1–5.1.2, beginning pp. 250 and 253; Pinsker's inequality, Theorem 5.15, p. 263 | Classical relative entropy and distribution distance |

The Pauli matrices, Bell/GHZ decoder, erasure calculation, and batch-specific argument are supplied in this repository. They are not additional textbook prerequisites. Channel capacities, general quantum error correction, and the rest of the book are not required for this route.

## 2. What the source sends

A qubit has a two-dimensional state space. A density operator is a positive matrix with trace one; it specifies measurement probabilities. A tensor product joins distinct registers. Each specimen here contains $`n`$ payload qubits and $`n`$ readable classical markers.

The three Pauli matrices are

```math
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
```

Each has measurement outcomes $`+1`$ and $`-1`$. A hidden word $`a=(a_1,\ldots,a_n)`$ selects one matrix at each site. Their tensor product is $`P_a`$. The payload is

```math
\sigma_{a,c}=\frac{I+cP_a}{2^n}.
```

Knowing the axes turns the problem into estimating the average of a random sign, because

```math
\mathrm{Tr}(P_a\sigma_{a,c})=c.
```

At each site a marker reveals the correct axis with probability $`q`$, or displays an erasure with probability $`1-q`$. The marker is an instruction about a measurement, rather than an answer giving $`c`$. The hidden word stays fixed for every specimen. The independent erasures and payload outcomes vary.

Feedback lets the learner collect early instructions and use them to choose later measurements. The block benchmark allows that choice only from markers inside the current block. After every block has been measured, its classical records can be combined freely. The [model](../science/model.md) specifies this timing restriction.

## 3. A notation map

Watrous often uses matrix notation for vectors and adjoints. The project also uses standard ket and dagger notation.

| Book notation or convention | Project notation | Meaning |
|---|---|---|
| A vector $`u`$ and outer product $`uu^*`$ | Ket vector and pure-state projector, written below | A pure-state vector and its density operator |
| Adjoint $`A^*`$ | $`A^\dagger`$ | Conjugate transpose |
| A state in $`\mathrm D(\mathcal X)`$ | $`\sigma_{a,c}`$ for the payload | A positive trace-one operator |
| Measurement effect $`\mu(z)`$ | $`M_z`$ | The positive operator for recorded outcome $`z`$ |
| $`\langle\mu(z),\sigma\rangle`$ | $`\mathrm{Tr}(M_z\sigma)`$ | That outcome's probability |
| Trace norm $`\lVert A\rVert_1`$ | The same symbol | Sum of singular values; for Hermitian operators, sum of absolute eigenvalues |
| Base-two relative entropy $`D_{\mathrm{book}}(p\Vert r)`$ | Natural-log $`D_{\mathrm{KL}}(p\Vert r)`$ | $`D_{\mathrm{KL}}=(\ln2)D_{\mathrm{book}}`$ |

The vector and projector correspondence is

```math
u\longleftrightarrow|u\rangle,\qquad
uu^*\longleftrightarrow|u\rangle\langle u|.
```

The project's total variation distance is half the ordinary one-norm distance between probability vectors:

```math
\mathrm{TV}(p,r)=\frac12\sum_z|p(z)-r(z)|.
```

Watrous's classical Pinsker inequality therefore becomes, with natural logarithms,

```math
\mathrm{TV}(p,r)\leq
\sqrt{\frac12D_{\mathrm{KL}}(p\Vert r)}.
```

This conversion matters for finite constants. The proof's final information bound concerns classical records, so it does not require a quantum relative-entropy theorem.

## 4. Follow the two-qubit experiment

In the [worked example](../science/worked_example.md), $`n=2`$, $`q=1/2`$, and the hidden word is $`a=(Y,Z)`$. The source can prepare product eigenstates with local signs $`s,t\in\{-1,+1\}`$ according to

```math
\Pr(s,t)=\frac{1+cst}{4}.
```

For $`c=1/2`$, equal-sign pairs each have probability $`3/8`$ and unequal-sign pairs each have probability $`1/8`$. Either qubit alone looks uniformly random. Their correctly chosen product measurement has mean $`1/2`$.

For a one-specimen block, both axes are known with probability $`1/4`$, exactly one is unknown with probability $`1/2`$, and both are unknown with probability $`1/4`$. Their useful-record probabilities are respectively $`1`$, $`1/3`$, and $`1/3`$. Thus half the records are useful on average.

The last case uses a randomly rotated Bell basis. In the ordinary Bell frame, $`X\otimes X`$ and $`Z\otimes Z`$ commute, so their eigenvalues can be recorded together. They also determine a third covered correlation, with a necessary minus sign:

```math
Y\otimes Y=-(X\otimes X)(Z\otimes Z).
```

A basis can cover several axis words. Once the full marker transcript identifies the hidden word, the decoder recognizes covered records and recovers the correct product-Pauli sign. It cannot change a measurement that already occurred.

Every retained sign has mean $`c`$. Mapping a sign $`W`$ to $`(W+1)/2`$ puts it in the interval used by Watrous's Hoeffding theorem. Mapping the bound back to signs gives the estimation step in the [finite sample guarantee](../science/attaining_measurements.md#a-finite-sample-guarantee).

Every record remains a charged specimen, including discarded records and unused payloads. The complete example also prices failure to recover the hidden word. It shows the whole operation; two qubits alone cannot establish an asymptotic lower bound.

## 5. The additional steps between the book and the theorem

A general block measurement is a POVM on all payloads, rather than a particular Bell or GHZ circuit. The [collective converse](../science/collective_converse.md) therefore makes four further steps explicit.

First, read the block's markers. With $`b`$ specimens, a site remains unresolved precisely when all its markers were erased:

```math
K\sim\mathrm{Bin}\big(n,(1-q)^b\big).
```

Second, compare fixed possibilities $`c=+c_0`$ and $`c=-c_0`$. Their product-state difference contains only terms using an odd number of copies of $`P_a`$. Odd tensor powers of $`X,Y,Z`$ still act as a logical Pauli triple, with a possible sign and an extra multiplicity space. Pauli orthogonality limits the average squared response of every block effect.

Known-site factors require care: their weighted partial trace can have negative eigenvalues. The proof establishes a trace-norm bound for this signed operator. It does not treat it as a density operator without justification.

Third, reveal the one fixed hidden word only to the final decoder, as a mathematical strengthening. Conditioned on that word and the preplanned classical random seed, the blocks have product outcome laws, so their classical relative entropies add. The proof then averages over the common seed and word. Averaging each block over a separately redrawn word would describe a different experiment.

Fourth, Pinsker and binary discrimination turn the information bound into a specimen lower bound. At worst-case sign error at most one third,

```math
N\geq
\frac{2b}{9A_b(c_0)\beta_b^n},
\qquad
\beta_b=1-\frac{(1-q)^b}{3},
```

where

```math
A_b(c_0)=
\frac{\big[(1+c_0)^b-(1-c_0)^b\big]^2}{(1-c_0)^b}.
```

These steps give the finite-contrast result. A local sensitivity calculation alone would not imply it.

## 6. Why the same factor appears in the upper bound

The Bell count extends to a GHZ stabilizer basis. On $`k\geq1`$ unresolved sites it covers

```math
2^{k-1}+\mathbf1_{\{k\ \mathrm{even}\}}
```

full-support axis words among $`3^k`$ possibilities. The [attaining proof](../science/attaining_measurements.md#the-ghz-coverage-calculation) gives the generators, count, and decoder signs. At $`k=0`$, the useful-record probability is one.

Averaging over the erasures gives useful-record probability between $`\beta_b^n/2`$ and $`\beta_b^n`$. The lower bound's exponential factor is therefore achievable. For fixed block size and contrast, the [phase-boundary theorem](../science/phase_boundary.md) gives $`N_{\min}=\Theta_{b,q,c_0}(\beta_b^{-n})`$.

When the allowed cap grows with $`n`$, polynomial specimen cost is possible exactly when

```math
n(1-q)^b=O(\log n).
```

For the example's $`q=1/2`$, the left side is $`n2^{-b}`$. Each additional specimen inside a block halves the expected unresolved count. A sufficiently large logarithmic cap makes the useful-record probability large enough for polynomial cost; an arbitrary constant fraction of $`\log_2 n`$ need not suffice. The exact theorem, rather than the two-qubit illustration, establishes this criterion.

The signed task includes opposite fixed contrasts and an accuracy smaller than their magnitude. The sign-based necessity result is not a theorem for a positive-only interval. Nor does $`b`$ measure minimum coherent width or holding time: an attaining experiment can collect its markers and measure only its final payload, with no quantum carrier between arrivals. The [resource account](../science/resources.md) keeps these distinctions visible.

## 7. From erasures to noisy markers

An erasure leaves all three axes equally likely. A noisy observation supplies a posterior with three possibly different weights. Sort those weights, then decompose the posterior into a mixture of one, two and three uniform candidates. Only the three-axis component pays the odd-Pauli incompatibility bound. After averaging the markers, the loss of useful measurement coverage is the minimax probability of omitting the true axis.

Go through the [weighted converse](../science/noisy-markers.md#the-posterior-bound-for-arbitrary-joint-measurements) and use the [two-axis GHZ measurement](../science/noisy-markers.md#measuring-with-two-retained-axes-at-every-site) to track where the omitted axis and final word estimate enter the protocol. The [Goldar example](../science/noisy-markers.md#polynomial-budgets-and-goldars-noisy-qubit-markers) connects this finite decision problem to the logarithmic batch threshold.

## 8. Continue through the project

The [30-milestone map](MILESTONES.md) joins the textbook objects to these project-specific steps. It supplies understanding targets and dependencies, rather than a replacement table of contents for the book.

For a direct proof route, read the [model](../science/model.md), [finite collective converse](../science/collective_converse.md), [attaining measurement](../science/attaining_measurements.md), and [phase boundary](../science/phase_boundary.md), then the [resource interpretation](../science/resources.md). The [related-work comparison](../references/RELATED_WORK.md) credits research antecedents separately from the one educational anchor. Standard Pauli algebra, GHZ stabilizers, and statistical inequalities remain inherited tools; the source-specific growing-batch frontier is the contribution being explained.

