---
title: "Mining Software Repositories — Lecture 4 Overview (Developer Social Networks)"
tags: [topic, mining-software-repositories, semester-2, social-networks]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 4 turns software development into a graph: it fixes the graph vocabulary, then asks the
two questions every network definition must answer — what the nodes are and what the edges mean —
before defining the measures later chapters use to quantify centrality and cohesion.

## Core Map

```
Chapter 4 — Developer Social Networks
│
├── Social networks
│   ├── Merriam-Webster: network of individuals connected by relationships
│   ├── Research questions: who works together, which teams, how they form/evolve
│   └── Forge features as social features, but mostly exploited as data
│
├── Graphs
│   ├── G = (V, E), E subset of V x V; directed vs undirected
│   ├── Paths, path length d(u,v), connectedness
│   ├── Degree, in-degree, out-degree
│   └── Communities and partitions
│       ├── Clusters with many internal, few external connections
│       ├── No fixed definition; detection via components or clustering coefficient
│       └── P = {p1..pk} partitioning of G -> [[community-structure]]
│
├── Developer social networks
│   ├── Purely social (developers as nodes)
│   ├── Technical (artifacts as nodes: dependency and co-change graphs)
│   └── Socio-technical (both)
│
├── Defining networks for research
│   ├── Two questions: what are the nodes, what are the edges?
│   ├── Direct vs indirect modelling (who talked to whom is rarely observable)
│   ├── Node types: external (type_V) vs positional (type_V,loc)
│   ├── Edge types: type_E, single vs multiple types per edge
│
└── Network metrics
    ├── Size: |V|, |E|, number of components
    ├── Centrality
    │   ├── Degree centrality C_degree(v) = d(v), normalized per graph
    │   │       -> [[degree-centrality]]
    │   ├── Closeness centrality C_closeness(v) = (V-1) / sum d(u,v)
    │   │       -> [[closeness-centrality]]
    │   └── Betweenness centrality C_between(v) = sum sigma_st(v)/sigma_st
    │           -> [[betweenness-centrality]]
    └── Clustering coefficient C_clust(v), averaged per graph
            -> [[clustering-coefficient]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[developer-social-networks]] | Modelling developers, artefacts, or both as nodes, and choosing what an edge means |
| [[community-structure]] | Communities are clusters with many internal and few external edges; a partition covers the graph |
| [[degree-centrality]] | Centrality by connection count, with a per-graph normalization against the star graph |
| [[closeness-centrality]] | Centrality by inverse total shortest-path distance to all other nodes |
| [[betweenness-centrality]] | Centrality by the share of shortest paths that pass through a node |
| [[clustering-coefficient]] | How densely connected a node's neighbourhood is, relative to a clique |

## Lecture Structure

1. **Social networks** — the two-part Merriam-Webster definition, the research questions the
   field asks (who works together, which teams exist, how they form and evolve, what a
   developer's role is), and a note that forges have social features usually mined.
2. **Graphs** — the formal definition, directed versus undirected edges, the convention that
   undirected graphs are treated as directed pairs, paths and path length, connectedness,
   degree and in-/out-degree, components, induced subgraphs.
3. **Communities and partitions** — the definition, the absence of a fixed threshold for internal
   versus external connections, the family of detection algorithms, and the partition conditions:
   disjoint node sets, induced edges, full coverage of V.
4. **Three kinds of developer network** — purely social (developers as nodes, edges are
   communication interpreted broadly), technical (artefacts as nodes: dependency and co-change
   graphs), and socio-technical (both in one graph).
5. **Defining networks for research** — the two questions (nodes, edges) and the mirror of the
   direct/indirect measurement distinction from the enrichment chapter.
6. **Node and edge types** — external node types via `type_V`, positional types via
   `type_V,loc` reflecting importance; edge types via `type_E`, the two general cases, and the
   advice to use separate untyped graphs when there are several types.
7. **Weights** — node and edge weight functions, visual encoding through node size and edge
   thickness, and the recommendation to use multiple graphs rather than a joint weight/type
   function.
8. **Network metrics** — size and component counts, the three centralities with their formulas,
   the clustering coefficient and its per-graph average.

## Exam-Relevant Points

1. **Every network definition needs two answers**: what the nodes are and what the edges
   represent. Neither is automatic.
2. **Direction carries information.** An undirected issue-comment graph tells you who interacted;
   the directed version tells you the order, hence the flow of knowledge.
3. **Undirected graphs are directed graphs in disguise** — adding both (u,v) and (v,u) — which is
   why the notation convention in the slides is safe.
4. **Community detection has no fixed threshold.** The slides state this explicitly and decline
   to discuss the algorithms in detail.
5. **There are three network flavours, and choosing one is a modelling decision.**
6. **Positional node types are a function of the graph itself** (high degree equals importance),
   while external types come from outside the network.
7. **Weights and types do not mix well.** The recommended modelling for multiple edge types is
   multiple untyped graphs.
8. **Degree centrality normalized per graph divides by the largest attainable value**, which the
   star graph attains — the maximum degree is |V| − 1.
9. **The clustering coefficient's denominator is the number of edges a clique on the
   neighbourhood would have**, and the directed version differs by a factor of two from the
   undirected one.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-5]] — the next chapter, which uses these graphs for
  community smells and congruence.
- [[mining-software-repositories-lecture-3]] — where the direct/indirect distinction is
  introduced.
- [[developer-social-networks]] — the concept page for the modelling choices.
- [[community-structure]] — communities and partitions.
- [[degree-centrality]] — connection-count centrality.
- [[closeness-centrality]] — distance-based centrality.
- [[betweenness-centrality]] — brokerage centrality.
- [[clustering-coefficient]] — neighbourhood density.
- [[temporal-networks]] — the graph notions here extended over time, needed for black clouds.

## Open Questions

- **Community detection algorithms are deliberately not discussed** ("We do not discuss this in
  detail in this lecture"), so the community definition used later is left undecided.
- **No worked numbers appear** — the chapter gives formulas but no example graph with computed
  metric values.
- **The choice between an issue-comment graph and a co-change graph is not discussed** as a
  trade-off; both appear as examples.
- **Identity resolution is assumed, not solved** — the node is "a developer", but nothing says
  how a person across tools becomes one node.
- **The centrality definitions given are the textbook ones**; other measures exist "e.g., based
  on the eigenvectors of the adjacency matrix" without naming any.
