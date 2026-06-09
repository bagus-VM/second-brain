---
title: "What Is a Network?"
tags: [concept, network-science, semester-1, foundations]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A network is a collection of ==entities (nodes)== and the ==relationships (edges)== between them — the fundamental abstraction for studying connected systems.

## Core Intuition
The world is full of systems where individual things matter less than how they connect. A network strips away everything except "who is connected to whom." This simple abstraction is powerful because the same math applies whether the nodes are people, web pages, banks, or cities. The pattern of connections creates structure that determines outcomes — information flow, vulnerability, influence — that you cannot see by studying any single entity alone.

## Formal Definition / Statement
A network (or graph) consists of:
- A set of **nodes** (vertices, entities): $V = \{v_1, v_2, \dots, v_n\}$
- A set of **edges** (links, relationships): $E \subseteq V \times V$

An edge $(u, v)$ represents a connection between node $u$ and node $v$. The entire structure is written as $G = (V, E)$.

**Key principle:** A network is always a *model* — an abstraction that intentionally leaves out details. The same real-world situation can be modeled as different networks depending on the question being asked.

## Key Properties
- Networks are **domain-general**: the same formalism covers social, biological, technical, and economic systems.
- Networks are **lossy abstractions**: by design, they omit details. This is a feature (focus on structure) and a limitation (context is lost).
- The **same relational setting** can yield different network models (e.g., affiliation networks vs. projected people networks).
- The structure of connections — not just the properties of individual nodes — determines system-level outcomes.

## Worked Example
**Zachary's Karate Club (1977):** 34 club members (nodes), friendships between them (edges). The club split into two factions after a dispute. The network structure — two dense clusters with a thin bridge — predicted the split. You could not predict this from knowing each member individually; only the pattern of friendships made it visible.

## Common Pitfalls
- **Thinking a network captures everything.** It doesn't. Choosing what counts as a node and what counts as an edge is a modeling decision that always loses information.
- **Confusing the map with the territory.** The network is a model of reality, not reality itself.
- **Assuming edges are always symmetric.** They can be directed (see [[edge-types]]).
- **One-mode thinking.** The same system might be better modeled as a bipartite network (e.g., people belonging to groups) rather than a simple one-mode graph.

## Connections
- [[edge-types]] — edges can be directed, undirected, weighted, or typed
- [[network-examples]] — real-world systems modeled as networks
- [[network-effects]] — why the structure of connections matters beyond individual properties
- [[community-structure]] — dense clusters within networks
- [[centrality]] — which nodes occupy important positions

## Open Questions
- What are good heuristics for deciding how to model a given real-world system as a network? 
	- Strip away everything except "who is connected to whom" — but choose your node and edge definitions based on the question you're asking, not as a default to be extended later.
- How do we know when a network model has left out something critical?
	- When the information you've stripped away is necessary to answer the question at hand. You know this has happened if your model's predictions fail or produce misleading conclusions
- When is a bipartite or multi-layer model preferable to a simple graph? when we want to know 
	- When the relational structure has two distinct types of entities (like people and groups, or authors and papers) — use bipartite if you want to preserve that two-type distinction and ask questions about both sides. Use projection if you only care about one side.
