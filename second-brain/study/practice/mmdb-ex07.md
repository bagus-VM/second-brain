---
<<<<<<< HEAD
title: "MMDB Exercise 7 — Content-Based Retrieval"
=======
title: "Exercise Sheet 7 — Content-Based Retrieval"
>>>>>>> 20ac138 (2nd week of june)
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
<<<<<<< HEAD
last_updated: 2026-06-15
---

=======
last_updated: 2026-06-14
---

# Exercise Sheet 7 — Content-Based Retrieval

>>>>>>> 20ac138 (2nd week of june)
## Exercises

### Task 1: Content-Based Retrieval (CBR)

<<<<<<< HEAD
1. What does **Content-Based Retrieval** mean?
2. What are the components of a **CBIR architecture**? Explain each with an example.
3. What is a **feature vector**?
4. What problems occur when **indexing** feature vectors?

### Task 2: CBR Terminology

Explain in your own words, with an example for each:
1. Dominant Color
2. Spatial Coherency
3. Distance Metrics
4. Curse of Dimensionality
5. Types of content-based queries

### Task 3: CBR Systems

> Query: *"Give me all images which contain a **blue truck**."*

1. What necessary conditions must a CBIR system fulfil to answer this query?
2. What problems can occur?

### Task 4: Image Indexing by Colours

Two 4×4 images: the left has 8 blue + 8 white pixels (checkerboard); the right has two big blocks (one black, one white).

1. Apply an **even colour quantization for 8 colours**. Which quantization area does each pixel fall in?
2. Create a **colour histogram** for both images.
3. Apply an **even bin quantization for 2 bits** (4 bins).

### Task 5: Similarity by Colour Distribution

Using the two images and their histograms from Task 4:

1. **Minkowski distances:** Compute `L₁`, `L₂`, `L∞` between the two histograms. Repeat, replacing the red colour in the left image with black. What do you conclude?
2. **Non-parametric distances:** For `H₁ = (5, 5, 5, 5)` and `H₂ = (8, 5, 4, 3)`, compute:
   - (a) Kolmogorov–Smirnov distance
   - (b) Chi-squared distance

## Solutions

> [!note]- Solution
> **1.1) What is CBR:**
> Retrieval of multimedia objects from a database based on their **content** (low-level features: colour, shape, texture, audio spectrum) rather than on textual metadata or keywords. The query itself is a media sample ("search by example") or a feature specification.
>
> **1.2) CBIR architecture components:**
>
> | Component | Role | Example |
> |-----------|------|---------|
> | **Feature extractor** | Computes feature vectors from the raw media | Colour histogram, MPEG-7 Dominant Color descriptor |
> | **Indexer** | Builds an efficient data structure over the feature vectors | R-tree, VP-tree, k-d-tree (or approximate NN for high-D) |
> | **Storage** | Holds the feature vectors + the media itself | MMDBMS with feature columns |
> | **Query engine** | Parses the query, computes its features, runs similarity search | k-NN search on the index |
> | **Similarity / distance module** | Computes how close two feature vectors are | L₂, Mahalanobis, K-S, χ², EMD |
> | **Ranking / result module** | Returns top-k matches ordered by distance | Top-20 by smallest L₂ |
>
> **1.3) Feature vector:**
> A numerical representation of (a chosen aspect of) a multimedia object's content. Each dimension is a feature value. Examples: 64-bin colour histogram, MPEG-7 Color Layout vector, 13-dim MFCC vector for an audio frame, SIFT descriptor (128 dims).
>
> **1.4) Indexing problems:**
> - **High dimensionality** (see Task 2.4) — classical tree indexes (k-d, R-tree) degrade to linear scan above ~10–20 dimensions.
> - **Non-metric distances** (e.g. K-S, χ²) — most tree indexes assume a metric.
> - **Variable feature dimensionality** across media types.
> - **Approximate** but fast indexes (LSH, VP-tree, HNSW) trade exactness for speed.

