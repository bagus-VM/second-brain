---
title: "CBIR Systems Evaluation"
tags: [concept, multimedia-databases, semester-1, evaluation, ir-metrics, cbr]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[query-by-example-and-feature]]", "[[feature-vector]]"]
---

## One-line Summary
A set of metrics, mostly borrowed from information retrieval, that score how well a CBIR system returns the right images and how quickly it does so.

## Core Intuition
A CBIR system returns a ranked list of images. Two questions follow: did it find the relevant ones, and did it avoid the irrelevant ones? Text retrieval solved this decades ago with precision and recall, and CBIR borrows the same machinery because the shape of the problem is identical: a ranked result list judged against a ground truth set of relevant documents.

The catch is that precision and recall are not independent. Crank up the recall by returning more images and precision drops because you drag in irrelevant ones. Tighten the list to raise precision and recall falls because you leave relevant images behind. A single precision or recall number is therefore meaningless on its own. You compare systems over the whole precision recall curve, or you collapse the curve into one number such as MAP that respects rank position.

Efficiency (time and space) is the other axis. A system can be perfectly effective and still useless if a query takes minutes. Evaluation covers both.

## Formal Definition / Statement

**Efficiency**: time and space cost of the retrieval process.

**Effectiveness**: how well the system retrieves relevant documents, and whether one system is better than another.

**Core pair** (with *found* = retrieved, *relevant* = relevant in the collection):
- Precision = (number of found relevant docs) / (number of found docs)
- Recall = (number of found relevant docs) / (number of relevant docs)

**Precision recall relationship**: precision and recall are not independent. Systems cannot be compared at a single precision recall point. They are compared over the curve.

**MAP (Mean Average Precision)**: takes rank position into account.
- r_ij = rank of the j-th relevant document for query Q_i
- \|R_i\| = number of relevant documents for Q_i
- n = number of test queries

MAP = (1/n) * sum over Q_i [ (1/\|R_i\|) * sum over j ( j / r_ij ) ]

where j / r_ij is the precision at the j-th relevant document (j relevant items found within the first r_ij results).

**Other metrics**:
- Noise = (found irrelevant docs) / (found docs) = 1 - Precision
- Silence = (not found relevant docs) / (relevant docs) = 1 - Recall
- Fallout = (found irrelevant docs) / (irrelevant docs)
- F-measure = 2 * P * R / (P + R)
- Average Precision = average precision at 11 standard recall points
- Precision at n-th document (often used for Web IR)
- Expected search duration = number of irrelevant documents a user must inspect before n relevant documents are found

**IoU (Intersection over Union)**: also called the Jaccard index. Used for object detection. It measures the ratio between the common area of two regions and their total area.

## Key Properties / Complexity

### Efficiency versus effectiveness
- Efficiency is objective and cheap to measure: wall clock time and memory.
- Effectiveness needs ground truth, which is expensive to produce. Every document query pair needs a relevance judgement.
- A system is judged on both. Fast but irrelevant is no better than relevant but slow.

### The precision recall curve
- Typical shape: precision falls as recall rises. An ideal system holds precision near 1.0 across all recall levels.
- Comparing two systems at one operating point can be misleading. One system may win at high recall while the other wins at high precision.
- MAP solves this by integrating precision over the whole ranking, weighted by where relevant documents appear.

### Why MAP respects rank
- A relevant document at rank 1 contributes precision 1.0. The same document at rank 100 contributes 0.01.
- This matches user behavior: people read top results first. A system that surfaces relevant images early should score higher than one that buries them, even if both eventually retrieve the same set.
- MAP averages over multiple queries, so it rewards consistent early retrieval.

### Test corpus methodology
- Compare different IR systems on the same test corpus.
- A test corpus contains: multiple documents, multiple queries, and a relevance judgement for each document query pair.
- System performance is measured by comparing its output against the expected results.
- Known benchmarking events: TRECVID and MediaEval.
- TRECVID: run by NIST as an annual evaluation, explicitly not a competition. The collection is fixed and split 50/50 for development and testing. Test queries arrive in July with roughly one month to submit.

## Worked Example

Two queries, three relevant documents each.

**Query 1**: relevant documents appear at ranks 1, 5, 10.
- Precision at 1st relevant = 1/1 = 1.0
- Precision at 2nd relevant = 2/5 = 0.4
- Precision at 3rd relevant = 3/10 = 0.3
- AP_1 = (1/3) * (1.0 + 0.4 + 0.3) = (1/3) * 1.7 = 0.567

**Query 2**: relevant documents appear at ranks 2, 4, 8.
- Precision at 1st relevant = 1/2 = 0.5
- Precision at 2nd relevant = 2/4 = 0.5
- Precision at 3rd relevant = 3/8 = 0.375
- AP_2 = (1/3) * (0.5 + 0.5 + 0.375) = (1/3) * 1.375 = 0.458

**MAP** = (1/2) * (AP_1 + AP_2) = (1/2) * (0.567 + 0.458) = 0.513

Notice what MAP rewards. Query 1 put a relevant image first, so it scores higher even though both queries eventually found all three relevant documents. Rank position, not just set membership, drives the score.

For object detection, IoU works on bounding boxes. If a predicted box and a ground truth box overlap on 60 pixels and cover 100 pixels together, IoU = 60/100 = 0.6. A detection is usually counted as a true positive when IoU exceeds a threshold such as 0.5.

## Common Pitfalls
- **Quoting one precision or recall number without the other**: without the operating point (how many results were returned) the number says nothing. Report the curve or a rank aware single number like MAP.
- **Comparing systems at a single precision recall point**: the systems may cross elsewhere. Compare curves or MAP values instead.
- **Confusing Noise and Fallout**: both involve irrelevant documents, but Noise divides by found docs (it is 1 - Precision) while Fallout divides by all irrelevant docs in the collection. Fallout needs the total count of irrelevant items, which is large and easy to misstate.
- **Computing MAP without rank weighting**: summing 1/rank instead of precision (j/rank) gives a different, wrong value. The j in the numerator is the count of relevant items found so far, not a constant 1.
- **Forgetting the ground truth cost**: test corpora require a relevance judgement per document query pair. Scaling this to large collections is a research problem in itself, which is why shared benchmarks like TRECVID exist.
- **Using IoU thresholds without stating them**: "90% detection accuracy" is meaningless unless the IoU threshold (0.5? 0.75?) and the matching rule are specified.

## Connections
[[content-based-retrieval]]: evaluation metrics score the output of a CBR system's ranking step.
[[query-by-example-and-feature]]: QBE and QBF queries are the inputs whose ranked outputs these metrics judge.
[[feature-vector]]: the quality of the feature vector determines how early relevant items appear in the rank, which MAP measures directly.
[[minkowski-distance]]: the distance metric choice affects ranking quality, which these metrics then quantify.
[[color-histogram]]: a common descriptor whose retrieval quality is measured with precision, recall, and MAP.
[[curse-of-dimensionality]]: high dimensional features degrade ranking quality, visible as a flatter precision recall curve.

## Open Questions
- How do you build ground truth for subjective similarity? Two users may disagree on whether an image is relevant, which makes the relevance judgement itself uncertain.
- Can relevance feedback from the evaluation loop be reused to improve MAP, or does that bias the test?
- For real time CBIR, how should efficiency and effectiveness be traded when reporting a single score?
- Do deep learning embeddings change which metric matters most? Some recent retrieval work argues recall at small k is more realistic than MAP for interactive search.
