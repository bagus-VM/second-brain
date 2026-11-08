---
title: "Network Science — Exam Battle Plan"
tags: [exam-prep, network-science, battle-plan, semester-1]
course: "Network Science"
exam_date: 2026-07-28
days_remaining: 8
status: current
last_updated: 2026-07-19
---

# Network Science — Exam Battle Plan

> *"You clearly don't know who you're talking to, so let me clue you in. I am the one who studies."*

**Exam:** July 28, 2026 — 8 days from July 20
**Format:** Open questions + structured questions (from exercises AND lectures)
**Scope:** Lectures 1–8, Exercise Sheets 1–8 (L09 is NOT in scope)
**Confirmed by professor:** centrality equations, small-world equation, graph search algorithms

---

## 1. Vault Intelligence Report

You have two existing prep files — use them:
- **[[network-science-exercise-prep]]** — NetworkX code reference, key calculations, exercise priorities
- **[[exam-prep-network-science-2026-07-28]]** — 752-line comprehensive prep: structured questions with equations, 9 open questions with model answers, quick-fire recall section, priority queue

**Those two files are your primary weapons. This battle plan is your field commander.**

---

## 2. Coverage Map — What You Know vs. What You Don't

### Legend
- 🟢 **STRONG** — Topic page + concept pages + flashcards + practice problems
- 🟡 **MEDIUM** — Topic page + some concept pages, gaps in flashcards or practice
- 🔴 **WEAK** — Topic page exists but missing concept pages, no flashcards, or thin practice

### Lecture-by-Lecture Assessment

| Lecture | Topic | Vault Pages | Flashcards | Practice | Rating |
|---------|-------|-------------|------------|----------|--------|
| **L01** Introduction | Topic page ✓ | 8 concept pages (network-intro, network-examples, edge-types, centrality, community-structure, connected-component, network-effects, network-diffusion) | e01 ✓ | e01 ✓ | 🟢 |
| **L02** Graph Theory | Topic page ✓ | 10+ concept pages (graph-fundamentals, directed/undirected, weighted, bipartite, sparse/dense/random, graph-representations, random-graphs) | e02 ✓ | e02 ✓ | 🟢 |
| **L03** Strong/Weak Ties | Topic page ✓ | concept pages (triadic-closure, clustering-coefficient, neighborhood-overlap, bridges, weak-ties-hypothesis, social-capital, structural-holes, strong-triadic-closure) | e03 ✓ | e03 ✓ | 🟢 |
| **L04** Communities | Topic page ✓ | 10+ concept pages (modularity, modularity-resolution-limit, girvan-newman, louvain, leiden, community-detection-overview, graph-partitioning, graph-partitioning-cut-spectral, embedding-based-community-detection, product-space-network) | e04 + e05 ✓ | e04 + e05 ✓ | 🟢 |
| **L05** Social Context | Topic page ✓ | 7 concept pages (homophily, affiliation-networks, network-autocorrelation, schelling-segregation-model, echo-chambers, selection-vs-socialization) | e06 ✓ | e06 ✓ | 🟢 |
| **L06** Structural Balance | Topic page ✓ | 6 concept pages (signed-networks, balance-theorem, weak-structural-balance, structural-balance-theory, balanced-triads, k-balance) | e07 ✓ | e07 ✓ | 🟡 |
| **L07** Small-World | Topic page ✓ | 7 concept pages (small-world-property, watts-strogatz-model, scale-free-networks, preferential-attachment, hierarchical-navigable-small-world, web-bow-tie-structure) | ❌ MISSING | e08 ✓ | 🟡 |
| **L08** Network Dynamics | Topic page ✓ | 8 concept pages (sir-model-network-epidemics, basic-reproduction-number-r0, scale-free-epidemic-threshold-vanishes, complex-contagion, threshold-cascades, centola-2010-experiment, temporal-networks, network-diffusion) | ❌ MISSING | e06 partial | 🟡 |

### Critical Gaps

1. **🔴 No flashcards for L07 (Small-World)** — σ formula, Watts-Strogatz sweep, Kleinberg, scale-free, preferential attachment
2. **🔴 No flashcards for L08 (Network Dynamics)** — SIR model, R₀, epidemic threshold, complex contagion, threshold cascades
3. **🟡 L06 missing concept pages:** frustration-index, signed-laplacian, cycle-criterion, algebraic-connectivity — referenced in topic page but no standalone vault pages
4. **🟡 L09 (Node Representations) excluded from exam** — but concepts (node2vec, GNNs, DeepWalk) may appear as bonus or in open questions about embeddings

