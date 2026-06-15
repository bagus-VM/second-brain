---
title: "E-I Index"
tags: [concept, network-science, semester-1, homophily, ei-index, measurement]
course: "Network Science"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[homophily]]", "[[affiliation-networks]]"]
---

## One-line Summary
The E-I index is a single-number measure of homophily on a labeled network, defined as (E − I) / (E + I) where E is the number of cross-group (external) edges and I is the number of within-group (internal) edges — ranging from −1 (pure homophily) through 0 (neutral / random) to +1 (pure heterophily).

## Core Intuition
When you label every node with a group attribute (e.g., department, faction, gender, age bracket), you can ask: do edges tend to land *inside* groups or *across* groups? The E-I index compresses this into one signed scalar.

The sign encodes *direction* (more external = positive = heterophily; more internal = negative = homophily), and the magnitude encodes *strength* (how far from random mixing). The endpoints are clean: -1 means every edge is inside a group, +1 means every edge is across groups, 0 means the counts are equal.

## Formal Definition / Statement

For a graph G = (V, E) with a node attribute that assigns each node to a group:

- **E** = number of edges (u, v) where group(u) ≠ group(v) (external / cross-group)
- **I** = number of edges (u, v) where group(u) = group(v) (internal / within-group)

The **E-I index** is:

    EI = (E − I) / (E + I)

Notes on the formula:
- E + I = |E| (every edge is either external or internal; for undirected simple graphs).
- Range: [-1, +1]. Reached only when one of E, I is zero.
- The graph is **homophilic** when EI < 0, **heterophilic** when EI > 0, **neutral** when EI = 0.
- For directed graphs, count each directed edge separately (or symmetrise first).
- For weighted graphs, use sum of weights instead of edge counts.

### The random-mixing baseline

The E-I index alone does NOT tell you whether observed homophily is "real" or just a consequence of group sizes. Under random mixing, the *expected* cross-group fraction is:

    P(cross | random) = 1 − Σᵢ (nᵢ choose 2) / (N choose 2)

where nᵢ is the size of group i and N is the total number of nodes. If the observed cross-fraction is much below this baseline, the network is homophilic *beyond what group sizes alone predict*.

The "baseline E-I" is computed by plugging the expected E and I into the formula. A network can have EI < 0 by chance if one group is much larger than the others; the random baseline tells you how negative EI is "for free."

## Key Properties

### Strengths
- **Single number**: easy to report, easy to compare across networks, easy to test statistically.
- **Signed**: direction is built in (positive vs. negative homophily).
- **Bounded**: the [-1, +1] range makes interpretation universal.
- **Cheap to compute**: O(|E|) traversal.

### Limitations
- **Binary grouping only**: standard definition assumes a categorical attribute with two-or-more levels. For multi-valued attributes, you may need to collapse or stratify.
- **No control for group sizes**: a single very large group will dominate the count. Always report the random-mixing baseline alongside.
- **Treats all groups equally**: weight by group size, not by group identity. Two networks with very different group structures can have the same EI.
- **Ignores edge weight**: in a weighted graph, raw count treats a "follow" the same as a "best friend". Use sum-of-weights for weighted variants.
- **Single attribute only**: a person can have multiple group memberships (department × gender × nationality). EI captures one dimension at a time.

## Worked Example

The lecture's 8-student friendship network (4 CS students, 4 Business students):

Edges: C1–C2, C1–C3, C2–C3, C3–C4, C4–B1, B1–B2, B2–B3, B3–B4

- Within CS: 4 (C1–C2, C1–C3, C2–C3, C3–C4)
- Within Business: 3 (B1–B2, B2–B3, B3–B4)
- Across: 1 (C4–B1)
- Total: 8

EI = (1 − 7) / (1 + 7) = −6/8 = **−0.75**

Strongly negative → strong homophily. Students overwhelmingly befriend others in the same department.

Random baseline: with two equal-sized groups of 4, expected cross-group fraction is
1 − ((4 choose 2) + (4 choose 2)) / (8 choose 2) = 1 − 12/28 ≈ 0.57.

So under randomness, 57% of edges should be cross-department. We observe only 12.5%. The homophily is real and large.

The baseline EI is approximately +0.14 — meaning a *random* network of this structure would be slightly heterophilic, not homophilic. Observed −0.75 vs. baseline +0.14 is a gap of nearly one full unit on the [-1, +1] scale.

## Common Pitfalls
- **Reporting EI without the random baseline**: with skewed group sizes, the baseline can be strongly negative (large group dominates). Always ask: "is this homophily, or just group sizes?"
- **Conflating EI with homophily in general**: EI is one specific measure. The literature uses many others (assortativity coefficient, modularity on a fixed partition, conditional probability of within-group tie). They can disagree.
- **Forgetting to handle multi-graphs and self-loops**: a node with a self-loop or a multi-edge will inflate E+I and may be miscounted as "internal".
- **Treating EI as a p-value**: EI is a descriptive statistic, not a test. To test significance, use a permutation test (shuffle group labels, recompute EI, compare).
- **Single attribute fallacy**: people belong to many groups. EI on department says nothing about homophily on gender or year of study. Report all relevant dimensions.

## Connections
- [[homophily]] — the broader phenomenon
- [[affiliation-networks]] — one source of group labels (bipartite projection)
- [[selection-vs-socialization]] — the causal mechanisms EI does NOT distinguish
- [[zacharys-karate-club]] — classic dataset with a group label ("club" faction)
- [[modularity]] — the community-detection version (generalises EI to a *discovered* partition)

## Open Questions
- For multi-valued or ordinal attributes (e.g., age groups), how should EI be generalised? (Bridged via assortativity coefficient, which uses Pearson correlation on numeric labels.)
- How do you compute a confidence interval on EI? (Bootstrap on the edges, or permutation on the labels.)
- Can EI be used as an *objective* for a community-detection algorithm? (Yes — but with caveats; modularity is the more common choice because it doesn't require fixed labels.)
