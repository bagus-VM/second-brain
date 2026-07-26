---
title: "Milgram's Experiment & Six Degrees of Separation"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Milgram's 1967 letter-forwarding experiment showed that any two strangers are connected by roughly 6 intermediaries, revealing the small-world property of social networks.

## Core Intuition
In 1967, Stanley Milgram mailed 296 letters to random people in Nebraska and Kansas. Each letter named a target person — a stockbroker in Boston — and asked recipients to forward it to someone they knew on a first-name basis who might be "closer" to the target. The letters that arrived took a median of about 6 steps, giving rise to the phrase "six degrees of separation."

The experiment raised four fundamental questions that drive the rest of the lecture:
1. **Existence** — Why do short paths exist at all in a network of 200 million people?
2. **Coexistence** — How can a network be locally clustered AND have short paths to strangers?
3. **Navigability** — Can ordinary people find short paths using only local knowledge?
4. **Failure** — Only ~25% of chains arrived. Why did most fail?

## Formal Definition / Statement
Not a formal theorem but an empirical observation: in a social network of $n \approx 200$ million people, the median chain length between random pairs was approximately 6. This is consistent with logarithmic scaling $\bar{d} \approx \frac{\log n}{\log k}$ where $k$ is the average degree.

The key insight is the **navigational gap**: short paths may exist in the graph, but finding them with only local information is a separate (and harder) problem. Only ~25% of chains completed — the rest died when intermediaries refused or couldn't figure out who to forward to.

## Key Properties / Complexity
- Demonstrated that social networks have surprisingly short average path lengths
- The experiment required only local knowledge — each person saw only their own contacts
- ~75% of chains failed, revealing the gap between path existence and path findability
- The result held even though participants had no global view of the network
- Later replicated at scale by Dodds, Muhamad & Watts (2003) using email (see [[global-email-experiment]])

## Worked Example
Network with $n = 300$ million, average degree $k \approx 100$:
$$\bar{d} \approx \frac{\log(3 \times 10^8)}{\log 100} = \frac{19.5}{4.6} \approx 4.2$$

Milgram's observed median of ~6 is in the right ballpark — slightly higher because real social networks have heterogeneous degree distributions and geographic constraints.

For Facebook ($n \approx 3$ billion, $k \approx 300$): $\bar{d} \approx 3.8$, close to the empirical 3.57 reported in 2016.

## Common Pitfalls
- **"Six degrees" means exactly 6** — It's an approximate median; actual distances vary by pair
- **The experiment proved short paths exist** — It also showed that *finding* them is hard (75% failure rate)
- **Chain failure means no path exists** — Chain death is about motivation/willingness, not topology
- **Milgram's result applies to all networks** — It specifically demonstrates the small-world property in *social* networks

## Connections
- [[small-world-property]] — The formal property Milgram's experiment revealed
- [[watts-strogatz-model]] — The model explaining why short paths coexist with clustering
- [[kleinberg-decentralized-search]] — Explains when local actors can actually *find* short paths
- [[global-email-experiment]] — Dodds et al. (2003) replication at scale
- [[web-bow-tie-structure]] — Directed version of navigability on the Web
- [[small-world-property]] — The mathematical framework behind "six degrees" (logarithmic distances)

## Open Questions
- What is the true completion rate if all intermediaries cooperated fully?
- How do social categories (profession, geography) guide routing decisions?
- Does the six-degree result hold for all types of relationships or only strong ties?
