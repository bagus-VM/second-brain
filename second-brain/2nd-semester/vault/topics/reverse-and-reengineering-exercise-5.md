---
title: "Reverse- and Reengineering — Homework 5 Overview (Stack Frames and CFG Structuring)"
tags: [topic, reverse-and-reengineering, semester-2, exercise, assembly]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[reverse-and-reengineering-lecture-2]]", "[[reverse-and-reengineering-lecture-5]]"]
---

## One-line Summary
Homework 5 asks students to trace x86-64 stack arguments and reconstruct structured control flow from a goto-based intermediate program.

## Core Map

```
Homework 5 (dated 17 Nov 2026; discussion/submission details not stated)
├── Problem 1: program stack
│   ├── draw stack at call to swap
│   └── relate formal pointer parameters to main's local variables
└── Problem 2: intermediate representation
    ├── draw statement-level unstructured CFG
    ├── identify graph patterns
    ├── show iterative-refinement steps
    └── rewrite as structured code without goto
```

## Key Concepts at a Glance

| Page | What the sheet practices |
|------|--------------------------|
| [[x86-assembly-and-abi]] | Follow argument registers and stack-frame memory references in the listing. |
| [[control-flow-graph]] | Represent each statement as a node and each possible transfer as an edge. |
| [[structural-analysis-decompilation]] | Identify region patterns and describe iterative CFG refinement. |
| [[decompilation]] | Explain why the recovered structure is a plausible reconstruction rather than original source. |

## Exercise Structure

Problem 1 provides assembly listings for `swap(int*, int*)` and `main`. It asks for the stack at the call site and the relationship between the callee's formal pointer parameters and the caller's actual arguments. Problem 2 gives a goto-based function with branches and a loop that computes a recurrence. It asks for a statement-node CFG, observed patterns, every step of iterative refinement, and an equivalent structured program without `goto`.

The sheet says it is not for submission and encourages students to bring their own solutions to tutorial discussion. This page describes the tasks; it does not solve them.

## Exam-Relevant Points

- The System V x86-64 calling convention passes the first integer/pointer arguments in `rdi` and `rsi`; the provided assembly stores those pointers and dereferences them to access caller-owned locals.
- Keep a pointer parameter distinct from the pointed-to integer: the parameter's stack slot stores an address, and the load through that address reads the caller's variable.
- For the second task, preserve branch destinations and fall-through edges before identifying loop/conditional regions.
- Refinement may remove or virtualize edges that prevent a structured region match; document each transformation rather than jumping directly to a rewritten loop.
- Do not infer original source formatting from a reconstructed control-flow structure.

## Connections

- [[reverse-and-reengineering-lecture-5]] — decompilation and iterative structural analysis.
- [[reverse-and-reengineering-lecture-2]] — x86-64 registers, calling convention, and stack frames.
- [[control-flow-graph]], [[natural-loop]] and [[dominance]] — graph structures useful for the second problem.
- [[reverse-and-reengineering-exercise-4]] — prior sheet's assembly recovery and control-flow flattening.

## Open Questions

- The heading gives a date of 17.11.2026, but the sheet itself does not state a due date or discussion date.
- The PDF extraction preserves both listings but not all visual spacing; use the original PDF for exact diagram layout.
