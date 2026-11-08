---
title: "Chi-Squared Distance"
tags: [concept, multimedia-databases, semester-1, distance-metric, chi-squared, histograms, similarity]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[minkowski-distance]]", "[[feature-vector]]", "[[similarity-measures]]"]
---

## One-line Summary
The chi-squared distance is a normalised, scale-sensitive distance for histograms: it divides the squared difference by the expected count, so bins with small values don't dominate and bins with large values don't dominate either.

## Core Intuition
For histograms, the standard Lp distances have a problem: if a bin has 0.001 of the mass and another has 0.5, the L2 distance treats them equally per bin, but the 0.5 bin is 500x more important than the 0.001 bin. The chi-squared distance handles this by normalising by the expected count — the per-bin difference is weighted by the inverse of the expected count.

For two histograms P = (p₁, ..., p_n) and Q = (q₁, ..., q_n):

    χ²(P, Q) = Σᵢ (pᵢ - f'ᵢ)² / f'ᵢ

where f'ᵢ = (pᵢ + qᵢ) / 2 is the "expected" count (the average of the two).

The denominator f'ᵢ makes the distance *invariant to scale*: a difference of 10 in a bin with expected count 1000 contributes much less than a difference of 10 in a bin with expected count 100.

## Formal Definition / Statement

The **chi-squared distance** between two histograms P and Q is:

    χ²(P, Q) = Σᵢ (pᵢ - f'ᵢ)² / f'ᵢ

where f'ᵢ = (pᵢ + qᵢ) / 2.

Equivalent formulation (more common in statistics):

    χ²(P, Q) = Σᵢ (pᵢ - qᵢ)² / (pᵢ + qᵢ)

(both forms give the same result, just algebraically rearranged)

Properties:
- **Non-negative**: χ² ≥ 0
- **Symmetric**: χ²(P, Q) = χ²(Q, P)
- **Zero only when equal**: χ²(P, Q) = 0 iff P = Q
- **Does not satisfy the triangle inequality** in general, so it's a "divergence" not a strict metric

## Key Properties / Complexity

### Why chi-squared is good for histograms
- **Scale-sensitive**: bins with small counts are penalised more (relative to their magnitude)
- **Scale-invariant**: doubling both P and Q doesn't change the distance
- **Robust to outliers**: a single very large bin doesn't dominate (because the denominator grows with the bin's expected count)
- **Standard in statistics**: used for goodness-of-fit tests; well-understood properties

### When to use chi-squared vs Lp
- **Chi-squared**: histograms with very different scales across bins, or when you want scale-invariance
- **L1 or L2**: dense features (image pixels, CNN embeddings) where all dimensions have similar scales
- **KL-divergence**: when one histogram is a "true" distribution and the other is an "approximation"
- **Earth Mover's Distance**: when you care about the "work" to transform one histogram to another

### The two formulations
The "f'ᵢ = (pᵢ + qᵢ) / 2" form is what the lecture gives. The "f'ᵢ = pᵢ + qᵢ" form (without the 1/2) is equivalent up to a constant factor — both are used. The "1/2" version is more common because it has a nice probabilistic interpretation (variance of a Bernoulli).

### Interpretation
- χ² ≈ 0: P and Q are very similar
- χ² ≈ 1: P and Q have noticeable differences
- χ² >> 1: P and Q are very different (statistically significant difference)

The exact threshold depends on the number of bins and the application.

## Worked Example

Two histograms with 4 bins:
- P = (5, 5, 5, 5) (uniform)
- Q = (8, 5, 4, 3) (slightly skewed)

Compute chi-squared:
- Bin 1: (5-6.5)² / 6.5 = 2.25/6.5 ≈ 0.346
- Bin 2: (5-5)² / 5 = 0
- Bin 3: (5-4.5)² / 4.5 = 0.25/4.5 ≈ 0.056
- Bin 4: (5-4)² / 4 = 0.25
- χ² ≈ 0.346 + 0 + 0.056 + 0.25 ≈ 0.658

Compare to L1 = |5-8| + |5-5| + |5-4| + |5-3| = 3 + 0 + 1 + 2 = 6
Compare to L2 = √(9 + 0 + 1 + 4) = √14 ≈ 3.74

The chi-squared distance (0.658) is much smaller than L1 (6) and L2 (3.74) because the normalising denominator reduces the contribution of large-magnitude bins. This is the *scale-invariance* in action.

If we scale both histograms by 1000 (P = (5000, 5000, 5000, 5000), Q = (8000, 5000, 4000, 3000)):
- χ² = same as before (0.658) — the normalising denominator scales with the data
- L1 = 6000, L2 = 3740 — both scaled up

This is why chi-squared is preferred for histograms with very different scales.

## Common Pitfalls
- **Bins with zero count in both P and Q**: f'ᵢ = 0, division by zero. Convention: skip such bins (their contribution is 0 anyway).
- **Asymmetric interpretation**: chi-squared is symmetric in P and Q, but if you treat them asymmetrically (e.g., "P is the truth, Q is the approximation"), consider KL-divergence instead.
- **Doesn't satisfy triangle inequality**: can't use with metric-based indexes (VP-trees, ball trees). Need to use chi-squared-specific indexes or accept linear scan.
- **Confusing with chi-squared test**: the chi-squared *test* uses the same statistic but with a different denominator (expected counts from a hypothesis). The *distance* is the statistic itself, without the statistical test.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[minkowski-distance]] — the alternative
- [[kolmogorov-smirnov-distance]] — another histogram distance
- [[feature-vector]] — what the distance operates on
- [[similarity-measures]] — the broader family
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- For very sparse histograms (many zero bins), is chi-squared the right choice, or should you use a different distance (e.g., Hellinger, Bray-Curtis)?
- How do you choose the bin size for the histogram? (Affects the chi-squared distance significantly.)
- For multi-dimensional histograms (e.g., joint colour-texture), is chi-squared still the right distance?
- Can chi-squared be combined with deep learning? (Train an embedding where chi-squared is the natural distance.)
