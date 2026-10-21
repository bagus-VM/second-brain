---
title: "Virtual Machines and Runtime Systems — Lecture 2 Overview (The C runtime system)"
tags: [topic, virtual-machines, semester-2, c-runtime]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[virtual-machines-and-runtime-systems-lecture-1]]"]
---

## One-line Summary
Everything the C runtime system does at run time: process memory layout and the loader, dynamic
libraries and `dlopen`, error handling without exceptions (`errno`, `longjmp`, signals), and how
those same mechanisms implement thread scheduling and language-level exception handling.

## Core Map

```
Lecture 2 — The C runtime system
│
├── 1. The C runtime system                    -> [[runtime-system]]
│   ├── low abstraction over the kernel; tasks: memory, processes/signals, I/O,
│   │   error handling, strings, threads
│   ├── C standard library timeline (K&R -> C89 -> C99 -> C11 -> C17)
│   ├── POSIX standard library
│   ├── processes and memory layout           -> [[process-memory-layout]]
│   │   └── text | data | BSS | heap ↔ mmap ↔ stack | kernel
│   └── libraries: static vs dynamic          -> [[dynamic-linking]]
│       └── compilation pipeline, ld.so, -fPIC, dlopen/dlsym, mmap
│
├── 2. Error handling in C
│   ├── errno, return-value conventions       -> [[errno-error-handling]]
│   ├── longjmp / setjmp                      -> [[setjmp-longjmp]]
│   └── signals, handlers, sigaction          -> [[unix-signals]]
│       └── reentrancy vs thread safety
│
├── 3. Applications of longjmp and signals
│   ├── thread scheduling with longjmp + alloca + setitimer
│   │                                        -> [[thread-emulation-longjmp]]
│   └── exception handling                   -> [[exception-handling-implementation]]
│       ├── dynamic stack of handlers
│       └── static handler table
│
└── 4. Interactions with other runtime systems
    └── higher-level runtimes built on the C runtime: unintended interactions
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[runtime-system]] | (from lecture 1, extended here) the C runtime as a thin wrapper over the kernel, and why most higher-level runtimes sit on top of it |
| [[process-memory-layout]] | text/data/BSS/heap/stack plus the mmap area, virtual vs physical memory, page tables, PE/ELF/Mach-O — measured with `addrs.c` |
| [[dynamic-linking]] | Static vs shared libraries, the compilation pipeline, `ld.so`, `-fPIC`/relocations, `dlopen`/`dlsym`, `mmap` semantics |
| [[errno-error-handling]] | Return-value error signalling, the wrong `errno` pattern and why it is wrong, `EINTR` retry loops |
| [[setjmp-longjmp]] | Saving/restoring the execution context, registers (RIP/RBP/RSP), and the `volatile` local-variable trap |
| [[unix-signals]] | The signal catalogue, default dispositions, `sigaction`, masks, `sigsetjmp`, reentrancy vs thread safety |
| [[thread-emulation-longjmp]] | Emulating threads with `longjmp` + `alloca` stacks, `schedule()`, and `setitimer`-driven preemption |
| [[exception-handling-implementation]] | Why zero-cost-throwing matters, dynamic handler stack vs static handler table, and the cost comparison |

## Lecture Structure

1. **C runtime system** — its role, the standard-library timeline, POSIX, processes and memory layout,
   binary formats, libraries, the compilation pipeline, linker flags, `dlopen`/`dlsym`, the mmap area,
   `mmap()` semantics, and `ld.so` with `-fPIC` and relocations.
2. **Error handling in C** — `errno` and the correct/incorrect usage patterns, `strerror`/`perror`,
   then `setjmp`/`longjmp` with the register-level explanation and the `volatile` argument.
3. **Signals** — the catalogue, three possible responses, blocking, `sigaction` versus `signal`,
   signals + `longjmp`, `sigsetjmp`/`siglongjmp`, reentrancy versus thread safety, `EINTR` and
   `SA_RESTART`.
4. **Applications** — thread scheduling with `longjmp`/`alloca` and a timer, and exception handling
   with both implementation strategies and their runtime costs.
5. **Interactions with other runtime systems** — why higher-level runtimes depend on the C runtime and
   what can go wrong when programs reach through it.

## Exam-Relevant Points

1. **Draw the process memory layout** and place the mmap area. Explain how heap and stack growing into
   each other terminates a process, and why the sum of virtual address spaces can exceed physical RAM.
2. **Static vs dynamic linking** end to end: what happens at link time, what `ld.so` does at run time,
   why `-fPIC` exists, what relocation tables are for.
3. **`dlopen`/`dlsym` — including that a `NULL` symbol address is not a reliable error indicator.**
   Use `dlerror()` before and after.
4. **The `errno` trap**: it can be set even on success. Check the return value first; the exception is
   documented cases like `getpriority` returning a legitimate `-1`.
5. **`longjmp` mechanics**: which registers are restored, why the `setjmp` frame must still exist, and
   why a local variable modified in between must be `volatile`.
6. **Reentrancy vs thread safety**, with the `malloc`-in-a-signal-handler example: not allowed, because
   `malloc` touches global heap state.
7. **Exception handling costs**: the two strategies and the point that non-throwing code must not pay
   for exception tests.

## Connections

- Exercise Sheet 1 (dynamic libraries + JIT): `study/homework/virtual-machines-and-runtime-systems/sheet-01/`
  and [[virtual-machines-and-runtime-systems-exercise-1]] — the `addrs.c` measurements here come
  straight from lecture 2's memory-layout slides.
- [[virtual-machines-and-runtime-systems]] — course page (syllabus, exam dates).
- [[virtual-machines-and-runtime-systems-lecture-1]] — the definitions this lecture operationalises.

## Open Questions

- **The slide 52 cost-comparison table extracts with interleaved cells.** The rows appear as
  entry/exit/find/jump with O(c)/O(1) vs none, O(k) vs none, O(1) vs O(d·n) or optimised, O(1) vs O(1);
  the assignment of the `O(k)` entry to a specific row is a reconstruction, not a literal reading.
  Check the original PDF before quoting it.
- Garbage collection, interpreters/compilers for VMs, instrumentation, and containers are all on the
  syllabus but not yet taught.
- The lecture asserts that higher-level runtimes on top of the C runtime cause "unintended
  interactions" without giving the taxonomy of failures.
