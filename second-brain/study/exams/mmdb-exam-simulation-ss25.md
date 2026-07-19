---
title: "MMDB Exam Simulation — Based on SS25 Klausur"
tags: [exam-prep, multimedia-databases, semester-1, simulation]
course: "Multimedia Databases"
exam_date: "2026-07-21"
status: current
last_updated: 2026-07-18
prerequisites: []
---

> **Format:** Based on the actual SS25 exam (90 min, calculator allowed).
> **Source:** Last semester's exam syllabus transcribed from memory.
> **Strategy:** Work through each question under timed conditions. Check solutions only after attempting.

---

## Question 1 — Single-Choice Questions (8 pts)

Answer each sub-question with exactly one choice.

**1.1** Which color model is subtractive?
- (a) RGB
- (b) CMYK
- (c) HSV
- (d) YCbCr

**1.2** In the JPEG pipeline, which step is responsible for the actual information loss?
- (a) DCT transform
- (b) Level-shift by subtracting 128
- (c) Quantization
- (d) Zig-zag scan

**1.3** What does the Nyquist-Shannon sampling theorem state?
- (a) Sampling rate must equal the signal frequency
- (b) Sampling rate must be at least twice the highest frequency component
- (c) Sampling rate must be at least half the signal bandwidth
- (d) Sampling rate is irrelevant for digital reconstruction

**1.4** Which R-tree variant uses bounding circles instead of rectangles?
- (a) R+
- (b) R*
- (c) SS-tree
- (d) X-tree

**1.5** What is the main advantage of error-diffusion dithering over ordered-pattern dithering?
- (a) It is computationally cheaper
- (b) It produces fewer visible repeating patterns
- (c) It increases the number of available colors
- (d) It works only on grayscale images

**1.6** In Huffman coding, which property guarantees unique decodability?
- (a) Fixed-length codes
- (b) Prefix-free property
- (c) Alphabetical ordering of symbols
- (d) Equal probability of all symbols

**1.7** What does chroma subsampling 4:2:0 mean?
- (a) Full chroma resolution in both directions
- (b) Half horizontal chroma, full vertical chroma
- (c) Quarter chroma resolution in both directions
- (d) No chroma information at all

**1.8** Which of the following is a lossless compression method?
- (a) DCT
- (b) Quantization
- (c) Run-Length Encoding
- (d) Chroma subsampling

> [!success]- Solutions — Q1
> **1.1** (b) CMYK — subtractive model where inks absorb light.
> **1.2** (c) Quantization — dividing by the quantization table and rounding discards precision permanently.
> **1.3** (b) Sampling rate ≥ 2 × f_max to avoid aliasing.
> **1.4** (c) SS-tree uses bounding circles; SR-tree uses the intersection of circle and rectangle.
> **1.5** (b) Error diffusion distributes quantization error to neighbors, avoiding the visible tiling patterns of ordered dithering.
> **1.6** (b) Prefix-free property: no codeword is a prefix of another, so the decoder never has ambiguity.
> **1.7** (c) 4:2:0 means half chroma in both horizontal and vertical directions (1 chroma sample per 2×2 luma block).
> **1.8** (c) RLE is lossless — it perfectly reconstructs the original data. DCT, quantization, and chroma subsampling all discard information.

---

## Question 2 — RNN Training Problem (4 pts)

Briefly state a well-known problem in training Recurrent Neural Networks (RNNs) and name one specific architecture or technique that mitigates it.

> [!success]- Solution — Q2
> **Problem:** Vanishing gradients — during backpropagation through time (BPTT), gradients are repeatedly multiplied by small values (sigmoid/tanh derivatives < 1), causing them to shrink exponentially. The early time steps receive near-zero gradients, so the network cannot learn long-range dependencies.
>
> **Mitigation:** Long Short-Term Memory (LSTM) networks use a cell state with additive updates (not multiplicative) controlled by three gates (forget, input, output). The forget gate lets the cell state carry information forward across many time steps without vanishing. Gated Recurrent Units (GRU) are a simpler alternative with similar properties.

---

## Question 3 — Compression Step Identification (5 pts)

A multimedia compression pipeline consists of the following steps:

