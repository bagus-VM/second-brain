---
title: "Multimedia Databases — Condensed Exam Cheat Sheet"
tags: [multimedia-databases, cheat-sheet, semester-1, exam-prep]
course: "Multimedia Databases"
source_count: 18
status: current
last_updated: 2026-07-20
prerequisites: []
---

# MMDB Condensed Cheat Sheet (Ex01–Ex09)

---

## 1. SIGNAL PROCESSING (Ex01)

**Sine wave:** f(x) = A · sin(2πfx + φ) — A=amplitude, f=frequency, φ=phase, T=1/f=period

**PCM (Pulse Code Modulation):**
- **Sampling:** Define fixed grid of measuring points (spacing Δt). Sample = signal value at grid point. Sampling rate = density of samples.
- **Quantization:** Convert measured values to discrete countable range (binary). Resolution = bits per sample.

**Max Quantization Error:** Q = Δx / (2^N · 2), where Δx = signal range, N = bits

**Nyquist-Shannon Theorem:** If highest frequency = f_g, then sampling rate f_s > 2·f_g → signal reconstructable without loss.

**Aliasing:** Artifact from sampling below Nyquist rate. Anti-aliasing = pre-filter high frequencies.

---

## 2. DATA TYPES & SEMANTIC GAP (Ex02)

| Type | Structure | Query | Example |
|------|-----------|-------|---------|
| Structured | Predefined schema, relational DB | SQL, exact matching | Names, addresses |
| Unstructured | No model, raw media | Information retrieval, fuzzy/similarity | Video, audio, text |
| Semi-structured | Tags/markers, hierarchies | XPath, keyword query | XML, JSON |

**Semantic Gap:** Low-level features (color histogram, pixel intensity, bit rate, frequency spectrum) are easy to extract but carry no semantics. High-level features (objects, emotions, speech content) carry meaning but are hard to extract. "Bridging the gap" = connecting low-level data to high-level concepts.

**MMDB vs Classical DB:** MM data is unstructured, high-volume, needs multi-dimensional indexing (not just keywords), content/context-based retrieval, spatial/temporal queries, querying by example, fuzzy predicates.

---

## 3. COLOR MODELS (Ex03)

**Color model** = abstract method for representing color. Two types: additive (light) and subtractive (pigment).

| Model | Type | Primaries | Black | White | Use |
|-------|------|-----------|-------|-------|-----|
| RGB | Additive | R, G, B | (0,0,0) | (1,1,1) | Screens, monitors |
| CMY(K) | Subtractive | C, M, Y | (1,1,1) | (0,0,0) | Printers, ink |
| HSV/HSB | Perceptual | Hue(0-360), Sat(0-1), Bright(0-1) | — | — | Image processing |

