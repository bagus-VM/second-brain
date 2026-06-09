---
title: "Spectral Clustering"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: ["[[graph-fundamentals]]"]
---

## One-line Summary
Spectral clustering finds groups in a graph by looking at the eigenvectors of its Laplacian matrix — turning a combinatorial problem into a linear algebra one.

## Core Intuition
Partitioning a graph into clusters is NP-hard in general. But there is a beautiful trick: encode the graph structure into a matrix (the graph Laplacian), compute its eigenvectors, and use those as coordinates for a simpler clustering problem. The key insight is that the eigenvectors corresponding to the smallest eigenvalues of the Laplacian reveal the "natural cuts" in the graph — directions along which the graph is most easily separated. Nodes that are well-connected end up close together in this eigenspace; nodes in different communities end up far apart. Once embedded, a simple algorithm like k-means can find the clusters.

## Formal Definition / Statement

Given graph G = (V, E) with adjacency matrix A and degree matrix D = diag(d₁, ..., dₙ):

**Graph Laplacian**: L = D − A

**Normalized Laplacian**: L_norm = D^{-1/2} L D^{-1/2} = I − D^{-1/2} A D^{-1/2}

**Spectral clustering algorithm** (k-way partition):
1. Compute the k smallest eigenvectors of L (or L_norm): u₁, u₂, ..., uₖ
2. Form matrix U ∈ ℝ^{n×k} with these eigenvectors as columns
3. Normalize each row of U to unit length (for normalized spectral clustering)
4. Treat each row as a point in ℝᵏ
5. Run k-means on these n points to obtain k clusters

**Normalized Cut (Shi & Malik, 2000)**:
NCut(S₁, ..., Sₖ) = Σᵢ cut(Sᵢ, S̄ᵢ) / vol(Sᵢ)

where cut(S, S̄) = number of edges between S and its complement, and vol(S) = sum of degrees in S. Minimizing NCut is NP-hard, but the spectral relaxation gives the eigenvector solution.

## Key Properties / Complexity

- The number of connected components equals the multiplicity of eigenvalue 0 of L
- The second-smallest eigenvalue λ₂ (algebraic connectivity / Fiedler value) measures how well-connected the graph is
- λ₂ = 0 ⟺ graph is disconnected
- Computing k eigenvectors: O(|E| · k) with Lanczos/Arnoldi methods (sparse)
- k-means step: O(n · k · d · iterations)
- Total: polynomial time, but the relaxation introduces approximation error
- The method works well when clusters are "nearly separable" (small normalized cut)
- Spectral clustering can find non-convex clusters that k-means on raw features cannot

## Worked Example

Consider a graph with two clear communities connected by a single bridge:

```
Community A: {1,2,3} fully connected (triangle)
Community B: {4,5,6} fully connected (triangle)
Bridge: edge {3,4}
```

Laplacian eigenvalues: 0, 0.76, 1.0, 1.0, 1.68, 3.56

The second eigenvector (Fiedler vector) assigns:
- Nodes 1,2,3 → positive values
- Nodes 4,5,6 → negative values

This correctly separates the two communities. The gap between λ₂ = 0.76 and λ₃ = 1.0 indicates that a 2-way partition is the most natural.

## Common Pitfalls

- Confusing the graph Laplacian L = D − A with the normalized Laplacian L_norm — they give different eigenvectors
- Forgetting to normalize rows in the normalized spectral clustering variant
- Choosing k (number of clusters) incorrectly — look at the eigengap (largest gap between consecutive eigenvalues)
- Assuming spectral clustering works well for all graph types — it struggles when clusters have very different sizes or densities
- Spectral clustering is a *relaxation* of the discrete NCut problem — the continuous solution may not exactly minimize the discrete objective
- Computational cost can be high for very large graphs (need sparse eigensolvers)

## Connections

- [[graph-partitioning-cut-spectral]] — the cut-based formulation that spectral clustering optimizes
- [[community-detection-overview]] — spectral clustering as one family of community detection methods
- [[modularity]] — alternative objective for community detection (spectral clustering optimizes NCut, not modularity)
- [[laplacian-eigenmaps]] — the same eigenvectors used for node embedding
- [[network-science-l09]] — spectral methods as the "first wave" of graph embeddings
- [[graph-fundamentals]] — adjacency matrix and degree as inputs

## Open Questions

- How does spectral clustering compare to modularity-based methods (Louvain, Leiden) on real-world networks?
- When does the spectral relaxation fail to approximate the discrete NCut well?
- How do we handle directed or signed graphs in the spectral framework?
