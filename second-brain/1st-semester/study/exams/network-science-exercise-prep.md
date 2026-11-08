---
title: "Network Science Exam — Exercise-Based Prep"
tags: [exam-prep, network-science, networkx, calculations, semester-1]
course: "Network Science"
status: current
last_updated: 2026-06-16
prerequisites: []
---

## Exam Intel

**Exam leans heavily on:** Exercise sheets, NetworkX code implementation, and calculations from exercises.

This is the same pattern as MMDB — the exercises ARE the exam prep. Every calculation you did by hand, every NetworkX function you called, every formula you applied — that's fair game.

---

## Key NetworkX Functions — Know These Cold

### Graph Creation and Manipulation
```python
G = nx.Graph()                          # Undirected
G = nx.DiGraph()                        # Directed
G.add_node(n)                           # Add single node
G.add_nodes_from([n1, n2, n3])          # Add multiple nodes
G.add_edge(u, v)                        # Add single edge
G.add_edges_from([(u1,v1), (u2,v2)])    # Add multiple edges
G.remove_edge(u, v)                     # Remove edge
G.number_of_nodes()                     # |V|
G.number_of_edges()                     # |E|
```

### Graph Properties
```python
nx.density(G)                           # Edge density: 2|E| / (|V|(|V|-1))
nx.degree(G)                            # Iterator of (node, degree) pairs
nx.is_connected(G)                      # True if connected
nx.connected_components(G)              # Iterator of component node sets
nx.shortest_path_length(G, source, target)  # Hop count
nx.average_shortest_path_length(G)      # Average over all pairs
```

### Centrality Measures
```python
nx.degree_centrality(G)                 # deg(v) / (n-1)
nx.betweenness_centrality(G)            # Fraction of shortest paths through v
nx.closeness_centrality(G)              # 1 / avg distance to all others
nx.pagerank(G, alpha=0.85)              # PageRank scores
nx.eigenvector_centrality(G)            # Eigenvector centrality
```

### Community Detection
```python
nx.community.greedy_modularity_communities(G)  # Greedy modularity maximization
nx.community.modularity(G, communities)        # Compute modularity Q
nx.community.girvan_newman(G)                  # Iterator of partitions
nx.community.edge_betweenness_centrality(G)    # Edge betweenness
```

### Clustering and Triads
```python
nx.clustering(G)                        # Local clustering coefficient per node
nx.average_clustering(G)                # Average clustering coefficient
nx.transitivity(G)                      # Global transitivity (3×triangles / triads)
nx.triangles(G)                         # Number of triangles per node
```

### Special Graphs
```python
nx.karate_club_graph()                  # Zachary's karate club (34 nodes, 78 edges)
nx.complete_graph(n)                    # K_n (all possible edges)
nx.path_graph(n)                        # P_n (linear chain)
nx.cycle_graph(n)                       # C_n (ring)
nx.wheel_graph(n)                       # W_n (cycle + central hub)
nx.star_graph(n)                        # Star topology
nx.erdos_renyi_graph(n, p)              # Random graph G(n,p)
nx.barabasi_albert_graph(n, m)          # Preferential attachment
```

### Matrix Representations
```python
nx.to_numpy_array(G)                    # Adjacency matrix as numpy array
nx.to_scipy_sparse_array(G)             # Sparse adjacency matrix
nx.adjacency_matrix(G)                  # Sparse matrix (deprecated, use above)
```

---

## Key Calculations — Hand-Trace These

### 1. Degree and Handshaking Lemma
**Formula:** Σ deg(v) = 2|E|

**Example:** Graph with edges A–B, A–C, B–C, B–D, D–E
- deg(A) = 2, deg(B) = 3, deg(C) = 2, deg(D) = 2, deg(E) = 1
- Sum = 2+3+2+2+1 = 10 = 2×5 ✓

### 2. Density
**Formula (undirected):** density = 2|E| / (|V|(|V|-1))

**Example:** |V|=5, |E|=5 → density = 10 / (5×4) = 10/20 = 0.5

### 3. Clustering Coefficient
**Local C_v:** C_v = 2×(triangles through v) / (deg(v) × (deg(v)-1))

**Example:** Node B with deg=3, connected to A, C, D. If A–C exists but A–D and C–D don't:
- Triangles through B: 1 (A–B–C)
- C_B = 2×1 / (3×2) = 2/6 = 0.33

**Average C̄:** C̄ = (1/n) Σ C_v

### 4. Modularity Q
**Formula:** Q = (1/2m) Σ_c [e_c − a²_c / 4m]

