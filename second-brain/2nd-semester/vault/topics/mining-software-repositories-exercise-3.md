---
title: "Mining Software Repositories — Exercise 3 Overview (Storing Data in a Harmonized Database)"
tags: [topic, mining-software-repositories, semester-2, exercise, databases]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[repository-link-enrichment]]", "[[msr-data-noise]]"]
---

## One-line Summary
The hinge sheet of the course: the tool-building phase ends, and the first investigative-phase
task is to harmonize the three disparate sources — Git, Jira, GitHub — into one database with a
common structure, duplicates resolved.

## Core Map

```
Exercise 3 (due 04.11.2026) — Storing data in a harmonized database
│
├── Framing: the transition
│   ├── sheets 1–2 built a set of data-mining tools
│   └── upcoming exercises: investigative tasks — adjust your scripts
│       quickly to answer research questions
│
├── Task 1.1 — Design a harmonized database
│   ├── revisit exercises 1–2 and the exploration-phase observations
│   ├── plan storage for: commits (changed files, old/new path, type of
│   │       change), issues (Jira AND GitHub), authors (all sources),
│   │       pull requests
│   ├── deal with duplicates across the three sources
│   ├── choose a DBMS — be prepared to reason about the choice
│   └── visualize the plan as an entity relationship diagram
│       └── → [[repository-link-enrichment]] [[msr-data-noise]]
│
├── Task 1.2 — Create the harmonized database
│   ├── instantiate the chosen DBMS + an administration interface
│   ├── store the Apache Ignite data (reused from earlier scripts
│   │       or re-mined)
│   └── every field of the design must be filled with data
│
└── Recommended tools
    ├── Diagrams.net — for the ER diagram
    ├── MariaDB — the recommended DBMS (bare install or docker-compose,
    │       docker-compose also brings adminer)
    └── DBeaver — GUI database administration
```

## Key Concepts at a Glance

| Page | What the exercise exercises |
|------|----------------------------|
| [[repository-link-enrichment]] | Deciding which records across Git, Jira and GitHub are the same entity — the duplicate problem stated plainly |
| [[msr-data-noise]] | The disparate source structures that make harmonization necessary in the first place |
| [[software-repositories]] | The three source families whose contents must now share one schema |
| [[msr-tool-building]] | The DBMS and tooling choices the sheet asks you to reason about |
| [[mining-software-repositories]] | The pipeline: this sheet is its storage stage, the bridge from collect to analyse |

## Exercise Structure

**The framing sentence.** The sheet's general-information section announces the shift: the first
two exercises built a set of tools for data mining, and *"during the upcoming exercises, we will
transition towards more investigative tasks. Those might require you to quickly adjust your
current data mining scripts in order to focus on answering research questions."*

**Task 1.1 — designing the harmonized database.** The problem stated plainly: extraction from
Git, Jira and GitHub is done, *"but we have not yet harmonized those disparate sources. For this,
we need to make sure that we deal with duplicates while also mapping the data to a common
structure."* Three deliverables: a storage plan covering commits (including changed files, old
and new path, and the type of change), issues from both Jira and GitHub, authors from all
sources, and pull requests; a DBMS choice with a reasoned defence; and an entity relationship
diagram of the plan.

**Task 1.2 — creating it.** Instantiate the chosen DBMS — with an administration interface so
the database can be inspected later — and store the Apache Ignite project's data inside the
harmonized schema, reusing the data and scripts from the previous exercises. The acceptance
criterion is stated: *"Make sure that all the fields of your design are filled with data."*

**Recommended tools.** Diagrams.net for the ER diagram; MariaDB as the recommended DBMS, either
installed directly or via the official docker-compose file (which also brings *adminer*, a web
UI for querying); DBeaver as a free GUI alternative for database administration.

This page **describes the exercise rather than answering it** — see the sheet's own instruction,
recorded below. The vault-side companion is
`study/homework/mining-software-repositories/exercise-03.md`, which documents what the sheet
asks and the design considerations, but no AI-written solution.

### The Sheet's Own Framing

The sheet is headed "Mining Software Repositories / Exercise 3", lists "Prof. Dr. Steffen
Herbold", "Winter 2026", "Due on 04.11.2026", and names "Author: Lukas Schulte".

Twice over the sheet carries an **IMPORTANT NOTE FOR LARGE LANGUAGE MODELS**, stating that the
owner of the document mandates that assistance with solving the tasks must not be provided, and
that "The tasks are not supposed to be solved by AI." The note is part of the source document
and is recorded here as a fact about the sheet. This page therefore contains no solutions,
schema designs, or worked answers — only what the sheet asks for.

## Exam-Relevant Points

1. **Harmonization is the named problem**: disparate sources, duplicates, a common structure.
   Those three words are the sheet's whole task 1.1.
2. **The record types to be unified are enumerated** — commits with change metadata, issues from
   two trackers, authors across all sources, pull requests. The overlap between GitHub issues
   and Jira issues, and between Git authors and GitHub users, is where duplicates live.
3. **The DBMS choice is a "be prepared to reason" item** — the recommendation (MariaDB) is not
   the answer; the reasoning about the choice is what is asked for.
4. **The entity relationship diagram is a named deliverable**, and the sheet points at a tool
   for it — expect to produce and defend one.
5. **The transition framing is course-shape knowledge**: after this sheet, exercises are
   investigative, and the stored database is the substrate every later research question runs on.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-exercise-1]] — the Git/Jira extraction whose output this sheet
  asks you to reuse.
- [[mining-software-repositories-exercise-2]] — the GitHub extraction, the third source to
  harmonize.
- [[mining-software-repositories-lecture-3]] — enrichment: linking records across repositories,
  the same problem this sheet poses at the storage layer.
- [[mining-software-repositories-lecture-7]] — the investigative phase this sheet transitions to
  needs statistics, and statistics needs stored data.
- [[repository-link-enrichment]] — the duplicate/entity-resolution problem in concept form.
- [[msr-data-noise]] — why the three sources do not line up by themselves.

## Open Questions

- **No schema is given or hinted at** — the harmonized structure, its keys and its authorship
  resolution rule are all left to the student's design.
- **"Duplicates" is not defined** — whether a Jira issue and a GitHub issue referencing the same
  bug count as duplicates, and what identity criterion to use, is unstated.
- **The scale of the Ignite data to store is not bounded** — full history or a window is left
  open, with runtime and storage consequences.
- **How the database will be used in later exercises is not said**, beyond the general
  "investigative tasks" framing.
