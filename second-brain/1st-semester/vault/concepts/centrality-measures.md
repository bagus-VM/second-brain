---
title: "Centrality Measures"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[network-science-l03]]"]
---

## One-line Summary
Centrality measures quantify node importance — but each measure encodes a different theory of what "important" means (degree = exposure, closeness = access, betweenness = control, eigenvector = prestige).

## Core Intuition
There is no single "most important" node. Different centrality measures capture different social advantages. Choosing a measure is choosing a theory — not collecting an objective fact.

## Formal Definition / Statement

### Degree Centrality
$$C_D(v) = \frac{\deg(v)}{n-1}$$
- **Theory**: direct exposure — importance from immediate contacts
- **Complexity**: O(n + m) for all nodes

### Closeness Centrality
$$C_C(v) = \frac{n-1}{\sum_{u \neq v} d(v, u)}$$
- **Theory**: short-path access — importance from being near everyone
- **Complexity**: O(n + m) per node (BFS); O(n(n + m)) for all nodes

### Harmonic Centrality
$$H(v) = \sum_{u \neq v} \frac{1}{d(v, u)} \quad \text{with } \frac{1}{\infty} = 0$$
- **Theory**: robust reachability — unreachable nodes contribute 0, not ∞
- **Complexity**: same as closeness
- This is the disconnected-graph extension of closeness

### Betweenness Centrality
$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$
- **Theory**: brokerage — importance from sitting on paths between others
- **Complexity**: O(n(n + m)) for all nodes (Brandes algorithm)
- Exact for one focal node also requires all-source dependency info

### Eigenvector Centrality
$$C_E(v) = \frac{1}{\lambda} \sum_{u} A_{vu} C_E(u) \quad \Leftrightarrow \quad Ax = \lambda x$$
- **Theory**: recursive prestige — important nodes are connected to important nodes
- **Complexity**: O(k(n + m)) for k power-iteration steps

### PageRank
$$PR(v) = \frac{1-\alpha}{n} + \alpha \sum_{u \to v} \frac{PR(u)}{\text{outdeg}(u)}$$
- **Theory**: random surfer model — follow links with prob α, jump randomly with prob 1-α
- **Range**: scores sum to 1 (probabilities)
- **Cheatable**: link farms can manufacture endorsements

## Key Properties / Complexity

| Measure | Theory | One node | All nodes |
|---------|--------|----------|-----------|
| Degree | direct exposure | O(deg v) | O(n + m) |
| Closeness | short-path access | O(n + m) | O(n(n + m)) |
| Harmonic | reachable proximity | O(n + m) | O(n(n + m)) |
| Betweenness | path brokerage | O(n(n + m)) | O(n(n + m)) |
| Eigenvector/PageRank | recursive prestige | whole vector | O(k(n + m)) |

- With weighted edges: replace BFS by Dijkstra → O(m + n log n) per source
- Closeness asks "how near is v to everyone?"; betweenness asks "how many shortest paths depend on v?"

## Worked Example
Toy graph: edges AB, AC, AD, DE (n=5).

| Node | Distances | Closeness | Harmonic | Betweenness |
|------|-----------|-----------|----------|-------------|
| A | 1,1,1,2 | 4/5 = 0.80 | 3.50 | 5/6 = 0.83 |
| D | 1,1,2,2 | 4/6 = 0.67 | 3.00 | 3/6 = 0.50 |
| E | 1,2,3,3 | 4/9 = 0.44 | 2.17 | 0/6 = 0 |

A is near everyone (high closeness); D brokers access to E (high betweenness). Betweenness for A counts paths between B,C,D,E passing through A — not paths starting from A.

In the L04 workplace: Degree→Ana (most contacts), Closeness→Dia (bridge position), Betweenness→Dia+Fin (inter-team paths), Eigenvector→Ana/Ben (connected to dense neighbours).

## Common Pitfalls
- Confusing closeness with betweenness — one measures proximity, the other measures path control
- Forgetting that betweenness for a focal node still requires all-pairs shortest paths (Brandes)
- Assuming degree centrality is sufficient — it ignores indirect influence
- PageRank is cheatable (link farms); harmonic centrality is harder to game but more expensive

## Connections
- [[structural-holes-and-brokerage]] — brokerage is captured by betweenness centrality
- [[girvan-newman-algorithm]] — GN uses **edge** betweenness, derived from the same concept
- [[edge-betweenness]] — the edge-level extension of betweenness centrality
- [[network-science-l04]] — centrality is one half of L04 (nodes), community detection is the other (groups)
- [[network-science-l03]] — degree distribution connects to network topology
- [[degree-centrality]] — local exposure measure
- [[closeness-centrality]] — short-path access measure
- [[harmonic-centrality]] — robust reachability measure
- [[betweenness-centrality]] — path brokerage measure
- [[eigenvector-centrality]] — recursive prestige measure
- [[pagerank]] — random-walk prestige measure

## Open Questions
- How do centrality measures perform on dynamic/temporal networks?
- Can we combine multiple centrality measures into a unified ranking?
- How sensitive are centrality rankings to small changes in network structure?