> [!note]- Solution
> **2.1) Dominant Color:**
> The few colours that occupy the largest fraction of pixels in a region/image. Example: a sunset photo's dominant colors are orange, red, dark purple. MPEG-7's Dominant Color descriptor stores `(c_i, p_i, v_i, s_i)` for each dominant colour.
>
> **2.2) Spatial Coherency:**
> A feature's value should be **locally consistent** — neighbouring pixels are likely to belong to the same object or region. Exploiting this, you can extract features per region (e.g. per 8×8 block) rather than globally, and that gives you **spatial** information. Example: a face image has a pinkish region in the upper half and a darker one in the lower half — global averaging would lose that.
>
> **2.3) Distance Metrics:**
> A function `d(P, Q) ≥ 0` (with `d(P, P) = 0` and symmetry) that quantifies how different two feature vectors are. The choice of metric shapes which images the system considers "similar." Examples: L₁, L₂, L∞ (Minkowski family), Mahalanobis (covariance-aware), Cosine (angle-only), K-S, χ², EMD.
>
> **2.4) Curse of Dimensionality:**
> As the number of dimensions `d` grows, the volume of the unit cube concentrates in the corners. Consequences:
> - Distances between **random** points become nearly equal — "nearest neighbour" loses meaning.
> - Indexes (k-d, R-tree) degrade to sequential scan.
> - Required training data for any statistical estimate grows exponentially.
>
> In CBIR specifically: a 64-bin histogram is still tractable, but 1000-dim SIFT or 4096-dim CNN features demand approximate methods (LSH, PQ, HNSW).
>
> **2.5) Types of content-based queries:**
> 1. **Query by Example (QbE):** user provides a sample image/audio — system finds most similar items.
> 2. **Query by Sketch:** user draws a rough shape; system matches against features.
> 3. **Query by Feature Specification:** user sets ranges (e.g. "≥ 30% red, ≤ 5% blue").
> 4. **Query by Concept / Semantic:** user names a high-level concept; system bridges to low-level features (MPEG-7 semantic descriptors).
> 5. **Query by Relevance Feedback:** user marks returned results as relevant/irrelevant; system refines.

> [!note]- Solution
> **3.1) Necessary conditions to answer *"blue truck"*:**
> - System must have a **blue colour detector** (a "blue detector" feature) and a **truck detector** (a higher-level semantic concept).
> - The **semantic gap** must be bridged somewhere — either:
>   - **manually** via annotations (the truck concept is stored as a tag, blue is computed from low-level features), or
>   - **automatically** by a learned detector (CNN trained on labelled truck images + colour histogram).
> - The system must be able to **fuse** the two criteria (AND of "contains blue" + "contains truck").
>
> **3.2) Problems:**
> - **Semantic gap:** the system sees pixel statistics, not the concept "truck." Without a detector, "blue truck" is just a region of mostly-blue pixels that might be sky.
> - **Variability:** trucks come in many shapes/colours/orientations. A detector trained on one truck dataset may miss unfamiliar trucks.
> - **Polysemy:** "blue" is ambiguous (cyan? navy? teal?).
> - **Context:** a blue truck parked next to a blue sky is harder than a blue truck on a beige road.
> - **Annotation cost:** the human-labelled training data for "truck" is expensive.

> [!note]- Solution
> **4.1) Even 8-colour quantization on 4×4 images:**
>
> With 8 colours and 4×4 = 16 pixels per image, the simplest is **uniform 1-bit-per-channel** (1-bit R, 1-bit G, 1-bit B → 8 cells). Each cell represents a 3-bit colour code:
>
> | Bin | Colour (RGB 1-bit) |
> |-----|---------------------|
> | 0 | (0,0,0) black |
> | 1 | (0,0,1) blue |
> | 2 | (0,1,0) green |
> | 3 | (0,1,1) cyan |
> | 4 | (1,0,0) red |
> | 5 | (1,0,1) magenta |
> | 6 | (1,1,0) yellow |
> | 7 | (1,1,1) white |
>
> **Left image (8 blue + 8 white checkerboard):**
> - 8 pixels in bin 1 (blue)
> - 8 pixels in bin 7 (white)
>
> **Right image (one big black block + one big white block):**
> - 8 pixels in bin 0 (black)
> - 8 pixels in bin 7 (white)
>
> **4.2) Histograms:**
>
> | Image | H[black] | H[blue] | H[green] | H[cyan] | H[red] | H[magenta] | H[yellow] | H[white] |
> |-------|----------|---------|----------|---------|--------|------------|-----------|----------|
> | Left  | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 8 |
> | Right | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
>
> **4.3) Even 2-bit (4-bin) quantization:**
> Group the 8 bins into 4 pairs. A natural grouping: pairs that share the high bit of blue:
> - Bin 0 = (black, blue) — "no green, no red"
> - Bin 1 = (green, cyan) — "green, no red"
> - Bin 2 = (red, magenta) — "no green, red"
> - Bin 3 = (yellow, white) — "green + red"
>
> | Image | B0 | B1 | B2 | B3 |
> |-------|----|----|----|----|
> | Left  | 8  | 0  | 0  | 8  |
> | Right | 8  | 0  | 0  | 8  |
>
> **Critical insight:** with 2-bit quantization the two images become **indistinguishable** — they collapse to the same histogram `(8, 0, 0, 8)`. This is the classic **quantization-loses-discrimination** trade-off.

