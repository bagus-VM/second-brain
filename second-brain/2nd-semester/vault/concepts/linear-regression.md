---
title: "Linear Regression"
tags: [concept, ml-security, semester-2, supervised-learning]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

Linear regression fits a straight line through feature space by minimising the sum of squared residuals, which has a closed-form solution — and that closed form is exactly why it cannot be a classifier.

## Core Intuition

The question linear regression answers is "what value should y have, given x?" That is a *regression* question: y is a continuous quantity — a price, a temperature, a number of packets. The model is the simplest useful one: a weighted sum of the features plus a bias, i.e. a hyperplane in feature space.

The second half of the lecture's point is the hand-off. For a classification task you need a categorical output, and a linear function produces **unbounded** values: it happily returns −400 or +4,000, neither of which can be a probability. So a linear model cannot be thresholded into a probability — you would have to clamp it, and clamping destroys calibration. That is the reason the next slide introduces the sigmoid.

The third thread is computational. The least-squares optimum has a beautiful closed form, w = (XᵀX)⁻¹XᵀY, but forming and inverting XᵀX is cubic in the number of features and quadratic-ish in the number of samples. For very large datasets an iterative method (gradient descent, `SGDRegressor`) is cheaper overall — it never materialises the inverse.

## Formal Definition / Statement

**Model.** Given a training set {(x₁, y₁), …, (xₙ, yₙ)} with xᵢ a d-dimensional feature vector, find a function y = f(x) that predicts y from x:

```
f(x) = b + w₁x₁ + w₂x₂ + … + w_d x_d
```

w₁ … w_d are the **weights**, b the **bias**; together they are the model parameters. With the constant x₀ = 1 and w₀ = b, the model collapses to the vector form **y = wᵀx**.

**Objective.** Least squares: minimise the sum of the squares of the residuals, where a residual is the difference between the observed value yᵢ and the predicted value f(xᵢ):

```
E(w) = Σᵢ₌₁ⁿ (yᵢ − wᵀxᵢ)²
```

**Matrix form.** With X the n×d matrix of training data, Y the n×1 vector of outputs, and w the vector of weights:

```
f(X) = X w
E(w) = (Y − Xw)ᵀ (Y − Xw)
```

**Derivation of the optimum.** Set the gradient to zero:

```
∂E(w)/∂w = −2 Xᵀ (Y − Xw) = 0
⇒ Xᵀ (Y − Xw) = 0
⇒ XᵀY = XᵀXw
⇒ w = (XᵀX)⁻¹ XᵀY
```

**Computational cost** (slide 27): XᵀX is a d×n matrix multiplied by an n×d matrix, and (XᵀX)⁻¹ is the inversion of a d×d matrix. Matrix inversion is O(d³). For very large datasets, iterative optimisation algorithms such as gradient descent can be more efficient; scikit-learn's `SGDRegressor` is the stochastic-gradient-descent implementation of the same least-squares objective.

## Key Properties

- **Linear in the parameters.** The model is linear in w (not necessarily in the features — with interaction terms the surface in feature space can be curved, but the fit stays linear in w). The normal equations have a single global optimum, not a local one.
- **The closed form is exact, not approximate.** There is no learning rate, no epoch count, no convergence criterion. This is the flip side of "no closed form" in [[logistic-regression]].
- **Squared error punishes outliers quadratically.** A single extreme target value moves the whole fitted line.
- **Closed form only exists when XᵀX is invertible** — i.e. when the features are not linearly dependent. With collinear or constant columns the system is singular and the pseudo-inverse (`scikit-learn`'s `LinearRegression`) is used instead.
- **The output is unbounded.** f(x) ∈ ℝ, so f(x) ≤ 1 and f(x) ≥ 0 cannot be guaranteed. This is the formal reason the same linear function cannot be thresholded into a probability: any threshold τ on an unbounded output produces a decision boundary, but the *value* of the output carries no probabilistic meaning, and there is no principled way to pick τ other than by rescaling.
- **Prediction is cheap.** Once w is known, f(x) is a dot product. That asymmetry — expensive fit, cheap prediction — is the opposite of KNN, and it is the reason the lecture's comparison table gives logistic regression a **Low** classification cost and KNN a **High** one.

## Worked Example

**The hand-off to logistic regression, in the lecture's own order.** The slides go: linear regression predicts a continuous value y; for classification we want a categorical output (spam yes/no); logistic regression passes the outcome of a linear function of the features through a logistic (sigmoid) function to obtain the probability of an occurrence, and maps that probability to a binary outcome. So the linear part is *not* discarded — it is reused, and the sigmoid is bolted onto the front of it to bound the output into (0, 1).

**The sigmoid in the vault's own pipeline.** The L2 credit-card model is a logistic regression — `LogisticRegression(max_iter=1000).fit(x_train, y_train)` — and it prints Accuracy 0.9989 / Precision 0.7869 / Recall 0.4898 / F1 0.6038 on 284,807 rows. The linear part of that model is exactly the f(x) = b + wᵀx above; the sigmoid makes it a probability; the 0.5 default threshold turns it into a label. See [[ml-pipeline-scikit-learn]] and [[classification-metrics]] for the numbers.

**Why the direct fit is not usable in the vault's setting.** In the credit-card data the target is binary. Fitting a linear regression to it produces values like −2.4 and 1.1, and the honest error metric (squared error) is not the metric anyone cares about; F1 is. That mismatch is the whole reason the next slide changes the cost function.

## Common Pitfalls

- **Thresholding a linear regression and calling it a classifier.** It gives a decision boundary, but the output is not a probability, so it cannot be calibrated, and the AUC computed from its raw scores is not the AUC of a probabilistic model.
- **Confusing "linear in the parameters" with "linear in the features".** Polynomial terms keep the fit linear in w while making the surface curved in x.
- **Ignoring the cost of the closed form on wide data.** (XᵀX)⁻¹ is O(d³) and, done naively, forms a dense d×d matrix; for high-dimensional data `SGDRegressor` or a least-squares solver on normal equations is preferable.
- **Fitting a regression where the target is a class label.** The error metric, the loss, and the decision rule are all mismatched; see [[logistic-regression]].
- **Reporting R² or RMSE on security data.** The credit-card set is 99.83% negatives; a squared-error regression on it will look mediocre for reasons that have nothing to do with the model.
- **Not scaling features before an iterative fit.** Poorly conditioned features make gradient descent converge slowly — see [[feature-normalization]].

## Connections

- [[logistic-regression]] — the same linear model with a sigmoid on top, and the cost function that makes it a classifier.
- [[ml-pipeline-scikit-learn]] — where the logistic-regression instantiation of this linear model appears in the L2 code.
- [[classification-metrics]] — the metrics that regression does not optimise, and why.
- [[k-nearest-neighbors]] — the other L3 model; opposite cost profile (cheap fit, expensive prediction).
- [[feature-normalization]] — scaling before an iterative least-squares fit.
- [[ml-learning-paradigms]] — supervised learning, loss function as the definition of the hypothesis space.
- [[ml-task-taxonomy]] — regression vs classification as the two task families.

## Open Questions

- The slides do not discuss the closed form's breakdown when XᵀX is singular (collinear or near-constant features), nor mention the pseudo-inverse.
- No actual regression example is worked through in the lecture — no data, no fitted line, no R². The entire section is derivation.
- Ridge or Lasso regularisation is never mentioned, although the comparison of closed form vs iterative optimisation invites the question of what happens with many features.
- The lecture does not state what "best model" means beyond least squares, and does not discuss alternatives to squared error (MAE, Huber) for outlier-heavy targets.
