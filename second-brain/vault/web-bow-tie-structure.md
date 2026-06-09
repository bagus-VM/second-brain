---
title: "Web Bow-Tie Structure"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Broder et al. (2000) found that the Web decomposes into a bow-tie: a strongly connected core (~28%), IN and OUT components, and tendrils — making reachability asymmetric and navigability fundamentally different from social networks.

## Core Intuition
Hyperlinks are directed: page A can link to page B without B linking back. This asymmetry means the [[small-world-property]] doesn't apply uniformly across the Web.

Broder et al. crawled ~200 million web pages and found the Web decomposes into:
- **SCC (Strongly Connected Component)**: ~28% — every page reachable from every other via directed paths. This IS the "small world" of the Web.
- **IN**: pages that can reach the SCC but aren't reachable from it
- **OUT**: pages reachable from the SCC but can't reach back
- **Tendrils and tubes**: connected to IN or OUT but not to the SCC

Short paths exist *within* the SCC (~16 clicks between random pages), but NOT from OUT back to SCC, or between tendrils.

## Formal Definition / Statement
**Bow-tie decomposition (Broder et al., 2000):**

For a directed graph $G = (V, E)$:
- **SCC**: $\{v \in V \mid \forall u \in V, \text{directed path exists both } v \to u \text{ and } u \to v\}$ — the largest set of mutually reachable nodes
- **IN**: $\{v \in V \mid v \notin \text{SCC}, \exists u \in \text{SCC}: v \to u\}$ — can reach SCC but not reached from it
- **OUT**: $\{v \in V \mid v \notin \text{SCC}, \exists u \in \text{SCC}: u \to v\}$ — reached from SCC but can't reach back
- **Tendrils**: connected to IN or OUT but not to SCC

**Empirical findings (~200M pages):**
| Component | Fraction |
|---|---|
| SCC | ~28% |
| IN | ~21% |
| OUT | ~21% |
| Tendrils/tubes | ~22% |
| Disconnected | ~8% |

## Key Properties
- The SCC is a small world: ~16 clicks between random page pairs within it
- Reachability is **asymmetric**: IN → SCC → OUT works, but OUT → SCC does not
- Most pairs of pages (~76%) do NOT have a directed path between them
- Search engines solve the navigability problem through **centralized indexing** — the opposite of [[kleinberg-decentralized-search|Kleinberg's decentralized search]]
- The directed structure makes [[small-world-property|small-world]] properties local to the SCC, not global

## Worked Example
**Directed network with 1000 nodes:**
- SCC: 300 nodes
- IN: 200 nodes
- OUT: 250 nodes
- Tendrils: 250 nodes

**From IN to OUT?** Yes: IN → SCC → OUT (through the SCC as relay).

**From OUT to IN?** No: OUT nodes can't reach back to SCC (by definition).

**Reachable pairs:**
- SCC → SCC: 300 × 299 = 89,700
- IN → SCC: 200 × 300 = 60,000
- SCC → OUT: 300 × 250 = 75,000
- IN → OUT (via SCC): 200 × 250 = 50,000
- Total: ~274,700 out of 1000 × 999 ≈ 10⁶ → **~27%** of pairs are reachable

## Common Pitfalls
- **"The Web is a small world"** — Only the SCC (~28%) is. The rest has asymmetric or missing reachability.
- **"Short paths exist between any two pages"** — Only within the SCC. From OUT to IN, no directed path exists.
- **"Decentralized search works on the Web"** — It's much harder because you can only follow outgoing links. Search engines solve this by building a global index (centralized).
- **"Directed graphs are just undirected graphs with arrows"** — The directionality fundamentally changes reachability, navigability, and the applicability of small-world results.

## Connections
- [[small-world-property]] — Applies within the SCC but not globally across the Web
- [[kleinberg-decentralized-search]] — Assumes undirected links; the Web's directed links break this
- [[milgrams-experiment-six-degrees]] — Milgram's social network was effectively undirected (acquaintance is symmetric); the Web is not
- [[random-graphs]] — Directed random graphs have different connectivity thresholds
- [[scale-free-networks]] — The Web's degree distribution is heavy-tailed (in-degree follows power law)

## Open Questions
- How has the bow-tie structure changed since 2000 (with social media, SPAs, JavaScript rendering)?
- Can decentralized search work on directed networks if you add a small number of bidirectional links?
- How do modern search engines' ranking algorithms (PageRank) interact with the bow-tie structure?
