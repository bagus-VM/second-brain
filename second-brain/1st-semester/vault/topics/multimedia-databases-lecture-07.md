---
title: "Multimedia Databases - Lecture 07: Content-Based Image Retrieval"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]", "[[mpeg-7-descriptors]]"]
---

## One-line Summary
Lecture 07 covers CBIR end to end: the QBE/QBF query process, visual characteristics (color, texture, shape), histogram representation and quantization, distance metrics for comparing feature vectors, MPEG-7 color descriptors, deep learning integration, and IR evaluation metrics.

## Core Intuition
Content-based image retrieval skips text annotations. The system extracts numerical features from images, represents them as vectors, and ranks database images by similarity to a query. This lecture builds the full pipeline: how you query (QBE vs QBF), what you compare (histograms, descriptors), how you measure closeness (distance metrics), and how you evaluate the whole system (precision, recall, MAP).

## Key Topics

### 1. Query Process: [[query-by-example-and-feature]]
- QBF (Query By Features): user submits feature values (dominant color, texture pattern). Exploratory, inaccurate, used to expand the search.
- QBE (Query By Example): user submits a sample image. Precise, detailed, used to restrict the search.
- Result page feeds back: result images for further QBE, similar features for further QBF.
- QBE is QBF underneath: the system extracts the query image's feature sequences and runs QBF on them.

### 2. Visual Characteristics
- Color: histograms, dominant color, color structure
- Texture: patterns, edges, repeating structures
- Shape: contours, boundaries
- Content descriptor: a tuple of (property value, similarity level) pairs, or a histogram

### 3. [[color-histogram]] Representation and Quantization
- Histogram = list of (color, share) pairs, sums to 1
- Range quantization (color space quantization): reduces bin count. 256³ colors into 512 bins, each containing 32,768 colors.
- Bin quantization: defines bit-coding of values in each bin. 15 bits instead of 16 saves ~50% space.
- Adaptive (individual) binning: adapts bins to each image. More accurate content representation.
- Regular (uniform) binning: fixed bins across all images.

### 4. Distance Metrics
- [[minkowski-distance]] Lp family: L1 (Manhattan), L2 (Euclidean), L∞ (Chebyshev)
- [[chi-squared-distance]]: scale-invariant, bin-by-bin, no positivity or triangle inequality
- Kullback-Leibler divergence: measures encoding cost, non-symmetric, no triangle inequality
- Jeffrey divergence: symmetric and robust version of KL
- Histogram intersection: ideal for partial matching, bin-by-bin
- Earth Mover's Distance (EMD): uses ground distance between bins, accounts for bin adjacency
- Distance vs. similarity: human similarity perception violates symmetry (d(A,B) ≠ d(B,A)), depends on context and knowledge

### 5. MPEG-7 Color Descriptors
- Dominant Color (DCD): compact set of (color, percentage, variance) pairs plus spatial coherency
- Color Structure Descriptor (CSD): captures both color distribution and local structure via 8×8 structuring element. Distinguishes images that a global histogram cannot.
- Extraction: generalized Lloyd algorithm in perceptually uniform color space (CIE LUV)

### 6. Machine Learning / Deep Learning
- ML basics: labeled data → training → learned model → prediction
- Deep learning: forward propagation, backpropagation, ReLU activation
- CNNs: convolutional filters as learned feature detectors, max pooling
- RNNs: sequential processing, vanishing gradient problem
- GANs: generator vs discriminator adversarial training
- Vision Transformers (ViT): image split into patches, linear embeddings, transformer encoder
- CNN limitations: local operators only, cannot model distant patch correlations, pooling causes information loss
- Data augmentation: vertical/horizontal flip, rotation, blurring (CLoDSA tool)

### 7. [[cbir-systems-evaluation]]
- Efficiency: time, space
- Effectiveness: precision = found relevant / found docs; recall = found relevant / relevant docs
- Precision and recall are not independent: compare over the curve, not at a single point
- MAP (Mean Average Precision): accounts for rank position
- Other metrics: Noise (1-Precision), Silence (1-Recall), Fallout, F-measure = 2PR/(P+R)
- IoU (Intersection over Union): for object detection, Jaccard index
- Test corpus methodology: TRECVID (NIST, annual, not a competition), MediaEval

## Worked Example: Butterfly Identification System
1. User remembers an orange-yellow butterfly with many spots but has no photo
2. Opening QBF: submit color = orange_yellow, texture = many_spots. System returns loose ranking.
3. Result page shows matching images and their extracted features
4. User spots the right species, clicks it as example for QBE
5. System extracts that image's feature sequences, runs QBF on them. Tight ranking.
6. Iterate until correct species is pinned down

## Connections
- [[content-based-retrieval]] → [[query-by-example-and-feature]] → [[color-histogram]] (the retrieval pipeline)
- [[mpeg-7-descriptors]] → [[dominant-color]] → [[spatial-coherency]] (descriptor details)
- [[minkowski-distance]] → [[chi-squared-distance]] → [[kolmogorov-smirnov-distance]] (distance metric family)
- [[cbir-systems-evaluation]] (how to measure if the system works)
- [[multimedia-databases-lecture-06]] (modeling layer feeds into this lecture's retrieval layer)

## Exam-Relevant Key Points
- QBE vs QBF: which is precise, which is exploratory, how they feed each other
- Range quantization vs bin quantization: what each controls, the 50% space gain example
- Adaptive vs regular binning
- Distance metric properties: which are metrics, which are semi-metrics or pseudo-metrics
- Why Minkowski fails for color similarity (ignores similarity between colors in different bins)
- CSD: how the 8×8 structuring element distinguishes images with identical global histograms
- MAP formula and worked calculation
- Precision-recall curve: why systems cannot be compared at a single point

## Open Questions
- How do deep CNN embeddings change the CBIR pipeline? Are they a replacement for hand-crafted features or a complement?
- How to build ground truth for subjective similarity judgments?
- For very large databases, can the feature sequence be produced approximately to keep the interactive loop fast?
