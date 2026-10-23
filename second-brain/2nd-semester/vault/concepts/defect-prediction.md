---
title: "Defect Prediction"
tags: [concept, mining-software-repositories, semester-2, defect-prediction]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]", "[[szz-algorithm]]"]
---

## One-line Summary

Defect prediction learns from historic defect data to flag which software artifacts are likely
defective, and in the just-in-time variant it must use the labels that were actually available
at the time the prediction was made.

## Core Intuition

The lecture's framing for the chapter is that defects are a first-class data source:

- "No developer writes code without defects"
- "No non-trivial piece of software is without defects"
- Possible exception: "systems in which millions or more are invested into proving the quality as
  is, e.g., often the case for space exploration"

And defect data is already tracked: "In changes through commits and their (descriptive) messages",
"In issue tracking systems", "In pull requests". "MSR is a very good tool to investigate the
nature of defects!"

The lecture is explicit that defect data work is not one thing. Chapter 2's contribution was
data-related: "Identifying bug fixing commits", the "SZZ algorithm to identify bug introducing
changes". What this chapter adds is what you *do* with such data:

- "Localize defects, e.g., based on an issue description" — **bug localization**
- "Learn to identify defects within code" — **defect prediction**
- "Learn to fix defects based on the bug fixing commits" — **program repair**, "often seen as a
  topic independent of MSR, as there are also non-MSR based approaches for this"

"Within this lecture, we focus on defect prediction."

The organising device of the chapter is a four-cell diagram that recurs across the chapter:

```
Input: Software  ->  Output: Prediction of defects  ->  Reaction: Correction of defects  ->  Result: Less post-release defects
```

Underneath it sit three questions the slides attach to the pipeline: "Are the predictions
correct?", "Can developers find predicted defects?", "Is this really profitable?" Those map onto
the three things the chapter measures: performance metrics, the reaction step, and the cost
model.

## Formal Definition / Statement

**Basic terminology**, the lecture's own list:

| Term | Definition as printed |
|---|---|
| Target project | "The project for which we want to predict defects" |
| Training project(s) | "The project(s) from which we obtain data to train a defect prediction model" |
| Defect prediction model | "A machine learning model trained on historic data about defects" |
| Performance metric | "A metric that can be used to assess how good a defect prediction model is at finding defects" |

**The three strategy axes.** "Defect prediction is diverse", and the diversity has three
dimensions:

1. *For which artifacts do we predict if they are defective?* Files? Classes? Methods? Lines?
2. *Where do we get our training data?* "Cross-project: training data only from other projects";
   "Within-project: training data from the same project".
3. *When do we predict defects?* "When we prepare a release (or release candidate) to organize
   QA activities? Called release-level defect prediction in the literature"; "For every commit?
   Called just-in-time defect prediction in the literature".

**The cross-project design problem.** On the "Example: cross-project defect prediction" slide the
product is the release of a project, and each variant has different implications for possible
usage scenarios — "Some scenarios unrealistic". On that slide the pair-wise scenario "would lead
to multiple predictions models per target product", and "In reality, we can only one model or
need a strategy to combine multiple models into a single output". (Reference on the slide:
S. Herbold, A. Trautsch and J. Grabowski, "A Comparative Study to Benchmark Cross-Project Defect
Prediction Approaches", *IEEE TSE* 44(9), 811-833, 2018.)

**The JIT pipeline**, as printed on the "Example: Just-in-time (JIT) defect prediction" slide:

```
Model training:
  Issue tracker  -> Bug reports
  SZZ            -> Bug introducing commits + clean commits
  Version control -> Commits -> Training data, Test data -> Performance estimation
  ML model to predict if a commit is introducing a bug

Model deployment:
  Version control -> New commit -> ML model -> Prediction
  Some action within the development process:
    - E.g., extensive code review or testing in case of prediction as bug
    - E.g., only rudimentary quality checks in case of prediction as clean
  Model monitoring
```

**The temporal constraints.** "When working with JIT, many aspects need to be considered. Most
importantly, this is a process that should work in a real-time manner. This needs to be
considered when we create our model. Mostly affects data creation." Two rules:

