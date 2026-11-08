---
title: "Locality-Sensitive Hashing (LSH)"
tags: [concept, multimedia-databases, semester-1, locality-sensitive-hashing, indexing]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[curse-of-dimensionality]]", "[[signature-vectors]]"]
---

## One-line Summary
Locality-sensitive hashing finds approximate nearest neighbours in high dimensions by hashing similar vectors into the same bucket with high probability, so search only examines a small candidate set instead of the whole database.

## Core Intuition
Exact tree indexes lose to the [[curse-of-dimensionality]] in high dimensions. LSH gives up on exactness and bets on probability. If you hash vectors repeatedly, and the hash function sends nearby vectors to the same bucket more often than distant ones, then similar vectors will collide at least once across the runs. You only compare pairs that shared a bucket.

The hash function is a hyperplane cutting the space. Take random projections of the data and quantize each projection with a few bits. A vector lands on one side of the hyperplane or the other, producing a bit. Stack several such hyperplanes and you get a hash code. Similar vectors produce similar codes and tend to share a bucket.

The trick is tuning. Split the signature matrix into bands and rows so that genuinely similar pairs collide in at least one band while dissimilar pairs rarely do. Get b and r right and you catch most similar pairs while filtering out most dissimilar ones.

## Formal Definition / Statement
**Big idea**: hash the columns of a signature matrix M several times so that (only) similar columns are likely to hash to the same bucket. **Candidate pairs** are column pairs that hash to the same bucket for at least one band.

**Band construction**:
- Divide matrix M into **b bands** of **r rows** each.
- For each band, hash its portion of each column into a hash table with **k buckets** (make k as large as possible).
- A pair of columns hashing to the same bucket in at least one band becomes a candidate.
- Tune b and r to catch most similar pairs while catching few dissimilar pairs.

**Hash function for the hash code**: a hyperplane separating the space. Take random projections of the data and quantize each projection with a few bits to form the code.

**Query flow**: hash the query vector with the same functions, retrieve the small set of vectors sharing a bucket, and search only that set instead of all N vectors.

## Key Properties / Complexity
- **Approximate, not exact**: LSH returns near neighbours with high probability, not a guaranteed nearest neighbour.
- **Candidate filtering is the win**: a query touches a small set of candidates instead of N points, so search is sublinear in practice.
- **Tuning b and r controls the precision and recall trade-off**: more bands catch more similar pairs but also more false positives; more rows per band demand stricter agreement, cutting false positives but missing some true pairs.
- **Space cost is the main drawback**: the original scheme builds hundreds of hash tables, which causes a huge space requirement.
- **Reported as the most promising solution to approximate NN search** in high dimensions.

**Variants that address the space drawback**:
- **Multi-Probe LSH**: explore buckets near the one the query falls into, so fewer hash tables are needed.
- **C2LSH**: dynamic collision counting to collect candidates more efficiently.
- **SK-LSH (SortingKeys-LSH)**: verify candidates in units of disk pages. Points with close compound hash keys are arranged together on disk, so only a few disk-page accesses are required.

## Worked Example
A signature matrix M with 4 columns (C1 to C4) and 6 rows, split into b = 2 bands of r = 3 rows:

```
Band 1 (rows 1-3):
        C1  C2  C3  C4
row 1:   1   1   0   1
row 2:   0   0   1   0
row 3:   1   1   0   1

Band 2 (rows 4-6):
        C1  C2  C3  C4
row 4:   1   1   0   0
row 5:   0   0   1   1
row 6:   1   1   0   0
```

Hash each band's 3-bit column signature to k buckets:
- Band 1: C1 and C2 both hash to signature (1,0,1) = bucket A. C3 hashes to (0,1,0) = bucket B. C4 to (1,0,1) = bucket A.
- Band 2: C1 and C2 share (1,0,1) = bucket X. C3 and C4 share (0,1,0) = bucket Y.

Candidate pairs (shared bucket in at least one band): (C1,C2) from both bands, (C1,C4) from band 1, (C2,C4) from band 1, and (C3,C4) from band 2. C1 and C2 collide twice, so they are probably identical or near-identical. C3 and C4 collide only in band 2 and differ in band 1, so they are weaker candidates. The system then computes exact distances only on this candidate set rather than all pairs.

## Common Pitfalls
- Treating LSH as exact nearest-neighbour search. It is approximate; the true nearest neighbour may miss every bucket.
- Picking b and r without thought. Too few bands miss similar pairs; too many drown the candidate set in false positives.
- Ignoring the space blowup of the original scheme. Hundreds of hash tables are expensive; pick a variant (Multi-Probe, C2LSH, SK-LSH) to cut the count.
- Forgetting that the query must be hashed with the same functions and bands used at build time.
- Assuming one hash function is enough. A single hyperplane is weak; LSH relies on many projections to form a discriminating code.

## Connections
- [[curse-of-dimensionality]]: the reason exact tree indexes fail and LSH's approximate approach becomes attractive.
- [[signature-vectors]]: the columns of the signature matrix M that LSH hashes.
- [[r-tree]]: the exact index family LSH replaces when dimensions grow too large for MBR pruning.
- [[dimensionality-reduction]]: a complementary strategy; you can reduce first and then hash, or hash directly in high dimensions.
- [[quadtree-and-kd-tree]]: main-memory exact indexes that also lose to high dimensionality, motivating LSH.

## Open Questions
- How should b and r be set automatically for a given dataset's distance distribution?
- For modern high-dimensional embeddings, does LSH still beat graph-based methods like HNSW, or have graph indexes taken over?
- Can the space cost be driven down to a single hash table without the recall loss that Multi-Probe incurs?
