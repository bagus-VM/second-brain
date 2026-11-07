---
title: "Computation Graphs and the Forward/Backward Pass"
tags: [concept, introduction-to-deep-learning, semester-2, autodiff]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[binary-cross-entropy]]", "the chain rule"]
---

## One-line Summary

A computation graph decomposes a loss into atomic assignments over input, parameter and compute
nodes; the forward pass evaluates it to get the loss, the backward pass walks it in reverse to get
every gradient by the chain rule, and dynamic programming (storing intermediates) is what makes
both cheap.

## Core Intuition

The lecture poses the problem it has just created: for logistic regression "luckily, here the
gradient is simple – but not for more complex models such as deep neural networks. How can we
efficiently compute gradients in the general case?" The answer is to stop differentiating the
model as a formula and start differentiating the *program* that computes it, one assignment at a
time.

Two ideas carry it. First, any computation can be written as a sequence of atomic assignments —
"we call this sequence of assignments a computation graph or source code". Second, the chain rule
applied along that sequence reuses intermediates: "both, the forward pass and the backward pass are
efficient due to the use of dynamic programming, i.e., storing and reusing intermediate results.
This decomposition and reuse of computation is key to the success of the backpropagation algorithm,
the primary workhorse of deep learning."

## Formal Definition / Statement

**Node types.** "A computation graph has three kinds of nodes: input nodes, parameter nodes,
compute nodes."

**Linear regression as a graph** — the lecture's canonical example, with (x, y) inputs, w₀ and w₁
parameters:

(1) u = w₁x
(2) ŷ = w₀ + u
(3) z = ŷ − y
(4) L = z²

**Levels of granularity.** "Same function as before but different graph": the coarser
(1) ŷ = w₀ + w₁x, (2) z = ŷ − y, (3) L = z²; and coarser still: (1) ŷ = w₀ + w₁x,
(2) L = (ŷ − y)². Granularity is a design decision — it fixes how many partial derivatives the
backward pass must know.

**Logistic regression as a graph**: (1) u = wᵀx, (2) ŷ = σ(u), (3)
L = −y log ŷ − (1 − y) log(1 − ŷ).

**The two passes.** "The forward pass takes a training point (x, y) as input and computes a loss,
e.g. L = −log p_model(y | x, w)." "As we will see, gradients ∇_w L can be computed using a backward
pass." "Forward: top to bottom of the assignments; backward: in reverse order, reusing stored
values."

## Key Properties

**The backward pass is the chain rule applied node by node, and the numbers are checkable.** The
lecture works the linear-regression graph with x = 2, y = 3, w₀ = 1, w₁ = 0.5:

| Node | Forward (values) | Backward (gradients) |
|---|---|---|
| L = z² | L = 1 | ∂L/∂L = 1 |
| z = ŷ − y | z = −1 | ∂L/∂z = 2z = −2 |
| ŷ = w₀ + u | ŷ = 2 | ∂L/∂ŷ = ∂L/∂z·1 = −2 |
| u = w₁x | u = 1 | ∂L/∂u = ∂L/∂ŷ·1 = −2 |
| w₀, w₁ | — | ∂L/∂w₀ = −2, ∂L/∂w₁ = ∂L/∂u·x = −4 |

**Every stored forward value is reused exactly once.** z = −1 is needed for ∂L/∂z, ŷ = 2 and
y = 3 for z, x = 2 for ∂L/∂w₁. That is what "dynamic programming" means here: no recomputation, no
symbolic expansion.

**Autograd is the same thing implemented.** The PyTorch snippet on the same slide:

```python
import torch
x, y = torch.tensor(2.0), torch.tensor(3.0)
w0 = torch.tensor(1.0, requires_grad=True)
w1 = torch.tensor(0.5, requires_grad=True)

u = w1 * x          # forward pass:
y_hat = w0 + u      # builds the graph
z = y_hat - y
loss = z ** 2

loss.backward()     # backward pass
print(w0.grad, w1.grad)
# tensor(-2.) tensor(-4.)
```

"PyTorch records the computation graph during the forward pass; backward() computes all gradients
automatically; same numbers as on the previous slide."

