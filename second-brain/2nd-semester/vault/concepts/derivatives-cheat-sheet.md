---
title: "Derivatives Cheat Sheet"
tags: [concept, deep-learning, semester-2, calculus, reference]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[linear-algebra-for-deep-learning]]"]
---

## One-line Summary

The course's one-page derivative reference sheet, reproduced here as a lookup table: the differentiation rules needed to differentiate losses and activations by hand, in the four groups the sheet uses — basic functions, combination rules, several variables, and the handful of functions deep learning uses most — with the sheet's own worked examples attached to each row.

## Core Intuition

Gradient descent needs ∂E/∂w at every step, and the exercise sheets ask for a few of those derivatives by hand: exercise 2's task 2 requests the derivatives of linear-algebra, sigmoid, tanh and probability expressions, and exercise 3 asks for the derivative of a one-variable loss before it is stepped. The sheet exists so that this becomes a lookup rather than a derivation. It is scoped to exactly that use — scalar functions of one or several variables, results stated without proofs, no error bounds, and a short block of activation and loss derivatives. It is not a calculus chapter and does not claim to be one. [[gradient-descent-for-neural-networks]] records the course's parallel instruction that gradients for real models are "not computed by hand! → PyTorch"; this sheet covers the cases where they still are.

## Formal Definition / Statement

Notation, from the sheet: f′(x) = df/dx is the slope of f at x; c, n and a are constants; f and g are functions of x.

**Basic functions.**

| Rule | General | Example |
|---|---|---|
| Constant | (c)′ = 0 | (7)′ = 0 |
| Power rule (any real n) | (xⁿ)′ = n·xⁿ⁻¹ | (x⁵)′ = 5x⁴ |
| Roots | (√x)′ = (x^(1/2))′ = 1/(2√x) | (x^(1/3))′ = (1/3)·x^(−2/3) |
| Reciprocals | (1/x)′ = (x^(−1))′ = −1/x² | (1/x³)′ = (x^(−3))′ = −3/x⁴ |
| Exponential | (eˣ)′ = eˣ ; (aˣ)′ = aˣ·ln a | (5eˣ)′ = 5eˣ ; (2ˣ)′ = 2ˣ·ln 2 |
| Logarithm (x > 0) | (ln x)′ = 1/x ; (log_a x)′ = 1/(x·ln a) | (ln x²)′ = (2·ln x)′ = 2/x ; (log₂ x)′ = 1/(x·ln 2) |
| Sine, cosine | (sin x)′ = cos x ; (cos x)′ = −sin x | (2·sin x − cos x)′ = 2·cos x + sin x |

**Combining functions.**

| Rule | General | Example |
|---|---|---|
| Constant factor | (c·f)′ = c·f′ | (3x²)′ = 3·2x = 6x |
| Sum rule | (f + g)′ = f′ + g′ | (x³ + sin x)′ = 3x² + cos x |
| Product rule | (f·g)′ = f′g + fg′ | (x²eˣ)′ = 2xeˣ + x²eˣ |
| Quotient rule (g ≠ 0) | (f/g)′ = (f′g − fg′)/g² | (eˣ/x)′ = (eˣ·x − eˣ·1)/x² = (x − 1)eˣ/x² |
| Chain rule ("outer′ · inner′") | (f(g(x)))′ = f′(g(x))·g′(x); Leibniz form df/dx = df/dg · dg/dx | (e^(−x²))′ = e^(−x²)·(−2x), with outer eᵘ and inner u = −x² |
| Nested chains | apply repeatedly, from the outside in: df/dx = df/dg · dg/dh · dh/dx | ((ln(1 + x²))³)′ = 3(ln(1 + x²))² · 1/(1 + x²) · 2x |

## Key Properties

**Several variables.**

| Rule | General | Example |
|---|---|---|
| Partial derivative | differentiate with respect to one variable, treat all others as constants | f = x²y + 3y: ∂f/∂x = 2xy, ∂f/∂y = x² + 3 |
| Gradient | ∇f = (∂f/∂x₁, …, ∂f/∂xₙ)^T | ∇f(x, y) = (2xy, x² + 3)^T |

The sheet attaches one sentence to the gradient row: it "points in the direction of steepest ascent" — the fact the gradient descent loop inverts by subtracting ([[gradient-descent-step-mechanics]]).

**Frequently used in deep learning.**

| Rule | General | Example |
|---|---|---|
| Sigmoid | σ(x) = 1/(1 + e^(−x)) | σ′(x) = σ(x)(1 − σ(x)) |
| tanh | tanh(x) = (eˣ − e^(−x))/(eˣ + e^(−x)) | tanh′(x) = 1 − tanh²(x) |
| ReLU | ReLU(x) = max(0, x) | ReLU′(x) = 1 for x > 0, 0 for x < 0 (not differentiable at 0; in practice set to 0) |
| Squared error | (y − ŷ)² | ∂/∂ŷ (y − ŷ)² = −2(y − ŷ) |

Three properties follow from what the sheet is. It is a table of scalar rules: every row differentiates a scalar with respect to a scalar or a single vector component, so there is no Jacobian, no matrix calculus and no chain rule stated for vector-valued functions. It is exhaustive only for the four entries in the deep-learning block — the activation and loss derivatives this course uses. And it states results rather than derivations: the sigmoid and tanh identities are given as identities, with no route from the quotient rule to them.

## Worked Example

