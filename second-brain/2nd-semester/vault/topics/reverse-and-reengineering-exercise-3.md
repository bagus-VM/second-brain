---
title: "Reverse- and Reengineering — Exercise 3 Overview (Homework 3: x86 Shifts and the max CFG)"
tags: [topic, reverse-and-reengineering, semester-2, x86, reverse-engineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[x86-assembly-and-abi]]", "[[control-flow-graph]]"]
---

## One-line Summary
Homework 3 continues the ladder from homework 2 with two shift-only leaf functions and a
three-way `max` whose CFG — intra- and inter-procedural — has to be drawn from the jump
structure alone.

## Core Map

```
Homework 3 (3.11.2026) — Prof. Hammer, Dr. Rezaalipour
│
├── Sheet framing
│   ├── "not for submission"; solve and bring solutions to the tutorials
│   └── Intel syntax (dword ptr, no %) — hw02's AT&T listings are gone
│
├── Task 1 — x86 Assembly
│   ├── Listing 1: f1 — 15 sar 2 → arithmetic shift right → C: 15 >> 2
│   ├── Listing 2: f2 — 10 shl 2 → logical shift left  → C: 10 << 2
│   └── the trap: sar vs shr — arithmetic vs logical right shift
│       -> [[x86-assembly-and-abi]] [[reverse-engineering]]
│
└── Task 2 — Control Flow Graphs
    ├── max(a, b, c): three symmetric compare-pairs, each followed by a
    │       printf of the winning argument
    │   ├── 2.1 guess what max computes
    │   └── 2.2 draw the intra-procedural AND inter-procedural CFG
    │       -> [[control-flow-graph]] [[basic-block]] [[interprocedural-analysis]]
    └── main: 100, 200, 400 in stack slots, three argument registers, call max
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[x86-assembly-and-abi]] | Arguments arrive in `edi`, `esi`, `edx` and are spilled to `[rbp-N]`; the shift amount rides in `cl` |
| [[reverse-engineering]] | Task 1 is the code-level half: from machine code to equivalent C, with the shift semantics as the crux |
| [[control-flow-graph]] | The blocks and edges come from `cmp`/`jl` pairs and the fall-through structure — recovered from jumps, not source |
| [[basic-block]] | The listing's labels (`.L3`, `.L6`, `.L9`) delimit the blocks the CFG is assembled from |
| [[interprocedural-analysis]] | `main` calls `max` once with three register arguments; the call edge joins the two intraprocedural graphs |
| [[binary-reverse-engineering]] | The discipline applied to both tasks: reconstruct higher-level artefacts from the assembly |

## Exercise Structure

**Task 1 — two shift functions.** The two listings follow the same frame shape as homework 2
(`push rbp`, `mov rbp, rsp`, spill to stack slots, work, `pop rbp`, `ret`) but in **Intel
syntax** — `mov dword ptr [rbp - 4], 15`, no `%` registers. `f1` loads 15 and 2, moves them into
`eax` and `ecx`, and executes `sar eax, cl` — an *arithmetic* shift right, which for positive
values is C's `>>` on signed ints. The recovered C:

```c
int f1(void) { int x = 15; int y = 2; return x >> y; }
int f2(void) { int x = 10; int y = 2; return x << y; }
```

The semantics check matters: `sar` versus `shr` differ for negative operands, and the sheet's
use of `sar` is exactly the kind of detail reading alone can get wrong.

**Task 2 — the `max` CFG.** `max` compares its three arguments pairwise — first `a` against `b`
and `c`, then `b` against `a` and `c`, then `c` against `a` and `b` — and prints the winning
argument with `printf("%d is the largest number.", …)`. The asks: guess what `max` computes, and
draw **both** the intra-procedural CFG (one graph per function, blocks delimited by the `.L3`,
`.L6`, `.L9` labels) and the inter-procedural CFG (the two graphs joined by main's `call max`
edge, arguments in `edi`/`esi`/`edx`). `main` itself is small: three constants into stack slots,
three into argument registers, call, `xor eax, eax`, return.

**How the homework deliverable was verified.** `hw03-verify.py` (in
`study/homework/reverse-and-reengineering/`) does two independent checks, both recorded in
`output-hw03-verify.txt`: a semantic simulation of the recovered C compared instruction-by-
instruction with the sheet's machine code, and a **compiler round-trip** — the recovered C
compiled at `-O0` and its generated mnemonics compared with the sheet's listing, matching
exactly, instruction for instruction. The round-trip settles two things reading alone leaves
open: that `sar` is really `sar`, and that the effective comparison in Task 2 is `>=`, not `>`
(the fall-through path also fires on equality — the "largest" value is printed once, by the
first argument that is not smaller than either rival).

## Exam-Relevant Points

1. **`sar`/`shr`/`sal`/`shl` is the semantic minefield of Task 1** — arithmetic versus logical
   right shift only differs on negatives, which is exactly where a silent misreading hides.
2. **The shift amount must be in `cl`** — the two-instruction dance `mov eax, …` / `mov ecx, …`
   before the shift is the ABI in action.
3. **Task 2's CFG has to be recovered from jumps, not source** — every `jl` has a taken and a
   fall-through edge, and the three compare-pairs give `max` a symmetric block structure.
4. **Intra- vs inter-procedural is a named distinction this time** — homework 2 only asked for
   the intraprocedural graph; here both are required, so the `call max` edge and the argument
   registers are examinable.
5. **"Guess what max computes" is checkable** — the same verify-by-simulation discipline as
   homework 2's `foo`, now with the compiler round-trip added as a second witness.
6. **The syntax switched from AT&T (hw02) to Intel (hw03)** — reading both fluently is part of
   the course's implicit training goal.

## Connections

- [[reverse-and-reengineering-lecture-3]] — the binaries lecture whose file-format half this
  sheet's sibling material covers; the assembly half feeds this sheet.
- [[reverse-and-reengineering-lecture-2]] — the x86 lecture the sheet applies.
- [[reverse-and-reengineering-lecture-1]] — where CFGs and basic blocks were introduced.
- [[reverse-and-reengineering-exercise-2]] — the direct predecessor: same frame shape, same
  recover-C-and-draw-CFG shape, AT&T there, Intel here.
- [[reverse-and-reengineering-exercise-1]] — the graph-construction sheet that started the
  ladder.
- [[x86-assembly-and-abi]] — registers, subregisters, the ABI's argument registers, shifts.
- [[control-flow-graph]], [[basic-block]], [[interprocedural-analysis]] — the CFG toolkit.
- `study/homework/reverse-and-reengineering/hw03-solution.md` — the worked solution;
  `hw03-verify.py` / `output-hw03-verify.txt` — the verification evidence.

## Open Questions

- The sheet gives no marks and no submission channel; it is explicitly not for submission, with
  solutions brought to the tutorials for discussion.
- Whether the inter-procedural CFG should show the `printf` calls as nodes with their own
  (library) graphs or terminate at the call edge is not specified.
- The equality case in `max` — which argument prints when two are equal — is decided by the
  fall-through structure, but the sheet never asks about it explicitly; only the round-trip
  evidence in the homework pins it down.
- Task 1's functions take no arguments and return constants folded through shifts; whether an
  exam variant would generalise to parameterised shifts is unknown.
