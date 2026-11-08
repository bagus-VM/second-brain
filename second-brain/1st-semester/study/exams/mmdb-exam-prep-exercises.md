---
title: "MMDB Exam Prep — Exercise-Based Mock Exam"
tags: [exam-prep, multimedia-databases, semester-1, practice]
course: "Multimedia Databases"
exam_date: "2026-07-21"
status: current
last_updated: 2026-07-20
prerequisites: []
---

> **Format:** 14 questions, exercise-based, covering all 9 sheets (Ex01–Ex09).
> **Strategy:** The exam is confirmed to be based on the exercise sheets. Every question here is adapted from a real exercise task. Master these and you master the exam.
> **Allowed aids:** Calculator (confirmed).

---

## Question 1 — Signal Processing (Ex01, 6 pts)

**(a)** In the Pulse Code Modulation process, explain the sampling and quantization steps. (2 pts)

**(b)** Given a sine wave with amplitude A = 10V, what is the maximum quantization error if a uniform quantization to 5 bits is applied? Show your work. (2 pts)

**(c)** For the composite signal `f(x) = sin(0.8πx) + sin(1.5πx) + sin(3πx)`, calculate the minimum sampling rate so that no information is lost. State the theorem you are using. (2 pts)

> [!success]- Solution
> **(a)** Sampling: A fixed grid of equally-spaced measuring points is defined on the signal's axis (time for audio, spatial for images). The signal value at each grid point is a "sample." The sampling rate determines how accurately the original signal can be reconstructed.
>
> Quantization: The continuous measured values from sampling are converted to a discrete, countable value range (typically binary). The number of bits per sample determines the resolution/accuracy.
>
> **(b)** Range Δx = 10 - (-10) = 20V. For N=5 bits: Q = Δx / (2^N × 2) = 20 / 64 = **0.3125 V**
>
> **(c)** Nyquist-Shannon theorem: sampling rate f_s must be > 2 × f_g (highest frequency component).
> - f1 = 0.4 Hz, f2 = 0.75 Hz, f3 = 1.5 Hz
> - f_s > 2 × 1.5 = **f_s > 3 Hz**

---

## Question 2 — Structured vs. Unstructured Data (Ex01 + Ex02, 5 pts)

**(a)** What are the characteristics of structured, unstructured, and semi-structured data? Give one example for each. (3 pts)

**(b)** What are the effects of such data on databases and their query properties? (2 pts)

> [!success]- Solution
> **(a)**
> - **Structured:** Predefined schema, quantitative data, fits in fixed fields/columns (e.g. names, addresses). Can be stored in relational DBs with standard SQL querying and exact matching.
> - **Unstructured:** No predefined model (e.g. text, video, audio). Requires metadata for retrieval — if metadata is structured → exact matching; if not → information retrieval methods (fuzzy/similarity-based).
> - **Semi-structured:** Does not obey formal relational structure but contains tags/markers to separate semantic elements (e.g. XML, JSON). Typically queried via XPath or keyword queries.
>
> **(b)**
> - Structured data → relational DB, standard SQL, exact matching
> - Unstructured data → needs metadata, content-based retrieval, similarity comparison
> - Semi-structured data → structured queries (XPath) or keyword queries

---

## Question 3 — Semantic Gap (Ex02, 5 pts)

**(a)** Give examples of "low-level features" and "high-level features" for an image. How would you interpret "bridging the semantic gap"? (3 pts)

**(b)** Identify analogous low-level and high-level features for an audio signal from a phone call recording. (2 pts)

> [!success]- Solution
> **(a)**
> - **Low-level features:** Color histogram, pixel intensity, pixel gradient — easy to extract directly from data, but have no semantics.
> - **High-level features:** "Winter sports", "Person skiing", "snow", "mountain" — more semantics, harder to extract.
> - **Bridging the semantic gap:** The process of mapping low-level features to high-level semantic concepts. Central challenge in MMDB — human perception operates at high semantic level while data is stored at low feature level.
>
> **(b)**
> - **Low-level:** Audio length, bit/sample rate, frequency spectrum, dynamic range, signal-to-noise ratio
> - **High-level:** Speech content, gender of the speaker, physical features of the audio source, emotional connotation

---

## Question 4 — Color Models: RGB ↔ CMYK ↔ HSV (Ex03, 8 pts)

**(a)** What is a color model? What are the two types? (2 pts)

