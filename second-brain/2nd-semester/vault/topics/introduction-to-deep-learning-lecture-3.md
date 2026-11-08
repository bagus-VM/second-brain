---
title: "Introduction to Deep Learning — Lecture 3 Overview (Single-Layer Neural Networks)"
tags: [topic, introduction-to-deep-learning, semester-2, neural-networks]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[introduction-to-deep-learning-lecture-2]]"]
---

## One-line Summary

One lecture builds the whole single-layer stack in order — linear regression, gradient descent,
perceptron, logistic regression, computation graphs — so that each model is the previous one with
exactly one defect repaired, and each repair is what makes the next model necessary.

## Core Map

```
Lecture 3 — Single-Layer Neural Networks (63 slides)
│
├── Notation recap (lecture 2)
│   └── D = {(xᵢ,yᵢ)}, w = (w₀..w_k), ŷ = f_w(x), L(ŷ,y), E(w) = Σ L
│
├── 3.1 Linear regression
│   ├── ŷ = w₀ + w₁x₁ + … + w_kx_k ; least-squares E(w) = Σ(ŷᵢ − yᵢ)²
│   ├── matrix form min‖Xw − y‖² ; normal equation w = (XᵀX)⁻¹Xᵀy
│   ├── cost O(np² + p³) — exact, but costly for large n
│   └── -> [[linear-regression]]
│
├── 3.2 Gradient descent
│   ├── ∇ = vector of partials; step xₜ₊₁ = xₜ − α∇f(xₜ); α = learning rate
│   ├── optimise over the weights w, NOT over the data x
│   ├── convex vs non-convex; GD finds a local minimum in general
│   ├── worked example: E(w) = 10w − 20 → w converges to 2 at α = 0.05, diverges at 0.25
│   ├── batch / mini-batch / stochastic; epoch vs iteration
│   └── -> [[gradient-descent-step-mechanics]], [[gradient-descent-for-neural-networks]],
│        [[stochastic-gradient-descent]]
│
├── 3.3 Perceptron
│   ├── f = wᵀx then step: +1 if wᵀx ≥ 0 else −1
│   ├── history 1943 / 1958 / 1969 (XOR) / 1986 (backprop)
│   ├── no GD — threshold not differentiable; correction rule w ← w − α(ŷ−y)x
│   ├── Novikoff 1962: converges iff linearly separable
│   └── -> [[perceptron]]
│
├── 3.4 Logistic regression
│   ├── two deficits: not principled, only yes/no
│   ├── activation functions: sigmoid, tanh, ReLU, Leaky ReLU, GELU
│   ├── σ(z) = 1/(1+e^(−z)), σ′ = σ(1−σ); ŷ = σ(wᵀx) = P(y=1|x)
│   ├── maximum likelihood → binary cross-entropy
│   ├── why not MSE: vanishing gradient + non-convexity
│   └── -> [[activation-functions]], [[binary-cross-entropy]], [[logistic-regression]]
│
└── 3.5 Computation graphs
    ├── input / parameter / compute nodes; atomic assignments
    ├── forward pass = loss; backward pass = all gradients by chain rule
    ├── granularity is a design decision
    ├── worked table: x=2, y=3, w₀=1, w₁=0.5 → ∂L/∂w₀ = −2, ∂L/∂w₁ = −4
    └── autograd reproduces it exactly -> [[computation-graphs]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[perceptron]] | Linear sum + step; correction rule; XOR is impossible |
| [[activation-functions]] | Sigmoid as the differentiable, probabilistic replacement for the step |
| [[binary-cross-entropy]] | −y log ŷ − (1−y) log(1−ŷ), derived from maximum likelihood |
| [[computation-graphs]] | Atomic assignments; forward gives the loss, backward gives every gradient |
| [[stochastic-gradient-descent]] | Batch size, epochs, iterations, and why the noise is not only bad |
| [[linear-regression]] | The closed-form baseline this lecture starts from (MLCS course page) |
| [[logistic-regression]] | The same model completed by sigmoid + cross-entropy (MLCS course page) |

## Lecture Structure

1. **Notation recap** — dataset, feature vector, model, prediction, single-instance loss, total
   error E(w) = Σ L(ŷᵢ, yᵢ); "in this lecture, 'error function' E and 'loss function' L mean the same
   idea".
2. **3.1 Linear regression** — predicting a continuous y; the least-squares error; matrix notation
   with the constant column; the normal equation and its O(np² + p³) cost.
3. **3.2 Gradient descent** — gradient as the vector of partial derivatives; the five-step algorithm;
   "what we are optimizing here is the function f(x) … x is (typically) the weights w! NOT the input
   data x"; step size and convergence; convexity quiz (|x|, x², −x², and a non-convex example);
   the gradient in matrix notation; the worked example and its α = 0.25 divergence; learning-rate
   practice; stochastic and mini-batch variants; epoch/iteration arithmetic; the comparison plot;
   why the noise helps; outlook (momentum, RMSProp, Adam).
4. **3.3 Perceptron** — binary outputs and the step; the diagram; four history milestones; the
   geometric view; the non-differentiability problem and the correction rule; the numeric update
   example; Novikoff's convergence and the XOR limit.
5. **3.4 Logistic regression** — the two deficits of the perceptron; activation functions; the
   sigmoid and its derivative; the model and decision rule; probabilistic predictions and the
   calibration warning; maximum likelihood; binary cross-entropy; why not squared error; the
   gradient; a 1-D example; the non-linearity discussion that leads to multi-layer networks.
6. **3.5 Computation graphs** — the decomposition, the three node types, granularity, the linear and
   logistic examples, the forward/backward table, and PyTorch autograd.
7. **Summary and outlook** — five take-home messages, and lecture 4: multi-layer networks, XOR and
   linear separability, hidden layers, expressivity, backpropagation.

## Exam-Relevant Points

1. **The one-defect-one-repair structure is the lecture's argument**, and it is the most examinable
   thing in it: linear regression → cannot classify; perceptron → not differentiable, no
   probability; logistic regression → needs an efficient gradient for deep models; computation
   graphs → that efficiency.
2. **The normal equation w = (XᵀX)⁻¹Xᵀy with O(np² + p³)** is quoted with its cost and its
   limitation ("gets costly for large datasets"), which is why gradient descent follows.
3. **Gradient descent optimises the weights, not the data** — the slide underlines it.
4. **The convergence statement is conditional**: for convex functions with a small enough learning
   rate it finds the global minimum; in general it "finds any (local) minimum – not necessarily the
   global one".
5. **The worked divergence** — α = 0.05 converges to w = 2, α = 0.25 gives 0 → 5 → −2.5 → 8.75 → …
   and "each step overshoots the minimum w = 2 by more than before: GD diverges".
6. **The perceptron's update rule and Novikoff's guarantee** (finite convergence iff linearly
   separable) are both stated; XOR is the counter-example.
7. **σ′ = σ(1 − σ)** and **∇_w L = (ŷ − y)x** are the two derivations to be able to reproduce.
8. **The MSE-vs-BCE argument has two halves** — vanishing gradient for confident wrong predictions,
   and convexity in w — and both are on the slide.
9. **The computation-graph table** (x = 2, y = 3, w₀ = 1, w₁ = 0.5 → ∂L/∂w₀ = −2, ∂L/∂w₁ = −4) is a
   worked answer that can be asked for verbatim.
10. **Batch/epoch bookkeeping**: 10 000 examples at batch 32 gives ⌈10000/32⌉ = 313 updates per
    epoch; an epoch is a data pass, an iteration is one update.

## Connections

- [[introduction-to-deep-learning-lecture-2]] — the notation, the loss/empirical-risk framework, and
  the page that explicitly deferred cross-entropy to this lecture
  ([[loss-functions-and-empirical-risk]]).
- [[introduction-to-deep-learning-exercise-3]] — the same material done by hand (evaluation metrics
  and gradient descent), so the exercise and the lecture reinforce each other.
- [[deep-learning-course-roadmap]] — lecture 3's place in the fifteen-week plan.
- [[machine-learning-for-cybersecurity-lecture-3]] — Reiser's course reaches logistic regression by
  a different route (ROC and metrics first); the two treatments are complementary rather than
  duplicates.
- [[polynomial-regression-and-overfitting]], [[double-descent]] — lecture 2's generalisation
  material, which assumes the fitting machinery built here.
- Lecture 4 does not exist in the vault yet: multi-layer networks, backpropagation and
  expressivity have no deck in `raw/`.

## Open Questions

- **The convexity quiz's answers are printed but the fourth function (D, −x²) is only described as
  "concave, not convex"** — why |x| counts as convex despite being non-differentiable at 0 is stated
  in one clause and not developed.
- **The normal equation is given without a derivation**; the matrix-gradient derivation is supplied
  for the gradient form only (∇‖Xw − y‖² = 2XᵀXw − 2Xᵀy).
- **No regularisation appears** in either the regression or the classification treatment.
- **Calibration is named as a requirement and never defined** — "not every certainty score is a
  probability → we need calibration!".
- **The Kaleidoscope of optimisers is deferred** (momentum, RMSProp, Adam) with no slide-level
  pointer to where they will be covered.
- **The exercise-3 handwritten notes in `raw/`** (`03-PnP-01.jpg`, `03-PnP-02.jpg`, added
  2026-11-05) are the student's own pen-and-paper working, not course material: they duplicate the
  gradient-descent-by-hand content of [[introduction-to-deep-learning-exercise-3]] and are not a
  source for this page. One arithmetic slip in them is worth knowing: in Example 2 the gradient
  vector (16, 12) was written down as the new point, where the update from (2, 4) with α = 1 gives
  (2, 4) − (16, 12) = (−14, −8).