**Key conversions:**
- CMY = 1 − RGB: C=1-R, M=1-G, Y=1-B
- CMYK: K = min(C,M,Y); C'=(C-K)/(1-K), M'=(M-K)/(1-K), Y'=(Y-K)/(1-K)
- HSV from RGB: W=min(R,G,B); (R',G',B')=(R-W, G-W, B-W); find max channel; H depends on which channel is max (formula uses 120° offsets); S=(max-W)/max; V=max

**Metamers:** Different spectral distributions perceived as same color (same L,M,S cone stimulation).

**Chromatic Adaptation:** Eye recalibrates "white" reference under changing illumination.

**Color spaces:**
- **CIE XYZ:** Additive, linear, NOT perceptually uniform. Distance ≠ perceived similarity.
- **CIE L\*a\*b\*:** Perceptually uniform. Distance predicts visual similarity. Adapted to D50 (5000K).
- **YCbCr:** Luma (Y) + chroma (Cb, Cr). Used in video. Coefficients: BT.601 (SD), BT.709 (HD), BT.2020 (HDR).

---

## 4. IMAGE PROCESSING & FORMATS (Ex04)

**Vector vs Raster:** Vector = math commands (shapes, curves), scales well, small. Raster = pixel bitmap, degrades when scaled.

| Format | Color Model | Depth | Compression | Notes |
|--------|-------------|-------|-------------|-------|
| GIF | RGB (indexed) | 8 bpp (256 colors) | LZW (lossless) | Animation, logos, not photos |
| PNG | RGB/RGBA | Variable (1-48 bpp) | LZSS+Huffman (lossless) | No animation, transparency |
| JPEG | RGB | 24 bpp | DCT-based (lossy) | No animation, no transparency |

**Memory in Java 3D array:** Total = 4(H+WH) + 4(WH+H+1) + 4(3WH) ≈ 12WH + overhead. Packing pixel into single int (32-bit): 8 bits per channel → much less memory.

**Unpacking pixel:** R = (pixel >> 16) & 0xFF; G = (pixel >> 8) & 0xFF; B = pixel & 0xFF

**Pixel density (PPI):** Use Pythagoras on aspect ratio to get width in inches, then PPI = horizontal_pixels / width_inches.

**Uniform Quantization:** Divide each color axis into equal segments, map each pixel to nearest region, representative = average of mapped colors.

**Median Cut Quantization:**
1. Find bounding box of all colors
2. Sort along longest axis
3. Split at median → 2 regions
4. Repeat until 256 regions
5. Representative = average per box

**Noise Dithering:** Add uniform white noise before quantization to reduce banding: P(x,y) = Q(I(x,y) + noise(x,y))

---

## 5. POINT OPERATIONS & FILTERS (Ex05)

**HK Point Operation:** P_out = α · P_in + β — α = gain (contrast), β = bias (brightness)
- **Inversion:** P_out = -P_in + MaxValue (α=-1, β=255)
- **Clamping:** Clamp output to [0, 2^n - 1] to prevent overflow
- **Max contrast:** α = 255/(b-a), β = -a·α where a=min pixel, b=max pixel

**Convolution / Linear Filter:** Kernel slides over image, output = weighted sum of neighborhood.
- **Edge problem:** Kernel extends beyond boundary. **Fix:** zero padding, symmetric padding, redefine convolution (output=0 or output=I(x,y) at edges).
- **Moving average 5×5:** All 1s, divide by 25.
- **Weighted smoothing kernels:**
  - Pyramid: f(x,y) = -α·max(|x|,|y|) + k
  - Cone: f(x,y) = -α·√(x²+y²) + k
  - Gaussian: bell-shaped, most common
- Choose k so smallest coefficient ≥ 0, then round to integers.

**Laplacian Filter:** Second-derivative filter for edge detection. L(x,y) = ∂²I/∂x² + ∂²I/∂y². Approximated with discrete kernels (e.g., [0,1,0; 1,-4,1; 0,1,0]).

---

## 6. JPEG COMPRESSION (Ex06)

**Baseline Process pipeline:**
1. **Pre-processing** (lossless/lossy):
   - Color space: RGB → YCbCr (separate luma/chroma; human less sensitive to color changes)
   - Subsampling: Reduce chroma (4:4:4=none, 4:2:2=half horizontal, 4:2:0=half both) — **LOSSY**
   - Block formation: Divide into 8×8 blocks (MCU). 4:2:0 → MCU=16×16, image must be divisible by 16
   - Scale image to be divisible by 8 (or 16 for 4:2:0)
2. **Forward DCT** (lossless): Transforms 8×8 spatial block → 64 frequency coefficients
   - DC coefficient = DCT(0,0) = basic hue of block
   - AC coefficients = 63 remaining = color change detail
   - High frequencies most useful for compression (human eye sensitive to low freq)
3. **Quantization** (LOSSY): Divide each DCT coefficient by quantization matrix entry, round to integer. Non-standardized matrix, tuned to human vision.
4. **Entropy Coding** (lossless):
   - **Zig-zag scan:** 8×8 → 1×64 vector, groups low freq at front, high freq at end
   - **RLE on AC:** (skip, value) pairs for zeros + next non-zero
   - **Difference coding on DC:** Encode difference between neighboring blocks' DC coefficients (they're similar → small differences)
   - **Huffman coding:** Variable-length codes based on probability

**LZW Compression (lossless, used in GIF):**
- **Encoding:** Init dictionary with single chars. P=empty. For each char z: if P+z in dictionary, P=P+z; else output code(P), add P+z to dictionary, P=z. Output code(P) at end.
- **Decoding:** Read code, output entry, track oldCode. If code in dict: output it, add prefix+first_char(code) to dict. If not in dict: char=first char of decoding of oldCode, output prefix+char, add to dict.

