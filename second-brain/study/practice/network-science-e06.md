---
title: "Exercise Sheet 6 — Social Context"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-07-14
---

# Exercise Sheet 6 — Social Context

## Exercises

### 6.A Homophily and Measurement

**Exercise 6.A.1: Measuring Homophily by Hand**

A friendship network of 8 students: 4 study CS (C1–C4) and 4 study Business (B1–B4).
Edges: C1–C2, C1–C3, C2–C3, C3–C4, C4–B1, B1–B2, B2–B3, B3–B4.

1. Count edges within CS, within Business, and across departments.
2. Compute the E-I index: (E − I)/(E + I), ranging from −1 (pure homophily) to +1 (pure heterophily).
3. Is this network homophilic, heterophilic, or neutral with respect to department?
4. What would the E-I index be if ties formed randomly regardless of department?

> [!note]- Solution
> 1. **Edge counts:** Within CS: 4 (C1–C2, C1–C3, C2–C3, C3–C4). Within Business: 3 (B1–B2, B2–B3, B3–B4). Across: 1 (C4–B1). Total: 8.
> 2. **E-I index:** E = 1, I = 7. E−I = (1 − 7)/(1 + 7) = **−0.75**.
> 3. **Interpretation:** Strongly negative → strong homophily. Students overwhelmingly befriend others in the same department.
> 4. **Random baseline:** With two groups of 4, expected cross-group fraction is $1 - \frac{\binom{4}{2} + \binom{4}{2}}{\binom{8}{2}} = 1 - 12/28 \approx 0.57$. So 57% of edges should be cross-department under randomness; here only 12.5% are. The E-I index under random mixing would be ≈ **+0.14**.

---

**Exercise 6.A.2: Homophily vs. Confounding**

Using `nx.karate_club_graph()` with the "club" attribute as the group label:

1. Count within-faction and cross-faction edges.
2. Compute the E-I index for faction.
3. Compute the expected cross-faction edge fraction under random mixing.
4. Is the network homophilic? By how much relative to random?

> [!note]- Solution
> ```python
> import networkx as nx
>
> G = nx.karate_club_graph()
> factions = nx.get_node_attributes(G, "club")
>
> internal, external = 0, 0
> for u, v in G.edges():
>     if factions[u] == factions[v]:
>         internal += 1
>     else:
>         external += 1
>
> ei_index = (external - internal) / (external + internal)
> ```
>
> The E-I index is ≈ **−0.5** — strong homophily. The observed cross-faction fraction is far below the ≈ 0.50 expected from random mixing, confirming that faction membership strongly constrains friendship opportunities.

### 6.B Affiliation and Similarity

**Exercise 6.B.1: Three Closure Types**

Affiliation network: students S1, S2, S3, S4 and courses C1, C2, C3.
Enrolments: S1–C1, S1–C2, S2–C1, S3–C2, S3–C3, S4–C3.

1. Project onto the student layer (two students connected if they share a course).
2. Identify one example each of: (a) triadic closure, (b) focal closure, (c) membership closure.
3. If S2 joins C2, does this enable any new closure?
4. What information is lost when projecting?

> [!note]- Solution
> 1. **Projection:** S1–S2 (via C1), S1–S3 (via C2), S3–S4 (via C3).
> 2. **Closures:**
>    - (a) **Triadic:** (S2, S1, S3) is an open triad — predicts S2–S3.
>    - (b) **Focal:** S1 and S3 both attend C2 — the shared course is a focal context.
>    - (c) **Membership:** S4 is friends with S3 who attends C2 — predicts S4 may join C2.
> 3. **After S2 joins C2:** S2 now shares C2 with S1 and S3, forming S2–S3 via focal closure. This simultaneously closes the triadic closure identified above — both mechanisms operate.
> 4. **Information lost:** (a) which course generated each tie, (b) the course nodes themselves, (c) tie-strength weights (multiple shared courses indicate stronger ties).

---

**Exercise 6.B.2: Bipartite Projection in Python**

Implement the affiliation network from 6.B.1 in NetworkX and compute a weighted projection onto the student layer.

