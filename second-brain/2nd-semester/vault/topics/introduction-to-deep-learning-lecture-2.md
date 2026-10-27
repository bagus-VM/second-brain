---
title: "Introduction to Deep Learning — Lecture 2 Overview (Foundations of Machine Learning)"
tags: [topic, introduction-to-deep-learning, semester-2, machine-learning, evaluation]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[introduction-to-deep-learning-lecture-1]]"]
---

## One-line Summary
The classical machine-learning course the deep-learning course assumes you already had: what a task
is, what training actually minimises, why the model that fits the training data best is usually the
worst one, and how to measure a model without fooling yourself.

## Core Map

```
Lecture 2 — Foundations of machine learning (44 slides)
│
├── 2.1 Tasks and terminology                          (slides 3-14)
│   ├── ML = statistical algorithms that learn from data and generalize
│   ├── running example: bot detection, 15 labelled registrations, 5 features
│   ├── row = instance, column = feature, i.i.d. assumption
│   │       -> [[ml-data-and-iid-assumption]]
│   ├── four learning paradigms by training feedback:
│   │       unsupervised / supervised / self-supervised / reinforcement
│   │       -> [[ml-learning-paradigms]], [[ml-task-taxonomy]]
│   ├── unsupervised trio: clustering, dimensionality reduction, density estimation
│   │       -> [[clustering-and-dimensionality-reduction]]
│   ├── supervised outputs: classification (binary/multiclass/multi-label),
│   │       regression, structured prediction
│   └── hard vs soft output, calibrated probabilities
│           -> [[soft-classification-and-calibration]]
│
├── 2.2 Training and generalization                    (slides 16-23)
│   ├── learning vs inference; parameters vs hyperparameters
│   ├── training = minimising empirical risk
│   │       L(w) = (1/n) Σ ℓ(f_w(x_i), y_i)
│   │       0-1 loss (not differentiable), squared error, negative log-likelihood
│   │       w <- w - η ∇L(w)
│   │       -> [[loss-functions-and-empirical-risk]]
│   ├── scoring example: parameters are points per feature,
│   │       what may be scored is a hyperparameter
│   ├── underfitting / good fit / overfitting
│   │       -> [[polynomial-regression-and-overfitting]]
│   └── model capacity, and the deep-learning exception: double descent
│           -> [[double-descent]]
│
├── 2.3 Example methods                                (slides 25-32)
│   ├── k-NN: distance + k + majority vote -> [[k-nearest-neighbors]]
│   ├── decision trees: greedy top-down, inner node = attribute
│   │       -> [[decision-trees]]
│   ├── SVM: maximum margin, support vectors, kernels, soft margin
│   │       -> [[support-vector-machines]]
│   ├── logistic regression: sigmoid of a linear model = one neuron
│   │       -> [[logistic-regression]]
│   ├── ensembles: bagging/random forest, boosting/AdaBoost,
│   │       gradient boosting (XGBoost, LightGBM, CatBoost)
│   │       -> [[ensemble-learning]]
│   └── the punchline: gradient-boosted trees still beat deep learning
│           on tabular data
│
└── 2.4 Evaluation                                     (slides 34-43)
    ├── train / validation / test, and why three and not two
    │       -> [[cross-validation]]
    ├── k-fold cross-validation, leave-one-out
    ├── information leakage: normalise after the split, never before
    │       -> [[information-leakage]]
    ├── leakage in the LLM age: test-set contamination, GSM8k vs GSM1k
    ├── i.i.d. violated: temporal shift, covariate shift, grouped instances
    │       -> [[ml-data-and-iid-assumption]]
    ├── accuracy / precision / recall / F1, and class imbalance
    │       -> [[classification-metrics]], [[class-imbalance]]
    └── MAE, MSE for regression
            -> [[regression-evaluation-metrics]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[ml-data-and-iid-assumption]] | Rows are instances, columns are features, and every guarantee in this lecture rests on the rows being independent and identically distributed |
| [[soft-classification-and-calibration]] | A hard label throws away the confidence; a probability keeps it, but only if 80 % really means 80 % |
| [[loss-functions-and-empirical-risk]] | Training is minimising the average loss on the training set, and the loss you pick decides what the model optimises for |
| [[double-descent]] | Past the interpolation threshold, bigger models get better again — the classical bias-variance story stops predicting |
| [[decision-trees]] | Ask one attribute at a time, greedily, and let the leaves carry the labels |
| [[support-vector-machines]] | Of all the separating hyperplanes, take the one with the widest margin; kernels buy non-linearity |
| [[ensemble-learning]] | Many weak, differently-wrong models combine into one better one — bagging by variance, boosting by bias |
| [[cross-validation]] | With little data, rotate which fold is held out and average, instead of trusting one lucky split |
| [[information-leakage]] | Any information from the test set that reaches training inflates the score and destroys the estimate |
| [[class-imbalance]] | With 1 % positives, 99 % accuracy is what a classifier that always says "no" achieves |
| [[regression-evaluation-metrics]] | MAE for "how wrong on average", MSE for "how wrong, with big errors punished" |

## Lecture Structure

| Slides | Section | What happens |
|--------|---------|--------------|
| 1-2 | Title, agenda | 2.1 tasks and terminology, 2.2 training and generalization, 2.3 example methods, 2.4 evaluation |
| 4-8 | Definition, running example, notation | Bot detection table; instance/feature; the formal notation D = {(x_i, y_i)} |
| 8-14 | Task taxonomy | Four paradigms by feedback; the unsupervised trio; supervised output types; hard vs soft |
| 13, 38, 546 | Two quizzes | "Which task is it?" (6 cases) and "Where is the leak?" (5 cases) — both left unanswered on the slides |
| 16-21 | Training | Learning vs inference, parameters vs hyperparameters, the scoring example, loss functions, gradient descent |
| 22-23 | Generalization | Underfitting/overfitting; model capacity; double descent and the interpolation threshold |
| 25-32 | Six methods | k-NN, decision trees, SVM, logistic regression, ensembles, gradient boosting |
| 34-43 | Evaluation | Train/test, train/validation/test, k-fold, leakage, distribution shift, measures, imbalance, MAE/MSE |
| 44 | Summary and outlook | Take-home messages; next lecture is single-layer networks |

## Exam-Relevant Points

- **The definitions are the exam's raw material.** Instance, feature, label, model, prediction, loss,
  parameter, hyperparameter — the lecture defines all of them explicitly with notation. Lecture 1
  said the exam covers everything in the course and may contain coding; the definitions are the
  cheap marks.
- **Training = empirical risk minimisation** with the explicit formula
  L(w) = (1/n) Σ ℓ(f_w(x_i), y_i) and the update w ← w − η∇L(w). The lecture says "details: next
  lecture", so expect the formula here and the derivation later.
- **Three loss functions by name**: 0-1 (not differentiable — the lecture says so), squared error,
  negative log-likelihood leading to cross-entropy.
- **Double descent is the lecture's one deliberate departure from the classical story**, with two
  citations (Belkin et al., PNAS 2019; Nakkiran et al., ICLR 2020). It is named on a slide, so it is
  fair game.
- **The leakage quiz is the most likely exam question in 2.4.** All five cases are classic:
  feature selection before the split, per-patient leakage, a feature that is a consequence of the
  target, hyperparameter selection on the test set, and the one case that is *correct*.
- **The three-split rule and k-fold** are both stated, with the reason for each.
- **Precision, recall, F1, accuracy** are given as formulas, plus the worked imbalance example
  (10,000 registrations, 100 bots, 99.4 % accuracy, 0.67 precision, 0.8 recall, F1 0.73).
- **MAE and MSE** are given as formulas.
- **The claim that gradient-boosted trees beat deep learning on tabular data** is stated with a
  citation (Grinsztajn et al., NeurIPS 2022) and a counterpoint (TabPFN, Nature 2025). Quotable.

## Connections

- **Prerequisite:** [[introduction-to-deep-learning-lecture-1]] — the overview and history lecture.
  Lecture 1's "assumed knowledge" list (linear algebra, calculus, statistics) is exactly what this
  lecture draws on.
- **Next lecture:** single-layer neural networks — linear regression, gradient descent, SGD and
  mini-batches, the perceptron, logistic regression with cross-entropy, computation graphs. This
  lecture's loss and gradient-descent formulas are the setup for it.
- **[[machine-learning-for-cybersecurity-lecture-3]]** covers the same evaluation material
  (metrics, ROC, k-NN, regression) from the security side; the overlap is large and deliberate, so
  one reading serves both courses.
- **Exercise 2** (`02-homework.pdf`) is the paper half of this lecture's material: MML 2.4, matrix
  products, derivatives, probability. Solved in
  `study/homework/introduction-to-deep-learning/exercise-02-solution.md`.
- **Exercise 2's coding half** (polynomial regression) is the practical demonstration of the
  overfitting section — degrees 1/2/3/9 compared by measured train and validation loss.
- **The course's own roadmap** ([[deep-learning-course-roadmap]]) places this lecture as week 3
  ("gradient descent, evaluation metrics"), which matches the content even though lecture 1's
  tentative schedule numbered it differently.

## Open Questions

- **Both quizzes have no answers in the deck.** "Which task is it?" (slide 13) and "Where is the
  leak?" (slide 38) are posed and abandoned. They are answered on this vault's pages where the
  material determines the answer, and left open where it does not (see
  [[information-leakage]] for the fifth leak case, which is the *correct* procedure).
- **"Later on: log-likelihood, log-odds, cross-entropy"** — all three are promised here and deferred.
  Only negative log-likelihood is named in 2.2.
- **No numbers are given for the capacity/error curves.** The double-descent figure is labelled
  "schematic curves" and the interpolation threshold is marked but not defined quantitatively.
- **The lecture does not say how to choose k in k-fold** beyond "often k = 10", nor how to trade the
  runtime cost against the estimate's quality.
- **No guidance on what to do about distribution shift**, only that one should split by time or
  group and monitor after deployment. Which drift-detection method to use is not covered.
- **The tabular-vs-deep-learning claim is asserted with citations but no data** from the lecture
  itself; the reader is expected to take the papers' word.