---

## 3. Priority Queue — What to Study First

Sorted by: **(likelihood on exam) × (current weakness)**

| Rank | Topic | Why This Priority | Study Time |
|------|-------|-------------------|------------|
| 1 | **Centrality equations** | Professor confirmed it. 6 measures, each with formula + when to use. You need to compute by hand AND write NetworkX code. | 3h |
| 2 | **Small-world equation + Watts-Strogatz** | Professor confirmed it. σ formula, d ≈ log N / log k, W-S sweep interpretation. No flashcards exist — build them NOW. | 2.5h |
| 3 | **BFS + graph search** | Professor confirmed it. Trace by hand, know complexity, know it's for unweighted only. | 2h |
| 4 | **Modularity Q** | Formula, hand computation, resolution limit, compare detection algorithms. | 2h |
| 5 | **Structural balance** | Balanced triangle definition, two-camp partition, strong vs. weak balance. Formulas + conceptual. | 2h |
| 6 | **SIR model + R₀** | Epidemic threshold, scale-free vanishing threshold, simple vs. complex contagion. No flashcards — build them. | 2h |
| 7 | **Clustering coefficient + neighborhood overlap** | Hand computation, understand what they measure, connection to weak ties. | 1.5h |
| 8 | **Community detection algorithms** | Girvan-Newman vs. greedy modularity vs. Louvain vs. Leiden. Compare strategy, complexity, strengths. | 1.5h |
| 9 | **Homophily + E-I index + Schelling** | Formula, interpretation, selection vs. socialization. | 1.5h |
| 10 | **Web bow-tie + temporal networks** | SCC/IN/OUT classification, time-respecting paths. Conceptual + diagram. | 1h |

**Total: ~19 hours of focused study across 7 days (July 20–26)**

---

## 4. Day-by-Day Battle Schedule

### Day 1 — Monday, July 20: **Centrality + BFS (The Foundation)**

**Morning (3h): Centrality Deep Dive**
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S1 (all centrality measures)
- [ ] Hand-compute all 6 measures on the 6-node example graph
- [ ] Write NetworkX code for each measure from memory
- [ ] Create flashcards: formula + when to use + complexity for each measure

**Afternoon (2h): Graph Search**
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S2 (BFS, Dijkstra, graph properties)
- [ ] Hand-trace BFS on 3 different graphs (from e02)
- [ ] Know: BFS → unweighted, Dijkstra → weighted non-negative, Bellman-Ford → negative weights
- [ ] Practice: Euler's theorem (degree parity conditions)

**Evening (1h): Flashcard Review**
- [ ] Run through e01–e04 flashcards
- [ ] Flag anything you can't answer in under 10 seconds

---

### Day 2 — Tuesday, July 21: **Strong/Weak Ties + Clustering (The Social Layer)**

**Morning (2.5h): Triadic Closure + Clustering**
- [ ] Read [[network-science-l03]] topic page
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S3
- [ ] Hand-compute clustering coefficient for 3 different nodes
- [ ] Hand-compute neighborhood overlap for 3 different edges
- [ ] Know: STC condition, why local bridges must be weak ties

**Afternoon (2h): Weak Ties Theorem + Applications**
- [ ] Explain the Weak Ties Theorem out loud (Socratic test)
- [ ] Know: Granovetter's job study, Onnela et al. cell phone experiment, Bakshy et al. Facebook study
- [ ] Create flashcards for L03 key concepts that aren't covered by e03 flashcards

**Evening (1h): e03 + e04 Flashcard Drill**
- [ ] Run through e03 and e04 flashcards
- [ ] Focus on: clustering coefficient computation, centrality comparisons

---

### Day 3 — Wednesday, July 22: **Community Detection + Modularity (The Group Layer)**

**Morning (3h): Modularity Deep Dive**
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S4
- [ ] Read [[modularity]] and [[modularity-resolution-limit]] concept pages
- [ ] Hand-compute Q for a 2-community and 3-community partition
- [ ] Know: Q = 0 means random, Q = 1 means perfect, real networks Q ∈ [0.3, 0.7]
- [ ] Know: resolution limit — why modularity can't detect small communities

**Afternoon (2h): Detection Algorithms**
- [ ] Compare: Girvan-Newman (top-down, edge betweenness), Greedy Modularity (bottom-up merge), Louvain (local moves + aggregation), Leiden (Louvain + refinement)
- [ ] Know: Girvan-Newman returns an iterator — `next(gn)` gives 2 communities
- [ ] Know: hierarchical clustering — dendrogram, cut at largest gap
- [ ] Practice: Zachary's karate club — what algorithms find, what they miss