| Step | Description |
|------|-------------|
| A | Color space conversion (RGB → YCbCr) |
| B | Chroma subsampling (4:2:0) |
| C | Forward DCT on 8×8 blocks |
| D | Quantization using a quality table |
| E | Zig-zag scan |
| F | Run-length encoding |
| G | Huffman coding |

(a) Which step **primarily** reduces the precision of the data (i.e., is the main source of information loss)?

(b) For each of the remaining steps, state in one sentence what it achieves.

> [!success]- Solution — Q3
> **(a)** Step D — **Quantization**. Dividing DCT coefficients by the quantization table entries and rounding to integers permanently discards information. Higher-frequency coefficients are quantized more aggressively (larger divisor), producing many zeros. This is the only irreversible step in the pipeline.
>
> **(b)**
> - **A (Color space conversion):** Separates luminance from chrominance, enabling perceptually-guided compression because the eye is less sensitive to color detail than brightness.
> - **B (Chroma subsampling):** Reduces color resolution by keeping only 1 chroma sample per 2×2 luma block, cutting chroma data by ~75% with minimal visible quality loss.
> - **C (Forward DCT):** Converts spatial pixel values into frequency coefficients, concentrating energy in the top-left (low-frequency) coefficients so most high-frequency coefficients can be discarded.
> - **E (Zig-zag scan):** Reorders the 8×8 coefficient block into a 1D sequence that groups low-frequency coefficients first and high-frequency coefficients last, creating long runs of zeros.
> - **F (RLE):** Compresses the long runs of zero-valued high-frequency coefficients produced by quantization and zig-zag scanning.
> - **G (Huffman coding):** Assigns short codes to frequent symbols and long codes to rare symbols, achieving lossless compression of the quantized, RLE-encoded data.

---

## Question 4 — Huffman Tree Construction (8 pts)

Given the following symbol frequencies:

| Symbol | Frequency |
|--------|-----------|
| A      | 45        |
| B      | 13        |
| C      | 12        |
| D      | 16        |
| E      | 9         |
| F      | 5         |

(a) Build the Huffman tree. Show each merge step.

(b) Derive the Huffman code for each symbol.

(c) Compute the total expected code length (average bits per symbol).

(d) Compute the entropy H of this source. How close is the Huffman code to the entropy bound?

> [!success]- Solution — Q4
> **(a) Merge steps:**
> 1. Merge F(5) + E(9) = 14 → internal node [FE]
> 2. Merge C(12) + B(13) = 25 → internal node [CB]
> 3. Merge [FE](14) + D(16) = 30 → internal node [FED]
> 4. Merge [CB](25) + [FED](30) = 55 → internal node [CBFED]
> 5. Merge A(45) + [CBFED](55) = 100 → root
>
> **(b) Huffman codes** (assigning 0=left, 1=right at each merge):
>
> | Symbol | Code | Bits |
> |--------|------|------|
> | A      | 0    | 1    |
> | B      | 100  | 3    |
> | C      | 101  | 3    |
> | D      | 110  | 3    |
> | E      | 1110 | 4    |
> | F      | 1111 | 4    |
>
> **(c) Average code length:**
> Total symbols = 45 + 13 + 12 + 16 + 9 + 5 = 100
>
> L = (45×1 + 13×3 + 12×3 + 16×3 + 9×4 + 5×4) / 100
>   = (45 + 39 + 36 + 48 + 36 + 20) / 100
>   = 224 / 100 = **2.24 bits/symbol**
>
> **(d) Entropy:**
> p(A)=0.45, p(B)=0.13, p(C)=0.12, p(D)=0.16, p(E)=0.09, p(F)=0.05
>
> H = −(0.45·log₂0.45 + 0.13·log₂0.13 + 0.12·log₂0.12 + 0.16·log₂0.16 + 0.09·log₂0.09 + 0.05·log₂0.05)
>   = −(0.45×(−1.152) + 0.13×(−2.943) + 0.12×(−3.059) + 0.16×(−2.644) + 0.09×(−3.474) + 0.05×(−4.322))
>   = 0.518 + 0.383 + 0.367 + 0.423 + 0.313 + 0.216
>   = **2.220 bits/symbol**
>
> The Huffman code (2.24) is very close to the entropy bound (2.22), within 0.02 bits/symbol. Huffman coding is optimal among prefix-free integer-length codes.

