---
title: "Reverse- and Reengineering — Exercise 2 Overview (Homework 2: x86 Assembly to C and Assembly CFG)"
tags: [topic, reverse-and-reengineering, semester-2, x86, reverse-engineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Homework 2 puts the lecture's x86 material to work: recover two functions' arguments and
their equivalent C from assembly, then draw the CFG of an assembly `foo(int)` and work out
what it computes.

## Core Map

```
Homework 2 (27.10.2026) — Prof. Hammer, Dr. Rezaalipour
│
├── Sheet framing
│   ├── "not for submission"; solve and bring solutions to the tutorials
│   └── slides: homework "not corrected" but "required to pass"
│
├── Task 1 — x86 Assembly
│   ├── two side-by-side listings, AT&T syntax
│   │   ├── Listing 1 = bar, Listing 2 = foo
│   │   └── the text layer interleaves the two columns
│   └── "Identify the function arguments and write the equivalent C programs"
│        -> [[x86-assembly-and-abi]] [[reverse-engineering]]
│
└── Task 2 — Control Flow Graph
    ├── an assembly `foo(int)` with .L2/.L3/.L4/.L5/.L6 labels
    ├── a `main` that reads a number, calls foo(int), prints the result
    ├── 2.1 draw the intraprocedural CFG for foo
    │       -> [[control-flow-graph]] [[basic-block]]
    ├── 2.2 which functions are called from main
    │       -> [[interprocedural-analysis]]
    └── 2.3 guess what foo computes
            -> [[reverse-engineering]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[x86-assembly-and-abi]] | Reading assembly means knowing the ISA: the calling convention decides where the arguments are, the frame layout what each `[rbp-N]` slot holds |
| [[reverse-engineering]] | Recovering an equivalent C program from machine code is the code-level half of reverse engineering — identify artifacts, discover relationships, generate an abstraction |
| [[control-flow-graph]] | The assembly function's CFG is recovered from the jump structure: `jg`, `jne`, `jle` and the `jmp` labels define the blocks and the edges |
| [[basic-block]] | In assembly the blocks are delimited by labels and by the jump instructions, the same notion as the source-level basic block |
| [[interprocedural-analysis]] | `main` calls `__isoc99_scanf`, `foo(int)` and `printf`; knowing which functions are called turns per-function graphs into an interprocedural one |
| [[binary-reverse-engineering]] | The discipline this sheet applies: reconstruct higher-level constructs from a lower-level representation |

## Lecture Structure

The sheet is one page with two tasks.

**Task 1** prints two assembly listings side by side and says: "The two assembly programs
below define two functions: foo and bar. Identify the function arguments and write the
equivalent C programs." Listing 1 is `bar`, Listing 2 is `foo`. Both use AT&T syntax with `%`
for registers — `mov dword ptr [rbp - 4], edi` — and follow the frame shape `push rbp`,
`mov rbp, rsp`, spill arguments to stack slots, do the work, then `pop rbp` and `ret`.

One note about the artefact: the PDF's text layer **interleaves the two side-by-side
columns**, so the extracted text of each numbered line mixes the two functions. The listings
therefore have to be **reconstructed by column** before they can be read, and that
reconstruction is documented in this sheet's homework deliverable: `hw02-verify.py` performs
the column split and checks the recovered functions against the assembly.

**Task 2** prints an assembly `foo(int)` and a `main`, and asks three things:

1. **Draw the intraprocedural CFG for the function foo.** The listing uses the labels `.L2`,
   `.L3`, `.L4`, `.L5`, `.L6` and the jumps `jg .L2`, `jne .L4`, `jle .L6`, so blocks and edges
   are visible in the listing.
2. **What are the functions called from main?** `main` reads an integer with
   `__isoc99_scanf`, moves it into `edi`, calls `foo(int)`, stores the result and prints it
   with `printf`.
3. **Guess what the function foo computes.** The body keeps two running values in stack
   slots, compares the argument against 1 and 2, and loops from a third slot — a recurrence,
   identified by checking the recovered function against a computed sequence.

The deliverable belongs in `study/homework/reverse-and-reengineering/`, next to
`hw02-verify.py`, which reconstructs the two listings by column and checks the recovered
functions against the assembly over the truth table and over a range of inputs.
[[reverse-and-reengineering-exercise-2]] is the vault-side index for that deliverable.

## Exam-Relevant Points

1. **The calling convention is what makes argument recovery possible.** Integer arguments
   arrive in `RCX`, `RDX`, `R8`, `R9`, and the callee spills them to `[rbp-4]`, `[rbp-8]`,
   `[rbp-12]`. That spill sequence is Task 1's first step.
2. **Task 1 asks for the equivalent C, and the C must have the same semantics** — the same
   arguments, the same return value.
3. **The CFG of Task 2 has to be recovered from jumps, not from source.** Every conditional
   jump has a true and a false edge, and the unconditional `jmp`s stitch the blocks
   together.
4. **The `main` listing is the interprocedural part**: it shows the call to `foo(int)` with
   the argument in `edi`, so the graph for `main` hangs off that edge.
5. **"Guess what foo computes" is checkable.** A candidate can be verified against the
   assembly by running the two side by side over a range of inputs, as the script does.
6. **Both tasks are exam-shaped**: given a binary artefact, produce the analysis artefacts
   (equivalent source, CFG, identified behaviour) lecture 2 names.

## Connections

- [[reverse-and-reengineering]] — the course page, listing this sheet and its deliverable.
- [[reverse-and-reengineering-lecture-2]] — the lecture whose x86 half this sheet applies.
- [[reverse-and-reengineering-lecture-1]] — where CFGs and basic blocks were introduced.
- [[reverse-and-reengineering-exercise-1]] — the graph-construction sheet, this one's
  predecessor.
- [[x86-assembly-and-abi]] — registers, subregisters, the ABI's volatile split, addressing
  modes.
- [[binary-reverse-engineering]] — the concept page for the ladder and analysis levels.
- [[reverse-engineering]] — the definition behind Task 1.
- [[control-flow-graph]] — the Semester 1 CFG page, now applied to assembly.
- [[basic-block]] — the unit the assembly CFG is assembled from.
- [[interprocedural-analysis]] — the call-graph view behind question 2.2.

## Open Questions

- The sheet gives no marks, no due date and no submission channel, and states only that
  solutions should be brought to the tutorials for discussion.
- The two listings are printed side by side and their text layers interleave, so which
  instruction belongs to which function is a decision the sheet leaves open.
- The sheet calls the functions `foo` and `bar` while Listing 1 is labelled `bar` and Listing 2
  `foo`; the ordering is recoverable only from the text, and "guess" in 2.3 carries no stated
  criterion for a sufficient answer.
- The functions' argument counts are not stated, so whether the recovered C takes one
  argument or several comes from the spill sequence.
