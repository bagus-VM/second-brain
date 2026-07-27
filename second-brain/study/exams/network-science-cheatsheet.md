---
title: "Network Science — Exam Cheatsheet"
tags: [network-science, exam, cheatsheet, semester-1]
course: "Network Science"
status: current
last_updated: 2026-07-27
---

# Network Science — Exam Cheatsheet

All formulas written out with full variable names for quick recall.

---

## 1. GRAPH FUNDAMENTALS

### Core Definitions
| Term | Definition |
|------|-----------|
| **Graph** | G = (V, E) where V = set of nodes/vertices, E = set of edges/links |
| **Undirected edge** | {u, v} — symmetric, no direction |
| **Directed edge** | (u, v) — asymmetric, u → v |
| **Simple graph** | No self-loops, no multi-edges |
| **Weighted graph** | G = (V, E, w) where w: E → ℝ assigns a weight to each edge |

### Degree
| Formula | Plain English |
|---------|--------------|
| deg(v) = \|N(v)\| | Degree of node v = number of neighbors of v |
| Σ deg(v) = 2\|E\| | **Handshaking Lemma** — sum of all degrees = twice the number of edges |
| Average degree = 2\|E\| / \|V\| | Average degree = twice the edges divided by the number of nodes |
| In-degree(v) = \|{u : (u,v) ∈ E}\| | Number of edges pointing TO v (directed graphs) |
| Out-degree(v) = \|{u : (v,u) ∈ E}\| | Number of edges pointing FROM v (directed graphs) |

### Density
| Formula | Plain English |
|---------|--------------|
| density = 2\|E\| / (\|V\|(\|V\| − 1)) | Actual edges / possible edges for undirected simple graph |
| density = \|E\| / (\|V\|(\|V\| − 1)) | For directed graphs (no factor of 2) |
| density = 1 → complete graph | Every possible edge present |
| density = 0 → no edges | Isolated nodes only |

### Neighbourhood
| Term | Definition |
|------|-----------|
| N(v) = {u ∈ V : {u, v} ∈ E} | The set of all nodes directly connected to v |
| Bipartite graph | G = (U, V, E) — edges only between U and V, never within U or within V |

