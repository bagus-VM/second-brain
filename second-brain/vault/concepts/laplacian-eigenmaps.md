---
title: "Laplacian Eigenmaps"
tags: [concept, network-science, semester-1, spectral-methods, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-laplacian]]", "[[graph-partitioning-cut-spectral]]"]
---

## One-line Summary
Laplacian eigenmaps embed each node as a point in R^d using the eigenvectors of the graph Laplacian corresponding to the d smallest non-zero eigenvalues (Belkin & Niyogi 2003).

## Core Intuition
The graph Laplacian L = D - A encodes connectivity. Its smallest non-zero eigenvectors capture the graph's large-scale structure — connected nodes get similar values. Using these eigenvectors as coordinates places connected nodes close together in R^d.

## Formal Definition / Statement
Let v_2, v_3, ..., v_{d+1} be the eigenvectors of L for the d smallest non-zero eigenvalues (0 = λ_1 ≤ λ_2 ≤ ... ≤ λ_n). The embedding is:

z_v = (v_2(v), v_3(v), ..., v_{d+1}(v)) ∈ R^d

This is the solution to:
min_Z Σ_{(u,v)∈E} ||z_u - z_v||²  subject to  Z^T D Z = I

The objective pulls connected nodes together; the constraint prevents the trivial z = 0.

Two variants of the Laplacian:
- Combinatorial: L = D - A
- Normalised: L_sym = I - D^{-1/2} A D^{-1/2}

## Key Properties / Complexity
1. L is symmetric positive semi-definite with eigenvalues 0 = λ_1 ≤ λ_2 ≤ ... ≤ λ_n
2. Multiplicity of λ = 0 equals the number of connected components
3. The eigenvectors for the smallest non-zero eigenvalues are most informative (encode large-scale structure)
4. Spectral gap λ_{k+1} - λ_k indicates the "natural" number of clusters
5. [[spectral-clustering-embeddings]] = k-means on Laplacian eigenmaps

## Worked Example
Graph with 3 disconnected components of similar size:
- λ_1 = λ_2 = λ_3 = 0 (multiplicity = 3 components)
- First 3 eigenvectors span piecewise-constant vectors (indicator of each component)
- Gap between λ_3 = 0 and λ_4: large λ_4 → components well-separated; small λ_4 → ambiguous

For two weakly connected clusters: eigenvectors v_2, v_3 embed nodes in R^2 where clusters separate linearly.

## Common Pitfalls
- Cost: O(|E|·d) per iteration for sparse solvers — infeasible for 10^9 × 10^9 Laplacian
- Transductive: new node requires recomputing the entire spectrum
- No features: uses only graph structure, ignores node attributes (text, images)
- Global basis: all nodes share the same eigenvectors; local patterns get averaged away
- Choosing d: use the spectral gap to find natural dimensionality

## Connections
- [[graph-laplacian]] — the matrix being decomposed
- [[graph-partitioning-cut-spectral]] — k-means on eigenmaps
- [[node-embeddings]] — first wave of embedding methods
- [[adjacency-matrix-factorization]] — eigenmaps as implicit matrix factorisation
- [[signed-networks]] — signed Laplacian for signed networks (L06)
- [[deepwalk]] — random-walk alternative that scales better

## Open Questions
- How to approximate spectral embeddings for very large graphs (Lanczos, Nyström)?
- Can we make spectral methods inductive?
- Relationship between Laplacian eigenmaps and graph convolution in GNNs?
