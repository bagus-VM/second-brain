---
title: "Multimedia Databases - Lecture 09: Indexing and Access Structures"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[curse-of-dimensionality]]", "[[feature-vector]]"]
---

## One-line Summary
Lecture 09 covers access structures for multimedia databases: signature vectors, dimensionality reduction (transformations and space-filling curves), multidimensional index structures (R-tree family, quadtrees, kd-trees, LSH), query types (k-NN, range, approximate NN), the SR-tree case study with pruning, and the GiST framework.

## Core Intuition
CBIR systems compute high-dimensional feature vectors for every image. Searching those vectors naively means scanning the entire database. Index structures make search fast, but traditional B-trees break down in high dimensions. This lecture covers the full indexing pipeline: extract signature vectors, reduce dimensionality, build a multidimensional index, and answer similarity and range queries with pruning.

## Key Topics

### 1. [[signature-vectors]]
- Low-level features (color distribution, texture) described as signature vectors, automatically computed from data
- Example: greyscale histogram as a signature vector
- Pipeline: multimedia data → signature extraction → signature vectors → reduction of dimensionality → dimension-reduced vectors → index computation → index structure

### 2. [[dimensionality-reduction]]
- Goal: fewer dimensions while preserving distance
- Why: index efficiency decreases with dimensionality (curse of dimensionality: sequential scan becomes faster than index search)
- Transformations: change basis to orthonormal vectors, delete low-influence coefficients
  - Karhunen-Loeve (KLT): clustered data
  - Fourier/FFT: periodic data
  - Wavelet: discrete data
  - DCT: locally correlated data
- Space-filling curves: represent multidimensional space as single curve, preserving order
  - Hilbert curve
  - Z-Ordering: divide space into regions, store in B*-tree pages

### 3. Multidimensional Access Structures

#### Secondary storage algorithms
- [[r-tree]] family: generalization of B-trees for multidimensional spaces, each node described by MBR (Minimum Bounding Rectangle)
  - R-tree: overlapping MBRs allowed
  - R+-tree: no MBR overlap, objects added to all overlapping nodes, higher tree
  - R*-tree: overlap allowed, modified add/split with forced re-add, more efficient
  - SS-tree: bounding circle instead of rectangle, similarity-ordered
  - [[sr-tree]]: intersection of rectangle and circle (see case study below)
  - TV-tree: varying dimensions per node height, telescope function
  - X-tree: supernodes with double capacity, split history for minimal overlap
- VA-file: vector approximation file

#### Multi-feature access structures
- M-tree, M2-tree: index multiple feature vectors in one structure
- TempoM2: two-level structure for temporal video search. First level: M2-tree for content-based search. Second level: container nodes with time intervals for temporal relations.

#### Main memory algorithms
- [[quadtree-and-kd-tree]]: quadtree splits space into 2^d equal subsquares (exponential in dimension). kd-tree (Bentley 1975) does one-dimensional splits, linear space, less empty space.
- [[locality-sensitive-hashing]]: hash similar items to same bucket. Partition signature matrix into b bands of r rows. Candidate pairs hash to same bucket for at least one band. Tune b and r. Variants: Multi-Probe LSH, C2LSH, SK-LSH. Most promising for approximate NN.

### 4. Query Types
- Similarity query: k most similar objects, generalization of k-NN search. Ignore nodes with distance too high.
- Range query: find all objects intersecting a region. Ignore nodes with intersection below threshold.
- Near neighbor: find points within distance r from q
- Approximate near neighbor: find points within (1+ε) times the true nearest distance

### 5. [[sr-tree]] Case Study
- Sphere/Rectangle-tree: extension of R* and SS trees
- Regions = intersection of bounding rectangles (lower volume) and bounding spheres (lower diameter)
- Combined: lower volume AND lower diameter
- Insertion: based on SS-tree, uses center of bounding spheres, updates both regions
- NN search: ordered depth search, candidate set, visit overlapping leaves
- Key distances:
  - MINDIST: Euclidean distance from query point to region
  - MINMAXDIST: minimal value of maximal distances on all axes
- Pruning:
  - Downward: exclude region if MINDIST(R1) > MINMAXDIST(R2)
  - Upward: exclude object if distance > MINMAXDIST of region; exclude region if MINDIST > distance to found object
- Strengths: small volume + low diameter = better disjunctivity
- Weaknesses: higher creation cost, node size grows with dimensionality

### 6. [[gist-framework]] (Generalized Search Tree)
- Template index structure abstracting the type of tree (B+, R-tree, SR-tree, etc.)
- Problem solved: each new search tree requires re-implementing concurrency control and recovery
- GiST provides: extensible datatypes/queries, template algorithms (search, insert, delete), height-balanced tree
- Available examples: B-trees, R-trees, SR-trees
- Reference: Hellerstein, Naughton, Pfeffer, VLDB 1995

## Worked Example: SR-tree Pruning
Given a query point P and two regions R1, R2:
1. Compute MINDIST(P, R1) and MINMAXDIST(P, R2)
2. If MINDIST(P, R1) > MINMAXDIST(P, R2), prune R1 (downward pruning): R1 cannot contain the nearest neighbor
3. If distance(P, O) > MINMAXDIST(P, R2) for some object O, prune O (upward pruning)
4. If MINDIST(P, R1) > distance(P, O) for found object O, prune R1 (upward pruning)
5. Result: fewer nodes visited, faster search

## Connections
- [[signature-vectors]] → [[dimensionality-reduction]] → [[r-tree]] (the indexing pipeline)
- [[curse-of-dimensionality]] (why dimensionality reduction is necessary)
- [[r-tree]] → [[sr-tree]] → [[gist-framework]] (tree family and abstraction)
- [[locality-sensitive-hashing]] (alternative to tree-based indexing for high dimensions)
- [[content-based-retrieval]] (indexing is the backend of CBR)
- [[multimedia-databases-lecture-07]] (CBIR from L07 needs these structures for speed)

## Exam-Relevant Key Points
- The indexing pipeline: signature extraction → dimensionality reduction → index computation
- Four transformation methods and when to use each (KLT/FFT/Wavelet/DCT)
- Space-filling curves: Hilbert and Z-Ordering, how they enable 1D indexing
- R-tree variants and their trade-offs (R+ no overlap but taller, R* forced re-add, SS bounding circle)
- SR-tree: why intersection of rectangle and sphere beats either alone
- MINDIST vs MINMAXDIST and the two pruning directions
- LSH: band partitioning (b bands of r rows), candidate pairs, tuning b and r
- GiST: what problem it solves, what it provides
- Query types: similarity (k-NN), range, approximate NN with (1+ε) factor

## Open Questions
- At what dimensionality does LSH overtake tree-based methods? The lecture hints it is the most promising for approximate NN, but where is the crossover?
- How do learned index structures (ML-Index, BB-Tree from the lecture's references) compare to GiST-based trees?
- For multi-feature queries (TempoM2), how do you balance the cost of maintaining multiple feature indexes vs one combined structure?
