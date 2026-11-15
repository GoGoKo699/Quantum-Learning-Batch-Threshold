# Collective block measurements: a finite-contrast converse

The block restriction concerns when an experiment may use earlier information. Inside one block the learner may inspect every classical marker, make an arbitrary joint measurement on all payloads, and retain an arbitrary classical record. A later block cannot use any earlier marker or payload outcome, and no coherent carrier or entangled ancilla connects the blocks. Unlimited joint classical inference remains available after all measurements. The precise source and controls are specified in [the model](model.md).

The proof below works directly with two nonzero contrasts. Its conclusion therefore covers fixed-confidence estimation by arbitrary estimators, including biased estimators.

## 1. Finite theorem

Let $`n\geq1`$, $`0\lt q\lt 1`$, and let the block cap $`b\geq1`$ be an integer. Fix a contrast $`0\lt c_0\lt 1`$. Write

```math
t_b=(1-q)^b,\qquad
\beta_b=1-\frac{t_b}{3},\qquad
A_b(c_0)=
\frac{\big[(1+c_0)^b-(1-c_0)^b\big]^2}{(1-c_0)^b}.
```

A protocol uses at most $`N`$ source specimens, partitioned into preplanned blocks of sizes at most $`b`$. Block sizes and measurements may depend on an independent shared classical seed. Each block ends in a classical record. The specimen budget is a maximum budget; the theorem does not assume an unbounded stopping rule controlled by previous outcomes.

**Theorem.** If the protocol decides whether $`c=+c_0`$ or $`c=-c_0`$ with error at most $`\eta\lt 1/2`$ for every hidden axis word $`a\in\{X,Y,Z\}^n`$, then

```math
N\ \geq\
\frac{2b(1-2\eta)^2}
     {A_b(c_0)\,\beta_b^n}.
```

In particular, error at most one third requires

```math
N\ \geq\ \frac{2b}{9A_b(c_0)\,\beta_b^n}.
```

The weaker bound obtained by omitting the numerator factor $`b`$ is also valid. The displayed stronger form includes unequal predetermined block sizes.

If an estimator has absolute error at most $`\epsilon\lt c_0`$ with probability at least $`1-\eta`$ uniformly over the hidden word and both contrasts, the sign of its estimate gives such a decision. Thus the same lower bound applies whenever the estimation interval contains $`\pm c_0`$. The bound is minimax: it does not assert that every individual hidden word has the same difficulty.

We use natural logarithms in relative entropy and asymptotic logarithms.

## 2. Reading a block's markers loses no generality

Consider a block of $`s`$ specimens. Its payload state, conditioned on the fixed hidden word, is

```math
\rho_{a,c}^{\otimes s}
=
2^{-ns}\big(I+cP_a\big)^{\otimes s},
\qquad
P_a=\bigotimes_{i=1}^n \sigma_{a_i}.
```

For the lower bound only, draw $`a`$ once, uniformly from the ternary words, and use that same word in every block.

Marker registers are classical in orthogonal known basis states. Consequently an arbitrary joint marker-payload POVM has the same outcome statistics as first reading all markers and then applying a marker-dependent payload POVM. The off-diagonal marker blocks of an effect never contribute. This reduction includes internal feedforward, arbitrary ancillas used only within the block, and arbitrary joint processing of the payloads.

Fix the observed marker pattern and its revealed values. Let $`K`$ be the coordinates erased in all $`s`$ marker copies and write $`k=|K|`$. Every remaining coordinate has a known axis. Conditional on these observations, the unresolved axes are still independent uniform elements of $`\{X,Y,Z\}`$. Furthermore,

```math
k\sim\mathrm{Bin}\!\big(n,t_s\big),
\qquad t_s=(1-q)^s.
```

The marker pattern has the same law at the two contrasts.

## 3. Odd tensor powers retain a Pauli algebra

For a nonempty subset $`S\subseteq\{1,\ldots,s\}`$, let $`Q_{a,S}`$ put $`P_a`$ on each payload copy in $`S`$ and the identity on every other copy. Only odd cardinalities will enter the sign difference.

**Odd-subset lemma.** Fix any conditional marker record, any positive operator $`\omega`$ of trace one on the $`s`$ payloads, and an odd nonempty subset $`S`$. Averaging over its unresolved axes gives

