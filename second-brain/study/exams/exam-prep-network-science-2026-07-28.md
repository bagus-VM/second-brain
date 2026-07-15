---
title: "Network Science Exam Prep — July 28, 2026"
tags:
  - exam-prep
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-07-15
exam_date: 2026-07-28
exam_format: "Open questions + structured questions, from exercises and lectures"
scope: "Lectures 1-8, Exercises 1-8"
---

# Network Science — Exam Battle Plan

## Scope Confirmation
- **Format:** Open questions + structured questions
- **Source:** Both exercises AND lectures
- **Up to:** Lecture 8, Exercise Sheet 8
- **Key topics confirmed by professor:** centrality equations, small-world equation, graph search algorithms

---

## Topic Coverage Map

| Topic | Exercises | Lectures | Vault Pages | Priority |
|---|---|---|---|---|
| Network fundamentals & modeling | E01 | L01-L02 | [[network-examples]] | Medium |
| Graph theory (BFS, paths, connectivity) | E02 | L02-L03 | — | **HIGH** |
| Strong/weak ties & triadic closure | E03 | L03-L04 | [[triadic-closure]] | **HIGH** |
| Centrality measures (EQUATIONS!) | E04 | L04-L05 | [[centrality]] | **CRITICAL** |
| Community detection & modularity | E05 | L05-L06 | — | **HIGH** |
| Homophily, affiliation, Schelling | E06 | L06-L07 | — | Medium |
| Structural balance (signed networks) | E07 | L07-L08 | — | **HIGH** |
| Small-world networks (EQUATION!) | E08 | L08 | — | **CRITICAL** |
| Graph search algorithms | E02 | L02-L03 | — | **CRITICAL** |

---

# PART A: STRUCTURED QUESTIONS (with equations and computations)

---

## S1. Centrality Measures — The Equations

### S1.1 Degree Centrality
**Formula:**
$$C_D(v) = \frac{\deg(v)}{n - 1}$$

- Counts direct connections (local measure)
- Normalised by maximum possible connections (n-1)
- For directed graphs: split into in-degree and out-degree
- Complexity: O(n + m)

**Exam question:** Graph with 6 nodes: A-B, A-C, B-C, B-D, D-E, D-F, E-F. Compute C_D for all nodes.

> **Answer:** n=6, so divide by 5.
> A: deg=2 → 0.4 | B: deg=3 → 0.6 | C: deg=2 → 0.4
> D: deg=3 → 0.6 | E: deg=2 → 0.4 | F: deg=2 → 0.4
> B and D are tied for highest degree centrality.

---

### S1.2 Closeness Centrality
**Formula:**
$$C_C(v) = \frac{n - 1}{\sum_{u \neq v} d(v, u)}$$

- Inverse of average shortest-path distance to all other nodes
- Captures global reach / broadcast capability
- Fails on disconnected graphs (infinite distances)
- Complexity: O(n(n+m)) — need BFS from every node

**Exam question:** For node B in the same graph, compute C_C.

> **Answer:** Distances from B: d(B,A)=1, d(B,C)=1, d(B,D)=1, d(B,E)=2, d(B,F)=2. Sum=7.
> C_C(B) = 5/7 ≈ 0.714

---

### S1.3 Harmonic Centrality
**Formula:**
$$H(v) = \sum_{u \neq v} \frac{1}{d(v, u)} \quad \text{where } \frac{1}{\infty} = 0$$

- Robust alternative to closeness for disconnected graphs
- Unreachable nodes contribute 0 instead of infinity
- Same complexity as closeness: O(n(n+m))

---

### S1.4 Betweenness Centrality
**Formula:**
$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

Where:
- σ_st = total number of shortest paths from s to t
- σ_st(v) = number of those paths that pass through v

- Identifies brokers / bridges
- Brandes algorithm: O(n(n+m)) for unweighted graphs
- For edges: same formula but sum over paths through edge (e, f)

**Exam question:** For node D in the graph A-B, A-C, B-C, B-D, D-E, D-F, E-F, compute C_B.

> **Answer:** D sits on the ONLY path from {A,B,C} to {E,F}. All 3×2=6 node pairs require D. After normalisation (divide by (n-1)(n-2)/2 = 10), C_B(D) = 6/10 = 0.6. B has similar but slightly lower betweenness because paths from {A,C} to {E,F} go through both B and D.

---

### S1.5 Eigenvector Centrality
**Formula (matrix form):**
$$Ax = \lambda x$$