**(b)** Describe the main properties of RGB, CMYK, and HSV. (3 pts)

**(c)** Convert the RGB color (R=0.2, G=0.6, B=0.3) to CMYK and HSV. Show all steps. (3 pts)

> [!success]- Solution
> **(a)** A color model is an abstract method for representing color information using characteristics of human vision. Two types: additive (light produces color) and subtractive (pigments/dyes produce color).
>
> **(b)**
> - **RGB (Additive):** Lights produce colors. Black=(0,0,0), White=(1,1,1). Used in monitors/TVs.
> - **CMYK (Subtractive):** Pigments produce colors. White=(0,0,0), Black=(1,1,1). C=1-R, M=1-G, Y=1-B. K=Key (black) for deeper black. Used in printers.
> - **HSV:** Hue (0-360°), Saturation (0=gray, 1=full color), Value/Brightness (0=black, 1=white). Approximates human perception. HS and B treated separately.
>
> **(c)**
> **CMYK:** C=1-0.2=0.8, M=1-0.6=0.4, Y=1-0.3=0.7, K=min(0.8,0.4,0.7)=0.4
> - C'=(0.8-0.4)/(1-0.4)=0.667, M'=(0.4-0.4)/(1-0.4)=0, Y'=(0.7-0.4)/(1-0.4)=0.5, K=0.4
>
> **HSV:** W=min(0.2,0.6,0.3)=0.2. R'=0, G'=0.4, B'=0.1.
> - Since max=G': H=(B'-R')/(max-min)×60+120 = (0.1/0.4)×60+120 = 144°
> - S=(max-min)/max = 0.4/0.6 = 0.667 = 66.7%
> - V=max = 0.6 = 60%

---

## Question 5 — Metamers and Chromatic Adaptation (Ex03, 4 pts)

**(a)** What are metamers? (2 pts)

**(b)** A white piece of paper appears white under both daylight and incandescent light, despite different irradiance. Explain this phenomenon. (2 pts)

> [!success]- Solution
> **(a)** Metamers are colors that have different spectral power distributions (wavelength compositions) but are perceived as identical by the human eye due to the trichromatic nature of vision. Types include light metamers, material metamers, and observer metamers.
>
> **(b)** This is **chromatic adaptation** — the human visual system adjusts to changes in illumination to preserve the appearance of object colors. The visual system "subtracts" the color cast of the illuminant, so white appears white regardless of the light source.

---

## Question 6 — Image Formats and Memory Layout (Ex04, 8 pts)

**(a)** Tabulate the differences between GIF, PNG, and JPEG with respect to: color model, color depth, compression, and file size. (3 pts)

**(b)** Let I be a 12×12 RGB image stored in Java as a 3D integer array `int[H][W][C]`. How much memory does this require, including array-of-arrays overhead? (3 pts)

**(c)** If we pack each pixel into a single 32-bit integer instead, how much memory is saved? (2 pts)

