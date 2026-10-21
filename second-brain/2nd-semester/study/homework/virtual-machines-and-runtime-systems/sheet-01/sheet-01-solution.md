---
title: "Exercise Sheet 1 — Dynamic Libraries in C (Solutions + measured output)"
tags: [homework, virtual-machines, semester-2]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-19
---

# Virtual Machines and Runtime Systems — Exercise Sheet 1

Source: `01.pdf`, `addrs.c`, `eval.c` (Größlinger, due 22.10.2026, discussion 23.10.2026).
Files in this folder: `showaddrs.c`, `showaddrs.h`, `addrs.c`, `eval.c`.
The outputs below are from real runs on x86-64 Linux (glibc 2.35), not from the slides.

---

## Problem 1 — Addresses

### Deliverables

- `showaddrs.c` / `showaddrs.h` — the library: declares the same linker symbols (`etext`, `edata`, `end`) and prints them from inside the library.
- `addrs.c` — the extended main program: prints the segment bounds itself, then calls the library. `-DUSE_DLOPEN` switches it to the run-time-loading variant.

### Build commands (as the sheet asks)

```bash
# (a) static
gcc -c showaddrs.c -o showaddrs.o
ar rcs libshowaddrs.a showaddrs.o
gcc addrs.c libshowaddrs.a -o addrs_static

# (b) link-time dynamic, found at run time via rpath
gcc -fPIC -shared showaddrs.c -o libshowaddrs.so
gcc addrs.c -L. -lshowaddrs -Wl,-rpath,. -o addrs_dynamic

# (c) no link at all — dlopen/dlsym
gcc -DUSE_DLOPEN addrs.c -ldl -o addrs_dlopen
```

One portability note: `-Wl,-rpath,.` puts a *relative* path into the binary, which is fragile outside the build directory. `-Wl,-rpath,'$ORIGIN'` is the portable form (the loader resolves it relative to the executable's own directory). The measured run below used `$ORIGIN`.

### Measured results

```
=== (a) STATIC ===
[main] end of text: 0x1001840
[main] end of data: 0x10039d0
[main] end of bss:  0x1004970
[main] beginning of heap: 0xa23e2a0
[main] top of stack: 0x7fff0d0e0300
[main] show_addrs (library code): 0x10017a0
[lib] end of text: 0x1001840
[lib] end of data: 0x10039d0
[lib] end of bss:  0x1004970

=== (b) DYNAMIC (link-time, $ORIGIN rpath) ===
[main] end of text: 0x1001880
[main] end of data: 0x1003a40
[main] end of bss:  0x10049e0
[main] beginning of heap: 0x22da42a0
[main] top of stack: 0x7fff1e2a1a20
[main] show_addrs (library code): 0x7d0deb17d460
[lib] end of text: 0x1001880
[lib] end of data: 0x1003a40
[lib] end of bss:  0x10049e0

=== (c) DLOPEN (loaded at run time) ===
[main] end of text: 0x1095620
[main] end of data: 0x109cf10
[main] end of bss:  0x109ef00
[main] beginning of heap: 0x1a8f72a0
[main] top of stack: 0x7ffca25fa520
[lib] end of text: 0x7b569d2fb4e0
[lib] end of data: 0x7b569d2fc658
[lib] end of bss:  0x7b569d2fd000
[main] library function at: 0x7b569d2fb460
```

(Addresses change between runs: PIE executables and ASLR. The *pattern* is what matters.)

### How the three cases compare

| | Library code lives at | `etext`/`edata`/`end` seen by the library |
|---|---|---|
| (a) static | same address range as `main` (`0x10017a0`) | **identical** to main's — there is one copy of everything in one binary |
| (b) link-time dynamic | a high address (`0x7d0d…`) — the mmap area, far from text/data/BSS | **identical** to main's, despite the code being elsewhere |
| (c) dlopen | a high address (`0x7b56…`) | **different** — the library's own segment ends |

**Why (b) and (c) differ from each other is the interesting part.** `etext`, `edata`, `end` are produced by the linker script, and the dynamic loader resolves a shared object's undefined symbols against the **global symbol scope**, in which the main executable comes first. In case (b) the library was linked *with* the program, so the linker exports those symbols from the executable and the library binds to the executable's definitions — both print the same values. In case (c) nothing links against the library, and the standalone `.so` carries its own definitions of the same symbols, so it reports its own segment ends. Meanwhile the library's *code address* is high in both (b) and (c), because that is where the mmap area is: between heap and stack, which is exactly the slide's layout (`text | data | BSS | heap ↔ … ↔ mmap ↔ stack | kernel`).

Practical takeaway: "where does the library live" and "which segment ends does it see" are two different questions, and the answers diverge as soon as symbols are preemptible.

On 32-bit targets (`-m32`) the same program prints the same structure with the layout compressed below the 2 GiB boundary — the slide's 32-bit versus 64-bit note.

---

## Problem 2 — Primitive JIT compiler

`eval.c` reads an expression, writes

```c
#include <math.h>
double f(void) { return (<expression>); }
```

to `expr_tmp.c`, calls a compiler to build `expr_tmp.so`, `dlopen`s it, resolves `f` with `dlsym`, calls it, prints the value and unloads.

The compiler is taken from `$CC` (default `gcc`) so the same program works on any machine with any compiler.

### Measured run

```
$ printf "2+3*4\nsqrt(144)\nsin(0)+cos(0)\n" | ./eval
> 2+3*4 = 14
> sqrt(144) = 12
> sin(0)+cos(0) = 1
> quitting
```

Every expression was genuinely compiled into a shared object at run time and executed through `dlsym`. `-lm` is needed because the generated code calls `math.h` functions.

### Notes that matter

- **`dlopen` is what makes this a JIT**, not a wrapper: the compiler's output is a library, and the running process obtains a function pointer from it. No re-execution, no `exec`.
- **`dlsym` error handling is the trap the lecture warns about.** A symbol can legitimately resolve to `NULL`, so the return value alone is not an error indicator — you must clear with `dlerror()` before the lookup and check `dlerror()` after it. The solution does both.
- **Relative paths on purpose.** The compiler runs as a child process and the loader runs in this process; both must see the same file. Using relative filenames plus the working directory keeps them consistent.
- **Notice the ordering bug that is not obvious:** compiling into `expr_tmp.so` while a previous version is still `dlopen`ed replaces the file on disk, but the loaded image stays mapped. Closing the handle before the next compile (as here) avoids relying on that.
- **32-bit vs 64-bit and `-fPIC`:** the generated object has to be position-independent to be loaded as a shared object; without `-fPIC` the link fails on x86-64.

### Static-versus-dynamic size consequence

In case (a) the library's code is copied into the binary. In (b) and (c) one physical page of the library can be mapped into the address spaces of many processes, so the library's text is shared. That is the memory argument for dynamic libraries from the lecture — and the reason the very first thing `ld.so` does is decide where to map each library.
