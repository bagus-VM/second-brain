---
title: "Reverse- and Reengineering — Exercise 1 Overview (Homework 1: CFG, PDG and Program Slicing)"
tags: [topic, reverse-and-reengineering, semester-2, program-analysis, slicing]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Four drawings that turn the lecture's graph vocabulary into practice — an intra-procedural
CFG, a dependence graph, two backward slices, one forward slice — plus an inter-procedural
CFG for a C++ program that calls through a function pointer.

## Core Map

```
Homework 1 (20.10.2026) — Prof. Hammer, Dr. Rezaalipour
│
├── Sheet framing
│   ├── "not for submission"; solve and bring solutions to the tutorials
│   └── slides: homework "not corrected" but "required to pass"
│
├── Task 1 — Intra-procedural CFG, PDG and program slicing
│   ├── the program: a gcd/lcm calculator
│   │   ├── reads x and y with scanf
│   │   ├── for loop i=1..min(x,y), gcd = last common divisor
│   │   ├── prod = x*y; lcm = prod/gcd
│   │   └── printf of gcd, prod, lcm
│   ├── 1.1 intra-procedural CFG
│   │       -> [[control-flow-graph]] [[basic-block]]
│   ├── 1.2 program dependence graph (scanf defines, printf uses)
│   │       -> [[program-dependence-graph]] [[control-dependence]]
│   ├── 1.3 backward slices for line 13 and 14
│   │       -> [[program-slicing]]
│   └── 1.4 forward slice for `int i=1` at line 5
│           -> [[program-slicing]]
│
└── Task 2 — Inter-procedural CFG
    ├── C++ program with `add`, `sub` and a function pointer
    │   ├── `func = &add;` / `func = &sub;` by a parity test
    │   └── `y = func(a,b);` — indirect call
    └── inter-procedural CFG
            -> [[interprocedural-analysis]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[control-flow-graph]] | Nodes are basic blocks, edges are possible transfers of control; the loop header, the `if` body and the two loop exits are the interesting structure |
| [[basic-block]] | The unit the CFG is built from: a chain of statements guaranteed to execute one after the other |
| [[program-dependence-graph]] | Statement order disappears; what remains are control and data dependencies between statements |
| [[control-dependence]] | A controls B if A determines whether or how often B executes — the loop header and the `if` are the controlling nodes here |
| [[program-slicing]] | Forward slicing lists statements influenced by the criterion, backward slicing lists statements that influence it |
| [[interprocedural-analysis]] | Nodes are functions, calls are edges; a call through a function pointer makes the target set depend on the data flow, not the syntax alone |

## Lecture Structure

The sheet is one page with two tasks.

**Task 1** gives a fifteen-line C program that reads two integers with `scanf`, computes their
gcd with a `for` loop, derives `prod = x*y` and `lcm = prod/gcd`, and prints all three.

1. **Draw the intra-procedural CFG.** The loop with the compound condition `i <= x && i <= y`,
   the `if (x%i==0 && y%i==0)` body and the three `printf` statements are what it must show.
2. **Draw the program dependence graph.** One assumption is fixed: *scanf defines the variable
   and printf uses the variable*. It decides where the `scanf` nodes land and whether the
   `printf` statements appear as uses.
3. **Compute the backward slice for line 13** (`printf("prod=%d", prod);`) **and for line 14**
   (`printf("lcm=%d", lcm);`). They differ because `lcm` depends on `gcd`, assigned inside the
   loop.
4. **Compute the forward slice for `int i=1` at line 5.** The criterion is the loop
   initialiser; everything depending on `i` afterwards is in scope.

**Task 2** gives a C++ program with two trivial functions, `add` and `sub`, and a function
pointer `func` set to `&add` when `x` is even and to `&sub` otherwise, before the call
`y = func(a,b)`. The **inter-procedural CFG** must account for the called function not being
known statically at the call site.

Both the sheet and the slides say the homework is not corrected but is required to pass the
exam; the slides add that questions are "developed on blackboard together" — bring your own
ideas or there will not be a sample solution.

The deliverable belongs in `study/homework/reverse-and-reengineering/`, next to
`hw01-slices.py`, which models the program and computes the CFG edges, dependence edges and
the three slices. [[reverse-and-reengineering-exercise-1]] indexes it.

## Exam-Relevant Points

1. **The intra-/inter-procedural distinction** from the lecture's learning objectives is
   exactly what the two tasks apply: Task 1 stays inside `main`, Task 2 crosses functions.
2. **The modelling assumption in 1.2 is part of the question.** "scanf defines, printf uses"
   makes the `scanf` calls definition points and the `printf` calls use points, fixing the
   PDG's data-dependence edges.
3. **The two backward slices differ in one specific way**: the slice for line 14 reaches
   back through `lcm = prod/gcd` into `gcd = i` inside the loop; line 13's slice does not.
4. **A forward slice from `int i=1` grows through the loop** — `i` is the loop variable, so
   the loop condition, the `x%i` and `y%i` tests and `gcd = i` are downstream.
5. **The function-pointer program is the interprocedural trap.** The call has two possible
   targets and the branch on `x%2` decides which; both `add` and `sub` are reachable.
6. **Everything the sheet asks for is drawn, not computed numerically.** It is a modelling
   exercise, and the exam checks the graph structure.

## Connections

- [[reverse-and-reengineering]] — the course page, listing this sheet and its deliverable.
- [[reverse-and-reengineering-lecture-1]] — the lecture introducing CFGs, PDGs, slicing.
- [[reverse-and-reengineering-lecture-2]] — the binary-analysis half of the course.
- [[reverse-and-reengineering-exercise-2]] — the assembly-based follow-up sheet.
- [[control-flow-graph]] — the Semester 1 CFG page, the same structures, analysis side.
- [[program-dependence-graph]] — the Semester 1 PDG page, re-derived here.
- [[program-slicing]] — the Semester 1 slicing page, whose terminology the sheet uses.
- [[basic-block]] — the basic-block definition used to build the CFG.
- [[interprocedural-analysis]] — behind Task 2's call-graph-plus-CFG combination.
- [[software-analysis]] — the field these techniques belong to.

## Open Questions

- The sheet gives no marks, no due date and no submission channel, and states only that
  solutions should be brought to the tutorials for discussion.
- Task 1's program is printed with line numbers 1-15 but no separate listing of which line is
  which, so the "line 13" and "line 14" criteria are read off the listing.
- Task 2 says only "draw the inter-procedural CFG"; it does not say whether the two callees
  are merged into one super-node or kept as separate nodes from the call site.
- The sheet does not say whether the PDG for Task 1 includes the `printf` uses as nodes or
  only the data dependences between assignments.
