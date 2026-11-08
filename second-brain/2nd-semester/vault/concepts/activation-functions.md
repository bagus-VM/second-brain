---
title: "Activation Functions"
tags: [concept, introduction-to-deep-learning, semester-2, neural-networks]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-11-07
prerequisites: ["[[perceptron]]", "[[derivatives-cheat-sheet]]"]
---

## One-line Summary

An activation function replaces the perceptron's step with a differentiable non-linearity —
sigmoid, tanh, ReLU, Leaky ReLU or GELU — which buys gradient-based training and (for the sigmoid)
a probabilistic output, while leaving a single neuron's decision boundary linear.

## Core Intuition

The step function made two things impossible at once: gradient descent (no derivative) and soft
output (no score, only a verdict). Any smooth replacement fixes the first; the sigmoid fixes both
and additionally produces a number in (0, 1) that can be read as a probability. That is why the
lecture moves from perceptron → activation functions → logistic regression in one continuous
argument rather than presenting the functions as a catalogue.

The second thing to keep straight: non-linearity in the activation does **not** make a single
neuron non-linear as a classifier. The activation is monotone in z = wᵀx, so thresholding it is
thresholding wᵀx, and the boundary is still a hyperplane.

## Formal Definition / Statement

"To address these issues, we can replace the step-function in the perceptron with other functions:
activation functions." The lecture's own taxonomy:

- **Sigmoid types:** the logistic function ("sigmoid") and the hyperbolic tangent ("tanh").
- **Partially linear:** ReLU, Leaky ReLU, GELU.

It then restricts itself to one, with a promise: "We will learn more about other activation
functions later on!"

**The sigmoid, in full:**

σ(z) = 1 / (1 + e^(−z)) = e^z / (e^z + 1)

- "Squeezes any input into (0, 1)."
- "σ(0) = 0.5, σ(−z) = 1 − σ(z)."
- "Smooth and differentiable everywhere."
- "Interpretation: probability of the positive class."

**Its derivative**, derived on the slide by the chain rule: σ(z) = (1 + e^(−z))^(−1), so
dσ/dz = −(1 + e^(−z))^(−2)·(−e^(−z)) = e^(−z)/(1 + e^(−z))², and using 1 − σ(z) = e^(−z)/(1 + e^(−z)):

dσ(z)/dz = σ(z)·(1 − σ(z))

That identity is what makes logistic regression's gradient collapse to (ŷ − y)x later.

**The decision rule with a sigmoid** is unchanged in position: predict class 1 if ŷ ≥ 0.5 ⇔ wᵀx ≥ 0 —
"same linear decision boundary as the perceptron – but now with a probability and a differentiable
model".

## Key Properties

**Differentiability is the whole point, and it is used immediately.** Because σ′ exists everywhere,
gradient descent becomes applicable, which resolves the perceptron's first deficit ("it is not a
'principled' method like gradient descent").

**The output range determines the interpretation.** Sigmoid: (0, 1), "probability of the positive
class". Tanh: (−1, 1), zero-centred — which is why it is the usual hidden-layer choice in the
material's plots, though the lecture does not argue the point. ReLU and GELU are unbounded above,
so they cannot be read as probabilities.

**The symmetry identity σ(−z) = 1 − σ(z)** is a computational and conceptual convenience: it makes
"probability of the negative class" free, and it makes the sigmoid's behaviour around zero
symmetric.

**A probability-shaped output is not yet a calibrated probability.** The lecture flags this before
building on it: "With sigmoids, we can model uncertainty in the outcome. But… not every certainty
score is a probability → we need calibration!" The details live on
[[soft-classification-and-calibration]].

**Non-linearity must be stacked to matter.** "Activation functions add an element of non-linearity.
But: a single neuron still has a linear decision boundary. Non-linear problems (right) need
non-linear models → stack several neurons with non-linear activations: multi-layer networks
(lecture 4)."

## Worked Example

**The sigmoid at five points**, computed from σ(z) = 1/(1 + e^(−z)):

| z | σ(z) | reading |
|---|---|---|
| −4 | 0.0180 | almost certainly class 0 |
| −1 | 0.2689 | leans class 0 |
| 0 | 0.5000 | the decision boundary |
| +1 | 0.7311 | leans class 1 |
| +4 | 0.9820 | almost certainly class 1 |

**The derivative at the same points**, using σ(1 − σ): at z = 0 it is 0.25 (the maximum); at
z = ±1, 0.1966; at z = ±4, 0.0177. So the gradient is largest exactly at the decision boundary and
vanishes in the saturated regions — the reason a confidently-wrong sigmoid unit learns slowly, which
is the motivation for binary cross-entropy over squared error (see [[binary-cross-entropy]]).

**The asymmetry check:** σ(−1) = 0.2689 and 1 − σ(1) = 1 − 0.7311 = 0.2689 — the identity
σ(−z) = 1 − σ(z) holds to four decimals, which is the quickest way to verify an implementation.

## Common Pitfalls

- **Believing a sigmoid output is a probability.** It is shaped like one; the lecture explicitly
  says calibration is needed before treating it as one.
- **Thinking the sigmoid makes the classifier non-linear.** The boundary is still wᵀx = 0.
- **Using the derivative formula without deriving it** — the identity σ′ = σ(1 − σ) is usually
  asked for, and it follows in two lines from the quotient/chain rule.
- **Forgetting the vanishing gradient at saturation.** σ′ ≤ 0.25 everywhere, so gradients shrink by
  at least a factor of 4 per sigmoid layer; deep stacks of sigmoids are the classic failure case.
- **Mixing output ranges.** Sigmoid outputs (0, 1) with labels {0, 1}; the perceptron used {−1, 1}.
  Applying a {0, 1} loss to {−1, 1} labels silently trains the wrong thing.
- **Assuming ReLU/GELU behave like sigmoids.** They are not bounded, not probabilistic, and not
  zero-centred; the lecture names them but does not analyse them here.

## Connections

- [[perceptron]] — the model whose step function these replace.
- [[binary-cross-entropy]] — the loss designed for a sigmoid output, and the reason MSE is wrong
  with one.
- [[logistic-regression]] — sigmoid + cross-entropy, i.e. the complete model.
- [[soft-classification-and-calibration]] — what "probability" requires beyond the sigmoid's range.
- [[gradient-descent-for-neural-networks]] — the training procedure that becomes possible once the
  activation is differentiable.
- [[derivatives-cheat-sheet]] — the exercise material this derivation draws on.
- [[introduction-to-deep-learning-lecture-3]] — the lecture that presents it, section 3.4.

## Open Questions

- **Why these five functions** and not others is not argued; the lecture says only that the others
  come later.
- **tanh is shown but never given a formula or a derivative** on these slides, even though it is
  plotted next to the sigmoid.
- **ReLU, Leaky ReLU and GELU are named and plotted without formulas**, so their derivatives (the
  practically important part) are deferred entirely.
- **The calibration requirement is stated as a slogan** ("not every certainty score is a
  probability") with no method attached — whether it is examinable in this course is unclear.
- **No guidance on choosing an activation for a given layer** appears in the lecture material.