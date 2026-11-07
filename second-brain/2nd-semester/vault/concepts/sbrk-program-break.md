---
title: "sbrk and the Program Break"
tags: [concept, virtual-machines, semester-2, runtime-system, memory-management]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: ["[[process-memory-layout]]"]
---

## One-line Summary
The program break is the end of the process's data segment; `sbrk(delta)` moves it by `delta` bytes and returns the *old* break, which is the cheapest possible allocator primitive — and the reason every real allocator above it has to think about alignment, reuse and locking.

## Core Intuition
A process's heap is not a heap in the data-structure sense; it is one contiguous region that grows and shrinks by moving a single address (the break) up and down. `sbrk` is that move, and nothing else: no block headers, no reuse, no notion of an allocation. Asking the kernel for memory is therefore trivially fast — it is a pointer update, with the kernel only involved when the break crosses a page boundary that is not mapped yet. All the interesting behaviour of `malloc` (sizes, alignment, reuse, free lists, fragmentation) is *invented on top*, which is exactly what exercise sheet 3 asks for.

## Formal Definition / Statement
- The **program break** is the address of the first byte past the end of the process's uninitialised data segment (the heap area). It is per-process state, not per-thread.
- `void *sbrk(intptr_t delta)` increments the break by `delta` bytes and returns the **previous** break. So `sbrk(0)` is the idiom for "tell me the current break" and `sbrk(n)` is "give me the next `n` bytes starting at the old break".
- On failure it returns `(void *) -1` and sets `errno` (typically `ENOMEM`).
- Declared in `<unistd.h>`; on glibc it is guarded by `__USE_MISC`, so under strict `-std=c99` it needs `_DEFAULT_SOURCE` (or `-std=gnu99`) to be declared at all.

Contrast with `mmap`-based allocation: `sbrk` can only move one end of one region, cannot return memory in the middle, and is not thread-safe by itself — POSIX `malloc` uses `mmap` for large requests and `brk`/`sbrk` for the arena, and serialises both.

## Key Properties
- **Return value is the old break.** The new memory is `[old_break, old_break + delta)`; a call that *shrinks* the break returns a pointer to memory that has just been released.
- **One currency, one direction of thought.** Because the region is contiguous and only its end moves, any allocator that wants reuse must impose its own structure on it — headers, free flags, lists.
- **Alignment is entirely the caller's problem.** `sbrk` returns whatever the break happened to be. If every request is a multiple of 16, the break stays 16-aligned forever; mix in an unaligned request and every later block is misaligned, which is why the exercise demands 16-byte-aligned returns.
- **It is a single serialisation point.** In a multithreaded program, two concurrent `sbrk` calls can hand out overlapping memory. The exercise skeleton takes a `pthread_mutex_t` around the break manipulation for exactly this reason.
- **The kernel is only touched at page granularity.** Moving the break within already-mapped pages costs no system call; the first `malloc` in a new page may fault. So "`sbrk` is cheap" is true in the common case and not a hard guarantee.

## Worked Example
A minimal 16-byte-aligned bump allocator — the whole of part (a), minus the skeleton's logging:

```c
#define HEADER 16
static size_t round16(size_t n) { return (n + 15) & ~(size_t)15; }

void *malloc(size_t size) {
    if (size == 0) size = 1;
    uintptr_t brk = (uintptr_t)sbrk(0);            /* current break */
    if (brk & 15)                                   /* align it once, then keep */
        if (sbrk((intptr_t)(16 - (brk & 15))) == (void *)-1) return NULL;
    void *block = sbrk((intptr_t)(HEADER + round16(size)));   /* old break */
    if (block == (void *)-1) return NULL;
    *(size_t *)block = size;                        /* header: for realloc */
    return (char *)block + HEADER;                  /* 16-byte aligned payload */
}
```

The recorded trace makes the mechanism visible: `malloc(4096); program break = 0x26269000` then, after a `free` that is a no-op, `malloc(4096); program break = 0x2626A010` — the break moved by exactly `16 + round16(4096) = 4112, 0xA10`. Compare the free-list build on the same page, where the break stays at `0x8333FD0` across dozens of allocations.

`free` in part (a) is a single `myprintf` and nothing else; the block is abandoned, and that is the whole cost model of the design.

## Common Pitfalls
- **Treating `sbrk`'s return as the *new* break.** It is the old one; the block you may use starts there. Reading `sbrk(0)` afterwards gives the end of it.
- **Forgetting the `(void *)-1` check.** On failure `errno = ENOMEM` and any pointer arithmetic on `-1` walks off the top of the address space.
- **Unaligned requests.** One odd-sized `sbrk` desynchronises every later allocation; the fix is to round every request up (and, defensively, to align the break on first use).
- **No locking.** The break is shared process state; the skeleton's mutex is not decoration.
- **`memcpy(new, old, size)` in `realloc`.** Without a header, the old size is unknown, so the copy either truncates the data or reads past the old block. The lecture's own `libmemory.c` does the latter and flags it in a comment; the working example above stores the requested size in the header instead.
- **Mixing `sbrk` with `malloc`.** libc's allocator has its own view of the break; moving it behind libc's back corrupts the arena. A replacement allocator must replace the whole family, so there is only one owner.
- **`free` must preserve `errno`.** The interposed `free` is called on libc's error paths.

## Connections
- [[process-memory-layout]] — where the break sits relative to text, data, stack and the mappings above it.
- [[ld-preload-symbol-interposition]] — how the allocator built on `sbrk` gets installed in place of libc's.
- [[runtime-system]] — the C runtime facilities (`errno`, locking, stdio) the allocator has to cooperate with, and the reason it cannot use `printf`.
- [[virtual-machines-and-runtime-systems-exercise-3]] — Problem 2, in both variants.
- `study/homework/virtual-machines-and-runtime-systems/sheet-03/` — the two implementations, their traces, and the test harness.

## Open Questions
- The sheet does not say whether `sbrk`-based allocation is expected to remain competitive, only that it must work; the free-list variant's fragmentation is left as the natural next topic.
- Whether the tutorials intend `mmap` as an alternative primitive (the lecture's memory-management material was not yet complete when this sheet was discussed) is not stated in the ingested slides.
