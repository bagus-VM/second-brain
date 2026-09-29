---
title: "Multimedia Databases Ex07 — Content-Based Retrieval Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-14
---

# Flashcards — Exercise Sheet 7 (Content-Based Retrieval)

> [!question]- What is Content-Based Retrieval (CBR)?
> [!answer]- Searching for multimedia objects (images, audio, video) based on their *automatically extracted content* (colour histograms, texture, shape), not on manually assigned text annotations. The user submits a query (example image, sketch, or feature vector) and gets the most similar objects back.

> [!question]- What are the five components of a CBIR architecture?
> [!answer]- (1) **Feature extraction** — derive feature vectors from media; (2) **Indexing** — store vectors in an index (kd-tree, HNSW, etc.); (3) **Query processing** — extract features from the query; (4) **Similarity search** — compute distance to indexed vectors; (5) **Ranking and presentation** — sort and show top results.

> [!question]- What is a feature vector?
> [!answer]- A compact numerical representation of a multimedia object's content — a point in a (typically high-dimensional) feature space where distance corresponds to semantic similarity. Example: an 8-bin colour histogram is a feature vector in ℝ⁸.

> [!question]- What is the curse of dimensionality?
> [!answer]- As the feature dimension grows, the volume of the space grows exponentially, so data becomes sparse. Nearest-neighbour search loses meaning because all points become roughly equidistant from any query. Indexing structures (kd-trees) become ineffective above ~20 dimensions.

> [!question]- What is "dominant color" in MPEG-7?
> [!answer]- A compact representation of the most prominent colours in an image, typically a small set of (colour, percentage) pairs. Used for scalable content description; the Dominant Color Descriptor can be matched efficiently with Earth Mover's Distance.

> [!question]- What is spatial coherency?
> [!answer]- The property that neighbouring pixels in an image tend to have similar values. Exploited in compression (JPEG DCT on 8×8 blocks), segmentation (regions of similar colour), and many CBIR features. Lack of spatial coherency implies noise or texture.

> [!question]- What are the three main types of CBR queries?
> [!answer]- (1) **Query by example (QBE)** — provide an example image; (2) **Query by sketch** — provide a hand-drawn sketch; (3) **Query by feature vector** — provide a numerical vector directly. Plus hybrids: query by colour, by texture, by shape, by semantics.

> [!question]- What is the Minkowski Lp distance?
> [!answer]- Lp(P, Q) = (Σᵢ |pᵢ - qᵢ|ᵖ)^(1/p). Special cases: p=1 is Manhattan (L1), p=2 is Euclidean (L2), p=∞ is Chebyshev (L∞ = max|pᵢ - qᵢ|). For histograms, L1 and L2 are common; for sparse vectors, cosine is often used.

> [!question]- What does the Kolmogorov-Smirnov distance measure for histograms?
> [!answer]- The maximum absolute difference between the cumulative distributions of the two histograms: KS(P, Q) = maxᵢ |cum(i, P) - cum(i, Q)|. It captures the worst-case cumulative difference, not the per-bin difference.

> [!question]- What does the chi-squared distance measure?
> [!answer]- A normalised sum of squared differences: χ²(P, Q) = Σᵢ (pᵢ - f'ᵢ)² / f'ᵢ where f'ᵢ = (pᵢ + qᵢ)/2. The denominator normalises by the expected count, so bins with small values don't dominate. Useful for comparing histograms with varying scales.

> [!question]- Why is "find all images with a blue truck" hard for CBR?
> [!answer]- Requires **object-level retrieval** (not whole-image similarity), **localisation** (where is the truck), **spatial reasoning** (the blue must be inside the truck), and **semantic gap handling** (mapping "truck" and "blue" to features). Traditional CBR works at the whole-image level, not object level.

> [!question]- What is the difference between a query by example and a query by sketch?
> [!answer]- QBE: provide an existing image, the system extracts its features and finds similar images. Query by sketch: provide a hand-drawn sketch, the system extracts shape/edge features and finds images matching the sketch structure (regardless of colour). Both bypass text annotation.


---

## Related Resources

### 📖 Multimedia Databases - Lecture 06: Modeling
- Lecture topic: [[multimedia-databases-lecture-06]]

**Key concepts covered:**
- [[multimedia-annotation]]
- [[sensory-gap]]
- [[semantic-gap]]
- [[multimedia-metadata]]
- [[mpeg-7]]
- [[mpeg-7-ddl]]
- [[mpeg-7-structural-description]]
- [[mpeg-7-semantic-description]]
- [[mpeg-7-indexing-pyramid]]
- [[mpeg-7-descriptors]]
- [[classification-schemes]]
- [[feature-extraction]]
- [[content-based-retrieval]]
- [[similarity-measures]]
- [[relevance-feedback]]

### 📖 Multimedia Databases - Lecture 07: Content-Based Image Retrieval
- Lecture topic: [[multimedia-databases-lecture-07]]

**Key concepts covered:**
- [[content-based-retrieval]]
- [[feature-vector]]
- [[mpeg-7-descriptors]]
- [[query-by-example-and-feature]]
- [[color-histogram]]
- [[minkowski-distance]]
- [[chi-squared-distance]]
- [[cbir-systems-evaluation]]
- [[dominant-color]]
- [[spatial-coherency]]
- [[kolmogorov-smirnov-distance]]
