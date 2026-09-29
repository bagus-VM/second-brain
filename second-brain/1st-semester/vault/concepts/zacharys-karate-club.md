---
title: "Zachary's Karate Club"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[modularity]]", "[[community-detection-overview]]"]
---

## One-line Summary
Zachary's karate club is the canonical benchmark for community detection: a 34-member club that split into two factions after a conflict, recoverable from friendship graph topology alone.

## Core Intuition
Wayne Zachary (1977) observed a university karate club for two years. A conflict arose between the instructor (Mr. Hi) and the chief administrator (Officer). The club eventually split, with each member following one or the other. The friendship graph (34 nodes, 78 edges) plus the ground-truth split became the standard test for community detection algorithms.

## Formal Definition / Statement
- **Nodes**: 34 club members
- **Edges**: 78 friendship ties observed during the study period
- **Ground truth**: two factions — Mr. Hi's group and Officer's group
- **Benchmark question**: can an algorithm recover the two factions from the graph alone?

**Typical algorithm results:**
| Method | Result |
|--------|--------|
| Girvan–Newman | Recovers 2 factions with ~1 misclassified node |
| Louvain/Leiden | Recovers 2 factions; typically finds 4 sub-groups at max Q |
| Exact max-modularity | Finds 4 sub-groups nested inside the 2 factions |

The ~1 misclassified node genuinely sat on the boundary — even Zachary noted it was a close call.

## Key Properties / Complexity
- Small enough for exact computation (34 nodes)
- The ground-truth split is **not** the modularity optimum — exact max-Q gives 4 communities, not 2
- The misclassified node is structurally meaningful (boundary position)
- Demonstrates that community detection can recover real social structure from topology alone
- Also demonstrates the limits: resolution limit, binary ground truth, static snapshot

## Common Pitfalls
- **Resolution limit** (Fortunato & Barthélemy 2007): the exact max-Q partition has 4 communities, not 2 — the algorithm answers "which partition maximizes Q", not "which matches the real factions"
- **Binary ground truth**: Zachary recorded faction membership but not preference strength, uncertainty, or possible neutral groups
- **Static snapshot**: friendships were recorded at one time — dynamics of influence and shifting are invisible
- Treating the karate club as "proof" that community detection works — it's one success case with known blind spots

## Connections
- [[modularity]] — the resolution limit is most clearly demonstrated on this graph
- [[girvan-newman-algorithm]] — GN recovers the 2-faction split with ~1 error
- [[louvain-algorithm]] — Louvain finds 4 sub-groups at max Q
- [[leiden-algorithm]] — similar to Louvain on this small graph
- [[community-detection-overview]] — the empirical validation anchor for the whole field
- [[network-science-l03]] — the weak-tie structure (cross-faction edges) connects to L03
- [[betweenness-centrality]] — edge betweenness drives Girvan-Newman
- [[network-science-l04]] — lecture overview

## Open Questions
- Are there better benchmarks than Zachary's for modern community detection?
- How would temporal/longitudinal data change the "ground truth"?
- Can we quantify the uncertainty in the ground-truth labels themselves?

## Worked Example

*To be filled.*
