---
title: "Connected Components"
tags: [concept, network-science, semester-1, graph-theory]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [network-intro, edge-types]
---

## One-line Summary
A connected component is a maximal set of nodes where every node can reach every other node via some path — the basic unit of network "togetherness."

## Core Intuition
If you pick any two people in a social network, can one reach the other through a chain of friendships? If yes, they're in the same connected component. If not, they belong to separate, isolated groups. Connected components tell you how many separate "islands" exist in a network. A network with one component is fully connected; a network with three components has three isolated sub-networks.

This matters practically: if a rumor starts in component A, it can never reach component B. If a financial institution in one component defaults, institutions in other components are safe.

## Formal Definition / Statement
Let $G = (V, E)$ be an undirected graph.

A **path** from node $u$ to node $v$ is a sequence of edges connecting them:
$$u = v_0, v_1, v_2, \dots, v_k = v \quad \text{where } (v_{i}, v_{i+1}) \in E$$

A **connected component** of $G$ is a maximal subset $C \subseteq V$ such that for every pair $u, v \in C$, there exists a path from $u$ to $v$ in $G$.

**For directed graphs**, we distinguish:
- **Weakly connected component:** connected if we ignore edge directions
- **Strongly connected component:** every node can reach every other node *following edge directions*

A graph is **connected** if it has exactly one connected component.

## Key Properties
- Every node belongs to exactly one connected component (they partition the node set).
- The number of components is a basic structural descriptor of a network.
- In random graphs, the transition from many small components to one giant component is a phase transition — a key result in [[network-intro]].
- Removing nodes or edges can *split* a component into two (related to network robustness).
- Real-world networks often have one **giant component** containing most nodes, plus many tiny isolated fragments.

## Worked Example
Consider a network with 9 nodes:
```
Component 1: A—B—C, B—D        (A, B, C, D are all reachable from each other)
Component 2: E—F               (E and F are connected to each other only)
Component 3: G, H, I           (three isolated nodes, each a component of size 1)
```
==This network has 5 connected components: {A,B,C,D}, {E,F}, {G}, {H}, {I}. A rumor starting at A can reach B, C, and D — but never E, F, G, H, or I.==

## Common Pitfalls
- **Confusing connected with "close together."** Nodes in the same component might be very far apart (many hops). Being connected just means *some* path exists.
- **Forgetting that directed graphs need "strongly connected."** In a directed graph, A→B→C doesn't mean C can reach A. Strong connectivity requires paths in *both* directions.
- **Assuming one component means robust.** A graph can be connected but have "bottleneck" edges whose removal splits it (related to [[centrality]] — betweenness).

## Connections
- [[network-intro]] — components are a fundamental structural property of networks
- [[edge-types]] — directed vs. undirected changes how components are defined
- [[community-structure]] — components are the coarsest form of grouping; communities are finer
- [[network-diffusion]] — diffusion can only occur within a component
- [[network-effects]] — disconnected components can't influence each other

## Open Questions
- How does the size distribution of components characterize a network's structure?
- What happens to components when nodes or edges are removed (robustness)?
- How do components evolve in dynamic (time-varying) networks?
