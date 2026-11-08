---
title: "Loss Functions and Empirical Risk"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, optimization]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[ml-data-and-iid-assumption]]"]
---

## One-line Summary
Training is minimising the average loss over the training data, and the loss you choose decides what
the model is actually optimising for — including whether the problem is differentiable at all.

## Core Intuition

"Learn from data" is not an algorithm. The lecture's move is to replace it with something you can
compute: define a number that is small when the parameters are good, average it over the training
set, and search for the parameters that make it smallest. The average loss on the training data has a
name — **empirical risk** — and the search is an optimisation problem.

Two things follow, and the lecture spends its budget on the first. First, **the loss function is a
design choice, not a given**. Squared error and 0-1 loss can rank the same two models in opposite
orders (worked example below), because they disagree about what counts as a bad prediction. Choosing
a loss is choosing what the model will care about. Second, **differentiability matters**, and the
lecture marks it explicitly: 0-1 loss is flat almost everywhere, so there is no gradient to follow.

The parameters/hyperparameters split enters here too, and it is the cleanest way to see it:
parameters `w` are *learned* by the optimiser; hyperparameters (the learning rate `eta`, the model
capacity, what may be scored at all) are *set by the user* and govern the procedure. The distinction
is not about importance — it is about who decides.

## Formal Definition / Statement

**Slide 19, training as optimisation.**

A loss function (also called an error function) "measures how good the current parameters are —
ideally differentiable". The training loss is the average loss over the training data, the empirical
risk:

```
L(w) = (1/n) * Σ_{i=1..n} l(f_w(x_i), y_i)
```

and the goal is

```
w* = argmin_w L(w)
```

**Three losses named on the slide:**

| Loss | Form | Domain | Note on the slide |
|------|------|--------|-------------------|
| Misclassification, 0-1 loss | `l = 1 if y_hat != y, else 0` | classification | **"not differentiable"** |
| Squared error | `l = (y_hat - y)^2` | regression | |
| Negative log-likelihood | `l = -log p_w(y | x)` | probabilistic | "→ cross-entropy, next lecture" |

**The optimiser, as given:**

```
w <- w - eta * grad_w L(w)
```

with the learning rate `eta` a hyperparameter, and "details: next lecture".

**Parameters versus hyperparameters (slide 16):**

- During training we choose a type/class of models, then learn the concrete model `f_w` of that type
  that is in line with the training data. Models are often functions with free parameters `w`, and we
  learn how to choose them so that the model makes good predictions on the training data → loss
  functions.
- **Hyperparameters are set by the user and determine the learning procedure (not learned).**

Slide 21 adds a worked construction of what parameters are: a scoring model where "we always start
with 1 point", each feature contributes points, and a bonus point applies when two features are
present together. **How many points each feature gets are the parameters. What we allow to be scored
is part of the hyperparameters.** With more parameters, more complex dependencies can be fitted.

## Key Properties

- **Empirical risk is an estimate of a population quantity.** The name is honest: it is the risk
  measured on the *empirical* sample, and nothing in the definition says it equals the risk on new
  data. That gap is the whole of [[polynomial-regression-and-overfitting]].
- **Differentiability is a licence to use gradients.** 0-1 loss is piecewise constant, so gradient
  descent has nothing to descend; the practical losses are the differentiable ones.
- **The loss fixes what "wrong" means.** Squared error punishes large errors quadratically; 0-1
  treats a 0.51 and a 0.99 prediction as equally right, and a 0.49 and a 0.01 as equally wrong.
- **Averaging over n is a modelling choice as well as an implementation one.** It makes the loss
  independent of dataset size, which is what lets one learning rate transfer between datasets.
- **"Ideally differentiable" is a preference, not a requirement.** The lecture does not claim
  non-differentiable losses are unusable, only that this pipeline will not optimise them.
- **Parameters are learned; hyperparameters govern learning.** It follows that a hyperparameter cannot
  be fitted by the same descent that fits `w` — which is why [[cross-validation]] exists.
