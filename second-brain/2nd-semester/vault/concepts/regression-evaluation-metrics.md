---
title: "Regression Evaluation Metrics"
tags: [concept, introduction-to-deep-learning, semester-2, evaluation, machine-learning]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[loss-functions-and-empirical-risk]]"]
---

## One-line Summary
MAE reports the average size of the error and MSE squares it before averaging, so MSE treats one
large error as worse than several small ones of the same total size — which is a choice about what
"wrong" means, not just a formula.

## Core Intuition

The error of a single prediction is a signed quantity, and averaging it would let a model that is
equally far too high and too low score zero. Both measures fix that, in different ways: MAE takes the
absolute value, MSE squares it. The choice is not cosmetic.

Squaring is the reason MSE is the default companion of least-squares fitting — it is differentiable
everywhere, it is the same quantity training minimises, and it is the sample analogue of variance.
It is also the reason MSE is dominated by outliers: an error of 10 contributes 100 to the sum, which
is as much as a hundred errors of 1. MAE, using the absolute value, weighs every unit of error
equally and therefore reports something closer to the typical error.

So the two metrics answer related but different questions. MAE asks "how far off is the model on a
typical prediction?"; MSE asks "how far off is it, with big misses counting disproportionately?" If
the application's pain is proportional to the size of the error, MSE is the honest one; if one
catastrophic prediction would be unacceptable regardless of the average, neither average is enough
and you need the error distribution.

## Formal Definition / Statement

**Slide 43, as given.** Error of instance `i`:

```
e_i = y_i - y_hat_i
```

Mean absolute error:

```
MAE(y, y_hat) = (1/n) * Σ |e_i| = (1/n) * Σ |y_i - y_hat_i|
```

Mean squared error:

```
MSE(y, y_hat) = (1/n) * Σ e_i^2 = (1/n) * Σ (y_i - y_hat_i)^2
```

The slide gives these two and no others. Both are averages over instances, so both are independent of
dataset size and in the units of the target (MAE) or its square (MSE).

## Key Properties

- **MAE is in the units of the target; MSE is in squared units.** An MAE of 1.6 on a price in euros
  means 1.6 euros; the MSE from the same predictions is 4.00 euros-squared, which is why RMSE exists as
  a rescaling — and the slide does not give it.
- **MSE is differentiable everywhere; MAE is not differentiable at zero.** That is one reason squared
  error is the training loss of choice for regression, and it is the metric's hidden link to
  [[loss-functions-and-empirical-risk]].
- **MSE punishes outliers quadratically.** Its value is dominated by the largest errors.
- **MAE weighs every unit of error equally** and therefore reports a typical error rather than a
  worst-case-sensitive average.
- **They can rank two models in opposite orders.** Demonstrated below with real numbers — this is the
  property that makes "which metric?" a real decision.
- **Both are means, so both hide the distribution.** With six predictions of error 5 and one of 30, the
  mean is respectable and the 30 is invisible.
- **Signs are discarded, not balanced.** Neither metric can tell systematic bias (predictions all too
  low) from noise.
- **They are not the same as the training loss by construction**, but MSE *is* squared error averaged,
  so when the model was trained on MSE the reported MSE is the same functional form on a different
  dataset — which is the train/validation distinction of the same lecture.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 9.

Ten instances with true value 10 throughout, and two models:

| Model | Predictions | Errors | MAE | MSE |
|-------|-------------|--------|-----|-----|
| A | 9 on all ten | −1 (×10) | **1.0000** | **1.0000** |
| B | 10 five times, 11.5 five times | 0 (×5), +1.5 (×5) | **0.7500** | **1.1250** |

**The two metrics disagree.** MAE prefers B (0.7500 < 1.0000); MSE prefers A (1.0000 < 1.1250).

Both verdicts follow from the definitions rather than from any subtlety:

- **MAE** = (5 × 0 + 5 × 1.5) / 10 = 7.5/10 = 0.7500 for B, against (10 × 1)/10 = 1.0000 for A. B has
  five *perfect* predictions, and MAE pays for them.
- **MSE** = (5 × 0² + 5 × 1.5²) / 10 = 11.25/10 = 1.1250 for B, against (10 × 1²)/10 = 1.0000 for A.
  B's 1.5-unit errors are squared to 2.25 each, which is more than A's ten 1-unit errors cost.

**Which model is better?** It depends on whether five perfect predictions compensate for five that are
50 % further off than A's — and that is a question about the application, not about the arithmetic. A
model whose errors are all exactly 1 is also a model with a *known* error bound, which matters if the
downstream decision is sensitive to a single bad case.

## Common Pitfalls

- **Reporting MSE as if it were in target units.** An MSE of 4 on prices in euros is not "4 euros off";
  the slide gives no RMSE, so the rescaling is the reader's problem.
- **Using MAE and MSE interchangeably.** The worked example is a two-model case where they disagree
  completely.
- **Assuming MSE is always worse under outliers.** It is *more sensitive* to outliers, which is a
  disadvantage if outliers are noise and an advantage if large errors are exactly what you care about.
- **Optimising MAE by gradient descent without noticing the kink at zero.** The absolute value is not
  differentiable at 0; the slide's training loss list is squared error, not absolute error.
- **Reading a good average as a guarantee.** Both are means; neither bounds the worst-case error.
- **Ignoring sign.** A model that overshoots everything is reported as if it were unbiased.
- **Comparing metrics across datasets or scales.** Both are in target units, so a lower MAE on a
  100-km target does not compare with a higher one on a 100-mm target.
- **Forgetting that the same error summary must be used for training and for the reported result to be
  comparable** — training loss is a different sample, not a different function.

## Connections

- [[loss-functions-and-empirical-risk]] — squared error as a training loss, alongside negative
  log-likelihood; this page is the evaluation side of the same quantity.
- [[linear-regression]] — the model whose loss and whose reported metric coincide.
- [[polynomial-regression-and-overfitting]] — the exercise that compares degrees by measured train and
  validation loss, which are these two quantities under another name.
- [[classification-metrics]] — the classification analogue, where accuracy, precision and recall replace
  MAE and MSE.
- [[class-imbalance]] — the classification version of "the metric can hide the model", and the reason
  the lecture splits evaluation into two pages.
- [[cross-validation]] — how an MAE or MSE estimate stops depending on one split.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **Only MAE and MSE are given.** No RMSE, no R-squared, no MAPE, no median absolute error — all of
  which change the outlier story.
- **No guidance on which to prefer.** The slide lists both without a recommendation or a criterion.
- **No worked example on the slide.** The disagreement case above is this vault's own construction.
- **The connection between the training loss and the reported metric is not made explicit.** MSE is
  exactly the empirical risk under squared error, but the lecture presents the loss list and the metric
  list as separate slides (19 and 43) without linking them.
- **No confidence interval or significance statement** accompanies either metric, so a difference
  between two reported values is not testable from the material alone.