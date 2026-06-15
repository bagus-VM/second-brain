---
title: "C Preprocessor"
tags: [concept, reproducibility-engineering, semester-1, c-preprocessor, macros, determinism]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducible-builds]]", "[[binary-build-reproducibility]]"]
---

## One-line Summary
The C preprocessor is a macro-expansion phase that runs before the compiler proper and substitutes `#define`d symbols and built-in macros into the source — and several of its built-in macros (`__FILE__`, `__TIME__`, `__DATE__`, `__LINE__`, `__TIMESTAMP__`) silently embed build-environment information (paths, timestamps, line numbers) that break bitwise-identical rebuilds.

## Core Intuition
The preprocessor operates on *tokens*, not on *types*. It does string substitution and file inclusion. The standard library of preprocessor macros is small but powerful — and three of them are the canonical sources of non-determinism in compiled C:

- `__FILE__` — expands to a string literal containing the *path* of the current source file (typically the path passed to the compiler, often absolute).
- `__LINE__` — expands to the current line number as an integer constant.
- `__TIME__` — expands to a string literal "hh:mm:ss" of the wall-clock time at which preprocessing began.
- `__DATE__` — expands to a string literal "Mmm dd yyyy" of the date preprocessing began.
- `__TIMESTAMP__` — non-standard but common; the file's mtime as a string.

If a `printf` statement contains any of these, the value is *baked into the binary* at compile time. Two builds at different times, from different directories, or after editing the source produce different binaries.

## Formal Definition / Statement

### The standard predefined macros
| Macro | Type | Value | Determinism |
|-------|------|-------|-------------|
| `__FILE__` | string literal | path of source file | **non-deterministic** (depends on build path) |
| `__LINE__` | integer constant | current line number | **non-deterministic** (depends on edits / move) |
| `__TIME__` | string literal | "hh:mm:ss" of preprocessing start | **non-deterministic** (wall clock) |
| `__DATE__` | string literal | "Mmm dd yyyy" of preprocessing start | **non-deterministic** (wall clock) |
| `__TIMESTAMP__` | string literal | source file mtime | **non-deterministic** (filesystem) |
| `__STDC__` | integer constant | 1 for conforming compilers | deterministic |
| `__STDC_VERSION__` | integer constant | C standard version (e.g., 201710L) | deterministic |
| `__GNUC__`, `__clang_major__` | integer constant | compiler version | deterministic per invocation |

### The four non-deterministic ones

#### `__FILE__`
```c
printf("Compiled from: %s\n", __FILE__);
// Output: "Compiled from: /home/alice/project/hello.c"
// Different if built from /home/bob/project/hello.c
```
**Fix:** Use `-ffile-prefix-map=/home/alice=.` to rewrite the prefix, or rewrite the code to not embed the path at all.

#### `__LINE__`
```c
printf("Error at line %d\n", __LINE__);
// Output depends on where the macro expansion occurs
```
**Fix:** Don't use `__LINE__` for anything that ends up in the binary (use it only for `assert` macros that get compiled out in release builds).

#### `__TIME__`
```c
printf("Built at: %s\n", __TIME__);
// Output: "Built at: 14:32:07"
```
**Fix:** Set `SOURCE_DATE_EPOCH` to a fixed Unix timestamp. The preprocessor uses this to compute `__TIME__`.

#### `__DATE__`
```c
printf("Built on: %s\n", __DATE__);
// Output: "Built on: Jun 14 2026"
```
**Fix:** Same as `__TIME__` — `SOURCE_DATE_EPOCH` controls this too.

## Key Properties