```math
\frac{1}{3^k}
\sum_{a_K\in\{X,Y,Z\}^k}
\big[\mathrm{Tr}(\omega Q_{a,S})\big]^2
\ \leq\ \left(\frac23\right)^k.
```

This includes $`k=0`$.

To prove the lemma, set $`r=|S|`$. At each unresolved coordinate, the three operators

```math
T_X=X^{\otimes r},\qquad
T_Y=Y^{\otimes r},\qquad
T_Z=Z^{\otimes r}
```

are Hermitian involutions and pairwise anticommute because $`r`$ is odd. Up to a unitary change of coordinates, they act as

```math
T_X=X\otimes I,\qquad
T_Z=Z\otimes I,\qquad
T_Y=(-1)^{(r-1)/2}Y\otimes I.
```

The identity factor is a multiplicity space. Taking all unresolved coordinates gives an ordinary $`k`$-qubit Pauli algebra with multiplicity. The extra signs do not affect squared expectations.

The known coordinates contribute a fixed Hermitian unitary $`F`$ on the complementary space; unused copies contribute identity factors. After the preceding unitary changes of coordinates, define the signed reduced operator

```math
B=\mathrm{Tr}_{\mathrm{comp}}
\big[(I\otimes F)\omega'\big].
```

It is essential that $`B`$ need not be positive. If $`F=\Pi_+-\Pi_-`$, cyclicity of the complementary partial trace gives

```math
B=B_+-B_-,
\qquad
B_\pm=
\mathrm{Tr}_{\mathrm{comp}}
\big[(I\otimes\Pi_\pm)\omega'
     (I\otimes\Pi_\pm)\big]\geq0,
\qquad
\mathrm{Tr}(B_++B_-)=1.
```

Hence $`\|B\|_1\leq1`$. The claim would be unjustified if this signed operator were treated as a density matrix without this step.

For a $`k`$-qubit density matrix $`\tau`$, Pauli Parseval gives

```math
\sum_{P\in\{I,X,Y,Z\}^{\otimes k}}
\big[\mathrm{Tr}(\tau P)\big]^2
=
2^k\mathrm{Tr}(\tau^2)
\leq2^k.
```

For $`k\geq1`$, removing the identity coefficient and keeping only full-support Paulis yields a sum at most $`2^k-1`$. The same bound holds for every Hermitian $`B`$ with trace norm at most one: express $`B`$ as a signed mixture of pure states with total absolute weight at most one, and apply the triangle inequality to their vectors of full-support Pauli coefficients. Therefore

```math
\sum_{a_K\in\{X,Y,Z\}^k}
\big[\mathrm{Tr}(\omega Q_{a,S})\big]^2
\leq2^k-1
\qquad(k\geq1).
```

Dividing by $`3^k`$ proves the stated bound. When $`k=0`$, use $`|\mathrm{Tr}(\omega Q_{a,S})|\leq1`$. The expression $`2^k-1`$ must not be used at that endpoint.

The proof places no restriction on entanglement inside $`\omega`$ or on the measurement effect from which it will be obtained.

## 4. One block at finite contrast

Fix a marker record. Let $`\{M_z\}_z`$ be its conditional payload POVM. Zero effects may be omitted. Define

```math
p_0(z)=\frac{\mathrm{Tr}M_z}{2^{ns}},
\qquad
r_{a,S}(z)=
\frac{\mathrm{Tr}(M_zQ_{a,S})}
     {\mathrm{Tr}M_z}.
```

The reference probabilities sum to one. Expanding the product payload state at $`c=\pm c_0`$ gives

```math
p_{a,+}(z)-p_{a,-}(z)
=
2p_0(z)
\sum_{\substack{S\subseteq[s]\\ |S|\ \mathrm{odd}}}
c_0^{|S|}r_{a,S}(z).
```

Every eigenvalue of $`I-c_0P_a`$ is at least $`1-c_0`$, so

```math
p_{a,-}(z)\geq(1-c_0)^s p_0(z).
```

The chi-squared divergence consequently satisfies

```math
\chi^2(p_{a,+}\|p_{a,-})
\leq
\frac{4}{(1-c_0)^s}
\sum_zp_0(z)
\left[
\sum_{\substack{S\subseteq[s]\\ |S|\ \mathrm{odd}}}
c_0^{|S|}r_{a,S}(z)
\right]^2.
```

