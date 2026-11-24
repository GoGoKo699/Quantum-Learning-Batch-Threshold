# Measurements that attain the batch threshold

The marked source supplies independent specimens with one fixed hidden axis word $`a\in\{X,Y,Z\}^n`$ and payload

```math
\sigma_{a,c}=\frac{I+cP_a}{2^n},\qquad
P_a=\bigotimes_{i=1}^n a_i.
```

Each classical marker independently reveals its axis with known probability $`q\in(0,1)`$, or reports an erasure. The [model](model.md) specifies the signed learning task and the permitted experiments. This page gives an explicit protocol for a working block size $`r\le b`$, where $`b`$ is the allowed cap. The protocol estimates $`c`$ for every $`c\in[-1,1]`$. The lower-bound comparison and the resulting polynomial-feasibility criterion concern the signed task on $`[-c_{\max},c_{\max}]`$, with $`0\lt c_0\le c_{\max}\lt 1`$ and fixed accuracy $`\epsilon\lt c_0`$.

## Read the block's markers, then measure one payload

Put

```math
\lambda=-\ln(1-q),\qquad
t_r=(1-q)^r,\qquad
\beta_r=1-\frac{t_r}{3}.
```

In each block, read all its markers in their known computational basis. Let $`U`$ be the sites whose axes have not been revealed by any of the block's $`r`$ specimens, and let $`K=|U|`$. Conditional on any fixed hidden word, the erasure events are independent across sites, so

```math
K\sim\mathrm{Bin}(n,t_r).
```

Use one payload from the block. The other payloads are unused and remain charged specimens. At every site outside $`U`$, measure the payload in the axis revealed by the block's own markers. On the $`K`$ unresolved sites, use the randomized GHZ-basis measurement below. Save the block's revealed-axis union, its random basis choices, and its payload outcomes.

All blocks use this same preplanned rule. A block may use its own marker outcomes to select its payload measurement. It never uses an earlier block's markers or payload outcomes to select that measurement. Classical inference across the full record is postponed to the decoder. Thus the experiment is an allowed nonadaptive block POVM, including its internal classical feed-forward.

## The GHZ coverage calculation

For $`k\ge1`$, consider the commuting generators

```math
g_0=X^{\otimes k},\qquad
g_j=Z_1Z_j\quad(2\le j\le k).
```

They define a complete GHZ stabilizer basis. Measure them after independent uniformly random single-qubit Clifford basis changes on the $`k`$ unresolved sites. Equivalently, apply the inverse local Clifford changes, apply the inverse GHZ preparation circuit, and measure every qubit in `Z`. Under all-to-all connectivity the GHZ part needs $`k-1`$ CNOT gates and one Hadamard gate. At $`k=1`$, it is simply an $`X`$-basis measurement before the random local basis change.

Ignoring their recorded signs, the stabilizer group contains exactly

```math
f_k=2^{k-1}+\mathbf 1_{\{k\ \mathrm{even}\}}
```

Pauli words with full support. To count them, the diagonal subgroup consists of all even-weight `Z` words. Multiplying this subgroup by $`X^{\otimes k}`$ gives $`2^{k-1}`$ full-support $`X/Y`$ words. The diagonal subgroup contributes the additional full-support word $`Z^{\otimes k}`$ precisely when $`k`$ is even.

Independent random local Cliffords map any fixed full-support Pauli word uniformly over the $`3^k`$ axis words, up to known signs. Therefore a fixed true unresolved Pauli belongs to the recorded randomized stabilizer group with probability

```math
h_0=1,\qquad
h_k=\frac{2^{k-1}+\mathbf 1_{\{k\ \mathrm{even}\}}}{3^k}
\quad(k\ge1).
```

The special value $`h_0=1`$ matters: when every axis is already known, local Pauli measurements give a valid payload parity on every block. For all $`k\ge0`$,

```math
\frac12\left(\frac23\right)^k
\le h_k\le
\left(\frac23\right)^k.
```

The GHZ group and its full-support count are standard stabilizer algebra. Their role here is to cover unresolved axis words efficiently after the decoder learns which word was relevant; GHZ state preparation by the source is unnecessary.

