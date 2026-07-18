---
title: "Network Science E02 — Graph Theory Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 2

## Flashcards

> [!question]- What does the right model depend on when studying a network system?
> [!answer]- The right model depends on the question being asked. Using a model at the wrong level of abstraction either gives the wrong answer or hides the relevant information. For example, ARPANET modelled at router-level reveals physical cable vulnerabilities; at institution-level it reveals reachability between organisations.

> [!question]- What information is irreversibly lost when projecting a bipartite graph onto a single node type?
> [!answer]- The specific connecting entities are lost. For example, projecting a student-course bipartite graph onto students loses which specific courses connect two students. Also lost is the degree of connection (unless edge weights are added). Every projection trades detail for simplicity.

> [!question]- What is the handshaking lemma and what does it mean?
> [!answer]- The handshaking lemma states that Σ deg(v) = 2|E|. The sum of all vertex degrees equals twice the number of edges. This is because every edge contributes exactly 2 to the total degree count (one for each endpoint). It also implies the number of odd-degree vertices must be even.

> [!question]- What is the difference between an Eulerian circuit and an Eulerian path?
> [!answer]- An Eulerian circuit visits every edge exactly once and returns to the start — it requires ALL vertices to have even degree. An Eulerian path visits every edge exactly once but does not return — it requires EXACTLY TWO vertices to have odd degree (the start and end). Königsberg had 4 odd-degree vertices, so it had neither.

> [!question]- Why does BFS not give shortest paths when edges have weights?
> [!answer]- BFS counts hops (unweighted edges), not accumulated weights. A path with fewer hops may have higher total weight than a path with more hops but lower weights. For weighted shortest paths, use Dijkstra's algorithm instead.


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