Where A is the adjacency matrix and x is the centrality vector (leading eigenvector).

- Recursive prestige: your centrality depends on the centrality of your neighbours
- A node connected to many central nodes is itself central
- Complexity: O(k(n+m)) per power iteration

---

### S1.6 PageRank
**Formula:**
$$PR(v) = \frac{1 - \alpha}{n} + \alpha \sum_{u \to v} \frac{PR(u)}{\text{outdeg}(u)}$$

Where α is the damping factor (typically 0.85).

- Models a random surfer who follows links with probability α and teleports with probability (1-α)
- Handles dangling nodes (nodes with no outgoing edges)
- Converges by power iteration
- Differences from eigenvector centrality: damping + teleportation + handles directed graphs naturally

**Quick decision guide:**
- Exposure / spreaders → **Degree**
- Fast reach / broadcast → **Closeness / Harmonic**
- Brokers / bridges → **Betweenness**
- Prestige from important neighbours → **Eigenvector / PageRank**

---

## S2. Graph Theory & Search Algorithms

### S2.1 BFS (Breadth-First Search)
- Explores nodes layer by layer (FIFO queue)
- Finds shortest paths in UNWEIGHTED graphs
- Complexity: O(n + m)
- Used to compute: distances, eccentricity, diameter, connected components

**Key properties:**
- BFS tree encodes all shortest paths from source
- Layer k = all nodes at distance exactly k from source
- Cannot handle weighted edges (use Dijkstra instead)

**Exam question:** Run BFS from node 1 on graph: 1-2, 1-3, 2-4, 2-5, 3-6, 4-7, 5-7, 6-8. Give the BFS tree layers.

> **Answer:**
> Layer 0: {1}
> Layer 1: {2, 3}
> Layer 2: {4, 5, 6}
> Layer 3: {7, 8}
> d(1,7) = 3, d(1,8) = 3. Node 7 has two shortest paths (via 4 or via 5).

---

### S2.2 Dijkstra's Algorithm
- Finds shortest paths in WEIGHTED graphs (non-negative weights)
- Uses a priority queue (min-heap)
- Complexity: O((n + m) log n)
- BFS is a special case of Dijkstra where all edge weights = 1

**When to use which:**
- Unweighted graph → BFS
- Weighted graph (non-negative) → Dijkstra
- Weighted graph (negative weights) → Bellman-Ford

---

### S2.3 Graph Properties & Terminology

| Concept | Definition |
|---|---|
| Walk | Any sequence of nodes connected by edges (nodes/edges may repeat) |
| Path | Walk with no repeated nodes |
| Cycle | Path that returns to its start |
| Diameter | Maximum eccentricity = longest shortest path |
| Radius | Minimum eccentricity |
| Centre | Node(s) with eccentricity = radius |
| Connected component | Maximal set of nodes reachable from each other |
| SCC (directed) | Maximal set where every node can reach every other via directed paths |
| WCC (directed) | Weakly connected: connected if you ignore direction |

---

### S2.4 Euler's Theorem
- **Eulerian circuit** exists iff every vertex has even degree
- **Eulerian path** exists iff exactly 0 or 2 vertices have odd degree
- Königsberg: all 4 vertices have odd degree → no Eulerian path or circuit

---

### S2.5 Connectivity & Robustness

**Giant component:** the largest connected component in a graph.

**Random failure vs. targeted attack:**
- Random removal: slow giant component shrinkage (most nodes are peripheral)
- Targeted removal (highest degree first): rapid giant component destruction
- Scale-free networks are robust to random failure but fragile under targeted attack

---

## S3. Strong and Weak Ties

### S3.1 Triadic Closure
**Statement:** If node A has edges to B and C, the probability that edge (B,C) forms is significantly higher than for two random nodes.

**Motivations:** opportunity, trust, social pressure.

**Predicts:**
- Triangle accumulation over time
- Shrinking average path lengths
- Increasingly clustered neighbourhoods for high-degree nodes

---

### S3.2 Clustering Coefficient
**Local clustering coefficient:**
$$C_v = \frac{\text{edges among neighbours of } v}{\binom{k_v}{2}}$$

Where k_v = degree of v.

**Average clustering:**
$$\bar{C} = \frac{1}{n} \sum_v C_v$$

**Exam question:** For node A with neighbours B, C, D where only B-C is an edge, compute C_A.

> **Answer:** k_A = 3, possible edges among neighbours = C(3,2) = 3. Actual edges = 1 (B-C). C_A = 1/3.

