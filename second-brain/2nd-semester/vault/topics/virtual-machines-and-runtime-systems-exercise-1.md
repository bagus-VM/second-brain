---
title: "Virtual Machines and Runtime Systems — Exercise Sheet 1 Overview"
tags: [topic, virtual-machines, semester-2, exercise]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[dynamic-linking]]", "[[process-memory-layout]]"]
---

## One-line Summary
Two problems that turn lecture 2's slides into running code: observe segment boundaries from inside a
program and a library under three linking modes, then build a primitive JIT by compiling a library at
run time and calling into it.

## Core Map

```
Exercise Sheet 1 — Dynamic libraries in C
│
├── Problem 1: Addresses
│   ├── library declares etext / edata / end   -> [[process-memory-layout]]
│   ├── (a) link statically   (libshowaddrs.a)
│   ├── (b) link dynamically  (-L. -lshowaddrs -Wl,-rpath,.)
│   └── (c) no link at all    (dlopen + dlsym) -> [[dynamic-linking]]
│
└── Problem 2: Primitive JIT compiler
    ├── read an expression
    ├── write `double f(void) { return (<expr>); }`
    ├── compile to a .so at run time
    └── dlopen + dlsym + call -> [[dynamic-linking]]
```

## What the Sheet Asks

**Problem 1.** `addrs.c` uses the linker symbols `etext`, `edata`, `end` to print the bounds of the
text, data and BSS segments. Write `libshowaddrs.a`/`.so` that declares the same symbols and prints
them from inside the library; extend `addrs.c` to call it, so the bounds print twice. Build it three
ways — static, dynamic, and not linked at all (`dlopen`/`dlsym`) — and compare the results. The sheet
also notes `-m32` may change the behaviour on 32-bit targets.

**Problem 2.** Using `dlopen`/`dlsym` and a compiler binary, build a simple JIT: write the user's
expression into a C file wrapped in `double f(void)`, compile it to a shared library, load it, call
`f`, print the value. Skeleton in `eval.c`. Hand-in optional, due 22.10.2026, discussed 23.10.2026.

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[dynamic-linking]] | The mechanisms this sheet exercises: link-time vs run-time resolution, `ld.so`, rpath, `dlopen`/`dlsym`, `-fPIC`, mmap area |
| [[process-memory-layout]] | What `etext`/`edata`/`end` actually bound, and where the heap, stack and mmap area sit relative to them |

## The Answer in One Paragraph

Static: one copy of everything, so the library prints *identical* addresses to the main program.
Link-time dynamic: the library's **code** sits high in the mmap area, but it prints the **same**
segment ends as main — the executable's symbol definitions take precedence over the library's, so both
references bind to the same `etext`/`edata`/`end`. `dlopen`: a standalone `.so` carries its own
definitions, so the library reports *its own* segment ends, at high addresses. The lesson: "where the
library lives" and "which segment ends it sees" are two different questions.

## Exam-Relevant Points

1. **Why rpath matters**: a relative `-L.` at link time says nothing about run time; the loader needs a
   runpath, and `$ORIGIN` is the portable form.
2. **`dlsym` error handling**: clear with `dlerror()` first, check it after — `NULL` is a legal symbol
   address.
3. **The three linking modes are three different answers to "when is the address known?"** — link time,
   load time, run time.
4. **A JIT is just compilation + dynamic loading**: no `exec`, no recompilation of the host program.
5. **`-fPIC`** is required for anything loaded as a shared object on x86-64.

## Connections

- Solutions, code and measured output: `study/homework/virtual-machines-and-runtime-systems/sheet-01/`
  (`showaddrs.c`, `addrs.c`, `eval.c`, `Makefile`) — all three builds and the JIT were compiled and run.
- [[virtual-machines-and-runtime-systems-lecture-2]] — the lecture that makes this sheet tractable.
- [[runtime-system]] — the API/ABI framing that explains why a `.so` is a runtime artefact.

## Open Questions

- How the executable and a shared library resolve the *same* linker-defined symbols is the interesting
  subtlety here, and the sheet leaves it to the tutorial discussion ("How do the results compare?").
- The `-m32` hint suggests a 32-bit/64-bit comparison, but no 32-bit toolchain is required to complete
  the sheet.