**Huffman Coding:**
1. Create leaf node per symbol, add to priority queue (min-heap by probability)
2. While >1 node: remove two lowest, create parent with sum probability, add back
3. Root = last remaining node. Left=0, Right=1. Read path from root to leaf = code.

---

## 7. CONTENT-BASED IMAGE RETRIEVAL (Ex07)

**CBR/CBIR:** Process visual content → extract features → match by similarity (not keywords).
- **Feature Extraction** → **Feature Vector** (numerical n-dimensional representation)
- **Matching** via distance metrics

**Feature Vector problems:** Curse of dimensionality — performance degrades as dimensions grow. Fix: feature selection, feature extraction, specialized index structures.

**Dominant Color Descriptor:** F = {(c_i, p_i, v_i), s} — c_i=color (RGB), p_i=percentage, v_i=variance, s=spatial coherency. Simplified: F = {(c_i, p_i)}, 1≤N≤8 clusters.

**Spatial Coherency:** Normalized avg number of connected pixels of same color (3×3 mask).

**Content-based query types:**
- **Point query:** Exact feature vector match
- **Range query:** All points within distance r from query
- **k-NN query:** k most similar results

**Precision & Recall:**
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)

**Distance Metrics:**

**Minkowski (L_p):** L_p(P,Q) = (Σ|x_i - y_i|^p)^(1/p)
- L1 = Manhattan (|x₁-y₁| + |x₂-y₂| + ...)
- L2 = Euclidean (√(Σ(x_i-y_i)²))
- L∞ = Maximum / Chebyshev (max|x_i - y_i|)

**Kolmogorov-Smirnov:** KS(P,Q) = max_i |Fr(i;P) - Fr(i;Q)| where Fr = cumulative histogram

**Chi-squared:** D_χ(P,Q) = Σ (x_i - f'(i))² / f'(i), where f'(i) = (x_i + y_i)/2

**Color Histograms:** Count pixels per quantized bin. Compare histograms with distance metrics. Bin quantization (e.g., 2-bit mask) reduces histogram size.

---

## 8. QUERYING — SQL/MM & MPQF (Ex08)

**Relational vs Object-Relational DB:**

| Feature | Relational | Object-Relational |
|---------|------------|-------------------|
| Data types | Predefined only | User-defined, inheritance, collections |
| Complex objects | Can't express | Full OO features |
| Query optimization | Easier | More complex |
| Scalability | Good for large data | Good for complex relationships |

**Key OR concepts:**
- **User-defined type:** CREATE OR REPLACE TYPE ... AS OBJECT (attributes + methods)
- **Inheritance:** UNDER supertype, NOT FINAL to allow subtypes
- **Table of objects:** CREATE TABLE ... OF type (row objects with OIDs)
- **Polymorphism:** Rows can hold subtype instances; overriding/overloading methods
- **OID:** System-generated or primary-key based object identifier
- **REF/DEREF:** Logical pointer to row object. SELECT REF(a) FROM ... ; DEREF(p.address)
- **Collections:** VARRAY (fixed size, ordered) vs Nested Tables (arbitrary size, queryable)
- **Dot operator:** Navigate schema without JOINs: s.address.street

**SQL/MM:** Features have SI_Score method returning 0-1 distance. Query by example using image features.
Example : 
```sql
-- UDT for image with MPEG-7 descriptors
CREATE TYPE ZooImageType AS (
    image_data BLOB,
    width INTEGER,
    height INTEGER,
    dominant_color DominantColorType,
    color_layout ColorLayoutType,
    edge_histogram EdgeHistogramType
);

-- UDT for dominant color (MPEG-7)
CREATE TYPE DominantColorType AS (
    colors ColorValue ARRAY[8],
    percentages FLOAT ARRAY[8],
    spatial_coherency FLOAT
);

-- Animal type with photo
CREATE TYPE AnimalType AS (
    animal_id INTEGER,
    name VARCHAR(50),
    species VARCHAR(50),
    birth_date DATE,
    photo ZooImageType
);

-- Keeper type with references to animals
CREATE TYPE KeeperType AS (
    keeper_id INTEGER,
    name VARCHAR(50),
    assigned_animals REF(AnimalType) ARRAY[]
);

-- Cage type
CREATE TYPE CageType AS (
    cage_id INTEGER,
    location VARCHAR(100),
    capacity INTEGER,
    occupants REF(AnimalType) ARRAY[]
);

-- Create tables
CREATE TABLE animals OF AnimalType (
    oid REF(AnimalType) SYSTEM GENERATED,
    PRIMARY KEY (animal_id)
);

CREATE TABLE keepers OF KeeperType (
    PRIMARY KEY (keeper_id)
);

CREATE TABLE cages OF CageType (
    PRIMARY KEY (cage_id)
);
```

**MPEG Query Format (MPQF):** XML-based. Three parts: QFDeclaration (define resources), OutputDescription (what to return, max items, sort), QueryCondition (similarity, spatial, freetext, arithmetic filters). Uses preferenceValue for weighting conditions.

---

## 9. INDEXING & SEARCH (Ex09)

**Index functions:** Speed up retrieval, improve query optimizer. Drawbacks: extra storage, slower inserts/deletes/updates.

**CBIR requirements:** Dimensionality reduction + specialized index structures.

**Index Structures:**

| Structure | Type | Key Idea |
|-----------|------|----------|
| B-tree | 1D, balanced | Order m: max m children, min ⌈m/2⌉. All leaves same level. Log search/insert/delete. |
| Hash | 1D | Hash function maps key → bucket. Collision: separate chaining. |
| K-d tree | k-dimensional | Binary tree, splits alternately on each dimension at each level. |
| Point Quadtree | 2D | Each node has 4 children (NW, NE, SW, SW). Splits space into quadrants. |
| **R-tree** | **n-dimensional** | **Groups nearby objects into MBBs (Minimum Bounding Rectangles). Height-balanced like B-tree.** |

**R-tree (most important for exam):**
- Parameters: M = max entries per node, m ≤ M/2 = min entries
- **Properties:** P1) leaf has m-M entries; P2) leaf entry I = MBB of object; P3) non-leaf I = MBB of children's MBBs; P4) non-leaf has m-M children; P5) root ≥ 2 children; P6) all leaves same level

