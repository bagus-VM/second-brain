---
title: "Support Vector Machines"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, classification]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[linear-algebra-for-deep-learning]]"]
---

## One-line Summary
Of all the hyperplanes that separate two classes, take the one with the widest margin to the closest
points — and if no hyperplane can do it, map the data into a higher-dimensional space where one can.

## Core Intuition

For linearly separable data there is never one separating line; there is an infinite family, and
almost all of them are arbitrarily close to some training point. That is the instability the SVM
removes: instead of any separating hyperplane, take the one that is as far as possible from the
nearest instance of either class. Moving the boundary in either direction would immediately
misclassify something, so the solution is pinned down by geometry rather than by the optimiser's
starting point.

The instances that touch that boundary are the **support vectors** — the circled points on the slide's
figure — and they are the only training points that determine the solution. Everything further away
could be deleted without changing the answer. That is an unusual and useful property: the model's
complexity is set by the hard cases near the boundary, not by the easy majority.

Two extensions make the method usable on real data. **Soft margin** with slack variables lets a few
points sit inside the margin or on the wrong side, at a price — necessary because real data is rarely
cleanly separable, and a hard margin would simply fail. **Kernels** replace an explicit
high-dimensional mapping with a similarity function, so a linear boundary in the mapped space becomes
a non-linear boundary in the original one. This is the lecture's bridge to deep learning: change the
representation, and a linear method becomes capable.

## Formal Definition / Statement

**Slide 27, as given:** data points in **d-dimensional space**; find the separating hyperplane with
the maximal distance to the closest instances — **the margin**. Those closest instances are the
**support vectors**, circled on the slide's figure. The slide adds: "Dotted line: also separates the
classes, but with a smaller margin."

**Measuring the margin.** For a hyperplane `w^T x + b = 0`, the perpendicular distance of a point `x`
is `|w^T x + b| / ||w||`. With the usual convention that the support vectors satisfy
`|w^T x + b| = 1`, the distance from the hyperplane to each support vector is `1/||w||`, so the total
margin **width** is

```
width = 2 / ||w||
```

Maximising the margin therefore means minimising `||w||` subject to every point being on the correct
side and outside the margin. The slide states the objective in this form — its formula fragment
reads "arg min" over the margin's parameters, with the margin annotated.

**Extension 1 — kernels (nonlinear boundary).** "Kernel methods: implicit mapping into a
higher-dimensional space → nonlinear boundaries." The map is never performed explicitly; only inner
products in the new space are needed, which is what makes it tractable.

**Extension 2 — soft margin (slack variables).** "Penalty for instances inside the margin or on the
wrong side." This converts an infeasible hard-margin problem into a feasible one with a cost.

## Key Properties

- **The solution depends only on the support vectors.** Points far from the boundary do not affect the
  hyperplane at all.
- **Maximum margin is a stability argument, not just an aesthetic one.** The widest-margin separator
  moves the least when a training point moves slightly, unlike any of the other separating
  hyperplanes.
- **The margin width is `2/||w||`**, so the optimisation is over the norm of `w` and the margin scales
  inversely with it.
- **A linear SVM cannot separate XOR-like data.** That is exactly what the kernel extension exists for.
- **The kernel trick trades explicit coordinates for inner products**, so the cost does not necessarily
  grow with the dimension of the mapped space.
- **Slack variables are a deliberate concession.** Hard margins assume separable data; soft margins
  accept violations and pay for them.
- **SVMs are in the classical-methods section** — the lecture presents them as one of six methods, in
  the same breath as k-NN and logistic regression, not as a deep-learning component.
- **Capacity control has two knobs**: the kernel and its parameters, and the penalty for slack. Neither
  is discussed in the slides beyond being named.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 6. Four
points in 2-D:

```
positive class: (1,1), (2,2)
negative class: (4,1), (5,2)
```

Four candidate hyperplanes, with each one's minimum perpendicular distance to a training point and
its margin width `2/||w||`:

| Hyperplane | Separates? | Margin | Width `2/||w||` |
|------------|-----------|--------|-----------------|
| `x - 3 = 0` (vertical, midway) | yes | **1.0000** | **2.0000** |
| `2x - 7 = 0` (vertical, shifted right) | yes | 0.5000 | 1.0000 |
| `x + 0.5y - 4 = 0` (tilted) | yes | 0.4472 | 0.8944 |
| `x + y - 5 = 0` (45°) | yes, but touching | 0.0000 | — |

All four separate the classes, and they are not equally good. The vertical line through the midpoint
`x = 3` wins with a margin of 1 and a width of 2 — which is exactly the 2 units of empty space
between the rightmost positive point (2,2) and the leftmost negative point (4,1). Tilting the line
costs more than half the margin (0.4472), and shifting it right cuts the margin in half. The 45° line
passes through the point (4,1), so its margin is zero: separated, but with no room for a new point to
land anywhere near the boundary.

**The support vectors of the winner are (2,2) and (4,1)** — the two points that sit exactly on the
margin at distance 1. The points (1,1) and (5,2) are at distance 2 and 1.5 respectively, and could be
moved further away without changing the hyperplane. That is the property worth remembering: four
training points, two of which matter.

## Common Pitfalls

- **Thinking "a separating hyperplane" is unique when it is not.** The entire method is a rule for
  choosing among many.
- **Confusing margin (distance) with margin width.** The slide's "maximal distance to the closest
  instances" is the half-width; the width is twice that, and is `2/||w||`.
- **Forgetting that scaling `w` rescales the distance formula.** The constraint `|w^T x + b| = 1` on
  the support vectors is a normalisation convention, not a property of the data.
- **Assuming every training point matters.** Only the support vectors do, which is why the method can
  be written in terms of inner products and therefore kernelised.
- **Expecting a hard margin to work on real data.** With overlapping classes it is infeasible; the
  slack variables exist for that reason.
- **Reading kernels as "more dimensions is better".** The kernel replaces an explicit mapping; whether
  the resulting boundary is better still depends on the kernel and its parameters.
- **Treating the SVM as a probabilistic classifier.** It outputs a decision function, not a
  probability; the lecture's soft-classification and calibration material does not automatically
  apply to it.
- **Assuming a linear SVM can handle any dataset.** XOR is the standard counterexample, and it is a
  two-dimensional one.

## Connections

- [[linear-algebra-for-deep-learning]] — hyperplanes, inner products and norms, which is the whole
  vocabulary of this page.
- [[linear-regression]] and [[logistic-regression]] — the other linear models in the same section, and
  the contrast: they fit a loss to all points, the SVM is determined by the boundary cases.
- [[k-nearest-neighbors]] — distance-based, no explicit boundary; the SVM's mirror image in the
  classical catalogue.
- [[representation-learning]] — the kernel extension is a hand-designed change of representation; the
  deep-learning version learns it, which is the course's overall arc.
- [[decision-trees]] — the other non-linear classical model in the lecture, non-linear by construction
  rather than by a kernel.
- [[ensemble-learning]] — SVMs also appear as ensemble components, though the lecture's ensembles are
  tree-based.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **The optimisation problem is not stated fully.** The slide shows a formula fragment ("arg min" over
  the margin) and a maximum-margin figure; the constraints, the dual formulation and the reason the
  kernel trick works are outside the lecture.
- **No kernel is named.** RBF, polynomial and linear kernels are not mentioned, nor is how to choose
  one.
- **The slack penalty is not defined.** "Penalty for instances inside the margin or on the wrong side"
  is the entire treatment; the regularisation constant that trades margin against slack is not named.
- **Multiclass SVMs are not discussed**, though the lecture's task taxonomy includes multiclass and
  multi-label classification.
- **No calibration statement**, so an SVM's output cannot be compared with the slide-14 confidence
  discussion without further machinery.
- **The worked example above is this vault's own** — the slide provides a figure and a formula
  fragment, not an example with numbers.