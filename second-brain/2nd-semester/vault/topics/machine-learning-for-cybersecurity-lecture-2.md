---
title: "Machine Learning for Cybersecurity — Lecture 2 Overview (Classification and spam)"
tags: [topic, ml-security, semester-2, naive-bayes]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[machine-learning-for-cybersecurity-lecture-1]]"]
---

## One-line Summary
The first working pipeline of the course: pandas → scikit-learn → metrics on credit-card fraud, then
Naive Bayes derived from Bayes' rule for text classification, then the spam assignment that makes you
build both.

## Core Map

```
Lecture 2 — Simple classification: basics, spam
│
├── 1. Python + ML basics on credit-card fraud     -> [[ml-pipeline-scikit-learn]]
│   ├── pandas: read_csv, head, columns, isnull, info, describe, filter
│   ├── train_test_split(0.2, random_state=42)
│   ├── matplotlib scatter of two features by class
│   ├── LogisticRegression(max_iter=1000).fit / .predict
│   ├── confusion_matrix + seaborn heatmap
│   ├── StandardScaler (fit on train, transform on test)
│   └── random undersampling of the majority class
│
├── 2. Metrics                                      -> [[classification-metrics]]
│   ├── accuracy / precision / recall / F1
│   └── the printed numbers: acc 0.9989, P 0.787, R 0.490, F1 0.604
│
└── 3. Naive Bayes for text                         -> [[naive-bayes-text-classification]]
    ├── bag of words
    ├── Bayes' rule, MAP decision
    ├── conditional independence
    ├── Laplace smoothing (+1)
    └── log-space to avoid underflow
        │
        └── Homework: LingSpam classifier + reading assignment
            -> study/homework/machine-learning-for-cybersecurity/spam-classifier/
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[ml-pipeline-scikit-learn]] | The lecture's exact workflow, step by step, including the two data-leakage traps (scaler fitted on test data; test data used for training) |
| [[classification-metrics]] | The four metrics, the confusion matrix behind them, and why 99.89% accuracy on imbalanced data is not a result |
| [[naive-bayes-text-classification]] | Bayes' rule → MAP → conditional independence → Laplace smoothing → log-space |

## Lecture Structure

1. **Data preparation with pandas** — load, inspect, query, check for nulls.
2. **Train/test split and visualisation** — `train_test_split`, scatter of features coloured by class.
3. **Training a model** — logistic regression, confusion matrix heatmap.
4. **Metrics** — accuracy, precision, recall, F1, and the printed values on the credit-card set.
5. **Better preprocessing** — standard scaling of `Amount`, then random undersampling because the
   dataset is highly unbalanced.
6. **Theory: Naive Bayes** — text classification problem, bag of words, Bayes' rule, the MAP
   classifier, why the joint probability cannot be estimated directly, the independence assumption,
   Laplace smoothing, and log probabilities.
7. **Homework** — implement a spam classifier (LingSpam, 2000-word vocabulary,
   `MultinomialNB`) and read Kontsewaya et al. 2021 with six guiding questions.

## Exam-Relevant Points

1. **Reproduce the metrics definition and the trade-off**: precision answers "of those I flagged, how
   many were right", recall answers "of the real ones, how many did I find". F1 is their harmonic mean
   and is dominated by the smaller value.
2. **Read a confusion matrix both ways** — from the matrix to the metrics and back.
3. **The credit-card numbers are a trap**: 0.9989 accuracy with 0.4898 recall means the model misses
   half the frauds. Say why accuracy is the wrong metric on a 0.17%-positive dataset.
4. **Derive Naive Bayes**: from `c_MAP = argmax P(d|c)P(c)` to the product of per-word probabilities,
   name the independence assumption as an assumption, and explain what breaks without Laplace
   smoothing (a single unseen word zeroes the product).
5. **Know why log-space is used**: multiplying thousands of probabilities below 1 underflows to zero.

## Connections

- [[machine-learning-for-cybersecurity-lecture-1]] — the terminology and task taxonomy used here.
- Homework solutions and code: `study/homework/machine-learning-for-cybersecurity/spam-classifier/`
  (measured on the real LingSpam dataset: accuracy 0.9897, precision 1.0000, recall 0.9388, F1 0.9684,
  against an 0.8316 always-ham baseline).
- [[python-environment-management]] / [[python-for-deep-learning]] — the same toolchain discipline,
  taught from the deep-learning side.

## Open Questions

- The lecture's credit-card numbers come from one split with no cross-validation, and the
  undersampling is applied *after* the metrics run — so the two configurations are not comparable.
  The slides do not acknowledge this.
- The reading assignment asks what ROC curve the Kontsewaya paper uses. The paper does not mention
  ROC or AUC at all — the question does not match the source.
- Which alternative to Naive Bayes the course expects for spam (the paper compares five) is unstated.
