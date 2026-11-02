---
title: "Introduction to Deep Learning — Exercise 3: Evaluation Metrics and Gradient Descent"
tags: [homework, deep-learning, semester-2, evaluation, gradient-descent]
course: "Introduction to Deep Learning"
source_count: 3
status: current
last_updated: 2026-10-29
prerequisites: ["[[classification-metrics]]", "[[gradient-descent-for-neural-networks]]"]
---

# Exercise 3 (29.10.2026) — Evaluation Metrics and Gradient Descent

Session slides: `03-slides.pdf` (36 pages). Homework: `03-homework.pdf`. Reference sheet:
`derivatives_cheat_sheet.pdf`. The sheet states: *"This exercise sheet will not be graded and is
provided for practice only."*

**Every number below is produced by `exercise-03-numbers.py`; the full run is
`output-exercise-03-numbers.txt`.** Nothing here is arithmetic done in the head. Each hand-derived
derivative in the script is checked against a central finite difference, so a wrong symbolic
derivative cannot pass silently — and that check did catch something (see *Two real findings*).

## 1. Gradient descent

### 1(a) Two steps on `f(x, y) = 3xy − 5y²` from `(0, 1)`, α = 0.1

```
∂f/∂x = 3y        ∂f/∂y = 3x − 10y
```

| Step | gradient | new (x, y) | f |
|---|---|---|---|
| start | — | (0, 1) | −5.000000 |
| 1 | (3.0000, −10.0000) | (−0.300000, 2.000000) | −21.800000 |
| 2 | (6.0000, −20.9000) | (−0.900000, 4.090000) | −94.683500 |

The gradient check passes at 1.4 × 10⁻¹⁰.

Two steps, and `f` has fallen from −5 to −94.7. Note the sign pattern: the first step moves *up*
in `y` because `∂f/∂y` is negative there, and the second step's `∂f/∂y` is even more negative
(−20.9) because `y` has grown. This is a surface with no minimum, and the descent is accelerating
towards −∞, not converging.

### 1(b) One step on `g(x, y) = xy² − x³e^(x−y) + sin²(xy)` from `(1, 1)`, α = 1

```
∂g/∂x = y² − (3x² + x³)·e^(x−y) + 2·sin(xy)·cos(xy)·y
∂g/∂y = 2xy + x³·e^(x−y) + 2·sin(xy)·cos(xy)·x
```

At `(1, 1)`: `e^(x−y) = 1`, `sin(xy)·cos(xy) = sin(1)cos(1) = sin(2)/2 = 0.4546487`.

```
∂g/∂x = 1 − (3 + 1) + 2·0.4546487·1 = −4 + 0.9092974 = −2.090703
∂g/∂y = 2 + 1     + 2·0.4546487·1 =  3 + 0.9092974 =  3.909297
```

Both checked against finite differences (rel. err 5.2 × 10⁻¹¹ and 1.3 × 10⁻¹¹).

One step: `(x, y) = (1 − (−2.090703), 1 − 3.909297) = (3.090703, −2.909297)`.

```
f(1, 1)          =   0.708073
f(3.0907, −2.9093) = −11884.398381
```

The value falls by 11,885. So the *direction* is a genuine descent — but α = 1 is enormous
relative to this function's curvature, and the step lands absurdly far from any minimum. The
lesson is the one the slides make with `f(x,y) = x²y + y²`: the update rule guarantees a descent
direction, not a good step.

### 1(c) Gradient descent into gradient ascent

Flip the sign of the update:

```
x ← x + α ∇f(x)
```

Equivalently, run descent on `−f`, because `∇(−f) = −∇f`. Everything else — the initialisation,
the stopping rule, the learning rate — is unchanged. There is no separate "ascent" algorithm.

## 2. Regressor evaluation — MAE and MSE for two models

| y | ŷ(1) | ŷ(2) |
|---|---|---|
| 5 | 5 | 4.5 |
| 7 | 7 | 7.5 |
| 9 | 9 | 10 |
| 3 | 2 | 2.5 |
| 10 | 12 | 11 |

| Model | errors | Σ\|e\| | Σe² | MAE | MSE |
|---|---|---|---|---|---|
| Model 1 | 0, 0, 0, −1, 2 | 3 | 5 | **0.6000** | **1.0000** |
| Model 2 | −0.5, 0.5, 1, −0.5, 1 | 3.5 | 2.75 | **0.7000** | **0.5500** |

**"Which model is better?" has no answer until the loss is chosen, and the two metrics disagree.**

