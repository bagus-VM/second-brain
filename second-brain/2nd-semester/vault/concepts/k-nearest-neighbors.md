---
title: "K-Nearest Neighbors"
tags: [concept, ml-security, semester-2, supervised-learning]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

KNN classifies a new sample by the majority class of its K closest training samples — no model parameters, no training phase, all the cost moved to prediction time.

## Core Intuition

"Tell me about your friends (neighbors) and I will tell you who you are." The classifier has no internal representation of the data; it *is* the data. To label a new observation, it measures how far that observation is from every stored training point, keeps the K closest, and copies their majority label.

The consequence is that the algorithm's "learning" is entirely deferred. There is no fitted weight vector, no objective solved at training time, and nothing to overfit. What you gain in simplicity you pay for at every single prediction: each new sample is compared against the entire training set. That is why the lecture's comparison table calls KNN's training effort **Low** and its classification effort **High** — the only non-trivial row in the table.

The other structural property that matters for this course is that **KNN produces a count, not a probability**. With K = 3, the score of a sample is "how many of my three neighbours are of class c" — one of 0, 1, 2 or 3. There is no continuous score to sweep a threshold over, so its ROC curve degenerates to three discrete operating points. See [[roc-curve]].

## Formal Definition / Statement

**Setup.** Training set T = {(x₁, y₁), …, (xₙ, yₙ)} with xᵢ ∈ ℝᵈ feature vectors and yᵢ class labels. For a new sample S:

1. Compute the distance D(S, xᵢ) to every training sample.
2. Take the K samples with the smallest distance.
3. Assign S the most frequent class among those K.

**Distance metrics** (slide 18):

| Metric | Definition | Note |
|--------|-----------|------|
| **Euclidean** | D(X, Y) = √(Σᵢ (xᵢ − yᵢ)²) | the straight-line distance; the default intuition |
| **Manhattan** | D(X, Y) = Σᵢ \|xᵢ − yᵢ\| | taxicab distance; axis-aligned, less sensitive to a single large deviation |
| **Minkowski** | D(X, Y) = (Σᵢ \|xᵢ − yᵢ\|^q)^(1/q) | the generalisation; q = 2 recovers Euclidean, q = 1 recovers Manhattan |

**Feature-weighted extension** (slide 20): D(X, Y) = √(Σᵢ wᵢ (xᵢ − yᵢ)²), where wᵢ is the weight of feature i. The weights can encode domain knowledge (which features matter for intrusion detection) or be learned dynamically, e.g. by cross-validation.

**Comparison table row** (slide 31, verbatim):

| Algorithm | Computational Effort (Training) | Computational Effort (Classification) | Dynamic Model Update |
|-----------|----------------------------------|------------------------------------------|----------------------|
| KNN | Low | High | Easy |

## Key Properties

- **No training phase.** Training is "collect the training data and do nothing". This is the cleanest possible separation between fitting and predicting — the exact inverse of the pipeline in [[ml-pipeline-scikit-learn]], where a scaler is fitted on the train split.
- **Distance is everything.** KNN has no parameters beyond K and the metric, so the entire inductive bias lives in the metric and the feature scaling.
- **The score is discrete.** With K = 3 the possible scores are 0, 1, 2, 3 — a *count*, not a probability. The ROC therefore has exactly three TPR/FPR pairs (thresholds between 0–1, 1–2, 2–3) and no steps.
- **Prediction cost is linear in the training-set size.** Every prediction touches all n training samples. This is the price of skipping the training phase.
- **Feature magnitudes decide the metric.** If one feature is expressed in thousands and another in tenths, the distance is dominated by the first, and the "nearest" neighbour is chosen by the wrong feature.
- **K controls the bias/variance trade-off.** Very small K is sensitive to noise and random outliers; very large K can pull in a majority of the other class.
- **Class-imbalance bias.** Because the majority class wins a vote more often, KNN tends to predict the majority class on imbalanced data — exactly the regime of intrusion detection.
- **High-dimensional degradation.** Distance becomes less meaningful as the number of features grows; in high dimensions all points are roughly equally far from each other, and "nearest" loses its discriminative power.