**The gradient's independence from the loss scale is visible in the table.** ∂L/∂w₀ = −2 and
∂L/∂w₁ = −4 differ by exactly x = 2 — the same structure as (ŷ − y)x in both the regression and
the cross-entropy case.

**Granularity trades generality against cost.** The finest graph needs derivatives of only trivial
operations (+, −, ·, square, σ), which is why an autodiff system can supply them; a coarse graph
needs a hand-derived derivative per node but has fewer nodes.

## Worked Example

**Recompute the lecture's table by hand, in full, to see why the order matters.**

Forward: u = w₁·x = 0.5·2 = 1; ŷ = w₀ + u = 1 + 1 = 2; z = ŷ − y = 2 − 3 = −1; L = z² = 1.

Backward, starting from ∂L/∂L = 1 and moving up the assignment list:

1. L = z² ⇒ ∂L/∂z = 2z = 2·(−1) = −2.
2. z = ŷ − y ⇒ ∂z/∂ŷ = 1 and ∂z/∂y = −1, so ∂L/∂ŷ = −2·1 = −2.
3. ŷ = w₀ + u ⇒ ∂ŷ/∂w₀ = 1 and ∂ŷ/∂u = 1, so ∂L/∂w₀ = −2 and ∂L/∂u = −2.
4. u = w₁x ⇒ ∂u/∂w₁ = x = 2, so ∂L/∂w₁ = −2·2 = −4.

Everything matches the slide's table, and the check is a single gradient step: with α = 0.1 the
update w₀ ← 1 − 0.1·(−2) = 1.2 and w₁ ← 0.5 − 0.1·(−4) = 0.9 lowers L from 1 to
(1.2 + 0.9·2 − 3)² = (0)² = 0 — the two-point problem is solved by one exact step, which is a
coincidence of this instance, not a general property.

**Why the reverse order is required.** To get ∂L/∂w₁ you need ∂L/∂u, which needs ∂L/∂ŷ, which
needs ∂L/∂z. Computing in forward order would recompute the tail three times; computing in reverse
order visits each node once, given that the forward values were stored.

## Common Pitfalls

- **Forgetting to store forward values.** The backward pass needs z, ŷ, u; a graph that discards
  them must recompute, which turns O(nodes) into O(nodes²).
- **Not zeroing gradients between iterations in PyTorch.** Autograd accumulates into `.grad`; the
  snippet works because it runs once.
- **Confusing "dynamic" with "rebuilt by hand".** PyTorch builds the graph on every forward call, so
  control flow (if, loops) is part of the graph — which is what makes the notebook's "dynamic graph"
  remark true.
- **Assuming a node's derivative is the whole story.** Each node contributes a local derivative; the
  chain rule multiplies it by the upstream gradient — sign errors here are the classic bug.
- **Treating the two parameter gradients as symmetric.** ∂L/∂w₁ includes the factor x; without it the
  bias and the weight would receive identical updates.
- **Believing backprop is a different algorithm from gradient descent.** It is gradient descent with
  the gradient computed efficiently.

## Connections

- [[pytorch-tensors-and-autograd]] — the same mechanism from the exercise-notebook side, including
  the dynamic-graph remark.
- [[binary-cross-entropy]] — its "not for more complex models" gradient is the motivation for this
  page.
- [[activation-functions]] — σ′ = σ(1 − σ) is the local derivative the logistic graph needs.
- [[gradient-descent-for-neural-networks]] — the update rule that consumes the gradients computed
  here.
- [[introduction-to-deep-learning-lecture-3]] — section 3.5, and the preview of lecture 4's
  backpropagation.
- [[neural-network-training-loop]] — where the two passes sit inside an epoch.

## Open Questions

- **The backward pass is explicitly a preview** — "→ lecture 4" — so the general algorithm
  (including how a node with several consumers sums its gradients) is not derived here.
- **The dynamic-programming argument is asserted**: no complexity comparison between stored-value
  and recompute variants is given.
- **Nothing is said about memory cost**, which is the practical limit of storing every intermediate
  in a deep network.
- **The graph granularity slides show three graphs for the same function without saying which is
  preferable**, or how an autodiff system chooses.
- **Reverse-mode vs forward-mode differentiation is never named**, so the reason backprop is
  efficient for "many parameters, one loss" does not appear in this material.