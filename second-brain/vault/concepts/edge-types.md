---
title: "Edge Types: Directed, Undirected, Weighted"
tags: [concept, network-science, semester-1, graph-theory]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [network-intro]
---

## One-line Summary
Edges can be undirected (symmetric), directed (asymmetric), and/or weighted (carrying numerical values) — the choice of edge type shapes what the network can model.

## Core Intuition
Not all relationships are the same. "Alice is friends with Bob" is symmetric — if Alice considers Bob a friend, the reverse is likely true too. But "Alice follows Bob on Twitter" is asymmetric — Bob might not follow back. And "Alice emails Bob 50 times a month" carries a strength that a simple binary edge misses. Choosing the right edge type is a modeling decision that determines what questions you can ask.

## Formal Definition / Statement
Let $G = (V, E)$.

**Undirected graph:** Edges are unordered pairs. $(u, v) = (v, u)$. Models symmetric relationships (friendship, co-authorship, road connections).

**Directed graph (digraph):** Edges are ordered pairs. $(u, v) \neq (v, u)$. Models asymmetric relationships (hyperlinks, "follows," email sender→receiver, financial lending).

**Weighted graph:** Each edge $e$ carries a numerical weight $w(e) \in \mathbb{R}$. Models strength, capacity, or frequency (email frequency, loan amount, distance).

Edges can combine properties: a network can be *directed and weighted* simultaneously.

## Key Properties
- **Undirected:** The adjacency matrix $A$ is symmetric ($A = A^T$). Each node's degree counts all incident edges.
- **Directed:** The adjacency matrix is generally asymmetric. Nodes have separate **in-degree** (edges arriving) and **out-degree** (edges leaving).
- **Weighted:** The adjacency matrix entries are real numbers (not just 0/1). Weight can represent strength, distance, cost, or frequency — interpretation depends on context.
- A **simple graph** has no self-loops and no multi-edges. Multi-graphs allow multiple edges between the same pair of nodes.

## Worked Example
Consider three people: Alice, Bob, Carol.
- **Undirected:** Alice—Bob, Bob—Carol (friendship: symmetric). Adjacency matrix is symmetric.
- **Directed:** Alice→Bob, Carol→Bob (Alice and Carol follow Bob, but Bob follows neither). Bob has in-degree 2, out-degree 0.
- **Weighted:** Alice→Bob (weight 5, meaning 5 emails/month), Carol→Bob (weight 1). Alice's connection to Bob is 5× stronger.

## Common Pitfalls
- **Assuming all networks are undirected.** Many real-world relationships are inherently asymmetric (hyperlinks, lending, influence).
- **Confusing weight with presence.** A weighted edge of 0.01 and no edge are different things — one is a weak connection, the other is no connection.
- **Forgetting that directed edges affect everything.** Paths, components, centrality — all behave differently in directed vs. undirected graphs.
- **Treating "social network" as always undirected.** Twitter (follows) is directed; Facebook (friends) is undirected — both are social networks.

## Connections
- [[network-intro]] — edge types are part of the basic network definition
- [[centrality]] — degree splits into in/out-degree in directed networks
- [[connected-component]] — strong vs. weak connectivity depends on directedness
- [[network-examples]] — different domains naturally produce different edge types

## Open Questions
- When is it appropriate to symmetrize a directed network (e.g., treat mutual follows as undirected)? 
	- You should symmetrize only if the underlying phenomenon is truly symmetric — i.e., the direction doesn't carry meaning for your question. If mutual edges already exist in the data and you only care about 'is there a relationship?' (not direction), then symmetrizing simplifies analysis. But this is a modeling choice that throws away information. For most social networks (Twitter follows, email), keeping direction is safer.
- How does weighting affect algorithmic analysis compared to binary edges? 
	- Weights change which algorithms work and what they compute:
	    - Shortest paths: BFS stops working; Dijkstra's algorithm is needed (assuming non-negative weights).
	    - Distance: Path length = sum of weights, not edge count.
	    - Centrality: Weighted measures (weighted degree, weighted betweenness) replace binary versions.
	    - Clustering: Weights affect density and community strength.
	    In your email example, the difference between b→a (5x) and b→c (1x) means a is a 5× stronger connection. Algorithms must incorporate this — treating them equally would hide important structure.
- How do we handle mixed networks where some edges are directed and others are not? 
	- Mixed directionality is rare in practice and requires explicit handling:
	    1. Convert to consistent form: Replace undirected edges with bidirectional directed pairs (u→v and v→u).
	    2. Then treat as pure directed graph: Apply directed-graph algorithms (strong/weak connectivity, BFS/DFS following arrow direction).
	    3. Track edge type: Keep metadata noting which edges were originally undirected for interpretation.
	    
	    Alternatively: keep directionality as an edge attribute and have algorithms check it per-edge. But this is more complex and rarely necessary.
