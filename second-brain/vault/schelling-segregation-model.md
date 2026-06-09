---
title: "Schelling Segregation Model"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [homophily]
---

## One-line Summary
Schelling's threshold model shows that mild local preferences for similar neighbors (τ ≈ 1/3) can produce sharp global segregation — a powerful demonstration of how micro-level rules generate macro-level patterns.

## Core Intuition
No one needs to be a segregationist for segregation to emerge. Schelling's insight (1971): if each agent just wants *some* fraction of their neighbors to be like them (say, 1/3), and unhappy agents relocate to where they're satisfied, the iterated process produces stark global separation. The key is the gap between local preference (mild) and global outcome (extreme). This is an emergent property: no agent intends the macro pattern, but the dynamics of local adjustment produce it anyway. In networks, "moving" becomes rewiring — dropping ties to dissimilar contacts and forming ties to similar ones.

## Formal Definition / Statement
**Setup**: Agents of two types on a grid (or network). Each agent i has threshold τ ∈ [0,1] — minimum fraction of same-type neighbors for satisfaction.

**Update rule**:
1. Identify all unsatisfied agents (fraction of same-type neighbors < τ)
2. Each unsatisfied agent moves to a random vacant cell (grid) or rewires a random tie (network)
3. Repeat until no agent wants to move (equilibrium) or stable oscillation

**Key result**: Even τ as low as 1/3 produces sharply segregated patterns.

**Network version**:
- "Neighbors" = graph-adjacent nodes
- "Moving" = dropping a tie to a dissimilar contact, forming a new tie to a similar contact
- Threshold τ controls how much same-type concentration triggers rewiring

## Key Properties
1. **Micro-macro gap**: mild local preferences (τ ≈ 1/3) produce extreme global segregation
2. **Emergent pattern**: no agent intends segregation; it arises from iterated local adjustments
3. **Threshold sensitivity**: small changes in τ can dramatically change the equilibrium pattern
4. **Vacancy matters**: the availability of vacant cells (or potential ties) affects dynamics
5. **Network adaptation**: on graphs, "moving" becomes rewiring — same logic, different topology
6. **Algorithmic amplification**: recommendation algorithms act as automated Schelling rewirers

## Worked Example
**Grid example** (τ = 3/8):
- Blue agent at (1,1) has 1/8 same-type neighbors — below τ = 3/8
- Agent relocates to vacant cell (4,3), where 3/5 neighbors are same-type — satisfied
- Repeat across all unsatisfied agents until equilibrium

**Empirical motivation**: Residential segregation in Chicago by race/ethnicity. Sharp neighborhood boundaries are consistent with Schelling dynamics: each household's mild preference for "some" same-type neighbors, iterated over decades of moves, produces stark global segregation.

**Network implication**: If a platform suggests contacts similar to your current contacts, it acts as an automated Schelling rewirer — accelerating homophily-driven segregation beyond what individual preferences alone would produce.

## Common Pitfalls
1. **Assuming agents are prejudiced**: τ can be very low (1/3) and still produce segregation
2. **Confusing local rule with global outcome**: the macro pattern is not intended by any agent
3. **Ignoring vacancy/rewiring costs**: real agents face constraints on movement
4. **Treating equilibrium as unique**: multiple stable configurations may exist
5. **Overlooking algorithmic amplification**: recommendation systems run Schelling dynamics at machine speed

## Connections
- [[homophily]] — Schelling shows how mild homophily preferences scale to global segregation
- [[selection-vs-socialization]] — Schelling is a generative model that bypasses the causal question
- [[affiliation-networks]] — foci create the opportunity structure for Schelling dynamics
- [[echo-chambers]] — algorithmic recommendation as automated Schelling rewiring
- [[network-science-l05]] — lecture overview

## Open Questions
- What is the right threshold τ for real social networks?
- How do recommendation algorithms interact with Schelling dynamics?
- Can we design platform features that counteract Schelling-style segregation?
- How does the model change with more than two types or continuous attributes?
