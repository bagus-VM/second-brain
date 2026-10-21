---
title: "Python for Deep Learning"
tags: [concept, deep-learning, python, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[python-environment-management]]"]
---

## One-line Summary
Python is the lingua franca of machine learning not because it is fast, but because it is readable, dynamically typed, garbage-collected, and glued to C — and every DL library speaks it.

## Core Intuition
The course assumes you can already program; the barrier is syntax, not concepts. Python is close to pseudocode: indentation instead of braces, no compile step, no type declarations, automatic memory management. That makes it fast to write and slow to run — which is fine, because the expensive parts (matrix multiplication, convolutions) are C or CUDA underneath. You write the orchestration; someone else wrote the loops.

## Formal Definition / Statement

**Why Python, per the lecture:**

- **Simple (?)** — high-level, almost pseudocode; interpreted (no compile step, runs everywhere); dynamically typed; automatic memory management (garbage collection).
- **Powerful** — large standard library, huge ecosystem.
- **Extensible** — integrate C for critical parts.
- **Inevitable** — almost everything related to ML uses Python.

The lecture adds the honest caveat: Python was never intended for AI. Alternatives are being explored (it names Tensor Logic).

**Syntax essentials demonstrated:**

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(a))
```

```python
for i in range(10):
    print(i)
```

Indentation is syntax, not style. A block must be consistently indented (typically 4 spaces); the lecture shows that the same two lines without indentation are an invalid program.

**FizzBuzz** (the course's canonical "you can actually write code" check):

```python
def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(n=100)
```

Note the order: the `and` case must come first, or it is shadowed by the single-condition branches. That is the classic trap in this exercise, and the reason it is used as a filter.

## Key Properties

- **Interpreted, dynamically typed, GC'd** — fast iteration, no compile-time safety net.
- **Ecosystem:** NumPy (arrays), pandas (tabular data), scikit-learn (classical ML), PyTorch (deep learning), matplotlib/seaborn (plots), Jupyter (interactive notebooks).
- **Performance model:** Python orchestrates, C/CUDA computes. Vectorise instead of looping.
- **Toolchain:** `uv` for environments, VS Code + Ruff for editing/formatting, Jupyter for exploration.

## Worked Example — the runtime path of one line

```python
print(sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
```

1. `sum` is a builtin implemented in C; it iterates the list without creating a Python-level loop frame.
2. Each `int` is a PyObject; small integers are cached, so no allocation per element.
3. `print` converts the result to a string and writes to stdout.

Compare with `for i in range(10): total += i`, which executes ten bytecode-level iterations and re-boxes the accumulator each time. Same result, ~an order of magnitude slower. This is why "use NumPy" is not a style preference but the whole performance strategy.

## Common Pitfalls

- **Inconsistent indentation.** Mixing tabs and spaces, or changing indent width mid-block, is a syntax error — not a warning.
- **Assuming Python is fast enough for the inner loop.** It is not; that is what NumPy and PyTorch are for.
- **Using Jupyter for everything.** The lecture calls notebooks a "blessing and curse": they keep state and encourage spaghetti code and bad habits.
- **Installing packages globally.** Two projects needing NumPy 1.13 and 2.0 cannot share one environment. See [[python-environment-management]].
- **Skipping FizzBuzz-class basics.** The homework assumes you can write simple functions; the course does not slow down for syntax later.

## Connections

- [[python-environment-management]] — `uv`, virtual environments, reproducibility.
- [[deep-learning-course-roadmap]] — where Python fits in the 15-week arc (week 1 only).
- [[ml-pipeline-scikit-learn]] — the same libraries used for a security task in ML4CySec.

## Open Questions

- The lecture mentions "Tensor Logic" as a possible post-Python direction. What is it, concretely? The slide gives no reference.
- How much of the homework is expected to be idiomatic Python versus working code? The course never states a style standard.
