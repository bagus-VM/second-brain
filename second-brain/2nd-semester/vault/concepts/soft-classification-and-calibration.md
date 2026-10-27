---
title: "Soft Classification and Calibration"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, evaluation]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[ml-task-taxonomy]]"]
---

## One-line Summary
A hard classifier returns a label and throws the confidence away; a soft classifier returns a
probability, which is only useful if it is calibrated — if 80 % really means 80 %.

## Core Intuition

Both outputs can be right and they are not the same product. A hard label answers "which class?"; a
soft output answers "how sure, and about what?" The second carries strictly more information, and it
is the form every modern classifier actually produces internally — the label is then obtained by
thresholding the probability at 0.5, or by taking the argmax over classes.

The reason to care is that confidence is often the more useful quantity. A spam filter that says
"definitely spam" and one that says "60 % spam" deserve different treatment: the second could be
routed to a review queue. In the security setting this is the whole point — a detector that flags
everything as certain is telling you less than one that ranks.

But a probability is only worth the arithmetic you do with it if it means what it says. **Calibration
is that property**: of all the predictions the model makes with 80 % confidence, about 80 % should be
correct. Nothing in a neural network's training procedure guarantees this — a soft output is a number
between 0 and 1, and a model can be confidently wrong in a perfectly consistent way. The lecture
introduces the concept here and defers the machinery (log-likelihood, log-odds, cross-entropy) to
later lectures.

## Formal Definition / Statement

**Slide 14, in the lecture's own three forms:**

| Form | Output |
|------|--------|
| **Hard** | the label, e.g. `"Beach"` |
| **Soft (binary)** | P("Beach") = 0.8, P("not Beach") = 0.2 |
| **Soft (multiclass)** | P("Beach") = 0.8, P("Sand") = 0.15, P("Tree") = 0.05 |

Soft outputs sum to 1 across the classes and carry a confidence.

**The lecture's two remarks on confidence:**

- "Soft classification also gives a confidence: *'My prediction is that soccer team A wins with 80 %
  probability'* — would I take that bet?"
- "**Good probabilities are calibrated:** of all predictions made with 80 %, about 80 % should be
  correct."

**Deferred to later lectures, named on the slide:** log-likelihood, log-odds, cross-entropy.

**Related forms from the task taxonomy (slide 12):** classification predicts a class or a
probability; multiclass classification chooses between more than two classes; multi-label
classification predicts several labels at once.

## Key Properties

- **A soft output is a superset of a hard output.** Given the probability vector, any threshold gives
  a hard label; the reverse loses information permanently.
- **Calibration is a property of the predictions in aggregate, not of a single prediction.** One
  prediction at 0.8 cannot be calibrated or uncalibrated; a *set* of them can be.
- **Calibration and accuracy are independent.** A model can be accurate and miscalibrated, or
  inaccurate and well calibrated, and improving one does not automatically improve the other.
- **Confidence is what makes a bet calculable.** The lecture's own framing — "would I take that
  bet?" — makes the probability an input to a decision, which is the reason to insist on it being
  honest.
- **The class-imbalance material in the same lecture depends on this page.** Thresholding a soft
  output is what produces the confusion matrix; moving the threshold trades precision against recall.
- **The output layer shape follows from the task**: a single sigmoid for binary soft classification,
  a softmax over the classes for multiclass. Both are named as the subject of the next lecture.
- **No calibration method is given in this lecture.** The concept is defined and left.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`.

**Calibration, taken literally.** If a model is perfectly calibrated, of 100 predictions made at
0.8 confidence, about 80 are correct. That is the whole definition, and it is checkable: bin the
predictions by stated confidence and compare each bin's average confidence with its observed accuracy.

**The bet.** Taking the lecture's framing at even money — win 1 unit if right, lose 1 if wrong —
the expected value of a single bet at stated probability p is

```
EV = p * (+1) + (1 - p) * (-1) = 2p - 1
```

| Stated p | Expected value per unit staked |
|----------|--------------------------------|
| 0.50 | +0.00 |
| 0.60 | +0.20 |
| 0.80 | **+0.60** |
| 0.90 | +0.80 |

So at a genuine 0.8 the bet is worth taking; at 0.5 it is exactly worthless; below 0.5 it is a loss.
**The entire argument depends on the number being calibrated.** If the model says 0.8 but is right
only half the time, the expected value is 0.00 — the bet you thought was worth +0.60 is worth
nothing. The overconfidence in that case is 0.30, and the calibration error for that single bin is
|0.8 − 0.5| = 0.30.

**A soft output that is not calibrated, without any error in the model's logic.** A model that
outputs 0.8 for every prediction on a population that is 50/50 is internally consistent and
completely uncalibrated: it promises 80 correct out of 100 and delivers 50. Nothing in the training
objective as stated on slide 19 (minimise the average loss on the training data) forces the
probabilities to match reality on new data — that is what the deferred cross-entropy discussion is
about.

## Common Pitfalls

- **Reading a probability as a hard label early.** `argmax` at 0.5 discards exactly the information
  that makes the output useful for triage.
- **Assuming a soft output is calibrated because it came from a softmax.** A softmax produces numbers
  in [0,1] that sum to 1; it does not produce frequencies that match reality.
- **Evaluating calibration on the training set.** A model that has memorised the training labels is
  often confidently right there and confidently wrong elsewhere; calibration must be checked on
  held-out data, which is the [[information-leakage]] rule applied to a different measurement.
- **Treating 0.8 as a decision rather than an input to one.** The lecture's question is about taking
  a bet at those odds, and the answer depends on the payoff, not only the probability.
- **Confusing multi-label with multiclass.** Multi-label predictions do **not** sum to 1 across
  labels; each is an independent binary decision, so the multiclass calibration argument does not
  transfer unchanged.
- **Assuming more classes means lower confidence.** A five-class softmax at 0.8 is a strong statement
  — 0.2 is the total mass on the wrong answer, not the mass per wrong class.
- **Believing accuracy improvements imply calibration improvements.** They are separate axes.

## Connections

- [[ml-task-taxonomy]] — the classification / multiclass / multi-label split this page's outputs come
  from.
- [[classification-metrics]] — what happens after thresholding: precision, recall, F1, the confusion
  matrix.
- [[roc-curve]] — the curve traced out by moving the threshold across a soft output; it is a
  calibration-and-ranking object rather than a single-label object.
- [[logistic-regression]] — the simplest model whose output *is* a probability, and the "single
  artificial neuron" the lecture points forward to.
- [[class-imbalance]] — where the threshold choice becomes a real trade-off.
- [[naive-bayes-text-classification]] — a classifier that produces probabilities by construction,
  with its own calibration behaviour in practice.
- [[ml-for-security-domains]] — the application context where a wrong confidence is a routed alert at
  best and a missed incident at worst.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **No calibration method, metric or diagram is given.** The lecture defines calibration, asks the
  bet question, and defers; reliability diagrams, temperature scaling and the Brier score are not
  mentioned.
- **"About 80 % should be correct" is not quantified.** No tolerance band is stated for how far a
  nominally calibrated model may deviate.
- **The lecture does not say how to obtain a calibrated classifier** from an uncalibrated one, or
  whether the models in this course tend to be over- or under-confident.
- **Whether the exam's "may contain some coding" would include threshold selection** is not stated;
  the slide mentions no tooling.
- **Log-likelihood, log-odds and cross-entropy are named and deferred** — cross-entropy does appear
  later in the course, so this page is deliberately incomplete rather than unfinished.