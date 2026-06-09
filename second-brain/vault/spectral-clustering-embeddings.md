---
title: "Spectral Clustering via Embeddings"
tags: [concept, network-science, semester-1, spectral-methods, clustering]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[laplacian-eigenmaps]]", "[[spectral-clustering]]"]
---

## One-line Summary
Spectral clustering is k-means applied to Laplacian eigenmaps — nodes in the same community have similar low-frequency eigenvector values, so clustering the embeddings recovers communities.

## Core Intuition
Laplacian eigenmaps embed nodes such that connected nodes are close in R^d. Communities correspond to clusters in this embedding space. Running k-means on the embeddings is equivalent to solving the Normalised Cut (NCut) problem (Shi & Malik 2000).

## Formal Definition / Statement
1. Compute the d smallest non-zero eigenvectors of L = D - A (or L_sym)
2. Form embedding matrix Z ∈ R^{|V|×d} with rows z_v = (v_2(v), ..., v_{d+1}(v))
3. Run k-means on Z to recover k clusters

The spectral gap λ_{k+1} - λ_k indicates the "natural" number of communities:
- Large gap at position k → graph has exactly k clear clusters
- Small gap → partition is ambiguous

## Key Properties
1. Reduces graph clustering to linear algebra + k-means
2. The spectral gap reveals the natural number of clusters
3. Used in image segmentation (NCut), community detection, and graph partitioning
4. Principled: globally optimal for the relaxed NCut objective
5. Limitation: O(|E|·d) per eigenvector iteration — doesn't scale to very large graphs

## Worked Example
Graph with 3 disconnected components:
- λ_1 = λ_2 = λ_3 = 0 (multiplicity = number of components)
- Eigenvectors span piecewise-constant vectors (indicator of each component)
- k-means on 3-dimensional embedding perfectly recovers the 3 components
- Gap between λ_3 = 0 and λ_4: large → components well-separated

## Common Pitfalls
- Choosing k without checking the spectral gap
- Using the wrong Laplacian (combinatorial vs. normalised) for the task
- Forgetting that this is an approximation: k-means on relaxed solution, not exact NCut
- Scalability: eigendecomposition is expensive for large graphs

## Connections
- [[laplacian-eigenmaps]] — the embedding step
- [[spectral-clustering]] — the general technique
- [[graph-laplacian]] — the matrix being decomposed
- [[node-embeddings]] — spectral clustering is an application of embeddings
- [[community-detection]] — an alternative perspective on the same problem

## Open Questions
- How to choose d (embedding dimension) for clustering?
- Can spectral clustering be made inductive?
- How does this relate to modularity-based community detection?