### Walk, Path, Cycle Hierarchy
| Term | Definition |
|------|-----------|
| **Walk** | Any sequence of nodes connected by edges (nodes and edges may repeat) |
| **Path** | Walk with no repeated nodes (edges also don't repeat) |
| **Cycle** | Path that returns to its starting node (no repeated nodes except start = end) |
| **Trail** | Walk with no repeated edges (nodes may repeat) |

### Eulerian Conditions
| Condition | Meaning |
|-----------|---------|
| Eulerian **circuit** exists ⟺ every vertex has **even** degree | Traverse every edge exactly once and return to start |
| Eulerian **path** exists ⟺ exactly **0 or 2** vertices have odd degree | Traverse every edge exactly once (circuit if 0 odd, path if 2 odd) |
| Königsberg: all 4 vertices odd → no Eulerian path or circuit | |

---

## 2. PATHS, DISTANCE, AND CONNECTIVITY

| Formula | Plain English |
|---------|--------------|
| dist(u, v) = min{k : path of length k from u to v} | Shortest path distance = minimum number of edges between u and v |
| dist(u, v) = ∞ if no path exists | Unreachable nodes have infinite distance |
| diam(G) = max_{u,v ∈ V} dist(u, v) | **Diameter** = the longest shortest path in the entire graph |
| d̄ = (1 / \|V\|(\|V\|-1)) Σ_{u≠v} d(u, v) | **Average shortest-path distance** = mean of all pairwise distances |
| ecc(v) = max_{u ∈ V} d(v, u) | **Eccentricity** of v = distance to the farthest node from v |
| radius = min_{v ∈ V} ecc(v) | **Radius** = minimum eccentricity (the "most central" node's farthest distance) |
| diameter = max_{v ∈ V} ecc(v) | **Diameter** = maximum eccentricity = longest shortest path |
| centre = {v : ecc(v) = radius} | **Centre** = nodes whose eccentricity equals the radius |

### Connected Components
| Term | Definition |
|------|-----------|
| Connected component | Maximal set of nodes where every node can reach every other via some path |
| Weakly connected component | Connected if we IGNORE edge directions (directed graphs) |
| Strongly connected component | Every node can reach every other node FOLLOWING edge directions |
| Giant component | The largest connected component containing most nodes |

### Bridges
| Term | Definition |
|------|-----------|
| **Bridge** | An edge whose removal increases the number of connected components (lies on no cycle) |
| **Local bridge** | An edge (u, v) where N(u) ∩ N(v) = ∅ — endpoints share NO common neighbors |

### Graph Search Algorithms
| Algorithm | Key Property | Complexity |
|-----------|-------------|------------|
| **BFS** (Breadth-First Search) | Finds shortest paths in UNWEIGHTED graphs; explores layer by layer (FIFO queue); Layer k = all nodes at distance exactly k | O(\|V\| + \|E\|) |
| **Dijkstra** | Finds shortest paths in WEIGHTED graphs with non-negative weights; uses min-heap priority queue | O((\|V\| + \|E\|) log \|V\|) |
| **Bellman-Ford** | Shortest paths with NEGATIVE weights (no negative cycles) | O(\|V\| · \|E\|) |
| BFS = Dijkstra when all edge weights = 1 | | |
| BFS from node s discovers all nodes at distance k before any at distance k+1 | | |

---

## 3. CENTRALITY MEASURES

### Degree Centrality
| Formula | Plain English |
|---------|--------------|
| C_D(v) = deg(v) / (n - 1) | Degree centrality = number of direct connections / maximum possible connections |
| Range: 0 to 1 | 0 = isolated, 1 = connected to everyone |

### Closeness Centrality
| Formula | Plain English |
|---------|--------------|
| C_C(v) = (n - 1) / Σ_{u≠v} d(v, u) | Closeness = (number of other nodes) / (sum of distances from v to all others) |
| Range: 0 to 1 | 1 = directly adjacent to everyone |
| FAILS on disconnected graphs | Distance to unreachable nodes = ∞ |

### Harmonic Centrality
| Formula | Plain English |
|---------|--------------|
| H(v) = Σ_{u≠v} 1/d(v, u), with 1/∞ = 0 | Sum of reciprocal distances — unreachable nodes contribute 0, not ∞ |
| HMD(v) = (n - 1) / H(v) | Harmonic mean distance = how many hops on average to reach others |

### Betweenness Centrality
| Formula | Plain English |
|---------|--------------|
| C_B(v) = Σ_{s≠v≠t} σ_st(v) / σ_st | For every pair (s,t): fraction of shortest paths from s to t that pass THROUGH v |
| σ_st = total number of shortest paths from s to t | |
| σ_st(v) = number of those shortest paths that go through node v | |
| Normalized: divide by (n-1)(n-2)/2 for undirected | |
| Brandes algorithm: O(n(n+m)) for all nodes | |

### Edge Betweenness
| Formula | Plain English |
|---------|--------------|
| C_B(e) = Σ_{s≠t} σ_st(e) / σ_st | For every pair (s,t): fraction of shortest paths from s to t that pass THROUGH edge e |
| O(nm) with Brandes algorithm | Used in Girvan–Newman community detection |

### Eigenvector Centrality
| Formula | Plain English |
|---------|--------------|
| C_E(v) = (1/λ) Σ_u A_{vu} C_E(u) | A node's importance = the sum of its neighbors' importance, scaled by eigenvalue |
| Ax = λx | The centrality vector x is the leading eigenvector of the adjacency matrix A |
| Power iteration: x^(t+1) = Ax^(t) / \|\|Ax^(t)\|\| | Repeatedly multiply by A and normalize until convergence |

### PageRank
| Formula | Plain English |
|---------|--------------|
| PR(v) = (1-α)/n + α Σ_{u→v} PR(u)/outdeg(u) | PageRank of v = random jump + sum of (each incoming neighbor's PageRank / that neighbor's out-degree) |
| α = damping factor (typically 0.85) | Probability of following a link (vs. random jump) |
| (1-α)/n = random jump probability | With probability 1-α, teleport to any random page |
| Scores sum to 1 (they are probabilities) | |
| Convergence: O(m) per iteration, ~10 iterations | |

### Quick Comparison Table
| Measure | Captures | Complexity (all nodes) |
|---------|----------|----------------------|
| Degree | Direct exposure / popularity | O(n + m) |
| Closeness | Short-path access to everyone | O(n(n + m)) |
| Harmonic | Reachable proximity (handles disconnected) | O(n(n + m)) |
| Betweenness | Brokerage / control over paths | O(n(n + m)) |
| Eigenvector | Recursive prestige | O(k(n + m)) |
| PageRank | Random surfer prestige | O(k·m) |

---

## 4. CLUSTERING AND TRIADS

### Clustering Coefficient
| Formula | Plain English |
|---------|--------------|
| C(v) = 2 × (edges among v's neighbors) / (deg(v) × (deg(v) - 1)) | Local clustering = actual edges among neighbors / possible edges among neighbors |
| Range: 0 to 1 | 0 = no neighbors connected; 1 = all neighbors connected to each other |
| C_global = 3 × (number of triangles) / (number of connected triples) | Global clustering = 3× triangles / connected triples (each triangle has 3 triples) |

### Triadic Closure
| Term | Definition |
|------|-----------|
| **Triadic closure** | If A knows B and A knows C, then B and C are likely to become connected |
| **Open triad** | Triple (A, B, C) where A-B and A-C exist but B-C does not |
| **Strong Triadic Closure (STC)** | If node v has strong ties to u₁ and u₂, then edge (u₁, u₂) must exist (any label) |
| STC is about LABELINGS, not graphs | Same graph can have valid and invalid STC labelings |

### Weak Ties
| Term | Definition |
|------|-----------|
| **Weak-tie theorem** | If a node satisfies STC and has ≥ 2 strong ties, any local bridge incident to it must be Weak |
| **Proof idea**: If the local bridge were strong, STC would force shared neighbors → contradiction with local bridge definition |
| Weak ties bridge communities | They carry novel, non-redundant information |

### Neighborhood Overlap
| Formula | Plain English |
|---------|--------------|
| O(u, v) = \|N(u) ∩ N(v)\| / \|N(u) ∪ N(v)\| | Overlap = shared neighbors / all neighbors of u and v combined |
| O = 0 means local bridge | No shared neighbors between u and v |

---

## 5. HOMOPHILY AND E-I INDEX

### Homophily Index
| Formula | Plain English |
|---------|--------------|
| H_base = Σᵢ pᵢ² | **Random-mixing baseline** = sum of squared population shares for each group |
| H_obs = fraction of ties that are within-group | **Observed homophily** = actual proportion of same-group ties |
| r = (H_obs - H_base) / (1 - H_base) | **Homophily index** = (observed - baseline) / (maximum - baseline) |
| r = 0: random mixing | No preference beyond what chance predicts |
| r = 1: perfect segregation | All ties are within-group |
| r < 0: heterophily | Fewer within-group ties than expected by chance |

### E-I Index
| Formula | Plain English |
|---------|--------------|
| EI = (External ties - Internal ties) / (External ties + Internal ties) | |
| EI = (E - I) / (E + I) | |
| E = number of edges where group(u) ≠ group(v) | Cross-group / external edges |
| I = number of edges where group(u) = group(v) | Within-group / internal edges |
| E + I = total number of edges \|E\| | Every edge is either external or internal |
| Range: -1 to +1 | -1 = pure homophily, +1 = pure heterophily, 0 = neutral |
| EI < 0: homophilic | More internal than external edges |
| EI > 0: heterophilic | More external than internal edges |

### Random-mixing baseline for E-I
| Formula | Plain English |
|---------|--------------|
| P(cross \| random) = 1 - Σᵢ C(nᵢ, 2) / C(N, 2) | Expected cross-group fraction under random mixing = 1 minus the sum of within-group pair fractions |

### Selection vs. Socialization
| Term | Definition |
|------|-----------|
| **Selection** | Similarity causes tie formation (attribute → tie) |
| **Socialization** | Tie formation causes similarity (tie → attribute) |
| **Contextual correlation** | Shared environment causes BOTH (confounder → tie AND confounder → attribute) |
| Cross-sectional data CANNOT distinguish these three | Need longitudinal data, experiments, or causal models |

---

## 6. STRUCTURAL HOLES AND BROKERAGE

| Term | Definition |
|------|-----------|
| **Structural hole** | A missing connection between two groups that would otherwise be connected (Burt, 1992) |
| **Broker** | An actor who spans a structural hole — sole link between separated groups |
| **Information advantage** | Broker receives early, non-redundant signals from independent groups |
| **Control advantage** | Broker mediates flows between groups that cannot communicate directly |
| **Embedded node** | High clustering coefficient — neighbors are densely interconnected |
| **Broker** | Low clustering coefficient, high betweenness — sole link between clusters |

---

## 7. COMMUNITY DETECTION

### Modularity
| Formula | Plain English |
|---------|--------------|
| Q = (1/2m) Σ_{i,j} (A_{ij} - k_i·k_j / 2m) δ(c_i, c_j) | **Pairwise form**: for each pair in the same community, compare actual edge to expected edge under random rewiring |
| Q = Σ_c (l_c/m - (d_c/2m)²) | **Grouped form**: for each community c, (fraction of internal edges) minus (expected fraction)² |
| l_c = number of internal edges in community c | |
| d_c = sum of degrees of nodes in community c | |
| m = total number of edges | |
| δ(c_i, c_j) = 1 if nodes i and j are in the same community, 0 otherwise | |
| Range: [-0.5, 1] in practice | Q = 0 means no better than random; Q > 0 means community structure exists |
| Maximizing Q is NP-hard | All practical methods are heuristics |

### Resolution Limit
| Formula | Plain English |
|---------|--------------|
| Communities smaller than √(2m) are invisible | Modularity cannot detect communities below this size threshold |
| Max contribution of size-s community ≈ s²/(2m) | If this is < 1, the community is invisible to Q |

### Community Detection Methods
| Method | Strategy | Key Detail |
|--------|----------|------------|
| **Girvan–Newman** | Divisive (top-down) | Iteratively remove highest edge-betweenness edge |
| **Louvain** | Agglomerative (bottom-up) | Greedily merge pairs that increase Q |
| **Leiden** | Agglomerative | Improved Louvain — guarantees well-connected communities |
| **Spectral** | Cut-based | Use Fiedler vector (eigenvector of λ₂ of Laplacian) to partition |
| **Min-cut** | Cut-based | Find smallest edge set whose removal disconnects two groups |
| **Kernighan–Lin** | Local search | Iteratively swap node pairs to decrease cut size |
| **Embedding-based** | Learn + cluster | node2vec/k-means or GNNs, then cluster embeddings |

### Dendrogram
| Term | Definition |
|------|-----------|
| **Dendrogram** | Tree where leaves = nodes, internal nodes = merges/splits; each horizontal cut = a flat partition |
| Agglomerative | Start with n singletons, repeatedly merge closest pair |
| Divisive | Start with whole graph, repeatedly split or remove edges |
| Cut point | Analyst's choice — often the cut that maximizes Q |

---

## 8. SPECTRAL METHODS

### Graph Laplacian
| Formula | Plain English |
|---------|--------------|
| L = D - A | Laplacian = Degree matrix minus Adjacency matrix |
| D_ii = deg(i), D_ij = 0 for i≠j | Degree matrix is diagonal with node degrees |
| L_norm = D^(-1/2) L D^(-1/2) | Normalized Laplacian |
| L_rw = D^(-1) L = I - D^(-1)A | Random-walk Laplacian |

### Laplacian Properties
| Property | Meaning |
|----------|---------|
| L is positive semi-definite | All eigenvalues ≥ 0 |
| λ₁ = 0 always | With eigenvector = constant vector **1** |
| λ₂ > 0 ⟺ graph is connected | Second-smallest eigenvalue (Fiedler value) |
| λ₂ = 0 ⟺ graph is disconnected | |

### Algebraic Connectivity (Fiedler Value)
| Formula | Plain English |
|---------|--------------|
| λ₂ = second-smallest eigenvalue of L = D - A | Measures how easy the graph is to disconnect |
| Larger λ₂ → harder to disconnect | More robust connectivity |
| Fiedler vector = eigenvector of λ₂ | Nodes with x₂(i) > 0 go left, x₂(i) < 0 go right |

### Spectral Partitioning
1. Compute L = D - A
2. Find Fiedler vector x₂ (eigenvector of λ₂)
3. Partition: positive entries → group 1, negative entries → group 2
4. Generalize to k communities: use k smallest eigenvectors

### Signed Laplacian
| Formula | Plain English |
|---------|--------------|
| L_σ = D - A_σ | Signed Laplacian = Degree matrix minus Signed adjacency matrix |
| (A_σ)_ij = +1 for positive edges, -1 for negative edges | |
| λ₁(L_σ) = 0 ⟺ graph is balanced | Smallest eigenvalue is zero if and only if the signed graph is balanced |
| λ₁ > 0 means unbalanced | Magnitude measures how far from balanced |

---

## 9. RANDOM GRAPHS AND NETWORK MODELS

### Erdős–Rényi Random Graph G(n, p)
| Formula | Plain English |
|---------|--------------|
| n nodes, each pair connected independently with probability p | |
| Expected edges = C(n, 2) × p | C(n,2) = n(n-1)/2 possible edges, each present with prob p |
| Average degree k = p(n-1) ≈ pn | |
| Average path length d̄ ≈ log(n) / log(k) | **Small-world property** — distances grow logarithmically |
| Clustering C = p = k/(n-1) ≈ k/n | Very low for large n |
| Degree distribution: Binomial ≈ Poisson | Homogeneous — all nodes have roughly the same degree |
| Giant component threshold: k = 1 (i.e. p = 1/n) | Below this: many small components; above: one giant component |
| Connectivity threshold: p > ln(n)/n | Above this: graph is almost surely connected |

### Small-World Index (σ)
| Formula | Plain English |
|---------|--------------|
| σ = (C / C_rand) / (L / L_rand) | Small-world index = (clustering ratio) / (path length ratio) |
| C = average clustering of real graph | C_rand = average clustering of random graph with same n and m |
| L = average shortest path length of real graph | L_rand = average shortest path length of the random graph |
| σ >> 1 (typically > 3) → small-world | High clustering + short paths |
| σ ≈ 1 → random-like | No small-world structure |

### Average Path Length Estimation
| Formula | Plain English |
|---------|--------------|
| d ≈ log(N) / log(k) | Random-graph approximation: N = nodes, k = average degree |
| Example: N = 10⁹, k = 200 → d ≈ 20.7/5.3 ≈ 3.9 hops | |
| Real networks often slightly longer than random prediction | Clustering creates dead ends that trap walks |

### Watts–Strogatz Small-World Model
| Property | Value |
|----------|-------|
| Start with ring of n nodes, each connected to k nearest neighbors | Regular lattice |
| Rewire each edge with probability p | |
| p = 0 | High clustering, long paths (lattice) |
| 0 < p ≪ 1 | **Small-world regime**: high clustering + short paths |
| p = 1 | Low clustering, short paths (random graph) |
| Key insight | L(p) drops much faster than C(p) — a few shortcuts collapse path length without destroying clustering |

### Barabási–Albert Preferential Attachment
| Formula | Plain English |
|---------|--------------|
| Π(k_i) = k_i / Σ_j k_j | New node connects to existing node i with probability proportional to i's degree ("rich get richer") |
| P(k) ~ 2m² k^{-3} | Degree distribution is power law with γ = 3 |
| d̄ ~ log(n) / log(log(n)) | **Ultra-small** distances — even shorter than random graphs |
| C ~ (log n)² / n | Clustering decreases with n but higher than random graphs |

### Scale-Free Networks
| Formula | Plain English |
|---------|--------------|
| P(k) ~ k^{-γ} | Power-law degree distribution — no "typical" degree |
| γ typically between 2 and 3 for real networks | |
| ⟨k²⟩ diverges for γ ≤ 3 | Second moment of degree → ∞ as N → ∞ |
| Hubs act as shortcuts | Distances shorter than log(n)/log(k) |
| Robust to random failure | Random removal rarely hits hubs |
| Vulnerable to targeted attack | Removing hubs fragments the network |

### Kleinberg's Navigability Theorem
| Formula | Plain English |
|---------|--------------|
| Grid: d-dimensional grid + long-range links with probability ∝ r^(−α) | Long-range links decay with distance r |
| Greedy routing achieves O((log N)²) delivery **iff α = d** | Exponent must equal grid dimension for navigability |
| α < d: links too uniform — not enough local bias | Greedy routing gets lost |
| α > d: links too clustered — not enough reach | Greedy routing can't escape locally |
| 2D grid: α = 2 is optimal | Small-world but ALSO efficiently navigable |
| Key insight: short paths exist (small-world) but aren't always locally findable | Navigability requires the right link distribution |

### Distance Formulas Comparison
| Network Type | Average Path Length |
|-------------|-------------------|
| Random graph G(n,p) | log(n) / log(k) |
| Scale-free (BA model) | log(n) / log(log(n)) |
| Regular lattice (ring) | ~ n / (2k) |
| Real social networks | 3–6 (empirical) |

---

## 10. EPIDEMIC MODELS ON NETWORKS

### SI Model (Susceptible–Infected)
| Term | Definition |
|------|-----------|
| States: S, I | Irreversible: once infected, always infected |
| β = spreading rate per contact | |
| No recovery — used for irreversible spreading (rumors) | |

### SIS Model (Susceptible–Infected–Susceptible)
| Formula | Plain English |
|---------|--------------|
| dI/dt = βSI - γI | Change in infected = new infections - recoveries |
| R₀ = β/γ | **Basic reproduction number** = spreading rate / recovery rate |
| R₀ > 1: disease becomes endemic | Persists indefinitely |
| R₀ ≤ 1: disease dies out | |
| Endemic equilibrium: I* = 1 - γ/β (when β > γ) | |
| On networks: epidemic threshold τ = γ/β = ⟨k⟩ / ⟨k²⟩ | |
| On scale-free networks: τ → 0 | Any disease can persist (threshold vanishes) |

### SIR Model (Susceptible–Infected–Recovered)
| Formula | Plain English |
|---------|--------------|
| R₀ = (β/γ) × ⟨k⟩ | Basic reproduction number = (spreading rate / recovery rate) × average degree |
| R₀ > 1: epidemic spreads | |
| R₀ < 1: epidemic dies out | |
| Epidemic threshold (heterogeneous networks): T_c ≈ ⟨k⟩ / (⟨k²⟩ - ⟨k⟩) | T = transmissibility per edge; epidemic if T > T_c |
| On scale-free (γ ≤ 3): T_c → 0 | No finite epidemic threshold |

### SIRS Model (Susceptible–Infected–Recovered–Susceptible)
| Formula | Plain English |
|---------|--------------|
| R → S at rate δ | Waning immunity — recovered nodes become susceptible again |
| 1/δ = average immunity duration | |
| Oscillatory dynamics | Epidemic waves with period ~ 1/δ |
| Reduces to SIR when δ → 0 | Permanent immunity |
| Reduces to SIS when δ → ∞ | No immunity |

### Key Epidemic Results
| Result | Meaning |
|--------|---------|
| In scale-free networks (γ ≤ 3), ⟨k²⟩ → ∞ | Epidemic threshold τ = ⟨k⟩/⟨k²⟩ → 0 |
| Hubs are superspreaders | High-degree nodes infected more often, infect more neighbors |
| Targeted vaccination of top 5-10% hubs | Can restore a finite epidemic threshold |
| Random vaccination cannot achieve herd immunity | In scale-free networks, would need ~100% coverage |

---

## 11. SIGNED NETWORKS AND STRUCTURAL BALANCE

### Signed Graph Basics
| Term | Definition |
|------|-----------|
| Signed graph (G, σ) | Graph where σ: E → {+, −} assigns a sign to each edge |
| + edge | Alliance, friendship, trust |
| − edge | Rivalry, hostility, distrust |

### The Four Triad Types
| # Negative | Pattern | Strong Balance | Weak Balance | Interpretation |
|------------|---------|----------------|--------------|---------------|
| 0 | (+, +, +) | Balanced ✓ | Balanced ✓ | All friends |
| 1 | (+, +, −) | Unbalanced ✗ | Unbalanced ✗ | Friend of my friend is my enemy — TENSION |
| 2 | (+, −, −) | Balanced ✓ | Balanced ✓ | Enemy of my enemy is my friend |
| 3 | (−, −, −) | Unbalanced ✗ | Balanced ✓ | Three mutual enemies (Davis allows this) |

### Balance Theorem (Cartwright & Harary 1956)
| Statement | Meaning |
|-----------|---------|
| A complete signed graph is balanced ⟺ every triangle has an even number of negative edges (0 or 2) | Local triangle rule |
| ⟺ nodes can be partitioned into at most 2 camps | Global structure: positive within camps, negative between camps |

### Weak Structural Balance (Davis 1967)
| Statement | Meaning |
|-----------|---------|
| Only (+, +, −) is forbidden | Allows all-negative triangles |
| ⟺ nodes partitioned into k ≥ 1 camps | Positive within each camp, negative between camps |
| k = 1: all positive; k = 2: strong balance; k ≥ 3: multipolar | |

### Frustration Index
| Formula | Plain English |
|---------|--------------|
| F(G, σ) = minimum number of edge sign flips to make graph balanced | |
| Computing F is NP-hard | |
| Signed Laplacian check: λ₁(L_σ) = 0 ⟺ balanced | Polynomial-time alternative to check balance |

### Balance Test
| Method | Complexity |
|--------|-----------|
| Complete graphs: check all C(n,3) triangles | O(n³) |
| General graphs: cycle criterion — every cycle has even # negative edges | |
| Signed Laplacian: check if λ₁ = 0 | O(|E| · d) with Lanczos |

---

## 12. BIPARTITE AND AFFILIATION NETWORKS

### Bipartite Graph
| Formula | Plain English |
|---------|--------------|
| G = (U, V, E) | Two disjoint node sets, edges only between U and V |
| No edges within U or within V | A graph is bipartite ⟺ it contains no odd-length cycles |

### Co-occurrence Projections
| Formula | Plain English |
|---------|--------------|
| B = membership matrix (B_pf = 1 if person p in focus f) | |
| Person co-occurrence: BBᵀ | Edge weight = number of shared foci between two persons |
| Focus co-occurrence: BᵀB | Edge weight = number of shared participants between two foci |

### Three Closure Mechanisms
| Type | Mechanism | Example |
|------|-----------|---------|
| **Triadic closure** | Two nodes share a friend → become friends | "My lab partner introduces me to their friend" |
| **Focal closure** | Two nodes share an affiliation → become friends | "We sit in the same class and start talking" |
| **Membership closure** | A friend pulls you into a new context | "My friend invites me to the robotics club" |

### Projection Caution
| Issue | Meaning |
|-------|---------|
| Projection creates dense cliques | A focus with s members adds C(s, 2) = s(s-1)/2 edges |
| Co-occurrence ≠ relationship | Shared context is opportunity, not confirmed tie |
| Keep weights | Sharing 5 foci is stronger evidence than sharing 1 |

---

## 13. NETWORK DIFFUSION AND CASCADES

### Threshold Cascades
| Formula | Plain English |
|---------|--------------|
| Node v adopts if \|active neighbors\| / \|total neighbors\| ≥ q | Adoption threshold: fraction of neighbors that must be active |
| q ≤ 1/2 required for global cascades | If q > 1/2, cascades need local majority — very hard to trigger |
| Wide bridges (multiple edges) enable cross-community spread | |
| Thin bridges (single edges) block cascades | Insufficient reinforcement |

### Diffusion of Innovations (Rogers 1962)
| Category | % of Population | Characteristic |
|----------|----------------|---------------|
| Innovators | 2.5% | First to adopt, low threshold |
| Early adopters | 13.5% | Opinion leaders |
| Early majority | 34% | Adopt after seeing evidence |
| Late majority | 34% | Adopt due to social pressure |
| Laggards | 16% | Last to adopt, very high threshold |

### Simple vs. Complex Contagion
| Type | Mechanism | Example |
|------|-----------|---------|
| **Simple contagion** | Single contact sufficient | Disease (one S-I contact infects) |
| **Complex contagion** | Needs multiple adopting neighbors | Behavior change, innovation adoption |
| Simple → weak ties help | Any single path suffices |
| Complex → clustering helps | Dense reinforcement needed |

---

## 14. NODE EMBEDDINGS AND GNNs

### DeepWalk
| Formula | Plain English |
|---------|--------------|
| Treat random walks as sentences, nodes as words | Apply word2vec skip-gram to walk corpus |
| L = Σ_i Σ_t Σ_{-c≤j≤c, j≠0} log P(v_{t+j} \| v_t) | Skip-gram objective: predict context nodes from center node |
| P(u\|v) = exp(z_u · z_v) / Σ_{u'} exp(z_{u'} · z_v) | Softmax over all nodes (approximated by negative sampling) |
| Transductive: new node needs retraining | Feature-free: uses only graph structure |

### Node2Vec
| Formula | Plain English |
|---------|--------------|
| α(t, x) = 1/p if d(t,x)=0 (return) | Return parameter: small p → DFS-like (explore communities) |
| α(t, x) = 1 if d(t,x)=1 (stay local) | |
| α(t, x) = 1/q if d(t,x)=2 (move outward) | In-out parameter: small q → BFS-like (sample neighborhoods) |
| p = q = 1 recovers DeepWalk | |
| Small p → homophily (community similarity) | |
| Small q → structural equivalence (role similarity) | |

### Message Passing Framework (GNNs)
| Formula | Plain English |
|---------|--------------|
| h_v^{(l+1)} = UPDATE(h_v^{(l)}, AGG({h_u^{(l)} : u ∈ N(v)})) | Each layer: aggregate neighbor states, then update own state |
| AGG must be permutation-invariant | Sum, mean, max, or attention — neighborhoods are sets |
| L layers → L-hop receptive field | Each layer extends view by one hop |

### GNN Variants
| Variant | AGG | Key Feature |
|---------|-----|-------------|
| **GCN** | Normalized sum: Ã = D̃^{-1/2}(A+I)D̃^{-1/2} | Simple baseline |
| **GraphSAGE** | Sampled subset of neighbors | Scales to large graphs, inductive |
| **GAT** | Learned attention weights α_{uv} | Different neighbors contribute differently |
| **GIN** | Sum + MLP | Provably as powerful as Weisfeiler-Lehman test |

### Over-smoothing
| Problem | Meaning |
|---------|---------|
| Too many GNN layers → all embeddings collapse to same vector | Nodes become indistinguishable |
| Typical limit: L = 3-5 layers | Beyond this, performance degrades |

---

## 15. WEB STRUCTURE

### Web Bow-Tie (Broder et al. 2000)
| Component | Fraction | Definition |
|-----------|----------|-----------|
| **SCC** (Strongly Connected Core) | ~28% | Every page reachable from every other via directed paths |
| **IN** | ~21% | Can reach SCC but not reached from it |
| **OUT** | ~21% | Reached from SCC but can't reach back |
| **Tendrils/tubes** | ~22% | Connected to IN or OUT but not to SCC |

---

## 16. TEMPORAL NETWORKS

| Term | Definition |
|------|-----------|
| Temporal network | Graph where each edge e has an activation time t(e) |
| Time-respecting path | Sequence of edges e₁, e₂, …, e_k where t(e₁) < t(e₂) < … < t(e_k) |
| Static aggregation overestimates reachability | Paths in static graph may not exist as time-respecting paths |
| Order matters as much as existence | When edges activate is as important as which edges exist |

---

## 17. AUTOCORRELATION AND CONFOUNDING

### Network Autocorrelation
| Term | Definition |
|------|-----------|
| Network autocorrelation | Statistical tendency for connected nodes to share attributes |
| **Moran's I** | Global autocorrelation statistic |
| **Geary's C** | Alternative measure, more sensitive to local patterns |
| Autocorrelation ≠ mechanism | Same pattern from selection, socialization, or context |

### Confounding
| Term | Definition |
|------|-----------|
| **Confounder** | Third variable C that causes both attribute A and tie B |
| Selection: A → B | Attribute causes tie |
| Socialization: B → A | Tie causes attribute |
| Confounding: C → A and C → B | Shared environment causes both |
| Cross-sectional data cannot distinguish these | Need longitudinal/experimental design |

---

## 18. SCHELLING SEGREGATION MODEL

| Term | Definition |
|------|-----------|
| **Schelling model** | Agents on a grid, each with a type and a threshold τ for same-type neighbours |
| Threshold τ ≈ 30–40% | Agent is satisfied if ≥ τ fraction of neighbours are same-type; otherwise moves |
| Key result | **Mild** individual preferences (30–40%) cascade into **strong** global segregation |
| Mechanism | One agent's move changes neighbourhood composition → triggers further moves → cascade |
| Macro >> micro | Aggregate segregation far exceeds any individual's preference |
| **Identification problem** | Cannot infer individual preferences from aggregate outcomes |
| Recommendation algorithms | Act as automated Schelling rewirers, accelerating amplification |

---

## 19. THE SIX GAPS OF THE COURSE

| Gap | Lectures | Core Tension |
|-----|----------|-------------|
| **Computational** | L03–L04 | NP-hard ideals (modularity max, frustration index) vs. polynomial heuristics |
| **Causal** | L05 | Selection vs. socialisation — mechanism unidentifiable from cross-sectional snapshots |
| **Structural** | L06 | Balance theory assumes complete graphs, but real data is sparse |
| **Navigational** | L07 | Short paths exist (small-world) but aren't locally findable without the right structure (Kleinberg) |
| **Process-Structure** | L08 | Same network structure produces different outcomes for different spreading processes |
| **Temporal** | L08 | Static aggregation hides causal ordering, creating phantom paths |

---

## QUICK REFERENCE: KEY THRESHOLDS

| Threshold | Formula | Meaning |
|-----------|---------|---------|
| Giant component | ⟨k⟩ = 1 (p = 1/n) | Phase transition from fragments to giant component |
| Connectivity | p > ln(n)/n | Graph becomes connected |
| Epidemic (random graph) | R₀ = (β/γ) × ⟨k⟩ > 1 | Disease spreads |
| Epidemic (SIS on network) | τ = ⟨k⟩/⟨k²⟩ | Threshold below which disease dies |
| Epidemic (scale-free) | τ → 0 for γ ≤ 3 | No finite threshold — any disease can spread |
| Cascade | q ≤ 1/2 | Threshold for global cascades |
| Modularity resolution | community size > √(2m) | Below this, modularity can't detect the community |
