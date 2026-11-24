# What the learning task costs

The result compares specimen budgets for one scalar learning task. It charges every source specimen and limits which specimens may participate in one experiment. It does not establish an optimal coherent-width, memory-lifetime, circuit-depth, heat, or end-to-end training-time law.

The source and experiment classes are specified in the [model](model.md). Explicit finite costs and the decoding guarantee are proved in [attaining measurements](attaining_measurements.md).


The tables below follow the erasure protocol. For noisy markers, the receiver additionally computes or precomputes an omission rule and allocates a separate set of marker observations for final word identification. The [general protocol](noisy-markers.md#measuring-with-two-retained-axes-at-every-site) charges both that allocation and every rejected block.

## Supplied information and charged specimens

The learner knows $`n`$, the erasure probability $`q\in(0,1)`$, the source family, the allowed block cap $`b`$, the accuracy $`\epsilon`$, and the failure probability $`\delta`$. It does not know the fixed hidden axis word $`a`$ or the contrast $`c`$. Markers reveal axes only through the stated independent erasure channel. A classical description of the source's hidden word is not supplied.

One specimen contains an $`n`$-qubit payload and $`n`$ four-level classical markers. Encoding each marker in two computational-basis qubits uses $`3n`$ physical qubits per specimen. The unused symbol capacity of this encoding supplies no extra oracle or retained advice. Equivalently, the marker can be a native classical four-symbol register; the scientific bounds are the same.

For a working block size $`r\le b`$ and $`T`$ blocks, the deterministic specimen charge is

```math
N=rT.
```

All $`r`$ specimens of each block are counted, even though the attaining protocol uses just one of their payloads. Erasures, unsuccessful coverage, rejected records, and marker-recovery failures do not reduce the charge. The output is one estimate $`\widehat c`$; offline acceptance filters classical records and does not herald a recovered quantum state.

The model supplies native specimens, rather than a preparation circuit or a query oracle. It supplies no QRAM, coherent data-loading routine, state-preparation unitary, controlled unknown preparation, inverse preparation, or quantum access to the source's hidden classical description.

## A source can generate the family with linear work

A source that holds its own hidden $`a,c`$ can prepare a specimen with $`O(n)`$ elementary operations and classical random choices. Draw $`n-1`$ independent signs. Draw a parity sign with mean $`c`$, and choose the final sign to make their full product equal that parity. At site $`i`$, prepare the corresponding eigenstate of the axis $`a_i`$. Averaging these product eigenstates gives

```math
2^{-n}(I+cP_a).
```

Independently emit each marker as the appropriate axis symbol with probability $`q`$ and as an erasure otherwise. This construction shows that the source family requires neither entangled inputs nor an exponentially long classical data table. The hidden description belongs to the source, not to either learner. The ideal model assumes its stated sampling law; it does not price an experimental calibration procedure for $`q`$ or the source's preparation error.

## Operations in the attaining block protocol

For each block, read all markers, retain their revealed-axis union, and use one payload. If $`K`$ axes remain unresolved, measure the known-axis payload sites locally and measure the unresolved sites in an independently randomized local-Clifford GHZ basis. Reading the block's own markers before choosing its own payload setting is explicitly permitted.

| Resource | Explicit attaining cost |
|---|---|
| Source specimens | $`N=rT`$, including every unused payload and every rejected record. |
| Marker readout and processing | $`O(nr)`$ local symbol operations per block; $`O(nN)`$ in total. |
| Payload readout | One $`n`$-qubit payload per block, with $`n`$ binary outcomes. |
| Known single-qubit gates | $`O(n)`$ Clifford gates per measured payload. |
| Entangling gates | At most $`K-1`$ CNOTs for the GHZ basis when $`K\ge1`$; $`O(nT)`$ in total under all-to-all connectivity. |
| Classical randomness | $`O(n)`$ random Clifford choices per block. |
| Final marker recovery and filtering | $`O(nN)`$ classical operations for a direct implementation, including $`O(nT)`$ coverage checks and sign decodings. |
| Stored classical record | $`O(n)`$ bits per block after marker compression, or $`O(nT)`$ bits for a direct full-record implementation. |
| Quantum output | None; the payload is measured and the output is one scalar. |

The GHZ stabilizer membership check is linear in $`K`$. In its standard frame, a full-support Pauli is covered when it is an even-$`Y`$ $`X/Y`$ word, or the all-$`Z`$ word at even $`K`$. Local Clifford signs and the product of the relevant generator outcomes determine its eigenvalue. No exponentially large stabilizer table is required.

The gate count assumes all-to-all connectivity. A prescribed geometric architecture would require its own routing, depth, and noise account. Single-qubit Clifford changes and the GHZ basis can be implemented exactly in an ideal Clifford gate set; no precision-dependent arbitrary rotation is needed by the receiver's measurement.

The product-guess alternative uses only local payload measurements and removes the GHZ CNOTs. Its acceptance probability is smaller, so it generally uses more specimens. It already reaches the same polynomial-feasibility boundary; GHZ improves the exponential coverage factor.

## Block cardinality is not simultaneous coherent width

The cap $`b`$ is the number of source copies allowed to participate in each preplanned joint experiment. The converse permits every POVM on those copies, including inter-copy entanglement and arbitrary fresh ancillas. It places no gate-efficiency restriction on such a POVM. No quantum carrier or entangled ancilla persists from one block into the next, and earlier block outcomes do not control later block measurements.

The attaining protocol needs less quantum control than this benchmark allows. It may process the first $`r-1`$ specimens' classical markers sequentially, discard their payloads, and use the final specimen's payload after reading its marker. Only classical records persist between those arrivals. The GHZ version entangles qubits within that final payload and never entangles distinct source copies. Alternatively, one may retain a payload while reading the other markers; that implementation has an additional storage-duration cost that is unnecessary for the stated upper.

Thus a logarithmic block threshold is not a theorem requiring logarithmically many simultaneous coherent copies. It quantifies how much input pooling in a preplanned experiment compensates for the absence of feedback between experiments. Allowing all accumulated marker outcomes to control every later payload measurement changes the benchmark and gives the adaptive local protocol.

## Complete finite specimen cost

Write

```math
t_r=(1-q)^r,\qquad
\beta_r=1-\frac{t_r}{3},\qquad
\lambda=-\ln(1-q).
```

The randomized GHZ protocol accepts a block with exact probability

```math
p_r=\frac12\left[
\beta_r^n+
\left(1-\frac{2t_r}{3}\right)^n+
\left(1-\frac{4t_r}{3}\right)^n-
(1-t_r)^n\right],
\qquad
\frac12\beta_r^n\le p_r\le\beta_r^n.
```

The explicit block count in the attaining proof charges global marker recovery, a binomial accepted-count failure, and the estimation error separately. It gives

```math
N=O\left(
r\epsilon^{-2}\beta_r^{-n}\ln\frac1\delta
+\lambda^{-1}\ln\frac n\delta+r
\right).
```

The full $`N`$, rather than only the accepted $`Tp_r`$ payload records, is the specimen cost. At fixed $`q,\epsilon,\delta`$ and fixed $`r`$, $`\beta_r^{-n}`$ is the governing exponential factor. The arbitrary-block lower has the same exponential factor up to a contrast-dependent factor exponential in $`r`$, which is constant for fixed $`r`$ and polynomial when $`r=O(\log n)`$.

An allowed cap larger than necessary is not a requirement to acquire larger blocks. For example, use

```math
r=\min\left\{b,
\left\lceil\lambda^{-1}\ln\frac{6n}{\delta}\right\rceil
\right\}.
```

At fixed confidence and accuracy this caps the actual working block at order $`\log n`$. For the signed task at fixed $`q`$ and fixed nonzero accuracy, polynomial specimen cost is possible exactly when

```math
n(1-q)^{b(n)}=O(\log n).
```

This is a specimen-feasibility statement with unrestricted classical computation in the converse. It does not claim the exact optimal polynomial degree, exact finite constants, or optimal processing time.

## The feedback implementation

The adaptive protocol reads markers until a predetermined coverage budget is met, stores the recovered axes as classical information, and then changes the local product Pauli measurement used on fresh payloads. With one feedback round it uses

```math
O_q\left(\ln\frac n\delta+
\epsilon^{-2}\ln\frac1\delta\right)
```

specimens, $`O(n)`$ classical working bits for the axes and running statistics, and no coherent carrier between specimens. It needs no entangling receiver gates. Its advantage is against the stated preplanned block model; it is not a separation from every classical-data algorithm or an end-to-end quantum training-speedup claim.

All receiver operations and storage in this account are ideal. No robustness theorem for faulty markers, receiver noise, finite-temperature memory, source drift, or calibration acquisition is supplied. These are separate physical models, not omitted terms silently treated as zero in a noisy implementation claim.
