---
title: "Information Leakage"
tags: [concept, introduction-to-deep-learning, semester-2, evaluation, machine-learning]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[cross-validation]]", "[[ml-data-and-iid-assumption]]"]
---

## One-line Summary
Any information from the validation or test set that reaches training inflates the reported score
without improving the model — and the leaks are usually in the preprocessing, the splitting, or the
number of times you looked at the test set.

## Core Intuition

The held-out score is supposed to answer one question: how will this model do on data it has never
seen? Leakage breaks the premise. Some part of the held-out set — its mean, its variance, its feature
ranking, its labels, or just the fact that forty-nine other configurations were rejected — has been
folded back into the training process, and the number that comes out is optimistic in a way that is
invisible from the number itself.

The dangerous leaks are procedural, not exotic. Normalising before splitting is the canonical one and
the lecture draws it side by side with the correct version. The reason it matters is quantitative:
the mean and standard deviation of the full dataset encode the test rows. A model fitted to data
scaled with knowledge of the test rows has been given a small amount of the answer.

Then there is the leakage that has nothing to do with code: **using the test set as a decision
instrument**. Try fifty hyperparameter settings, report the best test score, and the reported number
is a maximum over fifty noisy measurements — it estimates the best of fifty, not the model. The
lecture's own three-way split (training / validation / test) is the structural fix, and it exists
precisely for this reason.

The lecture closes the section with the contemporary version: if the benchmark is on the web and the
web trained the model, the score may measure memorisation. Same concept, larger scale.

## Formal Definition / Statement

**Definition, slide 37:** "We use information that will not be available at prediction time" —
"leak information from the validation/test set into the training".

**The lecture's worked case, preprocessing:**

```
WRONG:  whole dataset -> normalise with mean/std of all data -> split into train/test
        -> train & evaluate
RIGHT:  whole dataset -> split into train/test
        -> mean/std from training data only -> normalise both -> train & evaluate
```

The slide prints **"Do not do that!"** under the wrong pipeline.

**The quiz, slide 38 — "Where is the leak?"** Five cases, with no answers on the slide:

1. We select the 20 best features using the whole dataset, then run cross-validation
2. Patient study with several scans per patient: we split the scans randomly into training and test data
3. Predict loan default using the feature "number of reminder letters sent"
4. We try 50 hyperparameter settings and report the best test set score
5. We compute mean and standard deviation on the training data and use them to normalise training and
   test data

**Answers, worked out here** (the slide gives none):

| Case | Leak? | Why |
|------|-------|-----|
| 1 | **Yes** | Feature selection saw every row, including the folds that later score the model. The selected 20 are chosen partly because they fit the test rows. Selection must happen inside each fold. |
| 2 | **Yes** | The same patient appears in training and test. The model can recognise the patient rather than the pathology. Split by patient. |
| 3 | **Yes** | "Number of reminder letters" is a *consequence* of the default, not a predictor available at decision time — a classic target leak. It is only observable after the outcome it predicts. |
| 4 | **Yes** | The test set was used to choose. The number reported is the maximum of 50 estimates, so it is biased upward; a validation split (or nested cross-validation) is required. |
| 5 | **No — this is the correct procedure** | Statistics computed on training data only, then applied to both. This is exactly the lecture's RIGHT pipeline. It looks like the others and is the one clean case. |

**Leakage in the age of LLMs, slide 39:**

- Benchmarks are published on the web, and web text is used to train LLMs.
- **Test set contamination**: the model may have seen the test questions and their answers during
  training.
- Scores then measure **memorisation** rather than generalisation.
- Evidence: on a fresh re-creation of a popular math benchmark (GSM8k → **GSM1k**), several models
  score clearly lower than on the original.
- **Countermeasures**: new, held-back or continuously updated benchmarks; contamination checks;
  "canary strings" in benchmark files.
- Citations: Sainz et al., *NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination
  for each Benchmark*, Findings of EMNLP 2023; Zhang et al., *A Careful Examination of Large Language
  Model Performance on Grade School Arithmetic*, 2024.

## Key Properties

- **Leakage is invisible from the score.** An inflated estimate looks like a good estimate; there is
  no error message.
- **It is a property of the *procedure*, not of the model.** The same model trained under a leaky and
  a clean pipeline is the same model; only the reported number differs.