---

## Question 5 — Curve Drawing (4 pts)

Draw the **characteristic curve of median-cut color quantization** as applied to a 24-bit RGB image being reduced to a k-color palette. Specifically:

- X-axis: number of palette colors k (from 1 to 256)
- Y-axis: quantization error (mean squared error)
- Mark the point where increasing k stops yielding significant error reduction for a typical photograph

Label the axes and annotate the "knee" of the curve.

> [!success]- Solution — Q5
> The curve is a **monotonically decreasing convex function**:
>
> - At k=1: maximum error (all pixels mapped to one color — the average of the entire image)
> - As k increases from 1→16: error drops steeply (each additional color captures a major cluster in color space)
> - At k≈32–64: the curve bends (the "knee") — most perceptually distinct color regions are now represented
> - At k>64: diminishing returns — the curve flattens, additional colors only refine subtle gradients
> - At k=256: near-zero error for most natural images
>
> The knee is typically around k=32–64 for photographs. Beyond this point, the human eye cannot distinguish the improvement. For images with fewer distinct color regions (graphics, logos), the knee comes earlier.
>
> Key shape: steep drop → bend → flat. Not linear, not exponential — it's a convex decay that reflects the diminishing marginal value of each additional palette entry.

---

## Question 6 — CMY to CMYK Conversion (4 pts)

A printer receives the following CMY values for a pixel:

| C    | M    | Y    |
|------|------|------|
| 0.20 | 0.35 | 0.50 |

Compute the corresponding CMYK values using the standard undercolor removal method. Show your work.

> [!success]- Solution — Q6
> **Step 1:** Find K = min(C, M, Y) = min(0.20, 0.35, 0.50) = **0.20**
>
> **Step 2:** Adjust CMY values:
> - C' = (C − K) / (1 − K) = (0.20 − 0.20) / (1 − 0.20) = 0.00 / 0.80 = **0.00**
> - M' = (M − K) / (1 − K) = (0.35 − 0.20) / (1 − 0.20) = 0.15 / 0.80 = **0.1875**
> - Y' = (Y − K) / (1 − K) = (0.50 − 0.20) / (1 − 0.20) = 0.30 / 0.80 = **0.375**
>
> **Result:**
>
> | C'   | M'     | Y'     | K    |
> |------|--------|--------|------|
> | 0.00 | 0.1875 | 0.375  | 0.20 |

---

## Question 7 — RLE and Zig-Zag Ordering (6 pts)

**(a)** Apply Run-Length Encoding to the following coefficient sequence (obtained after quantization and zig-zag scan of an 8×8 DCT block). Use the convention: encode each run of zeros as `(run_length, value)` for non-zero values, and `(0, 0)` for the end-of-block marker.

```
57, 0, 0, 0, -3, 0, 0, -1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
```
(64 values total — an 8×8 block has 64 coefficients)

**(b)** Explain why zig-zag scanning helps RLE achieve better compression on DCT coefficients.

> [!success]- Solution — Q7
> **(a) RLE encoding:**
>
> | Run-length | Value |
> |------------|-------|
> | 0          | 57    |
> | 3          | −3    |
> | 2          | −1    |
> | 5          | 2     |
> | 0          | 0     | ← end of block (remaining 53 zeros are implicitly EOB)
>
> Total: 5 (run, value) pairs instead of 64 numbers.
>
> **(b)** Zig-zag scanning reads the 8×8 block in a diagonal pattern starting from the top-left (DC) coefficient and moving toward the bottom-right (highest frequency). Because DCT concentrates energy in the low-frequency coefficients (top-left), quantization produces many zeros in the high-frequency coefficients (bottom-right). Zig-zag scanning groups these zero-valued high-frequency coefficients **consecutively** at the end of the 1D sequence, creating long runs of zeros that RLE compresses very efficiently. A row-by-row scan would interleave low and high frequency coefficients, breaking up the zero runs.

---

