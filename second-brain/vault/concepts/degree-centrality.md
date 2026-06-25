---
title: "Degree Centrality"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Degree centrality measures the number of direct contacts a node has — the simplest and most local measure of importance.

## Core Intuition
A node with many direct contacts has high degree centrality. This captures the idea of "popularity" or "exposure" — how many people does this node interact with directly?

## Formal Definition / Statement
**Raw form:**
C_D^raw(v) = deg(v)

**Normalized form:**
C_D(v) = deg(v) / (n-1)

**Range:** Raw: 0 to n-1. Normalized: 0 to 1.

**Complexity:** All scores: O(n + m) including initialization. Sorted ranking adds O(n log n).

**Interpretation:** direct exposure — importance comes from immediate contacts.

**Degree distribution:** the distribution of degrees across all nodes. Equal-sized degrees suggest homogeneous structure; a heavy-tailed/power-law distribution suggests hubs and inequality (Barabási & Albert 1999).

## Key Properties
1. **Local measure**: only counts direct neighbors
2. **Cheapest to compute**: O(1) per node if degree is stored
3. **Degree distribution**: quick property check for network structure
4. **Heavy-tailed distributions**: suggest hubs and inequality
5. **No information about neighbor importance**: all neighbors weighted equally

## Worked Example
Workplace graph — Team A (Ana, Ben, Cai, Dia):

**Degree of Ana:** 3 (connected to Ben, Cai, Dia)
**Degree of Ben:** 3 (connected to Ana, Cai, Dia)
**Degree of Cai:** 2 (connected to Ana, Ben)
**Degree of Dia:** 3 (connected to Ana, Ben, Cai) + 1 (Fin) = 4

**Winner: Dia** — most direct contacts (4).

## Common Pitfalls
1. **Assuming high degree means high importance**: degree ignores the structure of the neighborhood
2. **Confusing degree with other centrality measures**: degree doesn't capture brokerage, proximity, or prestige
3. **Ignoring degree distribution**: the shape of the distribution reveals network structure
4. **Over-interpreting degree in isolation**: high degree may not mean high influence

## Connections
- [[centrality-measures]] — one of the main centrality measures
- [[closeness-centrality]] — measures proximity, not direct contacts
- [[betweenness-centrality]] — measures brokerage, not direct contacts
- [[eigenvector-centrality]] — weights neighbors by their importance
- [[power-law-distribution]] — heavy-tailed degree distributions
- [[network-science-l04]] — lecture overview

## Open Questions
- How does degree centrality perform on directed or weighted graphs?
- Can we combine degree with other centrality measures?
- How does degree centrality relate to network robustness?
