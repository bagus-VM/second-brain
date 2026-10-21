---
title: "Naive Bayes Text Classification"
tags: [concept, ml-security, semester-2, text-classification]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[ml-task-taxonomy]]"]
---

## One-line Summary

Naive Bayes picks the class maximising P(d|c)·P(c), and makes that computable by pretending word occurrences are independent given the class — an assumption that is false and works anyway.

## Core Intuition

The question is "given these words, which class is most probable?" Bayes' rule turns it into "which class generates these words most often?", which counts answer. The obstacle is that P(w1,…,wn|c) ranges over every possible document, and no training set covers that space. Assuming conditional independence factorises one impossible estimate into n trivial ones. The assumption is wrong — words in a spam message are obviously correlated — but the decision only needs the *argmax* to be right, not the probabilities to be calibrated.

## Formal Definition / Statement

**Problem.** Input: a document d, a set of n classes C = {c1, …, cn}, and k labelled documents (d1,c1), …, (dk,ck). Output: a trained classifier y : d → c. Manually coded rules are the alternative, and they are expensive.

**Representation.** Bag of words: the words in the document and their frequencies, ignoring order.

**Derivation, as on the slide:**

```
c_MAP = argmax_{c∈C} P(c|d)              (MAP: maximum a posteriori)
      = argmax_{c∈C} P(d|c)P(c) / P(d)   (Bayes' rule)
      = argmax_{c∈C} P(d|c)P(c)          (simplified — P(d) is constant)
```

P(d) does not depend on c, so it cannot change which class wins. With d as a feature vector:

```
c_MAP = argmax_{c∈C} P(x1, x2, …, xn | c) · P(c)
```

**Why that cannot be estimated directly.** The slide's answer: *huge space, would require an extremely huge training set*. Every distinct word combination is its own event, and almost all are unseen.

**The naive assumption.** Features are conditionally independent given the class:

```
P(x1, …, xn | c) = P(x1|c) · P(x2|c) · … · P(xn|c)
```

Each factor is estimated by counting in the training data.

**Laplace (add-one) smoothing.** If a word never appeared in the spam training set, P(xi|spam) = 0 and the product collapses regardless of the other evidence. Pretend one extra spam email contained xi and one did not:

```
P(xi | spam) = (spam emails containing xi + 1) / (total spam emails + 2)
```

**Log space.** Multiplying hundreds of small probabilities underflows floating point, so implementations add logarithms:

```
score(c) = log P(c) + Σ_i log P(xi | c)
```

## Key Properties

- **Generative, not discriminative.** It models how each class produces documents and compares, rather than learning a boundary.
- **Training is one pass of counting** — no iterative optimisation, no hyperparameters beyond smoothing.
- **The independence assumption is knowingly false.** It is a computational device; that is why the classifier is "naive".
- **Class priors are learned for free.** In an imbalanced corpus the prior can dominate weak evidence — correct behaviour, often mistaken for a bug.
- **Vocabulary size is a design decision.** The L2 exercise builds a dictionary from the 2000 most frequent words of the *training* set, drops punctuation and single characters, converts each mail to a word-count vector, and trains `MultinomialNB`.
- **Alternatives on the slide:** logistic regression, SVMs, k-nearest neighbours.

## Worked Example

Illustrative training set: 100 spam and 100 ham; "viagra" occurs in 20 spam and 1 ham. Priors are equal and cancel.

| Quantity | Spam | Ham |
|---|---|---|
| raw count | 20 / 100 | 1 / 100 |
| Laplace-smoothed P(word \| class) | (20+1)/(100+2) = 0.2059 | (1+1)/(100+2) = 0.0196 |
| log P | −1.580 | −3.932 |

The log-odds contribution is 2.351 nats: the word is about 10.5× more likely under spam, so the MAP decision is spam. Two things to notice: without smoothing a word seen only in spam would give P(word|ham) = 0 and veto ham permanently; and the decision was made by *adding* two numbers.

## Common Pitfalls

- **Skipping smoothing.** One unseen word zeroes an entire class.
- **Multiplying instead of adding logs.** Fine on toy examples, underflows on real documents.
- **Building the vocabulary on the full corpus.** The exercise says "from training set" for a reason: a vocabulary chosen with test data leaks labels.
- **Reading the output as calibrated probability.** The independence assumption distorts the numbers; the ranking is what is trustworthy.
- **Expecting word order to matter.** Bag of words cannot distinguish "not spam" from "spam" if the words match.

## Connections

- [[classification-metrics]] — how the resulting classifier is scored.
- [[ml-pipeline-scikit-learn]] — the same pipeline in pandas/scikit-learn form.
- [[ml-task-taxonomy]] — naive Bayes sits in the classification family.
- [[ml-learning-paradigms]] — supervised, generative.

## Open Questions

- No threshold or cost model appears, so the 0.5 decision boundary is implicit.
- Laplace is the only smoothing variant mentioned; whether the course expects TF-IDF weighting is unstated. The assigned paper (Kontsewaya et al., 2021) supplies the alternatives, comparing NB against K-nearest neighbours, SVM, logistic regression, decision tree and random forest on a Kaggle spam dataset (5,695 messages after de-duplication) — logistic regression and NB reach the highest accuracy there.