## Question 8 — Compression Concept Explanations (6 pts)

Explain each of the following concepts in the context of image/video compression. Two sentences each.

**(a)** Chroma subsampling

**(b)** Quantization

**(c)** Discrete Cosine Transform (DCT)

> [!success]- Solution — Q8
> **(a) Chroma subsampling:** After converting from RGB to YCbCr, the human eye's lower sensitivity to color (chrominance) than brightness (luminance) is exploited by storing fewer Cb/Cr samples than Y samples. In 4:2:0 format, one chroma sample is shared across each 2×2 block of luminance samples, cutting chroma data by 75% with minimal visible quality loss.
>
> **(b) Quantization:** Each DCT coefficient is divided by the corresponding entry in a quantization table and rounded to the nearest integer, with higher-frequency coefficients using larger divisors. This is the step that actually discards information — it is the sole source of lossy-ness in JPEG, and the quality setting controls the quantization table entries.
>
> **(c) Discrete Cosine Transform (DCT):** The DCT converts each 8×8 block of pixel values from the spatial domain into the frequency domain, producing coefficients that represent how much of each frequency is present in the block. Because natural images have most of their energy in low frequencies, the top-left (low-frequency) coefficients are large while the bottom-right (high-frequency) coefficients are small and can be aggressively quantized to zero.

---

## Question 9 — DCT Computation (10 pts)

Given the following 4×4 pixel block (already level-shifted by subtracting 128):

```
  f(x,y) =
  ┌          ┐
  │  2   0   0   2 │
  │  0   0   0   0 │
  │  0   0   0   0 │
  │  2   0   0   2 │
  └          ┘
```

**(a)** Compute the 1D DCT of the first row [2, 0, 0, 2] using N=4.

The 1D DCT formula:
```
S(u) = c(u) × Σₓ₌₀³ f(x) × cos((2x+1)uπ / 8)
where c(0) = 1/√2, c(u) = 1 for u > 0, N = 4, denominator = 2N = 8
```

**(b)** Without computing all values, explain what the 2D DCT of this entire block will look like and why.

> [!success]- Solution — Q9
> **(a) 1D DCT of [2, 0, 0, 2], N=4:**
>
> **S(0):** c(0) × [2·cos(0) + 0 + 0 + 2·cos(0)]
> = (1/√2) × [2 + 0 + 0 + 2] = (1/√2) × 4 = **2√2 ≈ 2.83**
>
> **S(1):** 1 × [2·cos(π/8) + 0 + 0 + 2·cos(7π/8)]
> = 2·cos(π/8) + 2·cos(7π/8)
> = 2·cos(22.5°) + 2·cos(157.5°)
> = 2·(0.924) + 2·(−0.924) = 1.848 − 1.848 = **0**
>
> **S(2):** 1 × [2·cos(2π/8) + 0 + 0 + 2·cos(14π/8)]
> = 2·cos(π/4) + 2·cos(7π/4)
> = 2·(√2/2) + 2·(√2/2) = √2 + √2 = **2√2 ≈ 2.83**
>
> **S(3):** 1 × [2·cos(3π/8) + 0 + 0 + 2·cos(21π/8)]
> = 2·cos(67.5°) + 2·cos(3π/8 + 2π) = 2·cos(3π/8) + 2·cos(5π/8)
> = 2·(0.383) + 2·(−0.383) = **0**
>
> **Result: S = [2.83, 0, 2.83, 0]**
>
> **(b)** The block has a checkerboard pattern (non-zero at corners, zero in between). The 2D DCT will concentrate all energy into the DC coefficient S(0,0) and the highest-frequency coefficient S(2,2), with all other coefficients being zero. This is because a checkerboard is a pure high-frequency pattern in both dimensions — the DCT perfectly separates this into its two frequency components. After quantization, S(2,2) will likely be rounded to zero as well, leaving only the DC term (average pixel value).

---

## Question 10 — Median-Cut Color Quantization (6 pts)

**(a)** Define median-cut color quantization in your own words.

**(b)** State one advantage of median-cut compared to uniform quantization for color palette generation.

**(c)** Describe step by step how the color space is recursively split in median-cut until the target palette size k is reached.

