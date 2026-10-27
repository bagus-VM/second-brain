---
title: "Cross-Validation"
tags: [concept, introduction-to-deep-learning, semester-2, evaluation, machine-learning]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[ml-data-and-iid-assumption]]"]
---

## One-line Summary
One train/test split gives one noisy number; k-fold cross-validation rotates which fold is held out,
scores k times, and averages — so the estimate stops depending on which examples happened to land in
the test set.

## Core Intuition

The reason to hold data back at all is that a model's error on the data it was fitted to is
optimistic: the model has already seen those answers. So you keep a test set the model never touches.

But a single split answers a slightly different question than the one you asked. "How good is this
model?" becomes "how good is this model *on these particular 30 % of rows*", and with a small
dataset that number moves a lot depending on which rows you picked. Two runs of the same experiment
with a different random seed can disagree by several points, and neither is wrong.

Cross-validation replaces the single sample with an average over k samples that together use every
row exactly once. Every instance is tested exactly once and trained on k−1 times, so no data is
wasted and the estimate is an average rather than a draw.

The lecture is careful about what this costs and when to skip it: cross-validation is worth it when
data is limited and training is cheap, and it is rarely used for large deep networks, where the
training cost dominates and a single split is accurate enough because the test set is already big.

## Formal Definition / Statement

**Train-and-test (slide 34).** Split the labelled data into two subsets, e.g. 70 % / 30 %:

1. the **training set** is used to learn the classifier;
2. the **test set** is used to evaluate it.

**Three-way split (slide 35).** Split into training, validation and test data:

| Split | Purpose | Touched how often |
|-------|---------|-------------------|
| Training | learn the parameters | every epoch |
| Validation | compare models, choose hyperparameters | as often as you like |
| Test | estimate how well the final model will work on new data | **once, at the very end** |

The distinction between validation and test is the point of the slide: hyperparameter search is
itself a fitting procedure, so a score used to choose hyperparameters is no longer an unbiased
estimate. The test set exists to be spent once.

**k-fold cross-validation (slide 36).** Randomly split the labelled data into k parts (folds), often
k = 10. For each fold in turn: train on the other k−1 folds, score on the held-out fold. Repeat k
times, so each fold is the test fold exactly once, and average:

```
final estimate = (1/k) Σ_{i=1..k} s_i
```

The slide shows the k = 5 rotation explicitly: five rows of Train/Test, one test position per row,
one score s_i per row.

**Variants named on the slide:**

- **Leave-one-out**, the extreme case k = n: train on all but one instance, repeat n times.
- **More folds** means more training data per fold but higher runtime — the slide states the
  trade-off in exactly those terms.

## Key Properties

- **Every instance is tested exactly once.** The k scores are computed on disjoint test sets, so
  together they cover the whole dataset.
- **The estimate is an average, not a maximum.** Nothing is selected; the folds are pooled.
- **It reduces variance of the *estimate*, not of the model.** Cross-validation tells you more
  reliably how good the procedure is; it does not make any single trained model better.
- **The folds must be built before any preprocessing that learns from data.** Normalisation
  statistics computed on the whole dataset leak test information into training — see
  [[information-leakage]]. The lecture states the wrong and right order explicitly.
- **Random splitting assumes i.i.d. instances.** With several rows per patient or per user, a random
  split puts the same entity in train and test, and the score measures memorisation. The lecture
  names this as a case where the assumption is violated and prescribes splitting by group.
- **Cost is k times the training cost.** That is why it is skipped for large deep networks.
- **One split is subject to random fluctuations** — the lecture's own justification for k-fold.

## Worked Example

The lecture gives no numbers for cross-validation, so here is the arithmetic on a toy case that makes
the variance point concrete. Suppose ten instances and a classifier whose error rate is 20 % on any
five of them and 0 % on the other five — a plausible shape when a few hard examples dominate.

