---
title: "Introduction to Deep Learning — Exercise 2: Introduction to PyTorch"
tags: [topic, deep-learning, semester-2, exercise, pytorch]
course: "Introduction to Deep Learning"
source_count: 3
status: current
last_updated: 2026-10-20
prerequisites: ["[[python-environment-management]]"]
---

## One-line Summary
The first week in which the course stops being about Python: PyTorch's tensors and autograd on
one side, the fact that a network's loss cannot be minimised on paper on the other.

## Core Map

```
Introduction to Deep Learning — Exercise 2 (22.10.2026)
│
├── Goal for this week
│   └── Write a training script for a simple neural network
│       ... and understand the basics of PyTorch
│
├── What PyTorch is
│   ├── NumPy-like tensor ops, GPU support
│   ├── Automatic differentiation engine
│   ├── NN components library
│   └── Optimization tools library
│       └── → [[pytorch-tensors-and-autograd]]
│
├── GPU support
│   ├── CPU: few cores, low latency, serial
│   ├── GPU: many cores (H100: 456 Tensor Cores), high throughput, parallel
│   └── NN ops are highly parallelizable → speedup up to 2 orders of magnitude
│
├── The detour: minimising functions analytically
│   ├── f(x) = x² − 3x: derivative → critical points → second derivative
│   ├── But a real network's loss is non-linear (activation functions)
│   └── ⇒ we need numerical methods
│       └── → [[gradient-descent-for-neural-networks]]
│
├── Gradient descent
│   ├── w(t+1) = w(t) − α · ∂f/∂w
│   └── "Next week: gradient descent in more detail"
│
└── The homework: polynomial regression
    ├── Degree q, linear in the weights
    ├── Overfitting vs. underfitting
    └── → [[polynomial-regression-and-overfitting]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[pytorch-tensors-and-autograd]] | Tensors, the computation graph, and why only leaf tensors carry gradients. |
| [[gradient-descent-for-neural-networks]] | The update rule, and why a network with activation functions cannot be minimised on paper. |
| [[neural-network-training-loop]] | Five steps: forward, loss, zero_grad, backward, step. |
| [[polynomial-regression-and-overfitting]] | Nonlinear in x, linear in w — and the first measured overfitting experiment of the course. |
| [[python-environment-management]] | The `uv` setup this session's homework builds on. |
| [[linear-algebra-for-deep-learning]] | The matrix arithmetic a dense layer does, from week 1. |
| [[jupyter-notebook-state]] | The notebook-state trap, from the same notebook family. |

## What the Session Actually Covers

**PyTorch, in four bullet points** (the slide repeats them across several animation frames):
similar to NumPy, a library for array (tensor) operations, with GPU support; an automatic
differentiation engine; a library of neural network components; a library of optimization tools.

**GPU support**, with the CPU/GPU comparison credited to Kevin Krewell (2009): a GPU is a
processor with many cores but a limited instruction set. A CPU has several cores, low latency,
is good for serial processing, and can do a handful of operations at once. A GPU has many cores
— the recent NVIDIA H100 has 456 "Tensor Cores" — high throughput, is good for parallel
processing, and can do thousands of operations at once. Neural network operations are highly
parallelizable; GPUs handle tens of thousands of concurrent threads, and Tensor Cores accelerate
large matrix operations.

**The detour.** The session teaches the analytic route to a minimum — for `f(x) = x² − 3x`,
compute the derivative, find all `x` where `f′(x) = 0`, use the second derivative to classify
each critical point as a minimum or a maximum. Then it breaks the route deliberately: for a real
network

```
f(W(1), W(2), b(1), b(2), x, y) = yᵀ tanh( W(2) max(0, W(1)x + b(1)) + b(2) )
```

the conclusion is that the **non-linearity from the activation functions** means we need
numerical methods.

**Why it matters.** Neural networks are functions with many parameters. The input `x` is fixed,
and during a forward pass the parameters are also fixed. Weights `W` and biases `b` are trained
to minimise a loss — for a regression problem, the sum of squared errors between prediction and
truth over the `N` training points. Gradient descent is a general method to approximate that
minimum, with `α` as the learning rate and the update rule

```
w(t+1) = w(t) − α · ∂f(w(t), …)/∂w
```

repeated until convergence or until the compute budget is exhausted. The slide's own emphasis:
we need the derivatives of the loss with respect to the parameters, **not computed by hand** —
PyTorch does that. And the honest scoping: *"Next week: gradient descent in more detail."*

**The homework** is the notebook `02-hw-intro-pytorch-tasks.ipynb`: implement a 1-D polynomial
regression model in PyTorch, train it with the five general training steps, and study how the
model's allowed complexity (the degree `q`) affects the fit. The companion demo notebook
`02-demo.ipynb` (66 cells) is the professor's own walkthrough of PyTorch, and the paper sheet
`02-homework.pdf` carries the math half: MML 2.4 matrix products, five derivative exercises,
and four probability exercises.

The full worked solution, with real output from a real PyTorch run, is in
`study/homework/introduction-to-deep-learning/exercise-02-solution.md`.

## Exam-Relevant Points

1. **The exam "may contain some coding."** This is the first session where that is concrete:
   the task is a `torch.nn.Module` subclass, a training loop, and a loss comparison. Expect
   `forward`, `nn.Module`, `requires_grad`, `backward`, `optimizer.step`.
2. **The five training steps are examinable as a sequence.** Forward, compute loss,
   `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`. The order is the point, and so
   is the reason `zero_grad` is there.
3. **Why a network cannot be minimised analytically** is the conceptual core: activation
   functions introduce non-linearity, so there is no closed form, so we differentiate
   automatically.
4. **The two-axis distinction that trips people:** backward computes gradients, it does *not*
   update parameters. Only `optimizer.step()` updates parameters.
5. **Polynomial regression is linear in the weights.** The model is nonlinear in `x` but linear in
   `w` — it is linear regression on the transformed features `(x, x², …, x^q)`. This is the
   single most exam-able sentence in the session.
6. **Overfitting is measured, not asserted.** The homework's own logic: a higher-degree model
   must reach a training loss at most as large as a lower-degree one, so a higher training loss
   means the optimisation has not converged. And a model that interpolates 10 training points
   exactly can still be the worst generaliser of the set.

## Connections

- [[introduction-to-deep-learning-exercise-1]] — last week's Python on-ramp; this session's
  `uv add torch matplotlib` extends that environment.
- [[python-environment-management]] — the `uv` project the homework runs inside.
- [[jupyter-notebook-state]] — the notebook-state trap, which bites again when you re-run cells
  with a random seed.
- [[linear-algebra-for-deep-learning]] — the matrix multiply a `nn.Linear` performs.
- [[linear-regression]] — the closed-form sibling, in the Machine Learning for Cybersecurity
  course. The NumPy least-squares demo in the PyTorch notebook is the same model solved
  analytically instead of by gradient descent.
- [[gradient-descent-for-neural-networks]] — the update rule from this session's slides.
- [[neural-network-training-loop]] — the five steps, in full.
- [[polynomial-regression-and-overfitting]] — the homework's subject.

## Open Questions

- The exercise-2 slides' first "Goal for this week" slide names the goal as writing a training
  script for a simple neural network and understanding the basics of PyTorch, but the actual
  homework is a polynomial regression model rather than a neural network in the strict sense. A
  single linear layer over polynomial basis functions is linear in its parameters, so it is a
  degenerate network. Whether the course intends it as a first neural network or as a deliberate
  warm-up before the MLPs of week 5 is not stated.
- The slides list three contributors — Prof. Dr. Florian Lemmerich, Andreas Einwiller, and Max
  Klabunde (2021–2025) — with the footnote "*(2021-2025) Preparation, creation, and
  presentation" applying to Klabunde. The demo notebook is partly based on the UvA Deep Learning
  course notebooks (`uvadlc-notebooks.readthedocs.io`). Whether the demo notebook's contents are original to this course or adapted from
  that source is not stated beyond the credit line.
- The slides' homework slide says "Reminder: uv setup + VS Code or Jupyter server" and "If you
  missed last week's session, complete the installation steps first" — so session 2 assumes
  session 1's environment is already working. No fallback instructions are given.
- The feedback slide points to a per-session form (`lgms.nl/p/presentation-feedback/?code=...`).
  Whether feedback is collected for every session, and whether the responses feed into the
  course, is not stated.
