---
title: "Embeddedness"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Embeddedness describes a node whose neighbors are themselves densely interconnected — high clustering coefficient, trust, and redundant information.

## Core Intuition
An embedded node sits inside a tightly connected neighborhood. Its removal barely affects connectivity because its neighbors are already well-connected to each other. This contrasts with a [[structural-holes|broker]], whose removal would disconnect groups.

## Formal Definition / Statement
**Embedded node:** a node v with high clustering coefficient C(v), meaning many of v's neighbors are also connected to each other.

**Clustering coefficient:**
C(v) = 2 × (number of edges among v's neighbors) / (deg(v) × (deg(v) - 1))

**Properties:**
- High clustering coefficient (neighbors are interconnected)
- Low betweenness centrality (doesn't sit on many shortest paths)
- Redundant information (neighbors share the same information)
- Trust (neighbors verify each other's information)

## Key Properties
1. **High clustering coefficient**: neighbors are densely connected
2. **Low betweenness**: doesn't broker between groups
3. **Redundant information**: neighbors share the same signals
4. **Trust**: mutual connections enable verification
5. **Structural stability**: removal doesn't fragment the network

## Worked Example
Workplace graph — Team A (Ana, Ben, Cai, Dia):

**Embedded nodes:** Ana, Ben, Cai
- Their neighbors are mutually connected (dense triangle)
- High clustering coefficient
- Low betweenness (not on cross-team paths)

**Broker:** Dia
- Connects Team A to Team B
- Low clustering coefficient
- High betweenness

## Common Pitfalls
1. **Confusing embeddedness with degree**: a node can have high degree but low embeddedness (neighbors not connected to each other)
2. **Assuming embedded nodes are unimportant**: they are important for local cohesion, not for bridging
3. **Ignoring that embeddedness and brokerage are complementary**: a node can be both embedded locally and broker globally

## Connections
- [[structural-holes]] — the opposite of embeddedness
- [[betweenness-centrality]] — embedded nodes have low betweenness
- [[centrality-measures]] — embeddedness is one theory of importance
- [[clustering-coefficient]] — the formal measure of embeddedness
- [[community-detection]] — embedded nodes are community cores
- [[network-science-l04]] — lecture overview

## Open Questions
- How do embeddedness and brokerage interact in real networks?
- Can a node be both embedded and a broker at different scales?
- How does embeddedness relate to innovation and information diffusion?
