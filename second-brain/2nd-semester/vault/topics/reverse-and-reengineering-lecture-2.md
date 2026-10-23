---
title: "Reverse- and Reengineering — Lecture 2 Overview (Reverse Engineering Proper, Binary Analysis and x86)"
tags: [topic, reverse-and-reengineering, semester-2, reverse-engineering, x86]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Lecture 2 gives reverse engineering its definition, its ladder of artefacts, its static and
dynamic toolkits, and the x86 instruction set you need to read machine code.

## Core Map

```
Lecture 2 — Reverse Engineering (27 slides)
│
├── Disclaimer (slide 1)
│   ├── "may be illegal depending on purpose and situation";
│   │   Directive 2009/24/EC + national laws
│   └── for legacy code you may reverse
│        -> [[reverse-engineering]]
│
├── Origins and definition (slides 2-5)
│   ├── origin: hardware analysis; disassemble to copy or fix
│   ├── Chikofsky/Cross 1990: understand a system, discover relationships,
│   │   generate abstractions, "no alteration"
│   ├── goals: features, structure, functionality, dynamic behaviour,
│   │   rationale, construction
│   └── purposes: semantics, reengineering, bugs, audits, malware forensics,
│       protocol analysis, business model, IP
│
├── Process (slides 6-9)
│   ├── reversing forward engineering; problem: lost info
│   ├── data acquisition -> knowledge organization -> exploration
│   └── control flow, data flow, dependences
│
├── Abstraction levels (slides 10-12)
│   ├── worst case object code -> best case source (maybe cryptic)
│   ├── common goal: IR suitable for further analysis
│   └── code level vs system level
│        -> [[binary-reverse-engineering]]
│
├── Static and dynamic analysis (slides 13-14)
│   ├── static: disassembly, control flow reconstruction, decompilation
│   │   (undecidable), detection; headers, imports
│   ├── dynamic: observe behaviour, execute (VM/emulator for malware)
│   └── debugging vs fuzzing, symbolic execution; call monitoring
│        -> [[static-vs-dynamic-analysis]] [[symbolic-execution]] [[debugging]]
│
├── x86 evolution and registers (slides 15-17)
│   ├── 8086/8088 real mode -> 80286 protected mode -> ia32 -> Pentium
│   │   MMX/SIMD -> 64-bit, 32-bit regs and address space
│   ├── 16/32-bit: (e)ip (e)sp (e)bp ax bx cx dx si di, cs ds ss es,
│   │   FP stack st(0)-st(7), eflags, mmx0-7
│   └── 64-bit: rip rsp rbp, rax-r15, xmm0-xmm15
│
├── ABI and subregisters (slides 18-19)
│   ├── volatile: RAX RCX RDX R8 R9 R10 R11, XMM0-5
│   ├── nonvolatile: RBX RBP RDI RSI RSP R12-R15, XMM6-15
│   ├── integer args RCX RDX R8 R9, more params on the stack
│   │   right-to-left; FP args XMM0L-3L; return RAX or XMM0
│   └── writing eax zeroes the upper 32 bits; ax/al/ah do not
│        -> [[x86-assembly-and-abi]]
│
├── ISAs and instructions (slides 20-25)
│   ├── RISC (MIPS) vs CISC (x86): three- vs two-address code,
│   │   encoding 1-15 bytes variable length
│   ├── opcode + operands: register, immediate, memory address
│   ├── base + index*scale + displacement addressing
│   └── arithmetic, bitvector, jmp/call/ret, lea, push/pop, cmp/test
│
└── Call stack (slide 25)
    ├── prologue: push rbp, mov rbp rsp, save registers, sub rsp
    └── epilogue: add rsp, pop registers, pop rbp, ret
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[reverse-engineering]] | Understand a system by identifying its artifacts, discovering their relationships and generating abstractions, with no alteration at all |
| [[binary-reverse-engineering]] | The ladder from object code up to source; code level and system level; static and dynamic techniques climbing toward an IR |
| [[x86-assembly-and-abi]] | A CISC ISA with variable-length encoding, powerful addressing modes and an inhomogeneous register file, plus the calling convention |
| [[static-vs-dynamic-analysis]] | Static analysis cannot prove reachability; dynamic analysis sees only what was exercised |
| [[symbolic-execution]] | The (semi-)automatic counterpart to manual debugging in the tool list |
| [[debugging]] | The manual, user-mode or kernel-level counterpart to fuzzing |

## Lecture Structure

1. **Disclaimer** — reverse engineering may be illegal depending on purpose and situation,
   Directive 2009/24/EC, and the student's own responsibility.
2. **Origins and the Chikofsky/Cross definition** — hardware analysis, disassembling a product
   to copy a competitor or repair an owned one; the 1990 taxonomy; six goals; ten purposes.
3. **The process** — reversing forward engineering, lost information, and the three steps:
   data acquisition, knowledge organization, exploration.
4. **Levels of abstraction and binary analysis** — the ladder, the common goal of an IR, and
   source-to-binary correspondence when source exists.
5. **Static and dynamic analysis** — code level and system level for each; decompilation marked
   *undecidable*; VMs for legacy code.
6. **x86** — evolution, registers, subregister rules, the ABI's volatile/nonvolatile split,
   RISC vs CISC, instruction classes, and the call stack prologue and epilogue.
7. **References** — Chu et al., O'Brien at CMU, Kinder at UBW.

## Exam-Relevant Points

1. **The definition with the "no alteration" clause** — reverse engineering stops at
   understanding; alteration belongs to restructuring.
2. **The six goals and the ten purposes** — enumerable lists, easiest marks.
3. **The abstraction ladder and the common goal**: an IR suitable for analysis.
4. **The three-step process** and the central problem of lost information.
5. **Static versus dynamic analysis**, including that decompilation is *undecidable* and
   control-flow reconstruction *non-trivial*.
6. **The ABI's volatile/nonvolatile split**, the four integer argument registers, the
   right-to-left stack convention, and the return in RAX or XMM0.
7. **The partial-register rule**: writing eax zeroes the upper half of rax; ax, al, ah do not.
8. **The addressing-mode encoding** `base + index*scale + displacement`, and two-address CISC
   vs three-address RISC arithmetic.

## Connections

- [[reverse-and-reengineering]] — the course page, whose content list promises more than these
  lectures deliver.
- [[reverse-and-reengineering-lecture-1]] — the conceptual half: aging, reengineering, CFG,
  PDG, slicing.
- [[reverse-and-reengineering-exercise-1]] — Homework 1, the graph-construction side.
- [[reverse-and-reengineering-exercise-2]] — Homework 2, applying this lecture's assembly.
- [[binary-reverse-engineering]] — the concept page for the ladder and analysis levels.
- [[x86-assembly-and-abi]] — registers, subregisters, addressing, calling convention.
- [[static-vs-dynamic-analysis]] — the Semester 1 page for the two technique families.
- [[symbolic-execution]] — the Semester 1 page for the (semi-)automatic dynamic technique.
- [[debugging]] — the manual counterpart, user-mode and kernel-level.
- [[process-memory-layout]] — the stack and frames the call-stack slides assume.

## Open Questions

- The disclaimer names Directive 2009/24/EC and national laws but does not say how the course
  distinguishes the permitted case (your own or licensed code) from the prohibited one.
- Slide 10's ladder and slide 12's two levels are images whose ordering is not fully legible in
  the text layer, so bytecode vs machine code placement is inferred.
- The lecture names IDA only in lecture 1; no disassembler is demonstrated here, so the
  expected workflow is not shown.
- The ia64 ABI slide is the source's own naming; nothing states how it relates to the System V
  AMD64 convention GCC emits, which matters for Homework 2.
