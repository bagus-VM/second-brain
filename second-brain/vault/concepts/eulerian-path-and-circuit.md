---
title: "Eulerian Path and Circuit"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [paths-walks-and-cycles, graph-fundamentals]
---

## One-line Summary
==An Eulerian path traverses every edge exactly onc==e; an Eulerian circuit does so while returning to the start — existence depends purely on vertex degrees.

## Core Intuition
==The Königsberg bridges problem (1736) asked: can you walk through the city crossing each bridge exactly once? Euler proved it impossible== — and in doing so, founded graph theory. The answer depends entirely on the degrees of the nodes: ==if too many nodes have odd degree, no such path exists.==

## Formal Definition / Statement
- **Eulerian Path**: A walk traversing every edge exactly once. ==Exists iff exactly 0 or 2 vertices have odd degree.==
- **Eulerian Circuit**: ==An Eulerian path that starts and ends on the same vertex. Exists iff every vertex has even degree.==

**Intuitive proof**: Think of rooms with doors (=edges). If a room has an even number of doors, you can enter and leave it an equal number of times. If it has an odd number of doors, you must start or end in that room. With no odd-door rooms, you must start and end at the same room.

## Key Properties
- An Eulerian circuit is a special case of an Eulerian path (with 0 odd-degree vertices)
- The existence condition is purely about [[neighbourhood-and-degree|degree]], not about the graph's topology otherwise
- In Königsberg: all four land masses had odd degrees (3, 3, 3, 5), violating both conditions
- This is distinct from a Hamiltonian path (visits every **node** exactly once) — which is NP-hard to determine

## Worked Example
Königsberg bridges:
- 4 land masses (nodes), 7 bridges (edges)
- Degrees: 3, 3, 3, 5 (all odd)
- Eulerian path requires exactly 0 or 2 odd-degree vertices → impossible
- Eulerian circuit requires all even degrees → also impossible

A graph with degrees 2, 2, 2, 2: Eulerian circuit exists (all even).

A graph with degrees 3, 2, 2, 3: Eulerian path exists (exactly two odd-degree vertices — the endpoints).

## Common Pitfalls
- Confusing Eulerian paths with Hamiltonian paths — Eulerian visits every edge, Hamiltonian visits every node
- Forgetting that the condition is about odd-degree vertex **count**, not which specific vertices are odd
- Assuming a connected graph always has an Eulerian path — connectivity is necessary but not sufficient

## Connections
- [[neighbourhood-and-degree]] — existence depends on degree parity
- [[paths-walks-and-cycles]] — Eulerian paths are a special type of walk
- [[connectivity-and-components]] — the graph must be connected (ignoring isolated vertices) for Eulerian paths to exist
- [[graph-fundamentals]] — Euler's solution founded graph theory as a field

## Open Questions
- What is the computational complexity of finding an Eulerian path when one exists? (Answer: linear time via Hierholzer's algorithm)
- How does this relate to the Chinese Postman Problem (finding the shortest walk covering all edges)?