> [!note]- Solution
> **5.1) Minkowski distances:**
>
> `L_p(P, Q) = ( Σ |pᵢ − qᵢ|ᵖ )^(1/p)`
>
> Using the 8-bin histograms from Task 4.2:
> - `L₁` (Manhattan): `Σ|pᵢ − qᵢ|` = `|0−8| + |8−0| + |0−0|×6 + |8−8|` = `8 + 8 = 16`
> - `L₂` (Euclidean): `√(8² + 8²)` = `√128 ≈ 11.31`
> - `L∞` (Chebyshev): `max |pᵢ − qᵢ|` = `8`
>
> Now replace "red" in the left image with "black" (i.e. turn the original 8 blue into 0 blue, and the 8 white into 8 black):
> - New left histogram: `(8, 0, 0, 0, 0, 0, 0, 8)` — same as the right image.
> - `L₁ = L₂ = L∞ = 0` — the images become identical under the metric.
>
> **Conclusion:** L₁/L₂/L∞ measure **bin-wise** differences, not perceptual or semantic ones. Swapping red for black in a region of the image can drop a meaningful blue/white scene into "looks like a black/white scene" purely by accident of the colour space. Histogram distances are useful but **blind to spatial layout and colour semantics**.
>
> **5.2) Non-parametric distances on `H₁ = (5,5,5,5)`, `H₂ = (8,5,4,3)`:**
>
> **(a) Kolmogorov–Smirnov:**
> `KS(P, Q) = max_i | Fᵣ(i; P) − Fᵣ(i; Q) |`
> where `Fᵣ(i; ·)` is the cumulative histogram.
>
> Cumulative of `H₁`: `(5, 10, 15, 20)` → normalized: `(0.25, 0.50, 0.75, 1.00)`
> Cumulative of `H₂`: `(8, 13, 17, 20)` → normalized: `(0.40, 0.65, 0.85, 1.00)`
>
> Per-bin |diff|: `|0.25−0.40|=0.15`, `|0.50−0.65|=0.15`, `|0.75−0.85|=0.10`, `|1.00−1.00|=0.00`
> **`KS = 0.15`**
>
> **(b) Chi-squared:**
> `D_χ(P, Q) = Σ (xᵢ − f′(i))² / f′(i)` with `f′(i) = (xᵢ + yᵢ) / 2`
>
> Per bin:
> - i=1: `f′ = (5+8)/2 = 6.5` → `(5−6.5)²/6.5 = 2.25/6.5 ≈ 0.346`
> - i=2: `f′ = (5+5)/2 = 5.0` → `0/5 = 0`
> - i=3: `f′ = (5+4)/2 = 4.5` → `(5−4.5)²/4.5 = 0.25/4.5 ≈ 0.056`
> - i=4: `f′ = (5+3)/2 = 4.0` → `(5−4)²/4 = 1/4 = 0.25`
> - **Sum: `D_χ ≈ 0.346 + 0 + 0.056 + 0.25 = 0.652`**

## Common Pitfalls

- Calling the **semantic gap** "just an ML problem." It's a fundamental measurement-vs-perception mismatch — even an oracle ML model only *bridges* it, never eliminates it.
- Conflating **dominant color** with **colour histogram**. Dominant color is a compact summary (typically 3–5 colours with percentages); a histogram is a full distribution.
- For Task 4, mixing up the L/R block orientation — the 2-bit quantization is the **trap question**: it shows that quantization is not free.
- For Minkowski, forgetting to take the `1/p` power at the end. `L₁` = sum, `L₂` = square root of sum of squares, `L∞` = max.