Apply the triangle inequality in the real $`L_2`$ space with measure given by uniform unresolved axes and the reference probabilities $`p_0`$. The odd-subset lemma bounds every summand's squared norm by $`(2/3)^k`$. Thus, pointwise in the marker pattern and revealed values,

```math
\mathbb E_{a_K}
\chi^2(p_{a,+}\|p_{a,-})
\leq
\frac{4}{(1-c_0)^s}
\left[
\sum_{\substack{j=1\\j\ \mathrm{odd}}}^{s}
\binom{s}{j}c_0^j
\right]^2
\left(\frac23\right)^k
=
A_s(c_0)\left(\frac23\right)^k.
```

For discrete distributions, relative entropy obeys $`D_{\mathrm{KL}}(p\|q)\leq\chi^2(p\|q)`$; this follows from $`\log x\leq x-1`$. The same argument applies to general POVM outcome measures by using their densities relative to the maximally mixed reference measure.

Finally, average the marker pattern:

```math
\mathbb E\left[\left(\frac23\right)^k\right]
=
\left(1-\frac{(1-q)^s}{3}\right)^n
=
\beta_s^n.
```

Including the marker record in the block outcome, and averaging the one fixed hidden word under its uniform prior, gives

```math
\mathbb E_a
D_{\mathrm{KL}}\!\left(
P^{(s)}_{a,+}\middle\|P^{(s)}_{a,-}
\right)
\leq A_s(c_0)\beta_s^n.
```

This is a finite nonzero-contrast inequality. No inference from local Fisher information to a global fixed-error guarantee is required.

## 5. One hidden word across every block

The word $`a`$ is a shared nuisance parameter, so the unconditional block records are generally correlated. Their averaged laws must not be multiplied as though a fresh hidden word were drawn for each block.

Instead, strengthen the learner by revealing the actual $`a`$ only at final classical inference. This revelation cannot control any earlier experiment. Also include its independent classical seed $`R`$ in the final record.

Conditioned on $`a`$ and $`R`$, the blocks are independent: source specimens are independent, block measurements are preplanned, and no coherent system connects the blocks. The two augmented transcript laws $`\mathcal P_+`$ and $`\mathcal P_-`$ therefore obey

```math
D_{\mathrm{KL}}(\mathcal P_+\|\mathcal P_-)
=
\mathbb E_R
\sum_{j=1}^{T(R)}
\mathbb E_a
D_{\mathrm{KL}}\!\left(
P_{j,a,+}^{R}\middle\|P_{j,a,-}^{R}
\right)
\leq
\mathbb E_R
\sum_{j=1}^{T(R)}
A_{s_j(R)}(c_0)\beta_{s_j(R)}^n.
```

This identity grants all useful final information about the nuisance word, including what markers in other blocks might eventually reveal. It does not permit that information to choose any measurement retrospectively.

To express the bound in total specimens, observe that $`\beta_s`$ is nondecreasing in $`s`$. Also, if

```math
S_s(c_0)=
\sum_{\substack{j=1\\j\ \mathrm{odd}}}^{s}
\binom{s}{j}c_0^j,
```

then $`S_s(c_0)/s`$ is nondecreasing, because

```math
\frac{1}{s}\binom{s}{j}
=
\frac{1}{j}\binom{s-1}{j-1}
```

is nondecreasing in $`s`$ for every fixed positive $`j`$. It follows that

```math
\frac{A_s(c_0)}{s}
=
4s\left(\frac{S_s(c_0)}{s}\right)^2(1-c_0)^{-s}
```

is nondecreasing. For every $`s\leq b`$,

```math
A_s(c_0)\beta_s^n
\leq
\frac{s}{b}A_b(c_0)\beta_b^n.
```

Since $`\sum_js_j(R)\leq N`$ for each seed, the augmented transcript satisfies the single budget bound

```math
D_{\mathrm{KL}}(\mathcal P_+\|\mathcal P_-)
\leq
N\,\frac{A_b(c_0)}{b}\,\beta_b^n.
```

Shared independent randomness and unequal preplanned block sizes thus do not change the claimed resource law.

## 6. From divergence to minimax error

A decision with worst-case error at most $`\eta`$ also has average error at most $`\eta`$ under the uniform hidden-word prior and equal prior probabilities of the two signs. The same decision can ignore the extra final revelation of $`a`$. Therefore the augmented distributions must have total variation distance at least $`1-2\eta`$.

