# A complete two-qubit experiment

[Model](model.md) · [Attaining measurements](attaining_measurements.md) · [Scientific overview](README.md)

Take two payload qubits, reveal probability $`q=1/2`$, and a one-specimen block cap. To describe the source concretely, fix its hidden word to $`a=(Y,Z)`$. The learner is not told that word. Its payload is

```math
\sigma_{a,c}=\frac{I+c\,Y\otimes Z}{4}.
```

The source prepares product eigenstates $`|s_Y\rangle\otimes|t_Z\rangle`$ with signs $`s,t\in\{-1,+1\}`$ and probabilities

```math
\Pr(s,t)=\frac{1+cst}{4}.
```

For $`c=1/2`$, the two equal-sign pairs each occur with probability $`3/8`$ and the two unequal-sign pairs each occur with probability $`1/8`$. Each individual qubit is maximally mixed. The full $`Y\otimes Z`$ correlation has mean $`c`$.

Each marker independently either reveals its correct symbol or reports an erasure. Thus a specimen has the following three types of measurement record.

| Unresolved axes $`K`$ | Probability | Allowed payload measurement | Probability its recorded basis covers the true Pauli |
|---|---|---|---|
| $`0`$ | $`1/4`$ | Measure the two revealed local axes | $`1`$ |
| $`1`$ | $`1/2`$ | Measure the known axis; choose a random local Clifford frame on the unknown site | $`1/3`$ |
| $`2`$ | $`1/4`$ | Measure in a randomly locally rotated Bell basis | $`1/3`$ |

The last row is the two-qubit GHZ measurement. The ordinary Bell basis jointly measures the commuting operators $`X\otimes X`$ and $`Z\otimes Z`$. It also determines $`Y\otimes Y`$, because

```math
Y\otimes Y=-(X\otimes X)(Z\otimes Z).
```

If their recorded eigenvalues are $`z_0,z_2`$, the $`Y\otimes Y`$ eigenvalue is $`-z_0z_2`$. This sign is why counting covered axis words alone is insufficient to implement the decoder.

For an example of a covered random frame, take $`C=S\otimes H`$, where $`S=\mathrm{diag}(1,i)`$ and $`H`$ is Hadamard. Then

```math
C(X\otimes X)C^\dagger=Y\otimes Z.
```

Measuring in the rotated Bell basis $`C|\mathrm{Bell}\rangle`$ therefore records the desired correlation through the $`X\otimes X`$ Bell eigenvalue. The actual learner chooses its frames randomly without knowing the word; this particular frame is simply one covered choice. A later marker transcript tells the decoder which recorded frames were covered.

## Decode after collecting all specimens

Repeat the same preplanned block rule. Save the marker values, local Clifford frames and measurement outcomes. The union of all marker records eventually reveals the hidden word. At the end, keep each record exactly when its basis covers the now-known true Pauli, and decode its eigenvalue with the correct sign.

The acceptance probability is exactly

```math
p_1=\frac14\cdot1+
\frac12\cdot\frac13+
\frac14\cdot\frac13
=\frac12.
```

Every accepted decoded sign has distribution $`\Pr(W=w)=(1+wc)/2`$. For $`T`$ specimens, the ideal final decoder supplied the true word would therefore accept a binomial number of records with mean $`T/2`$. The actual decoder agrees with it whenever the full marker transcript recovers both axes. That failure probability is at most $`2\cdot2^{-T}`$.

The [finite guarantee](attaining_measurements.md#a-finite-sample-guarantee) prices this failure event, too few accepted records, and the mean-estimation error separately. All $`T`$ specimens are charged, including every rejected outcome. Nothing about a successful final marker transcript is used to control a later measurement.

Here $`\beta_1=5/6`$. The general coverage bounds give $`25/72\leq p_1\leq25/36`$, consistent with the exact value $`1/2`$. The product-guess alternative would accept with probability $`4/9`$. This small example illustrates the GHZ coverage gain; it does not establish an asymptotic threshold or the optimal finite number of specimens.
