---
title: "Reverse- and Reengineering — Lecture 5: Decompilation and Structural Analysis"
tags: [topic, reverse-and-reengineering, semester-2, lecture, decompilation]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[reverse-and-reengineering-lecture-4]]"]
---

## One-line Summary
Decompilation reconstructs a plausible high-level program from machine code by translating instructions to an intermediate representation, recovering control flow, and iteratively matching graph regions to structured constructs.

## Core Map

```
Machine code
├── translate instructions and flags into an intermediate representation
├── recover control-flow graph (indirect jumps remain difficult)
├── identify regions: sequence, branches, switches, loops
├── structural analysis collapses matched regions
└── iterative refinement virtualizes/removes obstructive edges
    └── output is a semantics-sensitive reconstruction, not the original source
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[decompilation]] | Decompilation reconstructs an approximate source-level explanation, but compiler transformations destroy original source details. |
| [[control-flow-graph]] | Structural analysis treats the program as nodes and possible transfers between them. |
| [[structural-analysis-decompilation]] | Region-pattern matching recovers sequences, branches, switches and loops; iterative refinement handles difficult edges. |
| [[binary-reverse-engineering]] | The broader abstraction ladder from machine code to source, now focused on recovery of structured control flow. |
| [[reverse-and-reengineering-lecture-4]] | The prior lecture covers disassembly and obfuscation, the inputs and obstacles for decompilation. |

## Lecture Structure

The source is a 23-slide deck, “Reverse Engineering – Decompilation.” It contrasts assembly with readable source (slide 2), then explains why decompilation is hard: compilers discard comments and file structure, machine code is untyped, and optimization changes the source's shape (slide 3). Slides 4–10 translate instructions/flags to an intermediate representation and show constant propagation, simplification, and dead-code elimination. Slides 11–17 introduce CFG structure recovery: vertices are straight-line code; edges are control transfers; interval/structural analyses classify regions; matching proceeds post-order; iterative refinement removes or virtualizes edges that block a match. Slides 18–22 discuss switch candidates, semantic-preservation hazards, loop refinement and an example where a loop-membership rule changes the reconstructed structure. Slide 23 lists references.

## Exam-Relevant Points

1. A decompiler's output is an interpretation of behavior, not recovery of comments, names, formatting, or necessarily the original control structure.
2. The intermediate representation makes machine-level effects explicit: assignments, memory operations, branches, flags, calls, returns and stack effects.
3. A CFG vertex represents straight-line code; edges represent possible transfers. An indirect jump such as `jmp %eax` needs target analysis (the slides mention value-set analysis).
4. Structural analysis recognizes and collapses common regions, including sequence, if/then/else, switch, while and do/while.
5. Iterative refinement removes or virtualizes obstructive edges so the structurer can make progress; the resulting decompiled code may need `break`, `continue` or `goto`.
6. Incorrect region patterns can change semantics. The lecture explicitly warns that structural analysis must preserve semantics and that loop membership choices matter.

## Connections

- [[reverse-and-reengineering-lecture-4]] — disassembly provides instructions and initial control-flow evidence.
- [[binary-reverse-engineering]] — the abstraction ladder and static/dynamic analysis framing.
- [[control-flow-graph]], [[natural-loop]], [[dominance]] and [[post-dominance]] — graph concepts structural analysis relies on.
- [[reverse-and-reengineering-exercise-5]] — the exercise sheet applies CFG reconstruction and iterative refinement; this page describes tasks without solving them.
- [[reverse-and-reengineering]] — course syllabus includes intermediate representations and program-analysis goals.

## Open Questions

- The deck asserts that some analyses are undecidable or structurally difficult but does not formally state the results or assumptions.
- The PDF extraction corrupts several formulas and diagrams; the overview uses only legible textual claims and does not reconstruct missing equations.
- The example figure comparing decompiler output is partly garbled in text extraction, so exact output formatting is not transcribed.
