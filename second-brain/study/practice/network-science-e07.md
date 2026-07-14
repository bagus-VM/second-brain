---
title: "Exercise Sheet 7 — Structural Balance"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-07-14
---

# Exercise Sheet 7 — Structural Balance

## Exercises

### 7.A Triadic Balance Theory

**Exercise 7.A.1: Classifying Signed Triangles**

For each triangle, determine if balanced (B) or unbalanced (U). A triangle is balanced if the product of its edge signs is positive (even number of negative edges).

1. (+, +, +) — all positive
2. (+, +, −) — two positive, one negative
3. (+, −, −) — one positive, two negative
4. (−, −, −) — all negative

Which pattern is most stable, and which is "socially unstable"?

> [!note]- Solution
> A triangle is balanced iff the product of edge signs is positive (0 or 2 negatives).
> 1. **(+,+,+):** Balanced. Three mutual friends — most stable.
> 2. **(+,+,−):** Unbalanced. Classic "two of my friends hate each other" tension.
> 3. **(−,−,+):** Balanced. Two allies sharing a common enemy.
> 4. **(−,−,−):** Unbalanced. Three mutual enemies — no coalition possible.
>
> The (+,+,−) pattern is the most common source of social tension; (+,+,+) is the most stable.

### 7.B Weak Balance

**Exercise 7.B.1: Strong vs Weak Balance**

For the two triangles (A, B, C all positive; D, E, F all negative) connected by a negative edge C–D:

1. Is A, B, C balanced under strong balance? Under weak balance?
2. Is D, E, F balanced under strong balance? Under weak balance?
3. What does the global partition look like under each?
4. In international relations, what does an all-negative triangle represent?

> [!note]- Solution
> 1. **A, B, C — all positive:** Balanced under both strong and weak balance.
> 2. **D, E, F — all negative:** Unbalanced under strong balance (product is −1). Weak balance forbids only (+,+,−) triangles, so all-negative is balanced (weakly).
> 3. **Partition:**
>    - Strong balance: impossible without resolving D, E, F (one edge must flip).
>    - Weak balance: allows more than two camps, e.g. {A, B, C}, {D}, {E}, {F} — three mutual enemies form three separate factions.
> 4. **Three mutually hostile countries.** Strong balance theory predicts an alliance forms (resolving to two camps). Weak balance treats multi-polar rivalry as stable.

---

**Exercise 7.B.2: Finding Camps in a Signed Network**

Graph: 1, 2, 3 mutually friends (+); 4, 5, 6 mutually friends (+); all cross-group edges are negative.

1. Check every triangle for balance.
2. Find the two-camp partition.
3. Verify within-group edges are positive, between-group negative.
4. Add a "rogue" positive edge 1–4. Which triangles become unbalanced?

> [!note]- Solution
> ```python
> import networkx as nx
> from itertools import combinations
>
> G = nx.Graph()
> G.add_edges_from([(1,2),(1,3),(2,3),(4,5),(4,6),(5,6)], sign=1)
> G.add_edges_from([(1,4),(2,5),(3,6),(1,5),(2,6),(3,4)], sign=-1)
>
> def triangle_sign(G, t):
>     a, b, c = t
>     return G[a][b]["sign"] * G[b][c]["sign"] * G[a][c]["sign"]
>
> triangles = [t for t in combinations(G.nodes, 3)
>              if all(G.has_edge(u, v) for u, v in combinations(t, 2))]
> balanced = sum(1 for t in triangles if triangle_sign(G, t) > 0)
> ```
>
> The partition {1, 2, 3} vs. {4, 5, 6} makes every triangle balanced. Adding the rogue edge 1–4 creates unbalanced triangles such as (1, 2, 4) and (1, 3, 4) — each becomes (+,+,−). The structural tension typically resolves either by breaking the rogue tie or by realigning groups.

### 7.C Relaxed Balance and Applications

**Exercise 7.C.1: WWI Alliance Network**

Allies: France, Britain, Russia (mutually +); Central Powers: Germany, Austria-Hungary (mutually +); all Allies–Central edges negative.

1. Is this network perfectly balanced? Identify any unbalanced triangles.
2. Does it match the two-camp Balance Theorem?
3. What if a new country joins with positive ties to both camps?
4. Italy switched from Germany to the Allies in 1915 — what does balance theory predict?

> [!note]- Solution
> 1. All within-camp triangles are (+,+,+). Cross-camp triangles like (France, Germany, Britain) are (−,−,+) — balanced. The network is **perfectly balanced**.
> 2. **Yes** — exactly the two-camp realisation predicted by the Balance Theorem.
> 3. A new country with positive ties to both camps creates (+,+,−) triangles immediately — unstable. Balance theory predicts the country must eventually choose a side.
> 4. Italy initially had a positive tie to Germany while Allies–Germany was negative — straddling two hostile camps. The (+,+,−) tension is exactly what balance theory predicts must resolve, and the historical switch in 1915 eliminated the unbalanced triangles.

---

**Exercise 7.C.2: Approximate Balance in Real Networks**

Using the karate club graph, sign edges by faction (within = +, cross = −).

1. Count balanced vs unbalanced triangles.
2. What fraction of triangles are balanced?
3. Remove cross-faction edges in order of how many unbalanced triangles they participate in. After removing the top 5, how does the fraction change?
4. Plot fraction-balanced vs edges-removed.

> [!note]- Solution
> ```python
> import networkx as nx
> from itertools import combinations
>
> G = nx.karate_club_graph()
> factions = nx.get_node_attributes(G, "club")
> for u, v in G.edges():
>     G[u][v]["sign"] = 1 if factions[u] == factions[v] else -1
>
> def fraction_balanced(G):
>     triangles = [t for t in combinations(G.nodes, 3)
>                  if all(G.has_edge(u, v) for u, v in combinations(t, 2))]
>     if not triangles:
>         return 1.0
>     pos = sum(1 for (a, b, c) in triangles
>               if G[a][b]["sign"] * G[b][c]["sign"] * G[a][c]["sign"] > 0)
>     return pos / len(triangles)
> ```
>
> Real networks are typically approximately balanced (often ≥ 75%). Removing high-impact negative edges — those in many unbalanced triangles — improves the global balance fraction sharply, mirroring how social groups resolve tension by severing conflicting ties.

## Wrap-Up

- Triangle sign products give a one-line balance test
- The Balance Theorem turns a local rule into a global two-camp partition
- Weak balance permits more than two camps and is often more realistic
- Real networks are rarely perfectly balanced — approximate balance is the typical regime

## Related Lectures
- [[network-science-l06]]
- [[balance-theorem]]
- [[structural-balance-theory]]
- [[balanced-triads]]
- [[weak-structural-balance]]
- [[signed-networks]]
- [[frustration-index]]
- [[cycle-criterion]]
- [[signed-laplacian]]
