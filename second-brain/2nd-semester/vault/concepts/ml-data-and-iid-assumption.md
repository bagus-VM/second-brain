---
title: "ML Data and the i.i.d. Assumption"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, evaluation]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: []
---

## One-line Summary
A row is an instance and a column is a feature, and every guarantee the course makes about a
model's performance rests on the rows being independent of each other and drawn from the same
distribution — an assumption that real data violates routinely.

## Core Intuition

Almost every formula in machine learning is written as a sum over `n` examples divided by `n`,
which is only an estimate of anything if the examples are a fair sample of the population the model
will meet in production. The lecture states the assumption once, in a parenthesis, and then spends
the evaluation section showing what happens when it fails.

The two halves of i.i.d. fail differently. **Independence** fails when one row tells you something
about another — several scans from the same patient, several sessions from the same user. Then a
random train/test split puts the same entity on both sides and the model is scored on records it
has effectively already seen. **Identical distribution** fails when the world moves: bots change
their behaviour, new browsers appear, the population that arrives next month is not the population
in the training file. The model does not become wrong; the *estimate* of how good it is becomes
wrong, which is worse, because nothing announces it.

The lecture's response is concrete and worth remembering as two instructions: split by time or by
group, and monitor after deployment.

## Formal Definition / Statement

**Terminology, from slide 6.**

- A **row** is a data **instance** (also: sample, example). It describes all the known properties of
  one entity. Rows "should be independent of each other (and come from the same distribution →
  i.i.d. assumption)".
- A **column** is a **feature** (sometimes attribute, or property). It gives information on one
  property for all instances. Columns **can** be dependent on each other — the independence
  requirement is on rows, not on features.

**Notation, from slide 7.**

```
D = {(x_1, y_1), ..., (x_n, y_n)}      dataset with n instances
x_i = (x_i1, ..., x_id)                 feature vector of instance i, d features
y_i                                     label / target of instance i (class or number)
f_w                                     model with parameters w
y_hat_i = f_w(x_i)                      prediction
l(y_hat_i, y_i)                         loss of a single prediction
```

Bot example: x_1 = (Windows, Chrome, .de, 17, 4), y_1 = Yes, n = 15, d = 5.

**Violations, from slide 40.**

| Violation | What it looks like | Consequence |
|-----------|--------------------|-------------|
| **Temporal shift** | bots change their behaviour over time | the model gets worse |
| **Covariate shift** | new browsers or email domains that never occurred in training | the model has no basis for those rows |
| **Dependent instances** | several rows per user or per patient | train/test splitting leaks identity |

**Consequences for evaluation (the slide's own prescription):** split by time (train on the past,
test on the future) or by group (user, patient); and monitor models after deployment.

## Key Properties

- **Independence is about rows; features are allowed to be dependent.** Confusing the two is a
  common misreading of the notation.
- **The assumption is what makes a held-out score an estimate of future performance.** Where it
  fails, the score estimates performance on the *old* distribution, not the future one.
- **Temporal and covariate shift degrade differently.** Temporal shift makes old patterns stale;
  covariate shift presents inputs the model never saw, so its behaviour on them is unconstrained
  rather than merely outdated.
- **Grouped data is a splitting problem, not a modelling problem.** The model may be fine; the
  random split is what is wrong.
- **Accuracy can improve while the model gets worse.** If the positive rate falls, a do-nothing
  classifier gains accuracy for free — see the worked example.
- **Monitoring is part of the method**, not operations. The lecture names it as the response to
  distribution shift.
- **The assumption is stated once and used everywhere**: cross-validation folds, validation
  splits, and the interpretation of every metric in the lecture's last section.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`.

Take one simple rule induced from the slide's bot table: **"posts per day above 100 → bot"**. On the
15 labelled rows it scores 13/15 = **0.8667**, and it catches 1 of the 3 bots (recall 0.3333).

Now serve it a later batch of 15 registrations drawn from a shifted population — new TLDs, and the
bot base rate down from 3/15 = 0.2000 to 1/15 = 0.0667:

| Quantity | Training rows | Shifted batch |
|----------|---------------|---------------|
| Accuracy of the rule | 13/15 = 0.8667 | 14/15 = **0.9333** |
| Recall of bots | 1/3 = 0.3333 | 0/1 = **0.0000** |
| Accuracy of "never a bot" | 12/15 = 0.8000 | 14/15 = **0.9333** |

Three things are worth reading off that table:

1. **The headline metric improved.** 0.8667 → 0.9333. A dashboard would show progress.
2. **The model stopped working.** Recall went from a third to nothing: on this batch it identifies no
   bot at all.
3. **It became indistinguishable from doing nothing.** The rule and the trivial classifier now both
   score 0.9333, because the base rate moved the floor up.

That is covariate shift plus class-imbalance drift in one number — and it is exactly why a score
computed on the training distribution cannot be trusted on a shifted one.

## Common Pitfalls

- **Splitting randomly when rows belong to groups.** Several scans per patient split randomly means
  the same patient is on both sides, and the score measures memorisation of that patient.
- **Splitting randomly when the data has time order.** The model then trains on the future. Split by
  time: train on the past, test on the future.
- **Reading the i.i.d. assumption as a claim about features.** The lecture's own wording restricts it
  to rows.
- **Treating a stable accuracy number as evidence of a working model.** Accuracy is a function of the
  base rate; the worked example above shows it rising while recall collapses.
- **Assuming that retraining on newer data is enough.** Covariate shift means the *inputs* are new;
  more data of the old kind does not cover them.
- **Forgetting that "monitor after deployment" needs a definition of the monitored quantity**,
  which the slide does not provide.
- **Using cross-validation without asking whether the folds respect the grouping or the time order.**
  See [[cross-validation]] for why stratified or grouped folds exist.

## Connections

- [[ml-task-taxonomy]] — the tasks that operate on these rows and columns.
- [[cross-validation]] — the procedure whose validity depends on this assumption, and the reason
  grouped and time-ordered folds exist.
- [[information-leakage]] — the failure mode that grouped data produces when the split ignores the
  grouping.
- [[class-imbalance]] — the reason a changing base rate moves the accuracy floor.
- [[feature-normalization]] — preprocessing that must be fitted on training rows only, because
  fitting it on all rows leaks information across the split.
- [[ml-pipeline-scikit-learn]] — where the split and the preprocessing order are enforced in code.
- [[threats-to-validity]] — the Mining Software Repositories course's treatment of the same question:
  when does a measured result not mean what it appears to mean.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **How much shift is too much is not quantified.** The lecture says to split by time or group and to
  monitor; it gives no threshold, no drift-detection method, and no retraining policy.
- **Slide 40 asserts the consequences for evaluation but gives no example.** The worked example above
  is constructed from the lecture's own table, not from the slides.
- **No statement about label shift** (the label distribution changing while the features do not),
  which is the mechanism behind the accuracy improvement in the worked example.
- **The i.i.d. assumption is stated in a parenthesis on slide 6** and never revisited as a formal
  assumption, so there is no statement of what the guarantees look like when it holds only
  approximately.