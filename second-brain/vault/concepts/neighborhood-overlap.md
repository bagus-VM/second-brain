---
title: "Neighborhood Overlap"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-fundamentals]]"]
---

## One-line Summary
Neighbourhood overlap measures the fraction of neighbours shared by two connected nodes — an edge-level proxy for how embedded or bridging that edge is.

## Core Intuition
An edge connecting two people with many shared friends is deeply embedded in a cluster. An edge connecting two people with *no* shared friends is a [[bridges-and-local-bridges|local bridge]] — it spans between otherwise disconnected groups. Neighbourhood overlap quantifies this distinction, giving us an edge-level measure that complements the node-level [[clustering-coefficient]]. Under [[weak-ties-hypothesis|the weak-tie theorem]], low overlap predicts weak ties.

## Formal Definition / Statement
**Neighbourhood overlap.** For an edge (u, v):

```
O(u, v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)|
```

where N(u) and N(v) are the neighbour sets of u and v, *excluding each other*.

**Range:** O(u, v) ∈ [0, 1]
- O = 0: u and v share no neighbours — the edge is a pure local bridge
- O = 1: u and v have identical neighbour sets — edge inside a complete clique

This is the **Jaccard similarity** of the two neighbour sets.

## Key Properties / Complexity
- Scope: per-edge measure
- Complexity: O(k) per edge (set intersection of neighbour lists)
- O(u, v) = 0 ↔ edge is a [[bridges-and-local-bridges|local bridge]]
- Monotonically correlated with tie strength in empirical data (Onnela et al. 2007)
- Serves as the measurable proxy for the weak-tie theorem

## Worked Example
From Onnela et al. (2007) cell-phone study:
- Edges binned by call-duration percentile (tie-strength proxy)
- Mean overlap computed per bin
- Result: clear monotone relationship — weakest ties cluster near O ≈ 0, strongest at high O
- This confirms the [[weak-ties-hypothesis|weak-tie theorem]] prediction: low-overlap edges are weak

**Workplace scenario (from lecture):** The Dia–Fin edge connects two separate teams. N(Dia) and N(Fin) share no common members → O(Dia, Fin) = 0 → local bridge → must be weak under STC.

## Common Pitfalls
- Confusing overlap with clustering coefficient — C is per-node, O is per-edge
- Forgetting to exclude u and v from each other's neighbour sets
- Assuming O = 0 means the edge is unimportant — it's structurally the *most* important (carries novel information)
- Thinking overlap directly measures tie strength — it's a proxy, tested empirically

## Connections
- Edge-level complement of: [[clustering-coefficient]] (node-level)
- Detects: [[bridges-and-local-bridges]] (O = 0 ↔ local bridge)
- Proxies for: [[weak-ties-hypothesis]] (low O → weak tie predicted)
- Empirically validated by: Onnela et al. (2007) cell-phone network
- Motivated by: [[maxstc-complexity]] (exact labeling intractable)
- Part of: [[network-science-l03]]

## Open Questions
- How does overlap behave in directed or weighted networks?
- Is there a threshold on O that reliably separates strong from weak ties?
- How do temporal dynamics (tie decay) affect overlap over time?
