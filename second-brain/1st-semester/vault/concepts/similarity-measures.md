---
title: "Similarity Measures"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Similarity measures quantify how "close" two multimedia objects are based on their feature representations, enabling ranked retrieval in content-based systems.

## Core Intuition
Once you have feature vectors (from [[feature-extraction]]), you need a way to say "image A is more similar to image B than to image C." Similarity measures are mathematical functions that take two feature vectors and return a distance or similarity score. The choice of measure significantly impacts retrieval quality — Euclidean distance works well for colour histograms, but cosine similarity might be better for texture features.

## Formal Definition / Statement
A similarity measure is a function d(x, y) that maps two feature vectors x, y to a real-valued score, where lower values (distance) or higher values (similarity) indicate greater resemblance.

**Common measures:**
- **Euclidean distance (L2)**: d(x,y) = √Σ(xᵢ - yᵢ)²
- **Manhattan distance (L1)**: d(x,y) = Σ|xᵢ - yᵢ|
- **Cosine similarity**: cos(x,y) = (x·y)/(||x||·||y||)
- **Histogram intersection**: Σmin(xᵢ, yᵢ)
- **Mahalanobis distance**: accounts for feature correlations
- **Earth Mover's Distance (EMD)**: optimal transport between distributions
- **Dynamic Time Warping (DTW)**: for temporal sequences

## Key Properties / Complexity
- Must satisfy: non-negativity, identity (d(x,x)=0), symmetry
- Metric properties (triangle inequality) enable indexing optimizations
- Choice depends on feature type: histogram features → histogram intersection; vector features → L2/cosine
- Perceptual similarity ≠ mathematical similarity — the [[semantic-gap]] persists
- [[relevance-feedback]] can learn user-specific similarity functions

## Worked Example
Comparing two colour histograms:
- Image A: [0.1, 0.3, 0.2, 0.4] (4 bins)
- Image B: [0.2, 0.3, 0.1, 0.4]
- Image C: [0.4, 0.1, 0.3, 0.2]

Euclidean distance: d(A,B) = √(0.01+0+0.01+0) = 0.141
Euclidean distance: d(A,C) = √(0.09+0.04+0.01+0.04) = 0.424

→ A is more similar to B than to C (by colour distribution).

## Common Pitfalls
- Using Euclidean distance for all feature types (inappropriate for histograms, sequences)
- Ignoring feature normalization — features with larger ranges dominate the distance
- Assuming one measure works for all queries — different content types may need different measures
- Forgetting that similarity is perceptually subjective — no single measure captures human perception

## Connections
- [[feature-extraction]] — provides the vectors that similarity measures operate on
- [[content-based-retrieval]] — similarity measures are the core of CBR
- [[mpeg-7-descriptors]] — each descriptor type suggests appropriate similarity measures
- [[relevance-feedback]] — learns user-specific similarity
- [[semantic-gap]] — mathematical similarity ≠ semantic similarity

## Open Questions
- Can learned metric spaces (triplet loss, contrastive learning) replace hand-designed measures?
- How to combine multiple similarity measures for multi-feature retrieval?
- What is the role of similarity measures in the age of neural retrieval?
