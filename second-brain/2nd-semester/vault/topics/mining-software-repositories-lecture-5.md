---
title: "Mining Software Repositories — Lecture 5 Overview (Studying Social Aspects)"
tags: [topic, mining-software-repositories, semester-2, social-aspects]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 5 applies the network machinery twice: detect four community smells from two
undirected graphs — silos, lone wolves, black clouds, and bottlenecks — then to test Conway's law
by comparing the coordination a project required with the coordination it actually performed.

## Core Map

```
Chapter 5 — Studying social aspects
│
├── Smells in software engineering
│   ├── Code smell: a pattern indicating a deeper problem (Fowler & Beck)
│   ├── Smells are not bugs but associated with them; a type of technical debt
│   └── Technical debt -> social debt -> community smells
│           -> [[community-smells]]
│
├── Community smells from two undirected graphs
│   ├── Communication graph G_comm: edge iff the two developers communicated
│   ├── Collaboration graph G_coll: edge iff they worked on the same files
│   ├── Assumption V_coll subset of V_comm
│   ├── Organizational silos: pairs in V_coll with no path between them in G_comm
│   ├── Lone wolfs: pairs in E_coll with no path in G_comm; subset of Silos
│   ├── Black clouds: one bridge pair between two communities and no communication
│   │       for 6 months (the literature's interval)
│   └── Bottlenecks: one developer handles the bridge; every black cloud is one
│
├── Diversity
│   ├── Gender, cultural, sexual orientation; unrelated to competency
│   ├── Hypothesis: more women -> better communication -> fewer community smells
│   ├── Linear model: dependent = smell counts, independent = number of women and
│   │       Blau index, controls = team size, turnover, project age, tenure,
│   │       E_coll/E_comm ratio, truck factor, centrality
│   └── Results: turnover drives bottlenecks; women reduce bottleneck likelihood;
│           lone wolfs explained by team size and collaboration/communication ratio
│
└── Conway's law and socio-technical congruence
    ├── "Organizations which design systems are constrained to produce designs which are
    │       copies of the communication structures of these organizations" (Conway, 1968)
    ├── Coordination requirements: task assignments x task dependencies
    ├── Architecture network: static imports or co-change
    └── Congruence = required-and-happened / required; near 1 = follows Conway's law
            -> [[conways-law]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[community-smells]] | Four detectable patterns — silos, lone wolves, black clouds, bottlenecks — defined over communication and collaboration graphs |
| [[conways-law]] | Architecture mirrors communication structure; congruence measures required against actual coordination |
| [[developer-social-networks]] | The graphs both halves of the chapter build on: communication, collaboration, architecture, activity |
| [[community-structure]] | The communities used as sub-projects in the black-cloud and bottleneck definitions |
| [[msr-statistical-methods]] | The linear model, ANOVA, and the significance reading applied to the diversity study |

## Lecture Structure

1. **Smells and their origin** — the negative connotation of "smell" in software engineering, its
   origin in the Refactoring book, code smells as patterns indicating deeper design problems and
   as technical debt; the debt metaphor extended to social debt, and community smells.
2. **How community smells were found** — a qualitative study with company developers, based on
   open and axial coding of interviews; broader evidence of prevalence is missing.
3. **The two graphs** — the communication graph and the collaboration graph, their node sets,
   edge conditions, and the assumption that collaborators also communicate.
4. **Organizational silos** — pairs of collaborators with no communication path; the
   consequences, duplicated effort and blocked architectural change.
5. **Lone wolves** — collaborators on the same code with no communication; the risk of unchecked
   autonomy against the team's design; LoneWolfs ⊆ Silos.
6. **Black clouds** — inability to exchange knowledge between sub-projects, named after the
   personal conflict that suppresses communication; a single bridge pair plus a long silence,
   six months being the literature's interval.
7. **Bottlenecks (radio silence)** — the structural version: one developer as single point of
   failure for communication between two communities; every black cloud is a bottleneck.
8. **Diversity** — the aspects of diversity, the hypothesis from management literature, the
   model with dependent, independent, and confounding variables, the linear model with ANOVA for
   coefficient significance, and the two results.
9. **Conway's law** — the 1968 quotation; communities as the social unit; the Apache example of
   code-oriented versus documentation-oriented developers.
10. **Modelling architectures and coordination** — files as nodes, static structure via imports
    versus the call graph, co-change as an alternative proxy; task assignments from issue
    metadata, task dependencies from overlapping files, the requirement matrix, and the
    congruence ratio.

## Exam-Relevant Points

1. **Two graphs, four smells.** The differences between them are in the edge condition, the path
   condition, and the time window.
2. **Silos and lone wolves are both "no path in G_comm" conditions**, but silos range over
   collaborators in general while lone wolves range over the edges of the collaboration graph —
   which is why lone wolves are a subset of silos.
3. **Black cloud adds time; bottleneck adds structure.** The black cloud needs a six-month
   silence, the bottleneck needs a single bridging developer.
4. **Diversity is not competency**, and the study's own results are specific: turnover, not
   gender, drives bottlenecks, while the number of women reduces bottleneck likelihood.
5. **The diversity model separates dependent, independent, and confounding variables** — project
   size and age are controls, not covariates of interest.
6. **Conway's law becomes a number.** Congruence is required-and-happened coordination divided
   by required coordination; near one means the communication matches the architectural
   dependencies, far from one means it does not.
7. **Coordination requirements come from architecture, not from chat.** Informal exchanges do not
   count; issue-tracker communication is the observable proxy, and tasks are the unit.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-4]] — the graph and metric machinery this chapter uses.
- [[mining-software-repositories-lecture-7]] — the statistics that read the diversity model.
- [[community-smells]] — the four smells and their definitions.
- [[conways-law]] — the congruence framework in full.
- [[developer-social-networks]] — the communication, collaboration, and architecture graphs.
- [[community-structure]] — the community notion behind black clouds and bottlenecks.
- [[temporal-networks]] — the time dimension behind the six-month rule.

## Open Questions

- **The six-month interval for black clouds comes from the literature**, and the slides do not
  say whether the choice is sensitive to it.
- **No prevalence figures for community smells are given** — the chapter motivates MSR as the
  source of that evidence but supplies none.
- **The diversity study's coefficients and effect sizes are not shown**.
- **How gender was determined in the data is never explained**, which matters for anyone
  repeating the study.
