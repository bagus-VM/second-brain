---
title: "Reduction of Dimensionality"
tags: [concept, multimedia-databases, semester-1, dimensionality-reduction, indexing]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[curse-of-dimensionality]]", "[[signature-vectors]]", "[[feature-vector]]"]
---

## One-line Summary
Shrink a signature vector to fewer dimensions while keeping the distances between vectors roughly intact, so that index structures stay faster than a sequential scan.

## Core Intuition
Index efficiency drops as dimensionality grows. Past a threshold, the [[curse-of-dimensionality]] kicks in and a plain sequential scan beats navigating the index. The fix is to throw away dimensions that contribute little to the distances between vectors, keeping only the ones that matter.

Two families do this. Transformations change the coordinate basis so that a few coefficients carry most of the information, then delete the rest. Space-filling curves take a different route: they map the multidimensional point onto a single one-dimensional curve that roughly preserves the multidimensional ordering, which lets you fall back on fast 1D index structures like a B*-tree.

## Formal Definition / Statement
**Goal**: produce a signature vector with fewer dimensions while preserving the distances between vectors as much as possible.

**Motivation**: the efficiency of index structures decreases with dimensionality. Under the curse of dimensionality, a sequential scan becomes faster than searching the index.

**Two approaches**:

1. **Transformations**
   - Change the basis of the vectors.
   - Convert to orthonormal vectors.
   - After transformation, distinguish coefficients with high influence from those with low influence.
   - Delete the low-influence coefficients.
   - The result is a signature vector with fewer dimensions.

   Which transform to use depends on the data:

   | Transformation | Application |
   | -------------- | ----------- |
   | Karhunen-Loeve | clustered data |
   | Fourier / FFT | periodic data |
   | Wavelet | discrete data |
   | DCT | locally correlated data |

2. **Space-filling curves**
   - Represent the multidimensional space as a single curve.
   - Map a d-dimensional point onto a one-dimensional value so that the multidimensional order is preserved as much as possible.
   - This enables the use of a one-dimensional index structure.
   - Examples: Hilbert curve, Z-Ordering.

## Key Properties / Complexity
- **Distance preservation is the success criterion**: if reduced vectors distort the original distances, similarity search results degrade.
- **Transformations are lossy by design**: deleting low-influence coefficients discards information, but only the information that barely affects distances.
- **Choice of transform is data-driven**: periodic data suits FFT, locally correlated data suits DCT, clustered data suits Karhunen-Loeve. See [[transform-coding]] for how these same transforms behave in compression.
- **Space-filling curves trade precision for 1D simplicity**: the curve cannot perfectly preserve all multidimensional neighbourhood relations, but it lets you reuse B*-tree machinery.
- **Z-Ordering stores regions in B*-tree pages**: divide the space into regions, store the four regions into the pages of a B*-tree.
- **Output feeds the index**: the dimension-reduced signature vectors are the input to the index computation step and the actual access structure, such as an [[r-tree]].

## Worked Example
Take signature vectors in 4D and apply a Karhunen-Loeve-style idea (principal components). Suppose the data clusters along one main direction, so the first basis vector captures most variance:

```
Original 4D:  [3.0, 2.9, 3.1, 3.0]   # points along the cluster
              [1.0, 1.1, 0.9, 1.0]
              [3.2, 3.0, 3.0, 3.1]

After transform, coefficients:
              [c1=5.2, c2=0.02, c3=0.01, c4=0.03]
              [c1=1.7, c2=0.01, c3=0.02, c4=0.01]
              [c1=5.3, c2=0.03, c3=0.01, c4=0.02]
```

c1 dominates. The other coefficients barely move, so deleting c2, c3, c4 keeps each point represented by a single number while preserving which points are close. The 4D vectors become 1D values, and a 1D index can handle them.

For a space-filling curve approach, a 2D point (x, y) with binary coordinates x = 10, y = 11 gets interleaved bits (Z-order): 1110, a single integer. Nearby 2D points usually get nearby integers, so a B*-tree on those integers approximates a 2D range query.

## Common Pitfalls
- Applying the wrong transform for the data. FFT on non-periodic, non-stationary data spreads energy across many coefficients, so few can be deleted.
- Expecting space-filling curves to preserve all neighborhoods. Two points close in 2D can end up far apart on the curve at order-4 boundaries. Hilbert curves mitigate this better than Z-ordering but do not eliminate it.
- Confusing dimensionality reduction with [[transform-coding]] quantization. Both discard coefficients, but here the goal is preserving distance for indexing, not preserving perceptual quality for compression.
- Reducing too aggressively. Drop too many dimensions and distinct objects collapse onto the same reduced vector, ruining retrieval.
- Forgetting that the query vector must be reduced with the same transform before searching the index.

## Connections
- [[curse-of-dimensionality]]: the reason reduction is needed, since index efficiency collapses as dimensions grow.
- [[signature-vectors]]: the input to the reduction step in the indexing pipeline.
- [[r-tree]]: a primary consumer of the dimension-reduced vectors.
- [[feature-vector]]: the general representation being shrunk.
- [[transform-coding]]: the same transforms (DCT, FFT, Wavelet) appear there for compression, with a different objective.
- [[locality-sensitive-hashing]]: an alternative that fights high dimensionality by hashing rather than by reducing dimensions first.

## Open Questions
- How many dimensions can you safely drop before nearest-neighbour results become unreliable for a given feature set?
- When is a space-filling curve preferable to a transformation, given the curve's imperfect ordering?
- Do learned reductions (autoencoders) preserve the metric properties the access structures assume, or do they distort distances in ways that break pruning?
