# A signed signal with erased measurement instructions

[Scientific overview](README.md) · [Finite converse](collective_converse.md) · [Attaining measurements](attaining_measurements.md)

A source carries a weak, global correlation. Classical markers say how to measure that correlation, but each marker can be erased. A learner with feedback can collect the instructions and then change its measurement. A learner committed to independent, preplanned measurement blocks can use instructions found inside a block, but cannot use one block's record to control another. The question is how large those blocks must be.

## Source specimens

Let $`n\geq1`$ and $`a=(a_1,\ldots,a_n)\in\{X,Y,Z\}^n`$. The axis word is fixed and unknown throughout the experiment. Put

```math
P_a=\bigotimes_{i=1}^n\sigma_{a_i},
\qquad
\sigma_{a,c}=\frac{I+cP_a}{2^n}.
```

The scalar $`c`$ is a **signed contrast**. Fix $`0<c_{\max}<1`$ and take $`c\in[-c_{\max},c_{\max}]`$. The payload is a valid, full-rank density operator: $`P_a`$ is traceless and $`P_a^2=I`$.

Each site also has a four-level classical marker with orthogonal known basis states $`\{\bot,X,Y,Z\}`$. At a fixed known reveal probability $`0<q<1`$,

```math
\tau_{a_i}=q|a_i\rangle\langle a_i|
+(1-q)|\bot\rangle\langle\bot|,
\qquad
\tau_a=\bigotimes_{i=1}^n\tau_{a_i},
\qquad
\omega_{a,c}=\tau_a\otimes\sigma_{a,c}.
```

One specimen means the entire marker-payload state $`\omega_{a,c}`$. Its marker dimension is $`4^n`$ and its payload dimension is $`2^n`$: two marker qubits and one payload qubit per site suffice. Markers are independent across coordinates and specimens, and independent of the payload conditional on the fixed word. The source supplies independent identical specimens; it does not resample the word between specimens.

The learner receives native specimens, not a classical description of $`a`$, a controlled preparation circuit, an inverse, a purification, or a coherent data-loading oracle. The marker basis, $`q`$, $`n`$ and the source family are known.

## The learning task

For fixed accuracy $`0<\epsilon<c_{\max}`$ and confidence failure $`0<\delta\leq1/3`$, return a classical estimate satisfying

```math
\sup_{a\in\{X,Y,Z\}^n}
\sup_{c\in[-c_{\max},c_{\max}]}
\Pr_{a,c}\bigl\{|\widehat c-c|>\epsilon\bigr\}
\leq\delta.
```

Choose any fixed $`c_0\in(\epsilon,c_{\max}]`$ for the converse. Successful estimation decides between $`c=+c_0`$ and $`c=-c_0`$ by taking the sign of the estimate. A symmetric domain containing those alternatives is load-bearing. The stated converse does not establish the same difficulty for a positive-only interval: even-copy measurements can reveal magnitude information while losing the sign.

The asymptotic comparison sends $`n\to\infty`$ with $`q,c_{\max},\epsilon,\delta`$ fixed. The finite theorem is stated separately at every allowed $`n,b,q,c_0`$. All logarithms in the resource laws are natural.

## Predetermined block experiments

A protocol has a hard maximum specimen budget $`N`$. Before obtaining any outcomes, it partitions the specimens into blocks of positive sizes at most an integer cap $`b`$. An independent classical random seed may determine the partition and the measurement assigned to each block.

Within a block, any joint POVM on all its markers and payloads is allowed. In particular, it may first read all markers and then choose a payload measurement using those marker values. Arbitrary fresh within-block ancillas and internal feedforward are included in the POVM. Reading orthogonal markers first loses no generality.

Between blocks:

- Neither an earlier marker outcome nor an earlier payload outcome may control a later block's measurement or partition.
- No coherent register or entangled ancillary state connects the blocks.
- Arbitrary classical records may be retained and processed jointly at the end, together with the seed.

Different blocks may use different preplanned POVMs. Randomization is allowed; a bound on expected cost under an unrestricted adaptive stopping rule is not being asserted. A protocol with a preplanned measurement sequence and bounded early stopping can be extended to its hard budget by ignoring extra outcomes.

The restriction therefore concerns the experiment's control structure. It is not a restriction to product measurements, Pauli settings, computationally simple effects, or a decoder that forgets the markers. The converse even grants the true word to the decoder **after** all measurements.

## Adaptive local comparison

The adaptive learner measures one specimen at a time and keeps only classical information between specimens. It can use earlier markers to choose later single-qubit measurement bases. One round of feedback suffices: read enough marker specimens to determine the axes, then measure fresh payloads in those axes. Every marker-only specimen and every final signal specimen counts.

| Learner | Within an experiment | Control between experiments | Final inference |
|---|---|---|---|
| Predetermined blocks | Arbitrary joint POVM on at most $`b`$ specimens, including internal marker-conditioned control | Independent of every earlier outcome; no coherent carrier | Unrestricted joint classical decoding |
| Adaptive local | Single-qubit marker and payload measurements on one specimen | One classical update after marker acquisition | Classical mean of matched Pauli parities |

If earlier marker records are allowed to control later blocks, the learner has the adaptive resource and the nonadaptive lower bound does not apply. Conversely, freezing only payload feedback while permitting marker feedback would not define the benchmark proved here.

## Why the input is simple but the measurement problem is not

For each fixed word, the payload is diagonal in a product eigenbasis. If $`s_i\in\{+1,-1\}`$ is the eigenvalue at site $`i`$, its classical probability is

```math
\Pr(s_1,\ldots,s_n)
=2^{-n}\left(1+c\prod_{i=1}^n s_i\right).
```

Thus the source is fully separable. Its preparation can sample $`n-1`$ fair signs, sample an independent parity of mean $`c`$, fix the final sign to realize that parity, and prepare the corresponding local eigenstates. Independently emit the axis or erasure marker. For the source holding the hidden parameters, this takes $`O(n)`$ elementary preparations and classical operations per specimen in the ideal model. Giving that hidden word to the learner before measurement would change the task.

For $`n\geq2`$, every proper payload marginal is maximally mixed, independent of $`c`$. The contrast appears in a full-support correlation. However, its magnitude is not exponentially small in trace distance:

```math
\frac12\|\omega_{a,c}-\omega_{a,c'}\|_1
=\frac{|c-c'|}{2},
\qquad
\operatorname{Tr}(P_a\sigma_{a,c})=c.
```

A known word would make estimating it a simple Bernoulli-mean problem. Unknown measurement instructions, rather than source entanglement or an expensive implicit state representation, produce the difficulty. The marked-Pauli mechanism is inherited from the closest work; the new quantitative question concerns growing blocks. See [attribution](../references/RELATED_WORK.md).

## The batch parameter

After $`r`$ specimens in a block, a coordinate remains unresolved with probability $`t_r=(1-q)^r`$. Define

```math
\beta_r=1-\frac{t_r}{3}.
```

The unresolved count is binomial, and $`\mathbb E[(2/3)^K]=\beta_r^n`$ controls both the collective converse and the GHZ coverage construction. Their [phase boundary](phase_boundary.md) is the central resource law.

The cap $`b`$ counts specimens in one preplanned experiment. An implementation may read early markers, discard their payloads, and use only the final payload; it need not retain a quantum carrier between arrivals. Consequently no lower bound on minimum simultaneous memory, coherent holding time, or entanglement depth follows from the batch theorem. Ideal operations, the specified independent erasure law, and fixed reveal probability are part of its scope.
