---
title: "Algebraic Connectivity"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Algebraic connectivity (λ₂) is the second-smallest eigenvalue of the [[graph-laplacian]] — it measures how easy a graph is to disconnect.

## Core Intuition
λ₂ = 0 means the graph is already disconnected. Larger λ₂ means the graph is more "connected" and harder to partition. The Fiedler vector (eigenvector of λ₂) encodes the natural 2-partition.

## Formal Definition / Statement
**Algebraic connectivity:**
λ₂ = second-smallest eigenvalue of L = D - A

**Properties:**
- λ₂ = 0 if and only if the graph is disconnected
- λ₂ > 0 if and only if the graph is connected
- Larger λ₂ means the graph is harder to disconnect
- λ₂ ≤ n/(n-1) × min(degree) for regular graphs

**Fiedler vector:** the eigenvector x₂ corresponding to λ₂.

**Partition rule:** nodes with x₂(i) > 0 go left; nodes with x₂(i) < 0 go right.

**Interpretation:** λ₂ is the algebraic connectivity — a measure of how well-connected the graph is.

## Key Properties
1. **Zero if disconnected**: λ₂ = 0 ⟺ graph has multiple components
2. **Positive if connected**: λ₂ > 0 ⟺ graph is connected
3. **Larger means harder to disconnect**: high λ₂ means robust connectivity
4. **Encodes the natural partition**: the Fiedler vector reveals the sparsest cut
5. **Connects to spectral partitioning**: the Fiedler vector is used for partitioning

## Worked Example
Graph with two dense clusters connected by a few edges:

**λ₂ = 0.42** (small, because the graph is easy to disconnect)
**Fiedler vector:** nodes in cluster A have x₂(i) > 0; nodes in cluster B have x₂(i) < 0
**Interpretation:** the graph is nearly disconnected — the two clusters are weakly linked

## Common Pitfalls
1. **Confusing λ₂ with λ₁**: λ₁ = 0 always; λ₂ measures connectivity
2. **Assuming λ₂ is the only eigenvalue that matters**: higher eigenvalues reveal finer structure
3. **Ignoring that λ₂ depends on normalization**: different Laplacians give different λ₂
4. **Over-interpreting the exact value**: λ₂ is a relative measure, not an absolute one

## Connections
- [[graph-laplacian]] — the matrix whose eigenvalue is λ₂
- [[spectral-partitioning]] — uses the Fiedler vector for partitioning
- [[conductance]] — related community quality measure
- [[normalized-cut]] — related partition objective
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How does λ₂ relate to other connectivity measures (edge connectivity, vertex connectivity)?
- Can we compute λ₂ efficiently for very large graphs?
- How does λ₂ change as the graph evolves?
