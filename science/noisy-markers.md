# Noisy markers and the batch threshold

[Model](model.md) · [Finite-contrast converse](collective_converse.md) · [Attaining measurements](attaining_measurements.md) · [Related work](../references/RELATED_WORK.md)

An erasure marker either reveals its Pauli axis or gives no information. With noisy markers every observation can leave all three axes possible. The quantity that controls the batch threshold is the error of ruling out one axis. The decoder can identify the full word after the measurements. During a measurement, two candidates per site already suffice to construct a commuting measurement that covers the true Pauli word with constant probability.

## Marker experiment and finite specimen bounds

Keep the [signed payload and predetermined-block model](model.md). A single fixed hidden word $`a\in\{X,Y,Z\}^n`$ selects the Pauli string $`P_a`$ in $`2^{-n}(I+cP_a)`$. For each specimen and site, the marker is a draw from a known finite law $`Q_{a_i}`$, conditional on the word. The markers are mutually independent and independent of the payload at fixed $`a`$. This includes markers represented by density matrices diagonal in a known common basis.

For $`b`$ marker draws at one site, let $`D(j\mid z)`$ be the probability of omitting axis $`j`$ after reading the transcript $`z`$. Define the minimax omission error $`e_b`$ and its complement $`\beta_b`$ by

```math
\begin{aligned}
e_b
&=\min_D\max_{j\in\{X,Y,Z\}}
\sum_z Q_j^{\otimes b}(z)D(j\mid z)\\
&=\max_{\pi}\sum_z\min_{j\in\{X,Y,Z\}}
\left[\pi_j Q_j^{\otimes b}(z)\right],\qquad \beta_b=1-e_b .
\end{aligned}
```

The dual identity follows from finite minimax. For a prior $`\pi`$, the best decision omits an axis with the smallest posterior probability. The optimal error is nonincreasing in $`b`$ because an omission rule can ignore observations. Uniform random omission gives $`0\le e_b\le 1/3`$.

**Converse.** For any three marker laws and $`0\lt c_0\lt 1`$, every preplanned block protocol with block sizes at most $`b`$ that distinguishes $`+c_0`$ from $`-c_0`$ with worst-case error at most $`\delta\lt 1/2`$ uses at least

```math
N\ge
\frac{2b(1-2\delta)^2}{A_b(c_0)\beta_b^n},
\qquad
A_b(c_0)=\frac{[(1+c_0)^b-(1-c_0)^b]^2}{(1-c_0)^b}.
```

The decoder may learn the true word after the measurements. The same bound applies to estimation with error tolerance $`\epsilon\lt c_0`$ on a contrast interval containing $`\pm c_0`$.

**Achievability.** Suppose the three marker laws are pairwise distinct. For any actual block size $`r\le b`$, the protocol below estimates $`c`$ with absolute error at most $`\epsilon`$ and failure probability at most $`\delta`$, uniformly in the word and valid contrasts, using

```math
O_Q\!\left(
  \log(n/\delta)+r\epsilon^{-2}\beta_r^{-n}\log(1/\delta)
\right)
```

specimens, for $`0\lt \epsilon\lt 1`$ and $`0\lt \delta\le 1/3`$. At fixed $`b`$, accuracy and confidence, the signed estimation task has matching specimen order $`\Theta(\beta_b^{-n})`$ whenever $`e_b\gt 0`$. If $`e_b=0`$, the upper bound still includes the logarithmic cost of learning the word. For the erasure marker of the [original model](model.md), a block leaves an unidentified axis uniformly distributed with probability $`(1-q)^b`$ under the uniform prior. Uniform omission in that event is also minimax, giving $`e_b=(1-q)^b/3`$.

## The posterior bound for arbitrary joint measurements

Choose a least-favorable prior $`\pi`$ for the cap $`b`$. Draw each site of the hidden word independently from $`\pi`$ once, and use that same word in every block. Because the marker registers are classical in a known basis, one may first read them and then apply a conditional payload POVM. Given the marker record of an $`s`$-specimen block, the posterior over the sites of the word remains a product distribution.

Write a one-site posterior in decreasing order as $`p_1\ge p_2\ge p_3`$. It is the mixture

```math
(p_1-p_2)\delta_1
 +2(p_2-p_3)\mathrm{Unif}\{1,2\}
 +3p_3\mathrm{Unif}\{1,2,3\}.
```

