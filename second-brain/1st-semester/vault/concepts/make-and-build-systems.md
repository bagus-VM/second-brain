---
title: "Make and Build Systems"
tags: [concept, reproducibility-engineering, semester-1, build-systems, make]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

Make is a build automation tool that uses file timestamps and dependency rules to determine what needs rebuilding, but its implicit behaviours can introduce non-determinism into builds.

## Core Intuition

The lecture (Exercises 3-5) builds up Make from scratch: Make tracks which source files are newer than their compiled outputs and only rebuilds what changed. This timestamp-based model is efficient but fragile -- it depends on filesystem timestamps, file ordering, and implicit rules that can all break reproducibility. Understanding Make deeply is essential because most real-world build systems (CMake, autotools, Meson) ultimately generate Makefiles.

## Formal Definition / Statement

A **Makefile** defines:

1. **Targets**: Files to be created (e.g., `tool`, `tool.o`)
2. **Dependencies**: Files that targets depend on (e.g., `tool.o` depends on `tool.c`)
3. **Recipes**: Commands to create targets from dependencies

The core rule: a target is rebuilt if any dependency is newer than the target (based on filesystem timestamps). This is the "timestamp model" of build correctness.

```
target: dependency1 dependency2
    command to create target
```

## Key Properties / Complexity

- **Timestamp-based rebuilds**: Make compares modification times to decide what to rebuild.
- **Wildcard expansion**: `$(wildcard *.c)` expands to files in filesystem-dependent order.
- **Automatic variables**: `$@` (target), `$^` (all dependencies), `$<` (first dependency).
- **Pattern rules**: `%.o: %.c` defines how to build any `.o` from its `.c`.
- **Phony targets**: `.PHONY` targets (like `clean`) always run regardless of timestamps.
- **Parallel builds**: `make -j` runs independent recipes in parallel, which can affect ordering.

## Worked Example

### The File Update Problem (Exercise 3)

```
thruster.c   11:43    → thruster.o   11:48    → \
turbo.c      12:15    → turbo.o      12:22    →  → ems  14:26
graticule.c  14:52    → graticule.o  14:25    → /  (but graticule.c is newer!)
servo.c      13:47    → servo.o      13:46    → /
```

`graticule.c` (14:52) is newer than `graticule.o` (14:25), so `graticule.o` must be rebuilt. Since `graticule.o` will be newer than `ems` (14:26), `ems` must also be rebuilt. But `turbo.o` (12:22) and `servo.o` (13:46) are also older than `ems` -- however, they don't need rebuilding because their source files haven't changed.

### The Non-Reproducible Wildcard (Exercise 5)

```makefile
SRCS = $(wildcard *.c)          # Problem: filesystem-dependent order
tool: $(SRCS:.c=.o)
    $(CC) -o $@ $^
```

The link order of object files depends on filesystem enumeration, which varies across systems and over time.

**Fix**:
```makefile
SRCS = $(sort $(wildcard *.c))  # Deterministic: sorted alphabetically
# or
SRCS = a.c b.c c.c             # Explicit: no ambiguity
```

### The Make Magnets (Exercise 4)

```makefile
oggswing: oggswing.c oggswing.h
	gcc oggswing.c -o oggswing

swing.ogg: whitennerdy.ogg oggswing
	./oggswing whitennerdy.ogg swing.ogg
```

Note: the recipe lines must start with a TAB character, not spaces. This is a classic source of Makefile errors.

## Common Pitfalls

1. **Spaces vs tabs in recipes**: Make requires TAB characters for recipe lines. Spaces cause cryptic errors.
2. **Wildcard ordering**: `$(wildcard *.c)` is not deterministic across filesystems.
3. **Missing .PHONY**: Without `.PHONY`, if a file named `clean` exists, `make clean` does nothing.
4. **Recursive make issues**: Sub-makes don't share the dependency graph, leading to redundant builds.
5. **Parallel build races**: `make -j` can expose missing dependencies between targets.
6. **Timestamp granularity**: Some filesystems have coarse timestamp resolution (1 second), which can cause missed rebuilds.

## Connections

- [[reproducible-builds]] -- Make's implicit behaviours are a major source of non-reproducibility
- [[deterministic-builds]] -- Wildcard ordering and parallel builds affect determinism
- [[c-preprocessor]] -- Make compiles C programs; the preprocessor runs first
- [[build-environment-isolation]] -- Make's behaviour depends on the host filesystem
- [[ci-cd-for-reproducibility]] -- CI systems must handle Make's quirks correctly
- [[reproducibility-engineering-lecture-5]] -- Lecture context (Exercises 3-5)

## Open Questions

1. How do modern build systems (Meson, Bazel) handle ordering more deterministically than Make?
2. Can Make's timestamp model be made fully reliable across different filesystems?
3. How does Ninja compare to Make in terms of reproducibility guarantees?