- "Test data should never be older than training data. If this were the case, we could predict
  the past from the future and overestimate the performance of our model. 'We observed in the
  future that we had bugs in this file. Maybe we had them in the past as well.'"
- "How do we label data … The labeling also has a temporal dimension. The bug is only known when
  the issue is reported. The location of the bug is only known when the bug is fixed."

**The internal/external quality split.**

- *Internal quality*: "Includes aspects like the readability and maintainability of the code";
  "Technical debt and code smells are an aspect of internal quality".
- *External quality*: "Quality of the product when it is used and executed"; "Bugs are one key
  aspect of external quality".
- The research question on the slide: "are smells (internal quality) and bugs (external quality)
  associated?"

## Key Properties

- **The unit of prediction is a choice, and it changes the problem.** Files, classes, methods and
  lines all appear on the slides; each implies a different label definition and a different
  deployment action.
- **Cross-project versus within-project changes what generalisation means.** Cross-project models
  claim transfer across projects; within-project models do not.
- **Release-level versus JIT is the time axis.** Release-level prediction organises QA activity;
  JIT prediction runs on every commit and must be cheap and fast.
- **JIT's temporal constraint is a hard one, and it is about labels, not features.** The
  restriction is on the *test* set's age and on the *label* of the training set.
- **The label for a commit is only knowable in the future.** This is the slide's own phrasing:
  "That c2 is bug introducing is only known when c3 is committed" and "That c1 and c3 are bug
  introduced is only when c7 is committed".
- **The realistic train/test split accepts label noise.** "Which labels do we use for c1 and c3?!
  At the time of training, we do not know that these are defective! → Realistic setting must use
  labels that are known to be noisy for training!"
- **Code smells are not bugs, but are associated with them.** The Chapter 5 slide states it:
  "Code smells are not bugs, but are associated with them (see Chapter 6)". Chapter 6 turns that
  association into an empirical question and then into a feature set.
