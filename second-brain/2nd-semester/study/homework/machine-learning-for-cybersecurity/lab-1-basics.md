---
title: "Lab 1 — Credit-Card Fraud with scikit-learn (Notebook Walkthrough)"
tags: [homework, ml-security, semester-2]
course: "Machine Learning for Cybersecurity"
source_count: 2
status: current
last_updated: 2026-10-20
---

# ML for Cybersecurity — Lab 1: Basics (credit-card fraud)

Source: `raw/lectures/Machine Learning for Cybersecurity/Vorlesung/Lab1-Basics-CC.ipynb` — the professor's own Lab 1 notebook, with executed outputs. It walks slides 2.3–2.11 of L2 (`02_Spam.pdf`).

**What could not be checked:** `creditcard.csv` is *not* in the vault, and `lab1/creditcard.csv` is the notebook's own relative path. Nothing here was re-run. Every number below is the notebook's own printed output, quoted.

## Index

1. [Load and inspect](#1-load-and-inspect)
2. [Describe a slice of the fraud class](#2-describe-a-slice-of-the-fraud-class)
3. [Split features from labels, then train from test](#3-split-features-from-labels-then-train-from-test)
4. [Scatter: are the classes separable at all?](#4-scatter-are-the-classes-separable-at-all)
5. [Fit logistic regression, draw the confusion matrix](#5-fit-logistic-regression-draw-the-confusion-matrix)
6. [Metrics and the classification report](#6-metrics-and-the-classification-report)
7. [Scaling: and why the metrics got worse](#7-scaling-and-why-the-metrics-got-worse)
8. [The corrected balancing experiment](#8-the-corrected-balancing-experiment)
9. [What the macro and weighted rows mean](#9-what-the-macro-and-weighted-rows-mean)
10. [Three findings](#10-three-findings)
11. [Open questions](#11-open-questions)

## 1. Load and inspect

```python
df = pd.read_csv('lab1/creditcard.csv')
df.head()
```

`df.head()` returns 5 rows × 31 columns: `Time`, `V1`–`V28`, `Amount`, `Class`. `df.columns` confirms the same index. `df.isnull().sum().max()` returns `np.int64(0)` — no missing values anywhere. `df.info()` reports:

```
RangeIndex: 284807 entries, 0 to 284806
Data columns (total 31 columns):
 #   Column  Non-Null Count   Dtype
 0   Time    284807 non-null  float64
 ...
29   Amount  284807 non-null  float64
 30   Class   284807 non-null  int64
dtypes: float64(30), int64(1)
memory usage: 67.4 MB
```

The point of these four cells is cheap: shape and dtypes before anything else, so a string-typed label or a NaN column is caught while it is still a five-second fix.

## 2. Describe a slice of the fraud class

```python
df[df.Class == 1].V2.describe()
```

```
count    492.000000
mean       3.623778
std        4.291216
min       -8.402154
25%        1.188226
50%        2.717869
75%        4.971257
max       22.057729
Name: V2, dtype: float64
```

`count = 492` is the headline: 492 frauds in 284,807 transactions, i.e. **0.17% positives**. Every metric decision downstream follows from that ratio. (The `V2` slice is arbitrary; the point is the *count*, and the fact that a single feature's distribution differs sharply between the two classes — the fraud mean of 3.62 against an overall mean near 0 is far outside the ±1 band of a standardised PCA component.)

## 3. Split features from labels, then train from test

```python
x = df.drop("Class", axis=1)
y = df.Class
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
```

30 feature columns in, one label out. 20% held out, `random_state=42` so the run is reproducible. This is the same contract as [[ml-pipeline-scikit-learn]] step 5: the split happens *before* any statistic is estimated, so the test set stays genuinely unseen.

## 4. Scatter: are the classes separable at all?

```python
xv = x.values
yv = y.values
plt.scatter(xv[yv==0, 1], xv[yv==0, 2], label="Class 0", alpha=0.5, linewidth=0.2)
plt.scatter(xv[yv==1, 1], xv[yv==1, 2], label="Class 1", alpha=0.5, linewidth=0.2, c='r')
```

Two features (`V1`, `V2`), one scatter per class. The fraud points are a small red cloud inside a huge grey one. The plot does not prove separability — it proves that the minority class exists and is not visually identical to the majority, which is what the lecture uses it for.

## 5. Fit logistic regression, draw the confusion matrix

```python
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_test_pred = model.predict(x_test)
m = confusion_matrix(y_test, y_test_pred)
ax = sb.heatmap(m, annot=True, cmap='Blues')
```

The fit emits:

```
ConvergenceWarning: lbfgs failed to converge after 1000 iteration(s) (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT
Increase the number of iterations to improve the convergence (max_iter=1000).
You might also want to scale the data as shown in: ...
```

**The fit did not converge.** `max_iter=1000` was already the raised value, and the solver hit the limit anyway. scikit-learn only warns; it does not raise, so the model that is scored is the partially-optimised one.

## 6. Metrics and the classification report

```python
precision = precision_score(y_test, y_test_pred)
accuracy  = accuracy_score(y_test, y_test_pred)
recall    = recall_score(y_test, y_test_pred)
f1score   = f1_score(y_test, y_test_pred)
```

```
Accuracy = 0.9992451107756047
Precision = 0.8481012658227848
Recall = 0.6836734693877551
F1 Score = 0.7570621468926554
```

`classification_report(y_test, y_test_pred, digits=4)`:

```
              precision    recall  f1-score   support

           0     0.9995    0.9998    0.9996     56864
           1     0.8481    0.6837    0.7571        98

    accuracy                         0.9992     56962
   macro avg     0.9238    0.8417    0.8783     56962
weighted avg     0.9992    0.9992    0.9992     56962
```

Support is 56,864 negatives and 98 positives: 56,962 total test rows, 98 of them fraud. A constant "no fraud" predictor would score 56,864/56,962 = 99.81%, so the 99.92% accuracy buys 0.11 points over a trivial baseline while the model still misses roughly a third of the frauds. See [[classification-metrics]] for why accuracy is the wrong headline here.

## 7. Scaling: and why the metrics got worse

```python
s = StandardScaler()
x_train = x_train.copy()
x_test = x_test.copy()
x_train["Amount"] = s.fit_transform(x_train[["Amount"]])
x_test["Amount"]  = s.transform(x_test[["Amount"]])
model.fit(x_train, y_train)
```

The scaler is fitted on train and applied to test — the correct order, no leakage (see [[feature-normalization]]). The refit emits **the same `ConvergenceWarning`**: `lbfgs failed to converge after 1000 iteration(s)`. So scaling `Amount` did **not** fix convergence.

The report after scaling:

```
              precision    recall  f1-score   support

           0     0.9994    0.9997    0.9996     56864
           1     0.8025    0.6633    0.7263        98

    accuracy                         0.9991     56962
   macro avg     0.9009    0.8315    0.8629     56962
weighted avg     0.9991    0.9991    0.9991     56962
```

Every positive-class number got **worse**: precision 0.8481 → 0.8025, recall 0.6837 → 0.6633, F1 0.7571 → 0.7263, accuracy 0.99925 → 0.99914. The interpretation is narrow and honest: rescaling `Amount` changes the logistic model's decision boundary, and on this particular dataset that new boundary catches slightly fewer frauds and raises slightly more false alarms. It is one experiment on one dataset, not a verdict on normalisation. The gain the lecture expects from scaling is convergence, and that gain did not materialise either.

## 8. The corrected balancing experiment

The notebook's last block replaces the slides' undersampling with a cleaner construction:

```python
# 1. split on the original (imbalanced) data
x = df.drop("Class", axis=1); y = df.Class
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y)

# 2. undersample the training set only
train = x_train.copy(); train["Class"] = y_train
n_pos = (train.Class == 1).sum()
bal_train = pd.concat([
    train[train.Class == 1],
    train[train.Class == 0].sample(n_pos, random_state=42),
]).sample(frac=1, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(bal_train.drop(columns="Class"), bal_train.Class)
```

Three things are right here, and all three are wrong or absent in the slides:

- `stratify=y` guarantees the same class ratio in train and test, instead of hoping a random 20% split preserves it.
- Only the **training set** is undersampled. The test set stays at its natural 0.17% prevalence.
- The model is then evaluated **twice**: once on a balanced test set built the same way (`bal_test`, cell 24) and once on the untouched, imbalanced `x_test` (cell 25). The second evaluation is the honest one, because it is the score the model would actually get in production, where frauds remain rare.

The final two cells (24 and 25) print **no metric text** — only the rendered heatmap axes (`<Axes: >`). So the notebook gives no printed numbers for the balanced experiment, and none are invented here. The `ConvergenceWarning` appears a third time, on the balanced fit.

This closes the open gap recorded in [[ml-pipeline-scikit-learn]]: the slides never resplit after undersampling, so they have no honest test score for the balanced model. The notebook supplies the honest version — the professor's own corrected procedure, not a student's fix.

## 9. What the macro and weighted rows mean

L3 slide 7 defines them: **support** is the number of test samples in a class; the **macro average** is the direct average of each class's metric; the **weighted average** weights each class's metric by its support.

| Row | Reading |
|---|---|
| `0` (no fraud) | precision 0.9995, recall 0.9998, F1 0.9996 over 56,864 samples |
| `1` (fraud) | precision 0.8481, recall 0.6837, F1 0.7571 over 98 samples |
| `accuracy` | one number over all 56,962 samples: 0.9992 |
| `macro avg` | (0.9995 + 0.8481)/2 = 0.9238 precision, (0.9998 + 0.6837)/2 = 0.8417 recall, F1 0.8783 — every class counts once |
| `weighted avg` | the same numbers pulled towards the majority class by its support — 0.9992 everywhere, identical to accuracy |

The macro row is the honest one for a security detector: it says "treat a caught fraud and a missed fraud as equally weighted errors", which is why macro recall (0.8417) is much closer to the fraud-class recall (0.6837) than the weighted row (0.9992) is. The weighted row looks perfect and tells you almost nothing, because 56,864 majority samples drown the 98 that matter.

## 10. Three findings

**1. The metric discrepancy against the slides is unexplained.** The L2 slides print Accuracy 0.9988939995084443, Precision 0.7868852459016393, Recall 0.4897959183673469, F1 0.6037735849056604. The notebook prints 0.9992451 / 0.8481013 / 0.6836735 / 0.7570621. These are not the same fit: the notebook is better on *every* metric — higher accuracy, higher precision, and much higher recall (0.684 vs 0.490, i.e. roughly 67 of 98 frauds caught instead of 48). Neither source states why. Plausible causes (different scikit-learn version, different solver, a different `random_state` effect) are speculation and are not asserted here. The vault records the discrepancy as an open question rather than resolving it.

**2. `max_iter=1000` was not the fix for convergence.** The vault's concept page previously said the slides raise `max_iter` "so the solver converges". The notebook shows the opposite: the fit still emits `lbfgs failed to converge after 1000 iteration(s)`, and it *still* fails after `StandardScaler` is applied to `Amount`. Raising the iteration cap and normalising one feature were both insufficient; the honest statement is that the solver did not converge and scikit-learn only warned.

**3. The corrected balancing procedure closes the vault's open gap.** `stratify=y` plus undersampling of the training set only plus evaluation on the untouched imbalanced test set is the professor's own version of the experiment, and it fixes the two leakage/validity problems the slides had.

## 11. Open questions

- **Why do the notebook and the slides disagree on every metric?** Both claim to be the same 80/20 split of the same dataset with `random_state=42` and `LogisticRegression(max_iter=1000)`. Unexplained; the only honest answer is that the runs differ in some unrecorded way.
- **What are the balanced model's actual scores?** The last two cells produce heatmaps but no printed metrics, so the balanced run's precision/recall/F1 on the imbalanced test set are unknown from the notebook alone.
- **Would the ConvergenceWarning go away with more iterations, a different solver (`liblinear`, `saga`), or full feature scaling?** The notebook only scales `Amount`; the 28 PCA components are already unit-variance, so the warning is not obviously about `Amount` at all.
- **Does the corrected balancing actually help the fraud class?** Without the printed metrics, the procedure is known to be *valid* but not known to be *better* on this dataset.
- **No cross-validation anywhere.** A single 20% holdout on 492 positives is noisy; the notebook does not quantify the noise.
