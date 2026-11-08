---
title: "Clustering and Dimensionality Reduction"
tags: [concept, introduction-to-deep-learning, semester-2, unsupervised-learning, machine-learning]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[ml-learning-paradigms]]"]
---

## One-line Summary
Unsupervised learning works on the features alone, and the lecture names three jobs for it —
grouping similar instances, compressing them, and modelling the distribution they come from — before
admitting in one slide that evaluating the result is the hard part.

## Core Intuition

Remove the labels and there is no right answer to compare against, so what is left is structure. The
lecture frames three uses of that structure. **Clustering** asks which instances resemble each other;
**dimensionality reduction** asks whether the same information can be carried in fewer numbers; and
**density estimation / generative models** ask what distribution the data could have come from —
which is the question that lets you call something anomalous, or generate something new.

All three rest on a notion of similarity, and the lecture is honest that this is where the trouble
starts: slide 11 is two illustrations captioned "Similarity?" and the conclusion printed beside them
is **"Evaluation is difficult!"**. That is not a throwaway. In supervised learning the test set
decides whether the model is good. In clustering, two defensible groupings of the same data can
disagree, and nothing in the data says which is right — the "correct" number of clusters is often a
choice about what the analysis is for.

The deep-learning relevance is stated in the same slide and is easy to miss: two of the three tasks
reappear later in the course as representation learning. Autoencoders are dimensionality reduction and
learned embeddings are a compression that makes similar things close.

## Formal Definition / Statement

**Unsupervised learning (slide 9):** "Learn the structure of the data x_1, ..., x_n — no labels y
given." Three tasks named:

| Task | What it finds | Examples on the slide | Deep-learning form |
|------|---------------|----------------------|--------------------|
| **Clustering** | groups of similar instances | customer segments, groups of similar gene sequences | — |
| **Dimensionality reduction** | a compact representation of the data | PCA | autoencoders, learned embeddings |
| **Density estimation / generative models** | the distribution `p(x)` | anomaly detection | image and text generation |

**Clustering (slide 10):**

- Identification of a finite set of **clusters** in the data (= categories, "classes", groups).
- Instances in the **same cluster**: as **similar** as possible.
- Instances in **different clusters**: as **dissimilar** as possible.
- **Unsupervised**: no groups are given.
- Examples: group website users by behaviour; groups with similar political opinions; gene sequences
  with similar expression; stocks with similar behaviour.

**The evaluation problem (slide 11):** a picture pair captioned "Similarity?" with the printed
conclusion **"Evaluation is difficult!"**

**The paradigm context (slide 8):** unsupervised learning is one of four paradigms distinguished by
training feedback, alongside supervised (labels given), self-supervised (labels created automatically
from the data itself, e.g. next-token prediction for LLM pretraining) and reinforcement learning
(exploration with sparse rewards).

## Key Properties

- **There is no ground truth to score against.** Every clustering metric is a proxy for an internal
  criterion (compactness, separation), not a check of correctness.
- **The grouping depends on the distance.** "The k nearest neighbours" and "the most similar
  instances" are only defined once a metric is fixed.
- **The number of clusters depends on the purpose.** The lecture asks for a *finite set* of clusters
  and gives no rule for how many.
- **Dimensionality reduction is a lossy promise.** A compact representation keeps what the method
  considers important, which is a modelling decision.
- **Density estimation is the generative framing.** It is the only one of the three that models
  `p(x)` outright, and it is the one that makes anomaly detection principled: rare means low density.
- **Two of the three reappear as deep learning later in the course** — autoencoders, learned
  embeddings — which is why the lecture fixes the vocabulary here.
- **Clustering is often the first step of a supervised pipeline**, not an end in itself: clusters
  become features, or a labelling aid.
- **The lecture's clustering description is geometric**: similarity inside, dissimilarity between.

## Worked Example

Computed in `study/homework/introduction-to-deep-learning/idl-lecture2-numbers.py`, section 10. Six
points in 2-D:

```
(0.0, 0.0), (0.5, 0.2), (1.0, 1.0), (5.0, 5.0), (5.2, 4.8), (9.0, 1.0)
```