- **The four models used to study the smells–defects relationship are baselines with different
  feature families.** JIT = only process metrics ("The name JIT is not very precise here, but
  these are the metrics commonly used in the JIT defect prediction literature and hence the
  namesake of this baseline"); STATIC = only the product metrics ("also known as static product
  metrics"); PMD = only the code smell metrics ("PMD is the tool used for this study");
  Combined = all of them together.
- **Performance must be compared statistically.** The comparison slide uses a "Boxplot with
  jittered points that show the actual performances within experiments" and "Confidence
  intervals of the mean values computed with Tukey's HSD test".
- **Feature importance is a model-internal lens, and the slides flag its limits.** It is
  "essentially a measure about how often a certain feature was used to make decisions about the
  class"; "This should be controlled for correlations, which we do not discuss here."
- **The whole thing must be judged economically, not only statistically.** See
  [[defect-prediction-cost-model]].

## Worked Example

**The c1–c7 timeline** is the lecture's central example, and it is a graph, not a table. Its
elements: commits c1 … c7 on a time axis; two bugs (Bug 1, Bug 2) with issue reporting dates;
links from commits to issues; and blame/candidate annotations marking commits as "Candidate
Introducing for bug 1", "Candidate Introducing for bug 2", "Bug fixing", "Hard suspect". The
slide's own annotations state the two facts that break naive labelling:

- "That c2 is bug introducing is only known when c3 is committed"
- "That c1 and c3 are bug introduced is only when c7 is committed"

The train/test split slide repeats the diagram and adds "Training data" / "Test data" regions
plus the two questions above. The point of the example: by the time you train, c1 and c3 are
commits with no bug label attached — you cannot know they are defective — so the training
labels must be the ones obtainable *at training time*, which are noisy by construction.
(References on both slides: A. Trautsch, S. Herbold and J. Grabowski, "Static source code
metrics and static analysis warnings for fine-grained just-in-time defect prediction", ICSME
2020, 127-138.)

**The smells–defects study** is the chapter's applied example. Changes are measured on three
feature families: "Process related metrics such as number of past changes, number of authors,
etc."; "Product related metrics such as the size and complexity"; and code smells for the same
code — "Number of code smells before/after the change", "Types of code smells that were
added/removed". Four models (JIT, STATIC, PMD, Combined) are then compared, with reading rules:

- "If the performance decreases, the code smells were used to overfit on the training data"
- "If the performance is similar, the code smells did not have an impact"
- "If the performance increases, the code smells helped to better identify defective code"

The outcome: "Results show that there is a statistically significant impact. There is a large
effect size and this is also visible with other performance metrics. This provides already a
strong indicator that there is a relationship. Otherwise, such features should not help to predict
defects."

**Feature importance** then asks which features carried the signal, using the random forest: "The
results show that la (lines added) is most important, but that the warning density (WD) of PMD is
also very important → Size is the most important factor for risk, but smells matter!" The random
forest is the model chosen because it "can compute the feature importance".

## Common Pitfalls

- **Treating a commit as a bug or as clean because the label says so.** The c1–c7 example
  exists precisely to break that reflex.
- **Leaking the future into the test set.** "Test data should never be older than training data"
  — otherwise "we could predict the past from the future and overestimate the performance of our
  model".
- **Using issue-reported defects as if they were all the defects.** "The bug is only known when
  the issue is reported", so any defect not reported in the tracker is invisible to the label.
- **Confusing the JIT baseline with the JIT setting.** The "JIT" model in the smells study uses
  only process metrics; the lecture notes "The name JIT is not very precise here".
- **Reading feature importance as a causal statement.** The slide says it should be "controlled
  for correlations, which we do not discuss here".
- **Comparing models by eyeballing the boxplot.** The comparison slide pairs the jittered
  boxplot with Tukey's HSD confidence intervals; the decision rules assume a statistical
  comparison.
- **Stopping at "significant and large effect" and skipping profitability.** The pipeline's
  third question is "Is this really profitable?", which the cost model answers.
- **Assuming a prediction is usable without a reaction.** The Reaction stage says what happens:
  "extensive code review or testing in case of prediction as bug", "only rudimentary quality
  checks in case of prediction as clean".
- **Forgetting model monitoring.** The deployment slide lists it as a stage of the pipeline.

## Connections

- [[defect-prediction-cost-model]] — the money side of the same pipeline.
- [[szz-algorithm]] — how bug-introducing commits are identified in the first place.
- [[msr-data-noise]] — label noise is the JIT train/test problem in its general form.
- [[community-smells]] — code smells are the internal-quality side of the smells–defects
  question.
- [[software-metrics]] — the process and product metrics that become features.
- [[msr-statistical-methods]] — the significance testing and effect sizes behind "statistically
  significant impact".
- [[msr-tool-building]] — turning a predictor into a tool a developer can act on.
- [[threats-to-validity]] — where a JIT evaluation's leakage and label assumptions break.
- [[mining-software-repositories-lecture-6]] — the source lecture for this page.

## Open Questions

- **The slides never fix the unit of prediction for the flagship JIT setting.** "For which
  artifacts to we predict if they are defective? Files? Classes? Methods? Lines? …?" is posed as
  an open choice, and the JIT model in the smells study is described as "commit is introducing a
  bug" without a stated granularity.
- **The exact content of the training labels in the realistic setting is never specified.** The
  slides say labels must be "known to be noisy for training", but do not say whether the noisy
  label is the SZZ candidate set, the issue-linked set, or something else — the source of the
  noise and its magnitude are left open.
- **The pipeline diagram names "Model monitoring" without defining it.** No slide says what is
  monitored, how drift would be detected, or what triggers retraining.
- **The chapter asserts the smells–defects association without reporting numbers.** "There is a
  large effect size" and "statistically significant" are stated without the values, the sample,
  or the number of projects.
- **The deployment side is a bullet list of reactions only.** "Can developers find predicted
  defects?" is asked in the overview diagram but never answered; no measure of developer
  acceptance or review yield appears.
