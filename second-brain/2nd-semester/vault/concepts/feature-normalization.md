---
title: "Feature Normalization"
tags: [concept, ml-security, semester-2, preprocessing]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

Scaling features to a common range is what stops one large-magnitude column from deciding every distance or every gradient step — and it must be fitted on the training data only.

## Core Intuition

A raw feature vector mixes quantities that have no common unit: `Amount` in euros, a packet count in the thousands, a latency in milliseconds, a PCA component around ±5. Any algorithm that compares features *to each other* — a distance, a gradient, a regularisation penalty — silently lets the largest number win. The features are not more important; they are just written in bigger digits.

The fix is to re-express every feature on a comparable scale, using statistics estimated from the training set. The catch is which data those statistics come from: they must come from the training set, because a statistic computed on the full dataset has already seen the test set, and the test set is no longer unseen. That single ordering rule is the one the L2 pipeline got wrong and L3 restates in the KNN context.

## Formal Definition / Statement

**Why the distance is dominated.** For a weighted Euclidean distance D(X, Y) = √(Σᵢ wᵢ (xᵢ − yᵢ)²), a feature with range 10⁴ contributes differences of order 10⁴ squared = 10⁸, while a feature with range 10⁰ contributes 10⁰. The large feature dominates the sum by eight orders of magnitude, so the *ordering* of candidate neighbours is decided almost entirely by it. The lecture states the rule plainly: **distance is dominated by features expressed by large numbers, so it is important to normalize features.**

**StandardScaler** (slide 21) — zero mean, unit variance:

```
x' = (x − mean) / std
```

```python
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
x_train["Amount"] = s.fit_transform(x_train[["Amount"]])
x_test["Amount"]  = s.transform(x_test[["Amount"]])
```

**MinMaxScaler** (slide 21) — linear rescale into a fixed range, here −1 … 1, with out-of-range test values clipped:

```python
from sklearn.preprocessing import MinMaxScaler
s = MinMaxScaler(feature_range=(-1, 1), clip=True)
x_train["Amount"] = s.fit_transform(x_train[["Amount"]])
x_test["Amount"]  = s.transform(x_test[["Amount"]])
```

**The fit/transform contract.** `fit` *learns* parameters from the data it is given (mean and standard deviation, or min and max). `transform` *applies* already-learned parameters. `fit_transform` does both on the same data. The training split is where the parameters are learned; the test split is only ever transformed.

**The clipping rule.** `clip=True` means a test value that falls outside the range seen in training is clamped to the boundary instead of being extrapolated. The alternative — extrapolating with the training min/max — lets a single extreme test value sit far outside the range of anything seen in training, which for a distance-based method means the test sample can be very far from *every* training point.

## Key Properties

- **Scale-invariance for distance-based methods.** After scaling, the nearest neighbour is chosen by the *pattern* of feature values rather than by the unit the columns happen to be written in.
- **Conditioning for gradient-based methods.** For logistic regression and SGD, features on wildly different scales make the loss surface narrow and elongated, so the optimiser needs many more iterations along the steep direction. Scaling is what makes `max_iter=1000` sufficient in the L2 pipeline.
- **Regularisation is scale-dependent.** A penalty like L1/L2 applies to the raw coefficients; if one feature is 10⁴ times larger than another, the penalty implicitly punishes the small one.
- **The parameters are data-dependent, so the order of operations matters.** Scaling before the split leaks test information; scaling after the split does not.
- **StandardScaler vs MinMaxScaler.** StandardScaler centres and scales by spread, so it is robust to outliers in the *scale* sense (an extreme value shifts the mean but the result is still unbounded); MinMaxScaler maps the observed range onto the target range and is bounded by construction, but is maximally sensitive to outliers (one extreme value compresses everything else into a tiny sub-interval).
- **Bounded output has a cost.** A probability or a normalised score is useful, but clipping throws information away — a test value of 10⁵ when training max was 10³ becomes 10³.

## Worked Example

**The credit-card `Amount` column.** In the L2 pipeline the `V1`–`V28` columns are PCA components with a small spread around zero, while `Amount` runs from 0 to about 2,125.87 with a mean of 122.21 for the fraud class. Untreated, `Amount` dominates any distance or any gradient. The fix applied on the slide is exactly the four lines above: `fit_transform` on `x_train`, `transform` on `x_test`.

**The two ways it goes wrong.** Fitting the scaler on the *whole* frame before the split makes the test mean and standard deviation part of the training procedure, so the test set influences the model — the score becomes optimistic. The second failure is using `fit_transform` on the test split, which re-estimates the parameters from test data and means the test set is transformed with statistics it helped define. Both are the same error: parameters learned from data that should have been unseen.

**The interaction with KNN.** KNN has no weights to learn and no objective to optimise, so normalisation is not a refinement for it — it is a precondition. A distance of 3,000 units contributed by one feature and 0.3 units by another means the neighbourhood is selected by a single column, and the classifier degenerates into a one-dimensional rule no matter how many features the dataset has.

## Common Pitfalls

- **Fitting the scaler on the test set.** The classic leak; the parameters must be learned on training data only.
- **Applying `fit_transform` to the test split** instead of `transform`. Same leak, different API call.
- **Scaling before splitting.** Order matters: split, then fit on train, then transform both.
- **Fitting a separate scaler per split.** Two different scalers mean the two halves live in different coordinate systems, and the "unseen" data is not comparable with the training data.
- **Using a scaler fitted on the full dataset for the final production model** is fine and standard — the leak only matters when the test set is meant to be an honest estimate.
- **Forgetting that normalization does not fix a genuinely informative outlier.** MinMaxScaler with `clip=True` hides it; StandardScaler lets it distort the variance; both leave a decision to the analyst.
- **Assuming scaling improves accuracy.** It usually changes little for tree-based models and a lot for distance- and gradient-based ones. It is a correctness fix, not a performance trick.

## Connections

- [[k-nearest-neighbors]] — the algorithm for which normalisation is a precondition rather than an improvement.
- [[logistic-regression]] — the algorithm for which scaling is about optimiser conditioning and `max_iter`.
- [[ml-pipeline-scikit-learn]] — the L2 pipeline where the scaler appears, and where the two leakage traps are described.
- [[classification-metrics]] — the metrics that are read off a model trained on unscaled features in the L2 run.
- [[ml-learning-paradigms]] — preprocessing as part of the inductive bias, not a neutral step.
- [[minkowski-distance]] — the distance family that large-magnitude features distort.
- [[roc-curve]] — the ROC of a KNN classifier, whose shape depends on how the distances were computed.

## Open Questions

- The lecture presents StandardScaler and MinMaxScaler as alternatives without saying when to prefer which beyond "scale to zero mean/unit variance" versus "scale to the range −1…1". The outlier argument for choosing between them is not made.
- Robust alternatives (RobustScaler, quantile transform) are not mentioned.
- Whether the intrusion-detection feature set should be normalized at all, given that some features may be counts where relative ratios matter, is not discussed.
- No experiment isolates the effect of normalisation: no KNN run with and without scaling is shown, so the claim that distance is dominated by large features is asserted rather than measured.