Grouping by k-means from fixed starting centroids:

| k | Euclidean | Manhattan |
|---|-----------|-----------|
| 2 | {(0,0), (0.5,0.2), (1,1)} \| {(5,5), (5.2,4.8), (9,1)} | same |
| 3 | {(0,0)} \| {(0.5,0.2), (1,1)} \| {(5,5), (5.2,4.8), (9,1)} | same |

**The number of clusters changes the answer; the metric did not.** At k = 2 the point (1,1) belongs
with the small cluster near the origin; at k = 3 it is grouped with (0.5,0.2) and (0,0) is alone. Both
groupings are defensible, and there is nothing in the six points that prefers either — which is the
lecture's slide-11 point, made concrete. The metric choice, by contrast, changed nothing here, because
these clusters are far apart relative to their internal spread.

**Where the metric does change the answer.** Nearest neighbour of the origin among two candidates:

| Metric | d to (1,1) | d to (1.5,0) | Nearest |
|--------|-----------|--------------|---------|
| Euclidean | 1.4142 | 1.5000 | (1,1) |
| Manhattan | 2.0000 | 1.5000 | (1.5,0) |

The two metrics disagree about which point is closer, so the same algorithm with two "obvious"
distance functions produces two different groupings. That is the mechanism behind "evaluation is
difficult": the answer is a joint property of the data, the metric and the number of clusters, and
only one of those three has anything to do with the data.

## Common Pitfalls

- **Expecting a unique right answer.** Two analysts with different metrics and different k will
  produce different, defensible groupings.
- **Choosing k by convenience.** The lecture requires a *finite* set of clusters and gives no
  criterion for its size.
- **Treating cluster labels as classes.** They are arbitrary identifiers; relabelling cluster 1 as
  cluster 2 changes nothing about the model.
- **Reading "evaluation is difficult" as "evaluation is impossible".** Internal criteria and
  downstream task performance are both usable; the point is that neither is ground truth.
- **Assuming dimensionality reduction is lossless.** PCA and autoencoders both discard; which
  direction they discard is the modelling decision.
- **Confusing this material with graph clustering.** The vault's Semester 1 pages on
  clustering-coefficient, hierarchical clustering and spectral embeddings are about partitioning
  *graphs* — a different technique that happens to share a word.
- **Forgetting that unsupervised work has no label leakage to protect against, but does have leakage.**
  Fitting a scaler or a clustering on all data before a supervised split is still a leak — see
  [[information-leakage]].
- **Assuming generative models must be deep.** Density estimation is the classical framing; the
  deep-learning examples are named as instances of it, not as its definition.

## Connections

- [[ml-learning-paradigms]] — the four-way split by training feedback that places unsupervised
  learning next to supervised, self-supervised and reinforcement learning.
- [[ml-task-taxonomy]] — the supervised counterpart: classification, regression and structured
  prediction, where a target exists.
- [[k-nearest-neighbors]] — the supervised method that uses the same similarity machinery with labels
  attached.
- [[representation-learning]] — where the dimensionality-reduction bullet reappears in the course:
  autoencoders and learned embeddings.
- [[feature-normalization]] — preprocessing that changes which points are "similar" and therefore
  changes the clustering.
- [[information-leakage]] — the supervised-split rule that still applies when unsupervised steps are
  part of a pipeline.
- [[introduction-to-deep-learning-lecture-2]] — the lecture this page belongs to.

## Open Questions

- **No clustering algorithm is named.** k-means, hierarchical clustering and DBSCAN do not appear;
  the slide describes the *goal* (similar within, dissimilar between) and nothing about how to reach it.
- **No evaluation criterion is offered.** "Evaluation is difficult!" is the entire treatment; internal
  indices, silhouette scores and downstream-task evaluation are not mentioned.
- **No distance metric is specified**, although the whole notion of similarity depends on one.
- **PCA is named for dimensionality reduction and never explained** — no variance criterion, no
  components, no reconstruction error.
- **Anomaly detection is listed as a density-estimation use case without a method**, and no density
  model is named.
- **The number of clusters is not addressed** at any point in the slide.