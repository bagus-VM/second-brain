---
title: "Reverse- and Reengineering — Lecture 1 Overview (Reengineering, Control Flow Analysis and Slicing)"
tags: [topic, reverse-and-reengineering, semester-2, reengineering, program-analysis]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Software ages, reengineering is the response, and control-flow graphs, dependence graphs and
slicing are the analysis machinery that makes reverse engineering possible.

## Core Map

```
Lecture 1 — Reengineering and Reverse Engineering (51 slides)
│
├── Organisation (slides 1-6)
│   ├── lecture Wed 12:15-13:45; tutorial Tue 14/16-18; 6 ECTS
│   └── Exams: 2 dates, Campus Portal, 90 pts / 90 min
│
├── Software aging (slides 9-11)
│   ├── requirements change; features do not fit the architecture
│   └── quality loss: error-proneness, performance, maintainability
│        -> [[software-aging]]
│
├── Reengineering (slides 8, 12, 38, 45)
│   ├── Chikofsky/Cross 1990: examination and alteration "to reconstitute
│   │   it in a new form"
│   └── Reverse Eng -> Restructuring -> Forward Eng
│        -> [[reengineering]]
│
├── Reverse engineering (slides 13-15, 36-37)
│   ├── identify components and relationships, present understandably
│   ├── ladder: object code -> source -> detailed design -> spec
│   ├── post-documentation, architectural rediscovery
│   └── problems: lost information, no proof of execution, partial automation
│        -> [[reverse-engineering]]
│
├── Control flow analysis (slides 16-23)
│   ├── intra- vs interprocedural control flow
│   ├── basic blocks, intraprocedural CFG, call graph
│   └── tools: Sourcecode Visualizer, GCC CFG, IDA
│        -> [[control-flow-graph]] [[basic-block]] [[interprocedural-analysis]]
│
├── Program dependence graph (slides 24-29)
│   ├── statement order no longer visible
│   └── control vs data dependence
│        -> [[program-dependence-graph]] [[control-dependence]]
│
├── Program slicing (slides 30-35)
│   ├── forward vs backward slicing, criterion S
│   ├── variants: static/dynamic, analysis, data unit
│   └── spec: interprocedural?, GOTO, late binding, concurrency
│        -> [[program-slicing]]
│
├── Refactoring and smells (slides 39-44)
│   ├── restructuring keeps semantics and behaviour
│   ├── code smell -> code refactoring; architecture smell -> architecture
│   │   refactoring, "not automatable"
│        -> [[refactoring-and-code-smells]] [[architecture-smell]]
│
├── Maintenance vs reengineering (slides 46-47)
│        -> [[reengineering-vs-maintenance]]
│
└── Legacy systems and renewal (slides 48-49)
    ├── obsolete stacks, poor docs, huge code base, lost knowledge
    ├── "nevertheless, legacy systems oftentimes perform critical tasks"
    └── packing / migration / replacement in one go
         -> [[legacy-systems]] [[legacy-system-renewal]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[software-aging]] | Quality decays because requirements drift and features do not fit the architecture |
| [[reengineering]] | Reconstitute a system in a new form; a loop through reverse engineering, restructuring, forward engineering |
| [[reverse-engineering]] | Identify components and relationships, present the system understandably, to enable maintenance |
| [[refactoring-and-code-smells]] | Internal structure improves while behaviour is maintained, so refactoring needs regression tests |
| [[architecture-smell]] | Weaknesses at the architecture level, needing architecture refactoring, which cannot be automated |
| [[reengineering-vs-maintenance]] | Maintenance serves the customer; reengineering serves the developer |
| [[legacy-systems]] | Obsolete stacks, poor docs, huge code bases, lost knowledge — still critical |
| [[legacy-system-renewal]] | Packing behind a modern shell, migrating component by component, or replacing in one go |

## Lecture Structure

1. **Organisation** — schedule, six ECTS, content list, learning outcomes, exam logistics (two
   dates, Campus Portal, 90 points / 90 min), and the homework rule.
2. **Learning objectives** — the slide-6 checklist: aging, reengineering, refactoring, smells;
   legacy systems, CFGs, PDGs, slicing, maintenance vs reengineering.
3. **Software aging** — three causes, four consequences, the aging process graph.
4. **Reengineering** — the Chikofsky/Cross definition and the process diagram.
5. **Reverse engineering** — its three bullets, the workflow ladder, the process table,
   post-documentation, architectural rediscovery.
6. **Control flow analysis** — intra- versus interprocedural, basic blocks, the
   intraprocedural CFG of a read/compare/print program, the call graph and their combination;
   then the three tools that make these graphs visible.
7. **Program dependence graph** — the same program as a PDG in four stages: nodes, control
   dependencies, data dependencies, finished graph.
8. **Program slicing** — forward and backward slicing of a loop, the slicing variants, and the
   questions a slicing specification must answer.
9. **Restructuring and refactoring** — restructuring, refactoring, code smells and their
   remedies, architecture smells and theirs.
10. **Closing slides** — forward engineering, maintenance vs reengineering, legacy systems and
    renewal, then references (Ludewig & Lichter, Parnas, Bennicke & Rust, Fowler).

## Exam-Relevant Points

1. **The three-stage process diagram** (reverse engineering → restructuring → forward
   engineering) recurs three times and frames every other slide.
2. **The Chikofsky/Cross definition** of reengineering and the maintenance/reengineering
   distinction — an objective in itself.
3. **The two kinds of control flow** and the three graph types: intraprocedural CFG, call
   graph, combination.
4. **The basic-block definition** and the two dependence kinds in a PDG: control dependence
   ("determines the execution of") and data dependence ("no reassignment").
5. **Forward versus backward slicing** and the term *slicing criterion* for S, plus variants
   and the four specification questions.
6. **The code smell list and the architecture smell list**, each matched to its remedy.
7. **The three renewal procedures** for legacy systems, and the legacy-system properties plus
   the clause that they nevertheless run critical tasks.
8. **The three problems of reverse engineering**: information lost in compilation, static
   analysis unable to assert execution, partial automation.

## Connections

- [[reverse-and-reengineering]] — the course page, whose process diagram this lecture expands.
- [[reverse-and-reengineering-lecture-2]] — reverse engineering proper: abstraction ladder,
  static vs dynamic analysis, x86.
- [[reverse-and-reengineering-exercise-1]] — Homework 1 turns CFG, PDG and slicing into drawings.
- [[reverse-and-reengineering-exercise-2]] — Homework 2 applies the assembly material.
- [[control-flow-graph]] — the Semester 1 CFG page, re-derived as a reverse-engineering tool.
- [[program-dependence-graph]] — the Semester 1 PDG page, re-derived from these slides.
- [[program-slicing]] — the Semester 1 slicing page, whose criterion terminology this deck uses.
- [[basic-block]] — the same definition, used to build the CFG here.
- [[code-clones]] — the duplication smell of slide 41 has its own page.
- [[software-analysis]] — the SE pipeline run backwards.

## Open Questions

- The content list promises "effects of obfuscation techniques" and "automatic refactoring",
  and neither has a slide here.
- The aging process graph (slide 11) is an image whose axes and R1-R5 scale are not legible in
  the text layer, so the model behind it is not recoverable.
- The deck names three tools — Sourcecode Visualizer, GCC CFG dumps, IDA — but never shows their
  output or says which the exercises use.
- The slide-6 objectives are never mapped to the exam's 90 points, so the weighting between the
  conceptual and the analysis half is unknown.
