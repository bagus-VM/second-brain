---
title: "Virtual Machines and Runtime Systems — Exercise Sheet 3 Solution (Exceptions, Memory Management)"
tags: [homework, virtual-machines, semester-2, exceptions, memory-management]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: []
---

# Exercise Sheet 3 — Exceptions, Memory Management

*Virtual Machines and Runtime Systems, WS 2026/27 (Dr. Armin Größlinger)*
*Sheet: `03.pdf` — due Thursday 05.11.2026, 18:00; discussion Friday 06.11.2026.*
*Hand-in is optional (source files only, "Submissions" folder in Stud.IP).*

| Problem | Deliverable here | State |
|---------|------------------|-------|
| 1 (Exceptions) | this page, parts (a)–(c) | answered |
| 2(a) bump allocator | `mymalloc-bump.c` | **built and run**: 5/5 checks pass under `LD_PRELOAD` |
| 2(b) free list (optional) | `mymalloc-freelist.c` | **built and run**: 5/5 checks pass; block reuse demonstrated |
| harness | `test-mymalloc.c`, `Makefile` | run three ways: system malloc, part (a), part (b) |

Captured evidence: `output-test-runs.txt` (the three runs) and
`output-trace-excerpt.txt` (the `myprintf` allocation traces, which are where the
difference between (a) and (b) becomes visible).

---

## Problem 1 — Exceptions

### (a) Why entering a `try` block can be constant time

Two families, and the cost sits in a different place in each:

* **Static (table-driven) management.** The compiler emits, per function, a table
  of entries `(range_start, range_end, handler_address)` — one entry per `catch`
  clause (plus cleanup entries). These tables are built at compile time and do not
  change at run time, but *finding* the right entry later means searching them.
  The lecture's `static_ex.c` shows the naive form of this: `register_handler()`
  scans the handlers already installed to reject a duplicate before appending, so
  registering the `k`-th try block costs O(k) — and a `try` with several `catch`
  clauses adds one entry per clause.
* **Dynamic management.** Instead of a table, the runtime keeps an explicit
  **handler stack**: entering a `try` block pushes *one* record — the address of
  the catch dispatcher (or a `jmp_buf`, in `dyn_ex.c`'s `handle()` macro) plus the
  saved frame pointer and the previous top of the stack. That is a fixed number of
  instructions, independent of how many `catch` clauses the block has. Leaving the
  block pops one record.

So "constant time to enter" is achieved by making the entry operation a **single
push of one handler descriptor onto a per-thread handler stack**, rather than
registering (or later searching) one entry per clause:

```
struct handler { void *catch; void *frame; struct handler *prev; };
on entering try:   push(&handler_stack, {catch_addr, frame_ptr});
on leaving try:    pop(&handler_stack);
```

`dyn_ex.c` is exactly this: `handle()` expands to `sigsetjmp(handlers[n_handlers++], 1)`,
one `sigsetjmp` per try block entered. The number of `catch` clauses inside the
block never enters the expression.

### (b) Finding the handler faster than O(d·n)

The naive static search is O(d·n): walk the *d* frames of the call stack, and for
each frame compare the faulting instruction pointer against all *n* catch-clause
ranges in the program.

Three improvements, in increasing power:

1. **Per-function handler tables with sorted ranges.** Each function carries only
   its own clauses (k of them, k ≪ n). A binary search for the range containing the
   throw IP is O(log k) with a tiny constant; while unwinding, each frame is then an
   O(1) table lookup. Total O(d · log k) → in practice O(d), because k is 1–3 in real
   functions. This is what the Itanium ABI / LSDA tables do.
2. **Index by return address (a hash map or interval tree over the whole program).**
   Then even the first lookup is O(1)/O(log n), giving O(d) overall and removing the
   per-function assumption. Optimising JITs (and the `.eh_frame`-based walkers used
   by `libunwind`, as in `static_ex.c`) do this.
3. **The dynamic handler stack of (a) makes the search O(d) directly:** each try
   frame has its handler record at a known place, so per frame the check is O(1)
   and the only work is the unwinding itself.

**Theoretical best: Θ(d)** — and it is a *lower bound*, not a gap in the design.
The handler can be in the outermost frame, so every frame between the throw site and
the handler must be visited (at minimum to run its cleanups, and even with no
cleanups at all to decide that it has no handler). With an O(1) per-frame test, Θ(d)
is reached. The only way to "beat" it would be to know the handler without walking
the stack — which is what a `setjmp`/`longjmp`-style dynamic scheme does in the
degenerate case where the handler record is already at the top of the stack: the
jump is then O(1), at the price of the bookkeeping in (a).

### (c) Emulating `finally` by rewriting

`finally` has no equivalent in the return-address-based mechanism, so it must be
*duplicated onto every exit path*: the normal one, and the exceptional one. The
exceptional copy must run after the `catch` (or after the exception is seen to have
no matching `catch`), and it must **rethrow** afterwards so the original exception
keeps propagating. Java-like pseudo code with `goto`:

```
// original
//   try { S }
//   catch (E e) { C }
//   finally { F }

// rewritten, no finally clause anywhere:
    boolean pending = false;       // an exception is in flight
    Exception cur  = null;

    install handler H;             // (a) — one push, O(1)
try_entry:
    S                              // may throw, may return/break
    remove handler H;              // normal leaving of the try block
    F                              // <-- copy 1 of F: normal completion
    goto after;

H:                                 // entered by the unwinder / siglongjmp
    if (cur matches E) { e = cur; cur = null; }
    else { pending = true; goto run_finally; }   // no catch here: still run F
    C                              // the catch body
    remove handler H;
run_finally:
    F                              // <-- copy 2 of F: exceptional completion
    if (pending) rethrow cur;      // keep unwinding with the same exception
    goto after;

after:
```

Three points the sketch encodes:

* **F is inlined twice** (normal and exceptional), because there is no way to jump
  into the middle of a block once the stack has been cut back. A compiler that wants
  one copy instead emits a *finally subroutine* (`jsr`/`finally` blocks in old Java
  bytecode) and calls it from each exit — the duplication is an implementation
  choice, not a semantic one.
* **The exceptional path rethrows.** Running F is not the end: the exception must
  carry on to the enclosing handler. If F itself throws while an exception is
  pending, the new exception *replaces* the pending one (Java semantics) — the
  `rethrow cur` line is where that decision has to be made explicit.
* **Every abrupt exit needs a copy of F**, not just exceptions: `return`, `break`
  and `continue` out of the `try` block must also run F, which is why the real
  rewrite interleaves F with the state variable instead of just two copies.

---

## Problem 2 — Memory Management

The Stud.IP skeleton `mymalloc.c` is filled in twice — once per part. Both keep the
skeleton's `myprintf()` (it uses `write(2, …)` only, because `printf` may call
`malloc` and would recurse), its `errno` discipline in `free`, its mutex, and its
`posix_memalign`/`memalign`/`aligned_alloc`/`valloc`/`pvalloc` wrappers, which are
built on top of `malloc` and therefore need no changes.