> [!note]- Solution
> ```python
> import networkx as nx
>
> B = nx.Graph()
> students = {"S1", "S2", "S3", "S4"}
> courses = {"C1", "C2", "C3"}
> B.add_nodes_from(students, bipartite=0)
> B.add_nodes_from(courses,   bipartite=1)
> B.add_edges_from([("S1","C1"),("S1","C2"),("S2","C1"),
>                    ("S3","C2"),("S3","C3"),("S4","C3")])
>
> P = nx.bipartite.weighted_projected_graph(B, students)
> # Weights = number of shared courses
> ```
>
> The student projection reveals hidden social structure created by shared course memberships. Edge weights record how many shared affiliations exist between any pair.

### 6.C Social Dynamics and Causal Inference

**Exercise 6.C.1: Distinguishing Social Forces**

For each scenario, state whether it is best explained by selection, socialization, or confounding:

1. Two students both like jazz, become friends, and a year later both discover classical music.
2. Two colleagues at a tech startup both use Python; their friendship forms day 1.
3. Students in the same dormitory become friends and all prefer the same pizza place.
4. A smoker quits after befriending non-smokers.

For each: what data (cross-sectional vs. longitudinal, observational vs. experimental) is needed to identify the mechanism?

> [!note]- Solution
> 1. **Jazz → friends → classical:** Primarily **socialization** — the shift happens after friendship. Confirming requires longitudinal data on preferences before and after friendship formation.
> 2. **Python users, day-1 friendship:** Primarily **confounding**. Both speak Python because of the workplace; friendship arose from co-presence. Comparing pre-hire language use would help isolate the confound.
> 3. **Dormitory pizza preference:** Mostly **socialization with confounding**. Proximity (dorm) is the confound; shared experiences create the convergent preference. Comparing same-floor vs. different-floor pairs partially isolates proximity from preference convergence.
> 4. **Smoker quits:** Classic **socialization** (peer influence), but selection is plausible — the smoker may already have wanted to quit and selected a friendlier environment. Random assignment of smokers to friend groups would identify the mechanism, but raises ethical issues.

---

**Exercise 6.C.2: Designing a Study**

You want to know whether students in the same study group become more similar in performance (socialization) or whether similar students form study groups together (selection).

1. What cross-sectional data would you collect?
2. What longitudinal data is needed to separate the mechanisms?
3. What would an ideal experimental design look like?
4. What would you observe if both mechanisms operate?

> [!note]- Solution
> 1. **Cross-sectional:** Group membership and current GPA. You'd find that group members have more similar GPAs than non-members — but cannot distinguish selection from socialization.
> 2. **Longitudinal:** Measure GPA before groups form, record group formation, measure GPA after. Selection: groups whose pre-formation similarity is higher form more often. Socialization: GPA similarity increases more within groups than between random pairs.
> 3. **Experimental:** Randomly assign students to groups, eliminating selection. Any convergence is socialization. Ethical concerns: forced groupings; randomized encouragement designs are a softer alternative.
> 4. **Both mechanisms:** Pre-formation, groups already show above-average similarity (selection). Post-formation, similarity increases further (socialization). Initially-similar groups may converge more, indicating selection-by-socialization interaction.

### 6.D Spatial Segregation

**Exercise 6.D.1: Schelling Model Analysis**

In Schelling's model, agents on a grid prefer at least k of 8 neighbours to be the same type. Dissatisfied agents move.

1. If k = 1, do you expect strong segregation? Why?
2. If k = 5 (majority), what outcome do you predict?
3. Why is it surprising that mild preferences (k = 3 or k = 4) can still produce strong global segregation?
4. How does this connect to homophily? What is the "network" in Schelling's model?

> [!note]- Solution
> 1. **k = 1:** No strong segregation expected. With only 1 of 8 same-type neighbours needed, almost everyone is satisfied regardless of composition. The grid stays roughly mixed.
> 2. **k = 5 (majority):** Strong segregation. Agents need a majority of neighbours to be the same type — this creates cascading moves that separate the grid into distinct clusters.
> 3. **Mild preferences → strong segregation:** This is Schelling's key insight. Individual preferences are mild (e.g., just 30–40% same-type neighbours), but the *dynamics* amplify them. When one agent moves, it changes the neighbourhood composition for others, triggering chain reactions. The macro-level segregation is far stronger than anyone's micro-level preference.
> 4. **Connection to homophily:** Schelling's model is spatial homophily — agents prefer similar neighbours. The "network" is the spatial grid itself: edges connect adjacent cells. The model shows that homophilic preferences, even weak ones, produce emergent structural segregation through feedback dynamics.

