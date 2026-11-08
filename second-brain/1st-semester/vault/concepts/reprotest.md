---
title: "ReproTest"
tags: [concept, reproducibility-engineering, semester-1, reprotest, reproducibility, build]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducible-builds]]", "[[containerization-for-builds]]", "[[build-environment-isolation]]"]
---

## One-line Summary
ReproTest is a tool that builds a program twice in different simulated environments and checks whether the resulting binaries are identical — a practical, automated way to test whether a build is [[reproducible-builds|reproducible]].

## Core Intuition
A reproducible build means: given the same source, the same build environment, and the same build commands, the output is bit-for-bit identical. To *test* whether a build is reproducible, you need to vary the build environment and see if the output still matches.

**ReproTest** does exactly this. It builds the program twice, in two different simulated environments (different timestamps, different paths, different locales, etc.), and compares the resulting binaries. If they match, the build is reproducible. If they differ, ReproTest reports the differences.

The "simulated environment" is implemented using `disorderfs` (a FUSE filesystem that randomises file metadata) and `faketime` (a library that intercepts time-related system calls and returns fake values). These are wrapped in a Docker container for isolation.

## Formal Definition / Statement

A ReproTest run takes:
- A **build command**: the command to build the program (e.g., `gcc hello.c -o hello`)
- A **test artifact**: the built artifact to test (e.g., `hello`)
- Optional: a **diffoscope** call to visualise the differences

It runs the build command in two different environments:
- Environment A: original environment (no faketime/disorderfs)
- Environment B: simulated environment (faketime sets a fixed timestamp, disorderfs randomises file metadata)

It compares the two resulting artifacts using `sha256sum` (or similar). If they match: the build is reproducible. If not: the differences are reported.

## Key Properties / Complexity

### What ReproTest can detect
- **Embedded timestamps**: `__TIME__`, `__DATE__` macros, build-time `date` commands
- **Embedded paths**: `__FILE__`, absolute paths in debug info
- **Non-deterministic build order**: parallel builds with race conditions
- **Locale-dependent behaviour**: sorting strings differently in different locales
- **Random seeds**: uninitialised random number generators

### What ReproTest cannot detect
- **Source code differences**: ReproTest tests the build, not the source
- **Semantic equivalence**: identical bytes don't mean identical behaviour
- **Build environment bugs**: if the build environment is broken, ReproTest may not notice
- **Long-term reproducibility**: ReproTest tests "two builds in quick succession", not "build today matches build in 5 years"

### The dependencies
- **disorderfs**: a FUSE filesystem that randomises file metadata (timestamps, permissions, etc.)
- **faketime**: a library that intercepts time-related system calls (gettimeofday, time, etc.) and returns fake values
- **Docker**: for isolation (running the two builds in containers)
- **diffoscope**: for visualising differences (optional but recommended)

### How to use ReproTest
```bash
# Inside a Docker container with disorderfs and faketime installed:
reprotest 'gcc hello.c -o hello' hello
```

The output is a "reproducibility verdict":
- ✓ Reproducible: the two builds produced identical bytes
- ✗ Not reproducible: the two builds differ; ReproTest reports the differences

### When to use ReproTest
- **CI/CD pipeline**: run ReproTest on every build to catch non-determinism regressions
- **Release engineering**: verify that the release artifact is reproducible before publishing
- **Research**: verify that a paper's results are reproducible from the archived source
- **Supply chain security**: prove that the binary matches a known-good source

## Worked Example

The lecture's exercise:
```bash
$ reprotest 'gcc hello.c -o hello' hello
✓ hello: reproducibility verdict: reproducible (100%)
```

For a non-reproducible build:
```bash
$ reprotest 'gcc -g hello.c -o hello' hello-debug
✗ hello-debug: reproducibility verdict: not reproducible
Differences found:
  - .debug_info section: paths differ
  - .debug_line section: timestamps differ
```

This tells you that the debug build embeds paths and timestamps in the binary — the debug info is the source of non-determinism.

To fix:
```bash
$ reprotest 'gcc -g -ffile-prefix-map=$PWD=. hello.c -o hello-debug' hello-debug
# Now the paths in debug info are relative to the source dir
```

## Common Pitfalls
- **ReproTest needs to run in a controlled environment**: use Docker or similar to avoid host-specific effects
- **disorderfs and faketime must be installed**: in Debian/Ubuntu: `apt install disorderfs faketime`
- **The build must be hermetic**: if the build fetches files from the network, ReproTest may not catch the non-determinism (the network may return different bytes)
- **ReproTest only tests *build* reproducibility**, not *result* reproducibility. A reproducible build can still produce different *results* if the source code is non-deterministic.
- **Some differences are intentional**: e.g., reproducible-build-specific metadata in Debian packages. Use `--ignore` flags or `diffoscope` filters.

## Connections
- [[reproducible-builds]] — the broader topic
- [[deterministic-builds]] — the same idea, narrower scope
- [[source-date-epoch]] — a way to make timestamps deterministic
- [[diffoscope]] — the tool ReproTest uses to show differences
- [[containerization-for-builds]] — Docker for isolation
- [[build-environment-isolation]] — preventing host-specific effects
- [[reproducibility-engineering-lecture-6]] — the lecture

## Open Questions
- How do you integrate ReproTest into a CI/CD pipeline? (Run on every PR; fail the build if non-reproducible.)
- Are there language-specific ReproTest configurations? (Yes — Debian's reproducible-builds project has per-language notes.)
- Can ReproTest be extended to test for *semantic* reproducibility? (Harder — requires running the binary and comparing outputs, not just bytes.)