> [!success]- Solution — Q10
> **(a)** Median-cut is a color quantization algorithm that recursively subdivides the color space (represented as a 3D RGB histogram) into smaller regions, each containing approximately the same number of pixels. At each step, the region with the largest range along any color axis is split at the median pixel value along that axis. After k−1 splits, k regions exist; the average color of each region becomes a palette entry.
>
> **(b)** Median-cut adapts to the actual distribution of colors in the image. Uniform quantization divides each axis into equal intervals regardless of where the pixels actually cluster, wasting palette entries on empty regions. Median-cut concentrates palette entries where the image has the most colors, producing lower quantization error for the same palette size.
>
> **(c) Recursive splitting:**
> 1. Start with one box containing all pixels in RGB space.
> 2. Find the box with the longest side (largest range in R, G, or B).
> 3. Sort the pixels in that box along the longest axis.
> 4. Split at the median: half the pixels go into the lower box, half into the upper box.
> 5. Repeat from step 2 until k boxes exist.
> 6. The representative color for each box is the mean of all pixels in that box.

---

## Question 11 — R-Tree Considerations (4 pts)

List two important considerations for the **insertion** and **deletion** operations in an R-tree. For each, explain what problem it addresses.

> [!success]- Solution — Q11
> **Insertion — Choosing the right leaf node:**
> When inserting a new object, the algorithm must decide which leaf node (and thus which MBR) should contain it. The standard approach picks the leaf whose MBR needs the least enlargement to accommodate the new object. If two MBRs need equal enlargement, the one with the smaller area is chosen. This minimizes MBR overlap over time, which is critical for search efficiency.
>
> **Insertion — Handling overflow (node split):**
> When a leaf node is full, it must be split into two nodes. The split strategy matters enormously: a bad split creates overlapping MBRs that degrade future searches. The R* tree improves on the standard split by choosing the split axis and position that minimize the sum of MBR perimeters (and thus overlap).
>
> **Deletion — Handling underflow:**
> When a deletion causes a node to fall below the minimum occupancy, the node's entries must be reinserted into the tree (typically by re-adding them from the root). This prevents chronically underfull nodes that waste space and degrade search performance.
>
> **Deletion — MBR shrinking:**
> After removing an object, the parent MBR may be larger than necessary. The MBR should be recomputed to tightly fit the remaining children. However, some implementations skip this for performance, accepting slightly loose MBRs.

---

## Question 12 — R-Tree Operations (10 pts)

Given an R-tree with max capacity M=3 entries per node and minimum m=2. The tree currently contains rectangles A through G arranged as follows:

```
          Root
        /   |   \
      N1    N2   N3
     / \   / \    |
    A  B  C  D   E F G
```

MBRs:
- N1: [0,4] × [0,4] (contains A at [0,2]×[0,2], B at [2,4]×[2,4])
- N2: [5,9] × [0,6] (contains C at [5,7]×[0,2], D at [7,9]×[3,6])
- N3: [3,8] × [7,9] (contains E at [3,5]×[7,8], F at [5,7]×[8,9], G at [6,8]×[7,8])

**(a)** Insert rectangle H at position [1,3] × [1,3]. Which leaf node does H go into? Explain your reasoning.

**(b)** What happens if N1 overflows after the insertion? Describe the split procedure.

**(c)** Now delete rectangle F from N3. Does this cause underflow? If so, what happens?

