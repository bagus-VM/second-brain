---
title: "Process Memory Layout"
tags: [concept, virtual-machines, semester-2, processes]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-19
prerequisites: ["[[runtime-system]]"]
---

## One-line Summary
A process is a program in execution — text plus data, where data splits into data, BSS, heap and stack — laid out in a *virtual* address space whose regions grow toward each other and are mapped to physical pages by page tables.

## Core Intuition
The address in a pointer is not a physical memory cell. It indexes a per-process fiction that the CPU translates through page tables the OS maintains. That fiction is what makes the layout possible: fixed low addresses for code and static data, a heap creeping up, a stack creeping down, and a hole in the middle for shared libraries.

The layout is not bookkeeping detail. Every mechanism in this course — `malloc`, dynamic libraries, `longjmp`, thread stacks — is a statement about *which region* something lives in and *which direction* it grows.

## Formal Definition / Statement

**Process (s02):** a program that is currently executing. It consists of the code that is executed (**text segment**) and the data that is manipulated.

The data area consists of initialized data (**data segment**), uninitialized data (**BSS segment**), the **heap** and the **stack**. Heap and stack grow and shrink as required; text, data and BSS are loaded together **from the program binary**.

**Virtual layout (x86_64 Linux):**

```
text | data | BSS | heap ↔ · · · ↔ mmap ↔ stack | kernel
0                                              128 TiB
```

Heap and stack grow in **opposite directions**. When they meet, the process has to be terminated. Their sizes can be limited — cf. `ulimit`.

The 128 TiB boundary between user space and kernel is a typical value on 64-bit Linux (x86_64). On 32-bit systems it is typically at **2 GiB** (= 2³¹).

**Physical vs. virtual:** the CPU maps logical to physical addresses via page tables managed by the OS, at **page granularity**, typically **4 KiB … 1 MiB**. One physical page can be mapped into the address spaces of several processes, possibly at different virtual addresses — so the sum of all virtual address spaces can exceed physical memory even without swap.

**Binary formats:** PE (Windows, 32- and 64-bit), ELF (Linux, FreeBSD, Solaris), Mach-O (macOS X). ELF is inspected with `readelf`.

## Key Properties

- **Text is executable, data is not.** The segments differ in protection, not just content.
- **BSS costs nothing on disk.** Zero-initialized data occupies address space, not file size.
- **The heap grows by moving the program break** — the address of the first byte past the heap's end. `sbrk(0)` reads it, `sbrk(x)` moves it by `x` and returns the old value, `brk(addr)` sets it. `malloc` was historically built on these; modern implementations prefer `mmap`.
- **The `mmap` area is the hole** between heap and stack, used for shared libraries and explicit mappings — see [[dynamic-linking]].
- **Addresses are per-process.** Two processes printing the same address may touch different physical pages.

## Worked Example

Exercise 1 ships `addrs.c`, which prints the addresses of the linker-provided symbols `etext` (end of text), `edata` (end of initialized data), `end` (end of BSS) and `heap_begin` / `&heap_begin` (start of heap).

Run it and the addresses come out **ascending**: text lowest, then data, then BSS, then heap. The gaps are the segment sizes; the distance from `end` to `heap_begin` is padding plus allocator bookkeeping.

The exercise then prints the same symbols from inside a library, in three builds — static `libshowaddrs.a`, dynamic with `-Wl,-rpath,.`, and `dlopen`/`dlsym` at run time. The comparison is the point:

- **static** — the library's symbols *are* the program's symbols; addresses agree.
- **dynamic** — the library is a separate object in the `mmap` area; its text/data/BSS sit elsewhere and the printouts disagree.
- **`dlopen`** — same as dynamic, but the mapping happens after `main` started.

## Common Pitfalls

- **Assuming addresses are physical.** They are virtual; the mapping is at page granularity.
- **Confusing `end` with the heap end.** `end` is the end of BSS; the heap *starts* there.
- **Thinking heap and stack are adjacent.** On x86_64 a large hole separates them, and `mmap` lives in it.
- **Forgetting the 32-bit case.** The 2 GiB boundary changes every address comparison; the exercise suggests `-m32`.

## Connections

- [[runtime-system]] — `malloc` and `sbrk` are runtime services over this layout.
- [[dynamic-linking]] — why the `mmap` area exists.
- [[thread-emulation-longjmp]] — each emulated thread needs its own stack area.
- [[setjmp-longjmp]] — `longjmp` works by resetting RSP/RBP, i.e. rewriting the stack region.

## Open Questions

- The lecture gives "4 KiB … 1 MiB" without saying which systems use the large end. Huge pages are the likely reason; the slide does not say so.
- Where a `dlopen`ed library lands relative to a running stack, and whether ASLR matters, is left to the exercise's comparison.
