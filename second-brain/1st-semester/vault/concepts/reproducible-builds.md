---
title: "Reproducible Builds"
tags: [concept, reproducibility-engineering, semester-1, builds]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

A build is reproducible if the same source code, build instructions, and build environment always produce a bit-for-bit identical artifact.

## Core Intuition

Reproducible builds solve the "trusting trust" problem: when you download a compiled binary, how do you know it was actually built from the source code you can see? If anyone -- anywhere, anytime -- can take the same source and produce the exact same binary, then the build process itself becomes verifiable. This eliminates an entire class of supply-chain attacks where a compromised compiler or build server could inject malicious code.

## Formal Definition / Statement

A build is **reproducible** if:

> Given the same source code, build environment, and build instructions, any party can recreate bit-for-bit identical copies of all specified artifacts.

Formally: for all builders B₁, B₂ and source S: `Build(B₁, S) = Build(B₂, S)` at the byte level.

This means:
- Same compiler version and flags
- Same library versions
- Same build environment (paths, locale, timezone)
- Same ordering of inputs

## Key Properties / Complexity

- **Bit-for-bit identity**: The output must be byte-identical, not just functionally equivalent.
- **Build environment specification**: The entire build environment must be fully described and reproducible.
- **Input determinism**: File ordering, glob results, and iteration order must be deterministic.
- **No embedded non-determinism**: No timestamps, no random values, no machine-dependent paths.
- **Verifiable by third parties**: Anyone with access to the source and build description can verify.
- **Detection of supply-chain attacks**: Any unauthorized modification to source or tools produces a different binary.

## Worked Example

### The Non-Deterministic Makefile (from Lecture 5)

```makefile
SRCS = $(wildcard *.c)
tool: $(SRCS:.c=.o)
    $(CC) -o $@ $^
```

Build 1 on machine A: `wildcard` returns `a.c b.c c.c` → link order: `a.o b.o c.o`
Build 2 on machine B: `wildcard` returns `c.c a.c b.c` → link order: `c.o a.o b.o`

The resulting binaries may differ due to different link ordering affecting symbol tables and layout.

**Fix**: Use `$(sort $(wildcard *.c))` to impose lexicographic ordering, or explicitly list sources.

### The Timestamp Macro Problem

```c
printf("Built at: %s %s\n", __TIME__, __DATE__);
```

Two builds one second apart produce different binaries. The `SOURCE_DATE_EPOCH` mechanism (see [[source-date-epoch]]) overrides these macros to use a fixed timestamp.

## Common Pitfalls

1. **Wildcard file enumeration**: `$(wildcard *.c)` depends on filesystem ordering.
2. **Embedded timestamps**: `__TIME__`, `__DATE__` change every second.
3. **Embedded paths**: `__FILE__` includes the absolute build path.
4. **Locale-dependent output**: Tools like `sort` behave differently under different locales.
5. **Parallelism-dependent ordering**: Parallel builds may process files in different orders.
6. **Network-dependent downloads**: Fetching dependencies during build introduces network-state dependency.

## Connections

- [[deterministic-builds]] -- The technical mechanisms for achieving bit-for-bit identity
- [[build-environment-isolation]] -- Isolating the build context from host variations
- [[source-date-epoch]] -- Standard mechanism for reproducible timestamps
- [[diffoscope]] -- Tool for comparing build artifacts
- [[ci-cd-for-reproducibility]] -- Automated verification of reproducibility
- [[containerization-for-builds]] -- Using containers for environment isolation
- [[package-manager-reproducibility]] -- Nix, Guix, and lock files
- [[reproducibility-engineering-lecture-5]] -- Full lecture notes

## Open Questions

1. What is the economic cost of maintaining reproducible builds for large projects?
2. How do reproducible builds interact with link-time optimization (LTO)?
3. Can reproducibility be guaranteed across different hardware architectures?
