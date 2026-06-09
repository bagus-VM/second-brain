---
title: "Centola's Online Experiment (2010)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Centola (2010) experimentally confirmed that behavior spread is faster in clustered networks (54% adoption) than random networks (38%), validating the simple vs. complex contagion distinction.

## Core Intuition
The simple/complex contagion distinction predicts opposite effects of clustering: for simple contagion, random networks with shorter paths should spread faster; for complex contagion, clustered networks with local reinforcement should spread faster. Centola built an online experiment to test this directly, and complex contagion won in clustered networks despite their longer paths.

## Formal Definition / Statement
**Study:** Centola (2010), "The Spread of Behavior in an Online Social Network Experiment," Science 329, 1194–1197.

**Design:** 1,528 participants randomly assigned to:
- **Clustered condition:** Lattice-like network (high clustering)
- **Random condition:** Watts-Strogatz-style network (low clustering)

Both networks had the same degree and diameter. Participants could register for a health program; registration was visible to neighbors.

**Results:**
1. Behavior spread faster and further in the clustered network (54% vs. 38% adoption)
2. Adoption was driven by multiple exposures — participants with 2+ adopting neighbors were far more likely to adopt
3. The random network had shorter paths — if simple contagion were the mechanism, it should have won. It lost.

## Key Properties
1. **Clustering beats shortcuts** for complex contagion — local reinforcement matters more than path length
2. **Multiple exposures drive adoption** — consistent with threshold rules, not single-contact rules
3. **Same degree and diameter** — the only difference was clustering, isolating its effect
4. **Random network advantage reversed** — shorter paths helped simple contagion theory but not behavior spreading

## Limitations of the Study
1. **Binary behavior:** Tracked registration (yes/no), not intensity or quality of adoption
2. **Controlled networks:** Assigned structures were regular and static — real networks are heterogeneous, dynamic, and have different degree distributions
3. **Single behavior type:** Tested one health-program registration — generalization to other complex contagions not directly tested
4. **No decay or reversal:** Once registered, participants stayed — real adoption can reverse

## Worked Example
In the clustered network, a participant sees multiple neighbors register. Because neighbors are also connected to each other (high clustering), they reinforce each other's adoption decisions. The local density creates a feedback loop that sustains and spreads the behavior.

In the random network, neighbors are less likely to be connected to each other. A participant may see one neighbor adopt, but without reinforcement from a second neighbor, the threshold is not met. The shorter paths don't help because the process needs local density, not long-range shortcuts.

## Common Pitfalls
- Overgeneralizing from one experiment — the study tested one behavior in controlled conditions
- Assuming clustering always wins — for simple contagion (diseases, rumors), random/short-path networks spread faster
- Ignoring the limitations — real networks are heterogeneous and dynamic in ways the experiment did not capture

## Connections
- Empirical validation of [[complex-contagion]] and the [[weak-tie-paradox-contagion]]
- Contrasts with [[simple-contagion]] predictions — random networks should win for diseases
- Connects to [[threshold-cascades]] — the multiple-exposure finding supports threshold models
- Relates to [[network-community-structure-l06]] — clustering is a community-level property
- Part of [[network-dynamics-l08]]

## Open Questions
- Does the clustering advantage hold for other complex contagions (political mobilization, technology adoption)?
- How does the result change with heterogeneous thresholds across nodes?
- What happens when adoption can reverse (abandonment, counter-influence)?