> [!success]- Solution
> **(a)**
>
> | Format | Color model | Color depth | Compression | File size |
> |--------|-------------|-------------|-------------|-----------|
> | **GIF** | RGB (8-bit indexed, 256 colors) | 8 bpp | LZW (lossless) | Small |
> | **PNG** | RGB/RGBA (true color + alpha) | 24/48 bpp true color | LZ77+Huffman (lossless) | Medium |
> | **JPEG** | RGB (Y'CbCr internally) | 24 bpp | DCT-based (lossy) | Small (tunable) |
>
> Key: GIF = animations; PNG = lossless + transparency; JPEG = lossy, no alpha.
>
> **(b)** Java 3D array overhead:
> - References: 4(H + W·H) = 4(12 + 144) = 624 bytes
> - Object headers: 4(W·H + H + 1) = 4(144 + 12 + 1) = 628 bytes
> - Image data: 3·W·H·4 = 3·144·4 = 1728 bytes
> - **Total: 2980 bytes**
>
> **(c)** Packed: W·H·4 = 144·4 = 576 bytes (plus ~24 bytes for the single array header ≈ 600 bytes).
> Memory saved ≈ 2980 − 600 = **~2380 bytes**

---

## Question 7 — Point Operations and Contrast Stretching (Ex05, 6 pts)

HK point operation: `P_out = α · P_in + β`, 8-bit grayscale.

**(a)** How do α and β influence the result? (1 pt)

**(b)** Which HK operation implements image inversion? (1 pt)

**(c)** Let image G have minimum pixel value a=50 and maximum b=200. Which HK operation maximizes the contrast ratio of G? Derive α and β. (2 pts)

**(d)** What problems occur with poorly chosen α, β? How do you deal with them? (2 pts)

> [!success]- Solution
> **(a)** α = gain/contrast factor (scales spread), β = bias/brightness offset (shifts up/down).
>
> **(b)** P_out = -1 · P_in + 255 → α = -1, β = 255.
>
> **(c)** Map a→0, b→255:
> - α·50 + β = 0 and α·200 + β = 255
> - α(200-50) = 255 → **α = 255/150 = 1.7**
> - **β = -1.7×50 = -85**
>
> This is the min-max normalization / contrast stretch.
>
> **(d)** If α·P_in + β falls outside [0, 255], the result is undefined. Fix: **clamping** — saturate values below 0 to 0 and above 255 to 255: `clamp(x) = max(0, min(255, x))`.

---

## Question 8 — Linear Filters and Convolution (Ex05, 6 pts)

**(a)** What problem occurs at edge pixels during convolution? Name two fixes. (2 pts)

**(b)** Write the 5×5 kernel for a moving-average smoothing filter. (2 pts)

**(c)** Why are Laplacian filters used? Give the 4-neighbour discrete kernel. (2 pts)

> [!success]- Solution
> **(a)** The kernel extends beyond the image boundary. Fixes:
> 1. **Zero padding** — fill missing cells with 0
> 2. **Symmetric (mirror) padding** — reflect values across the edge (preferred, preserves mean intensity)
>
> **(b)** Every cell gets weight 1/25 (sum = 1):
> ```
> (1/25) × [1 1 1 1 1]
>           [1 1 1 1 1]
>           [1 1 1 1 1]
>           [1 1 1 1 1]
>           [1 1 1 1 1]
> ```
>
> **(c)** Laplacian = second-derivative filter (∇² image). Highlights regions of rapid intensity change = **edges**. Used for edge detection and image sharpening.
> ```
> [ 0  1  0]
> [ 1 -4  1]
> [ 0  1  0]
> ```

---

## Question 9 — JPEG Pipeline Walk-Through (Ex06, 8 pts)

**(a)** What are the main goals of the JPEG baseline process? (2 pts)

**(b)** For each step in the JPEG pipeline, summarize its function and mark whether it is lossy or lossless. (4 pts)

**(c)** Why are DC and AC coefficients entropy-coded differently? Which procedure is recommended for each? (2 pts)

> [!success]- Solution
> **(a)** Lossy compression of still images; reversibility (inverse decompression reconstructs a degraded image); low computational cost; tunable compression ratio via quantization factor.
>
> **(b)**
>
> | Step | Function | Lossy? |
> |------|----------|--------|
> | Image scale + block formation | Pad to MCU multiple; divide into blocks | No |
> | RGB → Y'CbCr | Separate luma from chroma | No |
> | Chroma subsampling | Reduce chroma resolution | **Yes** |
> | F-DCT (8×8 blocks) | Spatial → frequency domain | No |
> | Quantization | Discard perceptually insignificant high-freq coefficients | **Yes** |
> | Entropy coding (RLE + Huffman) | Lossless compression of quantized stream | No |
>
> **(c)**
> - **AC coefficients:** many of them, most are zero → **RLE + Huffman** of (run, value) symbols.
> - **DC coefficients:** one per block, neighboring blocks' DC values are similar → **DPCM** (encode difference between current and previous block's DC), then Huffman-code the differences.

---

## Question 10 — LZW Encoding (Ex06, 6 pts)

Encode the string `TATTARRATTAT` using the Lempel-Ziv-Welch algorithm. Show the dictionary building process and the output codes.