- On **MAE**, Model 1 wins (0.6 against 0.7). It is exact on three of five points and its one bad
  miss — 2 units on the last point — is counted once.
- On **MSE**, Model 2 wins (0.55 against 1.00), because that single 2-unit miss contributes 4 to
  the sum of squares, while Model 2 spreads five small misses whose squares total 2.75.

This is the whole argument for choosing a loss deliberately: MSE punishes the outlier, MAE does
not. A model that is usually close and occasionally badly wrong looks worse under MSE; a model
that is uniformly mediocre looks better. The slides show a "fitting a model with MAE vs. MSE"
figure that illustrates the same trade-off without reaching a verdict on either.

## 3. Binary classifier evaluation

### 3(a) On the 2×2 matrix

```
              ŷ = 0   ŷ = 1
    y = 0       3      147
    y = 1      17      137
```

**The convention has to be stated, because the sheet does not state it.** The course's own
protocol is visible on the slides and in task 4: *"to compute the metrics for class y = 0, we
merge all other classes into a single negative class"*, so **class 0 is the positive class**, and
the slide's own example puts the positive class in the first row and the first column. Under that
convention `TP = 3`, `FN = 147`, `FP = 17`, `TN = 137`:

| | class 0 positive | class 1 positive |
|---|---|---|
| TP / FN / FP / TN | 3 / 147 / 17 / 137 | 137 / 17 / 147 / 3 |
| Precision | 0.150000 | 0.482394 |
| Recall | 0.020000 | 0.889610 |
| Accuracy | 0.460526 | 0.460526 |
| F1 | 0.035294 | 0.625571 |

Accuracy is the same either way; precision and recall swap roles. Both readings are given because
the sheet does not disambiguate, and the two give very different impressions of the same model.

Under the course convention (class 0 positive) this classifier is close to useless for finding
positives: recall 0.02 means it finds 3 of the 150 actual class-0 samples, and precision 0.15
means 85% of its class-0 predictions are wrong.

### 3(b) On two label lists

```
y  = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
ŷ  = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
```

Counting by hand is the trap here, so the script counts:

| positive class | TP | FN | FP | TN | Precision | Recall | Accuracy | F1 |
|---|---|---|---|---|---|---|---|---|
| class 0 | 2 | 3 | 3 | 3 | 0.4000 | 0.4000 | 0.4545 | 0.4000 |
| class 1 | 3 | 3 | 3 | 2 | 0.5000 | 0.5000 | 0.4545 | 0.5000 |

**The thing worth noticing: accuracy 0.4545 is worse than a constant predictor.** Class 1 is 6 of
the 11 samples, so a classifier that always answers "1" scores 6/11 = 0.5455 — nine points higher
than this one, while never finding a class-0 sample at all. Accuracy below the majority-class
baseline is the clearest possible statement that the model has no signal.

## 4. Multi-class classifier evaluation

### 4(a) Per-class metrics, macro-F1, accuracy

```
              ŷ = 0   ŷ = 1   ŷ = 2
    y = 0       7      129      46
    y = 1      25      766     170
    y = 2      73       73     204
```

Note the total: **1493**, not 1500. The slide's example happens to round to 1500; this one does
not, and the number is used as printed.

| class | TP | FN | FP | Precision | Recall | F1 |
|---|---|---|---|---|---|---|
| 0 | 7 | 175 | 98 | 0.066667 | 0.038462 | 0.048780 |
| 1 | 766 | 195 | 202 | 0.791322 | 0.797086 | 0.794194 |
| 2 | 204 | 146 | 216 | 0.485714 | 0.582857 | 0.529870 |

```
macro-F1 = (0.048780 + 0.794194 + 0.529870) / 3 = 0.457615
accuracy = (7 + 766 + 204) / 1493           = 0.654387
```

`macro-F1` is the mean of the per-class F1 values, so each class counts once regardless of size.
That is a choice, and it is the right one when class 0 matters as much as class 1.

### 4(b) Does the classifier have good performance?

**No, and the aggregate number is the reason this question exists.**

| | class 0 | class 1 | class 2 |
|---|---|---|---|
| actual count | 182 | 961 | 350 |
| predicted count | 105 | 968 | 420 |
| recall | 0.0385 | 0.7971 | 0.5829 |

Per-class recall spread is **0.7586**. Accuracy 0.654 is dominated by class 1, which is 64% of
the data and which the model handles well (recall 0.80). Class 0 is 12% of the data and the model
finds 3.8% of it — it is, for practical purposes, not detected at all.