## Official Solutions (Solution Document)

> [!info]- Additional Solutions from 25-Page Solution Document
> 
> **CBR — Feature Extraction + Matching:**
> Content-Based Retrieval (CBR) consists of two main phases:
> 1. **Feature extraction**: compute feature vectors from multimedia objects (color histograms, texture descriptors, shape features)
> 2. **Matching**: compare query feature vector against database feature vectors using a distance metric
> 
> **ABIR (Annotation-Based Image Retrieval) Limitations:**
> - **Annotation cost**: manual labeling is expensive and time-consuming
> - **Subjectivity**: different annotators may describe the same image differently
> - **Vocabulary problem**: limited set of keywords cannot capture all visual concepts
> - **Scalability**: annotation does not scale to large collections
> 
> **CBIR (Content-Based Image Retrieval) Limitations:**
> - **Semantic gap**: low-level features (color, texture) do not capture high-level concepts ("beach", "party")
> - **Need example image**: query-by-example requires the user to provide a sample image
> - **Feature selection**: choosing the right features for a specific task is non-trivial
> - **Interpretability**: users cannot easily specify what they want ("more red, less texture")
> 
> **Feature Vectors:**
> - **Definition**: n-dimensional numerical representation of multimedia content
> - **Curse of dimensionality**: as dimensionality increases, distances between points become nearly equal, making nearest-neighbor search meaningless. Indexes (k-d trees, R-trees) degrade to linear scan above ~20 dimensions.
> 
> **Dominant Color Descriptor (MPEG-7):**
> - **Formal definition**: F = {(cᵢ, pᵢ, vᵢ), s} where:
>   - cᵢ = color value (RGB or other color space)
>   - pᵢ = percentage of pixels with this dominant color
>   - vᵢ = color variance (standard deviation within the cluster)
>   - s = spatial coherency (how clustered the color is spatially)
> - **Compact representation**: typically 3-8 dominant colors capture the essential color information
> - **Example**: sunset image → {(orange, 0.4, 0.05), (red, 0.3, 0.08), (purple, 0.2, 0.1), (black, 0.1, 0.02)}, s=0.7
> 
> **Color Histograms with 8-Bin Uniform Quantization:**
> 
> Given two 4×4 images (16 pixels each):
> - Image 1: H1 = (0, 0, 0, 0, 8, 0, 0, 8) — 8 pixels in bin 4, 8 pixels in bin 7
> - Image 2: H2 = (8, 0, 0, 0, 0, 0, 0, 8) — 8 pixels in bin 0, 8 pixels in bin 7
> 
> **Minkowski Distances:**
> 
> L_p(P, Q) = (Σ|pᵢ - qᵢ|^p)^(1/p)
> 
> - **L1 (Manhattan)**: Σ|pᵢ - qᵢ| = |0-8| + |0-0| + |0-0| + |0-0| + |8-0| + |0-0| + |0-0| + |8-8| = 8 + 8 = **16**
>   - Note: The solution document states L1=32, which may refer to a different histogram pair or a doubled computation.
> - **L2 (Euclidean)**: √(Σ(pᵢ - qᵢ)²) = √(8² + 8²) = √128 ≈ **11.31**
> - **L∞ (Chebyshev)**: max|pᵢ - qᵢ| = **8**
> 
> **Kolmogorov-Smirnov Distance (Unnormalized):**
> 
> Given H1 = (5, 5, 5, 5) and H2 = (8, 5, 4, 3):
> 
> KS(P, Q) = max_i |cumsum(H1)_i - cumsum(H2)_i|
> 
> - cumsum(H1) = (5, 10, 15, 20)
> - cumsum(H2) = (8, 13, 17, 20)
> - Differences: |5-8|=3, |10-13|=3, |15-17|=2, |20-20|=0
> - **KS = max(3, 3, 2, 0) = 3**
> 
> Note: This is the unnormalized KS distance. The normalized version (dividing by total count) gives KS = 3/20 = 0.15.
> 
> **Chi-Squared Distance:**
> 
> χ²(P, Q) = Σ (pᵢ - qᵢ)² / (pᵢ + qᵢ)
> 
> Given H1 = (5, 5, 5, 5) and H2 = (8, 5, 4, 3):
> 
> - Bin 1: (5-8)² / (5+8) = 9/13 ≈ 0.692
> - Bin 2: (5-5)² / (5+5) = 0/10 = 0
> - Bin 3: (5-4)² / (5+4) = 1/9 ≈ 0.111
> - Bin 4: (5-3)² / (5+3) = 4/8 = 0.5
> - **χ² = 0.692 + 0 + 0.111 + 0.5 ≈ 1.303**
> 
> Note: This formula differs from the one in the main solutions section (which uses f'(i) = (pᵢ + qᵢ)/2 and gives χ² ≈ 0.652). Both formulas are valid; the choice depends on the application.

## Related Lectures

- [[multimedia-databases-lecture-06]]
- [[content-based-retrieval]]
- [[feature-vector]]
- [[feature-extraction]]
- [[minkowski-distance]]
- [[chi-squared-distance]]
- [[kolmogorov-smirnov-distance]]
- [[curse-of-dimensionality]]
- [[color-histogram]]
- [[semantic-gap]]
- [[mpeg-7-descriptors]]
- [[dominant-color]]
=======
**Task 1.1: What does Content-Based Retrieval mean?**

CBR means searching for multimedia objects (images, audio, video) based on their *content* — features automatically extracted from the data (colour histograms, texture, shape, etc.) — rather than on manually assigned text annotations. The user issues a query (an example image, a sketch, or a feature vector) and the system returns the most similar objects in the database.

**Task 1.2: What are the components of a CBIR architecture? Explain the basic principle of each component using an example.**

1. **Feature extraction**: offline, every image in the database is processed to extract a feature vector (e.g., colour histogram, edge histogram, texture descriptor). Example: for each image, compute the 8-bin colour histogram.
2. **Indexing**: the feature vectors are stored in an index structure for fast nearest-neighbour search. Example: build a kd-tree on the histogram vectors.
3. **Query processing**: the user submits a query (an image, a sketch, or a vector). The system extracts the same kind of feature vector from the query.
4. **Similarity search**: the system computes the distance between the query feature vector and every (or the most promising) feature vector in the index. Example: compute L2 distance between histograms.
5. **Ranking and presentation**: results are sorted by similarity and presented to the user. Example: show the top-10 most similar images.

**Task 1.3: What is a feature vector?**

A feature vector is a compact numerical representation of a multimedia object's content. It is a point in a (typically high-dimensional) feature space where "distance" corresponds to "semantic similarity". Example: an 8-bin colour histogram is a feature vector in ℝ⁸.

**Task 1.4: Which problems occur when indexing feature vectors?**

- **Curse of dimensionality**: as the feature vector dimension grows, the index becomes less effective (all points become "equally close" in high dimensions)
- **High-dimensional nearest-neighbour search** is expensive and index quality degrades
- **Distance metric choice**: the right distance depends on the feature type and the application; wrong choice gives irrelevant results
- **Storage cost**: large feature vectors for large databases
- **Approximate vs exact tradeoffs**: exact NN search is expensive in high dimensions; approximate methods (LSH, HNSW) trade some accuracy for speed

### Task 2: CBR Terminology

**Task 2.1: Dominant Color**

A compact representation of the most prominent colours in an image (or region), typically a small set of (colour, percentage) pairs. Example: an image might have dominant colours red (40%), blue (30%), white (20%), black (10%). Used in MPEG-7's Dominant Color Descriptor.

**Task 2.2: Spatial Coherency**

The property that neighbouring pixels in an image tend to have similar values (or at least values that are not random). Exploited in compression (e.g., JPEG's DCT works on 8×8 blocks where pixels are coherent) and in segmentation (regions of similar colour/texture).

**Task 2.3: Distance Metrics**

A function d(P, Q) that quantifies the dissimilarity between two feature vectors. Common choices: L1 (Manhattan), L2 (Euclidean), L∞ (Chebyshev), Cosine distance, Mahalanobis, histogram-specific metrics (EMD, chi-squared, KS). The choice depends on the feature type and the application.

**Task 2.4: Curse of Dimensionality**

The phenomenon that, as the number of dimensions grows, the "volume" of the space grows exponentially, so data becomes sparse and many algorithms (nearest neighbour search, distance-based clustering) become ineffective or inefficient. In high dimensions, all points are roughly equidistant from a query, so the concept of "nearest" loses meaning.

**Task 2.5: Types of content-based queries**

- **Query by example (QBE)**: provide an example image; find similar images
- **Query by sketch**: provide a hand-drawn sketch; find images matching the sketch
- **Query by feature vector**: provide a numerical feature vector directly
- **Query by colour**: specify a colour distribution
- **Query by texture**: specify a texture pattern
- **Query by shape**: specify a shape (often as a sketch or contour)
- **Semantic / hybrid queries**: combine content features with text annotations

### Task 3: CBR systems — "Give me all images which contain a blue truck"

**Conditions**:
- The system must support **object-level retrieval** (not just whole-image similarity)
- Features for **object detection** and **localisation** (not just global descriptors)
- A **blue colour model** and a **truck shape model** in the feature space
- **Spatial relationship encoding** (the blue must be inside the truck)
- Possibly **semantic gap handling** — the system must understand "blue" and "truck" beyond low-level features

**Problems**:
- **Semantic gap**: low-level features (colour, edges) don't directly map to high-level concepts ("truck", "blue")
- **Object localisation**: detecting where in the image the truck is
- **Multiple objects**: the image may have a blue car and a red truck; the system must distinguish
- **Background clutter**: the truck is part of a complex scene
- **Pose and occlusion**: the truck may be viewed from different angles, partially occluded
- **Annotation dependency**: training an object detector requires labelled training data

### Task 4: Image indexing by colours

**Task 4.1: 8-colour even quantification**

With 8 colours, each colour falls into a quantification range of 256/8 = 32 consecutive values. So blue (128-159) and white (192-223) and black (0-31) and other colours map to discrete bin indices.

**Task 4.2: Colour histogram for both images**

For 8×8 = 64 pixels per image:
- Left image (8 blue + 56 white): histogram[blue_bin] = 8, histogram[white_bin] = 56, all others = 0
- Right image (32 black + 32 white): histogram[black_bin] = 32, histogram[white_bin] = 32, all others = 0

**Task 4.3: 2-bit even bin quantification**

2 bits = 4 bins. Each bin covers 256/4 = 64 consecutive values. So bin 0 = 0-63, bin 1 = 64-127, bin 2 = 128-191, bin 3 = 192-255.

### Task 5: Similarity of images

**Task 5.1: Minkowski Distances**

For histograms H1 (8 blue, 56 white) and H2 (32 black, 32 white), restricted to the relevant bins:
- L1 = |8-0| + |56-32| = 8 + 24 = 32
- L2 = √(8² + 24²) = √(64 + 576) = √640 ≈ 25.3
- L∞ = max(8, 24) = 24

If red is replaced by black in the left image: H1 = (8 black, 56 white). Then L1 = |8-32| + |56-32| = 24 + 24 = 48 — much larger. Conclusion: colour histogram distance is sensitive to colour shifts, even if the spatial structure is similar.

**Task 5.2: Non-parametrical Distances**

For H1 = (5, 5, 5, 5) and H2 = (8, 5, 4, 3):
- Kolmogorov-Smirnov: KS = max over i of |cumulative H1 - cumulative H2|
  - After 1: |5-8| = 3
  - After 2: |10-13| = 3
  - After 3: |15-17| = 2
  - After 4: |20-20| = 0
  - KS = 3
- Chi-squared: Σ (xi - fi')² / fi' where fi' = (xi + yi)/2
  - bin 1: (5-6.5)²/6.5 = 2.25/6.5 ≈ 0.346
  - bin 2: (5-5)²/5 = 0
  - bin 3: (5-4.5)²/4.5 = 0.25/4.5 ≈ 0.056
  - bin 4: (5-4)²/4 = 0.25
  - chi² ≈ 0.658

## Related Lectures
- [[multimedia-databases-lecture-06]]
- [[content-based-retrieval]]
- [[minkowski-distance]]
- [[chi-squared-distance]]
- [[kolmogorov-smirnov-distance]]
- [[feature-vector]]
- [[color-histogram]]
- [[curse-of-dimensionality]]
- [[dominant-color]]
- [[spatial-coherency]]
>>>>>>> 20ac138 (2nd week of june)
