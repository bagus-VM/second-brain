---
title: "Reverse- and Reengineering"
tags: [course, semester-2, reverse-and-reengineering]
professor: "Prof. Dr.-Ing. Christian Hammer"
semester: "WS 2026/27"
exam_date: "two dates via Campus Portal; Term 1 window 08.02.–05.03.2027 (sign-up 16.11.–15.12.2026), Term 2 window 22.03.–09.04.2027 (sign-up 01.03.–18.03.2027)"
credits: "6 ECTS"
language: "English"
source_count: 10
status: active
last_updated: 2026-11-12
prerequisites: ["Compiler construction or software analysis (lexing, parsing, intermediate representation)"]
---

## One-line Summary
What to do with code you are not allowed to read: recover its behaviour from its bytes, rebuild
its structure, and then rebuild it properly — the course's arc is *reverse engineering →
restructuring → forward engineering*.

## Course Information

- **Instructor:** Prof. Dr.-Ing. Christian Hammer (Chair of Software Engineering, FIM)
- **Tutor:** Dr. Mohammad Rezaalipour (named on both homework sheets)
- **Lecture:** 2 h/week, **Wednesday 12:15–13:45**
- **Tutorial:** 2 h/week, choose one slot — **Tuesday 14–16** or **Tuesday 16–18**
- **Total:** 6 ECTS
- **Recommended skills (from the slides):** Compiler construction *or* software analysis
  (lexing, parsing, intermediate representation)
- **Exams:** 2 dates, sign-up via **Campus Portal**
  - Termin 1, timeframe 08.02.–05.03.2027; sign-up 16.11.–15.12.2026; withdrawal until 11.01.2027
  - Termin 2, timeframe 22.03.–09.04.**2025** as printed; sign-up 01.03.–18.03.2027; withdrawal
    until 18.03.2027
  - **Total: 90 points, 90 minutes**
  - The slides carry the disclaimer: "NO guarantee, official: Prüfungssekretariat Uni Passau"
- **Homework rules (from the slides):**
  - "Homework not corrected" — but "required to pass exam"
  - "Thinking things through on your own makes you smarter; using LLM statistically leads to
    lower grades!"
  - Questions via **Stud.IP** (Tutorial); larger discussions by appointment with the tutor;
    homework questions are "developed on blackboard together"
  - "Bring your own ideas or there will not be a sample solution in the end"

## Content (as stated on the slides)

- Reverse engineering third-party programs in processor-specific binary formats as well as
  intermediate codes; effects of obfuscation techniques on this process.
- Transformation into a representation suitable for further processing; reconstruction of
  high-level data and control structures.
- Program analysis to improve program understanding.
- Automatic refactoring to improve program structure.

## Learning Outcomes (from the slides)

- Students are familiar with the techniques of analysis and refactoring of unspecified or
  outdated software systems, both with and without source code, in particular with the help of
  (semi-)automatic analysis.
- Students can independently create prototypical systems for reconstructing program semantics
  and transforming into a software-technically improved system.
- Students can support software development work by creating smaller, domain-specific systems
  to reconstruct program semantics or improve the structure of larger systems.

## Learning Objectives (the slide's own checklist)

1. Understand the concepts of **software aging, reengineering, refactoring, code smells**.
2. Explain the challenges of legacy systems and how they can be renewed.
3. Create simple **intra- and interprocedural control flow graphs** as well as **program
   dependence graphs**.
4. Understand and apply **program slicing**.
5. Explain the difference between **maintenance and reengineering**.

## The Reengineering Process (the spine of the course)

```
Reverse Engineering   ->   Program Code in poor Quality
Restructuring         ->   Rediscovered Requirements and Design
Forward Engineering   ->   Improved Requirements and Design
                       ->   Improved Code
```

Forward engineering runs the other way: abstract representation/model → concrete, physical
implementation.

## Lecture Index

Overview pages:
- [[reverse-and-reengineering-lecture-1]] — software aging, the reengineering process, reverse
  engineering, CFG/PDG/slicing, restructuring, refactoring, code smells, legacy systems
- [[reverse-and-reengineering-lecture-2]] — reverse engineering proper: goals and purposes, the
  abstraction ladder, binary analysis, static vs dynamic analysis, x86 assembly and the ia64 ABI
- [[reverse-and-reengineering-lecture-3]] — binaries: ELF, sections and segments, symbol tables,
  dynamic linking, GOT/PLT, eager vs lazy binding
- [[reverse-and-reengineering-lecture-4]] — disassembly (instruction decoding, linear sweep,
  recursive traversal) and obfuscation (packing, control-flow flattening, opaque predicates,
  function joining, virtualization, data-based obfuscation)
- [[reverse-and-reengineering-lecture-5]] — decompilation, intermediate representation, structural analysis and iterative CFG refinement
- [[reverse-and-reengineering-exercise-1]] — Homework 1 (20.10.2026): CFG, PDG, backward and
  forward slices, interprocedural CFG