---

**Exercise 6.D.2: Schelling Simulation**

Implement a 1D Schelling model: agents in a line; each needs at least threshold fraction of left+right neighbours to be the same type. Unhappy agents swap with random unhappy agents of the opposite type.

1. Implement and run for 100 steps.
2. Visualise initial and final states.
3. Vary threshold from 0.1 to 0.9 and plot average run-length at convergence.
4. At what threshold does strong segregation emerge?

> [!note]- Solution
> ```python
> import random
> import matplotlib.pyplot as plt
>
> def schelling_1d(n=200, threshold=0.3, steps=100):
>     """1D Schelling model. Types: 0, 1, empty (-1)."""
>     # Initialise: ~45% type 0, ~45% type 1, ~10% empty
>     agents = [0] * (n // 3) + [1] * (n // 3) + [-1] * (n - 2 * (n // 3))
>     random.shuffle(agents)
>
>     def satisfied(i):
>         if agents[i] == -1:
>             return True
>         neighbours = []
>         if i > 0 and agents[i-1] != -1:
>             neighbours.append(agents[i-1])
>         if i < n-1 and agents[i+1] != -1:
>             neighbours.append(agents[i+1])
>         if not neighbours:
>             return True
>         same = sum(1 for x in neighbours if x == agents[i])
>         return same / len(neighbours) >= threshold
>
>     for step in range(steps):
>         unhappy = [i for i in range(n) if not satisfied(i)]
>         if not unhappy:
>             break
>         random.shuffle(unhappy)
>         # Swap pairs of unhappy agents of opposite types
>         for i in range(0, len(unhappy) - 1, 2):
>             a, b = unhappy[i], unhappy[i+1]
>             if agents[a] != agents[b] and agents[a] != -1 and agents[b] != -1:
>                 agents[a], agents[b] = agents[b], agents[a]
>
>     return agents
>
> # Run and visualise
> initial = [0] * 67 + [1] * 67 + [-1] * 66
> random.shuffle(initial)
> final = schelling_1d(threshold=0.3)
>
> fig, axes = plt.subplots(2, 1, figsize=(12, 4))
> axes[0].imshow([initial], aspect='auto', cmap='RdBu')
> axes[0].set_title("Initial state")
> axes[1].imshow([final], aspect='auto', cmap='RdBu')
> axes[1].set_title("After 100 steps (threshold=0.3)")
> plt.tight_layout()
> plt.show()
> ```
>
> **Varying threshold:** Run for thresholds 0.1 to 0.9, measure the average run-length (consecutive same-type agents) at convergence:
>
> ```python
> import numpy as np
>
> def avg_run_length(agents):
>     runs = []
>     current_type = None
>     current_len = 0
>     for a in agents:
>         if a == -1:
>             if current_len > 0:
>                 runs.append(current_len)
>             current_len = 0
>             current_type = None
>         elif a == current_type:
>             current_len += 1
>         else:
>             if current_len > 0:
>                 runs.append(current_len)
>             current_type = a
>             current_len = 1
>     if current_len > 0:
>         runs.append(current_len)
>     return np.mean(runs) if runs else 0
>
> thresholds = np.arange(0.1, 1.0, 0.1)
> avg_runs = []
> for t in thresholds:
>     runs = [avg_run_length(schelling_1d(threshold=t)) for _ in range(20)]
>     avg_runs.append(np.mean(runs))
>
> plt.plot(thresholds, avg_runs, 'o-')
> plt.xlabel("Threshold")
> plt.ylabel("Average run length")
> plt.title("Segregation vs. tolerance threshold")
> plt.show()
> ```
>
> **At what threshold does strong segregation emerge?** Typically around **threshold ≈ 0.3–0.4**. Below this, the grid remains mostly mixed. Above it, run lengths increase sharply — even a 30% same-type preference produces visually striking clusters.


---

## Related Resources

### 📖 Network Science L06: Structural Balance
- Lecture topic: [[network-science-l06]]

**Key concepts covered:**
- [[balance-theorem]]
- [[weak-structural-balance]]
- [[frustration-index]]
- [[signed-laplacian]]
- [[signed-graphs]]
- [[balanced-triads]]
- [[structural-balance-theory]]
- [[k-balance]]
- [[cycle-criterion]]
- [[schelling-segregation-model]]
- [[homophily]]
- [[algebraic-connectivity]]
