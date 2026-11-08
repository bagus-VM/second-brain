---
title: "The Perceptron"
tags: [concept, introduction-to-deep-learning, semester-2, neural-networks]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-11-07
prerequisites: ["[[linear-regression]]", "vectors and dot products"]
---

## One-line Summary

A perceptron is a linear weighted sum followed by a step function — a binary classifier whose
decision boundary is a hyperplane, trained by a correction rule rather than by gradient descent
because the step function has no useful gradient.

## Core Intuition

Linear regression outputs any number; classification must output one of two labels. The perceptron
gets there with one change: keep the weighted sum f(w, x) = wᵀx, then threshold it. The lecture's
analogy is a neuron that "fires" if it gets "enough" input — the dot product is the amount of
input, the threshold is the firing condition.

Geometrically this is the cleanest model in the course: wᵀx = 0 is a line in 2-D, a plane in 3-D,
a hyperplane in general. **w** (without the bias) is its normal vector, and the bias w₀ shifts the
boundary away from the origin. Points on the side w points to satisfy wᵀx > 0 and get class +1.
Everything a perceptron can and cannot do follows from that one picture — which is why the XOR
failure is a statement about lines, not about learning.

## Formal Definition / Statement

**Model.** Labels y ∈ {−1, 1} (the lecture notes logistic regression will switch to y ∈ {0, 1}).
"Linear weighted function + decision rule":

f(w, x) = wᵀx for the linear part, and

f(w, x) = 1 if wᵀx ≥ 0, −1 if wᵀx < 0

with the convention "x = [1, x]ᵀ ⇒ f(x, w) = w₀ + w₁x", i.e. the bias is a weight on a constant
input of 1. The diagram is the standard one: inputs x₁ … x_k multiplied by w₁ … w_k, summed with a
bias w₀, then a step function producing ŷ ∈ {−1, 1}.

**Training rule.** "GD/SGD not applicable! Threshold function is not differentiable." Instead, "if
we make an error for one instance i: adapt the weights in the 'right' direction; the higher the
input, the larger the adjustment":

w₀^new = w₀^old − α·(ŷᵢ − yᵢ)
w₁^new = w₁^old − α·(ŷᵢ − yᵢ)·xᵢ,₁
…
w_k^new = w_k^old − α·(ŷᵢ − yᵢ)·xᵢ,k

"Correctly classified instances: ŷ − y = 0 → no update." With labels ±1 the rule is often written
as "w ← w + αyx (for misclassified x)" — the two forms agree because ŷ − y ∈ {−2, 0, +2}.

**Convergence.** "It has (very early!) been shown that this learning algorithm finds a solution for
every problem that the perceptron can solve: if the data are linearly separable, it converges after
a finite number of updates (Novikoff, 1962). [No proof here]" — and the limit: "many problems are
not linearly separable, e.g., XOR → needs several layers (lecture 4)".

## Key Properties

**The update is driven by error, scaled by input magnitude.** A large input produces a large weight
change; a correctly classified instance changes nothing. There is no learning rate schedule
question beyond α, and no notion of an epoch-wise loss to monitor.

**History, in the lecture's four dates:** 1943 McCulloch & Pitts model a neuron as a threshold unit
with fixed weights; 1958 Rosenblatt's perceptron learns the weights from data, with the Mark I
Perceptron hardware for image recognition using 20 × 20 photocells; 1969 Minsky & Papert's
*Perceptrons* shows a single perceptron cannot learn simple functions like XOR, and "interest in
neural networks dropped for years"; 1986 Rumelhart, Hinton & Williams provide backpropagation for
multi-layer networks.

**The step function is the deficiency, and it is stated twice.** The perceptron's training is "not
a 'principled' method like gradient descent" because "if we try to use gradient descent, the
gradient is actually zero or undefined for the step function"; and it returns "only a yes – no
answer for the class", with no certainty or probability. Both deficits are repaired in the next
section by replacing the step with a sigmoid.

