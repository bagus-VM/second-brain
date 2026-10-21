---
title: "Classification Metrics: Accuracy, Precision, Recall, F1"
tags: [concept, ml-security, semester-2, evaluation]
course: "Machine Learning for Cybersecurity"
source_count: 2
status: current
last_updated: 2026-10-20
prerequisites: ["[[naive-bayes-text-classification]]"]
---

## One-line Summary

Four numbers decide whether a detector is any good, and on security data the most quoted one is the least informative: L2's credit-card model scores 99.89% accuracy while missing half the fraud.

## Core Intuition

Each metric answers a different question about the same confusion matrix. Accuracy asks "how often am I right overall?", which is dominated by whatever class is common. Precision asks "when I raise an alarm, how often am I correct?" — the analyst's workload. Recall asks "of the incidents that happened, how many did I catch?" — the attacker's free pass. F1 refuses to let one of the two hide the other. Security data is imbalanced by construction, so the first question is almost never the interesting one.

## Formal Definition / Statement

Confusion matrix, positive = "attack/fraud":

|  | Predicted negative | Predicted positive |
|---|---|---|
| **Actual negative** | TN | FP (false alarm) |
| **Actual positive** | FN (missed) | TP |

| Metric | Slide definition | Formula |
|---|---|---|
| **Accuracy** | fraction of all predictions that are correct | (TP+TN) / (TP+FP+FN+TN) |
| **Precision** | of the predicted positives, how many are actually positive | TP / (TP+FP) |
| **Recall** | of the actual positives, how many we found | TP / (TP+FN) |
| **F1-score** | harmonic mean of precision and recall | 2·P·R / (P+R) |

The harmonic mean is background mathematics: it is dominated by the smaller value, is zero if either is zero, and is always ≤ the arithmetic mean — exactly the behaviour wanted, since perfect precision with 5% recall should not average into something respectable.

**Averages over classes (L3, slide 7).**

- **Support** — the number of test samples belonging to a class.
- **Macro average** — the direct, unweighted average of each class's metric. Every class counts once, whatever its size.
- **Weighted average** — each class's metric weighted by its support. The majority class dominates, so the weighted average collapses towards the majority class's numbers.

**Multi-class confusion matrix.** The same grid generalises to more than two classes: rows are true labels, columns predicted labels, and the cell is the count of samples that moved from that row class to that column class. Per-class recall and precision are read off the same way — recall from the row, precision from the column. L3 slide 5 shows a five-class network-intrusion matrix (KDD-style classes `0-normal`, `1-Probe`, `2-DoS`, `3-U2R`, `4-R2L`):

| True label ↓ / Predicted → | 0-normal | 1-Probe | 2-DoS | 3-U2R | 4-R2L | Recall |
|---|---|---|---|---|---|---|
| **0-normal** | 59199 | 1095 | 0 | 169 | 129 | 0.977 |
| **1-Probe** | 182 | 3824 | 19 | 8 | 133 | 0.918 |
| **2-DoS** | 39740 | 662 | 188984 | 35 | 432 | 0.822 |
| **3-U2R** | 142 | 0 | 0 | 40 | 46 | 0.175 |
| **4-R2L** | 14262 | 27 | 1 | 634 | 1265 | 0.078 |
| **Precision** | 0.521 | 0.682 | 1.000 | 0.045 | 0.631 | |

The diagonal is not the whole story. `2-DoS` is nearly perfect (precision 1.000, recall 0.822) because 188,984 of its samples land correctly, but `3-U2R` and `4-R2L` are almost undetectable (recall 0.175 and 0.078) and `4-R2L` is usually mistaken for `0-normal` (14,262 cases). A single overall accuracy over this matrix would be dominated by `2-DoS` and would hide both rare-class failures. This is the same imbalance argument as the credit-card example, one level up: see [[machine-learning-for-cybersecurity-lecture-3]].

## Key Properties

- **Accuracy is prevalence-dependent.** This is why imbalanced security data breaks accuracy-first reporting.
- **Precision and recall trade off through the threshold:** lowering it finds more positives and produces more false alarms.
- **F1 weights them equally**, which is a choice. If a missed intrusion costs more than a wasted analyst hour, equal weighting is wrong.
- **All four are computed on predictions, not probabilities**, so the threshold is part of the model even when unmentioned.

## Worked Example

Logistic regression on the 284,807-row credit-card dataset, 20% held out. L2 prints:

```
Accuracy  = 0.9988939995084443
Precision = 0.7868852459016393
Recall    = 0.4897959183673469
F1 Score  = 0.6037735849056604
```

Those four values fit one confusion matrix, reconstructed here by arithmetic on the printed numbers (not a slide):

|  | Predicted 0 | Predicted 1 |
|---|---|---|
| **Actual 0** | 56,851 | 13 |
| **Actual 1** | 50 | 48 |

Check: precision 48/61 = 0.7869, recall 48/98 = 0.4898, accuracy 56,899/56,962 = 0.9989, F1 = 0.6038.

