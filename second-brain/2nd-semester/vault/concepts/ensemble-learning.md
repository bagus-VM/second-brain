---
title: "Ensemble Learning"
tags: [concept, introduction-to-deep-learning, semester-2, machine-learning, classification]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[decision-trees]]"]
---

## One-line Summary
Many models that are wrong in different ways can be combined into one that is wrong less often —
bagging by averaging away variance, boosting by attacking the residual errors in turn.

## Core Intuition

A single model makes a systematic, repeatable kind of mistake. If three models make *different*
mistakes, a vote cancels most of them. That is the entire idea, and the lecture's illustrative table
makes it concrete: three classifiers with individual accuracies of 0.8, 0.8 and 0.6 produce a
majority vote with accuracy 1.0, because their errors land on different instances.

The mechanism is not magic and it has a condition. Voting helps when the members are **accurate** and
**diverse**. Perfectly correlated models — all wrong on the same rows — gain nothing from being
combined; the table above works precisely because the three error patterns are complementary. Both
families of method in the lecture are ways of manufacturing that diversity. Bagging resamples the data
and the features so each tree is grown on a different view; boosting reweights the data so each new
model is forced to concentrate on what the current ensemble still gets wrong.

The lecture's punchline is an uncomfortable one for the rest of the course: on tabular data, the
gradient-boosted-tree ensembles below still beat deep learning fairly routinely, while deep learning's
advantage lies with unstructured data. Two citations support the claim and one recent counterexample
(a tabular foundation model) is named as catching up on small datasets.

## Formal Definition / Statement

**The definition quoted on slide 29** (Dietterich, 2000): "**An ensemble of classifiers is a set of
classifiers whose individual decisions are combined in some way to classify new examples.**"

**Motivation as stated:** different classifiers make different errors; try to combine classifiers to
improve classification accuracy. The slide's figure is a set of base learners (C1 … Cn) producing
single predictions that enter a combining mechanism to give a final prediction.

**The slide's demonstration table** (five instances, "true class" as the reference):

```
                  i1 i2 i3 i4 i5
True class        +  +  +  -  -
Classifier 1      +  +  +  +  -      accuracy 0.8
Classifier 2      +  +  -  -  -      accuracy 0.8
Classifier 3      -  -  +  -  -      accuracy 0.6
Majority voting   +  +  +  -  -      accuracy 1.0
```

**Method 1 — Random Forest (bagging):**

- Build many slightly different trees
- Subset of instances for each tree (bootstrap sampling)
- Choose from a subset of attributes at each node
- Collect predictions for each tree
- **Majority decides**

**Method 2 — Boosting (e.g. AdaBoost):**

- Train a simple classifier
- Identify misclassified instances of this classifier
- Increase the weight of these instances
- Iterate: do this many times
- Overall classifier: combination of all previously trained models

**Method 3 — Gradient boosting (slide 32):** "each new tree is trained on the remaining errors of the
current ensemble (more precisely: the negative gradient of the loss)". Popular implementations:
**XGBoost, LightGBM, CatBoost**.

**The tabular claim and its citations:**

- For tabular data (like the bot example), gradient-boosted trees "are still a very strong baseline and
  often beat deep learning".
- Deep learning "shines on unstructured data: images, text, audio".
- Recent: tabular foundation models (e.g. **TabPFN**) "catch up, in particular on small datasets".
- Grinsztajn, Oyallon, Varoquaux, *Why do tree-based models still outperform deep learning on typical
  tabular data?*, NeurIPS 2022.
- Hollmann et al., *Accurate predictions on small data with a tabular foundation model*, Nature 2025.

## Key Properties

- **Ensembles need diversity, not just accuracy.** Combining identical models changes nothing.
- **Bagging attacks variance.** Independent-ish trees averaged reduce the instability of a single
  greedy tree ([[decision-trees]]).
- **Boosting attacks bias.** Each round fits what the current ensemble gets wrong, so the composite can
  represent more than any member.
- **Bagging is parallel, boosting is sequential.** One is a bag of independent models; the other is a
  chain where every stage depends on the previous errors.
- **The combination rule matters.** Majority voting for classification; for gradient boosting the
  combined model is a sum of trees with weights.
- **Gradient boosting is stated as gradient descent in function space** — "the negative gradient of the
  loss" — which is what connects this page to [[loss-functions-and-empirical-risk]].
- **The tabular claim is empirical and cited, not derived.** The lecture asserts it with two references
  and no experiment of its own.
- **Deep learning's advantage is scoped, not general.** "Shines on unstructured data"; the slide does not
  claim it wins everywhere.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 7.

