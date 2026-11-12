---
title: "Virtual Machines and Runtime Systems"
tags: [course, semester-2, virtual-machines]
professor: "Armin Größlinger"
semester: "WS 2026/27"
exam_date: "2027-02-11"
credits: "6 ECTS"
language: "English"
source_count: 8
status: active
last_updated: 2026-11-12
prerequisites: []
---

## One-line Summary
What sits between your program and the hardware: the C runtime system, processes, dynamic libraries, error handling — and how virtual machines and containers virtualize all of it.

## Course Information

- **Lecturer:** Armin Größlinger (IM 103, armin.groesslinger@uni-passau.de) — lectures and tutorials
- **Lecture:** Tuesday 16:00–17:30, (IM) SR 007
- **Tutorial:** Wednesday 12:15–13:45, (IM) HS 12
- **Credits:** 6 ECTS — Master Informatik, Modulgruppe "Programmierung und Softwaresysteme"
- **Exam:** written, 90 minutes — 1st: Thursday 11.02.2027, 14:00–15:30; 2nd: Thursday 01.04.2027, 14:00–15:30 (rooms via Stud.IP). Register via Campus Portal in time.
- **Literature:** J. Smith, R. Nair, *Virtual Machines*, Morgan Kaufmann, 2005

## Syllabus

1. **Introduction to virtualization** → [[virtualization-vs-abstraction]]
2. **Runtime systems**
   - C runtime system → [[runtime-system]]
   - processes → [[process-memory-layout]]
   - thread scheduling → [[thread-emulation-longjmp]]
   - memory management
   - runtime systems for high-level languages → [[exception-handling-implementation]]
3. **Virtual machines** — types (system VMs, process VMs, high-level-language VMs); implementation (interpreter, compiler, garbage collection); instrumentation; applications
4. **Containers** ("light-weight virtualization") — Linux namespaces, Kubernetes

## Tutorial Notes

- Languages: C and C++, maybe Rust.
- 21 October: quick C/C++ introduction. **No tutorial on 14 October.**
- C reference: *The C Book* (publications.gbdirect.co.uk/c_book/); C++: cplusplus.com

## Lecture Index

Overview pages:
- [[virtual-machines-and-runtime-systems-lecture-0]] — organisational matters (exam dates)
- [[virtual-machines-and-runtime-systems-lecture-1]] — Introduction to virtualization
- [[virtual-machines-and-runtime-systems-lecture-2]] — The C runtime system
- [[virtual-machines-and-runtime-systems-lecture-3]] — Abstract C machine, undefined behavior, Prolog and the Warren Abstract Machine
- [[virtual-machines-and-runtime-systems-exercise-1]] — Sheet 1 (dynamic libraries, JIT)
- [[virtual-machines-and-runtime-systems-exercise-2]] — Sheet 2 (signals, threads, `printf` race)
- [[virtual-machines-and-runtime-systems-exercise-3]] — Sheet 3 (exceptions, memory management, `LD_PRELOAD` allocator)

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 0 | Organisation | `s00.pdf` | ingested → [[virtual-machines-and-runtime-systems-lecture-0]] |
| 1 | Virtualization vs. abstraction, emulation vs. simulation, runtime system, VM | `s01.pdf` | ingested → 2 pages |
| 2 | C runtime system: libraries, memory layout, errno, longjmp, signals, exceptions | `s02.pdf` | ingested → 6 pages |
| 2 | Example programs for `s02`: the two exception strategies (`dyn_ex.c`, `static_ex.c`) and a complete `sbrk` allocator (`libmemory.c`) | `Example_programs_for_s02/exception/`, `.../mem/` | ingested, built and run → [[virtual-machines-and-runtime-systems-lecture-2]] |
| S1 | Dynamic libraries in C; primitive JIT compiler | `01.pdf`, `addrs.c`, `eval.c` | ingested as practice → [[virtual-machines-and-runtime-systems-exercise-1]] |
| S2 | Signals, reentrancy, `longjmp` threads | `02.pdf`, skeleton sources | ingested as practice → [[virtual-machines-and-runtime-systems-exercise-2]] |
| S3 | Exceptions (complexity of entry, handler search, `finally` rewrite) and memory management (`malloc`/`calloc`/`realloc`/`free` over `sbrk`) | `03.pdf`, `mymalloc.c` | ingested, implemented and run → [[virtual-machines-and-runtime-systems-exercise-3]] |
| 3 | Abstract C machine and undefined behavior; Prolog semantics and Warren Abstract Machine | `s03.pdf` | ingested → [[virtual-machines-and-runtime-systems-lecture-3]] |

## Exercise Sheet 1 (due 22.10.2026, discussion 23.10.2026)

1. **Addresses** — build `libshowaddrs.a` / `.so` that prints `etext`, `edata`, `end`; link `addrs.c` statically, dynamically with `-Wl,-rpath,.`, and load it at run time with `dlopen`/`dlsym`. Compare the three results.
2. **Primitive JIT compiler** — read an expression, write it into a C file, compile it to a `.so` with `system("gcc -fPIC -shared …")`, `dlopen` it, call `f()`, print the value. Skeleton in `eval.c`.

## Open Questions

- Garbage collection and container internals are in the syllabus but not yet taught.
- No exam date for a possible oral component — the source says written only.
