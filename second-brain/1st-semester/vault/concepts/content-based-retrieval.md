---
title: "Content-Based Retrieval (CBR)"
tags: [concept, multimedia-databases, semester-1, content-based-retrieval, cbr]
course: "Multimedia Databases"
source_count: 2
status: current
last_updated: 2026-06-25
prerequisites: ["[[multimedia-database-intro]]", "[[feature-vector]]", "[[multimedia-query-predicates]]"]
---

## One-line Summary
Content-based retrieval (CBR) is the search paradigm where multimedia objects are retrieved by their *automatically extracted content* (colour, texture, shape) — represented as a [[feature-vector|feature vector]] — rather than by manually assigned text annotations.

## Core Intuition
Text-based retrieval requires someone to *manually* describe each image with words ("beach", "sunset"). This is expensive, subjective, and incomplete. Content-based retrieval skips the text: it extracts numerical features from the image itself (e.g., a 256-bin colour histogram), and the user issues queries by example ("find images similar to this one") or by feature values.

The challenge: bridging the [[semantic-gap|semantic gap]] between low-level features (numbers) and high-level concepts ("a beach with a sunset"). Modern CBR combines low-level features with machine learning, relevance feedback, and increasingly with deep neural embeddings.

## Formal Definition / Statement

A **CBR system** for image retrieval has five components:
1. **Feature extraction**: offline, for each image I in the database, compute a feature vector f(I) ∈ ℝⁿ
2. **Indexing**: store {f(I)} in an index structure for fast nearest-neighbour search
3. **Query processing**: the user submits a query Q (an example image, a sketch, or a feature vector); extract f(Q)
4. **Similarity search**: compute the distance d(f(Q), f(I)) for each (or the most promising) image I in the database
5. **Ranking and presentation**: sort by distance, show the top-k most similar images

The distance function depends on the feature type:
- **Colour histograms**: L1, L2, [[chi-squared-distance|chi-squared]], [[kolmogorov-smirnov-distance|Kolmogorov-Smirnov]], Earth Mover's Distance
- **Texture features**: L2 on the texture descriptor vectors
- **Shape features**: L2 on the shape descriptor vectors, or specialised shape-distance metrics
- **Deep embeddings**: cosine distance, L2

## Key Properties / Complexity

### Why CBR
- **No manual annotation needed** — the system extracts features automatically
- **Consistent** — same image always gets the same features (unlike text annotations)
- **Scalable** — once features are extracted, similarity search is fast (with proper indexing)
- **Multilingual** — features don't depend on the language of the user

### Why CBR is hard
- **Semantic gap**: low-level features don't directly map to high-level concepts
- **Curse of dimensionality**: feature vectors are often high-dimensional; nearest-neighbour search becomes inefficient
- **Subjectivity of similarity**: what one user finds "similar", another doesn't
- **User intent is hard to capture**: a query image might be an example of colour, composition, subject, or style
- **Relevance feedback is needed**: the user must iterate to refine the query

### The five steps in detail
1. **Feature extraction**: image processing algorithms extract numerical descriptors. Common choices: colour histograms (RGB, HSV, Lab), texture features (Gabor filters, LBP), shape features (Fourier descriptors, moments), SIFT/SURF keypoints, deep CNN embeddings.
2. **Indexing**: high-dimensional indexing structures — kd-trees (for low dimensions), VP-trees, LSH, [[hierarchical-navigable-small-world|HNSW]] (for high dimensions).
3. **Query processing**: the user submits a query; the system extracts features using the *same* algorithms as in step 1. Two query modes drive the interactive loop: [[query-by-example-and-feature|QBE]] (submit a sample image, precise narrowing) and [[query-by-example-and-feature|QBF]] (submit feature values, exploratory widening). The result page reports both matching images (for further QBE) and their features (for further QBF).
4. **Similarity search**: compute distances. For top-k queries, use the index to find candidates. For full-rank queries, scan all images.
5. **Ranking and presentation**: sort by distance; present top-k. May include relevance feedback (user marks results as relevant/irrelevant, system refines the query).

### The curse of dimensionality
- For n = 256 (an 8-bit colour histogram), there are 256^256 possible histograms
- As n grows, the space becomes exponentially sparse
- All points become roughly equidistant from any query → "nearest" loses meaning
- Standard kd-trees become ineffective above ~20 dimensions
- Modern solutions: LSH, HNSW, dimensionality reduction (PCA), product quantization

## Worked Example

A simple colour-based CBR system:
- Database: 10,000 images
- Features: 8-bin colour histogram (RGB reduced to 8 representative colours)
- Index: linear scan (10,000 images is small enough)
- Query: user uploads an image of a sunset
- System: extracts the query's 8-bin histogram
- Distance: L1 between query histogram and each database histogram
- Result: top 10 images by L1 distance — most should be sunsets (orange/red heavy)

Limitations:
- An image of a fire and an image of a sunset have similar colour histograms (both orange/red heavy), but they're semantically different
- The system doesn't know "fire" and "sunset" are different concepts
- Relevance feedback could help: user marks some fire images as "not relevant", system refines the query

## Common Pitfalls
- **Confusing CBR with keyword search**: they're complementary, not the same. Most modern systems combine both.
- **Choosing the wrong distance metric**: L2 is not always best for histograms. For sparse histograms, chi-squared or KL-divergence often works better.
- **Ignoring the semantic gap**: low-level features can find "visually similar" images but not "semantically similar" ones. User expectations may not match the system's capabilities.
- **Not using relevance feedback**: the user's first query is rarely the right one. Iterative refinement is essential.
- **High-dimensional indexing**: kd-trees break down above ~20 dimensions. Use LSH, HNSW, or dimensionality reduction.

## Connections
- [[feature-vector]] — the core representation
- [[multimedia-query-predicates]] — the query language
- [[similarity-measures]] — the distance functions
- [[semantic-gap]] — the central challenge
- [[hierarchical-navigable-small-world|HNSW]] — modern high-dimensional indexing
- [[minkowski-distance]] — the Lp family
- [[chi-squared-distance]] — for histograms
- [[kolmogorov-smirnov-distance]] — for cumulative distributions
- [[color-histogram]] — the most common low-level feature
- [[dominant-color]] — MPEG-7's compact colour representation
- [[spatial-coherency]] — exploited in compression and segmentation
- [[curse-of-dimensionality]] — the central scaling challenge
- [[query-by-example-and-feature]] — the two query modes (QBE/QBF) that drive the interactive CBR loop
- [[cbir-systems-evaluation]] — precision, recall, MAP for measuring CBR system quality
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- How do modern deep learning approaches (CNN embeddings, contrastive learning) change CBR? Are they a replacement for hand-crafted features, or a complement?
- How can CBR systems be made *interactive* — using relevance feedback and active learning to refine the user's intent?
- How do you evaluate a CBR system? (Precision, recall, mean reciprocal rank — but these are hard to measure without ground truth.)
- For very large databases (billions of images), how do you scale CBR? Approximate methods, distributed indexes, GPU acceleration.
