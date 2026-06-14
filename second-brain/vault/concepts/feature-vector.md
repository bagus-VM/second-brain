---
title: "Feature Vector"
tags: [concept, multimedia-databases, semester-1, feature-vector, feature-extraction, cbr]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[multimedia-annotation]]", "[[feature-extraction]]"]
---

## One-line Summary
A feature vector is a numerical representation of a multimedia object's content — a point in a (typically high-dimensional) feature space where distance between vectors corresponds to semantic similarity between objects.

## Core Intuition
Computers can't directly compare images, audio, or video. They need a numerical representation that captures the *important* properties. A **feature vector** is that representation: a list of numbers where each number measures some property of the object.

For images, common features include:
- **Colour**: 8-bin colour histogram (8 numbers)
- **Texture**: Gabor filter responses, LBP histogram (often 50-100 numbers)
- **Shape**: Fourier descriptors, moments (10-50 numbers)
- **Local features**: SIFT/SURF keypoints (128 numbers per keypoint)
- **Deep embeddings**: CNN feature maps (256-2048 numbers)

The choice of feature vector is the central design decision in a CBR system. It determines what "similar" means.

## Formal Definition / Statement

A **feature vector** for a multimedia object I is a vector f(I) = (f₁, f₂, ..., f_n) ∈ ℝⁿ where each fᵢ is a numerical measurement of some property of I.

A **feature space** is the set of all possible feature vectors, with a distance function d: ℝⁿ × ℝⁿ → ℝ quantifying dissimilarity.

**Feature extraction** is the process of computing f(I) for a given object I. This is typically done by image processing algorithms (e.g., colour histogram computation, edge detection, CNN forward pass).

**Properties of good feature vectors**:
- **Discriminative**: similar objects have similar vectors, dissimilar objects have different vectors
- **Compact**: low enough dimension for efficient indexing
- **Invariant**: small changes in the object (rotation, translation, lighting) don't drastically change the vector
- **Robust**: noise, compression artifacts, and other perturbations don't drastically change the vector
- **Efficient to compute**: feature extraction shouldn't take longer than the query

## Key Properties

### Common feature types

| Feature | Dimensionality | Captures | Example |
|---------|---------------|----------|---------|
| Colour histogram (8 bins) | 8 | Colour distribution | Sunset images have red/orange-heavy histograms |
| Colour histogram (256 bins) | 256 | Fine-grained colour distribution | Distinguishes similar reds |
| Gabor texture | 48-128 | Texture at multiple scales/orientations | Distinguishes fabric textures |
| LBP (Local Binary Patterns) | 256 | Local texture patterns | Distinguishes smooth from rough surfaces |
| SIFT keypoint descriptor | 128 per keypoint | Local image patches | Robust to scale/rotation |
| HOG (Histogram of Gradients) | Variable | Edge orientations | Distinguishes shapes |
| CNN embeddings (ResNet) | 2048 | High-level visual concepts | "Beach", "car", "cat" |
| Colour moments (mean, std, skew) | 9 (3 colours × 3 stats) | Colour distribution | Compact colour description |

### The discriminative-vs-compact tradeoff
- **High-dimensional features** (e.g., CNN embeddings) are more discriminative but harder to index
- **Low-dimensional features** (e.g., colour moments) are compact and easy to index but less discriminative
- **Hybrid approaches**: combine multiple features (colour + texture + shape) for better discrimination
- **Deep learning approach**: a single CNN embedding can replace many hand-crafted features

### Invariance requirements
- **Translation invariance**: shifting the image shouldn't change the feature vector (colour histogram is translation-invariant; SIFT is too)
- **Rotation invariance**: rotating the image shouldn't change the feature vector (SIFT is rotation-invariant; raw pixels are not)
- **Scale invariance**: scaling the image shouldn't change the feature vector (SIFT is scale-invariant)
- **Illumination invariance**: changing lighting shouldn't change the feature vector (colour histograms in HSV are more illumination-invariant than RGB)

### The curse of dimensionality
- For n dimensions, the number of possible feature vectors grows exponentially
- Nearest-neighbour search becomes inefficient above ~20 dimensions for kd-trees
- For higher dimensions, use LSH, HNSW, or dimensionality reduction (PCA, t-SNE)
- Modern deep embeddings (512-2048 dim) require specialised indexes

## Worked Example

Consider a simple colour-based feature vector for two images:
- Image A (sunset over ocean): pixel colours are mostly orange, red, blue
- Image B (fire in fireplace): pixel colours are mostly orange, red, black

A 4-bin colour histogram (white, grey, black, colour):
- Image A: [0.05, 0.10, 0.05, 0.80] (mostly colour)
- Image B: [0.05, 0.10, 0.30, 0.55] (significant black, but still colour-heavy)

The colour histograms are similar (both colour-heavy) but Image B has more black (from the fireplace). The system ranks Image A and Image B as similar, even though they're semantically very different (sunset vs fire).

A more discriminative feature would also encode spatial layout, texture, or high-level concepts. Deep CNN embeddings would likely separate these two images cleanly.

## Common Pitfalls
- **Choosing a feature that captures the wrong property**: colour histogram for image similarity misses texture, shape, and semantic content.
- **Ignoring invariance requirements**: if your feature is not translation-invariant, the same object at different positions in the image will look different.
- **Using too high a dimension without proper indexing**: 2048-dim CNN embeddings need HNSW or similar indexes, not linear scan.
- **Not normalising features**: features with different scales (e.g., one dimension ranges 0-1, another 0-1000000) need normalisation before distance computation.
- **Forgetting about computational cost**: SIFT extraction is fast; deep CNN extraction is slower. For large databases, the bottleneck is often extraction, not search.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[feature-extraction]] — the process of computing the vector
- [[similarity-measures]] — the distance functions on feature vectors
- [[color-histogram]] — a specific feature type
- [[dominant-color]] — a compact colour feature
- [[multimedia-annotation]] — the alternative (text-based) approach
- [[minkowski-distance]] — common distance functions
- [[curse-of-dimensionality]] — the scaling challenge
- [[hierarchical-navigable-small-world|HNSW]] — modern high-dimensional indexing
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- Are hand-crafted features (colour, texture, shape) obsolete in the era of deep learning? Or do they still have a place for interpretability and efficiency?
- How do you choose the right feature for a specific CBR task? (Empirically, by testing on a labelled dataset.)
- Can feature vectors be made *adversarially robust*? (Right now, small perturbations to the image can cause large changes in the feature vector.)
- How do you handle multi-modal data (e.g., an image with text)? One feature vector per modality, then a fusion step.
