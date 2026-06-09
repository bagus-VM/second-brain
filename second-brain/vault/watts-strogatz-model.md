---
title: "Watts-Strogatz Model"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The Watts-Strogatz model (1998) resolves the clustering/path-length paradox: start with a regular lattice and rewire a small fraction of edges randomly to get a network with both high clustering and short paths.

## Core Intuition
Real social networks have two seemingly contradictory properties:
- **High clustering** ($C \sim 0.1\text{–}0.5$): your friends tend to know each other
- **Short paths** ($L \sim \log n$): you're only a few hops from anyone

A regular lattice has high clustering but long paths ($L \sim n/2k$). A [[random-graphs|random graph]] has short paths but low clustering ($C \sim k/n$). Neither captures reality.

Watts and Strogatz showed that adding just a *tiny* fraction of random long-range shortcuts to a regular lattice collapses the path length while barely affecting clustering. This is because $L(p)$ drops much faster than $C(p)$ as $p$ increases from 0.

## Formal Definition / Statement
**Watts-Strogatz model (1998):**
1. Start with a ring of $n$ nodes, each connected to its $k$ nearest neighbors ($k/2$ on each side)
2. For each edge, with probability $p$, rewire one endpoint to a uniformly random node (avoiding self-loops and duplicates)

The parameter $p \in [0, 1]$ controls the interpolation:

| $p$ | Clustering $C$ | Path length $L$ | Regime |
|---|---|---|---|
| $p = 0$ | High ($\sim 0.5$) | Long ($\sim n/2k$) | Regular lattice |
| $0 < p \ll 1$ | High | Short ($\sim \log n$) | **Small-world** |
| $p = 1$ | Low ($\sim k/n$) | Short ($\sim \log n / \log k$) | Random graph |

## Key Properties
- The small-world regime exists because $L(p)$ falls much faster than $C(p)$ as $p$ increases
- Even $p = 0.01$ (1% of edges rewired) is often enough to collapse $L$ to near-random-graph levels
- The model preserves the local lattice structure — most neighborhoods remain intact
- $C(p)$ is relatively insensitive to small $p$ because rewiring only affects the endpoints of rewired edges
- The model does NOT guarantee navigability — short paths exist but may not be findable with local information (see [[kleinberg-decentralized-search]])

## Worked Example
Regular lattice: $n = 1000$ nodes, $k = 10$ neighbors per node.

- Total edges: $nk/2 = 5000$
- At $p = 0$: $L \sim n/2k = 50$ (lattice scale), $C$ is high
- At $p = 0.01$: 50 edges rewired → 50 long-range shortcuts created
  - $L$ drops sharply (shortcuts jump across the lattice)
  - $C$ barely changes (only 50 of 5000 edges affected, most neighborhoods intact)
  - This is the small-world regime

## Common Pitfalls
- **"Just add random edges"** — The model specifically rewires *existing* edges, not adds new ones. The total edge count stays the same.
- **The model explains Milgram's experiment** — It explains why short paths *exist* (coexistence question), but NOT why people can *find* them. Watts-Strogatz uses uniform rewiring ($r = 0$ in Kleinberg's framework), which doesn't support efficient greedy routing.
- **Clustering and path length are always in tension** — The whole point is they're NOT: a small $p$ gives you both.
- **The model produces scale-free networks** — It does NOT. The degree distribution remains narrow (approximately $k$ for all nodes). See [[scale-free-networks]] and [[preferential-attachment]] for models that produce heavy-tailed degree.

## Connections
- [[small-world-property]] — The Watts-Strogatz model produces networks with this property
- [[milgrams-experiment-six-degrees]] — Resolves the coexistence question from Milgram's experiment
- [[kleinberg-decentralized-search]] — Shows that Watts-Strogatz's uniform rewiring is insufficient for navigability
- [[random-graphs]] — The $p = 1$ endpoint of the model; Erdős-Rényi graphs
- [[clustering-coefficient]] — The metric $C$ that stays high in the small-world regime
- [[scale-free-networks]] — A different family of network models (Watts-Strogatz is NOT scale-free)
- [[preferential-attachment]] — Barabási-Albert model, alternative to Watts-Strogatz

## Open Questions
- How does the small-world regime depend on the lattice dimension $d$?
- What happens when rewiring is not uniform but correlated with geography?
- Can the model be extended to produce heavy-tailed degree distributions while preserving the small-world property?
