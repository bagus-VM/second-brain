---
title: "Quadtrees and kd-trees"
tags: [concept, multimedia-databases, semester-1, quadtree, kd-tree, spatial-index]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[r-tree]]", "[[curse-of-dimensionality]]"]
---

## One-line Summary
Quadtrees and kd-trees are main-memory spatial index structures that partition space recursively, with quadtrees splitting all dimensions at once and kd-trees splitting one dimension at a time to avoid empty space.

## Core Intuition
Both structures answer the same question: how do you quickly find points near a query without scanning all of them? They partition space into smaller and smaller cells until each cell holds few points, then a range search only descends into cells the query ball touches.

A quadtree splits every dimension simultaneously, producing 2^d children per node. It is simple and versatile but wastes effort on empty regions when points form sparse clouds, and its size and time blow up exponentially with dimension. A kd-tree (Bentley, 1975) splits one dimension at a time and chooses the split position carefully rather than always halving, which removes most empty space and keeps storage linear.

Both are main-memory structures. Neither is balanced for secondary storage the way an [[r-tree]] is, and both can still hit exponential query time in high dimensions.

## Formal Definition / Statement
**Quadtree**:
- Split the space into 2^d equal subsquares (d = number of dimensions).
- Repeat until a stopping condition holds: only one pixel left, only one point left, or only a few points left.
- Variants: split only one dimension at a time, leading to kd-trees.

**Quadtree range search** (near neighbor):
- Put the root on a stack.
- Repeat: pop the next node T from the stack. For each child C of T:
  - If C is a leaf, examine the point(s) in C.
  - If C intersects the ball of radius r around the query q, add C to the stack.

**kd-tree** (Bentley, 1975):
- Only one-dimensional splits (not all dimensions at once).
- Instead of splitting in the middle, choose the split carefully (many variations).
- Near(est) neighbor queries proceed as for quadtrees.
- Linear space; less empty space than a quadtree.

## Key Properties / Complexity
- **Quadtree**: simple, versatile, easy to implement. The simplest spatial structure on Earth, per the lecture.
- **Quadtree space**: exponential in dimension (2^d children per split).
- **Quadtree query time**: exponential in dimension in the worst case (e.g., points on the hypercube).
- **Quadtree weakness**: empty spaces. Sparse point clouds force many splits before any point is reached.
- **kd-tree space**: linear.
- **kd-tree splits**: one dimension per level, position chosen carefully, reducing empty space.
- **Both**: exponential query time is still possible in high dimensions. The [[curse-of-dimensionality]] eventually dominates, which is why [[locality-sensitive-hashing]] is the high-dimensional fallback.
- **Both are main-memory**: designed for in-memory point data, not for disk-based, page-balanced storage like the [[r-tree]] family.

## Worked Example
Take 2D points and build a quadtree. The root square contains all points. Split it into four equal quadrants:

```
+---------+---------+
|  NW     |  NE     |
| {A,B}   |  {C}    |
+---------+---------+
|  SW     |  SE     |
|  {}     | {D,E,F} |
+---------+---------+
```

NW has two points (above the "few points" threshold), so split NW again into four sub-quadrants until each holds one point. SW is empty, so it stays a leaf with no points.

Range search for points within radius r of query q:
1. Push the root.
2. Pop root, test its four children. NW intersects the query ball, push NW. NE does not intersect, skip. SW is empty and does not intersect, skip. SE intersects, push SE.
3. Pop SE, examine its leaf points D, E, F, compute their distances to q, keep those within r.
4. Pop NW, recurse into its children, examine A and B.

For a kd-tree on the same points, the first split might be vertical at the median x, dividing points into left and right halves with no empty quadrants, then a horizontal split at the median y within each half. Storage stays linear and no region is purely empty.

## Common Pitfalls
- Using a quadtree in high dimensions. 2^d children per node makes 10 dimensions yield 1024 children per split; space and time explode.
- Forgetting quadtree empty-space waste. Sparse clouds cause deep, mostly empty trees before any point is isolated.
- Assuming kd-trees escape the curse of dimensionality. They use linear space and less empty space, but worst-case query time is still exponential in dimension.
- Confusing these main-memory structures with disk-based indexes. Quadtrees and kd-trees are not page-balanced for secondary storage; use an [[r-tree]] variant there.
- Skipping the intersection test during range search. A child that does not intersect the query ball must be pruned, or the search degrades to a full scan.

## Connections
- [[r-tree]]: the secondary-storage, page-balanced counterpart for multidimensional data on disk.
- [[curse-of-dimensionality]]: the reason both structures hit exponential query time as dimensions grow.
- [[locality-sensitive-hashing]]: the approximate high-dimensional method used once exact trees like these degrade.
- [[signature-vectors]]: the point data these structures index in the content-based retrieval pipeline.
- [[dimensionality-reduction]]: shrinking vectors first lets quadtrees and kd-trees stay in their effective low-dimensional regime.

## Open Questions
- For what dimensionality does a kd-tree's careful split choice stop beating a quadtree's uniform splits?
- Can adaptive cell sizes (as in some quadtree variants) recover the wasted space without losing simplicity?
- How do these structures compare to modern in-memory graph indexes for moderate-dimensional data?
