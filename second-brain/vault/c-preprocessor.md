---
title: "C Preprocessor and Build Non-Determinism"
tags: [concept, reproducibility-engineering, semester-1, c-language, preprocessor]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

The C preprocessor transforms source code before compilation, and its built-in macros (`__TIME__`, `__DATE__`, `__FILE__`) inject non-deterministic values that break reproducible builds.

## Core Intuition

Lecture 5 (Exercises 6-7) demonstrates that the C preprocessor is the first stage of the build pipeline and the first place where non-determinism can enter. The preprocessor handles `#include`, `#define`, conditional compilation (`#ifdef`), and built-in macros. Two of these built-in macros -- `__TIME__` and `__DATE__` -- directly embed the current wall-clock time into the binary, making every build unique. Understanding the preprocessor is essential because it reveals that non-determinism can enter the build *before* the compiler even runs.

## Formal Definition / Statement

The C preprocessor performs:

1. **File inclusion**: `#include <stdio.h>` → replaces with file contents
2. **Macro expansion**: `#define BUFFSIZE 1024` → text substitution
3. **Conditional compilation**: `#ifdef NDEBUG` → include/exclude code blocks
4. **Built-in macros**:
   - `__LINE__` → current line number (deterministic, given fixed source)
   - `__FILE__` → current file path (non-deterministic if build path varies)
   - `__TIME__` → compilation time as "HH:MM:SS" (non-deterministic)
   - `__DATE__` → compilation date as "Mon DD YYYY" (non-deterministic)

Macro expansion is **textual substitution**, not evaluation. This has surprising consequences (Exercise 6b).

## Key Properties

- **Textual substitution**: `#define a(b) b + 1` → `a(1) + 1` becomes `1 + 1 + 1` = 3, not `a(1)` = 2 then 2 + 1 = 3. The macro expands to `1 + 1`, then `+ 1` is added.
- **No type checking**: The preprocessor operates on text tokens, not typed values.
- **Conditional compilation**: `#ifdef NDEBUG` removes `assert()` entirely, changing program behavior (Exercise 7).
- **Non-deterministic macros**: `__TIME__` and `__DATE__` change with every build.
- **Path-dependent macros**: `__FILE__` contains the absolute path, which varies by build location.

## Worked Example

### Exercise 6a: Simple Macro Expansion

```c
#define BUFFSIZE 1024
int buf[BUFFSIZE + 1];
```

After preprocessing:
```c
int buf[1024 + 1];  // → int buf[1025];
```

This is deterministic -- no external state involved.

### Exercise 6b: Surprising Macro Expansion

```c
#define a(b) b + 1
int x = a(1) + 1;
```

After preprocessing:
```c
int x = 1 + 1 + 1;  // = 3, not 2 + 1 = 3
```

Wait -- both give 3 here. But consider `a(1) * 2`:
- Without macro: `(1 + 1) * 2 = 4`
- With macro: `1 + 1 * 2 = 3` (due to operator precedence)

This is why macros should use parentheses: `#define a(b) ((b) + 1)`.

### Exercise 6c: Non-Deterministic Macros

```c
printf("__TIME__ = %s\n", __TIME__);  // "14:32:07" -- changes every second
printf("__DATE__ = %s\n", __DATE__);  // "Jun  1 2026" -- changes every day
printf("__FILE__ = %s\n", __FILE__);  // "/home/user/test.c" -- varies by machine
printf("__LINE__ = %d\n", __LINE__);  // "5" -- deterministic
```

### Exercise 7: The Heisenbug

```c
#include <assert.h>
char *p = (char *)5;
int someinitialization(void) {
    p = "abc";
    return 0;
}
int main(int argc, char **argv) {
    assert(someinitialization() == 0);
    printf("%s\n", p);
    return 0;
}
```

- `gcc heisenbug.c -o heisenbug`: `assert()` calls `someinitialization()`, `p` becomes `"abc"` → prints "abc"
- `gcc -DNDEBUG heisenbug.c -o heisenbug`: `assert()` is removed entirely, `someinitialization()` never runs, `p` remains `(char *)5` → **SEGFAULT**

The preprocessor's conditional compilation changes program behavior. This is a form of build non-determinism between debug and release configurations.

## Common Pitfalls

1. **Embedding `__TIME__` and `__DATE__`**: Every build is different. Use [[source-date-epoch]] to fix.
2. **Using `__FILE__` in output**: Contains absolute path, varies by build location.
3. **Macro expansion surprises**: Textual substitution doesn't respect operator precedence. Always parenthesize macro arguments.
4. **Side effects in macro arguments**: `#define square(x) ((x) * (x))` evaluates `x` twice. `square(i++)` increments `i` twice.
5. **Debug/release behavioral differences**: `#ifdef NDEBUG` can remove code entirely, changing program semantics.
6. **Include path dependence**: `#include "file.h"` searches relative to the current file; `#include <file.h>` searches system paths. Both can vary by machine.

## Connections

- [[reproducible-builds]] -- Preprocessor macros are a primary source of non-reproducibility
- [[deterministic-builds]] -- `__TIME__` and `__DATE__` are non-deterministic by definition
- [[source-date-epoch]] -- The standard fix for timestamp macros
- [[make-and-build-systems]] -- Make invokes the preprocessor as part of compilation
- [[build-environment-isolation]] -- `__FILE__` depends on the build environment's path
- [[reproducibility-engineering-lecture-5]] -- Lecture context (Exercises 6-7)

## Open Questions

1. How do modern compilers handle `__TIME__` when `SOURCE_DATE_EPOCH` is set?
2. Can the preprocessor be made fully deterministic for cross-compilation?
3. How do header-only libraries (common in C++) affect preprocessor-based reproducibility?
