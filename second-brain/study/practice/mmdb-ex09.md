---
title: "Exercise Sheet 9: Indexing"
tags: [practice, multimedia-databases, semester-1]
course: "Multimedia Databases"
status: current
last_updated: 2026-07-11
---

# Exercise Sheet 9: Indexing

## Exercises

### Q1 General functions and drawbacks of index structures

What are the two main functions of index structures in a database system? Name two drawbacks of maintaining many indexes.

> [!note]- Solution
> **Functions:**
>
> 1. Increase execution speed of retrieval queries.
> 2. Improve the query optimizer's ability to access data quickly.
>
> **Drawbacks:**
>
> 1. Indexes consume additional storage space.
> 2. Insert, delete, and update operations slow down because indexes must be recomputed on every modification.

### Q2 CBIR-specific requirements

Which two requirements does Content-Based Image Retrieval (CBIR) place on index structures beyond those of a conventional database?

> [!note]- Solution
> 1. Methods for **reduction of dimensionality** (see [[curse-of-dimensionality]], [[dimensionality-reduction]]).
> 2. Efficiency in query processing using **specific indexing data structures** tailored to high-dimensional feature vectors.

### Q3 B-tree properties

State the properties of a B-tree of order `m`.

> [!note]- Solution
> - Every node has at most `m` children.
> - The root has at least 2 children (unless it is a leaf).
> - Every non-leaf node (except the root) has at least `ceil(m/2)` children.
> - All leaves appear at the same level.
>
> Search, delete, and insert operations run in **logarithmic time**.

### Q4 Hash indexing

How does a hash index work, and how are collisions resolved?

> [!note]- Solution
> A **hash function** maps each key to a bucket. When two keys map to the same bucket (collision), **separate chaining** is used: each bucket holds a linked list of all entries that hash to it.

### Q5 K-d tree and Point Quadtree

Sketch the key idea of a K-d tree and a Point Quadtree for 2D point data.

> [!note]- Solution
> **K-d tree:** Recursively split the space with axis-aligned cuts, alternating the dimension at each level (e.g., split on x, then y, then x, ...). Each internal node stores a splitting value along one axis; the left subtree contains points below the split, the right subtree contains points above. See [[quadtree-and-kd-tree]].
>
> **Point Quadtree:** Decompose 2D space around a chosen point into four quadrants (NW, NE, SW, SE). Each point becomes a node with up to four children, one per quadrant. Recurse until each quadrant contains at most one point.

### Q6 R-tree key idea

What is the central idea behind the [[r-tree]], and how does it relate to the B-tree?

> [!note]- Solution
> **Key idea:** Group nearby objects together and represent each group by its **minimum bounding rectangle** (MBR, also called minimum bounding box / MBB) in the next level up. The "R" stands for rectangle.
>
> The R-tree is a **height-balanced tree** similar to a B-tree, but the index records sit in the **leaf nodes** and contain pointers to the actual data objects. Non-leaf nodes store MBBs that cover their children.

### Q7 R-tree properties

List the five formal properties (P1 to P5) of an R-tree.

> [!note]- Solution
> | ID | Property |
> |----|----------|
> | P1 | Every leaf node contains between `m` and `M` entries, unless it is the root. |
> | P2 | Each leaf entry `I` is the MBB of one object. |
> | P3 | Each non-leaf entry `I` is the MBB that covers all children's MBBs. |
> | P4 | Every non-leaf node (non-root) has between `m` and `M` children. |
> | P5 | The root has at least 2 children, unless it is a leaf. |

### Q8 R-tree insert algorithm

Describe the steps of the R-tree insertion algorithm.

> [!note]- Solution
> 1. **Find leaf node:** Descend from the root, at each level choosing the subtree whose MBB needs the **least expansion** to accommodate the new entry.
> 2. **Insert entry:** Add the entry to the chosen leaf.
> 3. **Handle overflow:** If the leaf overflows (exceeds `M` entries), **split** the node into two groups (e.g., Q1 and Q2).
> 4. **Propagate upward:** Adjust MBBs along the path to the root. If a split reaches the root, create a new root.

### Q9 R-tree delete and condense algorithm

Describe the R-tree deletion algorithm, including the condense-tree step.

> [!note]- Solution
> **Delete algorithm:**
>
> - **D1:** Find the leaf node containing the entry to delete.
> - **D2:** Remove the entry from the leaf.
> - **D3:** Condense the tree (see below).
> - **D4:** If the root has only one child after condensing, make that child the new root (shorten the tree).
>
> **Condense tree (D3):**
>
> 1. Remove nodes that have too few entries (below `m`).
> 2. **Reinsert** the orphaned entries from removed nodes (starting at the leaf level, then upward).
> 3. Adjust covering MBBs along the path from affected leaves up to the root.

### Q10 Exact query with and without an index

How does an exact query on n-dimensional feature vectors work without an index, and how does an index change the process?

> [!note]- Solution
> **Exact query:** Retrieve all points whose feature vector is identical to the query point `q`.
>
> - **Without index:** Sequential scan over all data points. Compare each feature vector to `q`.
> - **With index:** Start at the root and recursively search every subtree whose region contains `q`. Because R-tree regions may **overlap**, more than one branch may need examination.

### Q11 Range query

Define a range query and explain how an index helps answer it.

> [!note]- Solution
> **Range query:** Return all points `P` with `dist(P, Q) <= r`, where `Q` is the query point and `r` is the search radius.
>
> - **Without index:** Sequential scan, computing the distance for every point.
> - **With index:** Use **MINDIST** (the minimum distance between the query point and a bounding region). Prune any subtree whose MINDIST exceeds `r`, since it cannot contain qualifying points.

### Q12 Nearest neighbor query (NNQ) and k-NNQ

Describe the nearest neighbor query and the pruning strategy used with an R-tree index.

> [!note]- Solution
> **NNQ:** Return the single point with the lowest distance to the query point `Q`. **k-NNQ** generalizes this to return the `k` nearest points.
>
> **With index (branch-and-bound):**
>
> 1. Initialize `resultdist` to infinity.
> 2. Traverse the tree from the root.
> 3. For each node, compute MINDIST between `Q` and the node's MBB.
> 4. **Prune** any branch whose MINDIST is greater than or equal to the current best `resultdist`.
> 5. When a leaf is reached, compute the actual distance to each candidate. If a distance is smaller than `resultdist`, update the best result.
> 6. Continue until no unexplored branch can improve the result.
>
> This avoids visiting branches that cannot contain a closer point than the current best.

## Cross-references

- [[r-tree]] | [[sr-tree]] | [[gist-framework]]
- [[quadtree-and-kd-tree]]
- [[curse-of-dimensionality]] | [[dimensionality-reduction]]
- [[locality-sensitive-hashing]]
- [[signature-vectors]]
- [[multimedia-databases-lecture-09]]