**Linearity is a property of the neuron, not of the activation alone.** Even with a non-linear
activation, "a single neuron still has a linear decision boundary", because the activation is
monotone in wᵀx and therefore thresholds at a single value of wᵀx. Non-linear problems "need
non-linear models → stack several neurons with non-linear activations".

## Worked Example

The lecture's numeric example, checked step by step.

Weights w = (w₀, w₁, w₂) = (0, 1, −1), learning rate α = 0.5, instance x = (1, 1, 2) (first entry
the constant 1 for the bias), label y = +1.

1. **Predict.** wᵀx = 0·1 + 1·1 + (−1)·2 = 0 + 1 − 2 = −1 < 0 ⇒ ŷ = −1. Wrong, since y = +1.
2. **Update.** w ← w − α(ŷ − y)x = (0, 1, −1) − 0.5·(−1 − 1)·(1, 1, 2)
   = (0, 1, −1) + (1, 1, 2) = (1, 2, 1).
3. **Re-predict.** wᵀx = 1·1 + 2·1 + 1·2 = 1 + 2 + 2 = 5 ≥ 0 ⇒ ŷ = +1. Correct.

The same arithmetic in the slide's compact form: w ← w + αyx = (0, 1, −1) + 0.5·(+1)·(1, 1, 2) =
(1, 2, 1) — identical, because ŷ − y = −2 and the two rules differ by exactly that factor.

Note what the update did geometrically: it rotated and shifted the hyperplane until this point fell
on the positive side, and because the point had a large x₂ it moved w₂ the most.

## Common Pitfalls

- **Trying to differentiate the step function.** Zero gradient or undefined — the whole reason the
  perceptron has its own update rule.
- **Updating on correct predictions.** ŷ − y = 0 leaves the weights untouched; a "bug" that applies
  the rule unconditionally still trains but converges differently.
- **Forgetting the bias input.** The constant 1 as x₀ is what makes w₀ a free parameter; without it
  the boundary is forced through the origin.
- **Confusing the label conventions.** With y ∈ {−1, 1} the correction term is 2α on an error; with
  y ∈ {0, 1} (logistic regression) the arithmetic is different. The lecture uses both conventions
  in consecutive sections.
- **Expecting convergence on non-separable data.** Novikoff's guarantee is conditional on linear
  separability; XOR never terminates with a separating boundary because none exists.
- **Reading "linear classifier" as "weak classifier".** The failure is specific: XOR, and anything
  needing two boundaries. See [[support-vector-machines]] for the margin-based linear classifier
  that follows the same geometry.

## Connections

- [[linear-regression]] — the same weighted sum without the threshold.
- [[activation-functions]] — the sigmoid replaces the step and makes the model differentiable; this
  is the fix for both stated deficits.
- [[binary-cross-entropy]] — the loss that comes with the sigmoid, i.e. logistic regression.
- [[logistic-regression]] — the same decision boundary, with a probability output (and the MLCS
  course's treatment of it).
- [[support-vector-machines]] — the other linear classifier in this semester's material; both are
  limited by the same line.
- [[soft-classification-and-calibration]] — what "only a yes/no answer" costs, and why a score is
  not yet a probability.
- [[introduction-to-deep-learning-lecture-3]] — the lecture that defines it, section 3.3.

## Open Questions

- **The learning rate α's admissible range is not given**; the update is a correction, so any
  α > 0 that does not overshoot works, but the lecture gives no guidance and the worked example
  fixes α = 0.5 without justification.
- **Whether the update is applied per-instance in a fixed or random order** is not stated, and the
  classic convergence proof assumes a fixed cycling order.
- **Novikoff's theorem is cited but not stated formally** — the bound on the number of updates in
  terms of margin and radius is not in the slides.
- **The Mark I Perceptron's 20 × 20 photocell array is described but not connected to the model**
  (how the weights were realised physically is not explained).