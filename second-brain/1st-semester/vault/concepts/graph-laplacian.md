---
title: "Graph Laplacian"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The graph Laplacian L = D - A encodes the structure of a graph — its eigenvalues and eigenvectors reveal connectivity, community structure, and partitioning properties.

## Core Intuition
The Laplacian captures how much a function varies across edges. The smallest eigenvalue (λ₁ = 0) corresponds to the constant eigenvector; the second-smallest eigenvalue (λ₂, the Fiedler value) measures how easy the graph is to disconnect.

## Formal Definition / Statement
**Graph Laplacian:**
L = D - A

where:
- D is the diagonal degree matrix (D_ii = deg(i))
- A is the adjacency matrix

**Normalized Laplacian:**
L_norm = D^(-1/2) L D^(-1/2) = I - D^(-1/2) A D^(-1/2)

**Random-walk Laplacian:**
L_rw = D^(-1) L = I - D^(-1) A

**Properties:**
- L is positive semi-definite
- λ₁ = 0 with eigenvector 1 (constant)
- λ₂ > 0 if and only if the graph is connected
- λ₂ is the algebraic connectivity (Fiedler value)

**Time complexity:** O(n³) for full eigendecomposition; faster sparse approximations exist.

## Key Properties / Complexity
1. **Positive semi-definite**: all eigenvalues are non-negative
2. **λ₁ = 0**: always, with constant eigenvector
3. **λ₂ > 0 if connected**: the Fiedler value measures connectivity
4. **Encodes community structure**: the Fiedler vector reveals the natural partition
5. **Multiple forms**: unnormalized, normalized, random-walk — each has different properties

## Worked Example
Graph with two dense clusters connected by a few edges:

1. Compute L = D - A
2. Find eigenvalues: λ₁ = 0, λ₂ = 0.42 (small, because the graph is easy to disconnect)
3. Find Fiedler vector x₂: nodes in cluster A have x₂(i) > 0; nodes in cluster B have x₂(i) < 0
4. The partition naturally separates the two clusters

The small λ₂ confirms that the graph is nearly disconnected — the two clusters are weakly linked.

## Common Pitfalls
1. **Confusing different Laplacians**: unnormalized, normalized, and random-walk have different properties
2. **Ignoring that λ₂ = 0 means disconnected**: the graph has multiple components
3. **Assuming the Laplacian is invertible**: it's singular (λ₁ = 0)
4. **Over-interpreting small eigenvalues**: small λ₂ means easy to disconnect, but the exact value depends on normalization

## Connections
- [[spectral-partitioning]] — uses the Fiedler vector for partitioning
- [[normalized-cut]] — uses the normalized Laplacian
- [[algebraic-connectivity]] — λ₂, the second-smallest eigenvalue
- [[conductance]] — related community quality measure
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How do different Laplacians compare on real-world networks?
- Can we use the Laplacian for other tasks beyond partitioning?
- How does the Laplacian relate to random walks and diffusion?