## Offline filtering and the exact acceptance probability

After data collection, combine all marker records to recover the hidden axis word. If some axis was never revealed, return a fixed estimate, such as zero. This branch is included in the failure probability below.

When the full word is recovered, examine each block's stored basis. Keep its payload record if the unresolved part of the true Pauli lies in that block's randomized GHZ stabilizer group. Compute that Pauli's eigenvalue from the recorded generator outcomes, including the local-Clifford and stabilizer signs. Multiply it by the measured parity on the known-axis sites. Call the resulting sign $`W\in\{-1,+1\}`$.

Membership and sign decoding take linear time in the number of unresolved sites. In the standard GHZ frame, a full-support word is covered exactly when it is an $`X/Y`$ word with an even number of $`Y`$ factors, or it is the all-`Z` word at even $`k`$. For an $`X/Y`$ word whose $`Y`$ positions form $`S`$, its eigenvalue is

```math
(-1)^{|S|/2}\,z_0
\prod_{j\in S\setminus\{1\}}z_j,
```

where $`\mathrm{z}_0,\mathrm{z}_j`$ are the outcomes of $`g_0,g_j`$. For the covered all-`Z` word, it is $`\prod_{j=2}^k z_j`$. The local Clifford changes supply an additional known sign.

Acceptance depends only on the markers and the randomly chosen basis, not on the payload outcomes. On an accepted record, the decoded observable on the entire payload is exactly $`P_a`$. Consequently, for every fixed $`a,c`$ and every accepted marker/basis choice,

```math
\Pr(W=w\mid\text{that accepted marker/basis choice})
=\frac{1+wc}{2},\qquad w\in\{-1,+1\}.
```

In particular, $`\mathbb E W=c`$. This proves more than an average-risk statement: the accepted sign law is the same for every accepted setting.

The per-block acceptance probability is uniform in the hidden word and independent of $`c`$:

```math
p_r=\mathbb E[h_K]
=\sum_{k=0}^n\binom nk t_r^k(1-t_r)^{n-k}h_k.
```

A closed form follows from the binomial generating function:

```math
p_r=\frac12\left[
\left(1-\frac{t_r}{3}\right)^n
+\left(1-\frac{2t_r}{3}\right)^n
+\left(1-\frac{4t_r}{3}\right)^n
-(1-t_r)^n\right].
```

The third base can be negative; the binomial sum is a nonnegative expression suitable for direct numerical evaluation. The pointwise bounds on $`h_k`$ give the simpler bounds

```math
\frac12\beta_r^n\le p_r\le\beta_r^n.
```

These bounds explain the common exponential factor in the attaining protocol and the arbitrary-block converse.

## A finite sample guarantee

Fix $`0\lt \delta\le1/3`$ and $`0\lt \epsilon\lt 1`$. Set

```math
m=\left\lceil\frac{2}{\epsilon^2}\ln\frac6\delta\right\rceil,
\qquad L=\ln\frac3\delta,
```

and use the deterministic number of blocks

```math
T=\left\lceil
\max\left\{
\frac{2m+8L}{p_r},\;
\frac{\ln(3n/\delta)}{r\lambda}
\right\}
\right\rceil.
```

There are exactly `N = rT` source specimens. After successful marker recovery, average the accepted signs; return zero if none were accepted. Projection of the estimate onto the promised interval can only reduce its absolute error.

Here is a proof that does not condition the sign analysis on successful global marker recovery. First define an ideal decoder that is supplied the true hidden word only for its final filtering step. Its measurements are the same as those of the actual protocol. For every fixed $`a,c`$, its acceptance indicators are independent Bernoulli variables with probability $`p_r`$. Conditional on their index set, the retained signs are independent, each with mean $`c`$. Thus the ideal accepted count $`M`$ is binomial with mean $`\mu=Tp_r`$.

Since $`\mu\ge2m+8L`$, a multiplicative Chernoff bound gives

