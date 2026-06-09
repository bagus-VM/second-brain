---
title: "Conductance"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Conductance measures the fraction of edges that leave a community relative to its total degree — a normalized measure of how "well-separated" a community is from the rest of the graph.

## Core Intuition
A good community has few edges leaving it relative to its size. Conductance captures this by comparing the cut size to the smaller of the two cluster volumes, ensuring the measure is sensitive to the weaker side of the partition.

## Formal Definition / Statement
For a subset S ⊆ V:

**Conductance:**
φ(S) = cut(S, S̄) / min(vol(S), vol(S̄))

where:
- cut(S, S̄) = number of edges between S and its complement S̄
- vol(S) = Σ_{i ∈ S} k_i (total degree of nodes in S)
- vol(S̄) = Σ_{i ∈ S̄} k_i (total degree of nodes not in S)

**Range:** φ(S) ∈ [0, 1]
- φ(S) = 0: no edges leave S (perfect community)
- φ(S) = 1: every edge from S goes outside (no community structure)

**Graph conductance:** φ(G) = min_{S ⊆ V} φ(S) — the minimum conductance over all subsets.

**NP-hard to compute exactly:** finding the set S that minimizes conductance is NP-hard. Spectral methods provide approximations.

## Key Properties
1. **Normalized**: accounts for cluster size, not just cut size
2. **Sensitive to the smaller cluster**: uses min(vol(S), vol(S̄)) to avoid trivial solutions
3. **NP-hard to minimize**: finding the exact minimum conductance is computationally hard
4. **Connects to spectral methods**: the Fiedler vector approximates the minimum conductance cut
5. **Used in community quality**: lower conductance means better community

## Worked Example
Community S with 10 nodes, vol(S) = 30, vol(S̄) = 200, cut(S, S̄) = 5:

φ(S) = 5 / min(30, 200) = 5 / 30 ≈ 0.167

Interpretation: 16.7% of S's edges leave the community — S is reasonably well-separated.

## Common Pitfalls
1. **Confusing conductance with [[modularity]]**: modularity compares observed to expected edges; conductance compares cut to volume
2. **Confusing conductance with [[normalized-cut]]**: normalized cut sums both sides; conductance uses the minimum
3. **Assuming low conductance always means a good community**: a single node with one edge has conductance 0, but isn't a meaningful community
4. **Ignoring that conductance is NP-hard to minimize**: spectral methods are approximations

## Connections
- [[normalized-cut]] — related but distinct normalized measure
- [[modularity]] — alternative community quality objective
- [[spectral-partitioning]] — spectral methods approximate minimum conductance
- [[graph-laplacian]] — the Laplacian encodes conductance information
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How does conductance compare to modularity on real-world networks?
- Can we compute conductance efficiently for large graphs?
- How do we handle overlapping communities with conductance?