---

### S3.3 Neighbourhood Overlap
**Formula:**
$$O(u, v) = \frac{|N(u) \cap N(v)|}{|N(u) \cup N(v)|}$$

Where N(u) and N(v) are the neighbourhoods of u and v (excluding u and v themselves).

- High overlap → strong tie (many shared friends)
- Low overlap → weak tie / local bridge (few shared friends)

---

### S3.4 Bridges and Structural Holes
- **Bridge:** edge whose removal disconnects the graph
- **Local bridge:** edge whose endpoints have no common neighbours
- **Structural hole:** gap between two groups that a broker can exploit
- **Weak Ties Theorem (Strong Triadic Closure):** Under STC, every local bridge is a weak tie
- STC condition: if a node has strong ties to two others, those two must be connected

---

## S4. Community Detection

### S4.1 Modularity
**Formula:**
$$Q = \frac{1}{2m} \sum_c \left[ e_c - \frac{a_c^2}{4m} \right]$$

Where:
- m = total number of edges
- e_c = number of edges inside community c
- a_c = sum of degrees of nodes in community c

**Interpretation:**
- Q = 0: no better than random
- Q = 1: perfect modularity
- Typical range for real networks: Q ∈ [0.3, 0.7]

---

### S4.2 Community Detection Algorithms

| Algorithm | Approach | Key Property |
|---|---|---|
| Greedy modularity | Bottom-up merge | Fast, may over-partition |
| Girvan-Newman | Top-down edge removal | Iteratively removes highest-betweenness edges |
| Hierarchical clustering | Dendrogram-based | Uses distance/similarity matrix |

**Girvan-Newman:** Returns an iterator of partitions. `next(gn)` gives 2 communities, then 3, etc. Built on edge betweenness centrality.

**Hierarchical clustering:** Height in dendrogram = dissimilarity between merged clusters. Cut at largest gap for natural number of clusters.

---

### S4.3 Comparing Detected vs Ground Truth
Use majority-vote per community (community labels are permutation-invariant):
1. For each detected community, count which ground-truth label has majority
2. Assign that majority label as the community's predicted label
3. Compare predicted vs actual per node → accuracy

---

## S5. Homophily, Affiliation, and Schelling

### S5.1 E-I Index
**Formula:**
$$\text{E-I} = \frac{E - I}{E + I}$$

Where E = external edges (between groups), I = internal edges (within groups).

- Range: -1 (pure homophily) to +1 (pure heterophily)
- 0 = neutral (same as random mixing)

---

### S5.2 Affiliation Networks (Bipartite)
- Two types of nodes (e.g., students and courses)
- Projection onto one layer creates edges where shared memberships exist
- Edge weights = number of shared affiliations

**Three closure types:**
- **Triadic closure:** A-B and A-C → B-C likely
- **Focal closure:** B and C both attend same course → B-C forms
- **Membership closure:** B is friends with C who attends course X → B joins X

---

### S5.3 Schelling Segregation Model
- Agents on a grid prefer at least threshold fraction of same-type neighbours
- Dissatisfied agents move
- Key insight: mild individual preferences (30-40%) produce strong global segregation
- The dynamics amplify individual preferences through cascading moves

---

### S5.4 Selection vs Socialization vs Confounding
- **Selection:** similar people become friends (homophily)
- **Socialization:** friends become similar (influence)
- **Confounding:** a third variable causes both similarity and friendship
- Distinguishing requires longitudinal data or experiments

---

## S6. Structural Balance (Signed Networks)

### S6.1 Balance Theorem
**A triangle is balanced iff the product of its edge signs is positive** (0 or 2 negative edges).

| Triangle | Balanced? | Social meaning |
|---|---|---|
| (+, +, +) | Yes | Three mutual friends — most stable |
| (+, +, -) | **NO** | "Two friends hate each other" — tension |
| (+, -, -) | Yes | Two allies sharing a common enemy |
| (-, -, -) | **NO** | Three mutual enemies — no coalition |

**Balance Theorem:** If a signed graph is perfectly balanced, the nodes can be partitioned into two camps such that all within-camp edges are positive and all between-camp edges are negative.

---

### S6.2 Strong vs Weak Balance
- **Strong balance:** only (+,+,+) and (+,-,-) are balanced. Forces exactly two camps.
- **Weak balance:** forbids only (+,+,−). Allows more than two camps (multi-polar world). All-negative triangles are weakly balanced.

