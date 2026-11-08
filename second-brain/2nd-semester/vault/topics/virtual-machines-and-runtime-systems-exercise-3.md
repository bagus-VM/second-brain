---
title: "Virtual Machines and Runtime Systems — Exercise Sheet 3 Overview (Exceptions, Memory Management)"
tags: [topic, virtual-machines, semester-2, exercise, exceptions, memory-management]
course: "Virtual Machines and Runtime Systems"
source_count: 3
status: current
last_updated: 2026-11-04
prerequisites: ["[[exception-handling-implementation]]", "[[process-memory-layout]]"]
---

## One-line Summary
Two halve-less problems: the exception machinery from lecture 2, measured in time complexity (entering a `try`, finding a handler, emulating `finally`), and a real allocator written on top of `sbrk` and installed with `LD_PRELOAD` — first as a bump allocator that never frees, then as a free-list allocator that does.

## Core Map

```
Exercise Sheet 3 (due 05.11.2026 18:00, discussion 06.11.2026) — Exceptions, Memory Management
│
├── Problem 1 — Exceptions (theory; no program to write)
│   ├── (a) entering a try block in constant time
│   │       → one handler record pushed onto a handler stack, O(1),
│   │         independent of the number of catch clauses
│   ├── (b) finding the handler: naive static O(d·n)
│   │       → per-function sorted range tables O(d·log k), IP-indexed
│   │         tables O(d); theoretical best Θ(d), because every frame
│   │         between throw and handler must be examined
│   │       → [[exception-handling-implementation]]
│   └── (c) finally emulated by rewriting: F inlined on the normal and on
│           the exceptional exit path, then rethrow
│
└── Problem 2 — Memory Management (skeleton mymalloc.c from Stud.IP)
    ├── (a) free does nothing; malloc only ever calls sbrk
    │       → [[sbrk-program-break]]
    └── (b) (optional, harder) free list: free marks a block available,
            malloc searches for one of sufficient size, sbrk only when
            nothing fits; split oversized blocks
        → [[ld-preload-symbol-interposition]]
        → [[sbrk-program-break]]
```

## Key Concepts at a Glance

| Page | What the sheet exercises |
|------|--------------------------|
| [[exception-handling-implementation]] | The lecture's two mechanisms — the `setjmp`/`longjmp` handler stack and the table-driven search — which Problem 1 asks about in complexity terms |
| [[ld-preload-symbol-interposition]] | How a library loaded early replaces `malloc` and friends for a program that never expected it |
| [[sbrk-program-break]] | The primitive both allocators are built on: one address, moved up, alignment on the caller |
| [[process-memory-layout]] | Where the break lives, and what the heap is |
| [[runtime-system]] | `errno`, locking and stdio discipline the interposed functions have to respect |

## The Sheet

*"Exercise Sheet 3 (Exceptions, Memory Management)"*, Dr. Armin Größlinger. Printed facts:

- **Due Thursday, November 05 at 18:00**; **discussion on November 06, 2026**.
- Hand-in is **optional**, via the **"Submissions" folder in Stud.IP**, **source files only**.
- The skeleton `mymalloc.c` is on Stud.IP; the sheet points at it for how `LD_PRELOAD` is used.
- Addresses returned by `malloc` etc. must be **16-byte aligned**.
- `memset` and `memcpy` from `stdlib.h` may be used.
- The allocation helpers (`memalign` and friends) are **already implemented in the skeleton on top of `malloc`** and need not be touched.

## Problem 1 — the three answers in brief

