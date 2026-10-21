---
title: "ROC Curve and AUC"
tags: [concept, ml-security, semester-2, evaluation]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

A ROC curve plots the true-positive rate against the false-positive rate as the decision threshold is swept from 1 down to 0, so it describes a detector across *all* thresholds instead of at the implicit 0.5 cut, and the area under it (AUC) summarises that in one number.

## Core Intuition

The confusion matrix answers one question: "how did this classifier do at *this* threshold?" It cannot tell you whether the detector was badly built or merely cut in the wrong place. The ROC curve answers the better question by sweeping the cut: every point on it is a different threshold, plotting TPR against FPR. A good detector bows up and to the left; a useless one follows the diagonal; a perfect one is a single point at the top-left corner.

The historical origin is worth knowing because it explains the shape. Signal Detection Theory, developed during World War II, measured whether radar operators could tell an enemy target from noise — a *human* threshold, adjustable at will. Sweeping that threshold over operators and plotting detection rate against false-alarm rate is exactly the ROC construction. The axes have kept their names ever since.

## Formal Definition / Statement

**Axes.** For a binary classifier, with "positive" = the event of interest:

| Rate | Formula | Meaning |
|------|---------|---------|
| **TPR** (true positive rate) | TP / (TP + FN) | of the real positives, how many we caught (= recall) |
| **FPR** (false positive rate) | FP / (FP + TN) | of the real negatives, how many we wrongly flagged (= fall-out, = 1 − specificity) |

**The sweep.** A *probabilistic* classifier returns a probability per sample. Lower the threshold and more samples cross it to "positive". Each additional positive is either a TP (TPR rises) or an FP (FPR rises) — or both, if several samples share exactly the same score and cross together. That is why the curve of a probabilistic classifier is a **step function**, and why a single binary classifier is a **single point** on the diagram: its threshold is baked in.

**Border cases** (the two extreme operating points, plus the two degenerate corners):

- All classified as 0 → TPR = 0, FPR = 0
- All classified as 1 → TPR = 1, FPR = 1
- Perfect classifier → the single point TPR = 1, FPR = 0
- Random classifier → the diagonal from (0,0) to (1,1)

**AUC.** The area under the curve. Larger is better. It is *independent of the slope* of the curve, i.e. it summarises the whole trade-off rather than rewarding a particular point on it. A classifier with AUC = 0.5 is the random diagonal.

**Threshold optimisation.** If FPR and TPR matter equally, maximise `TPR + (1 − FPR)`. Graphically, that is the point where a line of slope +1 touches the ROC curve. If the two costs differ, the optimal line has a different slope: the point on the curve closest to the top-left corner *in the metric that weights the errors*.

## Key Properties

- **Threshold-free by construction.** The curve is a property of the *scoring function*; any single point on it is a property of the scoring function *plus* a threshold. This is why the curve generalises a classifier better than one confusion matrix does.
- **Class-imbalance is only partly handled.** TPR and FPR are both *rates* normalised by their own class sizes, so the axis scales do not change when the class ratio changes. What the curve cannot show you is the *base rate* — on a 0.17%-positive dataset, a curve that looks excellent can still mean an unusable detector in practice.
- **The step structure is a property of the scores, not of the data size.** How many steps a ROC has is determined by how many distinct score values the classifier can emit.
- **AUC is rank-based, so it is invariant to monotone transformations of the scores.** Two classifiers with the same ranking of samples have the same AUC even if their probability calibrations differ wildly.
- **Connect-the-dots is not a ROC curve.** Joining two points of a hard binary classifier with a line adds no information over the two confusion matrices at the endpoints — the lecture says so explicitly.

## Worked Example

**A probabilistic classifier (the standard picture).** Sweeping the threshold down across a test set adds positives one at a time. Each addition moves the point right (if it was an FP) or up (if it was a TP) or both (tie in score). The resulting staircase is the ROC curve; the lecture's illustrative example has **AUC = 0.93**.

**A hard binary classifier.** A classifier that outputs only 0 or 1 has no threshold to sweep, so it contributes *one* operating point plus the two trivial corners (all-0 and all-1). The lecture's "connect the dots with a line" version of this is explicitly labelled **not very useful** — no information gain compared to a simple confusion matrix or to the FPR and TPR values.

**3-KNN.** A 3-nearest-neighbour classifier produces a *count* of neighbours per class (0, 1, 2 or 3), not a probability. Its score is therefore discrete, so the ROC curve has only **three distinct TPR/FPR pairs** — corresponding to thresholds between 0–1, 1–2 and 2–3 neighbours — and it has **no steps**. The lecture's example: **AUC = 0.82**, and the shape is independent of how many samples are in the test set.

**1-KNN (the quiz question).** The score is always 0 or 1 — there is no intermediate probability. So the 1-KNN ROC has exactly **one operating point** (the hard classifier itself) plus the two trivial corners. It looks exactly like the ROC of any non-probabilistic binary classifier, and it carries no more information than a single confusion matrix.

**Multi-class.** The confusion matrix generalises to a multi-class grid (see [[classification-metrics]]), and the ROC idea is a binary construction; extending it to multi-class means one-vs-rest, and the lecture does not go there.

## Common Pitfalls

- **Reporting AUC without the class balance.** AUC says nothing about how many actual attacks the detector will catch per week on your data. It is a *ranking* quality, not a deployment decision.
- **Treating a hard classifier's connect-the-dots line as a ROC curve.** It is an interpolation with no meaning.
- **Reading the step count as a data property.** Steps come from score granularity: a 3-KNN has three operating points no matter how large the test set is.
- **Confusing TPR with accuracy.** TPR is recall; it is normalised by the actual positives, not by all samples. On imbalanced data the two differ enormously.
- **Optimising the threshold without a cost model.** "Maximise TPR + (1−FPR)" assumes both error types cost the same. Security costs rarely do.
- **Expecting the paper assigned in L2 to have an ROC curve.** The Kontsewaya et al. 2021 paper reports accuracy, precision, recall and F-measure only — neither "ROC" nor "AUC" appears in it. The reading question does not match the source (see [[classification-metrics]]).

## Connections

- [[classification-metrics]] — the confusion matrix, accuracy/precision/recall/F1, and the multi-class matrix that the ROC's TPR/FPR are read off. The ROC page is the *threshold-sweeping* view of the same table.
- [[ml-pipeline-scikit-learn]] — where a model that produces the probabilities comes from, and where the threshold is currently hard-wired at 0.5.
- [[naive-bayes-text-classification]] — the classifier from L2; it emits posteriors, so its ROC is a proper staircase.
- [[k-nearest-neighbors]] — the L3 classifier whose discrete scores produce a stepped, three-point ROC.
- [[ml-task-taxonomy]] — classification as a task family; the ROC applies to any binary classifier in it.
- [[security-terminology-and-risk-model]] — the cost/benefit argument the threshold optimisation stands in for: false positives cost analyst time, false negatives cost incidents.

## Open Questions

- The lecture gives the equal-cost rule (slope +1) but never states how the slope changes for asymmetric costs, nor how a cost ratio maps to it.
- Multi-class ROC (one-vs-rest vs micro/macro averaging) is not covered, though a multi-class confusion matrix is shown.
- No AUC value is ever computed for the credit-card model or the spam classifier — the L2 numbers are point metrics only, so the exercise on the previous slide (does the paper use ROC?) is left hanging.
- Whether the KNN's discrete three-point ROC is "worse" than a probabilistic classifier's staircase, or merely differently shaped, is not addressed.
