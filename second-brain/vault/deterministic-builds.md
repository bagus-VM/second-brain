---
title: "Deterministic Builds"
tags: [concept, reproducibility-engineering, semester-1, builds]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reproducible-builds]
---

## One-line Summary

Deterministic builds ensure that compilation of identical source code always produces byte-identical output, regardless of when, where, or by whom the build is performed.

## Core Intuition

The compiler is a function: source code in, binary out. For this function to be deterministic, it must not depend on any hidden variables -- timestamps, file ordering, filesystem state, or machine identity. Every source of non-determinism must be identified and eliminated. The lecture's exercises reveal several hidden variables in even simple C build systems.

## Formal Definition / Statement

A build function B is **deterministic** if:

```
∀ t₁, t₂, m₁, m₂: B(source, env, t₁, m₁) = B(source, env, t₂, m₂)
```

Where t is time, m is machine, and env is a fully specified environment. The output must be identical regardless of *when* and *where* the build occurs.

## Key Properties

- **Time-independence**: Output does not depend on build time (no `__TIME__`, `__DATE__`).
- **Path-independence**: Output does not depend on build directory (no absolute paths in `__FILE__`).
- **Order-independence**: Output does not depend on file enumeration order (no unsorted wildcards).
- **Machine-independence**: Output does not depend on host machine identity.
- **Locale-independence**: Output does not depend on system locale or timezone settings.
- **Parallelism-safety**: Parallel builds must produce the same output as sequential builds.

## Worked Example

### Sources of Non-Determinism in C Builds

From Lecture 5, exercise 6c:

```c
printf("__TIME__ = %s\n", __TIME__);   // "14:32:07" -- changes every second
printf("__DATE__ = %s\n", __DATE__);   // "Jun  1 2026" -- changes every day
printf("__FILE__ = %s\n", __FILE__);   // "/home/user/project/test.c" -- machine-dependent
printf("__LINE__ = %d\n", __LINE__);   // 3 -- stable if source doesn't change
```

Only `__LINE__` is deterministic (given fixed source). The others inject external state.

### The Makefile Ordering Problem

```makefile
SRCS = $(wildcard *.c)      # Non-deterministic: filesystem-dependent order
SRCS = $(sort $(wildcard *.c))  # Deterministic: lexicographic order
SRCS = a.c b.c c.c             # Deterministic: explicit list
```

The object files linked into the final binary affect the binary's layout, making the output depend on filesystem enumeration order.

## Common Pitfalls

1. **Assuming functional equivalence equals reproducibility**: Two binaries may behave identically but differ at the byte level.
2. **Forgetting compiler-internal randomness**: Some compilers use random seeds for optimization heuristics (e.g., ASLR-influenced code layout).
3. **Ignoring archive metadata**: `.a` archive files store member ordering; different ordering = different archive.
4. **Not controlling timezone**: Some build tools embed timezone in output.
5. **Locale-dependent sorting**: `ls`, `sort`, and other tools use locale-specific collation.

## Connections

- [[reproducible-builds]] -- The broader goal; deterministic builds are a prerequisite
- [[build-environment-isolation]] -- Controlling the environment to eliminate variables
- [[source-date-epoch]] -- Standard mechanism for time-independence
- [[make-and-build-systems]] -- How Make's timestamp model interacts with determinism
- [[c-preprocessor]] -- Preprocessor macros as sources of non-determinism
- [[reproducibility-engineering-lecture-5]] -- Lecture context

## Open Questions

1. How do modern compilers handle random seeds for optimization?
2. Can link-time optimization (LTO) introduce non-determinism?
3. How does debug information (DWARF) affect deterministic builds?