---

## S7. Small-World Networks

### S7.1 Small-World Index (σ)
**Formula:**
$$\sigma = \frac{C / C_{\text{rand}}}{L / L_{\text{rand}}}$$

Where:
- C = average clustering coefficient of the real network
- C_rand = average clustering coefficient of a random graph with same n and m
- L = average shortest path length of the real network
- L_rand = average shortest path length of the random graph

**Interpretation:**
- σ >> 1 (typically > 3) → small-world property: high clustering + short paths
- σ ≈ 1 → random-like

---

### S7.2 Average Path Length Estimation
**Formula (random graph approximation):**
$$d \approx \frac{\log N}{\log k}$$

Where N = number of nodes, k = average degree.

**Exam question:** Estimate d for N = 10^9, k = 200.

> **Answer:** d ≈ log(10^9)/log(200) ≈ 20.7/5.3 ≈ 3.9 hops.

**When real networks deviate:**
- Shorter than random: hubs act as super-shortcuts
- Longer than high clustering traps walks inside communities

---

### S7.3 Watts-Strogatz Model
**Key insight:** A tiny rewiring fraction (p ∈ [0.01, 0.1]) destroys global distance without destroying local clustering.

**Behaviour of C(p)/C(0) and L(p)/L(0):**
- L(p) drops sharply around p ≈ 0.01
- C(p) stays near C(0) until moderate p (gradual decay)
- The sweet spot p ∈ [0.01, 0.1] = the small-world regime

**The model interpolates:**
- p = 0 → ring lattice (high clustering, long paths)
- p = 1 → random graph (low clustering, short paths)
- p ≈ 0.01-0.1 → small world (high clustering, short paths)

---

### S7.4 Web Bow-Tie Structure

**Components of a directed web graph:**
| Component | Meaning |
|---|---|
| SCC (giant) | Strongly connected core — mutually reachable hub pages |
| IN | Pages that can reach the SCC but cannot be reached from it |
| OUT | Pages the SCC reaches but which don't link back |
| Tendrils | Reachable only from IN, not from SCC |
| Tubes | Shortcuts connecting IN to OUT bypassing SCC |
| Isolated | Neither reach nor reachable |

**Key insight:** Pages in IN components are invisible to crawlers that start from the SCC core.

**How to find:** Use `nx.strongly_connected_components()` → `nx.condensation()` → classify SCCs relative to the giant SCC.

---

# PART B: OPEN QUESTIONS (conceptual, essay-style)

---

## OQ1. "Explain why different centrality measures can rank nodes differently. Give a concrete example."

**Model answer:**
Different centrality measures capture different structural intuitions. Degree centrality captures direct exposure — a node with many connections. Betweenness captures brokerage — a node that sits on many shortest paths. Closeness captures global reach — a node close to all others. Eigenvector captures recursive prestige — a node connected to other important nodes.

A concrete example: In the political blog network, a blogger who bridges liberal and conservative communities has high betweenness (many shortest paths cross through them) but may have moderate degree (fewer total links than a popular blogger within one community). The popular within-community blogger has high degree and high eigenvector centrality (connected to other popular nodes) but low betweenness (not on paths between communities).

The choice depends on the application: for disease vaccination targeting, betweenness identifies super-spreaders who bridge communities. For information broadcasting, closeness identifies nodes that can reach everyone fastest. For influence campaigns, eigenvector/PageRank identifies nodes whose endorsement carries the most weight.

---

## OQ2. "What is the Weak Ties Theorem? Explain the intuition and give an example."

**Model answer:**
The Weak Ties Theorem (Granovetter, under Strong Triadic Closure) states: if a node A has strong ties to both B and C, then B and C must be connected (STC condition). Therefore, any local bridge (an edge connecting two otherwise disconnected groups) must be a weak tie — because if it were strong, STC would require the two groups to already be connected, contradicting the bridge status.

Intuition: Strong ties create dense, redundant clusters where everyone knows everyone. The only way to connect to a genuinely different social world is through a weak tie — an acquaintance, not a close friend. These weak ties are the bridges that carry novel information (like job leads) across communities.

Example: Granovetter's job study found that people were more likely to hear about job opportunities through rarely-seen acquaintances than close friends. Close friends share your social world (high neighbourhood overlap), so they know what you already know. Acquaintances bridge to different social circles (low overlap), providing non-redundant information.

---

## OQ3. "Explain the small-world phenomenon. Why is it surprising? What two properties define it?"

