---
title: "Binary Cross-Entropy Loss"
tags: [concept, introduction-to-deep-learning, semester-2, loss-functions]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-11-07
prerequisites: ["[[activation-functions]]", "maximum likelihood (log-likelihood of a Bernoulli)"]
---

## One-line Summary

Binary cross-entropy is the negative log-likelihood of a Bernoulli model — L = −y log ŷ − (1−y)
log(1−ŷ) — and it is the right loss for a sigmoid output because its gradient never vanishes on
confidently wrong predictions and because it is convex in the weights.

## Core Intuition

The lecture arrives at BCE by a *principled* route, in explicit contrast to the perceptron's
correction rule: if the model outputs a probability, the natural thing to maximise is the
likelihood of the observed labels, and the natural thing to do with a product of probabilities is
take its logarithm. BCE is not designed as a "penalty that looks right"; it is derived.

The second intuition is what the log does to wrong answers. L = −log ŷ is roughly the number of
nats of surprise: predicting 0.99 for a label of 1 costs 0.01, predicting 0.5 costs 0.69, and
predicting 0.001 costs 6.9. "Confident wrong predictions are punished heavily" — that is the
property squared error lacks, and the reason a sigmoid trained with MSE stalls.

## Formal Definition / Statement

**The model.** Logistic regression: ŷ = f_w(x) = σ(wᵀx) = P(y = 1 | x), with labels y ∈ {0, 1}
and output "a probability (soft classification)". Decision rule: predict class 1 if
ŷ ≥ 0.5 ⇔ wᵀx ≥ 0.

**Maximum likelihood.** "If we interpret predictions as probabilities, how should we choose the
weights? Such that the overall likelihood of all predictions coming true gets maximised":

ŵ = argmax_w ∏ᵢ p_model(yᵢ | xᵢ, w)
  ⇔ ŵ = argmax_w Σᵢ log p_model(yᵢ | xᵢ, w)

with the per-instance likelihood written compactly as "p_model(y | x, w) = ŷ^y (1 − ŷ)^(1−y)",
which expands to "ŷ if y = 1, 1 − ŷ if y = 0".

**The loss.** Substituting and negating the maximisation:

ŵ_ML = argmin_w Σᵢ [ −yᵢ log ŷᵢ − (1 − yᵢ) log(1 − ŷᵢ) ]

and the bracket is the loss:

L(ŷᵢ, yᵢ) = −yᵢ log ŷᵢ − (1 − yᵢ) log(1 − ŷᵢ)

which splits into "−log ŷᵢ if yᵢ = 1" and "−log(1 − ŷᵢ) if yᵢ = 0". "In ML, we use the more general
term 'loss function' rather than 'error function'. Interpretation: we minimize the dissimilarity
between the empirical data distribution p_data (defined by the training set) and the model
distribution p_model."

**The gradient**, by the chain rule with z = wᵀx, ŷ = σ(z), σ′(z) = ŷ(1 − ŷ):
∂L/∂ŷ = −y/ŷ + (1−y)/(1−ŷ) = (ŷ − y)/(ŷ(1−ŷ)); ∂ŷ/∂z = ŷ(1−ŷ); ∂z/∂w = x — so

∇_w L(ŷᵢ, yᵢ) = (ŷᵢ − yᵢ)·xᵢ

"Same form as for linear regression (up to the factor 2) – only ŷ differs!"

**No closed form.** "In contrast to linear regression, the loss L(ŷᵢ, yᵢ) is not quadratic in w. No
closed-form solution: we must apply iterative gradient-based optimization."

## Key Properties

**Why not squared error — the argument is a vanishing gradient, and the slides draw it.**
"With a sigmoid output, the squared error has vanishing gradients for confident wrong predictions
(z ≪ 0 for y = 1) → learning gets stuck." The comparison plot shows MSE's gradient magnitude going
to zero exactly where the prediction is most wrong, while "BCE: gradient ŷ − y stays large as long
as the prediction is wrong; BCE is convex in w, MSE with sigmoid is not."

Note the two separate claims there, and they are worth keeping apart: the *gradient* argument
(learning dynamics) and the *convexity* argument (optimisation landscape). Either alone would
justify BCE; together they make it the standard choice.