> [!success]- Solution
> Dictionary seeded: `1:T, 2:A, 3:R`.
>
> | Input | P | P+z | In dict? | Output | Add | New P |
> |-------|---|-----|----------|--------|-----|-------|
> | T | "" | T | yes | — | — | T |
> | A | T | TA | no | 1 (T) | 4:TA | A |
> | T | A | AT | no | 2 (A) | 5:AT | T |
> | T | T | TT | no | 1 (T) | 6:TT | T |
> | A | T | TA | yes | — | — | TA |
> | R | TA | TAR | no | 4 (TA) | 7:TAR | R |
> | R | R | RR | no | 3 (R) | 8:RR | R |
> | A | R | RA | no | 3 (R) | 9:RA | A |
> | T | A | AT | yes | — | — | AT |
> | T | AT | ATT | no | 5 (AT) | 10:ATT | T |
> | A | T | TA | yes | — | — | TA |
> | T | TA | TAT | no | 4 (TA) | 11:TAT | T |
> | (end) | T | — | — | 1 (T) | — | — |
>
> **Output: 1 2 1 4 3 3 5 4 1** (9 codes for 12 characters ≈ 25% compression)

---

## Question 11 — Huffman Coding (Ex06, 8 pts)

Build the Huffman code tree for these 8 symbols:

| Symbol | A | R | Y | O | S | T | X | U |
|--------|---|---|---|---|---|---|---|---|
| Prob % | 30.1 | 17.5 | 21.5 | 14.9 | 9.3 | 2.2 | 2.3 | 2.2 |

**(a)** Show each merge step. (3 pts)

**(b)** Derive the final Huffman codes. (2 pts)

**(c)** Compute the expected code length. (1 pt)

**(d)** Compute the entropy H. How close is the Huffman code to the entropy bound? (2 pts)

> [!success]- Solution
> **(a) Merge steps:**
> 1. Merge T(2.2) + U(2.2) = 4.4 → [TU]
> 2. Merge X(2.3) + [TU](4.4) = 6.7 → [XTU]
> 3. Merge S(9.3) + [XTU](6.7) = 16.0 → [SXTU]
> 4. Merge O(14.9) + [SXTU](16.0) = 30.9 → [OSXTU]
> 5. Merge R(17.5) + Y(21.5) = 39.0 → [RY]
> 6. Merge [OSXTU](30.9) + A(30.1) = 61.0 → [AOSXTU]
> 7. Merge [RY](39.0) + [AOSXTU](61.0) = 100 → root
>
> **(b) Codes** (0=left, 1=right):
>
> | Symbol | Code | Bits |
> |--------|------|------|
> | A | 11 | 2 |
> | R | 00 | 2 |
> | Y | 01 | 2 |
> | O | 100 | 3 |
> | S | 1010 | 4 |
> | X | 10110 | 5 |
> | T | 101110 | 6 |
> | U | 101111 | 6 |
>
> **(c)** L = 0.301×2 + 0.175×2 + 0.215×2 + 0.149×3 + 0.093×4 + 0.023×5 + 0.022×6 + 0.022×6
> = 0.602 + 0.350 + 0.430 + 0.447 + 0.372 + 0.115 + 0.132 + 0.132 = **2.58 bits/symbol**
>
> **(d)** H ≈ **2.54 bits/symbol**. The Huffman code (2.58) is within 0.04 bits of the entropy bound — essentially optimal.

---

## Question 12 — Content-Based Retrieval Concepts (Ex07, 8 pts)

**(a)** What is a feature vector? Give three examples from different media types. (2 pts)

**(b)** Explain the "curse of dimensionality" and its consequences for CBIR indexing. (2 pts)

**(c)** List and briefly explain 4 types of content-based queries. (2 pts)

**(d)** Two 4×4 images: Left = 8 blue + 8 white checkerboard; Right = 8 black + 8 white (two solid blocks). Apply 8-color uniform quantization and create color histograms for both. What happens with 4-bin (2-bit) quantization? (2 pts)

> [!success]- Solution
> **(a)** A feature vector is a numerical representation of a multimedia object's content. Examples:
> - **Image:** 64-bin color histogram
> - **Audio:** 13-dim MFCC vector
> - **Video:** MPEG-7 motion trajectory descriptor
>
> **(b)** As dimensions grow, distances between random points become nearly equal → "nearest neighbor" loses meaning. Indexes (k-d, R-tree) degrade to sequential scan. Required training data grows exponentially. In CBIR: 64-bin histograms are tractable, but 1000-dim SIFT or 4096-dim CNN features demand approximate methods (LSH, PQ, HNSW).
>
> **(c)**
> 1. **Query by Example (QbE):** User provides a sample image/audio — system finds most similar.
> 2. **Query by Sketch:** User draws a rough shape; system matches against features.
> 3. **Query by Feature Specification:** User sets ranges (e.g. "≥ 30% red, ≤ 5% blue").
> 4. **Query by Relevance Feedback:** User marks results as relevant/irrelevant; system refines.
>
> **(d)** 8-color quantization (1 bit per channel):
> - Left: H = (0, 8, 0, 0, 0, 0, 0, 8) — 8 blue, 8 white
> - Right: H = (8, 0, 0, 0, 0, 0, 0, 8) — 8 black, 8 white
>
> With 4-bin (2-bit) quantization, both collapse to **(8, 0, 0, 8)** — the images become **indistinguishable**. This is the classic quantization-loses-discrimination trade-off.

