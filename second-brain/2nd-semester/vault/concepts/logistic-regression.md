---
title: "Logistic Regression"
tags: [concept, ml-security, semester-2, classification]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

Logistic regression takes a linear function of the features, squashes it through a sigmoid into a probability, and fits it by minimising log loss with an iterative optimiser instead of a closed-form solution.

## Core Intuition

Linear regression gives you a number that is not a probability. Logistic regression keeps the linear part and inserts the sigmoid between the score and the output: the linear function decides *which way* the score moves, the sigmoid decides *how much* of that movement becomes probability, and the decision threshold decides what probability counts as "attack".

Two consequences follow. First, the model is now non-linear in the input — the sigmoid bends the score, so the decision boundary in feature space is a hyperplane but the probability surface is curved. Second, and this is the point the lecture makes, squared error no longer works as the cost: the composed model is non-linear, so the squared-error cost has **multiple local minima** and is hard to optimise. The fix is a cost function that matches the probabilistic framing — log loss.

The third consequence is that there is no closed-form optimum any more. The normal equations that solve least squares have no logistic analogue, so the fit is done by iterative optimisation (gradient descent; `scikit-learn`'s `LogisticRegression`).

## Formal Definition / Statement

**The sigmoid.**

```
f(x) = 1 / (1 + e^(−x))
```

It maps ℝ into (0, 1): negative inputs map below 0.5, positive inputs above, and the output is a probability of occurrence.

**The model.** Pass the outcome of a linear function of the features through the logistic function to calculate the probability of an occurrence, then map the probability to a binary outcome:

```
p = σ(wᵀx + b)          # probability
ŷ = 1 if p ≥ 0.5 else 0  # binary decision
```

**Cost function — Log Loss** (slide 30):

```
Log Loss = −(1/n) Σᵢ₌₁ⁿ [ yᵢ log(ŷᵢ) + (1 − yᵢ) log(1 − ŷᵢ) ]
```

with yᵢ the true value (0 or 1) and ŷᵢ the predicted value.

**Why not squared error.** The sigmoid introduces non-linearity into the model, and as a result the squared-error cost function used for linear regression is not suitable: it will have multiple local minima and is difficult to optimise. Log loss is the negative log-likelihood of the Bernoulli outcome under the model, and it penalises confident mistakes without bound — ŷ = 0.001 when y = 1 gives a large loss — which is precisely the behaviour a probability model needs.

**No closed form.** There is no closed-form solution for the optimum, but several iterative optimisation algorithms can be used (e.g. gradient descent). The lecture points at `scikit-learn`'s `LogisticRegression` documentation.

**Comparison table row** (slide 31, verbatim):

| Algorithm | Computational Effort (Training) | Computational Effort (Classification) | Dynamic Model Update |
|-----------|----------------------------------|------------------------------------------|----------------------|
| Logistic Regression | Moderate | Low | Complex (Online Learning) |

## Key Properties

- **It is a linear model with a probabilistic output.** The decision boundary is still linear in the features; only the probability is curved. This is what makes it interpretable: the coefficient of feature i is the change in log-odds per unit of that feature.
- **The training cost is moderate, the classification cost is low.** One fit, then a dot product plus a sigmoid per sample. The dynamic-model-update column is "Complex (Online Learning)" — the weights can be updated as new data arrives, but not as trivially as in Naive Bayes or KNN, whose "model" is just the data.
- **Log loss is convex in the parameters** (unlike the squared error on a sigmoid output), so gradient descent finds the global optimum. The lecture's complaint about local minima is about the *squared-error* cost, not about log loss.
- **The default threshold of 0.5 is an assumption, not a derivation.** The lecture never justifies it; [[roc-curve]] shows what happens when the threshold is swept instead.
- **It emits a continuous probability, so its ROC is a proper staircase** — the opposite of KNN's three discrete points.
- **Probability ≠ separability.** A well-calibrated probability still says nothing about whether the classes overlap enough for any threshold to work; on the credit-card data the model is calibrated and still useless (recall 0.49).

## Worked Example

**The credit-card fraud model, which is exactly this algorithm.** The L2 pipeline fits `LogisticRegression(max_iter=1000)` on 284,807 rows of the credit-card dataset with a 20% holdout, and the printed metrics are:

```
Accuracy  = 0.9989
Precision = 0.7869
Recall    = 0.4898
F1 Score  = 0.6038
```

Read this as the sigmoid pipeline: the linear score wᵀx is squashed into a probability, the 0.5 threshold produces labels, and the confusion matrix behind those four numbers is TN 56,851 / FP 13 / FN 50 / TP 48. The important detail is that a probabilistic classifier like this one produces a proper step-function ROC — the kind the L3 lecture uses to contrast with KNN's three-point curve. The metrics themselves are analysed in [[classification-metrics]] and the code in [[ml-pipeline-scikit-learn]]; the point here is the *model family*.

**Why `max_iter=1000`.** Unscaled features with a 0.17% positive rate make the loss surface badly conditioned; the optimiser needs many iterations to converge, and scikit-learn only warns when it does not. Scaling `Amount` (see [[feature-normalization]]) is the other half of that fix.

**Threshold choice in practice.** Because the model emits a probability, the 0.5 cut is a free parameter. Lowering it raises recall and lowers precision; the L2 run's operating point (P 0.79 / R 0.49) is one of many. This is exactly the freedom the ROC curve exists to organise.

## Common Pitfalls

- **Using squared error on a sigmoid output.** The lecture's explicit point: it introduces multiple local minima and is hard to optimise. Use log loss.
- **Looking for a closed-form solution.** There isn't one; iterative optimisation is not a workaround but the standard path.
- **Reporting the 0.5 threshold as if it were optimal.** It is the scikit-learn default, and on security data the cost of a false negative is rarely equal to the cost of a false alarm.
- **Ignoring class imbalance.** 98 positives in the test split is what produces recall 0.49; the model is not broken, the prior is.
- **Not scaling features.** See [[feature-normalization]].
- **Reading accuracy on the credit-card model.** A constant "no fraud" predictor scores 99.81%; the trained model is only 0.08 points better.
- **Confusing "linear" with "not powerful".** Logistic regression captures a linear decision boundary; it cannot represent interactions without engineered features.

## Connections

- [[linear-regression]] — the linear function this model wraps; the source of the closed form and of the squared-error cost that fails here.
- [[ml-pipeline-scikit-learn]] — the credit-card walkthrough in which this model is fitted and scored.
- [[classification-metrics]] — accuracy/precision/recall/F1 for the credit-card model: 0.9989 / 0.7869 / 0.4898 / 0.6038.
- [[roc-curve]] — the probability-producing classifier whose ROC is a step function, in contrast to KNN.
- [[k-nearest-neighbors]] — the other L3 model, and the third row of the comparison table.
- [[naive-bayes-text-classification]] — the other probability-emitting classifier, and the table row the lecture warns about.
- [[feature-normalization]] — the preprocessing this model needs.
- [[ml-learning-paradigms]] — supervised learning, and the fact that this model is *not* an online learner by default.

## Open Questions

- The lecture does not derive the gradient of log loss or the update rule; the derivation stops at "use gradient descent".
- The "Dynamic Model Update: Complex (Online Learning)" cell is not explained — no online variant of logistic regression is introduced, even though the comparison table is precisely where that question arises.
- No penalty/regularisation discussion (L1, L2, `C`) appears, although the credit-card set has 30 features and only 492 positives.
- The lecture never explains how log loss relates to the accuracy/precision/recall metrics it taught in part 1 — the loss optimised and the metrics reported are different objectives.
- Whether a one-vs-rest extension to the five intrusion classes (normal, Probe, DoS, U2R, R2L) is intended is not stated.
