---
title: "Temporal Networks"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Temporal networks assign activation times to edges, revealing that static aggregation creates phantom paths and hides timing bottlenecks that affect whether contagion can actually spread.

## Core Intuition
A static graph takes the union of all edges across time, but real networks evolve — edges appear and disappear. A path that exists in the aggregated static graph may not exist as a time-respecting path if the edges activate in the wrong order. This means static analysis can overestimate reachability, hide bottlenecks, and create false predictions about spreading dynamics.

## Formal Definition / Statement
A **temporal network** is a graph where each edge e has an activation time t(e).

A **time-respecting path** from u to v is a sequence of edges e₁, e₂, …, eₖ where:
- The edges form a path from u to v
- t(e₁) < t(e₂) < ⋯ < t(eₖ)

A path that exists in the aggregated static network may not exist as a time-respecting path — the edges may activate in the wrong order.

## Key Properties / Complexity
1. **Reachability shrinks:** Node pairs connected by static paths may lack time-respecting paths
2. **Speed depends on timing:** A contagion may reach a node in 2 static hops but require 5 time steps for edges to activate in order
3. **Aggregation hides bottlenecks:** A brief bridge may appear permanent in the aggregated graph, masking its role as a temporal bottleneck
4. **Order matters as much as existence:** For time-sensitive processes (epidemics, cascades, information flow), when edges activate is as important as which edges exist

## Worked Example
Temporal network with 4 nodes (A, B, C, D):
- A–B at t = 1
- B–C at t = 3
- C–D at t = 2

**Static graph:** Path A–B–C–D exists. ✓
**Time-respecting path:** A–B (t=1) → B–C (t=3) works, but C–D activated at t=2, before the process reached C at t=3. The C–D edge has already "expired." ✗

**Fix:** Change C–D to t > 3 (e.g., t = 4), giving the time-respecting path A–B (t=1) → B–C (t=3) → C–D (t=4). ✓

## Common Pitfalls
- Treating aggregated static graphs as accurate representations of temporal processes
- Assuming that if a path exists statically, contagion can follow it
- Ignoring that temporal ordering can both help (by breaking transmission) and hinder (by creating waiting times)

## Connections
- Applies to [[simple-contagion]] and [[complex-contagion]] — timing affects both
- Extends [[sir-model-network-epidemics]] — edge timing changes effective R₀
- Connects to [[community-structure]] — temporal bridges are even more fragile than static ones
- Part of the process-structure interaction gap in [[network-diffusion]]
- Survey: Holme & Saramäki (2012), Temporal Networks, Physics Reports

## Open Questions
- How do temporal motifs (recurring interaction patterns) affect spreading dynamics?
- What is the temporal analog of the epidemic threshold?
- How does burstiness (edges clustered in time) affect contagion speed and reach?