- **Its size scales with how much information is aggregated across the split.** A global mean is a
  small leak; a feature ranking over the whole dataset is large; the labels themselves are fatal.
- **The fix is always "fit on training data, apply everywhere".** Scalers, imputers, encoders,
  feature selectors, resampling — every step that *learns* from data must be inside the training side.
- **Repeated use of the test set is leakage.** Leakage case 4 is not a coding error, it is a
  statistical one, and it is the reason for the validation split.
- **Grouped data leaks through the split.** Case 2 is the [[ml-data-and-iid-assumption]] problem
  seen from the evaluation side.
- **In the LLM setting the leak is in the corpus, not in the pipeline.** No amount of careful
  splitting helps if the model was trained on the benchmark.
- **The lecture's countermeasures are all about *withholding* information**: held-back benchmarks,
  continuous updates, contamination checks, canary strings.

## Worked Example

The lecture gives no numbers, so here is the arithmetic of the smallest leak type — a global
normalisation — computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`'s
neighbouring material and reproduced here by hand.

Take six values split 4 training / 2 test:

```
train: 10, 12, 14, 16        test: 100, 102
```

**Leaky**: the global mean is (10+12+14+16+100+102)/6 = 42.33. Dividing everything by it compresses
the training rows by a factor of about 4.2 and puts them all near 0.24–0.38, while the test rows land
at 2.36 and 2.41. The training data has been transformed using a statistic that the test rows
dominated.

**Clean**: the training mean is 13.0. Training rows become 0.77, 0.92, 1.08, 1.23; the test rows
become 7.7 and 7.8. Every value is measured against something computed without looking at the test set.

The two pipelines produce wildly different inputs for the same model, and only the second one answers
the question that was asked. **The diagnostic question is always the same**: could this number have
been computed if the test set did not exist? If the answer is no, the step belongs inside the
training side of the split.

## Common Pitfalls

- **Normalising, imputing, or encoding before splitting.** The single most common leak, and the one
  the lecture draws explicitly.
- **Selecting features on the whole dataset.** Case 1: selection is a fitting procedure and must run
  inside each fold.
- **Random splits on grouped data.** Case 2: several scans per patient, several sessions per user.
- **Keeping a feature that is a consequence of the target.** Case 3: "number of reminder letters"
  cannot exist before the default it predicts.
- **Tuning against the test set.** Case 4: the reported number is the best of many, so it is a maximum.
- **Reading case 5 as a leak because it mentions the test set.** It is the correct procedure; the
  test set is *applied to*, not *fitted on*.
- **Trusting a benchmark that is public and old.** Slide 39: contamination makes a high score
  ambiguous between generalisation and memorisation.
- **Assuming a big dataset protects against leakage.** Leakage inflates the estimate regardless of
  size; more rows do not undo the fact that the split was crossed.

## Connections

- [[cross-validation]] — the procedure leakage most often corrupts; the folds must be built before any
  learning step, and grouped or time-ordered when the data demands it.
- [[ml-data-and-iid-assumption]] — the assumption whose violation produces leakage cases 2, and the
  temporal/covariate shift material adjacent to this slide.
- [[feature-normalization]] — the specific preprocessing step the lecture's worked example uses.
- [[ml-pipeline-scikit-learn]] — the tooling where `train_test_split` before `StandardScaler` is the
  canonical bug, and where pipelines exist to prevent it.
- [[class-imbalance]] — oversampling and resampling performed before the split are leaks of exactly
  this kind.
- [[threats-to-validity]] — the Mining Software Repositories course's version of the same concern,
  applied to empirical studies of software rather than to classifiers.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **The slide gives no answers to its own quiz.** All five verdicts on this page are worked out from
  the lecture's RIGHT/WRONG pipeline and the i.i.d. material; the slide prints the cases and stops.
- **No leak-detection method is offered.** Contamination checks and canary strings are named as
  countermeasures for the LLM setting but not described.
- **How large a leak must be to matter is not quantified** — no bound, no experiment, no sensitivity
  analysis.
- **The GSM1k result is cited without numbers.** "Clearly lower" is the slide's phrasing; the
  difference in scores is not given.
- **No statement on whether nested cross-validation is expected.** The three-way split implies the
  problem case 4 describes, but the lecture does not name the nested solution.