> [!success]- Solution — Q12
> **(a)** H = [1,3]×[1,3] overlaps with N1's MBR [0,4]×[0,4]. We check which leaf's MBR needs the least enlargement to contain H.
> - N1 [0,4]×[0,4]: already contains H, enlargement = 0
> - N2 [5,9]×[0,6]: would need to extend left to x=1, enlargement > 0
> - N3 [3,8]×[7,9]: would need to extend down to y=1, enlargement > 0
>
> H goes into **N1** because its MBR already contains H with zero enlargement.
>
> **(b)** N1 now has 4 entries (A, B, H, and itself would need to accommodate the new MBR). Since M=3, N1 overflows.
>
> Split procedure:
> 1. **Choose split axis:** For each axis (x, y), sort entries by lower bound, try all possible split points, compute the sum of MBR perimeters. Pick the axis with minimum total perimeter.
> 2. **Choose split position:** On the chosen axis, find the split that minimizes the sum of perimeters of the two resulting MBRs.
> 3. **Distribute entries:** Assign entries to the two new nodes based on the chosen split. For example, if the x-axis split is chosen at x=2.5: N1a gets {A, H} (lower x), N1b gets {B} (higher x). But B alone is below m=2, so the split might instead be {A, H} and {B} with reassignment to ensure minimum occupancy.
> 4. **Update parent:** The root now has entries for N1a, N1b, N2, N3 (4 entries). If the root also overflows (M=3), it splits too, creating a new root.
>
> **(c)** N3 originally has 3 entries (E, F, G). After deleting F, N3 has 2 entries (E, G), which equals m=2. **No underflow occurs** — the minimum occupancy is met.
>
> The MBR of N3 should be recomputed to tightly fit E [3,5]×[7,8] and G [6,8]×[7,8], giving a new MBR of [3,8]×[7,8] (slightly smaller than before since F at [5,7]×[8,9] no longer extends to y=9).

---

## Question 13 — SQL Type Hierarchy (6 pts)

Write the SQL CREATE statements to define a type hierarchy for a multimedia database with the following requirements:

- A base type `MediaType` with attributes: `id INTEGER`, `name VARCHAR(100)`, `format VARCHAR(20)`, `size_bytes BIGINT`
- A subtype `ImageType` that inherits from `MediaType` and adds: `width INTEGER`, `height INTEGER`, `color_depth INTEGER`
- A subtype `VideoType` that inherits from `MediaType` and adds: `duration_sec INTEGER`, `fps DECIMAL(5,2)`, `codec VARCHAR(30)`
- A table `media_library` that stores objects of type `MediaType` (including subtypes)

> [!success]- Solution — Q13
> ```sql
> -- Base type
> CREATE TYPE MediaType AS (
>     id          INTEGER,
>     name        VARCHAR(100),
>     format      VARCHAR(20),
>     size_bytes  BIGINT
> );
>
> -- Subtype for images (inherits all MediaType attributes)
> CREATE TYPE ImageType UNDER MediaType (
>     width       INTEGER,
>     height      INTEGER,
>     color_depth INTEGER
> );
>
> -- Subtype for videos (inherits all MediaType attributes)
> CREATE TYPE VideoType UNDER MediaType (
>     duration_sec INTEGER,
>     fps          DECIMAL(5,2),
>     codec        VARCHAR(30)
> );
>
> -- Table that stores any MediaType (including subtypes via polymorphism)
> CREATE TABLE media_library OF MediaType;
> ```
>
> The `UNDER` keyword establishes inheritance. `ImageType` and `VideoType` automatically have all attributes of `MediaType` plus their own. The `media_library` table can store rows of any type in the hierarchy thanks to object-relational polymorphism.

---

## Question 14 — VARRAYs and Nested Tables (6 pts)

**(a)** Explain what VARRAYs and nested tables are in the context of Oracle (or similar object-relational DBMS). For each, describe storage characteristics and when you would choose one over the other.

**(b)** A multimedia database stores images, and each image has a set of feature descriptor vectors. Would you model the feature vectors as a VARRAY or a nested table? Justify your answer.

> [!success]- Solution — Q14
> **(a)**
>
> **VARRAY (Variable-size Array):**
> - Bounded: you declare a maximum number of elements at type creation (e.g., `VARRAY(100)`)
> - Ordered: element position is preserved and index-accessible (`collection(i)`)
> - Stored inline (for small sizes) or as a LOB (for larger declared sizes) — no separate storage table
> - Best when: the maximum size is known upfront, order matters, and you do NOT need to query individual elements with SQL
>
> **Nested Table:**
> - Unbounded: no declared maximum size
> - Stored in a separate system-generated storage table (with a hidden `NESTED_TABLE_ID` foreign key back to the parent row)
> - Supports SQL queries against the collection's contents (`SELECT * FROM TABLE(collection_column)`)
> - Supports set operations (MULTISET, EXCEPT, INTERSECT)
> - Best when: the collection size is unpredictable, you need to query or join on collection elements, or you need set semantics
>
> **(b)** Feature vectors should be modeled as a **nested table** because:
> 1. The number of feature vectors per image varies (not known upfront)
> 2. You will likely need to query feature vectors with SQL (e.g., find all images with a feature vector matching a certain pattern, or join feature vectors with a similarity search)
> 3. Set operations may be useful (e.g., finding images that share feature descriptors)
> 4. A VARRAY would require declaring a maximum number of features, which is arbitrary and limits flexibility

