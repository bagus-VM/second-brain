---
title: "The ML Pipeline in scikit-learn: Credit-Card Fraud Walkthrough"
tags: [concept, ml-security, semester-2, tooling]
course: "Machine Learning for Cybersecurity"
source_count: 2
status: current
last_updated: 2026-10-20
prerequisites: ["[[classification-metrics]]"]
---

## One-line Summary

L2's credit-card example is the supervised workflow end to end: inspect with pandas, split features from labels, hold out a test set, fit, predict, score, then fix scale and class balance — with two places where careless ordering silently inflates the score.

## Core Intuition

The pipeline is a sequence of contracts, not of function calls. `fit` learns parameters from data; `transform` applies them. Every leakage bug is that contract broken: something that should have been learned from the training set was learned from everything, so the test set is no longer unseen. Split before you scale, split before you resample, fit on train and only transform on test.

## Formal Definition / Statement

| # | Step | Call | Purpose |
|---|---|---|---|
| 1 | Load | `pd.read_csv('./creditcard.csv')` | 284,807 rows × 31 columns: `Time`, `V1`–`V28`, `Amount`, `Class` |
| 2 | Inspect | `df.head()`, `df.columns`, `df.isnull().sum().max()`, `df.info()` | shape, dtypes, missing values first |
| 3 | Describe a slice | `df[df.Class == 1].Amount.describe()` | 492 frauds; mean 122.21, median 9.25, max 2,125.87 |
| 4 | Features / labels | `x = df.drop("Class", axis=1)`, `y = df.Class` | separate what the model sees from what it predicts |
| 5 | Split | `train_test_split(x, y, test_size=0.2, random_state=42)` | 80/20 holdout, reproducible |
| 6 | Look | `plt.scatter` of features `[1]`, `[2]`, coloured by class | are the classes separable at all |
| 7 | Fit | `LogisticRegression(max_iter=1000).fit(x_train, y_train)` | learn coefficients; `max_iter` was raised to 1000, but L2's Lab 1 notebook shows the solver **still fails to converge** at that limit |
| 8 | Predict and score | `model.predict`, `confusion_matrix`, seaborn `heatmap` | errors by type, not a percentage |
| 9 | Scale | `StandardScaler`: `fit_transform` on train, `transform` on test | `Amount` is in currency units, the `V` columns are not |
| 10 | Rebalance | shuffle, take `num_fraud` non-fraud rows, `concat`, shuffle | 492 : 284,315 is 0.17% positives |
| 10b | Rebalance (corrected, in the Lab 1 notebook) | `train_test_split(..., stratify=y)`, undersample **the training set only**, evaluate on the untouched imbalanced test set | the professor's own corrected version of step 10 — see [[lab-1-basics]] |

```python
x = df.drop("Class", axis=1)
y = df.Class
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
```

```python
s = StandardScaler()
x_train["Amount"] = s.fit_transform(x_train[['Amount']])
x_test["Amount"]  = s.transform(x_test[['Amount']])
```

`fit_transform` learns mean and standard deviation *and* applies them; `transform` applies already-learned values. Fitting on test would leak the test distribution into preprocessing.

```python
df = df.sample(frac=1)                       # shuffle
num_fraud = len(df[df.Class == 1])
fraud_entries = df[df.Class == 1]
non_fraud_entries = df[df['Class'] == 0][:num_fraud]
sub_df = pd.concat([fraud_entries, non_fraud_entries])
random_undersampled_df = sub_df.sample(frac=1, random_state=42)
```

The shuffle before slicing matters: without it, `[:num_fraud]` takes the first 492 non-fraud rows in file order — the earliest transactions in time, a biased sample.

**The corrected version, from L2's Lab 1 notebook.** The slides' recipe resamples and then scores on data whose balance has changed. The notebook splits with `stratify=y`, undersamples the *training set only*, and evaluates on the untouched imbalanced test set:

```python
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y)

train = x_train.copy(); train["Class"] = y_train
n_pos = (train.Class == 1).sum()
bal_train = pd.concat([
    train[train.Class == 1],
    train[train.Class == 0].sample(n_pos, random_state=42),
]).sample(frac=1, random_state=42)
model.fit(bal_train.drop(columns="Class"), bal_train.Class)
```

