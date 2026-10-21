---
title: "Virtual Machines and Runtime Systems — Lecture 1 Overview (Introduction)"
tags: [topic, virtual-machines, semester-2, virtualization]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Three definitions that the rest of the course leans on: abstraction (loses detail) versus
virtualization (preserves state transitions), emulation (behaviour) versus simulation (internals), and
what separates a runtime system's API from a virtual machine's instruction set.

## Core Map

```
Lecture 1 — Introduction
│
├── Abstraction vs virtualization            -> [[virtualization-vs-abstraction]]
│   ├── abstraction: neglect non-essential details, hierarchy of interfaces
│   │   (SATA -> AHCI -> block device -> file I/O -> FILE* -> java.io)
│   ├── virtualization: injective map V with V∘σ = σ'∘V
│   └── worked example: Java `iadd` vs four x86 instructions
│
├── Emulation vs simulation
│   ├── emulation: recreate observable behaviour (semantics)
│   └── simulation: also recreate internal processes (timing, caches)
│
├── Runtime system                            -> [[runtime-system]]
│   ├── services at run time, explicit (malloc) or implicit (thread scheduling)
│   ├── abstracts the OS, incompletely (man 2 signal)
│   └── defines an API -> source-level compatibility, recompile per platform
│
└── Virtual machine
    ├── defines an API *and* the instruction set -> ABI or ISA
    ├── Java: class library + bytecode
    └── QEMU/VMware/VirtualBox: x86/x86_64 + emulated hardware interfaces
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[virtualization-vs-abstraction]] | The formal definition with injectivity, why injectivity is required, and the `iadd` example that separates abstraction, virtualization and emulation |
| [[runtime-system]] | What a runtime system provides, how it differs from an OS *and* from a VM (API vs instruction set), and the examples that make it concrete |

## Lecture Structure

1. **Virtualization vs abstraction** — definitions, the abstraction hierarchy example, the formal
   virtualization condition, and why V must be injective.
2. **Example** — Java bytecode `iadd` against `popl/popl/addl/pushl`, showing all three relations on
   the same instruction.
3. **Emulation vs simulation** — observable behaviour versus internal processes, with the
   microprocessor example (clock cycles, cache behaviour).
4. **Virtualization as multiple independent instances** — threads/processes, virtual memory, file
   systems, windows/display managers, network sockets.
5. **Runtime system** — services, explicit vs implicit use, OS abstraction (incomplete), resource
   virtualization, and the fuzzy OS boundary.
6. **Virtual machine** — API plus instruction set; ABI/ISA distinction; Java and hypervisor examples.

## Exam-Relevant Points

1. **State the virtualization definition formally** including injectivity, and explain what breaks
   without it: two guest states would collapse into one host state and H would become an abstraction
   of G.
2. **Distinguish abstraction / virtualization / emulation on a concrete instruction** — the course
   literally supplies the `iadd` worked example.
3. **Emulation vs simulation**: simulation reproduces internals (timing, caches), emulation only the
   observable result.
4. **Runtime system vs virtual machine**: API (source-level compatibility, recompile) versus
   instruction set (binary compatibility). Java and QEMU are the two examples to have ready.
5. **List the canonical virtualized resources** with one example each.

## Connections

- [[virtual-machines-and-runtime-systems]] — course page (schedule, exam dates 11.02.2027 and
  01.04.2027, syllabus).
- [[virtual-machines-and-runtime-systems-lecture-2]] — the C runtime system, where the abstract
  definitions become machines-layout and library-loading detail.
- [[process-memory-layout]] — virtual memory is the most familiar instance of the formal definition.

## Open Questions

- Where exactly is the boundary between an operating system and a runtime system? The lecture says it
  is "not always clearly defined" — likely an exam question with no crisp answer.
- The slide says virtual machines may define an ABI *or* an ISA "discussed in more detail later"; that
  distinction has not been unpacked yet.
- Containers are on the syllabus but are not touched in this lecture.
