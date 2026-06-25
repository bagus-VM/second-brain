---
title: "Source Date Epoch"
tags: [concept, reproducibility-engineering, semester-1, builds, timestamps]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reproducible-builds, deterministic-builds]
---

## One-line Summary

`SOURCE_DATE_EPOCH` is an environment variable that provides a deterministic timestamp to build tools, replacing the current time with a fixed value for reproducible builds.

## Core Intuition

Build tools often embed the current time in their output -- the C preprocessor's `__TIME__` and `__DATE__` macros are prime examples (Lecture 5, Exercise 6c). Every rebuild produces a different binary simply because time has passed. `SOURCE_DATE_EPOCH` solves this by providing a single, canonical timestamp that all build tools should use instead of the real clock. It is typically set to the last modification time of the source code (e.g., the last commit timestamp).

## Formal Definition / Statement

`SOURCE_DATE_EPOCH` is defined as an integer representing Unix epoch time (seconds since 1970-01-01 00:00:00 UTC). When set, build tools that support it should:

1. Replace all embedded timestamps with this value
2. Use it for any time-dependent output
3. Treat it as the canonical "build time" regardless of actual wall clock

The specification is maintained at https://reproducible-builds.org/specs/source-date-epoch/

Example:
```bash
export SOURCE_DATE_EPOCH=$(git log -1 --format=%ct)
# Now __TIME__ and __DATE__ use the last commit time, not wall clock
```

## Key Properties

- **Single source of truth**: One environment variable controls all build timestamps.
- **Git integration**: Naturally maps to the last commit timestamp via `git log --format=%ct`.
- **Tool support**: GCC, Python, Java, and many other tools recognize it.
- **Fallback behavior**: If not set, tools use the current time (backward compatible).
- **Integer format**: Unix epoch seconds -- simple, unambiguous, timezone-free.
- **Convention over configuration**: A simple convention that any tool can adopt.

## Worked Example

### The Problem (from Lecture 5)

```c
// testCPP.c
printf("__TIME__ = %s\n", __TIME__);  // "14:32:07"
printf("__DATE__ = %s\n", __DATE__);  // "Jun  1 2026"
```

Build at 14:32:07 → binary A
Build at 14:32:08 → binary B ≠ A

### The Solution

```bash
export SOURCE_DATE_EPOCH=1748784000  # Fixed timestamp
gcc -o testCPP testCPP.c
# Both builds produce identical binaries
```

When GCC sees `SOURCE_DATE_EPOCH`, it replaces `__TIME__` and `__DATE__` with values derived from that epoch.

### In Practice

```bash
# Set to last git commit time
export SOURCE_DATE_EPOCH=$(git log -1 --format=%ct)

# Build
make clean && make

# Verify reproducibility
sha256sum tool > checksum1
make clean && make
sha256sum tool > checksum2
diff checksum1 checksum2  # Should show no difference
```

## Common Pitfalls

1. **Not all tools support it**: Legacy tools may ignore `SOURCE_DATE_EPOCH` and still embed real timestamps.
2. **Using wall clock as fallback**: If `SOURCE_DATE_EPOCH` is not set, tools silently revert to non-reproducible timestamps.
3. **Sub-second precision**: `SOURCE_DATE_EPOCH` is integer seconds; some tools need sub-second precision.
4. **Not propagating to sub-builds**: In nested build systems, the variable must be explicitly passed to each sub-build.
5. **Confusing with other timestamp variables**: `BUILD_DATE`, `TIMESTAMP`, etc. are non-standard.

## Connections

- [[reproducible-builds]] -- `SOURCE_DATE_EPOCH` is a key mechanism for achieving reproducibility
- [[deterministic-builds]] -- Eliminates time as a source of non-determinism
- [[c-preprocessor]] -- The preprocessor macros `__TIME__` and `__DATE__` are the primary motivation
- [[build-environment-isolation]] -- Part of the environment that must be controlled
- [[diffoscope]] -- Use to verify that timestamp differences are eliminated
- [[reproducibility-engineering-lecture-5]] -- Lecture context (Exercise 6c)

## Open Questions

1. How do you handle projects with multiple independent source repositories (different commit times)?
2. What happens with `SOURCE_DATE_EPOCH` in cross-compilation scenarios?
3. Should there be a similar mechanism for other non-deterministic values (random seeds, etc.)?
