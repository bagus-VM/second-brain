---
title: "Network Dynamics"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The study of how processes unfold on networks — epidemic spreading, information diffusion, opinion formation, and cascading failures.*

## Core Intuition
A network is not just a static structure — things happen on it. Diseases spread through contact networks, information spreads through social networks, failures cascade through power grids, and opinions form through influence networks. The structure of the network fundamentally shapes how these dynamic processes unfold. A rumor spreads differently in a tight-knit community than in a random graph. Understanding network dynamics means understanding how structure determines behavior.

## Formal Definition / Statement
Network dynamics studies processes that evolve on or are influenced by network structure. Major models include:

**Epidemic Models:**

1. **SI (Susceptible-Infected)**: Nodes are either S or I. Infected nodes never recover.
   - dS/dt = -βSI, dI/dt = βSI
   - Simplest model; always reaches full infection

2. **SIS (Susceptible-Infected-Susceptible)**: Infected nodes recover and become susceptible again.
   - dS/dt = -βSI + γI, dI/dt = βSI - γI
   - Basic reproduction number R₀ = β/γ
   - Epidemic threshold: R₀ > 1 for spreading

3. **SIR (Susceptible-Infected-Recovered)**: Recovered nodes gain permanent immunity.
   - dS/dt = -βSI, dI/dt = βSI - γI, dR/dt = γI
   - Models one-time epidemics (measles, etc.)

4. **SIRS**: Like SIR but immunity wanes over time.

**On networks:**
- Heterogeneous mean-field theory: degree-dependent infection rates
- Epidemic threshold on scale-free networks: vanishes as ⟨k²⟩ → ∞
- Superspreaders: high-degree nodes drive epidemic propagation

**Information Diffusion:**
- Independent Cascade Model: each infected neighbor has one chance to infect
- Linear Threshold Model: node activates when fraction of neighbors exceeds threshold
- Rumor/LT models for viral marketing

**Cascading Failures:**
- Load redistribution after node failure can trigger cascades
- Scale-free networks are robust to random failures but fragile to targeted attacks

## Key Properties / Complexity
- R₀ (basic reproduction number): average number of secondary infections from one infected node
- Epidemic threshold on networks: depends on the spectral radius of the adjacency matrix
- Scale-free networks have no epidemic threshold (R₀ can be infinitesimally small and still spread)
- Network topology affects speed, final size, and critical thresholds of spreading
- Temporal networks (time-varying edges) can slow or accelerate spreading compared to static networks
- Superspreader events arise from network heterogeneity, not pathogen properties

## Worked Example
Modeling COVID-19 spread on a city contact network:
1. Build network: nodes = people, edges = daily contacts (home, work, transport, leisure)
2. Use SIR model with β = 0.05 (transmission rate per contact per day), γ = 1/7 (7-day recovery)
3. R₀ = β × ⟨k⟩ / γ = 0.05 × 15 / (1/7) ≈ 5.25
4. Simulate on the contact network:
   - Day 0: 1 infected node (the index case)
   - Day 10: 50 infected, mostly in the index case's workplace cluster
   - Day 30: 2,000 infected, spread across multiple communities
   - Day 60: Epidemic peaks at 8,000 active infections
5. Intervention: reduce β by 50% (masking) and remove 30% of edges (lockdown)
6. New R₀ ≈ 1.8 — epidemic still grows but slowly, buying time for vaccination

## Common Pitfalls
- **Mean-field assumptions**: Classical ODE models assume homogeneous mixing; real networks are heterogeneous
- **R₀ ≠ R_t**: The effective reproduction number changes as the network state changes
- **Network sampling**: Contact networks are hard to measure accurately; missing edges change predictions
- **Behavioral changes**: People change their behavior during epidemics, altering the network dynamically
- **Multiple timescales**: Network evolution (new contacts) and epidemic dynamics (infection/recovery) operate on different timescales

## Connections
- [[sis-model]] — SIS model detailed treatment on networks
- [[sirs-model]] — SIRS model with waning immunity
- [[basic-reproduction-number-r0]] — R₀ and epidemic thresholds
- [[scale-free-epidemic-threshold-vanishes]] — Why scale-free networks have no epidemic threshold
- [[network-community-structure-l06]] — Community structure affects epidemic containment strategies
- [[small-world-networks]] — Small-world structure accelerates spreading

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
