---
title: "Mining Software Repositories — Lecture 6 Overview (Studying Bugs and Defect Prediction)"
tags: [topic, mining-software-repositories, semester-2, defect-prediction]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 6 takes defect data seriously: it lays out defect prediction as a pipeline with three
checkable questions, shows why just-in-time prediction is a temporal problem, uses the pipeline
to show that code smells predict defects, and argues that only a cost model tells you whether the
prediction is worth running.

## Core Map

```
Chapter 6 — Studying bugs
│
├── Bugs and MSR
│   ├── "No developer writes code without defects"
│   ├── Defect data tracked in commits, issue trackers, pull requests
│   └── Three families: bug localization, defect prediction, program repair
│
├── Defect prediction in general
│   ├── Pipeline: Input Software -> Output Prediction -> Reaction Correction
│   │       -> Result Less post-release defects
│   ├── Three questions: correct? findable? profitable?
│   ├── Three strategy axes: artefact granularity (file/class/method/line),
│   │       training data (cross-project vs within-project),
│   │       timing (release-level vs just-in-time)
│   └── JIT: training and deployment; temporal aspects
│           -> [[defect-prediction]]
│
├── Temporal aspects of JIT
│   ├── Test data must never be older than training data
│   ├── Labels are known only later: bug at report, location at fix
│   └── Realistic training must use labels known to be noisy
│
├── Internal vs external quality
│   ├── Internal: readability, maintainability, technical debt, code smells
│   ├── External: quality when used and executed; bugs
│   ├── Four models: JIT (process metrics), STATIC (product metrics),
│   │       PMD (smell metrics), Combined
│   ├── Result: statistically significant impact, large effect size
│   └── Feature importance: lines added most important, warning density also high
│
└── Costs of defect prediction
    ├── cost = cost_INIT + cost_EXEC + cost_QA + cost_DEF
    ├── Trivial models: same QA for everything, no QA
    ├── profit = cost_all - cost
    ├── Mandatory condition for prediction to beat trivial models
    └── Metrics do not correlate with costs; cost model does
            -> [[defect-prediction-cost-model]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[defect-prediction]] | A pipeline with three questions: are the predictions correct, can developers find them, and is it profitable |
| [[defect-prediction-cost-model]] | Cost = INIT + EXEC + QA + DEF; profit comes from comparing against trivial models |
| [[szz-algorithm]] | The label source for defect prediction, whose temporal behaviour constrains the train/test split |
| [[msr-statistical-methods]] | Significance, effect size, and confidence intervals, which carry the smells-to-defects result |

## Lecture Structure

1. **Bugs and MSR** — defects are unavoidable and already recorded; MSR is well suited to
   investigating them; the three families of work (bug localization, defect prediction, program
   repair), with the focus on defect prediction.
2. **The prediction pipeline** — the four-cell diagram with the three questions hung off it, and
   the terminology.
3. **General strategies** — the three axes of diversity: which artefacts, whose training data,
   and when prediction happens; the cross-project example and the problem of combining models
   into one output.
4. **Just-in-time prediction** — the training pipeline (issue tracker plus SZZ over the VCS
   yields bug-introducing and clean commits; the model predicts the next commit) and the
   deployment pipeline (a new commit triggers a prediction, which triggers review or only
   rudimentary checks), plus model monitoring.
5. **Temporal aspects** — test data must never be older than training data, otherwise one
   predicts the past from the future; labels arrive late; and the consequence that a realistic
   setting must train on noisy labels.
6. **Internal versus external quality** — the definitions, the research question about
   correlation, and the four model variants (process metrics, product metrics, PMD smell
   metrics, and all three together).
7. **Reading the comparison** — statistically significant impact, large effect size; the three
   interpretations depending on whether performance falls, holds, or rises; and feature
   importance showing lines added as strongest, with PMD warning density also high.
8. **Costs** — the cost factors attached to each pipeline cell, the general cost model, the
   trivial models that define the floor, the profit formula, the estimation of QA cost per line
   and defect loss, and the condition for beating a trivial model.
9. **Do metrics predict cost?** — the two model families (bootstrap within-project for the
   relationship, cross-project and cross-version for generalization), the log-normal
   distributions of cost-saving potential, and the finding that correlations do not generalize
   because costs vary strongly between instances.

## Exam-Relevant Points

1. **The three questions are the structure of the chapter**: correctness (performance metrics),
   reaction (can developers find predicted defects), and profitability (the cost model).
2. **Defect prediction is diverse along three axes** — artefact granularity, cross- versus
   within-project training, and release-level versus just-in-time timing.
3. **JIT is a temporal problem in two places**: the train/test split must respect time order, and
   the labels are unavailable when the model would have to be used.
4. **The realistic setting therefore trains on noisy labels.** That is the point of the
   train/test slide, not an oversight.
5. **The smells-to-defects result is a design, not a coincidence**: four models differ only in
   which feature family they see, and the combined model with smell features performs
   significantly better.
6. **Feature importance is about decision usage, not causal contribution**, and the slides note
   it should be controlled for correlations.
7. **The cost model is the only thing that answers "is this profitable"**, and performance
   metrics do not correlate with cost savings.
8. **Bootstrap-based relationships do not generalize** across project or version boundaries,
   while the cost model does, because it prices each artefact and defect individually.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-3]] — where the defect data is collected.
- [[mining-software-repositories-lecture-7]] — the statistics behind the comparison.
- [[defect-prediction]] — the pipeline and its strategies.
- [[defect-prediction-cost-model]] — the cost and profit model.
- [[szz-algorithm]] — the labelling that makes JIT possible.
- [[software-metrics]] — the metrics used as prediction features.
- [[msr-statistical-methods]] — significance, effect size, and confidence intervals.

## Open Questions

- **The cost constants C_INIT, C_EXEC, C_QA, C_DEF are never given for a real project**, so no
  numerical profit example can be reproduced from the slides.
- **The condition for beating a trivial model** is an inequality with an unknown C, and the
  slides do not show where a practitioner would obtain C.
- **The absolute number of projects or commits in the smells-versus-defects experiment is not
  stated**.
- **"Class level imbalance" as the bias in test data** is mentioned without a method for
  correcting it.