where:
- m = total edges
- e_c = edges inside community c
- a_c = sum of degrees in community c

**Example (from e05):** Two communities {A,B,C} and {D,E,F}, m=7
- Community 1: e₁=3, a₁=7 → expected = 49/28 = 1.75
- Community 2: e₂=3, a₂=7 → expected = 49/28 = 1.75
- Q = (1/14) × [(3−1.75) + (3−1.75)] = 2.5/14 ≈ 0.18

### 5. Edge Betweenness
**Definition:** Fraction of all shortest paths that pass through edge e.

**Example:** Two triangles {1,2,3} and {4,5,6} connected by bridge 3–4
- Edge 3–4 lies on all 3×3=9 paths between the two triangles
- Betweenness of 3–4 = 9 (unnormalized)
- Intra-triangle edges have much lower betweenness

### 6. Neighborhood Overlap
**Formula:** O(u,v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)| (excluding u and v from N)

**Example:** A–B edge, N(A)={C,D}, N(B)={C,E}
- N(A) ∩ N(B) = {C} → |intersection| = 1
- N(A) ∪ N(B) = {C,D,E} → |union| = 3
- O(A,B) = 1/3 ≈ 0.33

### 7. Path Length and Diameter
**Shortest path:** Use BFS for unweighted graphs
**Diameter:** max over all pairs of shortest path length
**Average path length:** (1/n(n-1)) Σ d(u,v)

---

## Exercise Sheets — Study Priority

### High Priority (Calculations + Code)
- **e02 (Graph Theory):** Adjacency matrices, degree sequences, density, NetworkX basics
- **e03 (Strong/Weak Ties):** Clustering coefficient, neighborhood overlap, bridges
- **e05 (Community Detection):** Modularity calculation, Girvan-Newman, hierarchical clustering

### Medium Priority (Conceptual + Some Code)
- **e04 (Centrality):** Degree/betweenness/closeness centrality, PageRank
- **e06 (Diffusion):** SIR model, cascades, threshold models

### Lower Priority (Mostly Conceptual)
- **e01 (What Is a Network?):** Modeling questions, network types
- **e07 (Network Science in Practice):** Case studies, real-world examples

---

## Practice Questions — Answer These

### NetworkX Code
1. "Write NetworkX code to build a graph with 5 nodes and edges A–B, A–C, B–C, B–D, D–E. Print the adjacency matrix."
2. "Use NetworkX to compute the clustering coefficient of each node in the karate club graph. What's the average?"
3. "Apply greedy modularity communities to the karate club. How many communities does it find? What's the modularity score?"
4. "Use Girvan-Newman to partition the karate club into 2 communities. Compare to the known factions."

### Hand Calculations
1. "Compute the degree sequence of this graph. Verify the handshaking lemma."
2. "Compute the local clustering coefficient of node B (deg=3, one triangle). What does it mean?"
3. "Compute modularity Q for this 2-community partition. Show your work."
4. "Which edge has the highest betweenness in this two-triangle graph? Why?"
5. "Compute neighborhood overlap for edge A–B. Is it a local bridge?"

### Conceptual
1. "What does Q=0 mean? What does Q=1 mean? What range is typical for real networks?"
2. "Why does Girvan-Newman remove the bridge edge first?"
3. "What's the difference between degree centrality and eigenvector centrality?"
4. "Why do weak ties matter for finding jobs? (Granovetter's theorem)"
5. "What's the resolution limit of modularity? Why does it over-partition?"

---

## Common Pitfalls

1. **Confusing directed vs undirected density.** Undirected: 2|E|/(n(n-1)). Directed: |E|/(n(n-1)).

2. **Forgetting the +1 in clustering coefficient.** C_v = 2T / (k(k-1)), not 2T / k².

3. **Miscounting triangles.** A triangle is a set of 3 mutually connected nodes. Count each triangle once, not 3 times.

4. **Confusing edge betweenness with node betweenness.** Edge betweenness counts paths through an edge. Node betweenness counts paths through a node.

5. **Forgetting to exclude u and v from neighborhoods in overlap calculation.** O(u,v) = |N(u) ∩ N(v)| / |N(u) ∪ N(v)| where N(u) excludes u and v.

6. **Modularity expected value formula.** It's a²_c / (4m), not a_c² / (2m). The 4m comes from the configuration model.

7. **Girvan-Newman doesn't recompute betweenness after each removal in the basic version.** You remove the highest-betweenness edge, then recompute. The algorithm is iterative.

---

## Connections