### 2(a) — `mymalloc-bump.c`: `free` does nothing, `malloc` just asks `sbrk` for more

The break is only ever moved up, and every block starts with a 16-byte header that
records the *requested* size:

```
 block -> +----------------+   16-byte header; block itself 16-byte aligned
          | requested size |   (needed so realloc can copy min(size, old_size))
          +----------------+ <-- returned pointer, 16-byte aligned
          | payload        |
```

* `malloc(n)`: align the program break once (`sbrk(0)` rounded up to 16), then
  `sbrk(16 + round16(n))`, write `n` into the header, return `block + 16`.
  Because every request is a multiple of 16, the break stays 16-aligned forever.
* `free(p)`: `myprintf` only — the block is abandoned. `errno` is saved and restored,
  as the documentation demands.
* `calloc(nm, sz)`: one `sbrk`, then `memset` to zero. It does **not** call `malloc`
  — the skeleton already holds the lock, and the mutex is not recursive.
* `realloc(p, n)`: `p == NULL` → `malloc(n)`; `n == 0` → "free" and return `NULL`;
  otherwise allocate a fresh block and `memcpy` exactly `min(n, old_size)` bytes,
  where `old_size` comes from the header.

The header exists for that last line. Without it the only copy length available is
`n`, which reads past the old block whenever the allocation grows — the bug the
lecture's own `libmemory.c` flags in a comment (`memcpy(p, ptr, size); // wrong,
should be min(size,old_size)`).

### 2(b) — `mymalloc-freelist.c`: mark freed blocks, reuse them

Same skeleton, but the heap is one singly linked list of every block ever handed out
from `sbrk`, kept in address order, and the header carries both the size and a flag:

```
 struct header { size_t size; struct header *next; };   // 16 bytes
 // size is a multiple of 16, so bit 0 of `size` is the free flag