**(a) Constant-time entry.** Push *one* handler descriptor on entering the `try` block — the address of the catch dispatcher (or a `jmp_buf`, as in the lecture's `dyn_ex.c`), the frame pointer, and the previous top. One push is O(1) regardless of how many `catch` clauses the block has; the table-driven "static" variant instead makes entry depend on registering or later searching one entry per clause.

**(b) Finding the handler.** Naively O(d·n): *d* stack frames × *n* catch-clause ranges. Sorted per-function range tables turn the per-frame step into a binary search (O(d·log k), k the clauses in that function) — effectively O(d); indexing handler tables by instruction pointer (hash map / interval tree, what `.eh_frame`-walking unwinders do) makes each frame O(1). **The theoretical best is Θ(d)**, and it is a lower bound: the handler can sit in the outermost frame, so all *d* frames in between must at least be examined.

**(c) `finally` by rewriting.** There is no jump-into-the-middle after the stack is cut back, so the finally body F is **duplicated onto each exit path**: once on normal completion, once on the exceptional path — and on the exceptional path it must **rethrow** afterwards so the original exception keeps propagating. If F throws while an exception is pending, the new exception replaces the pending one. `return`/`break`/`continue` out of the `try` block each need their own copy of F too. The full sketch, with Java-like syntax and `goto`, is in `study/homework/virtual-machines-and-runtime-systems/sheet-03/sheet-03-solution.md`.

## Problem 2 — the design, and what the runs show

Both variants are in `study/homework/virtual-machines-and-runtime-systems/sheet-03/`
(`mymalloc-bump.c`, `mymalloc-freelist.c`, `test-mymalloc.c`, `Makefile`, `sheet-03-solution.md`,
plus `output-test-runs.txt` and `output-trace-excerpt.txt`).

- **Part (a)** stores the *requested* size in a 16-byte header, keeps the program break 16-byte
  aligned, and abandons every block on `free` — the header exists only so `realloc` can copy
  `min(size, old_size)`. The lecture's own `libmemory.c` copies `size` and reads past the old
  block; its own comment flags that, and the recorded demo shows the read stays inside the
  freshly extended heap, so it corrupts data rather than crashing.
- **Part (b)** keeps every sbrk block in one address-ordered list, marks freed blocks with bit 0
  of the size field, does a first-fit search with splitting, and stops moving the break once the
  heap is warm. No coalescing — the honest limitation, stated in `sheet-03-solution.md` and here.

Evidence, from the runs (all three variants pass the same 5-check harness with 0 failures):

| Run | Reuse after `free` | Break behaviour |
|-----|--------------------|-----------------|
| system `malloc` | same pointer | reused |
| part (a) bump | **different** pointer | `0x26269000 → 0x2626A010 → 0x2626B020` for three `malloc(4096)` calls |
| part (b) free list | **same** pointer | `0x8333FD0` unchanged across dozens of allocations |

Both libraries were also used for what the sheet suggests — preloading a program that knows
nothing about it: `LD_PRELOAD=./libmymalloc-{bump,freelist}.so ls -1 *.c` exits 0, with every
allocation in coreutils resolving to the replacement.

## Exam-Relevant Points

1. **The complexity table.** Entry O(1) (one push) vs O(#clauses) (register/search per clause); handler search O(d·n) naive → O(d·log k) with sorted per-function tables → **Θ(d)** as the floor, with the lower-bound argument (every frame must be examined).
2. **Why Θ(d) and not better.** The argument is the examinable part: the handler may be anywhere, and cleanups on the way must run.
3. **`finally` semantics, precisely.** Both exit paths, rethrow afterwards, replacement when F itself throws, and abrupt exits (`return`/`break`/`continue`) each needing a copy.
4. **The two exception mechanisms as code.** `dyn_ex.c`'s `handle()` macro (`sigsetjmp` per try) and `static_ex.c`'s handler-range scan with `libunwind` — both in `Example_programs_for_s02/exception/`, and both run (see [[virtual-machines-and-runtime-systems-lecture-2]]).
5. **Allocator basics.** Header-based size bookkeeping, 16-byte alignment discipline, first-fit + split, why `free` must preserve `errno`, why the allocator may not call `printf`, why the mutex cannot be re-entered.
6. **`realloc`'s contract.** `realloc(NULL,n) == malloc(n)`, `realloc(p,0) == free(p)`, and the copy is `min(new, old)` — the exact place the lecture's sample implementation is wrong.
7. **`LD_PRELOAD` mechanics.** Load order decides the winner; the failure mode is a silent stderr message; a partial replacement splits the heap between two owners.

## Connections

- [[virtual-machines-and-runtime-systems-lecture-2]] — the C runtime system lecture (exceptions, memory layout, `errno`, signals) this sheet applies, and where the professor's example programs belong.
- [[virtual-machines-and-runtime-systems-exercise-2]] — the previous sheet; same folder convention, same build-and-run approach (`zig cc` + WSL).
- [[exception-handling-implementation]] — Problem 1 in full.
- [[sbrk-program-break]], [[ld-preload-symbol-interposition]] — the two concept pages this sheet produced.
- `raw/lectures/Virtual Machine and Runtime System/Ubung/Sheet_3_Exceptions,_Memory_Management-_discussion_on_November_06/` — `03.pdf`, the skeleton `mymalloc.c`, `Makefile`.
- `study/homework/virtual-machines-and-runtime-systems/sheet-03/` — the working solution and its recorded output.

## Open Questions

- **The sheet does not say which of (a)/(b) is expected in the hand-in** — (b) is marked "more complex, optional". Both are implemented here; if only one should be submitted, it is presumably (b) with (a) as the stepping stone.
- **Part 1(b) does not define `d` and `n` beyond the formula** — "in common programs" hints at realistic per-function clause counts, but no expected answer is given, and the tutorials hold the answer key.
- **Whether the alignment requirement is 16 bytes for every function or only for `malloc`'s direct result** is not spelled out; the implementations align every payload, including the aligned variants' underlying blocks.
- **The lecture's memory-management material is not yet fully in `raw/`** (the syllabus lists "memory management" without a deck of its own), so the free-list design here is the sheet's text plus the standard treatment, not a reproduction of lecture slides.
