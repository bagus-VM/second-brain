---
title: "Basic Reproduction Number R₀"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
R₀ = (β/γ) × ⟨k⟩ is the expected number of secondary infections from one infected node; the epidemic spreads if and only if R₀ > 1.

## Core Intuition
R₀ captures the balance between how easily a disease transmits (β), how quickly people recover (γ), and how many contacts people have (⟨k⟩). If each infected person infects more than one new person on average, the disease grows. If fewer than one, it dies out. The network's average degree amplifies the biological transmission parameters.

## Formal Definition / Statement
For the [[sir-model-network-epidemics]] on a network:

**R₀ = (β/γ) × ⟨k⟩**

where:
- β = transmission probability per S–I edge per time step
- γ = recovery probability per I node per time step
- ⟨k⟩ = average degree of the network

**Epidemic threshold theorem:** A disease becomes an epidemic if and only if R₀ > 1.

**Heterogeneous extension:** For uncorrelated random networks with degree distribution P(k):

T_c ≈ ⟨k⟩ / (⟨k²⟩ − ⟨k⟩)

In scale-free networks with γ ≤ 3, ⟨k²⟩ → ∞, so T_c → 0 (Pastor-Satorras & Vespignani, 2001).

## Key Properties
1. R₀ > 1 ⟹ epidemic; R₀ ≤ 1 ⟹ disease dies out
2. R₀ depends on both biology (β/γ) and network structure (⟨k⟩)
3. In heterogeneous networks, the variance of degree matters more than the mean — hubs dominate transmission
4. For scale-free networks (P(k) ∝ k^(-γ), γ ≤ 3): T_c → 0, meaning no finite threshold
5. The result does not say every disease infects everyone — real networks have finite size, clustering, temporal structure, and capacity limits
6. Policy implication: protect or reduce exposure around high-degree and high-betweenness nodes

## Worked Example
Cold virus: β = 0.3/day, γ = 0.2/day, Ana has degree 4.

R₀ = (0.3/0.2) × 4 = 6

Since R₀ = 6 ≫ 1, the cold becomes an epidemic. If we vaccinate one of Ana's contacts (reducing effective ⟨k⟩), R₀ drops. Vaccinating Dia (the bridge to Team B) is optimal because it also severs inter-community transmission.

## Common Pitfalls
- Treating R₀ as a fixed property of a disease — it depends on the network
- Assuming R₀ > 1 means everyone gets infected — R₀ governs initial growth, not final size
- Ignoring network heterogeneity — in scale-free networks, R₀ based on ⟨k⟩ underestimates spread because hubs drive transmission
- Confusing R₀ with the effective reproduction number R_t, which changes as the epidemic progresses (susceptible pool shrinks)

## Connections
- Central to [[sir-model-network-epidemics]]
- Part of [[simple-contagion]] theory
- The scale-free vanishing threshold connects to [[scale-free-networks]] and [[network-centrality-l04]]
- Vaccination targeting relates to [[network-community-structure-l06]] — bridges and hubs
- Contrasted with [[threshold-cascades]] — complex contagion has a different kind of threshold (fraction q of neighbors)

## Open Questions
- How does R₀ change in temporal networks where edges appear and disappear?
- What is the relationship between R₀ and cascade thresholds in multiplex networks?