---

## Question 13 — Distance Metrics (Ex07, 8 pts)

Using the 8-bin histograms from Q12 (Left: blue+white, Right: black+white):

**(a)** Compute L₁ (Manhattan), L₂ (Euclidean), and L∞ (Chebyshev) distances. (3 pts)

**(b)** For H₁ = (5, 5, 5, 5) and H₂ = (8, 5, 4, 3), compute the Kolmogorov-Smirnov distance (normalized). (2 pts)

**(c)** For the same H₁ and H₂, compute the Chi-squared distance using the formula D_χ = Σ(xᵢ - f'(i))²/f'(i) where f'(i) = (xᵢ + yᵢ)/2. (3 pts)

> [!success]- Solution
> **(a)** Left H = (0, 8, 0, 0, 0, 0, 0, 8), Right H = (8, 0, 0, 0, 0, 0, 0, 8)
> - **L₁** = |0-8| + |8-0| + |8-8| = 8 + 8 = **16**
> - **L₂** = √(8² + 8²) = √128 ≈ **11.31**
> - **L∞** = max|pᵢ - qᵢ| = **8**
>
> **(b)** Cumulative H₁: (5, 10, 15, 20) → normalized: (0.25, 0.50, 0.75, 1.00)
> Cumulative H₂: (8, 13, 17, 20) → normalized: (0.40, 0.65, 0.85, 1.00)
> Per-bin |diff|: 0.15, 0.15, 0.10, 0.00
> **KS = 0.15**
>
> **(c)** Per bin:
> - i=1: f'=(5+8)/2=6.5 → (5-6.5)²/6.5 = 2.25/6.5 ≈ 0.346
> - i=2: f'=(5+5)/2=5.0 → 0/5 = 0
> - i=3: f'=(5+4)/2=4.5 → 0.25/4.5 ≈ 0.056
> - i=4: f'=(5+3)/2=4.0 → 1/4 = 0.25
> - **D_χ ≈ 0.346 + 0 + 0.056 + 0.25 = 0.652**

---

## Question 14 — Object-Relational DB Concepts (Ex08, 6 pts)

**(a)** Compare relational and object-relational databases across: data structure complexity, indexing, and query predicates. (3 pts)

**(b)** Define: User-Defined Type (UDT), OID, REF, DEREF. For each, give one key property. (3 pts)

> [!success]- Solution
> **(a)**
>
> | Dimension | Relational | Object-Relational |
> |-----------|-----------|-------------------|
> | **Data structure** | Flat tables, primitive types. Complex data decomposed into multiple tables. | Nested structures, arrays, UDTs. Complex data stored as structured objects. |
> | **Indexing** | B-trees, hash on scalar values. | B-trees on scalars + specialized indexes (R-trees for spatial, VP-trees for feature vectors). |
> | **Query predicates** | Exact match, range, LIKE. All on scalar values. | Scalar + similarity predicates (SIMILAR TO, WITHIN DISTANCE), object navigation (DEREF). |
>
> Key difference: relational treats multimedia as opaque BLOBs; OR treats them as structured objects with extractable features.
>
> **(b)**
> - **UDT:** Complex type encapsulating attributes + methods (like a class). Can be used as column types.
> - **OID:** System-generated, immutable, unique identifier for each object. Has no semantic meaning (unlike primary key).
> - **REF:** Typed pointer to an object, stored as a column value, references another object by its OID.
> - **DEREF:** Dereferences a REF to get the actual object. Without DEREF, you get the pointer, not the data.

---

## Question 15 — SQL Type Hierarchy and Collections (Ex08, 6 pts)

**(a)** Write SQL CREATE statements for a type hierarchy: base `MediaType` (id, name, format, size_bytes), subtype `ImageType` (width, height, color_depth), subtype `VideoType` (duration_sec, fps, codec). Create a table storing all types. (3 pts)

**(b)** Explain when to use VARRAYs vs. nested tables. Which would you choose for storing feature vectors per image? Justify. (3 pts)

> [!success]- Solution
> **(a)**
> ```sql
> CREATE TYPE MediaType AS (
>     id INTEGER, name VARCHAR(100), format VARCHAR(20), size_bytes BIGINT
> );
> CREATE TYPE ImageType UNDER MediaType (
>     width INTEGER, height INTEGER, color_depth INTEGER
> );
> CREATE TYPE VideoType UNDER MediaType (
>     duration_sec INTEGER, fps DECIMAL(5,2), codec VARCHAR(30)
> );
> CREATE TABLE media_library OF MediaType;
> ```
>
> **(b)**
> - **VARRAY:** Bounded (max declared), ordered, stored inline. Best when max size is known and you don't need SQL access to elements.
> - **Nested table:** Unbounded, stored in separate table, supports SQL via TABLE() and set operations. Best when size varies and you need to query elements.
>
> Feature vectors → **nested table** because: (1) number of features per image varies, (2) need SQL queries on feature vectors, (3) set operations may be useful, (4) VARRAY requires arbitrary max declaration.

---

## Question 16 — Indexing Fundamentals (Ex09, 6 pts)

**(a)** What are the two main functions of index structures? Name two drawbacks. (2 pts)

**(b)** What two requirements does CBIR place on index structures beyond conventional databases? (2 pts)

**(c)** State the properties of a B-tree of order m. (2 pts)

> [!success]- Solution
> **(a)**
> - **Functions:** (1) Increase execution speed of retrieval queries. (2) Improve query optimizer's ability to access data quickly.
> - **Drawbacks:** (1) Indexes consume additional storage. (2) Insert/delete/update slow down because indexes must be recomputed.
>
> **(b)**
> 1. Methods for **reduction of dimensionality** (curse of dimensionality makes high-D indexes impractical)
> 2. Efficiency in query processing using **specific indexing data structures** tailored to high-dimensional feature vectors
>
> **(c)** B-tree of order m:
> - Every node has at most m children
> - Root has at least 2 children (unless leaf)
> - Every non-leaf non-root node has at least ⌈m/2⌉ children
> - All leaves at the same level
> - Search/delete/insert in **O(log n)**

---

## Question 17 — R-Tree Operations (Ex09, 10 pts)

**(a)** What is the central idea behind the R-tree? How does it relate to the B-tree? (2 pts)

**(b)** List the five formal properties (P1–P5) of an R-tree. (3 pts)

**(c)** Describe the R-tree insertion algorithm steps. (3 pts)

**(d)** Describe the R-tree deletion algorithm, including the condense-tree step. (2 pts)

> [!success]- Solution
> **(a)** Group nearby objects and represent each group by its **minimum bounding rectangle (MBR)** in the next level up. The R-tree is height-balanced like a B-tree, but index records in leaves contain pointers to actual data objects. Non-leaf nodes store MBRs that cover their children.
>
> **(b)**
> | P1 | Leaf has between m and M entries (unless root) |
> | P2 | Each leaf entry is the MBB of one object |
> | P3 | Each non-leaf entry is the MBB covering all children's MBBs |
> | P4 | Non-leaf non-root has between m and M children |
> | P5 | Root has at least 2 children (unless leaf) |
>
> **(c) Insert:**
> 1. **Find leaf:** Descend from root, at each level choose subtree whose MBB needs **least expansion** for the new entry
> 2. **Insert entry** into the chosen leaf
> 3. **Handle overflow:** If leaf exceeds M entries, **split** into two nodes
> 4. **Propagate upward:** Adjust MBBs along path to root. If split reaches root, create new root
>
> **(d) Delete:**
> - D1: Find leaf containing the entry
> - D2: Remove the entry
> - D3: **Condense tree:** Remove nodes with too few entries (< m), **reinsert** orphaned entries from leaf level upward, adjust MBBs along the path
> - D4: If root has only one child, make that child the new root

---

## Question 18 — Range and Nearest-Neighbor Queries (Ex09, 6 pts)

**(a)** Define a range query and explain how an R-tree index helps answer it using MINDIST. (3 pts)

**(b)** Describe the nearest-neighbor query (NNQ) and the branch-and-bound pruning strategy with an R-tree. (3 pts)

> [!success]- Solution
> **(a) Range query:** Return all points P with dist(P, Q) ≤ r, where Q is the query point and r is the search radius.
> - Without index: Sequential scan, compute distance for every point.
> - With index: Compute **MINDIST** (minimum distance between query point and bounding region). **Prune** any subtree whose MINDIST > r, since it cannot contain qualifying points.
>
> **(b) NNQ:** Return the single point with lowest distance to Q. k-NNQ returns the k nearest.
>
> Branch-and-bound:
> 1. Initialize resultdist = ∞
> 2. Traverse tree from root
> 3. For each node, compute MINDIST between Q and the node's MBB
> 4. **Prune** any branch with MINDIST ≥ current best resultdist
> 5. At leaf: compute actual distance to each candidate. Update best if smaller
> 6. Continue until no unexplored branch can improve the result

---

## Scoring Summary

| Question | Topic | Sheet | Points |
|----------|-------|-------|--------|
| Q1 | Signal Processing, PCM, Nyquist | Ex01 | 6 |
| Q2 | Structured vs. Unstructured Data | Ex01+Ex02 | 5 |
| Q3 | Semantic Gap | Ex02 | 5 |
| Q4 | Color Models: RGB↔CMYK↔HSV | Ex03 | 8 |
| Q5 | Metamers & Chromatic Adaptation | Ex03 | 4 |
| Q6 | Image Formats & Memory Layout | Ex04 | 8 |
| Q7 | Point Operations & Contrast | Ex05 | 6 |
| Q8 | Linear Filters & Convolution | Ex05 | 6 |
| Q9 | JPEG Pipeline Walk-Through | Ex06 | 8 |
| Q10 | LZW Encoding Trace | Ex06 | 6 |
| Q11 | Huffman Coding Construction | Ex06 | 8 |
| Q12 | CBIR Concepts & Histograms | Ex07 | 8 |
| Q13 | Distance Metrics (L₁, L₂, K-S, χ²) | Ex07 | 8 |
| Q14 | ORDB Concepts | Ex08 | 6 |
| Q15 | SQL Type Hierarchy & Collections | Ex08 | 6 |
| Q16 | Indexing Fundamentals | Ex09 | 6 |
| Q17 | R-Tree Operations | Ex09 | 10 |
| Q18 | Range & NN Queries | Ex09 | 6 |
| **Total** | | **All 9** | **116** |

---

## Vault Page References

| Question | Related Vault Pages                                                               |
| -------- | --------------------------------------------------------------------------------- |
| Q1       | [[audio-sampling-nyquist-theorem]], [[pcm-digital-audio]]                         |
| Q2       | [[structured-vs-unstructured-retrieval]], [[multimedia-definition]]               |
| Q3       | [[semantic-gap]], [[sensory-gap]]                                                 |
| Q4       | [[rgb-color-model]], [[cmyk-color-model]], [[hsv-color-model]]                    |
| Q5       | [[metamers]], [[chromatic-adaptation]]                                            |
| Q6       | [[image-file-formats]], [[pixel-formats-and-bit-depth]]                           |
| Q7       | [[image-point-operations]]                                                        |
| Q8       | [[linear-convolution-filters]], [[dithering]]                                     |
| Q9       | [[jpeg-compression-pipeline]], [[lossless-vs-lossy-compression]]                  |
| Q10      | [[lz77-lzw-compression]]                                                          |
| Q11      | [[entropy-coding-huffman-arithmetic]]                                             |
| Q12      | [[content-based-retrieval]], [[color-histogram]], [[feature-vector]]              |
| Q13      | [[minkowski-distance]], [[kolmogorov-smirnov-distance]], [[chi-squared-distance]] |
| Q14      | [[object-relational-databases]], [[multimedia-query-languages]]                   |
| Q15      | [[object-relational-databases]], [[nested-tables-vs-varrays]]                     |
| Q16      | [[r-tree]], [[quadtree-and-kd-tree]]                                              |
| Q17      | [[r-tree]], [[gist-framework]]                                                    |
| Q18      | [[r-tree]], [[locality-sensitive-hashing]]                                        |

---

## Cross-references
- [[mmdb-exam-simulation-ss25]] — Previous exam simulation (SS25 Klausur format)
- [[mmdb-exam-prediction]] — Archetype analysis and probability ranking
- [[multimedia-databases-lecture-01]] through [[multimedia-databases-lecture-09]]
