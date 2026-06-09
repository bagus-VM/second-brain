---
title: "Bridges and Local Bridges"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[network-science-graph-fundamentals]]"]
---

## One-line Summary
A bridge is an edge whose removal disconnects the graph; a local bridge is an edge whose endpoints share no common neighbors — both are critical for information flow across communities.

## Core Intuition
Communities are densely connected internally but sparsely connected externally. The edges that connect communities are structurally special: they control what information flows between groups. Bridges are the extreme case — remove one and the network literally falls apart. Local bridges are the practical version — they don't disconnect the graph, but their endpoints have no shared neighbors, meaning any information that crosses must travel through this single edge. Under [[strong-triadic-closure|STC]], local bridges must be [[weak-ties-hypothesis|weak ties]].

## Formal Definition / Statement
**Bridge.** An edge e ∈ E is a **bridge** if removing it increases the number of connected components. Equivalently, e lies on no cycle.

**Local bridge.** An edge (u, v) is a **local bridge** if u and v have no neighbors in common:
```
N(u) ∩ N(v) = ∅
```
Equivalently, the [[neighborhood-overlap]] O(u, v) = 0.

A local bridge does *not* need to disconnect the graph — the endpoints may still reach each other via a long detour.

## Key Properties
- Every bridge is also a local bridge (but not vice versa)
- A local bridge with endpoints sharing no neighbors: if removed, endpoints' shortest-path distance must increase (no shortcut through shared neighbors)
- Local bridge ↔ O(u, v) = 0 (directly expressible in terms of neighborhood overlap)
- Under STC with ≥ 2 strong ties at an endpoint, any local bridge must be labeled Weak ([[weak-ties-hypothesis]])
- Bridges are rare in dense networks; local bridges are common

## Worked Example
In the lecture's workplace scenario:
- Team A (Ana, Ben, Cai, Dia, Eli) is densely connected
- Team B (Fin, Gia, Hal, Ivo) is densely connected
- The Dia–Fin edge is the only connection between teams
- N(Dia) ∩ N(Fin) = ∅ (they share no common neighbors)
- Therefore Dia–Fin is a **local bridge** with O = 0
- Under STC, since Dia has multiple strong ties (within Team A), the Dia–Fin edge must be **weak**

This single weak tie controls all information flow between the two teams.

## Common Pitfalls
- Thinking a bridge must be "important" in the sense of betweenness — a bridge in a tree is trivially a bridge but may not carry much traffic
- Confusing local bridges with edge cuts — an edge cut is a *set* of edges; a bridge is a single edge
- Assuming local bridges are always weak — this requires the STC premise (≥ 2 strong ties at an endpoint)
- Forgetting that local bridges are detected by O = 0, which is computable in polynomial time

## Connections
- Detected by: [[neighborhood-overlap]] (O = 0)
- Must be weak under: [[weak-ties-hypothesis]] (given STC)
- Related concept: [[structural-holes]] (Burt's theory of brokerage)
- Related concept: [[social-capital]] (bridges create information advantage)
- Empirically tested: Onnela et al. (2007) knockout experiment
- Part of: [[network-science-l03]]

## Open Questions
- How do multiplex networks (multiple edge types) change bridge semantics?
- What is the relationship between local bridges and betweenness centrality?
- How do temporal networks (edges appearing/disappearing) affect bridge identification?
