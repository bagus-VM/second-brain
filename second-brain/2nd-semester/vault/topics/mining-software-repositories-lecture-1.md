---
title: "Mining Software Repositories — Lecture 1 Overview (Introduction and Foundations)"
tags: [topic, mining-software-repositories, semester-2, foundations]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 1 argues that software development is decided by anecdote where it could be decided by
evidence, defines what a software repository and "data mining" each mean, and derives the
field's pipeline equation — repository data plus collection plus analysis, ending in insights
or tools.

## Core Map

```
Chapter 1 — Introduction and Foundations
│
├── Motivating examples
│   ├── GitHub Co-Pilot — code-change data trains AI models
│   ├── Insights into development processes
│   ├── Social networks — the social aspects of development
│   └── Insights into bugs and failures
│
├── Basic definitions
│   ├── Software repositories
│   │   ├── ISO/IEC/IEEE 24765:2017 — collection / location / persistent storage
│   │   ├── MSR 2023 conference scope — SCM, trackers, reviews, comms, Q&A, CI, telemetry
│   │   ├── Kagdi, Collard & Maletic (2007) — "artifacts produced and archived
│   │   │       during software evolution"
│   │   └── Many different kinds of repositories
│   │           -> [[software-repositories]]
│   └── Data mining
│       ├── Merriam-Webster — searching large amounts of data for patterns
│       ├── Three aspects: large data, searching, useful patterns
│       └── Mining analogy: ore, retrieving, refining
│
├── Software repositories + data mining = MSR
│   │   Data from repositories -> Collection -> Analysis -> Insights or tools
│   │   -> [[mining-software-repositories]]
│
├── Evidence-based software engineering
│   ├── Evidence-based medicine: therapy -> evidence -> decision
│   ├── Software engineering: suggestion -> discussion -> decision (PEPs)
│   ├── Remedy: suggestion -> we collect evidence -> decision
│   ├── Survey / case study / experiment (Wohlin et al. 2012)
│   │       -> [[evidence-based-software-engineering]]
│   ├── Repositories as developer profiles; ethics, GHtorrent, data protection
│   └── Repositories as case-study and experiment substrate
│
└── Building tools
    ├── Five improvement targets for existing tools
    ├── Four-step tool-building approach
    │       -> [[msr-tool-building]]
    ├── ML-based tools vs. tools without ML
    └── Examples: Nudge, Code City, Tesseract; MSR as a product (Teamscale)
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[software-repositories]] | Not one thing but a family of stores — SCM, trackers, reviews, CI, telemetry, forges, chats, wikis, Q&A sites |
| [[mining-software-repositories]] | The pipeline equation: repository data + collection + analysis yields insights or tools |
| [[evidence-based-software-engineering]] | Evidence-first decision making, transplanted from medicine into software engineering |
| [[msr-tool-building]] | Four steps — fix the goal, fix the data, build, then run an experiment — with proxy evidence |

## Lecture Structure

1. **Motivating examples** — four slides of applications: Co-Pilot training on change data,
   understanding the effect of best practices and tools, social networks, and understanding how to
   avoid or find bugs.
2. **Basic definitions** — the ISO/IEC/IEEE 24765:2017 definitions of a software repository, the
   MSR 2023 conference's own scope statement, and Kagdi et al. (2007) on archived artifacts; then
   the catalogue of repository kinds.
3. **Data mining** — the Merriam-Webster definition and its three key aspects, the physical-mining
   analogy, and the note that the term is used generically, similar to data science.
4. **The MSR equation** — repository data + data collection + data analysis = insights or tools.
5. **Evidence-based software engineering** — the medicine contrast, the software-engineering
   contrast (PEPs), the remedy slide, the three evidence-collection methods from Wohlin et al.,
   and what repositories contribute to each of them.
6. **Ethics** — developer profiles for surveys, the GHtorrent incident, ethics approval, and data
   protection regulation.
7. **Building tools** — the five tool-improvement targets, the four-step approach, ML-based
   versus non-ML tools, three named example systems, and MSR sold as a commercial product.

## Exam-Relevant Points

1. **The MSR equation is the spine of the course.** Every later chapter fills one cell: Chapter 2
   and 3 produce the data collection and enrichment, Chapter 7 produces the analysis, and the
   output cell is "insights or tools".
2. **The definition of a software repository is a family of definitions, and they agree.**
   ISO/IEC/IEEE 24765, the MSR conference, and Kagdi et al. all describe archived artifacts of
   software evolution rather than a single store.
3. **The mining analogy maps three-to-three**: raw data is ore, searching is retrieving ore,
   finding patterns is refining into metal. Each stage can be done badly.
4. **Evidence-based software engineering has a staging structure**, and repository data can
   stand in for several stages at once.
5. **The three evidence-collection methods differ in what they can answer**: a survey describes
   knowledge, attitudes, behavior; a case study investigates one instance in its real-life
   context; an experiment manipulates one factor with randomization.
6. **Repository data brings an ethics obligation.** Surveys of developers drawn from repository
   profiles require checking ethics approval, and data protection rules apply regardless.
7. **The tool-building approach always ends with an experiment, and the evidence is usually a
   proxy** — accuracy rather than ROI or time saved.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-0]] — the organization deck and content map this chapter
  opens.
- [[mining-software-repositories-lecture-2]] — the collection chapter that operationalizes
  "data collection".
- [[mining-software-repositories-lecture-3]] — the enrichment chapter, still part of the pipeline.
- [[mining-software-repositories-lecture-7]] — the methods chapter that fills the analysis cell.
- [[evidence-based-software-engineering]] — the medicine analogy and the three evidence methods.
- [[msr-tool-building]] — the four-step approach for the "tools" output.
- [[machine-learning-for-cybersecurity]] — the other course where repository-derived data trains
  models, and where the same presenters insist on class presentation.

## Open Questions

- **The definition slides cite three sources but do not reconcile them**, and no slides explain
  what is excluded by "repository" — e.g. whether a team's chat archive counts.
- **No exam date, credit points, or assessment format appear** in this chapter.
- **The Co-Pilot example is asserted without a citation or a number** — no dataset size, no
  model detail, no result is shown.
- **The MSR-as-a-product slide names Teamscale** but gives no information about what it measures
  or how it is sold.
- **The distinction between data mining and data science is asserted, not defined** — the slides
  say the terms are used "very generically" and "similar", leaving the boundary open.
- Whether the ethics guidance for surveys is enforced, or only advisory, is not stated.