**The loss is minimised exactly at ŷ = y.** "For yᵢ = 1 the loss L is minimized if ŷᵢ = 1; for
yᵢ = 0 the loss L is minimized if ŷᵢ = 0; thus, L is minimal if ŷᵢ = yᵢ."

**The gradient against z is bounded, which is the point.** Since ∂L/∂z = ŷ − y ∈ (−1, 1), no single
example can dominate an update, and a confidently wrong example produces a gradient near ±1 rather
than near 0.

**Numerically the log must be clamped.** ŷ ∈ (0, 1) from the sigmoid, so log ŷ and log(1 − ŷ) are
finite in exact arithmetic, but float32 saturates σ to exactly 0 or 1 for |z| ≳ 17 and then
−log 0 = ∞. The slides do not mention this; implementations use log-sum-exp or ε-clamping.

**BCE extends to more than two classes** — "can be extended to > 2 classes (later in the lecture)",
i.e. categorical cross-entropy with softmax.

## Worked Example

**Four predictions for the same label y = 1**, computed from L = −log ŷ:

| ŷ | L | reading |
|---|---|---|
| 0.999 | 0.0010 | nearly free |
| 0.9 | 0.1054 | cheap |
| 0.5 | 0.6931 | one nat — a coin flip |
| 0.1 | 2.3026 | expensive |
| 0.001 | 6.9078 | ten times the cost of the coin flip per unit of certainty |

The gradient with respect to z = wᵀx is ŷ − y:

| ŷ | ŷ − 1 | note |
|---|---|---|
| 0.999 | −0.001 | almost no correction needed |
| 0.5 | −0.500 | moderate push |
| 0.1 | −0.900 | strong push |
| 0.001 | −0.999 | maximal push |

Compare the squared-error alternative with the same sigmoid: L = (ŷ − y)² gives 0.998 at ŷ = 0.001
— *larger* than at ŷ = 0.5 (0.25) — while its gradient through the sigmoid is
2(ŷ − y)·ŷ(1 − ŷ) ≈ 2·(−0.999)·0.001 ≈ −0.002, i.e. essentially zero. The wrong answer produces
almost no learning signal. That is precisely the failure the slide plots.

## Common Pitfalls

- **Using MSE with a sigmoid output.** It is neither convex in w here nor informative when the
  prediction is confidently wrong.
- **Forgetting the second term.** For y = 0 the loss is −log(1 − ŷ), not −log ŷ; a single-term
  implementation trains the class-1 examples and silently ignores the rest.
- **Numerical overflow at σ = 0 or 1** — needs clamping or a fused log-sigmoid.
- **Reading the loss as an accuracy.** It measures calibration-like dissimilarity; a model can have
  low BCE and mediocre accuracy (and vice versa).
- **Confusing BCE with the perceptron's error count.** One is a differentiable surrogate, the other
  a discrete misclassification count; gradient descent is only available for the former.
- **Assuming the "same form as linear regression" means the same problem.** The gradient expression
  is (ŷ − y)x in both cases, but ŷ is linear in one and sigmoidal in the other, so the loss surface
  is not quadratic here and there is no normal equation.

## Connections

- [[activation-functions]] — the sigmoid whose derivative makes the gradient collapse to ŷ − y.
- [[logistic-regression]] — the complete model; the MLCS course reaches the same place by a
  different route.
- [[loss-functions-and-empirical-risk]] — the lecture-2 page that named cross-entropy and deferred
  it to this lecture; this page is that promise kept.
- [[soft-classification-and-calibration]] — probabilities as outputs, and why calibration is a
  separate question.
- [[perceptron]] — the yes/no model this replaces.
- [[gradient-descent-for-neural-networks]] — the optimiser that consumes this gradient.
- [[introduction-to-deep-learning-lecture-3]] — section 3.4 of the lecture.

## Open Questions

- **The convexity claim is asserted, not shown**: "BCE is convex in w, MSE with sigmoid is not" —
  the second half in particular would need the Hessian, which the slides do not compute.
- **The multiclass extension is promised and not delivered in this deck.**
- **No regularisation term appears**, so the lecture's logistic regression is unregularised, which
  differs from the MLCS course's treatment.
- **The calibration remark is a warning without a method** — how to calibrate, and whether it
  affects the loss, is not discussed.
- **Nothing is said about class imbalance**, although BCE weights each example equally and the
  semester's other course treats imbalance explicitly.