```

* `malloc(n)`: first-fit scan of the list for a free block of at least `round16(n)`;
  if the block is much larger, **split** it and leave the remainder as a new free
  block. `sbrk` is called *only* when no block fits — which is what the sheet asks
  for, and what makes the break stop moving once the heap is warm.
* `free(p)`: clears the flag and nothing else. Blocks are **not coalesced**, so this
  is first-fit without merging (see the honest limitation below). `free(NULL)` is a
  no-op, `errno` is preserved.
* `calloc`, `realloc`: same semantics as (a); `realloc` shrinks in place when the
  current block is big enough and otherwise allocates, copies
  `min(need, old_block_size)` and marks the old block free.

**Known limitation, deliberately left in:** no coalescing of adjacent free blocks,
so a workload that alternates sizes fragments the heap into unusable pieces. The
sheet asks for "marked as available" + "search for a free block", which this is; the
next step (and the standard exam follow-up) is a boundary-tag or bin-based allocator
that merges neighbours on `free`.

### What the runs show

Built on this Windows host — which has no `gcc` in either git-bash or WSL — with the
`zig cc` cross-compiler (same route as sheet 2), and executed under WSL:

```
zig cc -O0 -std=c99 -D_DEFAULT_SOURCE -fPIC -shared mymalloc-bump.c     -o libmymalloc-bump.so
zig cc -O0 -std=c99 -D_DEFAULT_SOURCE -fPIC -shared mymalloc-freelist.c -o libmymalloc-freelist.so
zig cc -O0 -std=c99 -D_DEFAULT_SOURCE        test-mymalloc.c            -o test-mymalloc
```

Two flags mattered and are worth remembering: **`-D_DEFAULT_SOURCE`**, because
strict C99 does not declare `sbrk` (glibc puts it under `__USE_MISC`), and
**`-fno-sanitize=integer-divide-by-zero`** when building the lecture's exception
programs — `zig cc` enables that sanitizer by default, and it preempts a program's
own `SIGFPE` handler with Zig's panic runtime.

`test-mymalloc.c` checks: 16-byte alignment for every size 1..200, `calloc` zeroing,
`realloc` growing from 96 to 200 000 bytes with the data intact, `realloc` shrinking,
reuse after `free`, and a mixed alloc/free workload with a content check on every
untouched block.

```
$ ./test-mymalloc                                     # system malloc, baseline
reuse after free: x=0x10828f20 y=0x10828f20 same=yes
5 checks, 0 failure(s)

$ LD_PRELOAD=./libmymalloc-bump.so ./test-mymalloc      # part (a)
reuse after free: x=0x26269010 y=0x2626a020 same=no
5 checks, 0 failure(s)

$ LD_PRELOAD=./libmymalloc-freelist.so ./test-mymalloc  # part (b)
reuse after free: x=0x83032c0 y=0x83032c0 same=yes
5 checks, 0 failure(s)
```

The difference between (a) and (b) is visible in the allocation trace (`myprintf`
prints `sbrk(0)` before every `malloc`). Same test, same block size, one after the
other: `malloc(4096)` … `free` … `malloc(4096)`:

```
# part (a) — the break advances; nothing is ever reused
malloc(4096);  program break = 0x26269000      # test's own 4096-byte block
malloc(4096);  program break = 0x2626A010      # after free: a NEW block
malloc(4096);  program break = 0x2626B020      # and again

# part (b) — the break does not move at all: the freed block comes back
malloc(4096);  program break = 0x8333FD0
malloc(4096);  program break = 0x8333FD0
malloc(4096);  program break = 0x8333FD0
```

And under the mixed workload of checks 6, part (b) serves dozens of allocations
(the `p[i]`/`q[i]` interleave, sizes 7…448 bytes) from the same warm heap:

```
malloc(294);  program break = 0x8333FD0
malloc(301);  program break = 0x8333FD0
malloc(308);  program break = 0x8333FD0
...
malloc(420);  program break = 0x8333FD0
```

Both allocators were also used for the real thing the sheet suggests — running a
program that does not know it is being intercepted:

```
$ LD_PRELOAD=./libmymalloc-bump.so ls -1 *.c
demomem.c  dyn_ex.c  fpeprobe.c  libmemory.c  mymalloc-bump.c      # exit 0
$ LD_PRELOAD=./libmymalloc-freelist.so ls -1 *.c
demomem.c  dyn_ex.c  fpeprobe.c  libmemory.c  mymalloc-bump.c      # exit 0
```

`ls` exits 0 under both, which is the interposition working: every `malloc`,
`calloc`, `realloc` and `free` in coreutils resolves to these implementations.

### A note on the lecture's own `libmemory.c`

`raw/…/Example_programs_for_s02/mem/libmemory.c` is the professor's worked example
for this topic, and its `realloc` contains the flagged bug:

```c
void *p = malloc(size);
if (ptr != NULL) {
    memcpy(p, ptr, size);   // wrong, should be min(size,old_size);
    free(ptr);
}
```

Run it to see what the bug actually does: because `malloc(size)` has *already* moved
the break past the source range by the time `memcpy` runs, the out-of-bounds read
lands inside the freshly extended heap and does not fault — it silently copies
whatever was there. Driver `demomem.c` (allocate 96 bytes as the last block, then
`realloc` to 200 000) under that library:

```
malloc(64);  malloc(96);  malloc(4096);  realloc(308C7040,200000);  malloc(200000);
free(308C7040) … free(308C80C0) …
zeroed=1
realloc ok, c[95]=A        # exit 0 — no crash, but 199 904 bytes were copied from
                           # outside the old block
```

Both implementations here copy `min(size, old_size)` from the header instead, so the
read never leaves the block.

---

## Environment notes

* No `gcc` on the host (git-bash) and none in WSL; `zig cc` cross-compiles to
  `x86_64-linux-gnu.2.35` and WSL runs the binaries. The `Makefile` here ships the
  commands for a machine that *does* have `gcc`, so the folder is rebuildable
  anywhere.
* Build products (`*.so`, `test-mymalloc`) are deliberately **not** in the vault;
  `make clean` and rebuild.