| Scheme | Estimate |
|--------|----------|
| One 70/30 split that lands three hard instances in the test set | 3/3 wrong → **100 % error** |
| One 70/30 split that lands none of them | 0/3 wrong → **0 % error** |
| 10-fold, each fold one instance | 2 folds wrong out of 10 → **20 % error** |

The single-split estimates are 100 % and 0 %, and both come from the same classifier on the same
data. The 10-fold estimate is 20 %, which is the number that describes the classifier rather than
the split. This is exactly the "random fluctuations" the slide warns about, exaggerated to be
visible — real datasets are less bimodal, but the mechanism is the same.

**The cost.** 10-fold means training ten models instead of one. On the polynomial-regression
exercise (`study/homework/introduction-to-deep-learning/exercise-02-solutions.py`), where degrees
1/2/3/9 are compared by train and validation loss, the same argument applies to the validation
split: a single 80/20 split decides which degree "wins", and a different split could reorder two
adjacent degrees. The exercise's conclusion (that degree 9 overfits while degree 2–3 generalises) is
robust because the gap is large, not because one split is trustworthy.

## Common Pitfalls

- **Using the test set to choose hyperparameters, then reporting the test score.** The number is
  then a validation score wearing a test score's clothes. The lecture's separate validation split
  exists precisely to prevent this.
- **Normalising, imputing, or selecting features on the full dataset before splitting.** The
  single most common leak; the lecture draws the wrong pipeline and the right one side by side.
- **Random splits on grouped data.** Several scans per patient, several sessions per user — a random
  split leaks identity across the boundary and inflates the score.
- **Reporting the best fold instead of the average.** The folds are a sample of the estimate, not a
  leaderboard.
- **Using leave-one-out for a model whose training is unstable.** k = n maximises training data per
  fold but also maximises the correlation between folds, so the variance reduction is smaller than
  it looks; the slide restricts its recommendation to "limited training data and reasonable training
  time".
- **Assuming cross-validation fixes a bad split strategy.** If the data has temporal order, the
  folds must respect time (train on the past, test on the future); rotating a random split still
  trains on the future.
- **Forgetting that the folds must be re-drawn after any change to the pipeline.** A fold assignment
  reused across many experiments is a source of quiet optimism.

## Connections

- [[information-leakage]] — the failure mode cross-validation exists to prevent, and the reason the
  split must come first.
- [[ml-data-and-iid-assumption]] — random folds assume i.i.d.; temporal and covariate shift break
  that assumption and change how folds must be built.
- [[classification-metrics]] — what s_i actually is: accuracy, precision, recall, F1.
- [[class-imbalance]] — with rare positives, a random split can produce folds with no positives at
  all, which makes the fold score undefined rather than bad. Stratified folds are the usual fix; the
  lecture does not mention stratification.
- [[polynomial-regression-and-overfitting]] — the exercise where train/validation comparison decides
  the model degree.
- [[ml-pipeline-scikit-learn]] — the tooling that implements the split, and the place where
  `train_test_split` before `StandardScaler` is the classic bug.
- [[threats-to-validity]] — the Mining Software Repositories course's framing of the same concern:
  what makes an empirical result not mean what it appears to mean.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **How to choose k** is not derived. "Often k = 10" is the whole guidance, with the trade-off
  (more folds → more training data, higher runtime) stated but not quantified.
- **No confidence interval is given** for the k-fold estimate. The k scores are not independent —
  the training sets overlap heavily — so the naive standard error over s_i would understate the
  uncertainty. The lecture does not raise this.
- **The lecture does not say whether the final model is retrained on all data** after
  cross-validation, which is standard practice but is a different model from any of the k that were
  scored.
- **Nested cross-validation** (an inner loop for hyperparameters, an outer loop for the estimate) is
  not mentioned, although the three-way split creates exactly the problem it solves.
- **Stratification is not mentioned** at all, despite the class-imbalance section later in the same
  lecture making it necessary.
