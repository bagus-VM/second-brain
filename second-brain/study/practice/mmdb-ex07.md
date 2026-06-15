---
title: "Exercise Sheet 7 — Content-Based Retrieval"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-14
---

# Exercise Sheet 7 — Content-Based Retrieval

## Exercises

### Task 1: Content-Based Retrieval (CBR)

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
