---
title: "Community Structure"
tags: [concept, network-science, semester-1, structure]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [network-intro, connected-component]
---

## One-line Summary
Communities are densely connected groups of nodes within a network — they often correspond to real-world groups like friend circles, research teams, or political factions.

## Core Intuition
Look at a network visualization and you'll often see clusters — groups of nodes with many internal connections and fewer connections to the outside. These clusters frequently correspond to meaningful real-world groupings: friend circles in a school, research groups in a collaboration network, liberal vs. conservative blogs in a political network. The remarkable thing is that you can discover these groups *from structure alone*, without knowing what the nodes represent.

**Community detection is one of the central tasks of network analysis. It answers: "Are there groups? Who's in them?"**

## Formal Definition / Statement
A **community** in a network is a subset of nodes $C \subseteq V$ such that:
- Nodes within $C$ are **densely connected** (many internal edges)
- Nodes within $C$ are **sparsely connected** to nodes outside $C$ (few external edges)

This is an informal definition — formalizing "dense" vs. "sparse" leads to various quality measures:
- **Modularity $Q$:** compares the density of edges within communities to what would be expected in a random graph with the same degree distribution.
- **Conductance:** the fraction of edges leaving a community (lower = more isolated).

There is no single "correct" community structure — different resolutions and methods can yield different valid decompositions.

## Key Properties / Complexity
- Communities are **relative**: what counts as a community depends on the resolution/scale of analysis.
- They are distinct from **connected components**: components are absolute (disconnected or not), while communities are about *relative density*.
- Community structure can reveal **polarization** (political blogs), **research groups** (scientific collaboration), or **social cliques** (high school friendships) — all without node metadata.
- **Overlapping communities** exist in reality: a person can belong to multiple social groups simultaneously.
- Community detection is **computationally hard** in general (NP-hard for many formulations).

## Worked Example
**Political Blog Network (Adamic & Glance 2005):** During the 2004 US election, blogs linking to each other formed two dense clusters — one liberal, one conservative. Community detection on the hyperlink structure alone correctly identifies political alignment. No content analysis needed: *structure reveals meaning*.

**Scientific Collaboration Network:** Researchers who frequently co-author papers form tight clusters corresponding to research groups. Bridges between clusters represent interdisciplinary collaborators.

## Common Pitfalls
- **Confusing communities with components.** Communities exist *within* a connected network. Components are disconnected pieces.
- **Treating detected communities as ground truth.** Community detection algorithms find *structural* clusters, which may or may not correspond to meaningful groups.
- **Assuming communities are non-overlapping.** Real people belong to multiple groups; forcing non-overlapping partitions can be misleading.
- **Ignoring resolution limits.** Some methods can't detect communities below a certain size (resolution limit problem of modularity).

## Connections
- [[connected-component]] — components are the coarsest grouping; communities are finer-grained
- [[network-examples]] — community structure appears across all network domains
- [[centrality]] — bridge nodes between communities have high betweenness centrality
- [[network-diffusion]] — diffusion often follows community boundaries
- [[network-effects]] — communities create echo chambers and lock-in effects

## Open Questions
- How do we determine the "right" number of communities?
- How do communities evolve over time in dynamic networks?
- What is the relationship between community structure and network function (robustness, efficiency)?