**Model answer:**
The small-world phenomenon is the observation that most pairs of nodes in a large network are connected by a surprisingly short path — typically logarithmic in the network size (d ≈ log N / log k). Milgram's experiment showed that the average path between two random people in the US was about 6 hops, despite a population of 200 million.

What makes it surprising: A purely random graph also has short paths but low clustering. A regular lattice has high clustering but long paths (d ≈ N/2k). Real social networks have BOTH: high local clustering (friends of friends are friends, C >> C_rand) AND short global paths (L ≈ L_rand). This combination is the small-world property.

The Watts-Strogatz model explains how: start with a ring lattice (high clustering, long paths), then rewire just a tiny fraction of edges (p ≈ 0.01-0.1). A few random shortcuts dramatically reduce global distances while barely affecting local clustering. The small-world index σ = (C/C_rand)/(L/L_rand) >> 1 quantifies this signature.

The deeper lesson: social networks sit in a sweet spot between order (clustering) and randomness (shortcuts). This structure enables both local cohesion and global reach.

---

## OQ4. "Explain the difference between random failure and targeted attack on a network. Why does the answer depend on the degree distribution?"

**Model answer:**
Random failure: remove nodes uniformly at random. Targeted attack: remove nodes in order of decreasing degree (hubs first).

In networks with a relatively homogeneous degree distribution (like random graphs or lattices), both strategies have similar effects because no node is dramatically more connected than others.

In scale-free networks (power-law degree distribution), the difference is dramatic. Most nodes have low degree, so random removal almost certainly hits a peripheral node — the giant component barely shrinks. But targeted removal immediately destroys the hubs that hold the network together, fragmenting it rapidly.

This has practical implications: the Internet backbone is robust to random router failures but vulnerable to targeted attacks on major hubs. Social networks withstand random unfollowing but collapse if key connectors leave. The asymmetry comes from the degree distribution's heterogeneity.

---

## OQ5. "What is modularity? Why can it be misleading? Explain the resolution limit."

**Model answer:**
Modularity Q measures whether communities have more internal edges than expected by chance. Q = 0 means no community structure beyond random; Q = 1 means perfect community structure. Real networks typically have Q ∈ [0.3, 0.7].

Modularity can be misleading for two reasons:
1. **Resolution limit:** Modularity cannot detect communities smaller than a scale that depends on the total number of edges. Small communities embedded in large networks get merged into larger groups even when they are clearly distinct. This is because the expected edge count a²_c/4m becomes non-trivial for small communities.
2. **High-Q ≠ good communities:** You can artificially increase Q by splitting communities further (more communities → typically higher Q, but not always more meaningful).

The resolution limit means greedy modularity maximisation on the karate club graph often finds 3-4 communities instead of the known 2 factions — it splits the larger faction into sub-clusters.

---

## OQ6. "Explain structural balance theory. Why does it predict a two-camp world? What are the limitations?"

**Model answer:**
Structural balance theory (Heider) studies signed networks where edges are positive (friendship) or negative (hostility). A triangle is balanced if the product of its edge signs is positive — meaning either all friends (+,+,+) or two allies sharing an enemy (+,-,-).

The Balance Theorem proves that if every triangle in a network is balanced, the nodes can be partitioned into exactly two camps where within-camp edges are positive and between-camp edges are negative. This is because the all-negative triangle (-,-,-) is forbidden — mutual enemies must eventually resolve into a coalition.

Limitations:
- Strong balance forces exactly two camps, which is unrealistic for multi-polar geopolitics
- Weak balance (Davis, 1967) relaxes this: forbids only (+,+,−), allowing all-negative triangles and thus more than two camps
- Real networks are only approximately balanced (typically ~75-85% of triangles are balanced)
- The theory is static — it predicts equilibrium but not dynamics

---

## OQ7. "What information is lost when you project a bipartite network? Give an example."

**Model answer:**
When projecting a bipartite network (e.g., students × courses) onto one layer (student-student), you lose:
1. **The specific course** that generated each tie — you know two students share a course but not which one
2. **The course nodes themselves** — courses disappear from the model
3. **Tie strength granularity** — unless you use edge weights, you cannot distinguish pairs sharing 1 course from pairs sharing 3
4. **The bipartite structure** — you can no longer ask questions about course popularity, course bridging, or which course cancellation would disconnect the student cohort

