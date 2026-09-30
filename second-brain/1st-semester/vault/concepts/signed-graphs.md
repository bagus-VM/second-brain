---
title: "Signed Graphs"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-fundamentals]]"]
---

## One-line Summary
A signed graph assigns a positive or negative label to every edge, encoding alliance vs. rivalry — a single bit per edge that powerfully constrains global structure.

## Core Intuition
Most of network science treats edges as binary: present or absent. But in social systems, relationships carry *valence*. A positive edge (+) means friendship, trust, or alliance; a negative edge (−) means hostility, distrust, or rivalry. This seemingly small addition — one bit per edge — turns out to impose strong constraints on which global structures are psychologically stable. The study of signed graphs is the study of *how local relational signs determine global network topology*.

## Formal Definition / Statement
A **signed graph** is a pair (G, σ) where G = (V, E) is a graph and σ : E → {+, −} assigns a sign to every edge.

- σ(e) = +: alliance, friendship, trust
- σ(e) = −: rivalry, hostility, distrust

A **complete signed graph** has an edge (with some sign) between every pair of nodes. The [[balance-theorem]] applies specifically to complete signed graphs.

## Key Properties / Complexity
- The sign is a single bit per edge, yet it constrains global structure
- Signed graphs are the foundation for [[structural-balance-theory]]
- Triangle-level sign patterns determine network-level stability (see [[balanced-triads]])
- Real signed networks (Epinions, Slashdot, Wikipedia) are typically sparse and directed — the complete-graph idealization rarely holds exactly
- Most observed edges are positive (~77–85% in empirical datasets)

## Worked Example
**Cold War alliances (pre-1960):** Five nations — USA, UK, France, USSR, China — form a complete signed graph K₅. Western nations share positive edges among themselves and negative edges toward Eastern nations (and vice versa). This produces exactly two balanced camps: {USA, UK, France} and {USSR, China}. Every one of the 10 triangles has 0 or 2 negative edges — the graph is strongly balanced.

**Post-1969 Sino-Soviet split:** The USSR–China edge flips to negative. Triangles like USA–USSR–China now have three negative edges (−, −, −), violating strong balance. But the graph satisfies [[weak-structural-balance]], partitioning into three camps: {USA, UK, France}, {USSR}, {China}.

## Common Pitfalls
- Assuming all edges are undirected — real signed networks (Epinions, Slashdot) are often *directed* (A trusts B doesn't mean B trusts A)
- Treating missing edges as neutral — in a sparse network, the absence of an edge is different from a negative edge
- Confusing the sign of an edge with its weight — a weak friendship is still positive, not "less positive"
- Applying the [[balance-theorem]] to incomplete graphs — the theorem requires a complete signed graph

## Connections
- Foundation for: [[structural-balance-theory]], [[balanced-triads]], [[balance-theorem]]
- Extends: [[graph-fundamentals]] (adds sign to edges)
- Measured by: [[frustration-index]] (how far from balanced)
- Related to: [[homophily]] (sign patterns reflect attitude alignment)
- Empirical data: Leskovec, Huttenlocher & Kleinberg (2010) — Epinions, Slashdot, Wikipedia signed networks

## Open Questions
- How do signs evolve over time — do unbalanced triangles resolve toward balance?
- Can we predict sign of missing edges from network structure?
- How does directionality interact with sign (directed signed balance)?
