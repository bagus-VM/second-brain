---
title: "Exercise Sheet 4 — Centrality and Structural Roles"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| 4.A Centrality Measures | [[centrality-measures]] · [[structural-holes-and-brokerage]] |
| 4.B Structural Roles | [[structural-holes-and-brokerage]] · [[edge-betweenness]] · [[clustering-coefficient]] |

# Exercise Sheet 4 — Centrality and Structural Roles

## Exercises

### 4.A Centrality Measures

**Exercise 4.A.1: Centrality by Hand**

Consider the graph with nodes A, B, C, D, E, F and edges A–B, A–C, B–C, B–D, D–E, D–F, E–F.

1. Compute degree centrality C_d(v) = deg(v)/(|V|−1) for all nodes.
2. Identify the shortest paths between all node pairs. Which node lies on the most shortest paths between other nodes? (Compute betweenness centrality by inspection.)
3. Which node has the highest degree centrality? Which has the highest betweenness centrality? Are they the same node?
4. Interpret: what structural role does the node with the highest betweenness play in this network?

---

**Exercise 4.A.2: When Centrality Measures Disagree**

Using `nx.karate_club_graph()`:

1. Compute degree, betweenness, closeness, and eigenvector centrality for all nodes.
2. Find the top-3 nodes for each measure. Do the top lists overlap?
3. Plot four subplots, each showing the network with node sizes proportional to one centrality measure.
4. Find a node that ranks very differently across measures. What does this reveal about its structural position?

### 4.B Structural Roles

**Exercise 4.B.1: Embedded vs. Broker**

Consider a graph with two triangles {1, 2, 3} and {4, 5, 6} connected by edge 3–4, plus node 7 connected only to nodes 3 and 4.

1. Is node 1 embedded or a broker? What evidence supports your answer?
2. Is node 7 embedded or a broker? What is its clustering coefficient C_7?
3. If edge 3–4 is removed, what happens to node 7's structural role?
4. Burt (1992) argues brokers gain "information advantage." What unique information could node 7 access that nodes in {1, 2, 3} cannot?

---

**Exercise 4.B.2: Betweenness as a Proxy for Brokerage**

Using the two-triangle + node 7 graph from Exercise 4.B.1:

1. Build the graph in NetworkX. Compute betweenness centrality for all nodes.
2. Verify that node 7 has high betweenness despite C_7 = 1.
3. Explain the apparent contradiction: high clustering coefficient yet high betweenness.
4. On the karate club graph: find the 3 nodes with the highest betweenness but lowest clustering coefficient. What does this combination mean structurally?

---

## Solutions

### 4.A.1 — Centrality by Hand

> [!note]- Solution
> 1. Degree centrality (|V|−1 = 5):
>
> | Node | Degree | C_d |
> |---|---|---|
> | A | 2 | 2/5 |
> | B | 3 | 3/5 |
> | C | 2 | 2/5 |
> | D | 3 | 3/5 |
> | E | 2 | 2/5 |
> | F | 2 | 2/5 |
>
> 2. **Betweenness — by inspection:** The graph has two triangle-like clusters: {A, B, C} on the left and {D, E, F} on the right, joined by edge B–D. Every shortest path from any node in {A, C} to any node in {D, E, F} must pass through B then D. Both B and D have very high betweenness; D slightly higher because it is the unique gateway to E, F.
> 3. **Highest degree centrality:** B and D are tied at 3/5. **Highest betweenness:** D (and B close behind), but D edges to E and F which are a "terminal" cluster, making D the unique gateway.
> 4. **Structural role of D:** D is a broker or bridge node. It sits on the unique path connecting the left cluster {A, B, C} to the right cluster {D, E, F}. Removing D would disconnect those two groups. High betweenness with moderate degree is the signature of a structural bridge.

### 4.A.2 — When Centrality Measures Disagree

> [!note]- Solution
> **Leading hubs:** Nodes 0 and 33 lead in almost every measure — they are the faction leaders with high degree and influence.
>
> **Structural disagreement:** Node 32 often shows high betweenness relative to its degree because it acts as a bridge to node 33's faction. High eigenvector centrality in dense cores often pairs with low betweenness due to redundant paths.

### 4.B.1 — Embedded vs. Broker

> [!note]- Solution
> 1. **Node 1 — embedded:** Node 1 is surrounded by the closed triangle {1, 2, 3} where all edges exist. C_1 = 1. Node 1 cannot reach {4, 5, 6} without going through 3 (and then 4), so it has no direct brokerage opportunity.
> 2. **Node 7 — broker:** Node 7 connects to 3 and 4, which are the two bridge points. C_7 = 1 (the one possible edge between its two neighbours exists). Despite C_7 = 1, node 7 structurally straddles two groups.
> 3. **If 3–4 is removed:** C_7 = 0. Now node 7 becomes the only bridge between the two components. Its brokerage role becomes critical.
> 4. **Information advantage:** Node 7 can learn about jobs, ideas, and events in the {4, 5, 6} cluster that are invisible to {1, 2, 3} (and vice versa). This is Burt's "structural hole" argument.

### 4.B.2 — Betweenness as a Proxy for Brokerage

> [!note]- Solution
> **Metric contrast:** Clustering coefficient is a local density measure (neighbours connected?), while betweenness is a global routing measure (on shortest paths?).
>
> **Brokerage with high C:** Node 7 has C_7 = 1 because its two neighbours are tied, but it still has high betweenness because it provides an alternative path between two large clusters.
>
> **Pure bridges:** High betweenness with low clustering (like node 32 in the karate club) indicates a pure bridge connecting otherwise separate groups.


---

## Related Resources

### 📖 L04 — Communities and Graph Partitioning
- Lecture topic: [[network-science-l04]]

**Key concepts covered:**
- [[structural-holes-and-brokerage]]
- [[centrality-measures]]
- [[modularity]]
- [[community-detection-overview]]
- [[girvan-newman-algorithm]]
- [[louvain-algorithm]]
- [[leiden-algorithm]]
- [[hierarchical-clustering]]
- [[graph-partitioning-cut-spectral]]
- [[graph-partitioning]]
- [[zacharys-karate-club]]
- [[product-space-network]]
- [[modularity-resolution-limit]]
- [[edge-betweenness]]
- [[embedding-based-community-detection]]
