---
title: "SIR Model on Networks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The SIR model partitions nodes into Susceptible, Infected, and Recovered states, modeling disease spread on networks with epidemic threshold R₀ = (β/γ) × ⟨k⟩.

## Core Intuition
Each node is in one of three compartments. Infected nodes transmit the disease to susceptible neighbors with probability β per time step, and recover (gaining immunity) with probability γ per time step. Whether the disease becomes an epidemic depends on the balance between transmission rate and recovery rate, amplified by network connectivity (average degree).

## Formal Definition / Statement
**SIR model on a network:**
- Each node is in state S (Susceptible), I (Infected), or R (Recovered)
- **Infection:** Each S–I edge transmits with probability β per time step
- **Recovery:** Each I node recovers with probability γ per time step
- **Basic reproduction number:** R₀ = (β/γ) × ⟨k⟩, where ⟨k⟩ is the average degree

**Epidemic threshold:** The disease spreads (becomes an epidemic) if R₀ > 1.

**Heterogeneous networks:** For uncorrelated random networks, the epidemic threshold depends on the first two moments of the degree distribution:

T_c ≈ ⟨k⟩ / (⟨k²⟩ − ⟨k⟩)

where T is transmissibility across an edge. If T > T_c, a macroscopic outbreak is possible.

**Scale-free result (Pastor-Satorras & Vespignani, 2001):** In idealized infinite scale-free networks with P(k) ∝ k^(-γ) and γ ≤ 3, ⟨k²⟩ diverges, so T_c → 0 — no finite epidemic threshold.

## Key Properties
1. Three-state compartmental model (S → I → R)
2. R₀ > 1 is the epidemic threshold — depends on both β/γ ratio and ⟨k⟩
3. Hubs are superspreaders — they create disproportionately many transmission opportunities
4. In scale-free networks (γ ≤ 3), the epidemic threshold vanishes: even low transmissibility can spread
5. Recovery provides immunity — nodes do not cycle back to S (contrast with [[sis-model]] and [[sirs-model]])
6. Vaccination strategy: target high-degree and high-betweenness nodes (dynamical version of "target the broker" from [[centrality]])

## Worked Example
A cold virus starts with Ana (β = 0.3 per contact per day, γ = 0.2 per day). Ana has 4 contacts.

R₀ = (β/γ) × ⟨k⟩ = (0.3/0.2) × 4 = 6

Since R₀ = 6 ≫ 1, the cold will spread through the workplace. To slow the spread, vaccinate Dia — she is the only bridge to Team B. Removing her from the susceptible pool severs the only transmission path between teams, confining the epidemic to Team A.

## Common Pitfalls
- Forgetting that R₀ depends on both the biology (β/γ) and the network (⟨k⟩) — changing either affects the threshold
- Assuming the scale-free result (T_c → 0) applies literally to real networks — real networks are finite, clustered, temporal, and capacity-limited
- Confusing SIR (immunity after recovery) with SIS (no immunity) — the dynamics are qualitatively different
- Using R₀ without specifying the network — the same disease has different R₀ on different networks

## Connections
- Core model of [[simple-contagion]]
- Threshold governed by [[basic-reproduction-number-r0]]
- Hubs and superspreading connects to [[centrality]] and [[scale-free-networks]]
- Vaccination targeting connects to [[community-structure]] — bridges are critical bottlenecks
- Contrasted with [[complex-contagion]] — same network, opposite effects of weak ties
- Extended by [[temporal-networks]] — edge timing affects whether transmission paths exist

## Open Questions
- How does network clustering affect the final epidemic size beyond the threshold?
- What is the optimal vaccination strategy when degree information is partial?