- [[reverse-and-reengineering-exercise-2]] — Homework 2 (27.10.2026): x86 assembly → C, CFG of an
  assembly function, guessing what it computes
- [[reverse-and-reengineering-exercise-3]] — Homework 3 (03.11.2026): `sar` vs `shl` recovery, the
  intra- and interprocedural CFG of a three-way `max`
- [[reverse-and-reengineering-exercise-4]] — Homework 4 (10.11.2026): a pointer-based swap recovered
  from x86-64, and control-flow flattening of a `while` loop with its flattened CFG
- [[reverse-and-reengineering-exercise-5]] — Homework 5 (17.11.2026): call-stack tracing and CFG structuring

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 1 | Reengineering & software aging, reverse engineering workflow, control flow analysis, PDG, program slicing, restructuring, refactoring, code smells, architecture smells, legacy systems | `01-reengineering-intro.pdf` | ingested → [[reverse-and-reengineering-lecture-1]] |
| 2 | Reverse engineering: definition, goals, purposes, levels of abstraction, binary analysis, static and dynamic analysis, x86 registers/ISA/instructions/call stack, ia64 ABI | `02-reverse.pdf` | ingested → [[reverse-and-reengineering-lecture-2]] |
| 3 | Binaries: executable formats, ELF header/tables/sections/segments, symbol tables, dynamic linking, GOT/PLT, lazy linking | `03-binaries.key` (+ `03-binaries.pdf` export, 15 slides) | ingested → [[reverse-and-reengineering-lecture-3]] |
| 4 | Disassembly: instruction decoding, linear sweep vs recursive traversal, obfuscation, packing, control-flow obfuscation, virtualization, data-based obfuscation | `04-disasssembly.pdf` (23 slides) | ingested → [[reverse-and-reengineering-lecture-4]] |
| H1 | Homework 1 — intra-procedural CFG, PDG, backward slices (lines 13/14), forward slice (`int i=1`), interprocedural CFG | `hw01.pdf` | ingested → [[reverse-and-reengineering-exercise-1]] |
| H2 | Homework 2 — recover `bar` and `foo` from x86-64 assembly, intraprocedural CFG of an assembly `foo`, infer what it computes | `hw02.pdf` | ingested → [[reverse-and-reengineering-exercise-2]] |
| H3 | Homework 3 — `sar`/`shl` recovery from two listings, the CFG of a three-way `max`, intra- and interprocedural | `hw03.pdf` | ingested → [[reverse-and-reengineering-exercise-3]] |
| H4 | Homework 4 — `void decode(long *xp, long *yp)` recovered from x86-64 assembly; control-flow flattening of `bar` plus its flattened CFG | `hw04.pdf` | ingested → [[reverse-and-reengineering-exercise-4]] |
| 5 | Decompilation: intermediate representation, structural analysis, region matching and iterative refinement | `05-decompilation.pdf` (23 slides) | ingested → [[reverse-and-reengineering-lecture-5]] |
| H5 | Program stack and goto-based CFG reconstruction; sheet is not for submission | `hw05.pdf` | task overview → [[reverse-and-reengineering-exercise-5]] |

## Concept Pages

| Page | One-line idea |
|------|---------------|
| [[reengineering]] | Chikofsky/Cross's definition — examination and alteration of a subject system to reconstitute it in a new form |
| [[software-aging]] | Requirements drift and inappropriate feature growth erode structure; quality decays in five named ways |
| [[reverse-engineering]] | Recover components, relationships and abstractions without altering the system — and the three goals that make it worth doing |
| [[binary-reverse-engineering]] | The abstraction ladder from machine code to source, and how static and dynamic analysis each climb it |
| [[x86-assembly-and-abi]] | Registers, subregisters, CISC addressing, instruction classes, and the ia64 calling convention |
| [[refactoring-and-code-smells]] | Six named smells, what a smell obliges you to do, and the regression-testing burden of every refactoring |
| [[architecture-smell]] | Smells one level up: cyclic classes, deep hierarchies, oversized packages — and why they need humans, not tools |
| [[legacy-systems]] | Obsolete stacks, missing documentation, lost knowledge — and the paradox that these systems still run the company |
| [[legacy-system-renewal]] | Packing, migration, replacement in one fell swoop — three ways to renew, with different risk profiles |
| [[reengineering-vs-maintenance]] | Maintenance serves the customer and adapts; reengineering serves the developer and reconstitutes |
| [[elf-executable-format]] | The ELF container in two tables — segments for the loader, sections for the linker — and the six-step load sequence |
| [[elf-symbols-and-tables]] | What the compiler emits beyond code, and why `.symtab` can be stripped while `.dynsym` cannot |
| [[got-plt-lazy-linking]] | The two tables that make a call into a shared library possible, and eager vs lazy resolution |
| [[disassembly]] | Machine code back to mnemonics: variable-length opcodes, linear sweep, recursive traversal, and where each breaks |
| [[code-obfuscation]] | Semantics-preserving transformation against analysis — the taxonomy, the impossibility claim, and superlinear composition |
| [[control-flow-obfuscation]] | Flattening, opaque predicates, function joining, virtualization — hiding which block runs next |
| [[binary-packing]] | Encrypt after linking, decrypt at load time: the stub, the manual import resolution, the tail jump |
| [[dynamic-code-rewriting]] | Code that is not in the binary: runtime generation, self-modifying code, and unsetting W^X |
| [[decompilation]] | A source-like reconstruction of binary behavior, limited by information discarded or transformed by compilation |
| [[structural-analysis-decompilation]] | CFG region matching and edge refinement recover structured branches and loops |

