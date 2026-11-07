---
title: "Stochastic and Mini-Batch Gradient Descent"
tags: [concept, introduction-to-deep-learning, semester-2, optimisation]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-11-07
prerequisites: ["[[gradient-descent-for-neural-networks]]"]
---

## One-line Summary

Instead of summing the gradient over all n training examples per update, estimate it from one
random example (SGD) or a small batch (mini-batch) — cheaper per update, noisier per step, and
better at escaping saddle points and finding flat minima.

## Core Intuition

"Computing the gradient requires a sum over all instances → can be slow for large datasets."
Everything else follows from relaxing that sum. Take one example and you get an unbiased but noisy
estimate for the price of one gradient; take 32 and you get a much better estimate for the price of
32, which on a GPU is nearly the price of one.

The noise is the interesting part, and the lecture refuses to treat it as a defect: "Mini-batch
gradients are noisy estimates of the true gradient – but: cheap; redundancy; escaping; 
generalization." The four justifications are the substance of the concept, not an afterthought.

## Formal Definition / Statement

**The procedure**, as the slide states it:

"While not converged or maximum_iterations_reached:
- draw random batch from training set
- compute the approximated gradient ∇f(wₜ) with the batch
- new parameters wₜ₊₁ = wₜ − α∇f(wₜ) (learning rate α)"

**The three points on the spectrum** are named explicitly: full-batch gradient descent (all n),
mini-batch (a small subset), and stochastic (one example) — "approximate the gradient with just one
random example. More often: mini-batch: use a small subset of instances, and compute the
error/gradient for those instances."

**The vocabulary:**

- **Batch size** is "a hyperparameter — determines how many training examples you look at until you
  update your parameters (weights w). Often limited by available memory (GPU/CPU limits); typical:
  16 … 512 (powers of 2)."
- **Epoch:** "a complete pass over the training data (each example used once)"; the number of epochs
  is "a hyperparameter, dependent on task/data".
- **Iteration (step):** "one parameter update = one mini-batch."

**The lecture's quiz** makes the arithmetic explicit: "n = 10 000 training examples, batch size 32:
how many updates per epoch?" — "⌈10 000/32⌉ = 313 updates (312 full batches + one batch of 16) —
with full-batch GD it would be 1 update." (Computed: ⌈10000/32⌉ = ⌈312.5⌉ = 313.)

## Key Properties

**The four reasons the noise helps**, in the lecture's own order:

1. **Cheap:** "cost per update independent of n → many more updates per epoch."
2. **Redundancy:** "large datasets contain many similar examples; a small batch already points in a
   good direction."
3. **Escaping:** "noise helps to leave saddle points and flat regions."
4. **Generalization:** "small-batch SGD tends to find 'flat' minima that generalize better (implicit
   regularization)" — citing Keskar et al., *On Large-Batch Training for Deep Learning:
   Generalization Gap and Sharp Minima*, ICLR 2017.

**The noise has a cost that must be paid at the end.** "Near the end of training, the noise prevents
exact convergence → reduce the learning rate." This is the first appearance of a learning-rate
schedule in the course; the outlook slide names "momentum-based algorithms, RMSProp, Adam" as
"improvements on this algorithm".

**Batch size is a memory decision before it is a statistical one.** The slide gives the practical
range (16 … 512, powers of 2) and the constraint ("often limited by available memory") rather than a
rule for choosing it.

**The comparison plot fixes the budget, not the batch size.** "40 updates each" for batch GD, mini-
batch GD (32) and stochastic GD (1), on 500 synthetic points for linear regression, "same start and
learning rate for all three" — which is the only honest way to compare them, and shows full-batch GD
taking 40 steps that each cost 500 gradient evaluations.

## Worked Example

**The lecture's quiz, computed and read.** n = 10 000, batch = 32 ⇒ 313 updates per epoch; with
full-batch GD an epoch is a single update over all 10 000 examples.

The cost per epoch, in example-gradients: 313 × 32 = 10 016 (one batch of 16 at the end), i.e. one
pass over the data — the same total work as one full-batch step, but distributed over 313 parameter
updates. If the optimiser needs ~100 updates to reach a given loss, mini-batch needs a third of an
epoch while full-batch needs 100 epochs. That asymmetry is the whole argument.

**The "40 updates each" experiment**, in the same currency: full-batch spends 40 × 500 = 20 000
example-gradients; mini-batch(32) spends 40 × 32 = 1 280; stochastic spends 40. So on the plot, the
three curves after 40 updates have cost 500×, 32× and 1× the data pass — the comparison favours the
noisy methods precisely because it is drawn against updates, and the slide is honest about which
axis it uses.

## Common Pitfalls

- **Reporting the number of epochs without the batch size.** An epoch is a data pass; the number of
  parameter updates is n/batch, so two runs with the same epochs and different batches are different
  experiments.
- **Comparing methods on iterations instead of evaluations.** Mini-batch does more updates per unit
  of work; a table of "updates to converge" without cost is misleading (the lab in the SBSE course
  makes exactly this point about evaluation budgets).
- **Expecting convergence to a point.** The noise keeps the iterates moving; either decay α or
  accept a noise floor.
- **Treating a small batch as a free approximation.** At batch = 1 the gradient variance is highest,
  and the "redundancy" argument that saves small batches depends on the dataset actually being
  redundant.
- **Assuming larger batches train better.** They give a better gradient estimate and, per Keskar et
  al., often a sharper minimum with worse generalisation.
- **Confusing batch size with learning rate scaling.** The lecture does not discuss scaling α with
  the batch size; that is a later concern.

## Connections

- [[gradient-descent-for-neural-networks]] — the parent procedure and the update rule.
- [[gradient-descent-step-mechanics]] — the learning-rate behaviour that the batching sits on top of.
- [[neural-network-training-loop]] — the epoch/batch loop in code (exercise 2's notebook).
- [[pytorch-tensors-and-autograd]] — how the per-batch gradient is actually obtained.
- [[introduction-to-deep-learning-lecture-3]] — section 3.2 of the lecture.
- [[double-descent]] — the neighbouring phenomenon about generalisation and capacity, from lecture 2.
- [[search-algorithm-evaluation]] — the SBSE course's rule that comparisons must share a budget;
  the same principle applies to "updates versus evaluations" here.

## Open Questions

- **The Keskar et al. citation supports "flat minima generalise better"** but the slides do not say
  whether it is examinable, and no number or experiment from the paper is reproduced.
- **No guidance on how to choose the batch size** beyond the memory constraint and powers of two.
- **"Reduce the learning rate near the end" is a directive without a schedule** — decay, step, or
  warm-up are all deferred to a later lecture.
- **The saddle-point escape claim is asserted**; the lecture does not demonstrate it, and it is
  contested in the literature for reasons the slides do not mention.
- **Whether the 40-update comparison is fair at all** is left implicit: the three curves have very
  different data costs, which the slide shows but does not comment on.