**The sheet's own example.** ((ln(1 + x²))³)′ = 3(ln(1 + x²))² · 1/(1 + x²) · 2x. Three factors, produced from the outside in by the nested-chain row: the derivative of the cube (3v² with v = ln(1 + x²)), the derivative of the logarithm (1/u with u = 1 + x²), and the derivative of the inner quadratic (2x). Reversing the order multiplies the same three factors in the wrong positions, which is why the sheet writes "from the outside in" explicitly.

**The hand differentiations the course asks for.** Exercise 2's task 2 asks for the derivatives of linear-algebra, sigmoid, tanh and probability expressions, and the official solutions use exactly these identities:

- σ′(x) = σ(x)(1 − σ(x)) — the sheet's sigmoid row, applied instead of differentiating 1/(1 + e^(−x)) from scratch.
- tanh′(x) = 1 − tanh²(x) — the sheet's tanh row, in the form the solutions use.
- grad_x (aᵀx) = aᵀ — a linear-algebra derivative with no row on the sheet: it differentiates a scalar with respect to a vector, and the "several variables" block gives only partial derivatives and the gradient of a scalar function.
- the Jacobian of a componentwise (elementwise) map a is diagonal — also outside the sheet, which defines no Jacobian at all.
- E(aX) = a·E(X) and E(a) = a — expectation rules rather than derivatives, asked in the same task.
- Var(X + Y) = Var(X) + Var(Y) + 2·Cov(X, Y) — the covariance term is the one that is usually dropped, and it vanishes only when X and Y are uncorrelated.
- the candidate density p(x) = 3x² − eˣ on [2, 4] fails as a PDF because p(4) < 0, and a density may not be negative (p(4) = −6.598150).

The pattern is worth stating plainly: the sheet covers the calculus rows of task 2 and nothing else, so the linear-algebra and probability rows are answered from the lecture's own material instead.

## Common Pitfalls

- **Applying the chain rule inside-out.** The sheet's nested example multiplies the outermost derivative first: 3(ln(1 + x²))² · 1/(1 + x²) · 2x. Written in the other order the factors attach to the wrong functions and the product is wrong — the most common way a correct-looking derivative is silently false.
- **The ReLU derivative at 0.** ReLU is not differentiable at x = 0; "in practice set to 0" is a convention chosen for convenience, not a limit value, and the sheet says as much in the same cell.
- **Forgetting that a partial derivative holds the other variables fixed.** For f = x²y + 3y, ∂f/∂x = 2xy — the 3y term is constant in x and contributes nothing — while ∂f/∂y = x² + 3 keeps it. Treating the second variable as active in the first derivative is the error this row exists to prevent.
- **Confusing a Jacobian with a gradient.** The sheet defines ∇f only for a scalar f, as the vector of partial derivatives. A Jacobian is the derivative of a vector-valued function and the sheet gives no rule for it, so the exercise-2 result that a componentwise a has a diagonal Jacobian cannot be read off this sheet.
- **Writing Var(X + Y) = Var(X) + Var(Y).** True only when Cov(X, Y) = 0. The exercise-2 identity is the general form with the +2·Cov(X, Y) term, and dropping it is the mistake the exercise tests.
- **Treating the sheet as complete for losses.** It gives the squared-error derivative and nothing for the classification losses, so anything involving cross-entropy is outside its coverage.

## Connections

- [[gradient-descent-step-mechanics]] — the consumer of every rule here: the step needs ∂E/∂w, and the polynomial derivative in its worked example comes from this sheet's sum, constant-factor and chain rows.
- [[gradient-descent-for-neural-networks]] — why gradients are needed at all, and why the course computes them with PyTorch rather than by hand for real models.
- [[linear-algebra-for-deep-learning]] — the vector and matrix notation the gradient row uses; the Jacobian and matrix-calculus results the sheet omits come from this direction.
- [[pytorch-tensors-and-autograd]] — the automated path that replaces the sheet for anything larger than a hand exercise.
- [[loss-functions-and-empirical-risk]] — the squared-error and negative-log-likelihood derivatives the sheet does and does not provide.
- [[introduction-to-deep-learning-exercise-2]] — task 2, where the sigmoid, tanh, linear-algebra and probability identities are asked for by hand.
- [[introduction-to-deep-learning-exercise-3]] — the session whose gradient descent tasks apply these rules to a polynomial loss and to a two-variable product.

## Open Questions

- **No softmax derivative and no cross-entropy derivative.** The sheet covers the sigmoid for two classes and stops; the multi-class counterparts and the combined softmax + cross-entropy gradient are absent, and that is precisely the case where the chain rule through a normalisation is worth having in writing.
- **ReLU at exactly 0 gets a convention, not a definition.** "In practice set to 0" is stated with no discussion of subgradients or of what a framework does at that point.
- **No numerical-differentiation guidance and no error bounds**, even though the vault's own verification of the exercise-3 numbers rests on finite-difference checks against the analytic derivative (see [[gradient-descent-step-mechanics]]); the sheet says nothing about how such a check is set up or how closely it should agree.
- **No Jacobian or matrix-calculus rows**, so the sheet cannot answer the linear-algebra part of exercise 2's task 2 on its own.
- **No second-order or higher derivatives**, and nothing on differentiating through a sum, a product or an expectation as such: the probability identities in exercise 2 are not consequences of any row here.
- **No provenance for the sheet itself.** It carries the course header and one page; no reference work, textbook or author is cited, so its conventions (for example "set to 0 in practice") have no external source to check against.
