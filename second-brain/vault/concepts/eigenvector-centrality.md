---
title: "Eigenvector Centrality"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Eigenvector centrality measures recursive prestige — important nodes are connected to important nodes, formalized as the leading eigenvector of the adjacency matrix.

## Core Intuition
A node's importance depends on the importance of its neighbours. This recursive definition leads to the eigenvector equation: Ax = λx, where x is the centrality vector and λ is the leading eigenvalue.

## Formal Definition / Statement
**Node equation:**
C_E(v) = (1/λ) Σ_u A_vu C_E(u)

**Vector equation:**
Ax = λx

where:
- A is the adjacency matrix
- x is the centrality vector (leading eigenvector)
- λ is the leading eigenvalue

**Power iteration:**
x^(t+1) = Ax^(t) / ||Ax^(t)||

**Complexity:** O(k(n + m)) for k iterations (often written O(km) on connected sparse graphs).

**PageRank extension:**
PR(v) = (1-α)/n + α Σ_{u→v} PR(u)/outdeg(u)

- Random surfer: with probability α, follow a link; with probability 1-α, jump to a random page
- Range: PageRank scores are probabilities (sum to 1)

## Key Properties / Complexity
1. **Recursive prestige**: importance flows from important neighbours
2. **Leading eigenvector**: the centrality vector is the eigenvector of the largest eigenvalue
3. **Power iteration**: converges quickly for connected graphs
4. **PageRank**: adds a damping factor to handle dangling nodes and disconnected components
5. **Cheatable**: link farms can manufacture endorsements (unlike harmonic centrality)

## Worked Example
Workplace graph — Team A (Ana, Ben, Cai, Dia):

**Eigenvector centrality of Ana:**
- Connected to Ben, Cai, Dia (all in Team A's dense core)
- High centrality because neighbours are also well-connected

**Eigenvector centrality of Dia:**
- Connected to Ana, Ben, Cai (Team A) and Fin (Team B)
- Moderate centrality — connected to both dense and sparse regions

**Winner: Ana or Ben** — connected to densely-connected others, which amplifies recursively.

## Common Pitfalls
1. **Confusing with degree centrality**: degree counts direct contacts; eigenvector weights contacts by their importance
2. **Assuming eigenvector centrality is always well-defined**: on disconnected graphs, there may be multiple leading eigenvectors
3. **Ignoring that PageRank adds a damping factor**: PageRank is not pure eigenvector centrality
4. **Forgetting that eigenvector centrality can be cheated**: link farms can inflate scores

## Connections
- [[centrality-measures]] — one of the main centrality measures
- [[pagerank]] — extension with damping factor
- [[degree-centrality]] — local measure, ignores neighbour importance
- [[betweenness-centrality]] — measures brokerage, not prestige
- [[network-science-l04]] — lecture overview

## Open Questions
- How does eigenvector centrality perform on directed or weighted graphs?
- Can we detect and prevent manipulation of eigenvector centrality?
- How does eigenvector centrality relate to network robustness?
