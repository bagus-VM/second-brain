---
title: "Machine Learning for Cybersecurity — Lecture 3 Overview (Metrics, ROC, KNN and regression)"
tags: [topic, ml-security, semester-2, evaluation]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[machine-learning-for-cybersecurity-lecture-2]]"]
---

## One-line Summary
Metrics and ROC curves get their own pass, KNN and the two regressions are added to the toolbox, and
the ROC is then re-examined through a 3-KNN classifier whose discrete scores give it only three
operating points.

## Core Map

```
Lecture 3 — More ML Basics
│
├── 1. Metrics and Receiver Operating Curves
│   ├── accuracy / precision / recall / F1 revisited  -> [[classification-metrics]]
│   ├── multi-class confusion matrix (5 classes)      -> [[classification-metrics]]
│   │     0-normal, 1-Probe, 2-DoS, 3-U2R, 4-R2L
│   │     per-class recall + per-class precision row
│   ├── support / macro average / weighted average
│   └── ROC basics                                    -> [[roc-curve]]
│         ├── TPR = TP/(TP+FN), FPR = FP/(FP+TN)
│         ├── border cases: all-0, all-1, perfect, random
│         ├── binary classifier = one point; connect-the-dots "not very useful"
│         ├── probabilistic classifier = step function
│         ├── threshold optimisation: maximise TPR + (1-FPR), slope +1 line
│         └── AUC (larger = better, slope-independent)
│
├── 2. More ML basics
│   ├── K Nearest Neighbors                            -> [[k-nearest-neighbors]]
│   │     ├── Euclidean / Manhattan / Minkowski distance
│   │     ├── no training phase; vote among K nearest
│   │     ├── feature weighting, feature normalisation -> [[feature-normalization]]
│   │     └── advantages / disadvantages
│   ├── Linear Regression                              -> [[linear-regression]]
│   │     ├── f(x) = b + w1x1 + ... + wdxd
│   │     ├── least squares E(w) = sum (yi - wT xi)^2
│   │     ├── normal equation w = (XTX)^-1 XTY
│   │     └── cost of the closed form -> SGDRegressor
│   └── Logistic Regression                            -> [[logistic-regression]]
│         ├── sigmoid f(x) = 1/(1+e^-x) -> probability
│         ├── squared error fails (local minima) -> Log Loss
│         └── no closed form -> iterative optimisation
│
├── 3. ROC revisited (with KNN)
│   ├── 3-KNN: scores 0/1/2/3 -> 3 discrete TPR/FPR pairs, no steps,
│   │          shape independent of test-set size, AUC = 0.82
│   └── quiz: 1-KNN -> score always 0 or 1 -> one operating point + 2 corners
│
└── 4. Upcoming student presentations (network intrusion detection)
    ├── Apruzzese, Laskov, Schneider — SoK: Pragmatic Assessment of ML for NIDS, EuroS&P 2023
    ├── Fu, Li, Xu — HyperVision, NDSS 2023
    └── Jacobs, Beltiukov, Willinger et al. — The Emperor has no Clothes, ACM CCS 2022
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[classification-metrics]] | The multi-class confusion matrix with per-class recall and precision, and what support / macro average / weighted average mean |
| [[roc-curve]] | TPR vs FPR swept over a threshold; step function for probabilistic classifiers, single point for hard ones, AUC as summary |
| [[k-nearest-neighbors]] | Vote among the K closest training samples; no training phase; discrete scores give a three-point ROC |
| [[feature-normalization]] | StandardScaler vs MinMaxScaler, and why the fit must happen on the training split only |
| [[linear-regression]] | Least squares and the normal equation w = (XᵀX)⁻¹XᵀY, plus the cost of inverting XᵀX |
| [[logistic-regression]] | Sigmoid on top of a linear score, log loss instead of squared error, iterative optimisation |

## Lecture Structure

1. **Metrics and ROC** — accuracy, precision, recall and F1 revisited from part 2; the multi-class
   confusion matrix for five intrusion classes with per-class recall and precision; support, macro
   average and weighted average; then the full ROC treatment: axes, border cases, what a binary
   classifier contributes versus a probabilistic one, threshold optimisation by the slope-+1 rule, and
   AUC.
2. **K Nearest Neighbors** — the "tell me about your friends" idea; Euclidean, Manhattan and Minkowski
   distance; the three-step procedure (distance to all, take K nearest, take the most frequent class);
   choosing K; feature weighting; feature normalisation with `StandardScaler` and `MinMaxScaler`;
   advantages and disadvantages.
3. **Linear Regression and Logistic Regression** — the linear model f(x) = b + wᵀx, least squares, the
   matrix derivation of the normal equation and its computational cost, gradient descent for large
   data; then the categorical case: the sigmoid, why squared error stops working, log loss, and the
   absence of a closed-form solution.
4. **The comparison table** — training effort, classification effort and dynamic model update for
   Naive Bayes, KNN and logistic regression, with the slide's own caveat that Naive Bayes's apparent
   superiority rests on a feature-independence assumption that may not hold.
5. **ROC revisited (with KNN)** — the 3-KNN curve: three discrete operating points, no steps, shape
   independent of the test-set size, AUC = 0.82; then the quiz on the 1-KNN.
6. **Student presentations** — three network-intrusion-detection papers, one to be presented in
   20 minutes on Nov 3 (or Oct 29).

## Exam-Relevant Points

1. **The multi-class confusion matrix.** True labels (rows): 0-normal, 1-Probe, 2-DoS, 3-U2R, 4-R2L.
   Predicted labels (columns) in the same order. Read off the slide:

   | True \ Predicted | 0-normal | 1-Probe | 2-DoS | 3-U2R | 4-R2L | Recall |
   |---|---|---|---|---|---|---|
   | **0-normal** | 59,199 | 1,095 | 0 | 169 | 129 | 0.977 |
   | **1-Probe** | 182 | 3,824 | 19 | 8 | 133 | 0.918 |
   | **2-DoS** | 39,740 | 662 | 188,984 | 35 | 432 | 0.822 |
   | **3-U2R** | 142 | 0 | 0 | 40 | 46 | 0.175 |
   | **4-R2L** | 14,262 | 27 | 1 | 634 | 1,265 | 0.078 |
   | **Precision** | 0.521 | 0.682 | 1.000 | 0.045 | 0.631 | |

   The pattern to explain: the two rare classes (U2R, R2L) are the ones that fail, with recall 0.175
   and 0.078, and U2R also has the worst precision in the table (0.045) because 634 of the 886
   samples predicted as U2R were actually R2L. DoS is the precision case — 1.000, because almost
   nothing is mistaken for it (20 of 189,004 predictions as DoS are wrong) — but its *recall* is
   only 0.822, so 40,869 real DoS attacks were missed. High precision and poor recall are
   independent facts, and a security detector needs both.
2. **Support, macro average, weighted average** — support is the number of test samples of a class
   (the row sums: 60,592 / 4,166 / 229,853 / 228 / 16,189, total 311,028); macro average is the
   direct average of the per-class metrics; weighted average weights the metrics by support. Macro
   average treats the 228-sample U2R class exactly like the 229,853-sample DoS class; weighted
   average does not, and therefore looks far better on this matrix.
3. **The three shapes of ROC.** A hard binary classifier is a single point (connect-the-dots adds no
   information over a confusion matrix); a probabilistic classifier is a step function; and a 3-KNN,
   whose score is a count, has exactly three TPR/FPR pairs and no steps — with the shape independent
   of the test-set size.
4. **The 1-KNN quiz answer**: the score is always 0 or 1, so there is one operating point (the hard
   classifier) plus the two trivial corners — the same as any non-probabilistic binary classifier.
5. **The comparison table, verbatim:**

   | Algorithm | Computational Effort (Training) | Computational Effort (Classification) | Dynamic Model Update |
   |---|---|---|---|
   | Naive Bayes | Low | Low | Easy |
   | KNN | Low | High | Easy |
   | Logistic Regression | Moderate | Low | Complex (Online Learning) |

   And the slide's caveat: Naive Bayes looks like the "best" approach in this table, but it assumes
   independence of all features, which might not hold in real-world scenarios, and therefore cannot
   capture complex relationships between features.
6. **The linear → logistic hand-off.** A linear function is unbounded, so it cannot be a probability;
   the sigmoid supplies the bound, and with the non-linearity the squared-error cost stops being
   suitable, so the cost becomes log loss and the closed form disappears.
7. **The three papers and the assignment**: select one, present the key insights in 20 minutes on
   Nov 3 (or Oct 29).

   | Paper | Venue | Link |
   |---|---|---|
   | Apruzzese, Laskov, Schneider — *SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection* | IEEE EuroS&P 2023 | https://arxiv.org/pdf/2305.00550 |
   | Fu, Li, Xu — *Detecting Unknown Encrypted Malicious Traffic in Real Time via Flow Interaction Graph Analysis* (HyperVision) | NDSS 2023 | https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023_s80_paper.pdf |
   | Jacobs, Beltiukov, Willinger et al. — *AI/ML for Network Security: The Emperor has no Clothes* | ACM CCS 2022 | https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf |

## Connections

- [[machine-learning-for-cybersecurity-lecture-2]] — the metrics and the credit-card pipeline this
  lecture extends.
- [[machine-learning-for-cybersecurity-lecture-1]] — the task taxonomy the new algorithms slot into.
- [[naive-bayes-text-classification]] — the L2 classifier, and the first row of the comparison table.
- [[ml-pipeline-scikit-learn]] — where the logistic regression and the scalers from this lecture
  appear in code.
- [[ml-task-taxonomy]] — classification and regression as the two task families used here.
- [[ml-learning-paradigms]] — KNN as instance-based learning, logistic regression as parametric.
- [[roc-curve]] — the dedicated page for the ROC material; this lecture is where it is first derived.
- [[machine-learning-for-cybersecurity]] — the course page: portfolio weights, topic list, lecture index.

## Open Questions

- The lecture does not name the dataset behind the multi-class confusion matrix. The class names
  (normal, Probe, DoS, U2R, R2L) are the standard network-intrusion attack categories, but no source
  is given, so no dataset can be attributed.
- The slide carries a single "Score: 0.457" next to the multi-class matrix without saying which
  metric or averaging it corresponds to.
- The rule of thumb for choosing K is garbled on the slide ("Choose K as N, with N = number of samples
  in training set"), which cannot be literal; the intended heuristic is not recoverable.
- Whether the 3-KNN AUC of 0.82 is computed on the multi-class matrix or a binary projection of it is
  not stated.
- No experiment is shown for KNN, linear regression or logistic regression on the intrusion or
  credit-card data, so every claim about their relative quality is asserted rather than measured.
- The "Dynamic Model Update: Complex (Online Learning)" entry for logistic regression is never
  explained; no online variant is introduced.
- How the three assigned papers map onto the algorithms of this lecture — which paper evaluates which
  classifier — is left entirely to the presenters.