- [[network-science-l01]] through [[network-science-l09]] — Lecture notes
- [[network-science-e01]] through [[network-science-e07]] — Exercise sheets with solutions
- [[network-science-e01-flashcards]] through [[network-science-e07-flashcards]] — Flashcards

---

## Open Questions

- Are there any NetworkX functions from the exercises that aren't listed here?
- What other calculations might appear? (e.g., assortativity, degree correlation)
- Will the exam provide NetworkX documentation, or do you need to memorize function signatures?


---

## Related Resources

### 📖 Network Science L01: Introduction — Topic Overview
- Lecture topic: [[network-science-l01]]

**Key concepts covered:**
- [[network-intro]]
- [[network-examples]]
- [[edge-types]]
- [[centrality]]
- [[community-structure]]
- [[connected-component]]
- [[network-effects]]
- [[network-diffusion]]

### 📖 Network Science L02 — Graph Theory
- Lecture topic: [[network-science-l02]]

**Key concepts covered:**
- [[graph-fundamentals]]
- [[directed-and-undirected-graphs]]
- [[weighted-graphs]]
- [[graph-representations]]
- [[neighbourhood-and-degree]]
- [[paths-walks-and-cycles]]
- [[connectivity-and-components]]
- [[bipartite-graphs]]
- [[eulerian-path-and-circuit]]
- [[breadth-first-search]]
- [[depth-first-search]]
- [[dijkstras-algorithm]]
- [[shortest-path-and-diameter]]
- [[sparse-dense-and-random-graphs]]
- [[directed-connectivity]]

### 📖 Network Science L03 — Strong and Weak Ties
- Lecture topic: [[network-science-l03]]

**Key concepts covered:**
- [[triadic-closure]]
- [[clustering-coefficient]]
- [[strong-triadic-closure]]
- [[bridges-and-local-bridges]]
- [[neighborhood-overlap]]
- [[weak-ties-hypothesis]]
- [[social-capital]]
- [[structural-holes]]
- [[maxstc-complexity]]
- [[graph-fundamentals]]

### 📖 Network Science L04 — Communities and Graph Partitioning
- Lecture topic: [[network-science-l04]]

**Key concepts covered:**
- [[community-detection-overview]]
- [[modularity]]
- [[louvain-algorithm]]
- [[leiden-algorithm]]
- [[girvan-newman-algorithm]]
- [[edge-betweenness]]
- [[graph-partitioning]]
- [[graph-partitioning-cut-spectral]]
- [[hierarchical-clustering]]
- [[modularity-resolution-limit]]
- [[zacharys-karate-club]]
- [[centrality-measures]]
- [[embedding-based-community-detection]]
- [[structural-holes-and-brokerage]]
- [[product-space-network]]

### 📖 Network Science L05: Social Context and Link Formation
- Lecture topic: [[network-science-l05]]

**Key concepts covered:**
- [[homophily]]
- [[selection-vs-socialization]]
- [[affiliation-networks]]
- [[network-autocorrelation]]
- [[schelling-segregation-model]]
- [[echo-chambers]]
- [[modularity]]

### 📖 Network Science L06: Structural Balance
- Lecture topic: [[network-science-l06]]

**Key concepts covered:**
- [[structural-balance-theory]]
- [[balanced-triads]]
- [[balance-theorem]]
- [[weak-structural-balance]]
- [[signed-graphs]]
- [[frustration-index]]
- [[cycle-criterion]]
- [[k-balance]]
- [[algebraic-connectivity]]
- [[signed-laplacian]]

### 📖 Network Science L07 — Small-World Networks
- Lecture topic: [[network-science-l07]]

**Key concepts covered:**
- [[small-world-property]]
- [[watts-strogatz-model]]
- [[milgrams-experiment-six-degrees]]
- [[kleinberg-decentralized-search]]
- [[random-graphs]]
- [[scale-free-networks]]
- [[preferential-attachment]]
- [[power-law-distribution]]
- [[web-bow-tie-structure]]

### 📖 Network Science L08: Network Dynamics
- Lecture topic: [[network-science-l08]]

**Key concepts covered:**
- [[simple-contagion]]
- [[sir-model-network-epidemics]]
- [[basic-reproduction-number-r0]]
- [[scale-free-epidemic-threshold-vanishes]]
- [[complex-contagion]]
- [[threshold-cascades]]
- [[weak-tie-paradox-contagion]]
- [[centola-2010-experiment]]
- [[temporal-networks]]
- [[process-structure-interaction-gap]]
- [[diffusion-of-innovations]]
- [[weak-ties-hypothesis]]
