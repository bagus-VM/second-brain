---
title: "Graph Partitioning: Cut-Based and Spectral Methods"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[network-science-l02]]"]
---

## One-line Summary
Graph partitioning splits a graph into k groups by minimising edge cuts (min-cut, Kernighan–Lin) or using spectral properties of the Laplacian (Fiedler vector), typically requiring k to be specified in advance.

## Core Intuition
Unlike [[modularity|maximizing modularity]] (which finds communities of any size), partitioning methods aim to split the graph into a **fixed number of balanced groups** while minimising the number of edges cut. This is useful for parallel computing, VLSI design, and network analysis where balanced splits matter.

## Formal Definition / Statement

### Min-Cut / Max-Flow
Find the smallest set of edges whose removal disconnects two specified groups. Exact in polynomial time (Ford–Fulkerson) but minimizes raw cut size, not normalized density — can favour trivially small groups.

### Kernighan–Lin (1970)
Local search: initialize a balanced 2-partition at random; iteratively swap node pairs to decrease cut size. Fast in practice; converges to a local optimum. Complexity: O(n²) per pass.

### Spectral Partitioning
1. Compute the **graph Laplacian** L = D - A (D = degree matrix, A = adjacency matrix)
2. Find the **Fiedler vector**: eigenvector of the second-smallest eigenvalue λ₂
3. Partition: nodes with positive Fiedler entries go left, negative go right

- λ₂ is the **algebraic connectivity**: λ₂ = 0 means the graph is already disconnected
- Generalizes to k communities using the k smallest eigenvectors → **spectral clustering**

## Key Properties / Complexity
- Min-cut: exact for 2-partition but ignores density, favors small cuts
- Kernighan–Lin: fast local search but stuck at local optimum, requires fixed k
- Spectral: principled global structure, but O(n³) exact; needs k in advance
- All three target **balanced splits**, not necessarily the densest communities
- Spectral methods connect to the deep mathematics of the Laplacian spectrum

## Worked Example
For a graph with two clear clusters connected by a few bridge edges:
- **Min-cut**: identifies the bridge edges as the minimum cut set
- **Spectral**: the Fiedler vector assigns positive values to one cluster, negative to the other; the sign pattern recovers the natural partition
- **Kernighan–Lin**: starting from a random split, node swaps converge to the same two-cluster partition

## Common Pitfalls
- Min-cut can produce trivially unbalanced partitions (one node vs. rest) unless normalized
- Spectral partitioning requires computing eigenvectors — expensive for large graphs without sparse approximations
- All methods require specifying k — unlike [[louvain-algorithm]] where k emerges naturally
- Cut-based methods optimise a different objective than [[modularity]] — answers may differ
- Conductance (normalized cut) is related but distinct from modularity

## Connections
- [[modularity]] — alternative objective; cut methods optimise cuts, modularity optimizes density surplus
- [[girvan-newman-algorithm]] — also a partitioning method but uses edge betweenness
- [[graph-partitioning]] — the general problem of dividing a graph into balanced clusters
- [[louvain-algorithm]] — doesn't need k; partitioning methods do
- [[community-detection-overview]] — partitioning is one family among several
- [[centrality-measures]] — spectral methods relate to the Laplacian, which encodes global structure

## Open Questions
- How to choose k when no domain knowledge is available?
- Can spectral methods be approximated efficiently for very large graphs?
- How do normalized cuts (conductance) compare to modularity in practice?
