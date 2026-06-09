---
title: "Directed and Undirected Graphs"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals]
---

## One-line Summary
Undirected graphs model symmetric relationships (friendship), while directed graphs model asymmetric ones (following, citing).

## Core Intuition
The same set of nodes can yield very different models depending on whether edges have direction. Friendship is symmetric — if A is friends with B, then B is friends with A. But "A follows B" on Twitter does not imply "B follows A." The choice of directed vs. undirected is a fundamental modeling decision.

## Formal Definition / Statement
- **Undirected graph**: An edge {u, v} connects two vertices without orientation. {u, v} = {v, u}. Source and target are not distinguished.
- **Directed graph (digraph)**: An edge (u, v) ∈ E has strict orientation from u to v. (u, v) does **not** imply (v, u).

## Key Properties
- In undirected graphs, edges have no arrows; the relation is symmetric
- In directed graphs, edges have arrows indicating direction
- The [[neighbourhood-and-degree|degree]] splits into **in-degree** and **out-degree** for directed graphs
- [[shortest-path-and-diameter|Distance]] is not symmetric in directed graphs: dist(u,v) ≠ dist(v,u) in general
- [[connectivity-and-components|Connectivity]] becomes more nuanced: [[directed-connectivity|strongly vs. weakly connected]]
- [[breadth-first-search|BFS]] works identically on directed graphs — it just follows edge direction

## Worked Example
Email network:
- Nodes: email addresses
- Edges: directed (sender → receiver)
- A sends email to B does not mean B sends email to A
- This asymmetry matters for influence analysis, spam detection, etc.

Contrast with co-authorship:
- Nodes: researchers
- Edges: undirected (both contributed to the same paper)
- If A co-authored with B, then B co-authored with A

## Common Pitfalls
- Treating a directed graph as undirected loses information about asymmetry
- Treating an undirected graph as directed doubles the edges unnecessarily
- Forgetting that dist(u,v) ≠ dist(v,u) in directed graphs affects [[shortest-path-and-diameter|shortest path]] algorithms

## Connections
- [[graph-fundamentals]] — the basic graph definition
- [[weighted-graphs]] — combining direction with weights
- [[directed-connectivity]] — strong vs. weak connectivity
- [[neighbourhood-and-degree]] — in-degree and out-degree
- [[graph-representations]] — adjacency matrix is not symmetric for directed graphs

## Open Questions
- When should a seemingly symmetric relationship be modeled as directed (e.g., mutual vs. non-mutual friendship)?
- How does directionality affect the emergence of [[directed-connectivity|giant components]]?
