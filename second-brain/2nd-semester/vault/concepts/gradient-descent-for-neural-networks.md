---
title: "Gradient Descent for Neural Networks"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[neural-network-training-loop]]", "[[linear-algebra-for-deep-learning]]"]
---

## One-line Summary

Gradient descent is the general method of approximately minimising a differentiable function by repeatedly stepping against its gradient; for neural networks it is the only practical option, because the activation functions make the loss non-analytic.

## Core Intuition

The exercise 2 slides open with a detour that exists to be demolished. For a scalar function of one variable, minimisation is a three-step ritual: "Compute the derivative / Find all x where f'(x) = 0 / Use the second derivative to check whether each critical point is a minimum or a maximum". Applied to $f(x) = x^2 - 3x$, this gives $f'(x) = 2x - 3$, a single critical point at $x = 3/2$, and $f''(x) = 2 > 0$, so it is a minimum. Clean, exact, over.

Then the slides put a real network in the same slot:

$$f(W^{(1,2)}, b^{(1,2)}, x, y) = y^T \tanh\big(W^{(2)} \max(0, W^{(1)} x + b^{(1)}) + b^{(2)}\big)$$

and state the conclusion plainly: "non-linearity (due to activation functions) → we need numerical methods". The ReLU and the $\tanh$ break the algebra. You cannot differentiate through to a closed form and invert a matrix, because there is no matrix to invert — the derivative of a composition of a rectifier and a hyperbolic tangent is a composition of a rectifier and a hyperbolic tangent.

The intuition that replaces the calculus: you cannot see the shape of the loss surface, but you can measure its slope at the point where you stand. Move against the slope. Repeat. That is gradient descent, and it is the method the entire deep learning apparatus is built around.

## Formal Definition / Statement

**The analytic recipe, and why it fails.** For a differentiable $f(x)$ in one variable: compute $f'$, solve $f'(x) = 0$ for all critical points, classify each with $f''$. For a neural network, the same recipe fails at the first step — no closed form for the stationary points of a composition of nonlinearities.

**The loss that must be minimised.** Weights $W$ and biases $b$ are trained to minimise a loss function. For a regression problem, the slides give

$$\min_{W^{(1)}, W^{(2)}, b^{(1)}, b^{(2)}} \sum_{i=1}^{N} \big(\hat{y}_i^{(\mathrm{pred})} - y_i^{(\mathrm{true})}\big)^2$$

A simple network producing those predictions is $\hat{y}_{(\mathrm{pred})} = \tanh(W^{(2)} \max(0, W^{(1)}x + b^{(1)}) + b^{(2)})$.

**The fix that makes it matter.** The slides emphasise that "Neural networks (NNs) are functions with many parameters", and that "Input x is fixed; during a forward pass, the parameters are also fixed". So the only thing that moves between forward passes is the parameter vector itself, and the object to minimise is the loss as a function of that vector alone.

**The update rule.** "Gradient Descent is a general method to approximately minimize / optimize a function; $\alpha$ is the learning rate":

$$w^{(t+1)} = w^t - \alpha \frac{\partial f(w^t, \ldots)}{\partial w}$$

"Repeat until convergence or until the compute budget is exhausted." The demo notebook writes the same rule in gradient notation as $w^{(t+1)} \leftarrow w^t - \alpha \cdot \nabla E(w^t)$, where $t+1$ indicates the weight update (one time step) and $\alpha$ is the learning rate. All gradient descent needs are "the gradient values of the parameters, and access to the parameters itself."

**What is not needed.** The slides close the detour with a practical instruction: "For now: we need derivatives (gradients) of the loss with respect to the parameters; not computed by hand! → PyTorch". The hand derivation of a chain of derivatives through two layers is where students lose an afternoon and gain nothing; the machine does it in microseconds.

**Deliberately a preview.** The final slide of the deck says "Next week: gradient descent in more detail", and the roadmap page places week 3 on "Gradient descent, evaluation metrics" and week 4 on "Automatic differentiation, stochastic gradient descent". The depth here is intentional.

## Key Properties

- **Gradient descent needs only local information.** The gradient at a point gives a descent direction; the global shape of the loss is irrelevant to the method, which is why it survives non-convex surfaces where a global analysis would fail.
- **It is an approximation with a stopping rule, not a solution.** "Repeat until convergence or until the compute budget is exhausted" — the second termination condition is not a fallback, it is the normal case for large networks.
- **The learning rate $\alpha$ is the only knob in the update rule.** Too small and convergence is slow; too large and the iterate overshoots, oscillates, or diverges. The demo's task "observe parameter changes based on learning rate changes" exists precisely because this is the parameter students must feel rather than derive.
- **Non-convexity is a fact of the loss, not a defect of the method.** With tanh and ReLU activations, the loss of a multi-layer network is not convex, so stationary points need not be minima and no global optimum is guaranteed.
- **The gradient is only useful if it is the gradient of the loss with respect to the parameters.** Autograd delivers exactly that, which is the entire reason PyTorch exists in this workflow.
- **SGD is the same rule applied per mini-batch.** Full-batch gradient descent is the special case where the batch is the whole dataset; the stochastic variant estimates the same gradient from a subset.

## Worked Example

