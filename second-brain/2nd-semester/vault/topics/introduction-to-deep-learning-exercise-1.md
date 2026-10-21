---
title: "Introduction to Deep Learning — Exercise 1 Overview (Python)"
tags: [topic, deep-learning, semester-2, python]
course: "Introduction to Deep Learning"
source_count: 5
status: current
last_updated: 2026-10-20
prerequisites: []
---

## One-line Summary
The first session is not deep learning: it is the Python on-ramp the whole course stands on, plus an
opinionated toolchain (`uv`, VS Code, Ruff, Jupyter) that the remaining 14 weeks assume you already run.

## Core Map

```
Exercise 1 — Introduction to Python
│
├── Why Python                                        -> [[python-for-deep-learning]]
│   ├── high-level, interpreted, dynamically typed, GC'd
│   ├── huge ecosystem; C for the critical parts
│   └── syntax essentials: indentation, for/if/elif, FizzBuzz
│
├── Running code                                      -> [[python-environment-management]]
│   ├── environment managers: one venv per project
│   │   └── numpy 1.13 vs 2.0 conflict, reproducibility
│   ├── uv init / add / run
│   ├── VS Code + Python + Jupyter + Ruff, format on save
│   └── Jupyter: state-keeping and plots vs spaghetti code
│
├── The demo notebooks                                -> [[linear-algebra-for-deep-learning]]
│   ├── dot product, vector add, normalisation
│   ├── Matrix class: matmul, __add__, the deepcopy pitfall
│   └── NumPy: @ vs *, a[:, 1], a + 1
│
├── The notebook that lies about itself               -> [[jupyter-notebook-state]]
│   ├── stored outputs are snapshots of one execution
│   ├── the y == 4 / print(y) == 5 puzzle (f was x+3)
│   └── the rule: run each cell exactly once, in order
│
└── Where this is going (15 weeks)                    -> [[deep-learning-course-roadmap]]
    └── PyTorch in week 2
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[python-for-deep-learning]] | Why Python dominates ML — readable, glue to C, and unavoidable — plus the syntax traps (indentation is syntax) |
| [[python-environment-management]] | `uv`, one virtual environment per project, the kernel-selection trap, and the notebook trade-off |
| [[linear-algebra-for-deep-learning]] | The dot product, matrix multiply and normalisation a neural network performs, written out in plain Python and then in NumPy — and the aliasing pitfall that makes `b = a` not a copy |
| [[jupyter-notebook-state]] | A notebook cell's output is a snapshot of one execution, not a property of the code above it — with the course's own `f(2)` puzzle worked out |
| [[deep-learning-course-roadmap]] | The 15-week schedule and the actual dependency chain between topics |

## Lecture Structure

1. **Know your audience / organisation** — two identical Thursday sessions (12:15–13:45 and
   14:15–15:45) in SR 029 (WIWI); join one group in Stud.IP; homework is not graded; 1 ECTS ≈ 30 h.
2. **Tests** — do not affect the final grade, shown to improve learning (Roediger et al., 2011).
3. **Why Python** — the case for it, plus the honest caveat that it was never designed for AI.
4. **Simple programs** — lists, `print(sum(...))`, `range`, indentation as syntax, FizzBuzz.
5. **Running code** — `python fizzbuzz.py` versus `uv run`, and why environment managers exist.
6. **Jupyter Notebooks: blessing and curse** — reruns with state, inline markdown and plots, versus
   spaghetti code and bad habits. The demo notebook then shows the curse concretely: a notebook whose
   stored outputs disagree with its own source (see [[jupyter-notebook-state]]).
7. **The demo notebooks** — vectors, matrices and NumPy, the linear algebra week 2 will need
   (see [[linear-algebra-for-deep-learning]]).
8. **Next steps** — work through `01-hw-intro-py-tasks.ipynb`; use Pandas, NumPy, scikit-learn, PyTorch.

## Exam-Relevant Points

- This session itself is unlikely to be examined as content; what matters is that **week 2 assumes it**.
- Know the toolchain commands cold: `uv init`, `uv add`, `uv run jupyter lab`, and selecting the
  `.venv` kernel.
- The Python basics still surface later: generators/comprehensions in data pipelines, dictionary
  handling, file I/O.
- The schedule's shape is examinable knowledge in a different sense: which weeks are pen-and-paper
  (3, 6, 9, 12) versus coding tells you how the exam's written part is likely framed.

## Connections

- [[introduction-to-deep-learning]] — course page with the provisional 15-week schedule.
- Homework: `study/homework/introduction-to-deep-learning/exercise-01-solution.md` and
  `exercise-01-solutions.py` — every notebook task, executed, and cross-checked against the
  professor's own `01-hw-intro-py-solutions.ipynb`.
- [[jupyter-notebook-state]] and [[linear-algebra-for-deep-learning]] — the two demo notebooks,
  which are the sources for the pages the core map branches into above.
- [[python-environment-management]] deliberately overlaps with the Semester 1 reproducibility
  material: environments are the reproducibility argument in miniature.

## Open Questions

- The exam format and date are **not** in the material. The schedule implies a written exam; that is
  an inference.
- The slide's schedule export garbles the note column ("Test 1"/"Test 2" without legible weeks), so
  which weeks carry tests is unresolved.
- Whether the course expects idiomatic Python or merely working code is never stated.
