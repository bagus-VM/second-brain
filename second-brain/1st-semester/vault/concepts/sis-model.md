---
title: "SIS Model on Networks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*The Susceptible-Infected-Susceptible model where nodes cycle between infected and healthy states, modelling diseases without permanent immunity.*

## Core Intuition
Some diseases don't give lasting immunity — you get sick, recover, and can get sick again (common cold, flu, STIs). The SIS model captures this: nodes alternate between susceptible (S) and infected (I) states forever. The key question is whether the disease becomes endemic (persists indefinitely) or dies out. On networks, the answer depends critically on the network structure.

## Formal Definition / Statement
The SIS model is a compartmental epidemic model where nodes are either Susceptible (S) or Infected (I).

**Dynamics:**
- Infected nodes infect susceptible neighbours with rate β per contact per unit time
- Infected nodes recover and become susceptible again with rate γ
- No immunity: recovered nodes can be reinfected

**Mean-field equations (homogeneous mixing):**
- dS/dt = -βSI + γI
- dI/dt = βSI - γI
- Equilibrium: I* = 1 - γ/β (endemic state) if β > γ, else I* = 0 (disease-free)

**Basic reproduction number:** R₀ = β/γ
- R₀ > 1: disease becomes endemic
- R₀ ≤ 1: disease dies out

**On networks (heterogeneous mean-field):**
- dρ_k/dt = -γρ_k + βk(1 - ρ_k) Θ
- Where ρ_k is the probability a degree-k node is infected, and Θ is the probability a random neighbour is infected
- Epidemic threshold: τ = γ/β = ⟨k⟩/⟨k²⟩
- On scale-free networks: τ → 0 (any disease can persist)

**Stationary state on networks:**
- Below threshold: disease-free equilibrium
- Above threshold: endemic equilibrium with degree-dependent prevalence
- High-degree nodes are infected more frequently: ρ_k ∝ k

## Key Properties / Complexity
- Endemic equilibrium exists only when R₀ > 1
- On scale-free networks, the threshold vanishes (τ → 0)
- High-degree nodes are superspreaders: infected more often and infecting more neighbours
- SIS is a Markov process on the network state space
- Metastability: even below threshold, the disease can persist for O(N) time in finite networks
- Reinfection creates positive feedback: more infected → more contacts → more infection

## Worked Example
Modelling common cold spread in a university (1,000 students, contact network):
1. Parameters: β = 0.03/day, γ = 1/7 (7-day average illness)
2. R₀ = 0.03 × 7 × ⟨k⟩ = 0.21 × 12 = 2.52 > 1 → endemic
3. Simulate SIS on the student contact network:
   - Day 0: 1 infected student
   - Day 30: 15% infected, concentrated in high-degree students (social butterflies)
   - Day 90: equilibrium at ~20% prevalence
4. The disease never fully goes away — students keep getting reinfected
5. Intervention: reduce β by 40% (hand washing campaign)
   - New R₀ ≈ 1.5 — still endemic, but prevalence drops to ~8%
6. Further intervention: reduce β by 70% → R₀ ≈ 0.76 — disease dies out

## Common Pitfalls
- **Mean-field approximation**: Ignores correlations between node states; overestimates spreading
- **No memory**: SIS assumes each infection is independent; real immunity may be partial
- **Static network**: Assumes the contact network doesn't change during the epidemic
- **Constant rates**: β and γ may vary over time (seasonal effects, behavioral changes)
- **Multiple strains**: Real diseases have variants; SIS models a single strain

## Connections
- [[network-diffusion]] — General framework for epidemic dynamics on networks
- [[scale-free-epidemic-threshold-vanishes]] — Why SIS threshold vanishes on scale-free networks
- [[sirs-model]] — Extension with temporary immunity
- [[basic-reproduction-number-r0]] — R₀ determines endemic vs disease-free equilibrium
- [[centrality]] — High centrality nodes are superspreaders in SIS
- [[signed-networks]] — Signed network dynamics have analogous threshold phenomena

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
