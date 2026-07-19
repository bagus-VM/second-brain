---
title: "Exercise Sheet 2 — Graph Theory"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Exercise Sheet 2 — Graph Theory

## Exercises

### 2.A Properties of Networks

**Exercise 2.A.1: The Five Modeling Questions**

A hospital wants to study how infections spread among patients and staff. Answer the five modeling questions from the lecture for this system:

1. **Nodes:** What should each node represent? Is there more than one natural choice?
2. **Edges:** What should an edge represent? (Hint: an edge should encode a transmission-relevant relationship.)
3. **Direction:** Is the relation directed or undirected? Does it depend on how you define the edge?
4. **Weight:** Should edges have weights? If so, what should the weight encode?
5. **Time:** Does this network change over time? Does the order of events matter for your analysis?

Finally: what does your modeling choice reveal, and what does it hide?

---

**Exercise 2.A.2: Two Meanings of the Same Network**

The ARPANET had two distinct kinds of nodes: universities/labs and routers.

- **Model R (router-level):** nodes are routers; edges are physical cables.
- **Model U (institution-level):** nodes are institutions; an edge connects two institutions if at least one router-level path exists between them.

1. For a path A → B in Model R, what does it mean in the physical system?
2. For the same path in Model U, what does it represent? How do the two models differ in what they express?
3. If your question is "Can MIT reach Stanford in at most 3 hops?", which model do you use and why?
4. If your question is "Which physical cable, if cut, would disconnect the ARPANET?", which model do you use and why?
5. What general principle do these questions illustrate about modeling choices?

---

**Exercise 2.A.3: Bipartite vs Projected Networks**

Consider a university course enrollment system. Two researchers model it differently:

- **Model A:** A bipartite graph G_A = (S, C, E) where S = students, C = courses, and (s, c) ∈ E means student s is enrolled in course c.
- **Model B:** A projected graph G_B = (S, E') where two students are connected if they share at least one course.

1. Draw a small example: 3 students (Alice, Bob, Carol) and 3 courses (Math, CS, Physics). Alice takes Math and CS; Bob takes CS and Physics; Carol takes Math.
2. Draw both G_A and G_B for this example.
3. What does G_A let you analyse that G_B does not? Give a concrete example question.
4. What does G_B let you analyse that G_A does not? Give a concrete example question.
5. What information is irreversibly lost in the projection from G_A to G_B?

### 2.B Representing Graphs

**Exercise 2.B.1: From Picture to Formal Notation**

Consider an undirected graph with five nodes A, B, C, D, E and edges A–B, A–C, B–C, B–D, D–E.

1. Write the formal set notation: V = …, E = …
2. Draw the adjacency matrix (nodes in alphabetical order).
3. Write the adjacency list as a Python dictionary.
4. Compute |V| and |E|.
5. What is the degree of each node? Verify the handshaking lemma: Σ deg(v) = 2|E|.
6. Now suppose B–D becomes directed (B → D). What changes?

---

**Exercise 2.B.2: Graph Representations in Python**

Work with the graph from Exercise B.1 using NetworkX:

```python
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A","B"),("A","C"),("B","C"),("B","D"),("D","E")])
```

1. Print the adjacency matrix using `nx.to_numpy_array`.
2. Print the degree of each node. Does it match your hand calculation?
3. Compute and print the density of the graph. What does density = 1 mean? What does density = 0 mean?
4. Add a directed version: `DG = nx.DiGraph()`. Print in-degree and out-degree of B and D.
5. Bonus: Plot both graphs side by side with matplotlib.

---

**Exercise 2.B.3: Reading a Network Diagram**

Build the Zachary karate club graph with NetworkX:

```python
import networkx as nx
import matplotlib.pyplot as plt
G = nx.karate_club_graph()
```

1. How many nodes and edges does the network have?
2. What is the average degree? What does this mean for the "average member"?
3. Are there any isolated nodes (degree 0)? What would an isolated node mean socially?
4. Plot the network. Can you visually identify the two factions that the club split into?

### 2.C Paths and Cycles

**Exercise 2.C.1: Walks, Paths, and Cycles**

Consider the undirected graph with edges A–B, B–C, C–D, D–A, A–C. Classify each sequence as a walk, path, cycle, or none (edge doesn't exist). Justify each answer.

| Sequence | Classification | Reason |
|---|---|---|
| A, B, C, A | ? | ? |
| A, C, D, A | ? | ? |
| A, B, C, D, A | ? | ? |
| A, B, A, C | ? | ? |
| A, B, C, D, C | ? | ? |
| A, E | ? | ? |

Then: what is the diameter of this graph?

---

**Exercise 2.C.2: The Königsberg Bridge Problem**

The Königsberg bridges problem (Euler, 1736): can you walk through the city crossing each of the seven bridges exactly once and return to your starting point?

The city has four land masses: North bank (N), South bank (S), Island (I), East bank (E). Bridges: N–I (×2), S–I (×2), N–E (×1), S–E (×1), I–E (×1).

1. Model this as a multigraph G = (V, E). Write down V and E.
2. Write the degree of each node.
3. Euler proved that an Eulerian circuit exists iff every vertex has even degree. Does Königsberg satisfy this condition?
4. An Eulerian path exists iff exactly two vertices have odd degree. Does Königsberg have an Eulerian path?
5. What does this tell us?

---

**Exercise 2.C.3: Shortest Paths with NetworkX**

Work with a small synthetic ARPANET version:

```python
import networkx as nx
arpa = nx.Graph()
arpa.add_edges_from([
    ("UCLA", "SRI"), ("UCLA", "UCSB"), ("UCLA", "UTAH"),
    ("SRI", "UTAH"), ("SRI", "BBN"), ("UCSB", "SRI"),
    ("UTAH", "MIT"), ("BBN", "HARVARD"), ("BBN", "MIT"),
    ("MIT", "HARVARD"),
])
```

1. Plot the network using `nx.draw_spring()`.
2. Find the shortest path from "UCLA" to "HARVARD". Print path and length.
3. Compute eccentricities, diameter, and radius.
4. Which node is the center? What does this mean structurally?
5. Remove "BBN" and recompute the diameter. What changed and why?

### 2.D Breadth-First Search (BFS)

**Exercise 2.D.1: BFS by Hand — Layer Tracing**

Run BFS starting from node 1 on the following undirected graph:
Edges: 1–2, 1–3, 2–4, 2–5, 3–6, 4–7, 5–7, 6–8

1. Fill in the BFS discovery table with layer and parent for each node.
2. Draw the BFS tree.
3. What is d(1, 7) and d(1, 8)? Is there more than one shortest path to 7?
4. If we add weights w(2–4) = 10, w(5–7) = 1, does BFS still give shortest paths?

---

**Exercise 2.D.2: Implementing BFS and Computing Distances**

Implement BFS from scratch and use it to answer structural questions about the Zachary karate club network:

```python
from collections import deque
import networkx as nx
def bfs_distances(graph, source):
    """Return a dict {node: shortest-path distance from source}."""
    dist = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        # --- your code here ---
    return dist
G = nx.karate_club_graph()
adj = {n: list(G.neighbors(n)) for n in G.nodes()}
```

1. Complete `bfs_distances`. Verify it against `nx.single_source_shortest_path_length`.
2. Use it to find the eccentricity of node 0 (the instructor "Mr. Hi").
3. What fraction of the network is reachable within 2 hops from node 0?
4. Repeat for node 33 (the administrator "Officer"). Compare eccentricities and reachable fractions. What does the difference tell you?

### 2.E Connectivity and Components

**Exercise 2.E.1: Components and Connectivity by Hand**

Consider a directed graph with nodes 1, 2, 3, 4, 5, 6 and directed edges:
1 → 2, 2 → 3, 3 → 1, 4 → 3, 5 → 6, 6 → 5

1. List all weakly connected components (ignoring direction).
2. List all strongly connected components (following directed paths).
3. Node 4 is a "source" node. Explain what this means for information flow. Can node 4 receive information from nodes 1, 2, or 3?
4. If you removed edge 3 → 1, how would the SCCs change?

---

**Exercise 2.E.2: Giant Components in Practice**

Use NetworkX to investigate what happens to connectivity when we progressively remove nodes from the karate club network:

```python
import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.karate_club_graph()
```

1. What fraction of nodes belong to the giant component of the original network?
2. Random failure: repeatedly remove a randomly chosen node and record the size of the largest component after each removal. Plot the result.
3. Targeted attack: repeatedly remove the node with the highest current degree. Plot on the same axes.
4. Which strategy destroys the giant component faster? Why?

---

## Solutions

### 2.A.1 — The Five Modeling Questions

> [!note]- Solution
> 1. **Nodes:** Most natural: individual patients and staff. Alternative: hospital wards or departments (coarser model). Granularity determines visible patterns.
> 2. **Edges:** "Spent time in the same room", "direct physical contact", or "shared a care procedure". A stricter definition gives a sparser, accurate graph; a looser one gives a denser graph risking overestimation.
> 3. **Direction:** Depends on edge definition. "Direct contact" is symmetric (undirected). "Given treatment" is asymmetric (directed).
> 4. **Weights:** Yes — duration of contact (minutes) naturally encodes transmission probability.
> 5. **Time:** Strongly yes. A patient is infectious only during a specific window. A static snapshot misattributes risk; a temporal graph (edges with timestamps) is necessary.
>
> **Reveals:** Who could have transmitted the infection to whom, and via what chain.
> **Hides:** Airborne transmission over distance, environmental contamination, and asymptomatic carriers.

### 2.A.2 — Two Meanings of the Same Network

> [!note]- Solution
> 1. **Model R path:** A sequence of physical cable segments connecting two specific routers. Path length = number of cable hops.
> 2. **Model U path:** A sequence of institutions reachable from each other. This hides router-level detail — one Model U "hop" may correspond to dozens of physical cable segments.
> 3. **MIT → Stanford, 3 hops:** Use Model U. The question is about institutional reachability, not physical routing.
> 4. **Critical cable:** Use Model R. You need physical resolution. In Model U the cable is invisible.
> 5. **General principle:** The right model depends on the question. Using a model at the wrong level of abstraction either gives the wrong answer or hides the relevant information.

### 2.A.3 — Bipartite vs Projected Networks

> [!note]- Solution
> - G_A reveals: Course popularity, bridging courses. Q: "Which course cancellation disconnects the cohort?"
> - G_B reveals: Social clusters, student isolation. Q: "Are there isolated student groups?"
> - Information lost: The specific courses connecting two students; degree of connection (unless edge weights are added). **Lesson: Every projection trades detail for simplicity.**

### 2.B.1 — From Picture to Formal Notation

> [!note]- Solution
> 1. V = {A, B, C, D, E}, E = {{A,B}, {A,C}, {B,C}, {B,D}, {D,E}}
> 2. Adjacency matrix (order A, B, C, D, E):
>    ```
>    M = [[0,1,1,0,0],
>         [1,0,1,1,0],
>         [1,1,0,0,0],
>         [0,1,0,0,1],
>         [0,0,0,1,0]]
>    ```
> 3. Adjacency list: `{"A": ["B","C"], "B": ["A","C","D"], "C": ["A","B"], "D": ["B","E"], "E": ["D"]}`
> 4. |V| = 5, |E| = 5.
> 5. Degrees: deg(A)=2, deg(B)=3, deg(C)=2, deg(D)=2, deg(E)=1. Σ deg = 10 = 2 × 5 ✓
> 6. Directed B → D: Matrix loses symmetry. B's out-deg=3, in-deg=2; D's out-deg=1, in-deg=1. Lemma: Σ in-deg = Σ out-deg = |E|.

### 2.B.2 — Graph Representations in Python

> [!note]- Solution
> ```python
> nodes = sorted(G.nodes())
> print("Adjacency matrix:\n", nx.to_numpy_array(G, nodelist=nodes))
> print("Degrees:", dict(G.degree()))
> # {'A': 2, 'B': 3, 'C': 2, 'D': 2, 'E': 1}
> print(f"Density: {nx.density(G):.3f}")  # 0.500
> ```
> Density = 1 → complete graph; density = 0 → no edges. The directed version loses matrix symmetry; B's high out-degree reflects its role as a "broadcaster".

### 2.B.3 — Reading a Network Diagram

> [!note]- Solution
> - **34 nodes, 78 edges:** small but dense.
> - **Average degree ≈ 4.6:** each member is friends with 4–5 others.
> - **No isolated nodes:** every member has at least one friend — connected.
> - **Visual factions:** the spring layout reveals two clusters; high-degree hubs ("Mr. Hi" and "Officer") are structurally central.

### 2.C.1 — Walks, Paths, and Cycles

> [!note]- Solution
> | Sequence | Classification | Reason |
> |---|---|---|
> | A, B, C, A | Cycle | All intermediate nodes distinct; all edges exist |
> | A, C, D, A | Cycle | Edges A–C, C–D, D–A all exist |
> | A, B, C, D, A | Cycle | All 4 edges exist; returns to A |
> | A, B, A, C | Walk (not path) | A visited twice — not simple |
> | A, B, C, D, C | Walk (not path) | C appears twice |
> | A, E | None | Node E does not exist |
>
> **Diameter = 2.**

### 2.C.2 — The Königsberg Bridge Problem

> [!note]- Solution
> 1. V = {N, S, I, E}. E = {N–I, N–I, S–I, S–I, N–E, S–E, I–E} (7 edges).
> 2. deg(N)=3, deg(S)=3, deg(I)=5, deg(E)=3
> 3. **Eulerian circuit:** All degrees must be even. Here all four are odd → **no Eulerian circuit.**
> 4. **Eulerian path:** Requires exactly 2 odd-degree vertices. All four are odd → **no Eulerian path either.**
> 5. **Lesson:** Euler's result reduces a physical puzzle to a parity check. The actual shape of the river and bridge positions are irrelevant. This is the power of graph abstraction.

### 2.C.3 — Shortest Paths with NetworkX

> [!note]- Solution
> ```python
> path = nx.shortest_path(arpa, "UCLA", "HARVARD")
> # ['UCLA', 'SRI', 'BBN', 'HARVARD']
> print(f"Diameter: {nx.diameter(arpa)}")  # 4
> print(f"Radius: {nx.radius(arpa)}")      # 2
> center = nx.center(arpa)
> ```
> **Interpretation:** The center node(s) minimise the maximum detour any message must take. Removing BBN increases the diameter because it was a primary relay bridging the East Coast and West Coast clusters.

### 2.D.1 — BFS by Hand

> [!note]- Solution
> | Node | Layer | Parent |
> |---|---|---|
> | 1 | 0 | — |
> | 2, 3 | 1 | 1 |
> | 4, 5 | 2 | 2 |
> | 6 | 2 | 3 |
> | 7, 8 | 3 | 4 or 5; 6 |
>
> Node 7 can have either 4 or 5 as parent depending on tie-breakers, showing more than one shortest path.
> d(1,7) = 3, d(1,8) = 3.
> **Weighted BFS:** No. BFS counts hops, not weights. Use Dijkstra for weighted shortest paths.

### 2.D.2 — Implementing BFS

> [!note]- Solution
> ```python
> def bfs_distances(graph, source):
>     dist = {source: 0}
>     queue = deque([source])
>     while queue:
>         node = queue.popleft()
>         for neighbor in graph.get(node, []):
>             if neighbor not in dist:
>                 dist[neighbor] = dist[node] + 1
>                 queue.append(neighbor)
>     return dist
> ```
> Eccentricity of Mr. Hi (0): ≈ 4. Reaches more nodes in 2 hops than node 33. **Structural insight:** Node 0's central position is reflected in lower BFS distances. The two factions are anchored by these hubs (0 and 33), but Mr. Hi is often more "central" in the unweighted friendship graph.

### 2.E.1 — Components and Connectivity by Hand

> [!note]- Solution
> 1. **Weakly connected components:** {1, 2, 3, 4} and {5, 6}
> 2. **Strongly connected components:** {1, 2, 3} (cycle 1→2→3→1), {4} (reaches 1,2,3 via 4→3 but no path back), {5, 6} (cycle 5→6→5)
> 3. **Node 4 as source:** Information flows out of 4 into 1, 2, 3 but nothing flows back. Node 4 cannot receive information from 1, 2, or 3. It acts as a "broadcaster" influencing the main cluster without being influenced in return.
> 4. **Removing 3→1:** The cycle breaks. Each of 1, 2, 3 becomes its own trivial SCC. Dependency flow: 1 → 2 → 3 alongside 4 → 3. Node 3 becomes an absolute sink.

### 2.E.2 — Giant Components in Practice

> [!note]- Solution
> **Robustness vs fragility:** Hub-based networks are resilient to random failure (most nodes are peripheral) but fragile under targeted attack (hubs are critical). Removing the instructor (0) or administrator (33) disrupts connectivity far more than removing an average student. This principle explains why internet backbones and social hubs are high-value targets.


---

## Related Resources

### 📖 Network Science L02 — Graph Theory
- Lecture topic: [[network-science-l02]]

**Key concepts covered:**
- [[graph-fundamentals]]
- [[directed-and-undirected-graphs]]
- [[weighted-graphs]]
- [[bipartite-graphs]]
- [[sparse-dense-and-random-graphs]]
- [[graph-representations]]
- [[neighbourhood-and-degree]]
- [[paths-walks-and-cycles]]
- [[shortest-path-and-diameter]]
- [[eulerian-path-and-circuit]]
- [[breadth-first-search]]
- [[depth-first-search]]
- [[dijkstras-algorithm]]
- [[connectivity-and-components]]
- [[directed-connectivity]]
