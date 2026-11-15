# The boundary between polynomial and exponential sample cost

[Model](model.md) · [Converse](collective_converse.md) · [Attaining measurements](attaining_measurements.md)

The number of unresolved instructions in one block determines the statistical cost. For a block cap $`b`$, let

```math
t_b=(1-q)^b,\qquad
\beta_b=1-\frac{t_b}{3},\qquad
w_n=nt_b.
```

The source, accuracy convention and control restrictions are those of the signed-contrast [model](model.md). In particular, every earlier marker as well as payload outcome is unavailable for controlling another block; final classical processing remains unrestricted.

## One finite pair of bounds

Fix a testing contrast $`0<c_0<1`$ and error $`\eta<1/2`$. For every predetermined-block protocol of hard specimen budget $`N`$ that succeeds for every hidden word,

```math
N\geq
\frac{2b(1-2\eta)^2}{A_b(c_0)\beta_b^n},
\qquad
A_b(c_0)=
\frac{[(1+c_0)^b-(1-c_0)^b]^2}{(1-c_0)^b}.
```

The [finite converse](collective_converse.md) permits arbitrary joint measurements within blocks and unequal preplanned block sizes. Estimation to accuracy $`\epsilon<c_0`$ over a domain containing both $`\pm c_0`$ inherits the bound.

Conversely, at confidence failure $`0<\delta\leq1/3`$, a block experiment of actual size $`r\leq b`$ and randomized GHZ measurement attains uniform accuracy $`\epsilon`$ using

```math
N\leq
C_q\left[
r\epsilon^{-2}\beta_r^{-n}\log\frac1\delta
+\log\frac n\delta+r
\right]
```

for a finite constant $`C_q`$ depending only on $`q`$ in the stated accuracy/confidence range. The [protocol](attaining_measurements.md) supplies explicit integer choices and counts failed coverage events, rejected records and all specimens. Its useful-record probability lies between $`\beta_r^n/2`$ and $`\beta_r^n`$.

The finite prefactor $`A_b(c_0)`$ grows exponentially in $`b`$. Thus these bounds do not identify every finite optimum or the exact polynomial exponent at the transition. They do determine the following laws.

## Fixed blocks: the exponential base matches

For every fixed $`b\geq1`$, $`q\in(0,1)`$, nonzero contrast and constant confidence, sign testing has

```math
N_{\min}(n;b,q,c_0)
=\Theta_{b,q,c_0}\left(\beta_b^{-n}\right).
```

The same exponential order holds for fixed-accuracy estimation on a fixed symmetric contrast interval containing the testing pair. Constants may depend on the fixed parameters. Source preparation, measurement implementation and classical processing are additional costs; this is a specimen law.

The matching base uses the GHZ stabilizer measurement on a single payload inside each block. A simpler product-basis guess has success probability $`[1-2t_b/3]^n`$ and also gives an exponential upper, but it misses this sharper base. No joint entanglement of different payload copies is needed by the attaining construction, although the lower allows it.

## Growing blocks: an if-and-only-if criterion

For fixed $`q,c_{\max},\epsilon,\delta`$ as in the model and an integer cap sequence $`b=b(n)\geq1`$, a uniform polynomial specimen budget is possible **if and only if**

```math
n(1-q)^{b(n)}=O(\log n).
```

Here a polynomial budget means that one finite exponent and constant bound the necessary budget for all sufficiently large $`n`$. It does not require an oscillating sequence to have a limiting exponent.

For sufficiency, write $`\ell=-\log(1-q)>0`$ and choose

```math
r=\min\left\{b,\max\left(1,\left\lceil\frac{\log n}{\ell}\right\rceil\right)\right\}.
```

If the cap is smaller, the assumed criterion controls $`nt_r`$. If it is larger, the chosen block already has $`nt_r\leq1`$ for $`n\geq2`$. Therefore $`r=O_q(\log n)`$ and

```math
-n\log\beta_r
\leq\frac{nt_r}{3-t_r}
\leq\frac{nt_r}{2}
=O(\log n).
```

The protocol budget is polynomial. A large cap need not be filled with unnecessary specimens.

For necessity, suppose the criterion fails. Along a subsequence, $`w_n/\log n\to\infty`$, and eventually $`b\leq\log n/\ell`$. The finite lower gives

```math
\log N
\geq
\frac{w_n}{3}-\kappa(c_0)b
+\log\bigl(2b(1-2\eta)^2\bigr),
\qquad
\kappa(c_0)=2\log(1+c_0)-\log(1-c_0).
```

Dividing by $`\log n`$ diverges on that subsequence. No uniform polynomial budget can succeed. The $`b`$-dependent finite loss is harmless for this conclusion because $`b`$ is at most logarithmic precisely on the potentially difficult subsequence.

Equivalently, polynomial feasibility requires a constant $`C`$ such that, for all sufficiently large $`n`$,

```math
b(n)\geq
\frac{\log n-\log\log n-C}{-\log(1-q)}.
```

The constant determines the allowed polynomial degree. This is an asymptotic feasibility boundary, not an assertion that the right side is an exact minimum integer at finite size.

## Three regimes

| Batch scale | Residual instructions | Consequence at fixed accuracy |
|---|---|---|
| Fixed $`b`$ | $`\Theta(n)`$ | Exponential specimens with matching base $`\beta_b^{-n}`$ |
| $`b=\alpha\log n/\ell+O(1)`$, fixed $`0<\alpha<1`$ | $`\Theta(n^{1-\alpha})`$ | Stretched-exponential specimens, $`\log N=\Theta(n^{1-\alpha})`$ |
| $`b\geq(\log n-\log\log n-C)/\ell`$ | $`O(\log n)`$ | Polynomial specimens |

For the second row, bounded integer rounding changes $`t_b`$ by a constant factor. It must not be discarded when stating a leading exponent coefficient. The finite bounds are the authoritative statements.

With a cap allowing $`r=\lceil\log(6n)/\ell\rceil+O(\epsilon^{-2})`$, one internally adaptive joint experiment can perform the local locate-then-measure procedure, using only logarithmically many specimens at fixed accuracy. Using $`r=O(\log n)`$ with $`nt_r=O(1)`$, the GHZ protocol also has logarithmic total cost. Polynomial feasibility can begin earlier, at residual uncertainty of logarithmic order.

## What feedback changes

An adaptive local learner first reads enough markers to recover the entire word, then changes its payload measurement. It uses

```math
O_q\left(\log\frac n\delta+
\epsilon^{-2}\log\frac1\delta\right)
```

specimens and stores only classical information between specimens. The same old record would be perfectly available for final decoding in the nonadaptive benchmark; what it cannot do there is orient a future block's measurement.

This distinction is the physical interpretation of the boundary. The result quantifies specimen grouping and control between experiments. It does not prove a minimum number of coherent qubits, a storage lifetime, an entanglement requirement for the upper, or a hardware training speedup. See [resources](resources.md) and [related work](../references/RELATED_WORK.md) for the remaining assumptions and the inherited adaptivity mechanism.