**Evening (1h): e05 Flashcard Drill**
- [ ] Run through e05 flashcards
- [ ] Focus on: modularity computation, algorithm comparison

---

### Day 4 — Thursday, July 23: **Small-World Networks (The Shortcut Layer)**

**Morning (3h): Small-World Equation + Watts-Strogatz**
- [ ] Read [[network-science-l07]] topic page
- [ ] Read [[small-world-property]], [[watts-strogatz-model]], [[scale-free-networks]], [[preferential-attachment]]
- [ ] Know: σ = (C/C_rand)/(L/L_rand), σ >> 1 means small-world
- [ ] Know: d ≈ log N / log k estimation
- [ ] Know: Watts-Strogatz sweep — p ∈ [0.01, 0.1] is the sweet spot, L drops sharply, C stays high
- [ ] Know: W-S does NOT produce scale-free networks (narrow degree distribution)
- [ ] **CREATE FLASHCARDS** — no e07 flashcards exist. Build 15–20 cards covering:
  - σ formula and interpretation
  - d ≈ log N / log k computation
  - Watts-Strogatz model mechanics
  - Kleinberg's navigability theorem (r = d)
  - Scale-free networks: P(k) ~ k^(-γ), hubs, robustness vs. targeted attack
  - Preferential attachment (Barabási-Albert model)
  - Web bow-tie structure (SCC/IN/OUT/tendrils)

**Afternoon (2h): Scale-Free + Bow-Tie**
- [ ] Read [[scale-free-networks]] concept page
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S7 (small-world section)
- [ ] Know: scale-free epidemic threshold vanishes (T_c → 0 when γ ≤ 3)
- [ ] Know: bow-tie — SCC (~28%), IN, OUT, tendrils, tubes
- [ ] Practice: estimate d for N = 10^9, k = 200 → d ≈ 3.9

**Evening (1h): Self-Test**
- [ ] Without looking: write all formulas from Days 1–4
- [ ] Check against [[exam-prep-network-science-2026-07-28]] §C (quick-fire recall)

---

### Day 5 — Friday, July 24: **Structural Balance + Signed Networks (The Sign Layer)**

**Morning (2.5h): Balance Theory Deep Dive**
- [ ] Read [[network-science-l06]] topic page
- [ ] Read [[signed-networks]], [[balance-theorem]], [[weak-structural-balance]], [[balanced-triads]]
- [ ] Know: balanced triangle = even number of negative edges (0 or 2)
- [ ] Know: four triangle types and which are balanced
- [ ] Know: Balance Theorem → partition into ≤ 2 camps (strong) or k camps (weak)
- [ ] Know: frustration index (NP-hard), signed Laplacian (λ₁ = 0 ⟺ balanced)
- [ ] Know: empirical evidence — (+, +, −) massively underrepresented (~8% vs ~37.5% expected)

**Afternoon (2h): Applications + Edge Cases**
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S6 (structural balance section)
- [ ] Practice: determine if a signed graph is balanced by checking all triangles
- [ ] Practice: partition a balanced graph into camps
- [ ] Know: cycle criterion for incomplete graphs
- [ ] Know: strong vs. weak balance difference

**Evening (1h): e07 Flashcard Drill**
- [ ] Run through e07 flashcards
- [ ] Focus on: balanced triangle identification, camp partitioning

---

### Day 6 — Saturday, July 25: **Network Dynamics + SIR Model (The Spread Layer)**

**Morning (3h): SIR Model + Epidemic Threshold**
- [ ] Read [[network-science-l08]] topic page
- [ ] Read [[sir-model-network-epidemics]], [[basic-reproduction-number-r0]], [[scale-free-epidemic-threshold-vanishes]]
- [ ] Know: R₀ = (β/γ) × ⟨k⟩, epidemic if R₀ > 1
- [ ] Know: T_c ≈ ⟨k⟩ / (⟨k²⟩ − ⟨k⟩) for heterogeneous networks
- [ ] Know: scale-free (γ ≤ 3) → T_c → 0 (no finite threshold)
- [ ] Know: SIR (immunity) vs. SIS (no immunity) difference
- [ ] **CREATE FLASHCARDS** — no e08 flashcards exist. Build 15–20 cards covering:
  - SIR model mechanics (S → I → R)
  - R₀ formula and interpretation
  - Epidemic threshold condition
  - Scale-free vanishing threshold
  - Simple vs. complex contagion
  - Threshold cascades
  - Centola 2010 experiment (clustered > random for complex contagion)
  - Temporal networks + time-respecting paths
  - Weak tie paradox (helps simple, blocks complex contagion)

