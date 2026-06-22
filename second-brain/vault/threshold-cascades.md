---
title: "Threshold Cascades"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A threshold cascade occurs when [[complex-contagion]] spreads globally through a network, requiring dense clusters linked by wide bridges and a threshold q that is not too high.

## Core Intuition
A cascade starts from a seed set of initially active nodes. At each step, nodes whose active-neighbor fraction meets threshold q adopt. The cascade may spread globally or stall — the outcome depends on both q and the local network density around the wavefront. Unlike simple contagion epidemics that exploit any single path, threshold cascades need local reinforcement at every step.

## Formal Definition / Statement
**Threshold cascade:** Starting from a seed set, node v adopts if |active neighbors| / |total neighbors| ≥ q.

**Cascade condition:** In a uniform-threshold network, a global cascade starting from a small seed set is possible if:
1. The network contains enough dense clusters (where neighbors reinforce each other above q)
2. These clusters are linked by wide bridges (multiple edges providing enough reinforcement)
3. The threshold q ≤ 1/2 (if q > 1/2, cascades require majority adoption locally, which is very hard to trigger)

## Key Properties
1. Outcome depends on both threshold q and local network density
2. Dense clusters sustain internal adoption — essential for [[complex-contagion]]
3. Wide bridges (multiple edges between communities) enable cross-community spread
4. Thin bridges (single edges) block cascades — insufficient reinforcement
5. q > 1/2 creates a strong barrier — cascades require local majority
6. Opposite dynamics to [[simple-contagion]] epidemics

## Worked Example
Two communities of 20 people each. Behavior with q = 0.2 starts with all 20 in community 1 adopting.

**Wide bridge (5 parallel edges):** A community-2 node with 5 cross-community ties has 5/10 = 0.5 ≥ 0.2. Cascade crosses.

**Thin bridge (1 edge):** The bridging node has 1/10 = 0.1 < 0.2. Cascade blocked.

The same communities with a disease ([[simple-contagion]]) would see the epidemic cross in both cases — a single S–I contact suffices.

## Common Pitfalls
- Assuming cascades always spread if the seed is large enough — local density matters more than seed size
- Confusing threshold cascades with epidemic models — epidemics need only one contact; cascades need reinforcement
- Ignoring the q > 1/2 barrier — it makes cascades qualitatively different
- Treating cascades as deterministic — real adoption has stochastic elements not captured by pure threshold rules

## Connections
- Mechanism of [[complex-contagion]]
- Opposite dynamics to [[simple-contagion]] and [[sir-model-network-epidemics]]
- Bridge structure connects to [[community-structure]]
- Empirically studied by [[centola-2010-experiment]]
- The threshold q relates to [[basic-reproduction-number-r0]] — both are "will it spread?" conditions but for different processes
- Connects to [[weak-tie-paradox-contagion]]

## Open Questions
- How do cascades behave in multiplex networks where different layers have different thresholds?
- What is the effect of stubborn nodes (nodes that never adopt) on cascade dynamics?
- How does network adaptation (rewiring) affect cascade conditions?
