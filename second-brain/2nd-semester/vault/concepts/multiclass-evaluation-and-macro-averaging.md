---
title: "Multi-class Evaluation and Macro Averaging"
tags: [concept, deep-learning, semester-2, evaluation, multi-class]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[classification-metrics]]", "[[class-imbalance]]"]
---

## One-line Summary

A classifier choosing among C classes is scored by collapsing the C×C confusion matrix into C one-vs-rest problems — each class against the merged rest — and macro-F1 averages the resulting C F1 values with every class counted once. Accuracy asks how often the model is right; macro-F1 asks how it does across the classes.

## Core Intuition

Homework task 4 states the construction in one sentence: "to compute the metrics for class y = 0, we merge all other classes into a single negative class and add up their counts". Its illustration is Recall_{y=0} = 3/(3 + (147 + 33)), where "(147 + 33) are the combined counts of the other classes" — the slide matrix's class-0 row, reused. Precision, recall and F1 keep their binary definitions ([[classification-metrics]]); the only change is that one row's and one column's off-diagonal entries are folded into a single negative bucket, once per class.

Two summaries then compete. Macro-averaging takes the unweighted mean over classes, so every class contributes one number whatever its size. Accuracy is sample-weighted: it counts each of the 996 correct predictions of the 1500-sample slide matrix once, and the class supplying 833 of them is the one it mostly reports. Of the two, only macro-averaging can show what happens to class 0.

## Formal Definition / Statement

Slide 16 gives one 3×3 matrix — rows ground truth, columns prediction, total 1500 samples:

| | ŷ = 0 | ŷ = 1 | ŷ = 2 |
|---|---|---|---|
| **y = 0** | 3 | 147 | 33 |
| **y = 1** | 17 | 833 | 137 |
| **y = 2** | 86 | 84 | 160 |

One-vs-rest turns it into three binary tables. For class c: TP is the diagonal cell M[c][c]; FN is the remaining entries of row c; FP is the remaining entries of column c; TN is everything left over. Slide 20 defines macro-F1 = (1/3) Σ_{i=0}^{2} F1-score_{Y=i} and reports accuracy = (3 + 833 + 160) / 1500 = 0.664. The per-class values (output-exercise-03-numbers.txt):

| Class | TP | FN | FP | TN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|
| 0 | 3 | 180 | 103 | 1214 | 0.028302 | 0.016393 | 0.020761 |
| 1 | 833 | 154 | 231 | 282 | 0.782895 | 0.843972 | 0.812287 |
| 2 | 160 | 170 | 170 | 1000 | 0.484848 | 0.484848 | 0.484848 |

macro-F1 = 0.439299 (the slide prints ≈ 0.44); accuracy = 996/1500 = 0.664000 (the slide prints 0.664).

The slide reaches its 0.44 by rounding precision and recall to two decimals before averaging (0.03, 0.78, 0.48 and 0.02, 0.84, 0.48) and then computing F1 from those rounded values. The value 0.439299 is the mean of the three unrounded F1 values in the table above. These are two different procedures and there is no reason for them to agree digit for digit: the rounded path propagates the two-decimal error into every F1 it averages. Which of the two the course intends as "the" macro-F1 is not stated in the material.

Homework task 4(a) uses the sheet's own matrix [[7, 129, 46], [25, 766, 170], [73, 73, 204]], total 1493 (printed as 1493, not 1500 — recorded as printed):

| Class | Precision | Recall | F1 |
|---|---|---|---|
| 0 | 0.066667 | 0.038462 | 0.048780 |
| 1 | 0.791322 | 0.797086 | 0.794194 |
| 2 | 0.485714 | 0.582857 | 0.529870 |

macro-F1 = 0.457615; accuracy = 977/1493 = 0.654387.

## Key Properties

- **Macro weighting is a decision about what the number means.** Macro averaging weights every class equally; the aggregate accuracy is dominated by whatever class is largest. Both are computable from the same matrix, and they answer different questions — "how do I do across the classes I care about" against "how often am I right".
- **One-vs-rest TN is arithmetic filler in the multi-class case.** The output file prints TN = 1214, 282 and 1000 for the three classes of the slide matrix. Each of these counts every sample that is neither truly of class c nor predicted to be, which is nearly the whole dataset. In binary evaluation TN means correctly rejected negatives; here there is no single negative class to reject, so the count carries no information and exists only because the binary formulas need a fourth cell. It should not be quoted.
- **Per-class recall spread is the diagnostic accuracy cannot provide.** Homework 4(b): predicted counts per class [105, 968, 420] against actual counts [182, 961, 350]; per-class recall [0.0385, 0.7971, 0.5829]; spread 0.7586. Class 0 is predicted 105 times and is 182 of the 1493 samples.
- **Micro-F1 collapses to accuracy in the single-label case.** When each sample has exactly one true class and receives exactly one prediction, micro-precision and micro-recall both reduce to (correct)/(total), so their harmonic mean is the accuracy. Macro-F1 and micro-F1 are therefore not interchangeable: on the slide matrix they sit at 0.439299 and 0.664. This identity is background mathematics, not stated in the slides.
- **The number of classes fixes the mean.** macro-F1 is a plain mean over C values, so adding or removing a class changes it by construction; the value is not comparable across problems with different C unless that is stated.

