---
title: "Network Science L01: Introduction — Topic Overview"
tags: [topic, network-science, semester-1, lecture-notes]
course: "Network Science"
lecture: "01 — Introduction"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 1 introduces what networks are, why they matter, and what we can analyze with them — establishing the foundational motivation for the entire course.

## Core Concepts (Lecture 1)

### What Is a Network?
[[network-intro]] — A collection of entities (nodes) and relationships (edges). This simple abstraction applies across every domain. A network is always a *model*: it intentionally leaves out details to focus on structure. The same real-world situation can produce different network models depending on the question.

### Real-World Network Examples
[[network-examples]] — Social networks (Karate Club), communication networks (email), information networks (political blogs), economic networks (interbank lending), infrastructure networks (internet routing). Same math, different domains. Structure carries meaning: blog hyperlinks reveal political alignment without reading content.

### Edge Types
[[edge-types]] — Edges can be **undirected** (symmetric, like friendship), **directed** (asymmetric, like "follows"), and **weighted** (carrying strength/frequency). The choice of edge type is a modeling decision. Directed edges introduce in-degree vs. out-degree; weighted edges add nuance but require interpretation.

### Network Effects
[[network-effects]] — The structure of connections creates system-level outcomes (visibility, influence, lock-in, cascading failure) invisible at the individual level. Knowing every bank doesn't tell you which failure cascades. Vannevar Bush's MEMEX (1945) anticipated this: information's value comes from *connections*, not just storage. Dot-com survivors (Google, Amazon, Facebook) understood this.

### Connected Components
[[connected-component]] — A maximal set of mutually reachable nodes. The coarsest structural descriptor. Directed graphs distinguish weakly vs. strongly connected components. Diffusion is bounded by components: information in one component can never reach another.

### Community Structure
[[community-structure]] — Densely connected groups with sparse external links. Detected from structure alone (no metadata needed). Political blogs form liberal/conservative clusters; researchers form collaboration groups. Distinct from components (communities exist *within* connected networks).

### Diffusion and Spreading
[[network-diffusion]] — How information, disease, or influence spreads along edges. Starting position matters: core vs. peripheral nodes yield dramatically different outcomes. Key models: SI, SIS, SIR. Network structure determines speed, reach, and pathway of spreading.

### Centrality
[[centrality]] — Measures of node importance: degree (# connections), closeness (average distance), betweenness (bridge role). Different measures capture different intuitions. A bridge node between communities (high betweenness) may have fewer links than a popular node (high degree).

## How the Concepts Connect

```
network-intro (foundations)
├── edge-types (how edges are modeled)
│   └── centrality (importance depends on edge type)
├── network-examples (domains where networks appear)
│   ├── community-structure (groups within networks)
│   │   └── network-diffusion (spreading follows community boundaries)
│   └── network-effects (why structure matters)
│       └── centrality (influence through position)
└── connected-component (coarsest grouping)
    └── community-structure (finer grouping within components)
        └── network-diffusion (bounded by components)
```

## Key Takeaways from Lecture 1

1. **Networks are models, not reality.** They abstract away details to focus on relational structure. This is both their power and their limitation.

2. **Structure shapes outcomes.** The same entities with different connections produce different system-level behaviors. This is the core motivation for network science.

3. **The same formalism applies everywhere.** Social, information, economic, biological, infrastructure — all are instances of $G = (V, E)$.

4. **What we can analyze:** Structure (communities), Position (centrality), Dynamics (diffusion), Evolution (growth/change).

5. **This is a course about modeling, interpretation, and critique** — not just definitions.

## Course Topics Preview
The lecture outlines what's coming:
1. Graph theory — formal language
2. Social networks — ties, communities, information flow
3. Centrality and influence — who matters and why
4. Community detection — finding groups
5. Information networks and the Web — links, search, ranking
6. Network dynamics — diffusion, contagion, cascades

## Reading
- Easley & Kleinberg (2010), *Networks, Crowds, and Markets*
- Newman (2010), *Networks: An Introduction*