- **The scoring example shows capacity concretely**: more parameters permit more complex
  dependencies, which is the machine-learning statement of the classical overfitting warning.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`.

Five instances with labels `y = [1, 1, 0, 0, 1]` and two candidate models:

| Model | Predictions | 0-1 loss | Squared error |
|-------|-------------|----------|---------------|
| A | 0.51, 0.51, 0.49, 0.49, 0.51 | **0.00** (accuracy 1.00) | 0.2401 |
| B | 1.00, 1.00, 0.00, 0.00, 0.00 | **0.20** (accuracy 0.80) | **0.2000** |

**The two losses disagree.** 0-1 loss prefers A, which is right on every row but never confident;
squared error prefers B, which is exact four times and maximally wrong once. Neither verdict is a
mistake — the losses are answering different questions. A is a well-calibrated but undecided model;
B is a model with one serious error. Which is "better" depends on whether a confidently wrong
prediction costs more than five unconfident ones, and that is an application decision, which is why
it is a design choice.

**Why 0-1 loss cannot be optimised by gradient descent.** Using the same numbers, perturbing a
prediction of 0.51 down to 0.505 changes nothing in the 0-1 loss — the classification is unchanged —
so the gradient there is 0. Perturbing it below 0.5 jumps the loss by 0.2 with no intermediate value
in between. The loss is a step function with zero gradient everywhere except at the threshold, where
it is undefined. There is no direction for `w <- w - eta * grad L(w)` to move in.

**The empirical risk, assembled.** For B: L(w) = (1/5)(0 + 0 + 0 + 0 + 1) = 0.20 for squared error,
and (1/5)(0+0+0+0+1) = 0.20 for 0-1 loss — the two coincide only because B's errors are exactly 1 in
this construction. Model A: 0-1 gives 0.00 and squared error gives (1/5)(0.2401 × 5) = 0.2401. That
single coincidence is worth noticing because it is what makes model B look like a reasonable target
for both losses when the predictions are at the extremes.

## Common Pitfalls

- **Optimising accuracy directly.** Accuracy is one minus 0-1 loss; it is the loss with no gradient,
  and choosing it as the objective is choosing an objective the stated optimiser cannot handle.
- **Assuming the loss that is easiest to compute is the loss that matches the application.** Squared
  error on a classification task optimises a different thing from misclassification, as the worked
  example shows.
- **Treating the training loss as a performance estimate.** It is the quantity being minimised, so it
  falls almost by construction; slide 22-23 exist because of this.
- **Forgetting the `1/n`.** Without the average, the loss scales with dataset size and so does the
  effective learning rate.
- **Calling the learning rate a parameter.** It is the lecture's own example of a hyperparameter: "set
  by the user and determines the learning procedure".
- **Assuming hyperparameters must be integers or structural.** The learning rate is a continuous
  hyperparameter; "what we allow to be scored" in the scoring example is a structural one. Both are
  user-set.
- **Reading "ideally differentiable" as "always differentiable".** Negative log-likelihood is
  differentiable; 0-1 loss is not; the lecture names both in the same list.

## Connections

- [[ml-data-and-iid-assumption]] — the terms `l(y_hat_i, y_i)` and the average over `n` are defined
  there; this page is what the average is for.
- [[gradient-descent-for-neural-networks]] — the optimiser, developed properly; this page stops at the
  update rule.
- [[polynomial-regression-and-overfitting]] — the exercise that turns low training loss into a warning
  rather than a result.
- [[cross-validation]] — the procedure for the quantities that are not learned.
- [[linear-regression]] — the model whose canonical loss is squared error.
- [[logistic-regression]] — the model whose canonical loss is the negative log-likelihood leading to
  cross-entropy.
- [[classification-metrics]] — the measures that describe the *outcome* when 0-1 loss is what you
  finally care about but cannot optimise.
- [[class-imbalance]] — where a 0-1 loss on an imbalanced problem is quietly the wrong objective.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **The lecture gives the gradient-descent update and explicitly defers the details.** Step size
  selection, convergence, stochastic and mini-batch variants, and the computation graph are all
  announced for the next lecture.
- **No loss is recommended for any task.** The three are listed without guidance on which to pick,
  beyond the regression/classification split implied by "squared error (regression)".
- **What the empirical risk estimates is not stated.** The population risk, the i.i.d. assumption
  behind the estimate, and the generalisation gap are not named here; they are treated visually in
  the next section of the same lecture.
- **Cross-entropy is named and deferred.** The negative log-likelihood line ends with
  "→ cross-entropy, next lecture", so this page's treatment is deliberately partial.
- **The scoring example is presented without a loss.** Slide 21 shows parameters and hyperparameters
  but does not say which loss is being minimised on the small table.