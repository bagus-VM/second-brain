---
title: "SR-tree (Sphere/Rectangle-tree)"
tags: [algorithm, multimedia-databases, semester-1, sr-tree, access-structure]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[r-tree]]"]
---

## One-line Summary
The SR-tree indexes high-dimensional points for nearest-neighbor search by defining each region as the intersection of a bounding rectangle and a bounding sphere, combining low volume with low diameter for tighter pruning.

## Core Intuition
Bounding rectangles and bounding spheres each win on one axis and lose on the other. A rectangle tends to have low volume but a long diagonal (high diameter), especially in high dimensions. A sphere tends to have low diameter but high volume, because it balls out into empty space. Neither alone gives tight regions.

The SR-tree takes the intersection of the two. The intersection keeps the low volume of the rectangle and the low diameter of the sphere at the same time. Smaller, tighter regions mean fewer overlapping candidates during nearest-neighbor search, which means more aggressive pruning.

## Formal Definition / Statement
The **SR-tree** (Sphere/Rectangle-tree) is an extension of the R*-tree and the SS-tree. Each region is the **intersection of a bounding rectangle and a bounding sphere**.

**Region properties**:

| Region type | Volume | Diameter |
| ----------- | ------ | -------- |
| Bounding rectangle (R*) | lower | higher (long diagonal) |
| Bounding sphere (SS) | higher | lower |
| SR-tree (intersection) | low | low |

**Construction strategy**: minimize diameters (like SS) while keeping the rectangle's volume advantage.

**Insertion**: based on the SS-tree. Descend by choosing the subtree whose bounding-sphere center is most similar to the new entry. Update both the bounding sphere and the bounding rectangle on the way.

**Nearest-neighbor search**: ordered depth-first search. Build a candidate set of the closest points found so far, then visit every leaf whose region overlaps the candidate set. Return the last remaining candidate.

**Two key distances**:
- **MINDIST**: the Euclidean distance from the query point to the region.
- **MINMAXDIST**: the minimum, over all n axes, of the maximal distance from the query point to the region on that axis.

**Pruning**:
- **Downward pruning**: exclude a region R1 if its MINDIST is greater than the MINMAXDIST of another region R2, since R1 cannot contain the nearest neighbor.
- **Upward pruning**: exclude an object O if its distance to the query point exceeds the MINMAXDIST of a region. Also exclude a region whose MINDIST exceeds the actual distance from the query point to some object O.

## Key Properties / Complexity
- **Complementary regions**: rectangles give low volume, spheres give low diameter, the intersection keeps both.
- **Better disjunctivity**: smaller volume and lower diameter place points in tighter, more separable regions, which improves nearest-neighbor performance.
- **Insertion follows SS-tree logic**: center-of-sphere similarity guides descent, and both regions are updated on insert.
- **Pruning uses both MINDIST and MINMAXDIST**: downward pruning compares regions, upward pruning compares objects against regions.
- **Search cost**: ordered depth-first traversal with a priority on minimal distance, visiting only leaves whose regions overlap the candidate set.

**Strengths**:
- Regions with small volume and low diameter.
- Improved disjunctivity between regions.
- Higher nearest-neighbor search performance.

**Weaknesses**:
- Higher creation cost than R* or SS.
- Node size grows with dimensionality, since each node stores both a rectangle and a sphere.
- Reduced bifurcation can force reading more nodes per query, hurting query performance.

## Worked Example
A 16-dimensional test from the lecture reports normalized figures across trees:

| Tree | Diameter | Volume |
| ---- | -------- | ------ |
| R*-tree | 4 | 60 |
| SS-tree | 1 | 109 |
| SR-tree | 1 | 1 |

The SS-tree already wins on diameter (1) but loses badly on volume (109). The R*-tree has the smaller volume before SR (60) but a large diameter (4). The SR-tree keeps the SS-tree's diameter (1) while cutting volume to 1.

Now a pruning example. Query point P. Two regions R1 and R2:
- MINDIST(P, R1) = 5.2, MINMAXDIST(P, R1) = 6.0
- MINDIST(P, R2) = 3.1, MINMAXDIST(P, R2) = 4.0

Downward pruning: MINDIST(P, R1) = 5.2 is greater than MINMAXDIST(P, R2) = 4.0, so R1 cannot hold the nearest neighbor. Skip R1. Later, an object O at distance 4.5 from P is found. Upward pruning: any region with MINDIST above 4.5 is excluded, and any object farther than the current best MINMAXDIST is dropped.

## Common Pitfalls
- Using only MINDIST for pruning. MINDIST alone gives a lower bound but not the upward comparison; MINMAXDIST is what makes both pruning directions work.
- Forgetting that the SR-tree stores two regions per node, so node size (and I/O cost per node) grows with dimensionality.
- Assuming the intersection is always much smaller. In very high dimensions the rectangle and sphere can agree on little, and the gains shrink.
- Confusing MINMAXDIST with a plain distance. It is the minimum over axes of the per-axis maximum distance, a conservative upper bound on how close the nearest point in a region could be.
- Expecting low creation cost. Insertion updates both the sphere and the rectangle and follows SS-tree center similarity, so builds are more expensive than R*.

## Connections
- [[r-tree]]: the family the SR-tree extends, specifically the R* and SS variants it combines.
- [[curse-of-dimensionality]]: the reason tight regions matter, and the reason node-size growth with dimensionality is a real weakness.
- [[signature-vectors]]: the high-dimensional points the SR-tree indexes for nearest-neighbor search.
- [[gist-framework]]: the SR-tree is one of the tree types GiST templates can host, sharing search and concurrency logic.
- [[dimensionality-reduction]]: reducing signature vectors before indexing keeps the SR-tree's node-size growth manageable.

## Open Questions
- At how many dimensions does storing both a sphere and a rectangle per node stop paying off?
- Can the insertion strategy be improved beyond SS-tree center similarity to reduce creation cost?
- How does SR-tree pruning compare to modern graph-based approximate NN methods on the same data?
