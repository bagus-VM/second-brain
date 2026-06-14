---
title: "Binary Build Reproducibility"
tags: [concept, reproducibility-engineering, semester-1, reproducibility, binary-build, compiler]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducible-builds]]", "[[deterministic-builds]]", "[[reprotest]]", "[[c-preprocessor]]"]
---

## One-line Summary
Binary build reproducibility is the property that compiling the same source code twice — across different days, paths, build directories, or compiler versions — produces *bitwise identical* output binaries; the lecture's exercise shows that even trivial source differences (`__FILE__`, `__TIME__`, `__LINE__`) silently break this property.

## Core Intuition
For interpreted languages, "the program is the source" — copying the source reproduces the program. For compiled languages, "the program is the binary" — and the binary is generated. If the generation is non-deterministic, the binary can drift even when the source is identical.

The exercise (Sheet 6, task 2) makes this concrete with a C hello-world:

| # | Program | Bitwise identical rebuilds? |
|---|---------|------------------------------|
| 1 | `printf("%s\n", "Hello World")` | YES — no embedded non-determinism |
| 2 | `printf("File: %s\n", __FILE__)` | NO — `__FILE__` expands to the absolute path of the source file at compile time |
| 3 | `printf("Built: %s\n", __TIME__)` | NO — `__TIME__` expands to the wall-clock time of compilation |
| 4 | `printf("Line: %d\n", __LINE__)` | NO — `__LINE__` expands to the current line number; if the source is moved or edited, the value changes |

So 1 out of 4 programs allows for bitwise identical builds. The other 3 silently embed build-time information that varies with *where*, *when*, and *how* the build was performed.

## Formal Definition / Statement

A build is **binary-reproducible** if, for any two build environments e₁ and e₂ that satisfy the same source and build-commands contract:

    sha256(build(source, env₁)) == sha256(build(source, env₂))

The "contract" is everything the build is allowed to depend on:
- The source code (deterministic)
- The build commands (deterministic, in the right order)
- The build dependencies (libraries, compilers — pinned by version)
- The build environment (paths, timestamps, locales — should NOT affect output)

Anything *outside* the contract is a potential source of non-determinism.

### Sources of non-determinism in compiled builds

1. **Embedded timestamps**: `__TIME__`, `__DATE__`, build-time `date` invocations, filesystem mtimes in archives.
2. **Embedded paths**: `__FILE__` (absolute), debug info paths, RPATH/RUNPATH entries.
3. **Embedded line numbers**: `__LINE__`, debug info line tables.
4. **Locale-dependent behaviour**: sorting order, number formatting.
5. **Random seeds**: uninitialised RNG, parallel-build race conditions.
6. **Build-order effects**: parallel `make -j` can order object files differently.
7. **Compiler-internal randomness**: link-time optimisation, profile-guided optimisation.
8. **Filesystem metadata**: order of directory listings, inode numbers.

## Key Properties

### Why bitwise identical matters
- **Verifiability**: anyone can `sha256sum` the binary and compare against a published reference. No "trust me, it's the same code" step.
- **Distribution**: a single canonical binary can be served by many mirrors and verified by all users.
- **Forensics**: bitwise identicality rules out tampering. (This is the basis of the Reproducible Builds project for Debian.)
- **Reproducibility research**: bitwise identical binaries prove the *build* is reproducible; the *results* are a separate question.

### Why bitwise identical is harder than it looks
- The default GCC and Clang produce non-deterministic output for many legitimate code patterns.
- Even with `-O2` and no debug info, embedded paths in the symbol table can break bitwise identicality.
- The fix is usually `-ffile-prefix-map=old=new` for paths, `SOURCE_DATE_EPOCH` for timestamps, and careful dependency pinning.

### The Reproducible Builds project
A Debian-led project (reproducible-builds.org) that systematically fixes non-determinism in Debian packages. As of 2024, the vast majority of Debian packages build reproducibly. The tools: `diffoscope` (visual diff), `reprotest` (harness), `strip-nondeterminism` (post-processor).

## Worked Example

The lecture's task 2.4 walks through `hello.c` step by step:

```c
// hello.c
#include <stdio.h>
int main() {
    printf("Built: %s\n", __TIME__);  // Program 3 from above
    return 0;
}
```

Build #1:
```bash
user@container$ gcc hello.c -o hello
user@container$ ./hello
Built: 11:28:40
```

Build #2 (5 seconds later):
```bash
user@container$ gcc hello.c -o hello
user@container$ ./hello
Built: 11:28:45  # different time → different binary
```

Functional equivalence: yes (both print the time, just different times). Bitwise identical: no (the `__TIME__` string is embedded in the binary's `.rodata` section).

The fix: set `SOURCE_DATE_EPOCH` to a fixed value, or rewrite the program to not embed the time at all.

## Common Pitfalls
- **"Two compilers produced the same output"**: they did *functionally* — same hello-world text. But the binaries differ in symbol table, section ordering, debug info, etc. Bitwise identicality is a *much* stricter property.
- **"Different optimisation levels break it"**: yes, but the *same* optimisation level on the *same* source can still break it because of timestamps. Optimisation level is just one of many sources.
- **Confusing the build environment with the source**: `__FILE__`, `__TIME__`, `__LINE__` are *source-level features* that leak build-environment info. They are not bugs in the compiler.
- **Forgetting the symbol table**: even without source-level leaks, the symbol table embeds the build path. Use `-ffile-prefix-map` or strip.
- **Ignoring parallel builds**: `make -j` is faster but introduces order-dependent output. Solutions: deterministic make, sorted object lists, single-thread build.
- **The reproducibility-utility trade-off**: aggressive stripping breaks debugging. The Reproducible Builds project distinguishes "source identical" (good) from "source stripped of debug info" (also reproducible, but different artifact).

## Connections
- [[reproducible-builds]] — the broader topic
- [[deterministic-builds]] — the narrower form
- [[reprotest]] — the tool for testing bitwise identicality
- [[c-preprocessor]] — the macro-level sources of non-determinism (`__FILE__`, `__TIME__`, `__LINE__`)
- [[source-date-epoch]] — the standard fix for embedded timestamps
- [[diffoscope]] — for visualising the differences
- [[containerization-for-builds]] — for isolating the build environment

## Open Questions
- Can bitwise identical builds be guaranteed by *construction* in a programming language design? (E.g., a language with no preprocessor, no inline assembly, no path-dependent features. Crystal and Go make some progress.)
- For interpreted code that is "compiled" at install time (Python wheels, npm packages), how does the reproducibility story change? (The wheel is the binary; reproducibility requires bitwise-identical wheels from same source.)
- How does the Reproducible Builds project's verification scale to billions of binaries? (Distributed verification, attestation frameworks, in-toto.)
