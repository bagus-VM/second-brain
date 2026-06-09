---
title: "Network Science E05 — Community Detection Flashcards"
tags:
  - flashcards
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 5

## Flashcards

> [!question]- What is modularity Q and what do its values mean?
> [!answer]- Modularity Q measures whether communities have more internal edges than expected by chance. Q = 0 means no detectable community structure (no better than random). Q = 1 means perfect modularity (theoretically unachievable in practice). Typical real networks with clear community structure have Q ∈ [0.3, 0.7]. Random community assignments yield Q ≈ 0.

> [!question]- How does the Girvan-Newman algorithm work and why does edge 3–4 have the highest betweenness in the two-triangle graph?
> [!answer]- Girvan-Newman iteratively removes the edge with highest betweenness centrality, recomputing after each removal. Edge 3–4 (the bridge between two triangles) has betweenness = |L| × |R| = 3×3 = 9 because every path from {1,2,3} to {4,5,6} must cross it — there is no alternative route. It is the unique cut edge.

> [!question]- What is the difference between greedy modularity and Girvan-Newman for community detection?
> [!answer]- Greedy modularity (bottom-up) merges communities to maximise Q, but can over-partition due to the resolution limit (typically finds 3–4 communities in the karate club). Girvan-Newman (top-down) iteratively removes bridge edges, cleanly isolating hubs (~97% accuracy on 2-faction split). Girvan-Newman is more computationally expensive but gives cleaner hierarchical structure.

> [!question]- What does the height of a merge in a dendrogram represent?
> [!answer]- The height represents dissimilarity (distance) between the two clusters being merged. A merge at low height means very similar clusters were joined. A merge at high height indicates dissimilar clusters being forced together. The "right" number of clusters is found by looking for the largest gap in merge heights.

> [!question]- What is the difference between direct-link similarity and neighbourhood-overlap similarity in hierarchical clustering?
> [!answer]- Direct-link similarity measures whether two nodes share an edge — it merges nearby nodes but ignores global structure. Neighbourhood-overlap similarity = |N(u)∩N(v)|/|N(u)∪N(v)| measures shared neighbours even without a direct link. It is more robust to missing edges and better captures social equivalence.
