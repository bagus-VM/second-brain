---
title: "Reverse- and Reengineering — Exercise 4 Overview (Homework 4: x86-64 Swaps and Control-Flow Flattening)"
tags: [topic, reverse-and-reengineering, semester-2, x86, obfuscation]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[x86-assembly-and-abi]]", "[[control-flow-obfuscation]]", "[[control-flow-graph]]"]
---

## One-line Summary
Homework 4 pairs the reading skill with the obfuscation skill: recover a pointer-based swap from a
frame-based listing, then take a loop apart with the flattening technique from lecture 4 and draw
what is left of its CFG.

## Core Map

```
Homework 4 (10.11.2026) — Prof. Hammer, Dr. Rezaalipour
│
├── Sheet framing
│   ├── "not for submission"; solve and bring solutions to the tutorials
│   └── one listing and one transformation, both purely lecture-4 material
│
├── Problem 1 — x86-64 Assembly
│   ├── `decode(long *xp, long *yp)` — 19 rows, Intel syntax, no size suffixes
│   ├── the frame: rdi/rsi spilled to [rbp-8]/[rbp-16]; [rbp-24]/[rbp-32] hold the pointees
│   ├── reads BOTH pointees before writing either
│   └── C: a = *xp; b = *yp; *yp = a; *xp = b
│       → [[x86-assembly-and-abi]] [[reverse-engineering]] [[disassembly]]
│
└── Problem 2 — Control-Flow Flattening
    ├── `bar()`: i = 1; while (i <= 100) s += i, i++; return s
    ├── 2.1 apply the technique: number the blocks, add a dispatcher,
    │       replace every control-flow instruction with "next = <number>"
    └── 2.2 draw the flattened CFG: one join point, successors as data
        → [[control-flow-obfuscation]] [[control-flow-graph]] [[basic-block]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[x86-assembly-and-abi]] | Arguments in `rdi`/`rsi` spilled to the frame; `[rbp-N]` slots are locals; the prologue/epilogue shape recurs in every listing on this sheet |
| [[reverse-engineering]] | The reading half: from machine code to equivalent C, with the *order of the stores* as the part that has to be exactly right |
| [[disassembly]] | Why the listing had to be recovered by position rather than with `pdftotext -layout`, and what the compiler round-trip proves about a recovered listing |
| [[control-flow-obfuscation]] | The transforming half: flattening defined, and why the loop edge disappears into a number |
| [[control-flow-graph]] | What problem 2 asks for a drawing *of* — after the transformation has removed the structure the drawing used to show |
| [[basic-block]] | The three blocks of `bar` are the units the technique numbers, so the exercise assumes exactly the lecture-4 definition |

## Exercise Structure

**Problem 1 — one listing, one function.** 19 rows including the label, in Intel syntax
(`qword ptr [rbp - 8]`, no `%` on registers) — the same dialect as homework 3, and the same frame
shape as homework 2: `push rbp`, `mov rbp, rsp`, spill, work, `pop rbp`, `ret`. What is new
relative to homework 3 is that the function takes **pointers**: the recovered C has to dereference
twice, and the listing's instruction order determines in which order the two writes happen. The
recovered function is a swap:

```c
void decode(long *xp, long *yp) {
    long a = *xp;
    long b = *yp;
    *yp = a;
    *xp = b;
}
```

**Problem 2 — one transformation, one drawing.** The sheet gives the nine-line `bar` and asks for
two things: apply control-flow flattening, and draw the corresponding flattened CFG. The
transformation is the lecture-4 recipe applied by hand — three blocks (test, body, after-loop),
numbered, with a dispatcher and a successor-number variable — and the drawing is the flattened
graph with its single join point. Both are written out on
`study/homework/reverse-and-reengineering/hw04-solution.md`, and both versions of the function were
compiled and run: `bar() = 5050` and `bar_flat() = 5050`.

## Exam-Relevant Points

- **The pointer-dereference pattern.** `mov rax, [rbp-8]` then `mov rax, [rax]` is
  "load the pointer, then load through it" — the two-step that turns a spilled argument into a
  value. Recognising it is what makes the recovered C possible at all.
- **Statement order is part of the answer.** Load-both-then-store-both is not the same *listing*
  as the obvious `t = *xp; *xp = *yp; *yp = t;`, which is why the compiler round-trip is the right
  check here rather than a plausibility argument.
- **Flattening is three steps, not an idea.** Number the blocks; add the dispatcher; convert every
  control-flow instruction into a successor number. An exam answer that says "add a switch" without
  the numbering and the successor writes is incomplete.
- **The flattened CFG has one edge shape.** Block → dispatcher → block. If a drawing still shows
  loops or branches, the transformation has not been applied.
- **This is a transformation to *produce*, not to recognise** — the sheet's phrasing is "apply the
  control-flow flattening technique", which is also the only place in `raw/` where the course asks
  for obfuscation to be written rather than described.

## Connections

- [[reverse-and-reengineering-lecture-4]] — the deck both problems come from: problem 1 is slide
  2–7 material, problem 2 is slides 15–18 material.
- [[reverse-and-reengineering-exercise-3]] — the previous sheet, and the same recovery skills with
  scalars rather than pointers.
- [[reverse-and-reengineering-exercise-2]] — the first assembly-to-C homework: same frame shape,
  AT&T listings; this sheet's Intel syntax matches homework 3.
- [[reverse-and-reengineering]] — the course page, whose lecture index carries this sheet's row.
- [[hw04-solution|the written solution]] — `study/homework/reverse-and-reengineering/hw04-solution.md`
  with the recovered C, the flattened C, the flattened CFG and the recorded run outputs.
- [[refactoring-and-code-smells]] — the same class of transformation with the opposite intent:
  flattening *removes* the structure a refactoring would restore.

## Open Questions

- **What the tutorial expects for the drawing.** "Draw the corresponding flattened control-flow
  graph" does not say whether spurious blocks or dead paths (which the lecture allows) should be
  added — the minimal three-block version is what is answered here.
- **Whether the block numbering starts at 0 or 1 matters nowhere**, but the sheet gives no example,
  so an answer that names the blocks differently is not thereby wrong.
- **The sheet's date (10.11.2026) is the only schedule information** — no discussion slot is printed
  on it, unlike the VMRS sheets, so which tutorial covers it is not stated.
- **No solution sheet exists** for homework 4 in `raw/`, so nothing external corroborates the two
  answers beyond the checks recorded on the solution page.
