---
title: "Introduction to Deep Learning — Exercise 3: Evaluation Metrics and Gradient Descent"
tags: [topic, deep-learning, semester-2, exercise, evaluation, gradient-descent]
course: "Introduction to Deep Learning"
source_count: 3
status: current
last_updated: 2026-10-30
prerequisites: ["[[gradient-descent-for-neural-networks]]", "[[classification-metrics]]"]
---

## One-line Summary
The session the last one promised: gradient descent in detail, done by hand on paper, and the
evaluation metrics — MAE/MSE for regressors, precision/recall/F1 for binary classifiers, the
one-vs-rest expansion and macro-F1 for multi-class — computed on concrete tables.

## Core Map

```
Introduction to Deep Learning — Exercise 3 (29.10.2026, practice only, not graded)
│
├── Task 1 — Gradient descent, by hand
│   ├── 1(a) two steps on f(x,y) = 3xy − 5y² from (0,1), α = 0.1
│   │       surface has no minimum; descent accelerates towards −∞
│   ├── 1(b) one step on g(x,y) = xy² − x³e^(x−y) + sin²(xy) from (1,1), α = 1
│   │       descent direction is genuine, but α = 1 overshoots catastrophically
│   ├── 1(c) descent → ascent: flip the sign of the update
│   └── → [[gradient-descent-step-mechanics]] [[derivatives-cheat-sheet]]
│
├── Task 2 — Regressor evaluation
│   ├── MAE and MSE for two models on five points
│   └── which model is better depends on the metric — MSE punishes the outlier
│
├── Task 3 — Binary classifier evaluation
│   ├── 3(a) confusion matrix → precision, recall, F1, accuracy
│   └── 3(b) two label vectors → precision, recall, accuracy
│       └── → [[classification-metrics]]
│
├── Task 4 — Multi-class classifier evaluation
│   ├── one-vs-rest: collapse the C×C confusion matrix into C binary problems
│   ├── per-class precision/recall/F1, then macro-F1 = unweighted mean
│   └── 4(b) discuss whether the classifier is good — accuracy alone lies
│       └── → [[multiclass-evaluation-and-macro-averaging]]
│
└── Reference: derivatives_cheat_sheet.pdf — the course's one-page derivative table
    └── → [[derivatives-cheat-sheet]]
```

## Key Concepts at a Glance

| Page | What the exercise exercises |
|------|----------------------------|
| [[gradient-descent-step-mechanics]] | Read the gradient where you stand, scale by α, subtract — repeated by hand in 1(a) and 1(b). |
| [[gradient-descent-for-neural-networks]] | The update rule the whole sheet runs on; 1(c) shows ascent is the same rule with a sign flip. |
| [[derivatives-cheat-sheet]] | The course's own reference sheet for the differentiation rules 1(b) needs. |
| [[classification-metrics]] | Precision, recall, F1, accuracy — computed from confusion tables in tasks 3 and 4. |
| [[multiclass-evaluation-and-macro-averaging]] | One-vs-rest expansion and the macro average over per-class scores. |
| [[regression-evaluation-metrics]] | MAE and MSE, and why they disagree about which model is better. |
| [[roc-curve]] | The binary-evaluation picture from the ML for Cybersecurity course, same metric family. |

## Exercise Structure

**Task 1 — gradient descent.** 1(a) starts at (0, 1) and runs two steps with α = 0.1 on
`f(x, y) = 3xy − 5y²`, whose gradient is `(3y, 3x − 10y)`. Two steps take the iterate to
(−0.9, 4.09) and `f` from −5 to −94.7: the surface has no minimum and the descent accelerates
towards −∞. 1(b) is the derivative workout: one step with α = 1 on
`g(x, y) = xy² − x³e^(x−y) + sin²(xy)`, needing the product rule, the chain rule and
`sin·cos = sin(2·)/2` — the cheat sheet exists for exactly this. The step is a genuine descent
direction but lands absurdly far out (f drops by ≈ 11,885), which is the slides' own lesson: the
update rule guarantees a descent *direction*, not a good step. 1(c) is conceptual — flip the sign
of the update (`x ← x + α∇f`) and descent becomes ascent; equivalently, minimise −f.

