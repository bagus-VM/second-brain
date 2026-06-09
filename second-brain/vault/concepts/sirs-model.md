---
title: "SIRS Model on Networks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*An epidemic model with temporary immunity: Susceptible → Infected → Recovered → Susceptible, modeling diseases where immunity wanes over time.*

## Core Intuition
SIR assumes permanent immunity, SIS assumes no immunity. Reality is usually in between — you recover from the flu, have immunity for months, then become susceptible again. SIRS models this waning immunity. It creates oscillatory dynamics: an epidemic sweeps through, most people become immune, the disease dies down, immunity wanes, and the cycle repeats. This is why we have flu seasons.

## Formal Definition / Statement
The SIRS model extends SIR with waning immunity:

**States:**
- S (Susceptible): can be infected
- I (Infected): actively spreading the disease
- R (Recovered): temporarily immune

**Transitions:**
- S → I: infection at rate β per infected contact
- I → R: recovery at rate γ
- R → S: immunity loss at rate δ (waning immunity)

**Mean-field equations:**
- dS/dt = -βSI + δR
- dI/dt = βSI - γI
- dR/dt = γI - δR

**Endemic equilibrium:**
- I* = δ(β - γ) / (β(γ + δ)) when β > γ
- As δ → 0 (permanent immunity): reduces to SIR dynamics
- As δ → ∞ (no immunity): reduces to SIS dynamics

**On networks:**
- Heterogeneous mean-field: degree-dependent equations
- Oscillatory behavior: epidemic waves with period ~ 1/δ
- Network structure affects amplitude and frequency of oscillations

**Key parameter: 1/δ = average immunity duration**
- COVID-19: 1/δ ≈ 6-12 months
- Influenza: 1/δ ≈ 6-12 months (plus antigenic drift)
- Common cold: 1/δ ≈ weeks to months

## Key Properties / Complexity
- Oscillatory dynamics: epidemic waves driven by immunity waning
- Period of oscillations ≈ 2π/√(δ × γ × (β - γ)) in the mean-field limit
- Network heterogeneity affects wave amplitude but not fundamental period
- Can exhibit chaos in certain parameter regimes (seasonal forcing)
- Intermediate between SIR (δ=0) and SIS (δ=∞)
- More realistic than SIR/SIS for many real diseases

## Worked Example
Modeling influenza in a city (population 1M, contact network):
1. Parameters: β = 0.05/day, γ = 1/5 (5-day illness), δ = 1/180 (6-month immunity)
2. R₀ = β⟨k⟩/γ = 0.05 × 15 / 0.2 = 3.75
3. Simulate on the contact network:
   - Winter wave 1: peaks at 5% infected, 60% recovered (immune)
   - Summer: prevalence drops to 0.1%
   - Autumn: immunity wanes for wave 1 cohort, susceptible pool grows
   - Winter wave 2: peaks at 4.5% (slightly lower due to residual immunity)
4. Pattern: annual flu waves driven by the 6-month immunity cycle
5. Vaccination strategy: vaccinate before winter to boost immunity in the recovered cohort
6. Network effect: children (school networks) drive early spread; adults (workplace networks) sustain it

## Common Pitfalls
- **Parameter estimation**: β, γ, and δ are hard to measure accurately in the real world
- **Strain diversity**: Real diseases have multiple strains; SIRS models a single strain
- **Network evolution**: Contact patterns change seasonally (school terms, holidays)
- **Age structure**: Immunity duration varies by age; homogeneous δ is a simplification
- **Behavioral response**: People change behavior during outbreaks, affecting β dynamically

## Connections
- [[network-dynamics-l08]] — General framework for epidemic dynamics
- [[sis-model]] — Limiting case as δ → ∞ (no immunity)
- [[basic-reproduction-number-r0]] — R₀ determines epidemic potential
- [[network-community-structure-l06]] — Communities create localized waves before global spread
- [[scale-free-epidemic-threshold-vanishes]] — Threshold behavior in heterogeneous networks
- [[signed-networks]] — Signed network dynamics have analogous oscillatory behavior

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