The test set keeps its natural 0.17% prevalence, so the score is the one a deployed model would actually get. The notebook evaluates twice — on a balanced test set and on the original imbalanced one — but prints no metric text for either, only heatmaps.

## Key Properties

- **`fit` learns, `transform` applies.** Every leakage bug violates that split.
- **The split precedes everything that learns.** Scaling and resampling both estimate statistics, so both come after `train_test_split`.
- **The label is 0.17% of the data**, so accuracy is uninformative before a model is even trained.
- **Each step is inspectable.** `head`, `info` and `describe` exist to catch dtype and missing-value problems before they reach the model.

## Worked Example

The heatmap is annotated with raw counts, axes labelled False/True. From L2's metrics the matrix is TN 56,851 · FP 13 · FN 50 · TP 48. The plot makes the imbalance visible in a way accuracy hides: the top-left cell dwarfs everything, so a model predicting "never fraud" looks almost identical on the diagonal. That is why the four metric calls follow the plot.

**A second run of the same pipeline.** The Lab 1 notebook repeats the whole workflow on the same dataset and prints different numbers: Accuracy 0.9992451107756047, Precision 0.8481012658227848, Recall 0.6836734693877551, F1 0.7570621468926554, with a classification report whose positive class has support 98 and precision 0.8481 / recall 0.6837 / F1 0.7571. The notebook's run is better on *every* metric than the slides' run, including much higher recall (0.684 vs 0.490), so the two are not the same fit. **Neither source states why.** The difference is recorded as an open question rather than explained; see [[classification-metrics]] and [[lab-1-basics]].

## Common Pitfalls

- **Fitting the scaler on the test set.** The classic leak: test statistics must never inform preprocessing.
- **Touching test data during training.** L2 states the rule plainly: test data is for testing, never for training.
- **Resampling before splitting.** If undersampling runs on the whole frame and the split follows, majority rows can land in both halves. The slide applies undersampling as a separate experiment, so its numbers are not comparable to the imbalanced run.
- **Forgetting to shuffle before slicing.** `df[df.Class == 0][:n]` is ordered, not random.
- **Using the default `max_iter`.** Logistic regression on unscaled features may fail to converge, and scikit-learn only warns. The Lab 1 notebook shows that raising it to 1000 was *not* sufficient: `lbfgs failed to converge after 1000 iteration(s)` still appears, and it appears again after `StandardScaler` is applied to `Amount`.
- **Mutating the original frame.** The slide calls `.copy()` first; skipping it edits `x_train` in place.

## Connections

- [[classification-metrics]] — the four numbers step 8 produces.
- [[lab-1-basics]] — the professor's own Lab 1 notebook: the same pipeline with executed outputs, a second (different) metric set, the surviving `ConvergenceWarning`, and the corrected balancing procedure.
- [[naive-bayes-text-classification]] — same split discipline, different representation.
- [[ml-learning-paradigms]] — supervised learning, instantiated.
- [[ml-for-security-domains]] — process behaviour is where this fraud example belongs.
- [[feature-normalization]] — what step 9 does, and what it did and did not fix here.

## Open Questions

- **Why do the slides and the Lab 1 notebook produce different metrics from the same pipeline?** The notebook's numbers (accuracy 0.9992, precision 0.8481, recall 0.6837, F1 0.7571) are better than the slides' (0.9989 / 0.7869 / 0.4898 / 0.6038) on every metric, so the two runs are not the same fit. Neither source explains the difference.
- **Why does `lbfgs` still not converge after 1000 iterations, and why does scaling `Amount` not fix it?** The 28 `V` components are already unit-variance, so the warning is probably not about `Amount` at all. An alternative solver (`liblinear`, `saga`) or full feature scaling is untested.
- **Resolved — the slides never resplit after undersampling.** The Lab 1 notebook supplies the honest version: split with `stratify=y`, undersample the *training set only*, and score on the untouched imbalanced test set. It is the professor's own corrected procedure, not a student's fix. (The notebook prints no metric text for that final evaluation, only heatmaps, so the balanced model's numbers are still unknown.)
- **Partly resolved — `stratify`.** The notebook's corrected split uses `stratify=y`; the slides do not. What remains open is how noisy a single 20% holdout is with 492 positives — there is no cross-validation in either source.
