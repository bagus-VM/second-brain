---
title: "Spectral Partitioning"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Spectral partitioning uses the eigenvectors of the graph Laplacian to find a natural 2-partition — the Fiedler vector (eigenvector of the second-smallest eigenvalue) encodes the split.

## Core Intuition
The graph Laplacian L = D - A encodes the structure of the graph. The Fiedler vector (eigenvector of λ₂, the second-smallest eigenvalue) assigns a value to each node; nodes with positive values go one side, negative values go the other. This naturally separates the graph at its sparsest cut.

## Formal Definition / Statement
**Graph Laplacian:**
L = D - A

where D is the diagonal degree matrix and A is the adjacency matrix.

**Fiedler vector:** the eigenvector x₂ corresponding to λ₂ (the second-smallest eigenvalue of L).

**Partition rule:** nodes with x₂(i) > 0 go left; nodes with x₂(i) < 0 go right.

**λ₂ is the algebraic connectivity:** λ₂ = 0 means the graph is already disconnected. Larger λ₂ means the graph is more "connected" and harder to partition.

**Generalization to k communities:** use the k smallest eigenvectors of L as a basis for spectral clustering.

**Time complexity:** O(n³) for full eigendecomposition; faster sparse approximations exist.

## Key Properties / Complexity
1. **Principled**: based on the mathematical structure of the Laplacian
2. **Global structure**: captures the graph's overall connectivity, not just local patterns
3. **Natural 2-partition**: the Fiedler vector finds the sparsest cut (under certain conditions)
4. **Algebraic connectivity**: λ₂ measures how easy the graph is to disconnect
5. **Needs k in advance**: for k > 2 communities, must specify k beforehand

## Worked Example
Graph with two dense clusters connected by a few edges:

1. Compute L = D - A
2. Find the Fiedler vector x₂ (eigenvector of λ₂)
3. Nodes in cluster A have x₂(i) > 0; nodes in cluster B have x₂(i) < 0
4. The partition naturally separates the two clusters

The Fiedler vector "sees" the global structure: even if two nodes are far apart in the graph, if they are in the same cluster, their x₂ values will have the same sign.

## Common Pitfalls
1. **Expensive for large graphs**: O(n³) for full eigendecomposition
2. **Needs k in advance**: for k > 2, must specify the number of communities
3. **Assuming the Fiedler vector always finds the best cut**: it finds the sparsest cut, which may not maximise [[modularity]]
4. **Confusing spectral partitioning with spectral clustering**: spectral clustering uses eigenvectors as features for k-means; spectral partitioning uses the sign of the Fiedler vector directly

## Connections
- [[graph-laplacian]] — the matrix being decomposed
- [[algebraic-connectivity]] — λ₂, the second-smallest eigenvalue
- [[normalized-cut]] — related objective that spectral methods approximately minimise
- [[conductance]] — related community quality measure
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How do we choose k for spectral clustering?
- How does spectral partitioning compare to modularity-based methods?
- Can we use other Laplacians (normalized, random-walk) for better results?
- How do we handle directed or weighted graphs?