## Homework

| Sheet | Deliverable | State |
|-------|-------------|-------|
| Homework 1 (20.10.2026) | `study/homework/reverse-and-reengineering/hw01-solution.md` + `hw01-slices.py` | **run**: CFG, PDG and all three slices computed by a script that models the program, not drawn by hand |
| Homework 2 (27.10.2026) | `study/homework/reverse-and-reengineering/hw02-solution.md` + `hw02-verify.py` | **run**: both functions recovered to C, the assembly CFG reconstructed, and the recovered semantics simulated instruction by instruction against the sheet's opcodes — `ALL CHECKS PASSED` |
| Homework 3 (03.11.2026) | `study/homework/reverse-and-reengineering/hw03-solution.md` + `hw03-verify.py` | **run**: `sar`/`shl` recovered and confirmed by an exact `-O0` round-trip; the `max` CFG reconstructed; the `>=` vs `>` question settled by compiling both |
| Homework 4 (10.11.2026) | `study/homework/reverse-and-reengineering/hw04-solution.md` + `hw04-verify.py` | **run**: the pointer swap recovered and verified four ways (listing simulation, exact `-O0` round-trip, the sheet's own listing assembled and executed, aliasing case); the flattened `bar` compiled and run against the original — both 5050 |

All four sheets state: "This sheet is not for submission. However, we strongly encourage you to solve
the problems and bring your solutions to the tutorials for discussion."

## Connections

- [[control-flow-graph]] — the Semester 1 page on CFGs; the intra/interprocedural distinction here
  is the same distinction from the analysis side.
- [[program-dependence-graph]] — the Semester 1 PDG page; this course re-derives it as a
  reverse-engineering tool.
- [[program-slicing]] — the Semester 1 slicing page; forward/backward slicing and the slicing
  criterion come from there.
- [[basic-block]] — the Semester 1 definition; the slide's "chain of statements that is guaranteed
  to be executed one after the other for as long as possible" is the same idea.
- [[code-clones]] — the duplication smell has a dedicated Semester 1 page.
- [[software-analyse]] — the Semester 1 course whose CFG/PDG/slicing machinery this course reuses
  on binaries and legacy code.
- [[software-analysis]] — the general field; the slides' reverse-engineering workflow (parsing →
  intermediate representation → component analysis → design recovery) is the SE pipeline run
  backwards.
- [[x86-assembly-and-abi]] — the RISC/CISC contrast and the x86 instruction classes from the
  assembly lecture.
- [[process-memory-layout]] — the Semester 2 VM course's account of the stack and frames that
  `x86-assembly-and-abi` depends on.
- [[dynamic-linking]] — relevant to the lecture's tool list (IDA, GCC CFG dumps, Eclipse source
  visualiser) and to the "reconstructing libraries" problem in binary analysis.

## Open Questions

- **The Term 2 exam timeframe is printed as "22.03. – 09.04.2025"** — a year before the course
  even runs. It is reproduced here as printed and flagged as a typo, not silently corrected.
- **The number of teaching units is not stated.** Four decks are now in `raw/` (lectures 1–4,
  numbered to 51, 27, 39 and 23 slides respectively — and lecture 3 exists twice, as a `.key`
  package and as a 15-page PDF export that omits the lecture-2 recap). The course outline's content
  list also promises decompilation and intermediate-code formats, which no ingested deck teaches.
- **Obfuscation is covered, but only as mechanism.** Lecture 4 delivers the taxonomy — packing,
  control-flow flattening, opaque predicates, function joining, virtualization, data-based
  obfuscation — with no lab, no sample binary and no tool walkthrough, and no sheet in `raw/`
  exercises it.
- **"Automatic refactoring" is promised in the content list and never appears.** Refactoring
  appears only as a manual activity.
- **How the two tutorials differ in content, and whether either is in English**, is not stated.
- **The exercise format is unstated.** The slides say homework is developed on the blackboard
  together, which contradicts a fixed sheet-with-questions model; the two sheets in `raw/` are
  practice material with no submission channel.
- **Whether the 90 points / 90 minutes split into a fixed number of questions** is not stated.