**Afternoon (2h): Complex Contagion + Temporal Networks**
- [ ] Read [[complex-contagion]], [[threshold-cascades]], [[centola-2010-experiment]], [[temporal-networks]]
- [ ] Know: complex contagion needs fraction q of neighbors adopted
- [ ] Know: Centola — behavior spread faster in clustered networks (54%) than random (38%)
- [ ] Know: temporal networks — phantom paths, time-respecting paths
- [ ] Know: the six gaps of the course (computational, causal, structural, navigational, process-structure, temporal)

**Evening (1h): Homophily + E-I Index Quick Review**
- [ ] Read [[exam-prep-network-science-2026-07-28]] §S5
- [ ] Know: E-I index formula, range, interpretation
- [ ] Know: Schelling model — mild preferences → strong segregation
- [ ] Know: affiliation networks — triadic, focal, membership closure

---

### Day 7 — Sunday, July 26: **Mock Exam + Final Review**

**Morning (3h): Mock Exam**
- [ ] Complete the Professor White Mock Exam below WITHOUT looking at notes
- [ ] Time yourself: 3 hours, no breaks
- [ ] After finishing, check answers against the model answers

**Afternoon (2h): Gap Attack**
- [ ] Review mock exam results — what did you get wrong?
- [ ] Re-read the relevant vault pages for weak areas
- [ ] Run through ALL flashcards (e01–e07 + your new L07/L08 cards)
- [ ] Re-compute any formulas you got wrong by hand

**Evening (1h): Formula Sheet**
- [ ] Write out ALL formulas from memory on a blank sheet:
  - Density, degree centrality, closeness, harmonic, betweenness, eigenvector, PageRank
  - Clustering coefficient, neighborhood overlap
  - Modularity Q
  - E-I index
  - Small-world index σ, d ≈ log N / log k
  - R₀ = (β/γ) × ⟨k⟩
  - Balance: even negative edges = balanced
- [ ] Check against [[exam-prep-network-science-2026-07-28]] §C

---

### Day 8 — Monday, July 27: **REST DAY**

> *"The night before, you rest. You've done the work. Trust the vault."*

- [ ] Light review only — flip through flashcards for 30 minutes MAX
- [ ] No new material. No panic studying.
- [ ] Sleep well. Eat well. Arrive early.
- [ ] Bring: calculator, pen, student ID

---

## 5. Professor White Mock Exam

> *3 hours. No notes. No looking things up. Show your work.*

---

### Part A: Structured Questions (60 points)

#### A1. Centrality (15 points)

Consider the following graph:

```
1 — 2 — 3 — 4
|       |       |
5 — 6 — 7 — 8
```

Edges: (1,2), (2,3), (3,4), (1,5), (3,7), (4,8), (5,6), (6,7), (7,8)

**(a)** Compute degree centrality C_D for all 8 nodes. (3 pts)

**(b)** Compute closeness centrality C_C for node 3. Show all distances. (4 pts)

**(c)** Compute betweenness centrality C_B for node 3. List all shortest paths that pass through it. (5 pts)

**(d)** Which node has the highest betweenness? Why? Explain what this means in terms of network role. (3 pts)

> **Model Answer:**
> **(a)** n=8, divide by 7.
> Node 1: deg=2 → 0.286 | Node 2: deg=2 → 0.286 | Node 3: deg=3 → 0.429
> Node 4: deg=2 → 0.286 | Node 5: deg=2 → 0.286 | Node 6: deg=2 → 0.286
> Node 7: deg=3 → 0.429 | Node 8: deg=2 → 0.286
> Nodes 3 and 7 tie for highest degree centrality.
>
> **(b)** Distances from node 3: d(3,1)=2, d(3,2)=1, d(3,4)=1, d(3,5)=3, d(3,6)=2, d(3,7)=1, d(3,8)=2. Sum=12. C_C(3) = 7/12 ≈ 0.583.
>
> **(c)** Node 3 sits on shortest paths between {1,2,5,6} and {4,8}. Key paths through 3:
> - 1→3→4 (also 1→2→3→4, but 1→2→3 is length 2 vs 1→3 is length 2, so multiple shortest paths)
> - Actually: 1→2→3→4, 5→6→7→3→4 (no, 5→6→7→8→4 is shorter), etc.
> - The key bridge role: node 3 connects the left cluster {1,2,5,6} to the right cluster {4,8} via edges (2,3) and (3,4). Node 7 also bridges via (3,7) and (7,8).
> - Betweenness requires counting all s-t shortest paths through node 3 for all s≠3≠t.
>
> **(d)** Node 3 (or node 7) has highest betweenness because it sits on the critical paths connecting the left and right halves of the graph. This is a brokerage role — it bridges two otherwise loosely connected clusters.