Example: If Alice and Bob share 3 courses and Alice and Carol share 1, the unweighted projection shows Alice-Bob and Alice-Carol as identical edges. The weighted projection preserves the count but still loses which specific courses. You cannot answer "which course is the most central connector between social groups?" after projection.

---

## OQ8. "Explain the E-I index and how Schelling's model demonstrates that mild preferences create strong segregation."

**Model answer:**
The E-I index measures homophily: (E - I) / (E + I), where E = external edges and I = internal edges. Range from -1 (pure homophily) to +1 (pure heterophily). A strongly negative E-I index means people overwhelmingly connect within their group.

Schelling's model shows that even mild homophilic preferences (e.g., wanting just 30% same-type neighbours) produce strong global segregation. The mechanism is cascading dynamics: when one agent moves to satisfy their preference, they change the neighbourhood composition for others, triggering chain reactions. The macro-level segregation is far stronger than anyone's micro-level preference.

This is a profound insight: you cannot infer individual preferences from aggregate outcomes. A city that looks highly segregated might contain agents with only mild preferences. The dynamics amplify individual-level mildness into structural-level extremity.

---

## OQ9. "Explain the Bow-Tie structure of the web. Why are IN-component pages problematic for search engines?"

**Model answer:**
The web's directed structure forms a bow-tie when decomposed into strongly connected components:
- **SCC core:** mutually reachable pages (the "knot" of the bow-tie)
- **IN component:** pages that link into the SCC but receive no links from it
- **OUT component:** pages the SCC links to but which don't link back
- **Tendrils:** pages reachable from IN but not from SCC
- **Tubes:** paths from IN to OUT bypassing SCC

Search engines that crawl by following links starting from known hub pages (in the SCC) will discover the OUT component by following links forward. But IN-component pages are invisible to such crawlers — they link TO the SCC but nothing in the SCC links back. These are often new, poorly-linked, or niche pages that exist in isolation from the main web.

The practical consequence: a significant fraction of the web is unreachable by link-following crawlers, creating a visibility bias where established, well-linked pages dominate search results while newer or independent content remains hidden.

---

# PART C: QUICK-FIRE RECALL (memorise these)

## Handshaking Lemma
$$\sum_{v} \deg(v) = 2|E|$$

## Density
$$\text{density} = \frac{2|E|}{|V|(|V|-1)}$$

## Directed graph: in-degree and out-degree
$$\sum \text{in-deg}(v) = \sum \text{out-deg}(v) = |E|$$

## Bipartite graph
- Two disjoint node sets, edges only between sets (never within)
- Projection: connect nodes that share a neighbour in the other set

## Clustering Coefficient (local)
$$C_v = \frac{2 \times \text{triangles through } v}{k_v(k_v - 1)}$$

## Neighbourhood Overlap
$$O(u,v) = \frac{|N(u) \cap N(v)|}{|N(u) \cup N(v)|}$$

## Modularity
$$Q = \frac{1}{2m} \sum_c \left[ e_c - \frac{a_c^2}{4m} \right]$$

## E-I Index
$$\text{E-I} = \frac{E_{\text{external}} - I_{\text{internal}}}{E_{\text{external}} + I_{\text{internal}}}$$

## Small-World Index
$$\sigma = \frac{C / C_{\text{rand}}}{L / L_{\text{rand}}} > 3 \Rightarrow \text{small world}$$

## Average Path Length (random graph estimate)
$$d \approx \frac{\log N}{\log k}$$

## PageRank
$$PR(v) = \frac{1 - \alpha}{n} + \alpha \sum_{u \to v} \frac{PR(u)}{\text{outdeg}(u)}$$

## Betweenness Centrality
$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

## Closeness Centrality
$$C_C(v) = \frac{n - 1}{\sum_{u \neq v} d(v, u)}$$

---

# Priority Queue: Study This First

1. **Centrality equations** — know all 5 measures, when to use each, and compute by hand
2. **Small-world equation** — σ formula, d ≈ log N / log k, Watts-Strogatz sweep interpretation
3. **BFS** — trace by hand, compute distances, know it's for unweighted only
4. **Modularity** — formula, interpretation, resolution limit
5. **Balance theorem** — balanced triangle definition, two-camp partition
6. **Weak ties theorem** — STC condition, local bridges are weak ties
7. **Clustering coefficient** — formula, compute by hand
8. **Community detection** — Girvan-Newman vs greedy modularity vs hierarchical
9. **E-I index** — formula, interpretation
10. **Web bow-tie** — SCC/IN/OUT/tendril classification
