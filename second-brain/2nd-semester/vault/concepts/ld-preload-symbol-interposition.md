---
title: "LD_PRELOAD and Symbol Interposition"
tags: [concept, virtual-machines, semester-2, runtime-system, dynamic-linking]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: ["[[dynamic-linking]]", "[[got-plt-lazy-linking]]"]
---

## One-line Summary
`LD_PRELOAD` names shared libraries the loader maps *before* the ones the program asked for, so the symbols they define win the global lookup and replace their libc counterparts — the mechanism exercise sheet 3 uses to swap out `malloc`.

## Core Intuition
A dynamically linked program does not contain `malloc`; it contains a call through the PLT, and the PLT slot is filled by the loader from the *global symbol table* at start-up. The loader builds that table in load order, and preloaded libraries come first. So a library that defines `malloc` does not "intercept" anything at run time — it simply *is* the definition the loader resolves every `malloc` call to, including the calls inside libc itself. The program needs no changes, and usually does not know.

## Formal Definition / Statement
`LD_PRELOAD` is a whitespace-separated list of shared objects. The dynamic loader (`ld.so`) maps them before any dependency of the executable; their symbols are inserted into the global lookup scope ahead of the libraries that would otherwise define them. Lookup order for a symbol is: the executable itself, then the global scope in load order (preloads first, then the executable's `DT_NEEDED` closures), each searched breadth-first.

Two properties make the technique useful and dangerous:

- **It replaces the definition, not the call site.** Every reference resolved through the global scope — within the preloaded library itself, within libc, within other libraries — gets the preloaded definition.
- **It only affects dynamically resolved symbols.** Calls bound at link time (`-Wl,-Bsymbolic`, static linking, direct internal calls inside a library) are not redirected. In the exercise, `myprintf` exists precisely because `printf` → `malloc` → `printf` would recurse; the replacement must not call anything in the family it replaces.

## Key Properties
- Preloading one symbol lets a program substitute an entire allocation family: `malloc`, `calloc`, `realloc`, `free`, and the aligned variants (`posix_memalign`, `memalign`, `aligned_alloc`, `valloc`, `pvalloc`), which the skeleton implements on top of `malloc`.
- Order matters, and the *first* definition wins; a second preload defining the same symbol is shadowed (not layered).
- `LD_PRELOAD` is inherited through `execve`, so a program started by a preloaded process is intercepted too, unless it is set-uid or the loader's `AT_SECURE` flag is set.
- Diagnostics: the loader prints `ERROR: ld.so: object 'X' from LD_PRELOAD cannot be preloaded …` to stderr and continues *without* interception — a silent failure if the stderr is discarded. Verify with a self-identifying output rather than by assuming.
- Because the library is loaded, but not "called" first, its own initialisation order is a real constraint: it must not need anything from the library it is replacing at static-init time.

## Worked Example
The exercise's `mymalloc.c` is a preloadable allocator:

```c
// mymalloc.c — defines malloc, free, calloc, realloc, posix_memalign, …
$ gcc -Wall -std=c99 -fPIC -shared -o libmymalloc.so mymalloc.c
$ LD_PRELOAD=./libmymalloc.so ls
```

`ls` is not modified, is not recompiled, and does not cooperate. Its own `malloc(472)`, `malloc(120)`, `realloc(...)`, `free(...)` calls — and libc's internal ones — now run inside the preloaded library. The runs recorded in `study/homework/virtual-machines-and-runtime-systems/sheet-03/` show exactly that: the `myprintf` trace of a `ls -1 *.c` invocation, with the program break reported before every allocation.

The visible failure mode of the mechanism: `printf` may allocate, so a replaced allocator that logs with `printf` recurses until the stack dies. Hence `myprintf()` writing to fd 2 with `write(2, …)` and supporting only `%p`, `%u`, `%zu`.

## Common Pitfalls
- **Recursion through the replaced family.** Any allocation in the replacement's own logging path is a bug. The skeleton's `myprintf` exists only because of this.
- **Calling `malloc` while holding the allocator's lock.** The skeleton locks in `calloc`/`realloc` and then expects the body to do the work inline; calling the public `malloc` from there deadlocks on a non-recursive mutex. Implementations that share a helper must call the *unlocked* helper.
- **Interposing on a subset.** Replacing `malloc` but not `calloc`/`realloc` means a program can hand the replacement's pointer to libc's `free` (or vice versa) — two heaps, one program, immediate corruption.
- **`malloc_usable_size` and friends.** They are not part of the replaced set, so they still read libc's own chunk header, which is not there. Most programs never call them; those that do will misbehave.
- **Alignment promises.** The replacement must honour the ABI's alignment (16 bytes on x86-64), because the program may rely on it for SIMD or atomics, and glibc's own structures assume it.
- **`errno` preservation in `free`.** Any interposed function that libc calls on its own error paths must leave `errno` as it found it, or it silently changes another function's reported failure.

## Connections
- [[dynamic-linking]] — what makes the substitution possible at all: the call goes through the PLT to whatever the loader resolved.
- [[got-plt-lazy-linking]] — the resolution machinery; the preload is the global scope's first entry.
- [[sbrk-program-break]] — what the replacement allocator runs on in exercise sheet 3.
- [[runtime-system]] — the C runtime surface being replaced, and the reason `printf` cannot be used inside it.
- [[virtual-machines-and-runtime-systems-exercise-3]] — Problem 2 is this mechanism, implemented twice.
- `study/homework/virtual-machines-and-runtime-systems/sheet-03/` — both implementations and their recorded runs.

## Open Questions
- The sheet does not state whether a *partial* replacement (e.g. only `malloc`) is acceptable in the hand-in; the skeleton replaces the whole family and this vault follows it.
- Whether the tutorials expect `LD_PRELOAD` to be checked with something other than the recorded trace (e.g. `LD_DEBUG=bindings`) is not stated — the vault used the trace.