Pinsker's inequality and the budget bound give

```math
1-2\eta
\leq
\mathrm{TV}(\mathcal P_+,\mathcal P_-)
\leq
\sqrt{\frac12
D_{\mathrm{KL}}(\mathcal P_+\|\mathcal P_-)}
\leq
\sqrt{
\frac{NA_b(c_0)\beta_b^n}{2b}
}.
```

Rearranging proves the finite theorem. Equivalently, the minimax error of any budget-$`N`$ protocol is bounded below by

```math
\frac12\left[
1-\sqrt{
\frac{NA_b(c_0)\beta_b^n}{2b}
}
\right]_+,
\qquad [x]_+=\max\{x,0\}.
```

The prior is a proof device. The resulting guarantee rules out uniformly successful estimators over all hidden words.

## 7. Consequences for the batch frontier

The [attaining measurements](attaining_measurements.md) use randomized GHZ stabilizer bases and final classical filtering. Their per-block useful-record probability lies between $`\beta_b^n/2`$ and $`\beta_b^n`$. All unsuccessful source specimens and final recovery of the hidden word are counted.

For every fixed $`b`$, fixed $`q\in(0,1)`$, fixed nonzero contrast and fixed confidence, this upper bound and the finite converse give the matching exponential order

```math
N_{\min}(n;b,q,c_0)
=
\Theta_{b,q,c_0}\!\left(\beta_b^{-n}\right).
```

The constants may depend on those fixed parameters. This statement does not identify the optimal finite constants.

For a varying integer cap $`b=b(n)`$, fix $`q`$, the confidence and an accuracy $`\epsilon\lt c_0`$ on an estimation interval containing $`\pm c_0`$. Set $`\ell=-\log(1-q)>0`$ and $`w_n=n e^{-\ell b(n)}`$. A uniform polynomial specimen budget is possible exactly when

```math
w_n=n(1-q)^{b(n)}=O(\log n).
```

For necessity, suppose this condition fails. There is a subsequence along which $`w_n/\log n\to\infty`$. On that subsequence, eventually $`b\leq\log n/\ell`$. Moreover,

```math
A_b(c_0)
\leq
\exp\!\big(\kappa(c_0)b\big),
\qquad
\kappa(c_0)=2\log(1+c_0)-\log(1-c_0),
```

and $`-\log(1-t_b/3)\geq t_b/3`$. The finite lower bound then implies

```math
\log N
\geq
\frac{w_n}{3}
-\kappa(c_0)b
+\log\!\big(2b(1-2\eta)^2\big).
```

Dividing by $`\log n`$ diverges along the subsequence. No single polynomial bound can hold for all sufficiently large $`n`$.

For sufficiency, use the GHZ upper bound. A cap much larger than logarithmic size need not be filled: take

```math
\widehat b
=
\min\!\left\{
b,\,
\max\!\left(1,\left\lceil\frac{\log n}{\ell}\right\rceil\right)
\right\}.
```

Then $`\widehat b=O_q(\log n)`$ and $`n(1-q)^{\widehat b}=O(\log n)`$. Since

```math
-\log(1-t/3)\leq\frac{t}{3-t}\leq\frac t2
\qquad(0\leq t\leq1),
```

the inverse acceptance probability is polynomial. The attaining protocol's block cost and marker-recovery cost are also polynomial.

The criterion uses a uniform polynomial bound. An oscillating batch sequence need not possess a limiting exponent. The detailed boundary and its fixed-parameter interpretation are developed in [the phase boundary](phase_boundary.md).

## 8. Scope of the conclusion

The converse permits arbitrary joint POVMs within each block, arbitrary final classical decoding, and final revelation of the hidden word. Its limitation is the absence of control and coherent carriers between blocks. If previous markers may choose a later measurement, local single-copy experiments can first collect the axes and then measure the correct full Pauli; the exponential lower bound no longer applies.

The resource $`b`$ counts source specimens in one preplanned joint experiment. It is not a theorem about minimum coherent width, entanglement depth, gate depth, or memory lifetime. The attaining GHZ protocol entangles qubits within one payload and needs no entanglement between different payload copies. Ideal operations and the stated independent erasure markers are assumed. These qualifiers are part of the theorem, as discussed in [resources and interpretation](resources.md).