Recomputing the slide's table. Truth `[+, +, +, -, -]`; the three classifiers are
`[+,+,+,+,-]`, `[+,+,-,-,-]`, `[-,-,+,-,-]`.

| | i1 | i2 | i3 | i4 | i5 | accuracy |
|---|---|---|---|---|---|---|
| Truth | + | + | + | − | − | — |
| C1 | + | + | + | **+** | − | 4/5 = 0.8 |
| C2 | + | + | **−** | − | − | 4/5 = 0.8 |
| C3 | **−** | **−** | + | − | − | 3/5 = 0.6 |
| Majority | + | + | + | − | − | **5/5 = 1.0** |

Each column shows the mechanism directly: at i4 the vote is (+, −, −) → −; at i5 it is (−, −, −) → −;
and where one classifier errs, the other two are right. **The three errors are on different instances,
which is the whole reason the vote is perfect.**

**What independence would predict.** If the three classifiers were independent with per-instance
correctness rates 0.8, 0.8 and 0.6, the probability that a majority of three is correct is
**0.7440**, which is *lower* than the best individual classifier's rate. The table's 1.0 is not a
generic property of voting — it is what you get when errors are maximally anti-correlated. With
positively correlated classifiers (which is what happens in practice when they share training data)
the ensemble gain shrinks toward zero.

**A note on the slide's own table.** The extracted text of slide 30 lists the accuracies 0.8, 0.6 and
1.0 down the right-hand column against the three classifier rows, but recomputing from the printed
+/− rows gives **0.8, 0.8 and 0.6**, with **1.0 belonging to the majority-voting row**. The extraction
has shifted the accuracy column by one row; the recomputation above is the arithmetic consistent with
the row contents.

## Common Pitfalls

- **Assuming voting always helps.** With correlated errors the ensemble can be no better than its best
  member — the independence calculation above gives 0.7440 for an individual rate of 0.8.
- **Building members that are all the same.** Ensemble diversity has to be engineered (bootstrap
  samples, attribute subsets, reweighting); it does not appear by itself.
- **Confusing bagging and boosting.** Bagging reduces variance by averaging independent models;
  boosting reduces bias by fitting residuals sequentially. Mixing them up inverts the mechanism.
- **Reading "gradient boosting" as a gradient-descent step on the trees' parameters.** The slide is
  precise: the new tree fits the *negative gradient of the loss* in function space.
- **Extrapolating the tabular claim to every dataset.** The slide scopes it to tabular data and cites
  specific papers; TabPFN is named as narrowing the gap on small datasets.
- **Forgetting the base learner.** In this lecture the ensembles are ensembles of **trees**; random
  forests are not a generic bagging wrapper for arbitrary models.
- **Treating the hyperparameters of an ensemble as free.** Number of trees, sample size, attribute
  subset size and learning rate all exist, and none of them is mentioned on the slides.

## Connections

- [[decision-trees]] — the base learner for every method on this slide; bagging exists partly because
  greedy trees are unstable.
- [[loss-functions-and-empirical-risk]] — the loss whose negative gradient each new boosting tree fits.
- [[k-nearest-neighbors]] — another classical method from the same section, with the opposite
  bias-variance profile.
- [[support-vector-machines]] — the third classical non-linear method; also used as ensemble members in
  practice, though not in this lecture's account.
- [[neural-network-training-loop]] — the deep-learning alternative, and the contrast the tabular claim is
  drawn against.
- [[ml-pipeline-scikit-learn]] — where `RandomForestClassifier` and `GradientBoostingClassifier` live, and
  where the hyperparameters the slides omit are actually set.
- [[cross-validation]] — how the number of trees and the learning rate would be chosen.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **The tabular claim is cited, not demonstrated.** No dataset, accuracy difference or experiment is
  given; the lecture defers entirely to Grinsztajn et al. (2022) and notes TabPFN (Hollmann et al., 2025)
  as narrowing the gap on small datasets.
- **No hyperparameters are discussed** — number of trees, bootstrap size, attribute-subset size, learning
  rate, number of boosting rounds.
- **The combination rule for gradient boosting is not specified** beyond "each new tree is trained on the
  remaining errors"; whether trees are summed with equal weight or shrunk is not stated.
- **Why trees beat deep learning on tabular data is not explained.** The slide names the phenomenon and
  the paper; the reasons (rotation invariance, uninformative features, smoothness assumptions) are not
  mentioned.
- **The slide's own accuracy column is misaligned in the PDF text extraction** (recorded in the worked
  example). The row contents and the recomputed accuracies are used here; whether the rendered slide
  prints 0.8/0.8/0.6 or something else cannot be checked from the extracted text.