---
title: "Directed Connectivity"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [connectivity-and-components, directed-and-undirected-graphs]
---

## One-line Summary
In directed graphs, strong connectivity requires mutual reachability between all node pairs, while weak connectivity only requires connectivity when edge directions are ignored.

## Core Intuition
In undirected graphs, "connected" is straightforward. But in directed graphs, A can reach B without B being able to reach A. This creates two notions: **strong** (mutual reachability) and **weak** (connected if you ignore direction). The Web is the classic example: the strongly connected core (SCC) is much smaller than the weakly connected whole, forming a "bow tie" structure.

## Formal Definition / Statement
- **Strongly connected**: For every pair u, v ∈ V there is a directed path from u to v **and** from v to u.
- **Weakly connected**: The graph is connected when all directed edges are replaced with undirected edges.
- **Strongly connected component (SCC)**: A maximal subgraph where every node can reach every other node via directed paths.
- **Web bow tie structure** (Broder et al., 2000):
  - **SCC**: pages mutually reachable by directed paths
  - **IN**: pages that can reach the SCC but are not reachable from it
  - **OUT**: pages reachable from the SCC but unable to link back
  - **Tendrils/tubes**: side regions attached to IN or OUT

## Key Properties
- Every strongly connected graph is also weakly connected, but not vice versa
- Strongly connected components partition the node set (like undirected components)
- The SCC is often much smaller than the weakly connected component
- The Web's bow tie structure shows that most pages are NOT in the SCC
- Algorithm: Tarjan's algorithm finds all SCCs in O(|V|+|E|)

## Worked Example
Web graph (Broder et al., 2000):
- The Web decomposes into SCC, IN, OUT, tendrils, and tubes
- The SCC contains roughly 28% of pages
- IN contains pages that can reach the core but can't be reached back
- OUT contains pages reachable from the core but that can't link back
- This structure explains why "the Web is connected" is misleading — weak connectivity hides deep directional asymmetry

## Common Pitfalls
- Treating a weakly connected directed graph as "fully connected" — many node pairs may not be mutually reachable
- Confusing SCCs with undirected connected components — SCCs are much more restrictive
- Forgetting that [[connectivity-and-components|component detection]] with BFS on directed graphs finds WCCs, not SCCs

## Connections
- [[connectivity-and-components]] — directed connectivity is a refinement of the undirected notion
- [[directed-and-undirected-graphs]] — directionality creates the strong/weak distinction
- [[breadth-first-search]] — BFS on directed graphs follows edge direction
- [[depth-first-search]] — DFS is used in Tarjan's SCC algorithm

## Open Questions
- How does the bow tie structure of the Web affect search engine crawling strategies?
- How do strongly connected components relate to information flow and influence in directed networks?