```math
\Pr(M\lt m)\le\Pr(M\lt \mu/2)
\le e^{-\mu/8}\le\delta/3.
```

Conditional on any accepted index set of size at least $`m`$, Hoeffding's inequality gives

```math
\Pr\left(\left|\frac1M\sum_{j:\mathrm{accepted}}W_j-c\right|>
\epsilon\;\middle|\;\text{accepted index set}\right)
\le2e^{-M\epsilon^2/2}\le\delta/3.
```

Finally, over the $`rT`$ markers observed at each site,

```math
\Pr(\text{some axis never revealed})
\le n(1-q)^{rT}\le\delta/3.
```

On the complement of this last event, the actual decoder equals the ideal decoder. A union bound over marker failure, too few accepted records, and the ideal estimation error therefore proves

```math
\sup_{a,\,c\in[-1,1]}
\Pr_{a,c}(|\widehat c-c|>\epsilon)\le\delta.
```

No independence conditional on the global marker-coverage event is assumed. All rejected records and all unused payloads remain included in $`N`$.

Using $`p_r\ge\beta_r^n/2`$ gives

```math
N=O\left(
r\epsilon^{-2}\beta_r^{-n}\ln\frac1\delta
+\lambda^{-1}\ln\frac n\delta+r
\right),
```

with absolute constants for $`\epsilon\in(0,1)`$. For fixed $`q`$, the second term is $`O_q(\ln(n/\delta))`$.

## A large cap need not increase the cost

The cap permits blocks smaller than $`b`$. A convenient working choice is

```math
r=\min\left\{b,
\left\lceil\frac{\ln(6n/\delta)}{\lambda}\right\rceil
\right\}.
```

At the second value, the chance that a block leaves any axis unresolved is at most $`\delta/6`$. In particular $`p_r`$ is bounded below by a constant. This truncation prevents an unnecessarily large allowed cap from creating an artificial input-reading cost. At fixed confidence and accuracy, caps above order $`\log n`$ admit order-$`\log n`$ total specimen cost.

For the signed task, the finite converse and this upper bound establish the polynomial criterion

```math
n(1-q)^{b(n)}=O(\log n).
```

This criterion concerns a uniform polynomial bound along the chosen sequence of caps. The upper bound is valid on positive-only contrast intervals too; the sign-based necessity statement is not asserted for those different tasks.

## One feedback round with local single-copy measurements

An adaptive learner first reads markers on

```math
m_0=\left\lceil\frac{\ln(2n/\delta)}{\lambda}\right\rceil
```

specimens. It retains only their classical axis records and discards their payloads. Except with probability $`\delta/2`$, every axis is then known. It measures

```math
s=\left\lceil\frac{2}{\epsilon^2}\ln\frac4\delta\right\rceil
```

fresh payloads in that learned product Pauli basis and averages their parities. The mean is $`c`$, and Hoeffding bounds the conditional estimation error by $`\delta/2`$. Marker failure is handled separately by a union bound. The total is

```math
N_{\mathrm{adaptive}}=m_0+s
=O_q\left(\ln\frac n\delta+
\epsilon^{-2}\ln\frac1\delta\right).
```

Only local measurements and one change of measurement rule are used. No quantum carrier persists between source specimens. The block benchmark excludes this use of earlier blocks' marker records to control later payload measurements.

## A product-measurement alternative

One can replace the GHZ measurement by independently guessing each unresolved axis uniformly, then measuring the guessed product Pauli. Offline, keep only records whose full guessed word equals the recovered true word. The accepted sign again has mean $`c`$, while its acceptance probability is

```math
p_r^{\mathrm{product}}=\mathbb E[3^{-K}]
=\left(1-\frac{2t_r}{3}\right)^n.
```

The same finite-count and marker-recovery proof applies after substituting this probability. This simpler protocol already has the same polynomial-feasibility criterion. The randomized GHZ basis improves the exponential acceptance factor and uses entangling gates only among qubits of one payload. Neither construction needs inter-copy quantum entanglement. The [resource account](resources.md) distinguishes these implementations from the arbitrary collective measurements allowed in the converse.
