---
title: "Network Science L08: Network Dynamics"
tags: [topic, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Network dynamics studies how processes (diseases, rumors, behaviors) spread on networks, revealing that the same structure can accelerate one process and block another depending on the spreading rule.

## Core Intuition
Static network analysis (L03–L07) tells us what the network looks like. Dynamic analysis asks: what happens on the network? The key insight is that structure alone does not determine outcomes — the spreading rule matters just as much. A bridge that accelerates a rumor can block a behavior adoption, because rumor needs only one contact (simple contagion) while adoption needs social reinforcement (complex contagion).

## Key Topics in This Lecture

### [[simple-contagion]]
A single contact with an active node suffices to transmit. Weak ties and bridges accelerate spread. Modeled by the [[sir-model-network-epidemics]] (Susceptible–Infected–Recovered).

### [[sir-model-network-epidemics]]
Compartmental model where each node is S, I, or R. Infection probability β per S–I edge per time step; recovery probability γ per I node per time step. The epidemic threshold is governed by [[basic-reproduction-number-r0]].

### [[basic-reproduction-number-r0]]
R₀ = (β/γ) × ⟨k⟩. If R₀ > 1, the disease becomes an epidemic. In scale-free networks with γ ≤ 3, the threshold vanishes (T_c → 0) due to hubs — the [[scale-free-epidemic-threshold-vanishes]] result.

### [[complex-contagion]]
A node adopts only when a fraction q of its neighbors have adopted. Requires social reinforcement. Weak ties and bridges block spread instead of helping.

### [[threshold-cascades]]
Global cascades from complex contagion depend on threshold q, network density, and bridge width. If q > 1/2, cascades require local majority adoption — very hard to trigger.

### [[weak-tie-paradox-contagion]]
The same weak ties that Granovetter identified as carriers of novel information (simple contagion) become barriers for behaviors requiring reinforcement (complex contagion).

### [[centola-2010-experiment]]
Empirical confirmation: behavior spread faster in clustered networks (54% adoption) than random networks (38%) with same degree and diameter. Multiple exposures drive adoption.

### [[temporal-networks]]
Edges have activation times. Time-respecting paths require edges to activate in chronological order. Static aggregation creates phantom paths and hides bottlenecks.

### [[process-structure-interaction-gap]]
The sixth gap in the course: the same network structure produces different outcomes depending on the spreading process. Neither structure nor process alone determines the outcome.

## The Six Gaps of the Course
| Lecture | Gap Type | Core Tension |
|---------|----------|--------------|
| L03–L04 | Computational | NP-hard ideals vs. polynomial proxies |
| L05 | Causal | Mechanism unidentifiable from snapshots |
| L06 | Structural | Complete-graph theory meets sparse data |
| L07 | Navigational | Short paths exist but aren't locally findable |
| L08 | Process-structure | Same structure, different outcomes for different processes |
| L08 (temporal) | Temporal | Static aggregation hides causal order |

## Connections
- Builds on [[network-community-structure-l06]] — communities determine where contagion pauses or accelerates
- Builds on [[network-navigation-small-worlds-l07]] — navigability relates to how processes find paths
- Connects to [[weak-ties-and-bridges]] — Granovetter's weak ties play opposite roles for simple vs. complex contagion
- Connects to [[network-centrality-l04]] — hubs are superspreaders; targeting high-betweenness nodes is the dynamical version of "target the broker"
- Relates to [[diffusion-of-innovations]] — adoption thresholds model technology and norm spreading

## Open Questions
- How do competing contagions (e.g., two rumors, two technologies) interact on the same network?
- What happens when the network itself co-evolves with the contagion (adaptive networks)?
- How do memory and repeated exposure modify threshold models beyond simple fraction rules?

## Reading
- Easley & Kleinberg (2010), Ch. 19 (cascades/thresholds), Ch. 21 (epidemics)
- Centola (2010), Science 329, 1194–1197
- Holme & Saramäki (2012), Temporal Networks, Physics Reports
