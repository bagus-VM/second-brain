---
title: "Minkowski Distance"
tags: [concept, multimedia-databases, semester-1, distance-metric, minkowski, similarity]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]", "[[similarity-measures]]"]
---

## One-line Summary
The Minkowski distance Lp is a family of distance functions generalising Manhattan (p=1), Euclidean (p=2), and Chebyshev (p=∞) — the most common distance functions on feature vectors in CBR.

## Core Intuition
Given two feature vectors P = (p₁, ..., p_n) and Q = (q₁, ..., q_n), the Minkowski Lp distance is:

    Lp(P, Q) = (Σᵢ |pᵢ - qᵢ|^p)^(1/p)

- **p = 1**: Manhattan distance (sum of absolute differences)
- **p = 2**: Euclidean distance (square root of sum of squared differences)
- **p = ∞**: Chebyshev distance (max absolute difference)

Each p value gives a different notion of "similarity". For most CBR applications, p = 1 or p = 2 are used.

## Formal Definition / Statement

For p ≥ 1, the **Minkowski Lp distance** between P and Q is:

    Lp(P, Q) = (Σᵢ₌₁ⁿ |pᵢ - qᵢ|^p)^(1/p)

Special cases:
- **L1 (Manhattan)**: Σ |pᵢ - qᵢ| — the "taxicab" distance; sum of absolute differences
- **L2 (Euclidean)**: √(Σ (pᵢ - qᵢ)²) — the familiar straight-line distance
- **L∞ (Chebyshev)**: max |pᵢ - qᵢ| — the worst-case coordinate difference

For histograms, the Lp distances are common but not always the best choice. Alternatives include chi-squared, KL-divergence, and Earth Mover's Distance.

## Key Properties / Complexity

### When to use L1 vs L2
- **L1 is more robust to outliers**: a single large coordinate difference doesn't dominate
- **L2 is the most common default**: mathematically natural, geometric interpretation
- **L1 is preferred for sparse data**: e.g., bag-of-words text features
- **L2 is preferred for dense data**: e.g., image pixels, CNN embeddings
- **L∞ is the worst-case measure**: useful when any single dimension mismatch is unacceptable

### Properties of Lp distances
- **Non-negativity**: d(P, Q) ≥ 0, with equality iff P = Q
- **Symmetry**: d(P, Q) = d(Q, P)
- **Triangle inequality**: d(P, R) ≤ d(P, Q) + d(Q, R)
- These make Lp a proper **metric** for p ≥ 1

### Why Lp is a metric only for p ≥ 1
For 0 < p < 1, the triangle inequality fails. The "distance" is still useful for some applications (e.g., sparse representations) but is not a true metric.

### Practical considerations
- **Normalisation**: features with different scales (e.g., 0-1 and 0-1000000) need normalisation before Lp makes sense
- **Weighted Lp**: each dimension can be weighted to reflect its importance: Σ wᵢ |pᵢ - qᵢ|^p)^(1/p)
- **High dimensions**: Lp becomes less meaningful as the number of dimensions grows (curse of dimensionality)

## Worked Example

Two colour histograms, each with 3 bins (red, green, blue):
- P = (0.5, 0.3, 0.2) (mostly red)
- Q = (0.4, 0.4, 0.2) (red-green balanced)

- L1 = |0.5-0.4| + |0.3-0.4| + |0.2-0.2| = 0.1 + 0.1 + 0 = 0.2
- L2 = √(0.1² + 0.1² + 0²) = √0.02 ≈ 0.141
- L∞ = max(0.1, 0.1, 0) = 0.1

All three agree that P and Q are similar (small distance). L1 is the largest because it sums up; L∞ is the smallest because it only takes the maximum.

If the red bins differed by 0.5 (P = (0.5, 0.3, 0.2), Q = (0.0, 0.7, 0.3)):
- L1 = 0.5 + 0.4 + 0.1 = 1.0
- L2 = √(0.25 + 0.16 + 0.01) = √0.42 ≈ 0.648
- L∞ = 0.5

L2 is more forgiving of the 0.5 difference (only squared to 0.25, not added linearly). For noisy data, L1 might be preferred.

## Common Pitfalls
- **Not normalising features**: if P = (0.5, 300) and Q = (0.6, 400), the second dimension dominates. Normalise or weight the features.
- **Using Lp for histograms without thinking**: chi-squared or KL-divergence are often better for histograms (they account for the scale of each bin).
- **Using L2 for sparse high-dimensional data**: the distance is dominated by the few non-zero dimensions. Cosine similarity is often better.
- **Forgetting the triangle inequality**: if your "distance" function doesn't satisfy it, you can't use it with metric-based indexes (e.g., VP-trees).

## Connections
- [[content-based-retrieval]] — the broader topic
- [[feature-vector]] — what Lp operates on
- [[similarity-measures]] — the broader family
- [[chi-squared-distance]] — better for histograms
- [[kolmogorov-smirnov-distance]] — for cumulative distributions
- [[curse-of-dimensionality]] — limits Lp's effectiveness in high dimensions
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- For multimedia features, which p value is best in practice? (Often 1 or 2; depends on the feature type.)
- How do you choose weights for weighted Lp? (Empirically, by optimising on a labelled dataset.)
- Are there distance functions that adaptively choose p per dimension? (Yes — learned distance metrics, Mahalanobis distance.)
- For high-dimensional embeddings, is cosine similarity always better than L2? (Often, but not always — depends on the embedding normalisation.)