**Advantages** (slide 22): simple and intuitive; requires no training phase; quite good classification if the number of samples is large enough.

**Disadvantages** (slide 22): computational complexity of classification; sensitive to noisy data and outliers; the choice of K can significantly impact performance; distance becomes less meaningful with a very high number of features; bias towards the majority class in imbalanced datasets.

## Worked Example

**The discrete-score ROC.** A 3-KNN classifier is fed the test set, and for each sample the neighbour counts give one of four scores. Sweeping the decision threshold gives three distinct operating points, because the only meaningful thresholds are "predict positive if at least 1, 2, or 3 neighbours are positive". The resulting curve has **no steps** and its shape is **independent of the number of samples in the test set** — the curve is a property of the score granularity, not of the data. The lecture's example has **AUC = 0.82**.

**The 1-KNN quiz question.** With K = 1 a sample can have 0 or 1 neighbour of a class, so the score is always 0 or 1 and there is no intermediate probability. The 1-KNN ROC therefore has exactly **one operating point** — the hard classifier itself — plus the two trivial corners (all-0 at TPR = 0/FPR = 0 and all-1 at TPR = 1/FPR = 1). It looks exactly like the ROC of any non-probabilistic binary classifier, and carries no more information than one confusion matrix. This is the direct continuation of the "connect the dots is not very useful" point in [[roc-curve]].

**The credit-card set.** The `Amount` column is in currency units while the `V` columns are PCA components on a comparable small scale, so on raw features every nearest neighbour is effectively selected by `Amount` alone. Scaling `Amount` to zero mean and unit variance is what makes the neighbours meaningful at all — see [[feature-normalization]].

## Common Pitfalls

- **Forgetting to normalize before computing distances.** The single most common KNN bug; a feature measured in bytes will silently decide every neighbour lookup.
- **Choosing K too small.** K = 1 makes the classifier a noise amplifier; one mislabelled or adversarial sample in the neighbourhood changes the prediction.
- **Choosing K too large.** K = N reduces the classifier to "always predict the majority class" — which on imbalanced intrusion data is a useless detector with a flattering accuracy.
- **Reading the three-point ROC as a poor curve.** A discrete-score ROC is not a broken probabilistic ROC; it is the honest representation of a classifier that emits counts.
- **Assuming the training phase is free.** It is free, but the classification phase is O(n·d) per sample, which is what makes KNN unattractive for high-throughput intrusion detection.
- **Reporting accuracy on imbalanced data** and then being surprised by the majority-class bias. See [[classification-metrics]].

## Connections

- [[roc-curve]] — the L3 section that revisits ROC using KNN; the discrete-score argument lives there.
- [[feature-normalization]] — StandardScaler / MinMaxScaler, the prerequisite for KNN's distance to mean anything.
- [[classification-metrics]] — the metrics the neighbour votes are scored with; multi-class matrix, macro and weighted averages.
- [[ml-pipeline-scikit-learn]] — the L2 pipeline that KNN's "no training phase" contrasts with.
- [[ml-learning-paradigms]] — KNN as an instance-based learner: lazy, non-parametric, supervised.
- [[ml-task-taxonomy]] — classification as a task family; KNN is one classifier within it.
- [[naive-bayes-text-classification]] — the L2 classifier, and the other row of the comparison table on the same slide.
- [[logistic-regression]] — the other L3 model, and the one whose cost of classification is Low.
- [[minkowski-distance]] — the 1st-semester page on the metric family behind Euclidean and Manhattan distance.

## Open Questions

- The slide's rule of thumb for choosing K is garbled in the source ("Choose K as N, with N = number of samples in training set"), which cannot be literal — K = N would mean always predicting the majority class. What the intended heuristic was is not recoverable from the slides; the standard candidates (K ≈ √n, or a cross-validated sweep) are not stated either.
- The lecture does not say how K interacts with class imbalance in practice (class-weighted voting, distance weighting, or stratified sampling of the neighbourhood).
- No KNN experiment on the credit-card or intrusion data is shown, so the claimed advantage "quite good classification if number of samples is large enough" is never demonstrated.
- Whether the 3-KNN AUC of 0.82 is computed on the multi-class intrusion matrix or on some binary projection is not stated.
