---
title: "Reproducibility Engineering - Lecture 5: Reproducible Builds"
tags: [topic, reproducibility-engineering, semester-1, lecture-notes]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reproducibility-engineering-lecture-4]
---

## One-line Summary

Lecture 5 introduces reproducible builds through hands-on C programming exercises that expose how build systems, preprocessors, and file ordering introduce non-determinism into compiled artifacts.

## Core Intuition

A reproducible build guarantees that compiling the same source code with the same tools produces a byte-for-byte identical binary. The lecture builds this intuition from the ground up: starting with how C programs are compiled across multiple source files, how Makefiles orchestrate builds, and how the C preprocessor can silently inject non-determinism through macros like `__TIME__` and `__DATE__`. The key insight is that many seemingly innocuous build system features -- wildcard file globbing, implicit ordering, embedded timestamps -- break reproducibility in subtle ways.

## Formal Definition / Statement

A build is **reproducible** if: given the same source code, build instructions, and build environment, it is possible to reproduce a bit-for-bit identical artifact. This means no one can inject malicious code during the build process without detection. The formal criteria from reproducible-builds.org:

> A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-for-bit identical copies of all specified artifacts.

## Key Properties

- **Build environment isolation**: The build environment must be fully specified and reproducible (same compiler version, same libraries, same environment variables).
- **Deterministic file ordering**: Using `$(wildcard *.c)` in Makefiles produces file lists in filesystem-dependent order, causing non-deterministic linking order and potentially different binaries.
- **No embedded timestamps**: Macros like `__TIME__` and `__DATE__` embed the compilation time into the binary, breaking reproducibility on every rebuild.
- **No embedded paths**: `__FILE__` and `__LINE__` can vary based on build directory, introducing path-dependent differences.
- **Compiler determinism**: The same compiler version with the same flags must produce identical output regardless of build order or timing.
- **Verification via tools**: [[diffoscope]] can compare two builds at a deep structural level to identify exactly where they differ.

## Worked Example

### Exercise 5 (Non-reproducible Makefile)

The lecture presents this Makefile:

```makefile
SRCS = $(wildcard *.c)
tool: $(SRCS:.c=.o)
    $(CC) -o $@ $^
```

**Problem**: `$(wildcard *.c)` returns files in an unspecified, filesystem-dependent order. The compiler processes object files in this order, which can affect symbol resolution, link order, and even optimization decisions. Two builds on different machines (or even the same machine after a filesystem defrag) can produce different binaries from identical source code.

**Fix**: Replace the wildcard with an explicit, sorted source list:

```makefile
SRCS = $(sort $(wildcard *.c))
```

Or better, explicitly list all source files:

```makefile
SRCS = thruster.c turbo.c graticule.c servo.c
```

### Exercise 6c (Preprocessor timestamp injection)

```c
printf("__TIME__ = %s\n", __TIME__);
printf("__DATE__ = %s\n", __DATE__);
```

Every compilation embeds the current time and date into the binary. Two consecutive builds will always produce different binaries, making reproducibility impossible. The fix: avoid `__TIME__` and `__DATE__`, or override them with fixed values:

```bash
gcc -D__DATE__='"Jan  1 2026"' -D__TIME__='"00:00:00"' testCPP.c
```

### Exercise 7 (Heisenbug)

The `assert(someinitialization() == FALSE)` pattern: when compiled with `-DNDEBUG`, the assert is removed entirely, `someinitialization()` is never called, and `p` remains an invalid pointer `(char *)5`, causing a crash. This demonstrates how build flags can change program behavior -- a form of non-determinism between debug and release builds.

## Common Pitfalls

1. **Assuming wildcard is safe**: `$(wildcard *.c)` seems convenient but breaks reproducibility through filesystem-dependent ordering.
2. **Embedding build metadata carelessly**: `__TIME__`, `__DATE__`, `__FILE__`, and `__LINE__` all inject non-deterministic values. Many projects (including the Linux kernel) carefully manage these.
3. **Ignoring link order**: Object file order in linking can affect symbol resolution and binary layout. Different linkers may handle this differently.
4. **Not isolating the build environment**: System-dependent paths, locale settings, timezone, and environment variables can all leak into builds.
5. **Debug vs release behavioral differences**: As the Heisenbug exercise shows, build flags like `-DNDEBUG` can remove code entirely, changing program semantics.
6. **Trusting timestamps for correctness**: The "file update" exercise (Exercise 3) shows how Make uses file timestamps to determine what needs rebuilding -- but timestamps can be manipulated or unreliable.

## Connections

- [[reproducibility-engineering-lecture-4]] -- Prior lecture; this builds on containerization concepts
- [[deterministic-builds]] -- The core goal: bit-for-bit identical output from identical inputs
- [[build-environment-isolation]] -- Containers and virtual environments to control build context
- [[source-date-epoch]] -- The `SOURCE_DATE_EPOCH` environment variable for reproducible timestamps
- [[diffoscope]] -- Tool for deep comparison of build artifacts
- [[ci-cd-for-reproducibility]] -- Using CI pipelines to verify build reproducibility
- [[containerization-for-builds]] -- Docker/Podman for isolating build environments
- [[package-manager-reproducibility]] -- Nix, Guix, and lock files for reproducible dependency resolution
- [[make-and-build-systems]] -- Make fundamentals: dependencies, timestamps, and build ordering
- [[c-preprocessor]] -- How macros expand and what non-determinism they introduce

## Open Questions

1. How does the `SOURCE_DATE_EPOCH` mechanism work in practice for large projects with complex build systems?
2. What is the performance cost of enforcing reproducibility in CI/CD pipelines?
3. How do modern container runtimes (Docker, Podman) ensure build environment reproducibility across different host systems?
4. Can reproducibility guarantees be maintained for cross-compilation targets?
5. How does Nix/Guix approach the build ordering problem differently from traditional Make?
