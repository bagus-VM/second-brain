---
title: "R-tree and Variants"
tags: [algorithm, multimedia-databases, semester-1, r-tree, access-structure]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[signature-vectors]]", "[[dimensionality-reduction]]", "[[curse-of-dimensionality]]"]
---

## One-line Summary
The R-tree generalizes the B-tree to multidimensional data by grouping objects into minimum bounding rectangles, with a family of variants that trade overlap, region shape, and split strategy against search efficiency.

## Core Intuition
A B-tree orders one-dimensional keys so range queries prune whole subtrees. In a multidimensional feature space there is no single ordering, so the R-tree instead wraps each node's contents in a Minimum Bounding Rectangle (MBR). If a query region does not intersect an MBR, the whole subtree is skipped.

The catch is overlap. When MBRs overlap, a query point can fall inside several siblings, so the search must descend multiple branches. Overlap is the main enemy of R-tree efficiency, and every variant attacks it differently: forbidding it (R+), reorganizing on overflow (R*), changing the region shape (SS, SR), varying the active dimensions (TV), or delaying splits with oversized nodes (X).

## Formal Definition / Statement
An **R-tree** is a height-balanced generalization of the B-tree for multidimensional spaces. Each node is described by its **Minimum Bounding Rectangle (MBR)**, which contains all objects inside that node (signature vectors and subtrees).

**Variants covered in the lecture**:

| Variant | Region                     | Key idea                                                      | Trade-off                     |
| ------- | -------------------------- | ------------------------------------------------------------- | ----------------------------- |
| R+      | Rectangle, no overlap      | Object added to every node whose MBR it overlaps              | Better search, taller tree    |
| R*      | Rectangle, overlap allowed | Modified add and split; forced re-add on overflow             | More efficient than R-tree    |
| SS      | Bounding circle            | Tree ordered by similarity of circular regions                | Better than R*                |
| SR      | Rectangle and circle       | Region is the intersection of both; see [[sr-tree]]           | Low volume and low diameter   |
| TV      | Rectangle, varying dims    | Telescope function selects active dimensions per height       | Fewer dims near root          |
| X       | Rectangle, supernodes      | Double-capacity supernodes; split history for minimal overlap | More efficient than TV and R* |

**Multi-feature access structures** index several feature vectors in one structure rather than one tree per feature: the **M-tree** and **M2-tree**. **TempoM2** extends this to temporal video search with two levels (an M2-tree for content plus container nodes enforcing a total order over video segments).

## Key Properties / Complexity
- **MBR containment**: an MBR contains all signature vectors and subtrees in its node, so a non-intersecting MBR safely prunes the subtree.
- **Overlap hurts**: overlapping MBRs reduce efficiency because the search must follow every overlapping branch.
- **R+ eliminates overlap at a cost**: objects land in all overlapping nodes, which raises the tree height but improves search efficiency.
- **R* avoids splits when possible**: when a node is full, it tries to delete and re-add existing entries (forced re-add) before splitting, which reorganizes the tree incrementally.
- **SS uses circles, ordered by similarity**: bounding circles tend to have lower diameter than rectangles, helping nearest-neighbour pruning.
- **TV telescopes dimensions**: nodes near the root index fewer dimensions (computed by the telescope function), but overlaps and repeated first-dimension values cause problems.
- **X avoids splits with supernodes**: a supernode has double the normal capacity, and split history is used to find the split with minimal overlap.
- **All variants still suffer the curse of dimensionality**: in high dimensions, MBRs overlap heavily and pruning loses power. Reduction ([[dimensionality-reduction]]) or approximate methods ([[locality-sensitive-hashing]]) are the usual escapes.

## Worked Example
Two-dimensional points A, B, C clustered near the bottom-left, and F, G, H near the top-right. The R-tree groups them:

```
R1 = MBR around {A, B, C}      (bottom-left)
R2 = MBR around {D, E}         (middle)
R3 = MBR around {F, G, H}      (top-right)
```

Root has entries R1, R2, R3. A range query whose rectangle intersects only R1 descends into R1's subtree and ignores R2 and R3.

If R1 and R2 overlap (say both cover part of the middle region), a query point in the overlap must visit both R1 and R2. That is the efficiency loss the variants try to reduce. An R+ tree would clip the overlapping object into both regions with no shared area, at the cost of duplicating it and growing the tree. An R* tree would instead trigger a forced re-add of nearby entries to reshape R1 and R2 and shrink the overlap.

## Common Pitfalls
- Assuming MBRs never overlap in a plain R-tree. They do, and that overlap is the main performance killer.
- Forgetting that R+ duplicates objects across overlapping nodes. Search is faster, but storage and updates cost more.
- Confusing the SS-tree's bounding circles with rectangles. Circles change the distance computations used during insertion and pruning.
- Treating the TV-tree's dimension reduction as free. Overlaps among nodes that share active dimensions, plus repeated first-dimension values, degrade it.
- Expecting any R-tree variant to win in very high dimensions. Past a point the [[curse-of-dimensionality]] dominates, and approximate indexing ([[locality-sensitive-hashing]]) or [[dimensionality-reduction]] is the practical answer.
- Overlooking multi-feature needs. One feature space per tree means N features need N trees and a join at query time, which the M-tree family avoids.

## Connections
- [[sr-tree]]: the variant that intersects bounding rectangles and spheres to get low volume and low diameter, with explicit MINDIST and MINMAXDIST pruning.
- [[curse-of-dimensionality]]: the force that makes all MBR-based variants degrade as dimensionality grows.
- [[signature-vectors]]: the objects the R-tree indexes, usually after reduction.
- [[dimensionality-reduction]]: applied to signature vectors before indexing so the R-tree stays effective.
- [[gist-framework]]: a template that lets B-trees, R-trees, and SR-trees share search, insert, and concurrency machinery.
- [[quadtree-and-kd-tree]]: main-memory spatial indexes that solve a related partitioning problem without secondary-storage balancing.
- [[locality-sensitive-hashing]]: the approximate alternative when R-tree variants lose to the curse of dimensionality.

## Open Questions
- For a given feature distribution, which variant minimizes overlap best in practice?
- How do the multi-feature structures (M-tree, M2-tree) handle features with very different distance metrics in one tree?
- Does the X-tree's supernode strategy scale to the dimensions modern embeddings produce, or does it just delay the inevitable?