**R-tree Insert:**
1. **ChooseLeaf:** Start at root. If leaf → return. Else pick entry whose MBB needs smallest enlargement for new object. Go down recursively.
2. **Add entry** to leaf. If full → split into L and LL.
3. **AdjustTree:** Walk up from leaf to root, updating MBBs. Split further if needed. May create new root level.

**R-tree Delete:**
1. **FindLeaf:** Search tree for leaf containing entry E.
2. **Delete E** from leaf.
3. **CondenseTree:** Walk up from leaf. If node has too few entries → remove it, add entries to re-insert set Q. Adjust MBBs. Re-insert orphaned entries.
4. **Shorten tree:** If root has only one child → make child the new root.

**Search Algorithms:**

| Query | Without Index | With Index |
|-------|---------------|------------|
| **Exact** | Sequential scan | Start at root, recurse into regions containing Q (may check multiple branches due to overlap) |
| **Range** (dist ≤ r) | Sequential scan | Check if query region intersects page region using MINDIST. Only explore intersecting pages. |
| **k-NN** | Sequential scan | Initialize ResultDist=∞. Recursively explore closest regions first. Update best distance as results found. |

---

## KEY FORMULAS QUICK REF

| Formula | Use |
|---------|-----|
| Q = Δx / (2^N · 2) | Max quantization error |
| f_s > 2·f_g | Nyquist sampling rate |
| P_out = α·P_in + β | HK point operation |
| C = 1-R, M = 1-G, Y = 1-B | RGB → CMY |
| L_p = (Σ\|x_i-y_i\|^p)^(1/p) | Minkowski distance |
| KS = max\|Fr(P)-Fr(Q)\| | Kolmogorov-Smirnov |
| D_χ = Σ(x_i - f'(i))²/f'(i) | Chi-squared distance |
| Precision = TP/(TP+FP) | Retrieval precision |
| Recall = TP/(TP+FN) | Retrieval recall |
| PPI = pixels / inches | Pixel density |
| f(x,y) = -α·max(\|x\|,\|y\|) + k | Pyramid kernel |
| f(x,y) = -α·√(x²+y²) + k | Cone kernel |