**Task 2 — regressor evaluation.** MAE and MSE for two models over the same five points.
Model 1 is exact on three points but misses by 2 and 2 on the rest; Model 2 misses by 0.5
everywhere. MSE punishes the large misses, MAE does not — which model "wins" depends on the
metric, and the sheet asks you to say which and why.

**Task 3 — binary classifier evaluation.** 3(a) is a 2×2 confusion table (3/147/17/137) taken
through precision, recall, F1 and accuracy. 3(b) gives two length-11 label vectors and asks for
precision, recall and accuracy — counting true positives out of the raw vectors, no table given.

**Task 4 — multi-class.** A 3×3 confusion matrix, evaluated one-vs-rest: each class's metrics are
computed by merging the other two classes into one negative class, exactly as the worked example
in the sheet shows (`Recall_{y=0} = 3/(3+147+33) ≈ 0.016`). Then macro-F1 — the unweighted mean
of the per-class F1 scores — plus accuracy, and finally the discussion question: is this
classifier good? The per-class numbers are wildly asymmetric (one class is near-perfect, one is
near-useless), so accuracy alone gives a misleading answer.

The full worked solution, with every number produced and finite-difference-checked by
`exercise-03-numbers.py`, is in `study/homework/introduction-to-deep-learning/exercise-03-solution.md`.

## Exam-Relevant Points

1. **The update rule is three lines, and the sheet makes you execute them by hand.** Expect a
   "perform k steps of gradient descent" exam task: gradient, scale, subtract, repeat.
2. **Descent direction ≠ good step.** 1(b) is designed so that α = 1 is legal, direction-correct,
   and disastrous. The learning rate controls the step, not the direction.
3. **Ascent is descent with a sign flip** — there is no separate ascent algorithm.
4. **MAE vs MSE is a metric-choice question, not a computation question.** MSE squares errors, so
   the worst point dominates it; a model can win on one and lose on the other.
5. **One-vs-rest is the bridge from binary to multi-class.** The sheet states the merging rule
   explicitly, with a worked recall example — that rule is the examinable content of task 4.
6. **Macro-F1 is the unweighted mean of per-class F1s** — and 4(b) exists because a high accuracy
   can hide a class the classifier essentially never gets right.
7. **The cheat sheet is the course's own allowed toolbox** — the rules on it (product, chain,
   exponential, trig) are what 1(b) demands.

## Connections

- [[introduction-to-deep-learning-exercise-2]] — last week's session, which ended with the
  promise "next week: gradient descent in more detail". This is that week.
- [[introduction-to-deep-learning-lecture-2]] — the foundations-of-ML lecture that introduced
  the metrics this sheet computes.
- [[machine-learning-for-cybersecurity-lecture-3]] — the same metric family (precision, recall,
  F1, ROC) from the other course; the definitions agree.
- [[classification-metrics]], [[multiclass-evaluation-and-macro-averaging]],
  [[regression-evaluation-metrics]] — the concept pages behind tasks 2–4.
- [[gradient-descent-step-mechanics]], [[derivatives-cheat-sheet]] — the concept pages behind
  task 1.
- `study/homework/introduction-to-deep-learning/exercise-03-solution.md` — the worked solution,
  every number machine-verified.

## Open Questions

- The sheet is explicitly **not graded and for practice only** — whether its topics are still
  examinable is not stated here (the course-wide exam frame applies).
- 1(b) does not say whether the answer should be exact (symbolic) or decimal; the worked solution
  does both, with finite-difference verification.
- Task 2's "which model is better" has no single correct answer — the sheet expects the metric
  dependence to be argued, but states no preference.
- 4(b)'s "discuss" carries no rubric; the threshold for "good performance" is left to the student.
