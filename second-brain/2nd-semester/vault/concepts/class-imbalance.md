---
title: "Class Imbalance"
tags: [concept, introduction-to-deep-learning, semester-2, evaluation, machine-learning]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary
When the positive class is rare, accuracy is a base-rate artefact rather than a result — the
classifier that never says "positive" scores 99 % and finds nothing, so precision, recall and F1
carry the information instead.

## Core Intuition

Accuracy counts two very different things as equally good: finding a positive, and correctly ignoring
a negative. When negatives outnumber positives 99 to 1, the second is almost free. A classifier that
answers "no" to everything scores the base rate and is useless; a classifier that flags a hundred
people of whom eighty are real positives raises that score by four tenths of a percentage point and
is genuinely useful. The metric and the value of the model have come apart.

The lecture's bot example is exactly this situation — rare events in a large stream — and it is the
common situation in security work: intrusions, fraud, defects, spam. The remedy is not to abandon
accuracy but to report it *alongside* measures that condition on the positive class. Precision asks
"when you flag something, how often are you right?"; recall asks "of the real positives, how many did
you find?". A system that cannot answer both is not evaluated, only scored.

The last thing worth holding onto is that this trade-off is a *choice*, not a property of the model:
the same classifier produces different precision and recall depending on where you put the threshold
on its soft output. That connects this page to the calibration material earlier in the lecture.

## Formal Definition / Statement

**Slide 42, the example as given.** Bots are rare: 10,000 registrations, 100 of them bots.

- **Trivial classifier, "never a bot"**: accuracy = 99 %, but it finds no bot, **recall = 0**.
- **Better classifier**: flags 120 users, 80 of them bots.

**The confusion matrix on the slide:**

|  | Predicted bot | Predicted human |
|---|---|---|
| Actual bot | TP = 80 | FN = 20 |
| Actual human | FP = 40 | TN = 9,860 |

**The measures (slide 41, for reference):**

```
accuracy  = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
F1        = 2 * precision * recall / (precision + recall)
```

**The slide's computed values for the better classifier:** accuracy = 9,940 / 10,000 = 99.4 %,
precision = 80 / 120 ≈ 0.67, recall = 80 / 100 = 0.8, F1 ≈ 0.73.

**The conclusion, stated on the slide:** "For imbalanced data, report precision / recall / F1 (or
PR / ROC curves), not only accuracy."

## Key Properties

- **Accuracy is bounded below by the base rate.** With 1 % positives, 99 % accuracy is what doing
  nothing achieves; only the excess above that floor is evidence of a model.
- **Precision and recall condition on different things.** Precision is a statement about the
  *predictions* (how many flags are real); recall is a statement about the *positives* (how many were
  caught).
- **They trade off against each other.** Raising the threshold raises precision and lowers recall, and
  the lecture's F1 is one way to collapse the pair into a single number.
- **F1 is a harmonic mean, so it punishes imbalance between the two.** A precision of 1.0 with a recall
  of 0.1 gives F1 ≈ 0.18, not 0.55.
- **The trivial classifier has undefined precision, not zero.** It makes no positive predictions, so
  TP + FP = 0; the slide's own table does not give it a precision, and the "0/0" is a deliberate blank.
- **PR and ROC curves are the continuous version**, traced by moving the decision threshold over a soft
  output.
- **The choice of threshold is an application decision.** Which point on the curve is right depends on
  the relative cost of a missed bot and a false alarm, which the lecture does not specify.
- **Imbalance affects training as well as evaluation.** The lecture's treatment is about measurement;
  resampling and class weighting are not discussed. (And resampling must happen inside the training
  fold, or it leaks — see [[information-leakage]].)

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 8.

| | Trivial "never a bot" | Better classifier |
|---|---|---|
| TP | 0 | 80 |
| FP | 0 | 40 |
| FN | 100 | 20 |
| TN | 9,900 | 9,860 |
| Accuracy | 9,900/10,000 = **0.9900** | 9,940/10,000 = **0.9940** |
| Precision | undefined (0/0) | 80/120 = **0.6667** |
| Recall | **0** | 80/100 = **0.8000** |
| F1 | undefined | **0.7273** |

Read the first column and the second column together and the point is made:

- **The classifier improves accuracy by 0.0040** — four tenths of a percentage point. On a dashboard
  that is noise.
- **The same classifier improves recall from 0 to 0.80** — it finds four fifths of the bots that
  nothing at all was finding.
- **The accuracy floor is not a neutral baseline.** It is 0.99 because the data is 99 % negative, so
  the trivial classifier starts 0.99 of the way to any accuracy target before doing any work.

That gap is the reason the slide says "not only accuracy". If a report shows only 99.4 %, the natural
conclusion is "this excellent classifier is barely better than doing nothing" — which is true of the
number and false of the model.

## Common Pitfalls

- **Reporting accuracy alone.** The lecture's explicit instruction, and the mistake the example is
  designed to expose.
- **Reading 99.4 % as "better than the trivial 99 %" without a sense of scale.** The improvement is
  0.0040 in absolute terms; recall moves 0 → 0.80.
- **Reporting the best of precision and recall.** They move in opposite directions; a single number
  without the other hides which direction you chose.
- **Using F1 without knowing it is a harmonic mean.** It is low whenever either component is low, which
  is usually the intent, but it also means two very different systems can share an F1.
- **Assigning precision 0 to the trivial classifier.** It is undefined (no positive predictions), and
  a zero would suggest it makes many wrong flags.
- **Optimising accuracy on imbalanced data.** The optimum of accuracy is often a model that predicts the
  majority class everywhere — precisely the trivial classifier.
- **Choosing a threshold by habit.** The 0.5 default is arbitrary; the precision/recall trade-off is
  exactly the threshold, and a security application may want a different point on the curve.
- **Resampling before splitting.** A classic leak that silently reintroduces test rows into training.
- **Forgetting that imbalance also affects the loss and the gradient.** The lecture's evaluation
  section is about measurement; a 0-1 loss on a 99:1 problem is quietly the wrong objective.

## Connections

- [[classification-metrics]] — the full definition of every measure used here, plus the confusion
  matrix convention.
- [[roc-curve]] — the threshold sweep in ROC form; the lecture's parenthetical also names PR curves,
  which are the version usually preferred under heavy imbalance.
- [[soft-classification-and-calibration]] — the scores over which the threshold is swept.
- [[ml-data-and-iid-assumption]] — the shift material: the base rate is not stable, and a moving base
  rate moves the accuracy floor.
- [[loss-functions-and-empirical-risk]] — why 0-1 loss is not the right training objective under
  imbalance.
- [[information-leakage]] — the rule that applies to any resampling or reweighting used to compensate.
- [[ml-for-security-domains]] — the course where the same imbalance material is applied to detection
  problems.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **No remedy for imbalance is given.** The lecture prescribes *reporting* measures; resampling, class
  weights, cost-sensitive losses and threshold selection are not discussed.
- **The cost asymmetry is not quantified.** How much worse a missed bot is than a false alarm is the
  input needed to pick a threshold, and the slide does not supply it.
- **No numbers are given for the trivial classifier's precision**, which is undefined rather than zero;
  the slide simply omits it.
- **PR and ROC curves are named and not shown.** The lecture refers to them without defining them here
  (the ROC material lives in the Machine Learning for Cybersecurity course).
- **The downstream effect of imbalance on training is not covered** — only on evaluation, which is the
  part of the problem the lecture's section 2.4 is about.