To bound an odd tensor term in the sign comparison, fix the mixture component at every site and condition further on the actual axis at each singleton or two-candidate site. The remaining $`k`$ sites are uniform over all three axes. For any density operator $`\omega`$ on the block payloads and any odd set $`S`$ of payload copies, the [odd-subset lemma](collective_converse.md#3-odd-tensor-powers-retain-a-pauli-algebra) bounds the uniform average of $`[\mathrm{Tr}(\omega Q_{a,S})]^2`$ by $`(2/3)^k`$. Here $`Q_{a,S}`$ applies the Pauli word on the copies in $`S`$. The fixed axes at the other sites supply the same signed partial trace as in that lemma.

Averaging the mixture independently at each site replaces the factor $`(2/3)^k`$ by $`\prod_i(1-p_{i,3})`$. In particular, the bound applies to the normalized effect of any marker-conditioned joint POVM. The finite-contrast expansion and $`L_2`$ triangle inequality from the [erasure proof](collective_converse.md#4-one-block-at-finite-contrast) give conditional relative entropy at most $`A_s(c_0)\prod_i(1-p_{i,3})`$, averaged over the posterior word. Averaging the markers then gives

```math
\mathbb{E}_{a}
D_{\mathrm{KL}}\!\left(P_{a,+}^{(s)}\middle\Vert P_{a,-}^{(s)}\right)
\le A_s(c_0)\big[1-e_s(\pi)\big]^n.
```

Here $`P_{a,\pm}^{(s)}`$ includes the block's marker record, and $`e_s(\pi)`$ is the Bayes omission error after $`s`$ marker draws under this single prior. For $`s\le b`$, ignoring draws proves $`e_s(\pi)\ge e_b(\pi)=e_b`$. The [finite-contrast proof](collective_converse.md#5-one-hidden-word-across-every-block) also shows that $`A_s(c_0)/s`$ is nondecreasing. These two facts permit different block sizes under one prior and one fixed hidden word. Conditional on the word and the independently chosen schedule seed, block records are independent. Revealing the word and seed at final decoding makes the relative entropies add, giving a total at most $`NA_b(c_0)\beta_b^n/b`$. Pinsker's inequality and worst-case decision error $`\delta`$ yield the stated bound.

## Measuring with two retained axes at every site

Read all markers of a signal block of size $`r`$. At each site, use an optimal omission rule independently and retain the other two axes. The true word lies among the retained words with probability at least $`\beta_r^n`$ for every word.

Apply local Clifford changes of basis so that the retained axes are $`X`$ and $`Y`$, recording any signs. Divide the full-support $`X/Y`$ words into two classes according to the parity of the number of $`Y`$ factors. Two words in the same class differ at an even number of sites, so they commute. Randomly choose one class, then jointly measure a complete GHZ stabilizer basis containing that class, up to the recorded signs. For the even class, one can use the generators $`X^{\otimes n}`$ and $`Z_1Z_i`$ for $`2\le i\le n`$. A local Clifford that exchanges $`X`$ and $`Y`$ at one site changes the parity and gives the other class. This measurement uses just one payload. The probability that the measured class contains the true word is at least $`\beta_r^n/2`$.

To decode, use a disjoint, predetermined group of specimens for marker-only word identification. Their payloads are discarded and their copies count toward the budget. Pairwise distinct marker laws have maximum pairwise Bhattacharyya coefficient $`\zeta=\max_{j\ne k}\sum_y\sqrt{Q_j(y)Q_k(y)}\lt 1`$. After $`M`$ marker observations per site, maximum likelihood gives probability at most $`2n\zeta^M`$ of any wrong site. Choose $`M=O_Q(\log(n/\delta))`$ so that this is at most $`\delta/3`$. The case $`\zeta=0`$ allows one observation. These marker-only specimens can be partitioned into blocks of size at most $`b`$. Their records are consulted only at final decoding.

With the identified word, keep the signal records that contain its Pauli observable and recover the corresponding eigenvalue. For the true word the eligibility event depends on the markers and class choice alone, and every retained sign has mean $`c`$. At fixed word the signs are independent across blocks, conditional on the eligibility choices. For example, let

```math
m=\left\lceil
\max\{4\log(3/\delta),\,2\epsilon^{-2}\log(6/\delta)\}
\right\rceil,\qquad
T=\left\lceil4m/\beta_r^n\right\rceil .
```

Use $`T`$ signal blocks and average the first $`m`$ eligible signs. The mean eligible count is at least $`2m`$, so the probability of fewer than $`m`$ is at most $`\exp(-m/4)\le\delta/3`$ by a Chernoff bound. Given at least $`m`$, the sign average has error probability at most $`2\exp(-m\epsilon^2/2)\le\delta/3`$ by Hoeffding's inequality. The total budget is $`M+rT`$ even when decoding fails. All block measurements depend only on their own markers and independent random choices.

## Polynomial budgets and Goldar's noisy qubit markers

For fixed pairwise distinct marker laws, accuracy and confidence in the signed task, the specimen cost is polynomial in $`n`$ exactly when

```math
ne_{b(n)}=O(\log n).
```

Indeed, identifying the axis via maximum likelihood and omitting one of the other axes gives $`e_b\le2\zeta^b`$. If the criterion fails, there is a subsequence with $`ne_b/\log n\to\infty`$, and on that subsequence $`b=O(\log n)`$. The converse then wins because $`-\log(1-e_b)\ge e_b`$ and $`\log A_b(c_0)=O_{c_0}(b)`$. Conversely, one can truncate the actual block size at $`O_Q(\log n)`$ using $`e_r\le2\zeta^r`$. For either the original cap or the truncated size, the stated criterion ensures $`\beta_r^{-n}`$ is polynomial because $`e_r\le1/3`$.

Goldar et al.'s original ternary markers are the commuting qubit states $`(I-uZ)/2`$, $`I/2`$ and $`(I+uZ)/2`$. In the common eigenbasis, their laws are Bernoulli with parameters $`(1-u)/2`$, $`1/2`$ and $`(1+u)/2`$. Goldar et al. take $`0\lt u\lt 1/2`$; the calculation below holds for fixed $`0\lt u\lt 1`$. Their paper establishes the finite-accuracy separation for single-copy measurements and explicitly asks what happens when collective multicopy measurements are permitted. [Goldar et al., Sections V and VIII-C](https://arxiv.org/html/2610.38922v1)

Let $`\alpha_b=\tfrac12\sum_z\min\{Q_X^{\otimes b}(z),Q_Z^{\otimes b}(z)\}`$ be the symmetric binary error for distinguishing the two extreme laws, and let

```math
\rho_b=\max_z
\frac{\min\{Q_X^{\otimes b}(z),Q_Z^{\otimes b}(z)\}}{Q_Y^{\otimes b}(z)}
\le (1-u^2)^{b/2}.
```

The upper bound follows by comparing the minimum with the geometric mean. Omitting the less likely extreme with random tie-breaking gives $`e_b\le\alpha_b`$, since it never omits $`Y`$ and the two other conditional errors both equal $`\alpha_b`$ by symmetry. For the dual lower bound use prior weights $`(1,\rho_b,1)/(2+\rho_b)`$. The middle weighted likelihood is at least the smaller extreme one pointwise, giving $`e_b\ge2\alpha_b/(2+\rho_b)`$. Thus $`e_b/\alpha_b\longrightarrow1`$ at fixed $`u`$.

The extreme-law Bayes rule thresholds the binomial count at $`b/2`$, with a fair coin at a tie. At the nearest integer to the threshold in the error tail, Stirling's formula gives mass of order $`b^{-1/2}(1-u^2)^{b/2}`$ for both parities of $`b`$. Farther into the tail, successive terms decrease at least geometrically with ratio at most $`(1-u)/(1+u)`$. The central term bounds the tail below up to the factor of one half for ties. Therefore

```math
e_b=\Theta_u\!\left(b^{-1/2}e^{-C_u b}\right),
\qquad C_u=-\tfrac12\log(1-u^2).
```

Polynomial specimen cost is possible exactly when there is a constant $`K`$ such that, for all sufficiently large $`n`$,

```math
C_u b(n)\ge\log n-\tfrac32\log\log n-K .
```

At the transition $`b=\Theta_u(\log n)`$, substituting in $`ne_b=O(\log n)`$ gives the displayed logarithmic correction. Smaller and larger orders of $`b`$ fall on the corresponding sides by the exponential estimate.

For $`b=1`$, put $`q=(1-u)/2`$. Omitting $`Y`$ with probability $`q/(1+q)`$ and otherwise omitting the less likely extreme equalizes the three omission errors. The dual bound gives the same value, as $`\rho_1=2q`$ and $`\alpha_1=q`$. Hence

```math
e_1=\frac{1-u}{3-u},\qquad
\beta_1^{-n}=\left(\frac{3-u}{2}\right)^n .
```

This is the sharp exponential specimen order for fixed-accuracy signed estimation with single-copy global measurements. The finite-contrast proof also applies when the full estimation interval includes the endpoints $`c=\pm1`$, by taking an interior pair $`\pm c_0`$ with $`\epsilon\lt c_0\lt 1`$ for the lower bound.

The resource is specimens inside predetermined experiments without cross-block control. The model allows arbitrary within-block joint measurements in the converse and gives a one-payload implementation in the upper bound. The result leaves the minimum coherent storage, connectivity-dependent gate cost and noncommuting marker models open.