**The analytic case, done properly.** $f(x) = x^2 - 3x$. The derivative is $f'(x) = 2x - 3$, so $f'(x) = 0$ at $x = 3/2$. The second derivative is $f''(x) = 2 > 0$ everywhere, so $x = 3/2$ is a global minimum with $f(3/2) = 9/4 - 9/2 = -9/4$. Nothing is iterative; the answer is exact and immediate.

**The network case, where the recipe breaks.** Take $f(W^{(1)}, W^{(2)}, b^{(1)}, b^{(2)}, x, y) = y^T \tanh(W^{(2)} \max(0, W^{(1)}x + b^{(1)}) + b^{(2)})$. Even with $x$ and $y$ fixed, the function of $(W^{(1)}, W^{(2)}, b^{(1)}, b^{(2)})$ contains $\max(0, \cdot)$, which is not differentiable at zero, and $\tanh$, which is transcendental. There is no $2 \times 2$ system to invert, no critical point to solve for in closed form. The slides' conclusion: "we need numerical methods".

**The numerical method, one step.** Suppose the loss $E(w)$ has gradient $\nabla E(w) = [2, -4]^T$ at the current parameter vector $w = [1, 1]^T$, and $\alpha = 0.1$. Then

$$w^{(1)} = w^{(0)} - 0.1 \cdot [2, -4]^T = [1 - 0.2,\; 1 + 0.4]^T = [0.8,\; 1.4]^T$$

The first coordinate moves down (the gradient was positive, so the step is negative), the second moves up (the gradient was negative). That is the whole algorithm: read the slope, step against it, re-read the slope.

**The same thing in PyTorch.** The demo notebook implements the rule with `torch.optim.SGD(model_pt.parameters(), lr=5e-4)`, and the printed loss sequence

```
epoch=0: loss=5910.3193359375
epoch=1: loss=1652.3736572265625
epoch=2: loss=465.6243896484375
epoch=3: loss=134.8601837158203
epoch=4: loss=42.671321868896484
epoch=5: loss=16.976774215698242
```

is twenty applications of $w^{(t+1)} = w^t - \alpha \nabla E(w^t)$ with $\alpha = 5 \times 10^{-4}$. The gradient itself is never written down: `loss.backward()` computes it by autograd and `optimizer.step()` applies the rule. That is the entire bridge between the slide's formula and the notebook's code.

## Common Pitfalls

- **Trying to solve a network's loss analytically.** The slides show why: the ReLU's `max(0, ·)` is not differentiable at zero, and the composition has no closed-form stationary point. Numerical optimisation is not a convenience here; it is the only option.
- **Confusing a stationary point with a minimum.** On a non-convex loss, $\nabla E = 0$ need not mean the optimum. The second-derivative test that works for $x^2 - 3x$ has no analogue in general.
- **Treating $\alpha$ as a formality.** It is the parameter that decides whether training converges, oscillates, or diverges, and the demo's learning-rate exercise exists because of it.
- **Reading the update rule with the wrong sign.** $w^{(t+1)} = w^t - \alpha \nabla E$ steps *against* the gradient; the minus sign is the descent.
- **Hand-deriving gradients.** The slides' instruction is explicit — "not computed by hand! → PyTorch". Long chain rules over deep networks are where students burn time and introduce errors.
- **Expecting convergence to a global optimum.** With tanh and ReLU, the loss is non-convex; gradient descent finds a stationary point, not necessarily the best one.
- **Running out of patience.** "Repeat until convergence or until the compute budget is exhausted" — a training run that plateaus above the noise floor may need a different learning rate, not more epochs.

## Connections

- [[neural-network-training-loop]] — the implementation: `optimizer.step()` applies exactly this rule, and the loop is where it is invoked.
- [[pytorch-tensors-and-autograd]] — the source of the gradients the rule consumes; the slides' "not computed by hand" instruction is autograd's reason for existing.
- [[linear-regression]] — the one case where the analytic route works: a closed form $w = (X^T X)^{-1} X^T y$ exists, and the demo contrasts it with the iterative one.
- [[feature-normalization]] — the learning rate only means something relative to the scale of the features; the demo's $x \in [10, 30)$ is a concrete case where scaling changes what $\alpha$ should be.
- [[linear-algebra-for-deep-learning]] — the gradient of a linear model with respect to its weights is the matrix algebra of week 1; the nonlinearity is what makes it iterative.
- [[polynomial-regression-and-overfitting]] — a case where the model is nonlinear in $x$ but still linear in $w$, so gradient descent applies and the closed form survives.
- [[deep-learning-course-roadmap]] — the lecture is a preview of weeks 3 and 4, where gradient descent and stochastic gradient descent are taken apart.

## Open Questions

- The slides use the sum of squared errors over $N$ points as the loss, but the demo notebook optimises `nn.MSELoss()`, which averages. Whether the learning rate needs rescaling when the loss changes from a sum to a mean — and how much — is not addressed in either source.
- The detour's $f(x) = x^2 - 3x$ is convex and has a single critical point. No example is given of what the analytic recipe looks like on a non-convex one-dimensional loss, which is where its limitations would be visible without a network.
- How the second-derivative test generalises to many-parameter losses — Hessian-based classification of critical points — is not raised, though it is the natural extension of the argument the slides make.
- The slides give the loss as a sum of squared errors for regression only. Whether classification losses admit a comparable interpretation as an objective to be minimised numerically is left to the weeks that cover loss functions.
