---
title: "Decision Trees"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, classification]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[ml-task-taxonomy]]"]
---

## One-line Summary
Ask one attribute at a time, greedily from the top, and let the leaves carry the class labels — a
model you can read out loud, and the base learner that the ensemble methods later in the lecture
multiply.

## Core Intuition

Every other method in the lecture's catalogue constructs a numeric object: a distance, a hyperplane,
a weight vector. A decision tree constructs a *procedure*. Each internal node asks about one
attribute, each branch follows one answer, and each leaf delivers a class. Predicting is walking down
the tree with the instance's values, and nothing has to be computed at prediction time beyond
comparisons.

That structure buys interpretability for free — you can print the tree and a domain expert can argue
with it. It also fits mixed data without any numeric encoding: "Car type = Truck" and "Age > 60" sit
in the same tree, which is awkward for a linear model.

The cost is that the learning procedure is greedy. The lecture says Greedy top-to-bottom and stops
there: at each node, pick the attribute that splits best, recurse, never revisit. There is no
backtracking, so a locally reasonable split that blocks a better tree below it is never undone. This
is the same compromise as the ensembles that follow: many slightly different greedy trees, voted
together, is precisely the answer to one greedy tree being unstable.

## Formal Definition / Statement

**Slide 26, structure as stated:**

- Each **inner node** is an attribute.
- Each **edge** is a value (range) of its source node.
- Each **leaf node** is a class label.

**Learning:** greedy, top-to-bottom.

**Prediction:** "Follow the tree from top-to-bottom based on instance values."

**The slide's example tree**, on the slide's table of five instances:

```
                     Car type
                    /        \
              = Truck        != Truck
                /                \
          Risk = low            Age
                              /      \
                        > 60          <= 60
                        /                \
                 Risk = low            Risk = high
```

| ID | Age | Car type | Risk |
|----|-----|----------|------|
| 1 | 23 | Family | high |
| 2 | 17 | Sport | high |
| 3 | 43 | Sport | high |
| 4 | 68 | Family | low |
| 5 | 32 | Truck | low |

## Key Properties

- **The model is the tree, and the tree is readable.** Feature importance, thresholds and interactions
  are all visible without a post-hoc explanation method.
- **Prediction is a walk, not a computation.** Cost is the depth, and the same comparisons apply to
  every instance that reaches them.
- **Learning is greedy and local.** No global search, no pruning in the lecture's account, no
  revisiting of earlier splits.
- **No numeric encoding is required for categorical features**, unlike distance-based or linear
  methods.
- **Comparison-based tests are the default**: the slide's own tree splits Age at 60 with an
  inequality.
- **A tree can express interactions natively.** "Truck → low, otherwise look at age" is an
  interaction between Car type and Age with no cross-term needed.
- **Trees are unstable.** A different sample gives a different greedy sequence, which is why they are
  the base learner for bagging in [[ensemble-learning]].
- **Capacity is controlled by depth**, which is the hyperparameter in the classical overfitting sense.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 5.

Tracing all five rows through the slide's tree:

| ID | Car type | Age | Tree path | Prediction | Actual |
|----|----------|-----|-----------|------------|--------|
| 1 | Family | 23 | not Truck → Age ≤ 60 | high | high ✓ |
| 2 | Sport | 17 | not Truck → Age ≤ 60 | high | high ✓ |
| 3 | Sport | 43 | not Truck → Age ≤ 60 | high | high ✓ |
| 4 | Family | 68 | not Truck → Age > 60 | low | low ✓ |
| 5 | Truck | 32 | Truck | low | low ✓ |

**Training accuracy: 5/5 = 1.00.**

**Is it the smallest consistent tree?** No. A single split on Age alone reproduces all five labels:

```
Age > 60  ->  low
Age <= 60 ->  high
```

That stump gives 5/5 as well, using **one attribute and one threshold** instead of two attributes and
two thresholds. The slide's tree is consistent and correct, but it is not minimal — and this is a
general lesson rather than a quirk of the example: greedy construction cannot notice after the fact
that a subtree was unnecessary, and on a showcase table with five rows there are usually several
perfectly consistent trees of different sizes.

It also shows why the lecture's description of the learning procedure is incomplete: with no splitting
criterion given, nothing in the slide's account would prefer the Age-only stump over the Car-type-first
tree, or vice versa. Both have zero training error.

## Common Pitfalls

- **Assuming greedy means optimal.** Greedy top-to-bottom never undoes a split; a locally good split
  can prevent a better tree below it.
- **Assuming the first split is the most informative attribute.** In the example above the Age stump
  alone suffices, yet the slide's tree starts with Car type.
- **Confusing nodes and leaves.** Inner nodes test attributes; leaves carry labels. A "leaf attribute"
  anywhere in the lecture's description is a category error.
- **Forgetting the edge labels are *values or ranges*.** The slide's edges are "= Truck" and
  "!= Truck", then "> 60" and "<= 60" — two different kinds of test in one tree.
- **Treating a perfectly consistent tree on five rows as evidence of a good model.** Training
  accuracy 1.00 on five instances says almost nothing; see [[polynomial-regression-and-overfitting]]
  for the general shape of that mistake.
- **Forgetting that the lecture gives no splitting criterion.** Anyone arriving from another course
  will look for information gain or Gini; the slide's account has neither.
- **Using an unpruned deep tree and calling its accuracy an estimate.** Depth is capacity, and the
  validation material of the same lecture applies.

## Connections

- [[ensemble-learning]] — random forests and gradient boosting are built from exactly these trees;
  [[ensemble-learning]]'s bagging description ("choose from a subset of attributes at each node") is
  this page's greedy procedure run with a random restriction.
- [[k-nearest-neighbors]] — the opposite inductive bias: no model at all, all structure in the
  distance and the training set.
- [[ml-task-taxonomy]] — the classification framing whose output a leaf produces.
- [[classification-metrics]] — how a tree's predictions are scored.
- [[polynomial-regression-and-overfitting]] — capacity and generalisation, the frame in which tree
  depth becomes a hyperparameter.
- [[cross-validation]] — how tree depth would actually be chosen (the lecture does not say).
- [[ml-for-security-domains]] — where tree models are common because the explanation can be read.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **No splitting criterion is given.** Entropy, information gain, Gini impurity, and even a
  description of how "best split" is judged are absent. The slide shows structure, learning and
  prediction and nothing about the inner loop.
- **No stopping rule, depth limit or pruning is mentioned.** How the greedy recursion terminates is
  not stated.
- **Numeric attributes are split with inequalities but no threshold search is described** — the slide
  prints `> 60` and `<= 60` without saying where 60 came from.
- **Missing values are not addressed**, although the bot-detection table elsewhere in the lecture is
  full of them.
- **The example table cannot distinguish the slide's tree from a simpler one** (shown in the worked
  example), so the example does not demonstrate that the extra split is needed.