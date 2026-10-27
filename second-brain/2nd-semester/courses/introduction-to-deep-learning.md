---
title: "Introduction to Deep Learning"
tags: [course, semester-2, deep-learning]
professor: "Prof. Dr. Florian Lemmerich"
semester: "WS 2026/27"
exam_date: "TBD"
credits: "TBD"
language: "English"
source_count: 10
status: active
last_updated: 2026-10-23
prerequisites: []
---

## One-line Summary
A build-it-yourself tour of deep learning: two exercise hours a week that walk from Python syntax to transformers and graph neural networks, with pen-and-paper and coding homework between sessions.

## Course Information

- **Professorship:** Applied Machine Learning — Prof. Dr. Florian Lemmerich, Andreas Einwiller, Max Klabunde (2021–2025 material)
- **Exercise:** Thursdays, two identical sessions — 12:15–13:45 and 14:15–15:45, Room SR 029 (WIWI)
- **Group choice:** join one group in Stud.IP (participants → groups); the two sessions exist to balance load
- **Materials:** Stud.IP
- **Workload rule:** 1 ECTS ≈ 30 hours. Homework is **not graded**, but is the actual learning mechanism.
- **Tests:** in-class tests do not affect the final grade; they exist because retrieval practice improves learning (Roediger et al., 2011)

## Provisional Schedule (15 weeks)

| Week | Content | Homework type |
|------|---------|---------------|
| 1 | Introduction to Python | Coding, paper |
| 2 | Introduction to PyTorch | Coding |
| 3 | Gradient descent, evaluation metrics | Pen and paper |
| 4 | Automatic differentiation, stochastic gradient descent | Coding, paper |
| 5 | Multi-layer perceptrons | Coding |
| 6 | Loss functions, advanced programming | Paper |
| 7 | Activation functions, parameter initialization | Coding, paper |
| 8 | Improving training with optimizers and regularization | Coding |
| 9 | Convolutional neural networks I | Paper |
| 10 | Convolutional neural networks II | Coding, paper |
| — | Christmas break | — |
| 11 | Recurrent neural networks | Coding, paper |
| 12 | Word embeddings | Paper |
| 13 | Transformers | Coding, paper |
| 14 | Pretrained models, autoencoders, GANs | — |
| 15 | Graph neural networks, interpretability, recap | — |

The full map with prerequisites is [[deep-learning-course-roadmap]].

## Lecture Index

Overview pages:
- [[introduction-to-deep-learning-lecture-1]] — Lecture 1: Introduction and Overview
- [[introduction-to-deep-learning-lecture-2]] — Lecture 2: Foundations of Machine Learning
- [[introduction-to-deep-learning-exercise-2]] — Exercise 2: Introduction to PyTorch
- [[introduction-to-deep-learning-exercise-1]] — Python on-ramp
- [[deep-learning-course-roadmap]] — the whole 15-week schedule

| # | Topic | Source | Status |
|---|-------|--------|--------|
| L1 | Introduction and overview: what is deep learning, its history, its open problems | `01_introduction_to_dl.pdf` | ingested → [[introduction-to-deep-learning-lecture-1]] |
| L2 | Foundations of machine learning: tasks, training and generalization, example methods, evaluation | `02_foundations_of_ml.pdf` | ingested → [[introduction-to-deep-learning-lecture-2]] |
| E1 | Python, environment management, Jupyter | `01-slides.pdf`, `01-homework.pdf`, notebooks | ingested → [[python-for-deep-learning]], [[python-environment-management]] |
| E1 | Python demo notebooks (linear algebra, notebook state) | `01-demo.ipynb`, `01-notebook-issue.ipynb` | ingested → [[linear-algebra-for-deep-learning]], [[jupyter-notebook-state]] |
| E1 | Official solution notebook (cross-check of the homework) | `01-hw-intro-py-solutions.ipynb` | used to correct the homework solution — see below |
| E2 | PyTorch: tensors, autograd, the training loop | `02-slides.pdf`, `02-demo.ipynb` | ingested → [[pytorch-tensors-and-autograd]], [[neural-network-training-loop]] |
| E2 | Paper homework: MML 2.4, derivatives, probability | `02-homework.pdf` | solved → `study/homework/introduction-to-deep-learning/exercise-02-solution.md` |
| E2 | Coding homework: polynomial regression | `02-hw-intro-pytorch-tasks.ipynb` | solved and **run** → [[polynomial-regression-and-overfitting]] |

## The Exam Is Now Specified

Lecture 1 settles what exercise 1 left open. The exam is:

- **Written, 90 minutes.**
- **No prerequisites** to participate — no exercise scores required. **No bonus.**
- Covers **everything covered in the course**: lectures *and* exercises.
- **May contain some coding.**
- Explicitly **includes the first and the last lecture** — so the history lecture and the
  explainability wrap-up are both in scope.
- A **resit** is offered before the start of the next semester.
- Dates for both exams will be announced; the date is not yet in the material.

The slides also carry two warnings that shape how to study: *"no intentional omissions, but
completeness of the slides is not guaranteed"* and *"the spoken word counts"* for exam content.
The slides are therefore not a complete record of the exam scope — these vault pages are the
substitute record.