---

## Scoring Guide

| Question | Topic | Points |
|----------|-------|--------|
| Q1 | Single-choice (8 sub-questions) | 8 |
| Q2 | RNN training problem | 4 |
| Q3 | Compression step identification | 5 |
| Q4 | Huffman tree construction | 8 |
| Q5 | Curve drawing | 4 |
| Q6 | CMY to CMYK conversion | 4 |
| Q7 | RLE and zig-zag | 6 |
| Q8 | Compression concept explanations | 6 |
| Q9 | DCT computation | 10 |
| Q10 | Median-cut quantization | 6 |
| Q11 | R-tree considerations | 4 |
| Q12 | R-tree operations | 10 |
| Q13 | SQL type hierarchy | 6 |
| Q14 | VARRAYs and nested tables | 6 |
| **Total** | | **87** |

---

## Vault Page References

| Question | Related Vault Pages                                                                                                                                                                                                  |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1       | [[cmyk-color-model]], [[jpeg-compression-pipeline]], [[audio-sampling-nyquist-theorem]], [[r-tree]], [[dithering]], [[entropy-coding-huffman-arithmetic]], [[color-space-conversion-ycbcr]], [[run-length-encoding]] |
| Q2       | (ML/deep learning — not in vault scope, but relevant for multimedia)                                                                                                                                                 |
| Q3       | [[jpeg-compression-pipeline]], [[transform-coding]], [[lossless-vs-lossy-compression]]                                                                                                                               |
| Q4       | [[entropy-coding-huffman-arithmetic]]                                                                                                                                                                                |
| Q5       | [[color-quantization]], [[dithering]]                                                                                                                                                                                |
| Q6       | [[cmyk-color-model]]                                                                                                                                                                                                 |
| Q7       | [[run-length-encoding]], [[jpeg-compression-pipeline]]                                                                                                                                                               |
| Q8       | [[color-space-conversion-ycbcr]], [[transform-coding]], [[jpeg-compression-pipeline]]                                                                                                                                |
| Q9       | [[transform-coding]]                                                                                                                                                                                                 |
| Q10      | [[color-quantization]]                                                                                                                                                                                               |
| Q11      | [[r-tree]]                                                                                                                                                                                                           |
| Q12      | [[r-tree]]                                                                                                                                                                                                           |
| Q13      | [[object-relational-databases]]                                                                                                                                                                                      |
| Q14      | [[nested-tables-vs-varrays]], [[object-relational-databases]]                                                                                                                                                        |

---

## Related Resources

### 📖 Multimedia Databases - Lecture 05: Coding and Compression
- Lecture topic: [[multimedia-databases-lecture-05]]

**Key concepts covered:**
- [[lossless-vs-lossy-compression]]
- [[run-length-encoding]]
- [[entropy-coding-huffman-arithmetic]]
- [[transform-coding]]
- [[jpeg-compression-pipeline]]
- [[mpeg-video-compression]]

### 📖 Multimedia Databases - Lecture 02: Color Models
- Lecture topic: [[multimedia-databases-lecture-02]]

**Key concepts covered:**
- [[cmyk-color-model]]
- [[color-models-overview]]

### 📖 Multimedia Databases - Lecture 06: Modeling
- Lecture topic: [[multimedia-databases-lecture-06]]

**Key concepts covered:**
- [[object-relational-databases]]
- [[nested-tables-vs-varrays]]

### 📖 Multimedia Databases - Lecture 09: Indexing
- Lecture topic: [[multimedia-databases-lecture-09]]

**Key concepts covered:**
- [[r-tree]]
- [[sr-tree]]
