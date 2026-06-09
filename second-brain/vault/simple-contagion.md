---
title: "Simple Contagion"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Simple contagion spreads through a single contact with an active neighbor, making weak ties and bridges accelerators of global spread.

## Core Intuition
A node becomes infected or informed through any single contact with an active neighbor — no social reinforcement needed. This is how diseases and rumors work: one exposure is enough. Because only one contact is required, weak ties and bridges that connect different communities carry the process to otherwise unreachable parts of the network, accelerating global spread.

## Formal Definition / Statement
A contagion is **simple** if the probability of transmission per contact is independent of how many other active neighbors exist. In network terms: each edge from an active to an inactive node carries independent transmission probability β per time step.

Key structural implication: Weak ties and bridges help simple contagion — they carry the process to new communities that would otherwise be unreachable. This is why epidemics and rumors spread globally: they exploit the same inter-community shortcuts that Granovetter identified as carriers of novel information.

## Key Properties
1. Single exposure suffices — no threshold beyond one active neighbor
2. Transmission probability β is per-edge, independent of other edges
3. Weak ties and bridges accelerate spread (opposite of [[complex-contagion]])
4. Hubs are superspreaders due to many edges
5. Modeled by the [[sir-model-network-epidemics]]
6. Epidemic threshold depends on R₀ = (β/γ) × ⟨k⟩ (see [[basic-reproduction-number-r0]])

## Worked Example
A rumor starts with Ana in the workplace network. She has 4 contacts (Ben, Cai, Dia, Eli). One hearing suffices → the rumor crosses the Dia–Fin bridge to Team B. Dia tells Fin; Fin tells Gia and Hal. The rumor reaches everyone because weak ties carry single-exposure processes across community boundaries.

Contrast with [[complex-contagion]]: a new tool requiring 2 adopter contacts gets blocked at the same bridge because Fin only sees 1 adopter (Dia).

## Common Pitfalls
- Confusing simple and complex contagion — the spreading rule determines which structural features help or hinder
- Assuming simple contagion always leads to global spread — vaccination, immunity, and behavior change can create effective barriers
- Treating all processes as simple contagion — many real-world adoptions require social reinforcement

## Connections
- Modeled by [[sir-model-network-epidemics]] — the compartmental framework for simple contagion
- Threshold governed by [[basic-reproduction-number-r0]] — R₀ > 1 implies epidemic spread
- Opposite behavior to [[complex-contagion]] — same structures have opposite effects
- Weak ties role explained in [[weak-tie-paradox-contagion]]
- Hubs as superspreaders connects to [[network-centrality-l04]]
- Validated empirically by [[centola-2010-experiment]] — random networks (shorter paths) spread simple contagion faster

## Open Questions
- How does simple contagion interact with network recovery/removal dynamics?
- What is the effect of heterogeneous transmission probabilities across edges?