Course logistics from lecture 1: lectures **Friday 10:15–11:45**, (WIWI) HS 8, 16.10.2026 –
05.02.2027. Exercises: Master students **Thursday 12:15–13:45 or 14:15–15:45** in (WIWI) SR 029;
Bachelor students **Tuesday 14:00–14:45**. Language English. There is **no lecture recording** —
the course is under development, recording raises the threshold for interaction, and speaking "off
the record" is wanted. Slides go online in Stud.IP.

**Assumed knowledge** (so the vault can point back at it): linear algebra (vectors, matrices,
matrix operations, matrices as functions), calculus (minima, maxima, derivatives, partial
derivatives and gradients), and statistics (data types, joint and conditional probability,
likelihood, distributions). The recommended reference is Deisenroth, Faisal and Ong, *Mathematics
for Machine Learning* — which is already in `raw/assets/` and which exercise 2's paper half draws
its matrix-product questions from.

## The official solution notebook

`01-hw-intro-py-solutions.ipynb` is the professor's own answers to the exercise-0 tasks, and it was
not in `raw/` at the time the homework was first written. It has now been used as a **cross-check**,
and it caught one real error: the task cell reads "compute 256²", and the solution states it in
words — *"compute 256 times 256"* → `65536`. An earlier version of the homework page had read the
cell as "2562" and offered two guesses; both were wrong. The correction is recorded in
`study/homework/introduction-to-deep-learning/exercise-01-solution.md`.

The rest of the official solutions agree with the independently written ones, including the details
that are easy to get wrong: `is_prime` uses a square-root bound, `count_letter("a", "ftest.txt")`
returns `[1, 1, 2, 2, 1]`, and `pay_options` returns the same 11 coin combinations. Where the
approaches differ, the official one is a recursive `pay_options` with a mutable default argument
(`list_of_used_coins=[]`) — a pattern that works only because the function copies the list before
appending.

## Exercise 1 — what it actually teaches

Not deep learning yet. It is a Python on-ramp with an opinionated toolchain:

- `uv` instead of `python.org` installers; one virtual environment per project
- VS Code + Ruff, format-on-save, Jupyter extension
- Notebooks as a blessing and a curse: state-keeping and inline plots, but they "easily lead to spaghetti code"

## Lecture 2 — what it adds

Lecture 2 is the classical machine-learning course that deep learning is built on, and it is the
first lecture whose content the exam can test directly as definitions and formulas rather than as
history:

- **The vocabulary**: instance, feature, label, model, parameter, hyperparameter, prediction, loss,
  with the notation D = {(x_i, y_i)}, x_i of dimension d, y_hat_i = f_w(x_i).
- **The four paradigms** by training feedback — unsupervised, supervised, self-supervised,
  reinforcement — with the unsupervised trio spelled out (clustering, dimensionality reduction,
  density estimation).
- **Training as empirical-risk minimisation**, with three named loss functions and gradient descent
  as the optimiser, and the explicit deferral of the details to the next lecture.
- **Generalisation**: underfitting, overfitting, model capacity, and the deep-learning exception
  **double descent** — the one place where the lecture says the classical picture is wrong.
- **Six classical methods** (k-NN, decision trees, SVMs, logistic regression, ensembles, gradient
  boosting) and the claim, with citations, that gradient-boosted trees still beat deep learning on
  tabular data.
- **Evaluation**: train/validation/test, k-fold cross-validation, information leakage, distribution
  shift, precision/recall/F1 under class imbalance, MAE and MSE.

Two things are worth flagging for revision. First, the lecture poses two quizzes and answers
neither on the slides — "Which task is it?" and "Where is the leak?" — so the answers had to be
worked out on the concept pages. Second, the lecture repeatedly defers detail to lecture 3
("log-likelihood, log-odds, cross-entropy", "details: next lecture"), which means the exam's
single-layer-networks material will assume this lecture's formulas are already known.

The 12 concept pages this lecture produced are listed on
[[introduction-to-deep-learning-lecture-2]].

## Open Questions

- The exam **date** is not in the material (the format and length are, as of lecture 1). The exam
  dates "will be announced as soon as possible".
- **The two schedules disagree, and lecture 2 resolves one point in favour of lecture 1's version.**
  Lecture 1's "Course Overview (tentative)" lists 15 dated sessions — Introduction, Foundations of
  Machine Learning ×2, Single-Layer Neural Networks ×2, Multi-Layer ×3, CNN ×2, RNN, Language
  Models, Transformers, Generative Models, Explainability & Wrap-up. The exercise-1 sheet listed a
  15-**week** plan with a different mapping (week 2 = Introduction to PyTorch, week 3 = Gradient
  descent, …). The second lecture deck is titled **"Foundations of Machine Learning"**, which is
  lecture 1's item 2, not the exercise sheet's week-2 "Introduction to PyTorch". So the lecture-side
  schedule is the one being followed; whether the exercise sheet's week numbers are simply offset
  by one is not stated.
- Whether the exam's "may contain some coding" means writing PyTorch from scratch or reading code
  is not specified. Exercise 2 is the only concrete coding evidence so far.
- Exercise 1's material said the course covers "the first (!) and last (!) lecture" for the exam
  before lecture 1 had even been read; that is now confirmed by the lecture slides themselves.
- PyTorch material is now in `raw/` (session 2), as is lecture 2's deck (`02_foundations_of_ml.pdf`).
  Lecture 3 and exercise session 3 onward are not.