### Why these macros exist
They serve legitimate purposes:
- `__FILE__` / `__LINE__` for `assert` and error messages (great in dev, dangerous in release)
- `__TIME__` / `__DATE__` for build-info banners ("Compiled on Jun 14 2026")
- `__TIMESTAMP__` for build-tool dependency tracking (Make's "is the source newer than the object?")

The reproducibility problem is *not* that they exist — it's that they leak into release binaries by accident.

### The SOURCE_DATE_EPOCH convention
A standard environment variable (specified in <https://reproducible-builds.org/docs/source-date-epoch/>) that downstream tools *should* use as a substitute for "now":
- Build tools set `SOURCE_DATE_EPOCH=1234567890` (a fixed Unix timestamp)
- The C preprocessor (when implemented to follow the spec) uses it for `__TIME__`, `__DATE__`, and embedded timestamps
- Make uses it for `mtime` of generated files
- Tar uses it for archive mtimes
- ZIP uses it for entry mtimes

GCC, Clang, and recent versions of `tar`, `cpio`, `zip` honour the variable.

### Other non-determinism sources from the preprocessor
- `#include` paths that resolve differently based on `-I` flags or `CPATH`
- Macro expansion order (irrelevant for C — expansion is single-pass per file)
- `__has_include` (C++17 / C23) — depends on filesystem
- `__COUNTER__` (GCC/Clang extension) — non-deterministic by design

## Worked Example

The lecture's four "Hello World" variants (Sheet 6, task 6):

```c
// Program 1: reproducible
printf("%s\n", "Hello World");

// Program 2: NOT reproducible
printf("File: %s\n", __FILE__);

// Program 3: NOT reproducible
printf("Built: %s\n", __TIME__);

// Program 4: NOT reproducible
printf("Line: %d\n", __LINE__);
```

Question: "How many of the snippets allow for a bitwise identical build?"
**Answer: 1** (only Program 1).

Task 2.4(d-j) walks through the same source compiled from different working directories:
```bash
user@container$ pwd
/home/repro/task2
user@container$ gcc hello.c -o hello-file
# Internally, gcc records the path as "/home/repro/task2/hello.c"

user@container$ cd ..
user@container$ pwd
/home/repro/
user@container$ gcc task2/hello.c -o hello-file2
# Internally, gcc records the path as "/home/repro/task2/hello.c"
```

The paths happen to be identical here (gcc stores the relative path passed), so the binaries are *sometimes* bitwise identical. But:
```bash
user@container$ cd /tmp
user@container$ gcc /home/repro/task2/hello.c -o hello-file3
# gcc records "/home/repro/task2/hello.c" — still the same!
```

Surprise: gcc stores the path as it was *given* on the command line, not the resolved absolute path. So if you always pass the same path, you get identical builds. The non-determinism comes from *changing* the path, not from absolute-vs-relative.

For `__FILE__` *inside* the source:
```c
printf("%s\n", __FILE__);
```
gcc records the path as passed. If you `cd` to the directory and pass `hello.c`, you get `hello.c`. If you pass `./hello.c`, you get `./hello.c`. Identical source, different binaries.

## Common Pitfalls
- **"I'll just strip the binary"**: `strip` removes symbols but the `__FILE__`, `__TIME__` strings are in `.rodata`, not the symbol table. They survive stripping.
- **"I'll just delete the printf"**: in a 1M-line project, finding every `__FILE__` and `__TIME__` use is non-trivial. The `-Wdate-time` and `-Werror=date-time` GCC flags warn about all uses.
- **"SOURCE_DATE_EPOCH fixes it"**: only for tools that honour the variable. Custom build scripts, third-party libraries, hand-rolled Makefiles may not. Audit the full toolchain.
- **Confusing `__DATE__` and `__TIME__`**: they are *separate* string literals. `__DATE__` is the date, `__TIME__` is the time. Setting `SOURCE_DATE_EPOCH` fixes both.
- **Using `__LINE__` in inline functions**: the expansion is to the *use site*, not the definition site. Subtle and easy to miss.
- **Forgetting `__TIMESTAMP__`**: the non-standard `__TIMESTAMP__` (msvc-style) embeds the source's mtime. If the source was touched (e.g., by Git checkout), the binary changes.

## Connections
- [[reproducible-builds]] — the broader topic
- [[deterministic-builds]] — the same idea, narrower
- [[source-date-epoch]] — the standard fix for `__DATE__` / `__TIME__`
- [[binary-build-reproducibility]] — the umbrella concept
- [[c-preprocessor]] — what does the macro expansion

## Open Questions
- Should the C standard require compilers to honour `SOURCE_DATE_EPOCH` for the date/time macros? (C23 adds `__DATE_MACRO__` style features; the full integration is still in progress.)
- For non-deterministic macros (`__FILE__`, `__LINE__`), is there a portable "build-time freeze" mechanism? (Some compilers support `-fmacro-prefix-map`; not standardised.)
- Can a static analysis tool flag *all* sources of non-determinism in a C project, including indirect ones (e.g., a header that includes another header that uses `__TIME__`)? (Some linters do; full coverage is research-grade.)