The three statements that belong in any answer:

1. **Accuracy is a size-weighted average and hides the per-class result.** 0.654 is roughly what
   you get by predicting only the big class well.
2. **macro-F1 (0.4576) is the honest summary here**, because it counts the failure on class 0 as
   heavily as the success on class 1. The gap between 0.654 and 0.458 *is* the class-imbalance
   story.
3. **The model is not deployable as a three-class detector.** Which class is the interesting one
   decides everything: if class 2 matters, 0.583 recall is marginal; if class 0 matters, the
   model never fires.

## Two real findings from writing this up

Both are the kind of thing that would have gone into the notes as a silent error if the numbers
had been produced by hand.

**1. A stale-variable bug in the script, caught by the derivative check.** Section J (homework
task 1(b)) printed `grad = (6.000000, −20.900000)`. Those are *section I's* numbers — `gx` and
`gy` were still bound from the previous section's last update step, and section J reused the
names without rebinding them. The output was plausible, internally consistent, and wrong. What
caught it was the finite-difference check, which compares against a numerical derivative of the
function actually being differentiated. Rebounding `gx, gy` gives the correct
`(−2.090703, 3.909297)`. A plausible number is not a verified number.

**2. The slide's regression table has its row labels offset in the text layer.** Extracting slide
5 gives `54 1 1 1 / 79 2 4 / …`, which reads as ŷ=54, y=1. The pairs that reproduce the slide's
own printed `MAE = 93/5` are ŷ = (4, 7, 9, 3, 100) against y = (5, 9, 8, 2, 12): total absolute
error 93, total squared error 7751, giving MAE 18.6 and MSE 1550.2. The slide's `7744 + ε` in the
MSE numerator is 7744 for the last pair plus ε = 7 for the four small ones — which is the check
that confirms the pairing. Any answer built on the first reading is off by a lot.

## The derivative identities the homework leans on

Task 2 of the sheet asks for the sigmoid, tanh and linear-algebra derivatives by hand, and the
official solutions give them. They are on [[derivatives-cheat-sheet]] as a lookup table; the two
worth being able to reproduce:

```
σ(x) = 1/(1 + e^(−x))          σ'(x) = σ(x)·(1 − σ(x))
tanh(x) = (e^x − e^(−x))/(e^x + e^(−x))     tanh'(x) = 1 − tanh²(x)
```

The solutions' probability section also disposes of a trap: `p(x) = 3x² − e^x` on `2 ≤ x ≤ 4` is
**not** a valid density, because `p(4) < 0`. The fix is to pick an interval where the function is
positive — the solutions suggest `[1, 3]` — and then normalise.

## Connections

- [[gradient-descent-step-mechanics]] — the one-step mechanics this sheet's task 1 exercises.
- [[gradient-descent-for-neural-networks]] — why gradient descent is needed at all, from
  exercise 2.
- [[multiclass-evaluation-and-macro-averaging]] — one-vs-rest and macro averaging, with the
  slides' own 1500-sample worked example.
- [[classification-metrics]] — the definitions of precision, recall, accuracy and F1, and the
  imbalanced-data argument.
- [[regression-evaluation-metrics]] — MAE and MSE as loss choices.
- [[derivatives-cheat-sheet]] — the rules this sheet's task 2 applies.
- [[introduction-to-deep-learning-exercise-3]] — the session page.
- [[roc-curve]] — the threshold-sweeping view of the same confusion matrices.

## Open Questions

- **Which class is positive in task 3 is not stated.** The course's one-vs-rest convention from
  task 4 implies class 0, and the slide's own example puts the positive class in the first
  row/column, which agrees. Both readings are given rather than one being asserted.
- **The slides show an answer for the "Your Tasks" tables but no working.** The slide's MSE for
  the regression task is written `(7744 + ε)/5` with ε never defined; the four small terms sum to
  7, so ε = 7. The presentation is unexplained.
- **Nothing in exercise 3 says when to prefer MAE to MSE.** Task 2 asks "which model is better?"
  and the honest answer is that the metrics disagree; the slides show a "fitting a model with MAE
  vs. MSE" figure that does not reach a verdict.
- **The slides' macro-F1 is computed from values rounded to two decimals** (0.44), whereas
  averaging the exact per-class F1 values gives 0.439299. Both are on the slide; which one the
  course expects in an exam is not stated.
- **The gradient-descent tasks stop at one step.** No slide or sheet says what the convergence
  criterion should be, or how many steps are "enough", beyond "repeat until convergence or some
  limit".
