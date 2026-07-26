---
title: "Kolmogorov-Smirnov Distance"
tags: [concept, multimedia-databases, semester-1, distance-metric, kolmogorov-smirnov, histograms, similarity]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[minkowski-distance]]", "[[chi-squared-distance]]", "[[feature-vector]]"]
---

## One-line Summary
The Kolmogorov-Smirnov (KS) distance is the maximum absolute difference between the cumulative distributions of two histograms — it captures the worst-case cumulative difference, not the per-bin difference.

## Core Intuition
For two histograms P and Q, the KS distance asks: "what is the maximum gap between the cumulative distributions at any point along the bins?" The cumulative distribution at bin i is the sum of all bins up to i.

The intuition: instead of looking at *individual* bin differences, look at the *worst case* across the whole cumulative. If two histograms have a few bins that are very different but the cumulative is still close, the KS distance is small. If two histograms have similar per-bin values but one cumulative is consistently higher than the other, the KS distance is large.

## Formal Definition / Statement

The **Kolmogorov-Smirnov distance** between two histograms P and Q is:

    KS(P, Q) = maxᵢ |Fr(i, P) - Fr(i, Q)|

where Fr(i, P) is the cumulative histogram of P up to bin i:

    Fr(i, P) = Σⱼ≤ᵢ pⱼ

The maximum is over all bin indices i.

Properties:
- **Non-negative**: KS ≥ 0
- **Symmetric**: KS(P, Q) = KS(Q, P)
- **Bounded**: 0 ≤ KS ≤ 1 for normalised histograms
- **Zero only when equal**: KS(P, Q) = 0 iff P = Q

The KS distance is also the basis of the **Kolmogorov-Smirnov test**, a statistical test for whether two samples come from the same distribution.

## Key Properties / Complexity

### Why KS is useful
- **Captures worst-case cumulative difference**: robust to a few outlier bins
- **Bounded in [0, 1]**: easy to interpret (KS = 0.1 means 10% cumulative difference at some point)
- **Computable in O(n)**: just walk through the bins and track the max difference
- **Standard in statistics**: well-understood properties, used in many statistical tests

### When to use KS vs other distances
- **KS**: when you care about the *cumulative* difference, not per-bin
- **L1, L2**: when you care about per-bin differences
- **Chi-squared**: when you want scale-invariant comparison
- **Earth Mover's Distance**: when you want to measure "work" to transform one to the other

### KS in the lecture's Ex07
The exercise computes KS for P = (5, 5, 5, 5) and Q = (8, 5, 4, 3):
- Cumulative P: (5, 10, 15, 20)
- Cumulative Q: (8, 13, 17, 20)
- Differences: (3, 3, 2, 0)
- KS = max(3, 3, 2, 0) = 3

Normalised by the total (20): KS = 3/20 = 0.15 (or 15%).

### KS and the Kolmogorov-Smirnov test
The KS test uses the same statistic but with a different purpose: given two samples, test the null hypothesis that they come from the same distribution. The test rejects the null when KS is too large. The threshold depends on the sample sizes.

For CBR, you typically use KS as a *distance*, not as a *test*. The test machinery is more relevant when you want to make a binary decision ("are these two distributions significantly different?").

## Worked Example

Two colour histograms with 4 bins:
- P = (0.25, 0.25, 0.25, 0.25) (uniform)
- Q = (0.5, 0.25, 0.125, 0.125) (skewed to red)

Cumulative P: (0.25, 0.50, 0.75, 1.00)
Cumulative Q: (0.50, 0.75, 0.875, 1.00)
Differences: (0.25, 0.25, 0.125, 0)

KS = max(0.25, 0.25, 0.125, 0) = 0.25

The maximum cumulative gap is 0.25 (25%), occurring at the first and second bins. After that, the gap narrows.

If P = (0.5, 0.3, 0.1, 0.1) and Q = (0.1, 0.1, 0.3, 0.5) (opposite distributions):
- Cumulative P: (0.5, 0.8, 0.9, 1.0)
- Cumulative Q: (0.1, 0.2, 0.5, 1.0)
- Differences: (0.4, 0.6, 0.4, 0)
- KS = 0.6

The two distributions are very different — KS = 0.6 is large.

## Common Pitfalls
- **Normalising**: the raw KS depends on the total count; for histograms with different totals, normalise first (divide each bin by the total).
- **Bin order matters**: KS is sensitive to how bins are ordered. If the bin order is arbitrary, KS is not meaningful. For ordered features (e.g., brightness levels), KS makes sense.
- **Confusing with the test**: KS as a distance is straightforward; KS as a test has additional machinery (p-values, sample size effects).
- **Bins with very different scales**: KS doesn't normalise by bin magnitude, so a small per-bin difference in a small-count bin can have the same KS contribution as a large difference in a large-count bin. For histograms with very different scales, chi-squared is better.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[minkowski-distance]] — the alternative
- [[chi-squared-distance]] — the alternative for histograms with different scales
- [[feature-vector]] — what the distance operates on
- [[similarity-measures]] — the broader family
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- For what feature types is KS better than chi-squared? (Empirically: for ordered, evenly-scaled features.)
- Can KS be used in high dimensions? (Yes, but with care — the joint cumulative distribution is harder to compute.)
- Are there weighted variants of KS that emphasise certain bins? (Yes — weighted KS, used in some CBR systems.)