---

#### A2. Small-World Networks (15 points)

**(a)** A collaboration network has N = 10^6 researchers and average degree k = 50. Estimate the average path length using d ≈ log N / log k. (3 pts)

**(b)** The actual measured average path length is L = 3.2. The average clustering coefficient is C = 0.72. A random graph with the same N and k has C_rand = 0.00005 and L_rand = 2.8. Compute the small-world index σ. Is this a small-world network? (5 pts)

**(c)** Explain the Watts-Strogatz model. What happens to C(p)/C(0) and L(p)/L(0) as p increases from 0 to 1? Why is the range p ∈ [0.01, 0.1] special? (4 pts)

**(d)** Why does the Watts-Strogatz model NOT produce scale-free networks? What model does? (3 pts)

> **Model Answer:**
> **(a)** d ≈ log(10^6)/log(50) = 6/1.7 ≈ 3.5 hops.
>
> **(b)** σ = (C/C_rand)/(L/L_rand) = (0.72/0.00005)/(3.2/2.8) = 14400/1.143 ≈ 12598. Since σ >> 3, YES, this is a small-world network. The clustering is enormously higher than random while the path length is comparable.
>
> **(c)** W-S starts with a ring lattice (p=0): high C, long L. As p increases slightly (p ≈ 0.01), L drops sharply — a few random shortcuts collapse global distances. C stays near C(0) until moderate p (gradual decay). The sweet spot p ∈ [0.01, 0.1] is where L ≈ L_rand but C >> C_rand — the small-world regime. At p=1, the graph is fully random: low C, short L.
>
> **(d)** W-S preserves the narrow degree distribution of the initial lattice (all nodes start with degree k, rewiring doesn't change degree much). It produces a Poisson-like degree distribution, not a power law. The Barabási-Albert model (preferential attachment: new nodes connect preferentially to high-degree nodes) produces scale-free networks with P(k) ~ k^(-γ).

---

#### A3. Modularity + Community Detection (15 points)

**(a)** Compute modularity Q for the following partition of a graph with m=10 edges:
- Community A: {1, 2, 3} with internal edges e_A = 4, degree sum a_A = 12
- Community B: {4, 5, 6} with internal edges e_B = 3, degree sum a_B = 8

Show your work. (5 pts)

**(b)** Compare Girvan-Newman, greedy modularity maximization, and the Louvain algorithm. For each: state the strategy, complexity, and one strength/weakness. (6 pts)

**(c)** What is the resolution limit of modularity? Give a concrete example of when it fails. (4 pts)

> **Model Answer:**
> **(a)** Q = (1/2m) Σ_c [e_c - a_c²/(4m)]
> Q = (1/20) × [(4 - 144/40) + (3 - 64/40)]
> Q = (1/20) × [(4 - 3.6) + (3 - 1.6)]
> Q = (1/20) × [0.4 + 1.4]
> Q = 1.8/20 = 0.09
>
> **(b)**
> | Algorithm | Strategy | Complexity | Strength | Weakness |
> |-----------|----------|------------|----------|----------|
> | Girvan-Newman | Top-down: iteratively remove highest-betweenness edges | O(n·m²) | Finds hierarchical structure, interpretable | Slow on large graphs |
> | Greedy Modularity | Bottom-up: merge communities that maximize ΔQ | O(n log²n) | Fast, simple | May over-merge due to resolution limit |
> | Louvain | Local moves + super-node aggregation, iterative | O(n log n) | Very fast, good quality | Can get stuck in local optima, may produce disconnected communities |
>
> **(c)** The resolution limit states that modularity cannot detect communities smaller than a scale √(2m). In a large network, two small but distinct communities may be merged because the expected edge count a²/(4m) becomes non-trivial relative to the actual internal edges. Example: in the karate club graph (34 nodes, 78 edges), greedy modularity often finds 3-4 communities instead of the known 2 factions — it splits the larger faction into sub-clusters because the smaller faction is "too small" to stand alone against the expected random baseline.

---

#### A4. Structural Balance (15 points)

**(a)** For each triangle below, determine if it is balanced under strong balance theory:
- (+, +, +)
- (+, +, -)
- (+, -, -)
- (-, -, -)

Explain the social meaning of each. (4 pts)

**(b)** A complete signed graph has 5 nodes with the following edges:
```
A—B: +, A—C: +, A—D: -, A—E: -
B—C: +, B—D: -, B—E: -
C—D: -, C—E: -
D—E: +
```
Is this graph balanced? If so, partition it into camps. (5 pts)

**(c)** Explain the difference between strong balance and weak balance. How many camps does each allow? Who proposed each version? (3 pts)

**(d)** What is the frustration index? Why is it NP-hard? What is the polynomial-time alternative? (3 pts)

> **Model Answer:**
> **(a)**
> - (+, +, +): BALANCED — three mutual friends, most stable
> - (+, +, -): NOT BALANCED — two friends who share a mutual enemy creates tension
> - (+, -, -): BALANCED — two allies sharing a common enemy
> - (-, -, -): NOT BALANCED (under strong balance) — three mutual enemies, no coalition
>
> **(b)** Check all triangles:
> - {A,B,C}: +, +, + → balanced ✓
> - {A,B,D}: +, -, - → balanced ✓
> - {A,B,E}: +, -, - → balanced ✓
> - {A,C,D}: +, -, - → balanced ✓
> - {A,C,E}: +, -, - → balanced ✓
> - {A,D,E}: -, -, + → balanced ✓
> - {B,C,D}: +, -, - → balanced ✓
> - {B,C,E}: +, -, - → balanced ✓
> - {B,D,E}: -, -, + → balanced ✓
> - {C,D,E}: -, -, + → balanced ✓
> All balanced → YES.
> Partition: Camp 1 = {A, B, C} (all positive within), Camp 2 = {D, E} (positive within). All between-camp edges are negative.
>
> **(c)** Strong balance (Cartwright & Harary 1956): only (+,+,+) and (+,-,-) are balanced. Forces exactly 2 camps. Weak balance (Davis 1967): also permits (-,-,-). Only (+,+,−) remains forbidden. Allows k ≥ 1 camps (multipolar).
>
> **(d)** The frustration index F(G,σ) = minimum number of edge sign flips needed to achieve balance. It's NP-hard because finding the minimum set of edges to flip is equivalent to MAX-CUT (Sintos & Tsaparas 2014). The polynomial-time alternative is the signed Laplacian: L_σ = D - A_σ, where λ₁(L_σ) = 0 if and only if the graph is balanced. This gives a spectral test in O(|E|·d) time.

---

### Part B: Open Questions (40 points)

#### OQ1. (10 points)
*"Explain the Weak Ties Theorem. What is the Strong Triadic Closure condition? Why must every local bridge be a weak tie under STC? Give a real-world example."*

> **Model Answer:**
> The Strong Triadic Closure (STC) condition states: if a node A has strong ties to both B and C, then B and C must be connected (the triad must close). This is a formalization of triadic closure applied to typed (strong/weak) edges.
>
> Under STC, consider a local bridge — an edge (A,B) where A and B have no common neighbors. If (A,B) were a strong tie, then for any other strong tie of A (say A–C), STC would require B and C to be connected. But if B and C are connected, then (A,B) is no longer a local bridge (A and B now share neighbor C). Contradiction. Therefore, the local bridge must be a weak tie.
>
> Real-world example: Granovetter's job study. People hear about job opportunities through rarely-seen acquaintances, not close friends. Close friends share your social world (high neighborhood overlap), so they know what you know. Acquaintances bridge to different social circles (low overlap), providing non-redundant information. The weak tie that connects you to a different community is structurally a local bridge — and under STC, it must be weak.

---

#### OQ2. (10 points)
*"What is the small-world phenomenon? Explain why it is surprising that real networks can have both high clustering and short paths. How does the Watts-Strogatz model resolve this paradox?"*

> **Model Answer:**
> The small-world phenomenon is that most pairs in large networks are connected by surprisingly short paths — typically logarithmic in network size (d ≈ log N / log k). Milgram's 1967 experiment showed ~6 hops between random Americans despite 200 million people.
>
> The paradox: a regular lattice has high clustering (friends of friends are friends) but long paths (d ~ N/2k). A random graph has short paths (d ~ log N / log k) but low clustering (C ~ k/N). Real social networks have BOTH properties simultaneously — which seems contradictory.
>
> The Watts-Strogatz model resolves this. Start with a ring lattice (n nodes, each connected to k nearest neighbors). Rewire each edge with probability p. At p=0: lattice (high C, long L). At p=1: random graph (low C, short L). The key insight: a tiny rewiring fraction (p ≈ 0.01-0.1) collapses L to near-random levels while barely affecting C. A few random "shortcuts" create express routes across the network, but the local clustering structure remains intact because only a small fraction of edges are rewired. The small-world regime is this narrow window where L ≈ L_rand but C >> C_rand.

---

#### OQ3. (10 points)
*"Explain the difference between simple contagion and complex contagion. Why do weak ties help one but hinder the other? Reference the Centola experiment."*

> **Model Answer:**
> Simple contagion: a single contact with an active node suffices to transmit (e.g., disease, rumor). The SIR model captures this — each S-I edge transmits with probability β. Weak ties and bridges accelerate spread because they carry the contagion to new communities. This is Granovetter's insight applied to dynamics.
>
> Complex contagion: a node adopts only when a fraction q of its neighbors have adopted (e.g., behavior change, technology adoption, norm shifting). Social reinforcement is needed — one adopter isn't enough. Weak ties and bridges HURT here because they typically have only one adopter on the other side, which is below the threshold q. The bridge carries insufficient reinforcement.
>
> This is the weak tie paradox of contagion: the same structural feature (weak ties as bridges) that accelerates information spread actually blocks behavior adoption.
>
> Centola (2010) empirically confirmed this. He created both clustered networks and random networks with the same degree and diameter. A health behavior spread faster in the clustered network (54% adoption) than the random network (38%). The reason: in clustered networks, an adopter's neighbors are also neighbors of each other, so when one adopts, multiple neighbors see the adoption simultaneously, pushing them past the threshold q. In random networks, adopters are scattered, and each neighbor sees adoption from only one source — insufficient for reinforcement.

---

#### OQ4. (10 points)
*"Explain the E-I index and Schelling's segregation model. How do mild individual preferences produce extreme global segregation? What does this tell us about inferring preferences from outcomes?"*

> **Model Answer:**
> The E-I index measures homophily: E-I = (E_external - I_internal) / (E_external + I_internal). Range from -1 (pure homophily, all ties within group) to +1 (pure heterophily, all ties between groups). 0 = neutral mixing.
>
> Schelling's model places agents on a grid (or network). Each agent has a threshold τ: if fewer than τ fraction of neighbors are the same type, the agent moves to a new location. Even mild preferences (τ ≈ 1/3) produce sharp global segregation.
>
> The mechanism is cascading dynamics. When one dissatisfied agent moves, they change the neighborhood composition for remaining agents, potentially triggering new dissatisfactions. This chain reaction amplifies individual-level mildness into structural-level extremity. The macro-level segregation is far stronger than anyone's micro-level preference.
>
> The profound implication: you CANNOT infer individual preferences from aggregate outcomes. A city that looks highly segregated might contain agents with only mild preferences. Conversely, moderate aggregate mixing might coexist with strong individual preferences if the dynamics haven't converged. This is an identification problem — the same outcome can be generated by very different individual-level parameters. Recommendation algorithms act as automated Schelling rewirers, accelerating this amplification.

---

## 6. Formula Quick-Reference Card

*Write this out from memory on exam day morning. If you can't, you're not ready.*

| Formula | What It Measures |
|---------|------------------|
| density = 2\|E\| / (\|V\|(\|V\|-1)) | Edge saturation |
| Σ deg(v) = 2\|E\| | Handshaking lemma |
| C_D(v) = deg(v) / (n-1) | Degree centrality |
| C_C(v) = (n-1) / Σ d(v,u) | Closeness centrality |
| H(v) = Σ 1/d(v,u) | Harmonic centrality |
| C_B(v) = Σ σ_st(v)/σ_st | Betweenness centrality |
| Ax = λx | Eigenvector centrality |
| PR(v) = (1-α)/n + α Σ PR(u)/outdeg(u) | PageRank |
| C_v = 2T / (k(k-1)) | Local clustering coefficient |
| O(u,v) = \|N(u)∩N(v)\| / \|N(u)∪N(v)\| | Neighborhood overlap |
| Q = (1/2m) Σ [e_c - a_c²/(4m)] | Modularity |
| E-I = (E_ext - I_int) / (E_ext + I_int) | E-I index |
| σ = (C/C_rand) / (L/L_rand) | Small-world index |
| d ≈ log N / log k | Average path length estimate |
| R₀ = (β/γ) × ⟨k⟩ | Basic reproduction number |
| T_c ≈ ⟨k⟩ / (⟨k²⟩ - ⟨k⟩) | Epidemic threshold |

---

## 7. NetworkX Code — Know These Cold

*From [[network-science-exercise-prep]]. Drill until you can write these without looking.*

```python
# MUST KNOW: Graph creation, centrality, clustering, community detection
import networkx as nx

# Centrality
nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.closeness_centrality(G)
nx.eigenvector_centrality(G)
nx.pagerank(G, alpha=0.85)

# Clustering
nx.clustering(G)
nx.average_clustering(G)
nx.transitivity(G)

# Community detection
nx.community.greedy_modularity_communities(G)
nx.community.modularity(G, communities)
nx.community.girvan_newman(G)

# Graph properties
nx.density(G)
nx.is_connected(G)
nx.connected_components(G)
nx.shortest_path_length(G, source, target)
nx.average_shortest_path_length(G)

# Special graphs
nx.karate_club_graph()
nx.erdos_renyi_graph(n, p)
nx.barabasi_albert_graph(n, m)
```

---

## 8. The Six Gaps of the Course

*Know these. They're a unifying theme that shows deep understanding.*

| Lecture | Gap Type | Core Tension |
|---------|----------|--------------|
| L03–L04 | Computational | NP-hard ideals (MaxSTC, modularity max) vs. polynomial proxies |
| L05 | Causal | Snapshot cannot distinguish selection, socialization, confounding |
| L06 | Structural | Balance theorem requires complete graphs; real graphs are sparse |
| L07 | Navigational | Short paths exist but local actors can't find them (Kleinberg) |
| L08 | Process-structure | Same network, different outcomes for different spreading rules |
| L08 (temporal) | Temporal | Static aggregation creates phantom paths, hides bottlenecks |

---

## 9. Exam Day Checklist

- [ ] Can you compute all 6 centrality measures by hand?
- [ ] Can you compute clustering coefficient and neighborhood overlap by hand?
- [ ] Can you compute modularity Q by hand?
- [ ] Can you estimate d ≈ log N / log k?
- [ ] Can you compute σ (small-world index)?
- [ ] Can you determine if a signed graph is balanced?
- [ ] Can you partition a balanced graph into camps?
- [ ] Can you compute R₀ and determine if R₀ > 1?
- [ ] Can you trace BFS on a graph and give the layers?
- [ ] Can you write NetworkX code for all key operations?
- [ ] Can you explain the six gaps of the course?
- [ ] Can you explain weak ties theorem, small-world paradox, simple vs. complex contagion?

---

## 10. Connections to Existing Vault

### Related Prep Files
- [[network-science-exercise-prep]] — NetworkX reference + calculations + exercise priorities
- [[exam-prep-network-science-2026-07-28]] — Full structured questions + 9 open questions + quick-fire recall

### Lecture Topic Pages
- [[network-science-l01]] through [[network-science-l09]] — Full lecture notes with concept maps

### Key Concept Pages (read these for deep understanding)
- [[modularity]], [[modularity-resolution-limit]] — Community detection foundation
- [[signed-networks]], [[balance-theorem]], [[weak-structural-balance]] — Structural balance
- [[sir-model-network-epidemics]], [[basic-reproduction-number-r0]] — Network dynamics
- [[scale-free-networks]], [[preferential-attachment]] — Network families
- [[small-world-property]], [[watts-strogatz-model]] — Small-world theory
- [[temporal-networks]] — Time-respecting paths
- [[complex-contagion]], [[centola-2010-experiment]] — Behavior spreading

### Flashcard Decks
- [[network-science-e01-flashcards]] through [[network-science-e07-flashcards]]
- **⚠️ MISSING: L07 and L08 flashcards — build them on Days 4 and 6**

---

## 11. Open Questions — What You Don't Know Yet

These are the gaps Professor White is tracking. Resolve them before the exam.

1. ~~Are there flashcards for L07/L08?~~ → NO. Build them on Days 4 and 6.
2. Will the exam provide NetworkX documentation, or do you need to memorize function signatures?
3. Is L09 (Node Representations / Graph Embeddings) in scope? → Likely NOT per scope confirmation (L1–L8 only), but node2vec/GNNs could appear as bonus.
4. What other calculations might appear beyond the exercise sheets? (assortativity, degree correlation)
5. How detailed should the complexity analysis be? O() notation or exact step counts?

---

> *"This is what you don't know yet. These are your weak points. That's where we start."*
>
> *— Professor White*