## Worked Example

Class 0 of the homework matrix ([[introduction-to-deep-learning-exercise-3]], task 4(a)), worked from the matrix rather than from the summary numbers. Row 0 is [7, 129, 46]: 7 samples truly of class 0 are predicted 0, 129 are predicted 1 and 46 are predicted 2. Column 0 is [7, 25, 73]: 25 class-1 and 73 class-2 samples are predicted to be class 0.

Merging everything that is not class 0 into a single negative class gives TP = 7; FN = 129 + 46 = 175, which is the sheet's "add up their counts"; FP = 25 + 73 = 98. Then

- Precision = 7 / (7 + 98) = 0.066667. The predicted-0 column holds 105 samples — the file's predicted count for class 0 — and only 7 of them are really class 0.
- Recall = 7 / (7 + 175) = 0.038462. Of the 182 samples that are truly class 0 (the file's actual count), 7 are found.
- F1 = 2 · P · R / (P + R) = 0.048780, matching the output file.

The same three lines give class 1 (TP = 766, FN = 195, FP = 202 → 0.791322 / 0.797086 / 0.794194) and class 2 (TP = 204, FN = 146, FP = 216 → 0.485714 / 0.582857 / 0.529870). Averaging the three exact F1 values gives macro-F1 = 0.457615, and the accuracy is 977/1493 = 0.654387, where 977 is the diagonal's total.

**Task 4(b), whether the classifier has good performance.** The answer depends on which summary is asked. The aggregate accuracy of 0.654387 sounds like a working classifier; the per-class picture says it is a classifier of class 1 only. It predicts class 0 exactly 105 times in 1493 samples and finds 3.85 % of the 182 real class-0 cases, while class 1 recall is 0.7971 and class 2 recall is 0.5829 — a recall spread of 0.7586 across three classes. Anyone who needs class-0 decisions is not served, and the single accuracy number is why that failure is easy to miss.

## Common Pitfalls

- **Reporting accuracy alone on a skewed multi-class matrix.** 0.654387 on the homework matrix and 0.664000 on the slide matrix both read as summaries of a competent model while class 0 recall is 0.038462 and 0.016393 respectively. The accuracy is dominated by the largest class and says almost nothing about the smallest.
- **Treating macro-F1 and micro-F1 as interchangeable.** They agree only when every class is equally frequent and equally easy. In the single-label multi-class case micro-F1 equals accuracy, so the two numbers on the slide matrix stand at 0.439299 and 0.664 — far enough apart to reverse a verdict.
- **Quoting one-vs-rest TN as though it meant something.** 1214 for class 0 of the slide matrix is mostly "everything else": an artifact of writing a three-class problem as a binary one, not a count of correct rejections.
- **Averaging rounded per-class metrics.** The slide's ≈ 0.44 comes from precision and recall rounded to two decimals; 0.439299 comes from the unrounded F1 values. Reproduce the one you intend to quote, and say which it is.
- **Reading a good majority-class number as a good model.** Class 1 F1 is 0.794194 and class 0 F1 is 0.048780; the mean, 0.457615, is the only one of the three that describes the matrix as a whole.
- **Assuming the two matrices are comparable because they look alike.** The slide matrix totals 1500 samples and the homework matrix 1493; nothing in the material says the second is a variant of the first.

## Connections

- [[classification-metrics]] — the binary definitions applied C times here; the confusion matrix, precision, recall, accuracy and F1 are defined there and not repeated on this page.
- [[class-imbalance]] — the prior form of the same failure: a metric that reports the majority class and calls it performance.
- [[machine-learning-for-cybersecurity-lecture-3]] — a five-class matrix with macro and weighted averages among its reported rows: the same construction on real data.
- [[soft-classification-and-calibration]] — where the scores behind these hard labels come from.
- [[regression-evaluation-metrics]] — the other half of the same exercise's evaluation section, MAE and MSE.
- [[introduction-to-deep-learning-exercise-3]] — the session this page belongs to; tasks 3 and 4 are the binary and multi-class evaluation tasks.
- [[cross-validation]] — the reliability question a single matrix cannot answer.

## Open Questions

- **Which macro-F1 is the course's?** The slide rounds precision and recall to two decimals before averaging and prints ≈ 0.44; the mean of the unrounded F1 values is 0.439299. The material never says which procedure is intended, and the sheet's own illustration stops after one class's recall.
- **No weighted-F1 anywhere in the material.** The slide reports per-class metrics, macro-F1 and accuracy. The support-weighted average that [[classification-metrics]] records for another course is absent, so there is no summary between equal weighting and sample weighting.
- **No uncertainty statement.** Per-class recall on the homework matrix spans 0.7586 across three classes, and nothing gives a confidence interval, a standard error or a discussion of per-class support, so "good performance" in task 4(b) is argued from the numbers alone.
- **The homework matrix totals 1493 samples while the slide matrix totals 1500.** Recorded as printed; no source explains the difference and none is inferred here.
- **The classes are unnamed.** Neither matrix says what classes 0, 1 and 2 denote, so whether a recall of 0.038462 on class 0 is acceptable cannot be decided from the material.
- **No criterion for task 4(b).** The sheet asks whether performance is good without stating a threshold, a cost model or which metric governs the verdict.