**Why 99.89% is a bad model.** Predicting "no fraud" for every transaction scores 56,851/56,962 = 0.99805 — 99.81%. The trained model is 0.08 points better than a constant, while missing 50 of 98 frauds. The accuracy is high because the data is imbalanced, not because the model is good: it measures the majority class and calls it performance. Precision 0.79 and F1 0.60 are the numbers that describe the detector, and both say "not deployable".

**A second, different run: the Lab 1 notebook.** L2's Lab 1 notebook repeats the same pipeline on the same dataset and prints a different set of numbers:

```
Accuracy = 0.9992451107756047
Precision = 0.8481012658227848
Recall = 0.6836734693877551
F1 Score = 0.7570621468926554
```

with

```
              precision    recall  f1-score   support

           0     0.9995    0.9998    0.9996     56864
           1     0.8481    0.6837    0.7571        98

    accuracy                         0.9992     56962
   macro avg     0.9238    0.8417    0.8783     56962
weighted avg     0.9992    0.9992    0.9992     56962
```

The support is identical to the slides' (56,864 / 98, total 56,962), so the two runs used the same split and the same test set. The notebook's run is better on *every* metric — accuracy 0.9992 vs 0.9989, precision 0.848 vs 0.787, recall 0.684 vs 0.490, F1 0.757 vs 0.604 — so they are not the same fit. **The discrepancy is unexplained**: neither the slides nor the notebook states a cause, and none is asserted here. It is recorded as an open question; the full notebook walkthrough is [[lab-1-basics]].

Two further notebook results belong on this page:

- **Scaling `Amount` made the positive class worse.** After `StandardScaler` on `Amount` (fit on train, transform on test), the report becomes class 1 precision 0.8025, recall 0.6633, F1 0.7263, accuracy 0.9991, macro avg 0.9009 / 0.8315 / 0.8629, weighted avg 0.9991. Rescaling changed the decision boundary and cost accuracy on the fraud class. That is a statement about this dataset, not about normalisation in general.
- **The macro row is the informative one.** Macro recall 0.8417 is the honest summary (it halves the distance to the fraud class's 0.6837 by counting both classes equally); weighted recall 0.9992 is the majority class wearing a hat, and is numerically identical to accuracy. See [[roc-curve]] for the threshold view of the same trade-off.

**On ROC.** The reading assignment for the spam exercise asks what the ROC curve is and how the assigned paper (Kontsewaya et al., 2021) calculates it. Check the paper's full text before answering: neither "ROC" nor "AUC" appears in it — it reports accuracy, precision, recall and F-measure only. The question does not match the paper. L2 itself defers metric detail to the next week. Standard background: an ROC curve plots the true-positive rate (recall) against the false-positive rate (FP/(FP+TN)) while the decision threshold is swept from 1 down to 0, so it describes a detector across all thresholds instead of at the implicit 0.5 cut; the area under it (AUC) is the probability that a random positive is ranked above a random negative.

## Common Pitfalls

- **Reporting accuracy on an imbalanced dataset.** The baseline is the number to beat, and it is usually ~99%.
- **Swapping precision and recall.** Precision has the predictions in the denominator, recall the actual positives: "of the real ones, how many did I recall".
- **Maximising F1 when the costs are asymmetric.** Security costs almost always are.
- **Evaluating on training data.** L2 states it directly: test data is for testing, never for training.
- **Reading one split as the model's true performance.** `random_state=42` makes it reproducible, not representative.

## Connections

- [[naive-bayes-text-classification]] — the classifier these metrics judge.
- [[ml-pipeline-scikit-learn]] — where the four calls appear in code.
- [[roc-curve]] — the threshold-sweeping view of the same confusion matrix; the AUC the assigned HyperVision paper reports is built from exactly these TPR/FPR pairs.
- [[machine-learning-for-cybersecurity-lecture-3]] — where the multi-class matrix, support, macro average and weighted average are introduced.
- [[lab-1-basics]] — the professor's Lab 1 notebook: the same metrics with executed outputs, plus the unexplained discrepancy against the slides.
- [[security-terminology-and-risk-model]] — precision and recall are the technical form of the cost/benefit argument: false positives cost analyst time, false negatives cost incidents.

## Open Questions

- L2 uses the default 0.5 threshold throughout. Nothing discusses threshold selection against a cost model, the step that would connect metrics to risk.
- The 0.9989 accuracy comes from the full imbalanced split; after undersampling the balance changes completely, so the two configurations are not comparable.
- **Why do the slides and the Lab 1 notebook report different metrics from the same dataset, same split, same `random_state` and same model?** The notebook is better on every metric (recall 0.684 vs 0.490) with identical support, so the two are different fits. Neither source explains it.
- **What are the balanced model's metrics?** The notebook's corrected balancing (train-only undersampling, `stratify=y`, evaluation on the untouched imbalanced test set) prints heatmaps but no metric text, so the honest test score for the balanced model is still unknown.
- **No AUC is ever computed for the credit-card model**, in either source. The ROC page notes the same gap; the assigned HyperVision paper does report AUC, so the course has a number to compare against but not on its own data.
- **The multi-class matrix has no macro/weighted row printed**, only per-class precision and recall, so it is not possible to say from L3 whether the lecture's own averaging convention is macro or weighted for that matrix.

