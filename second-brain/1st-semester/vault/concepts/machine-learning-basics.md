---
title: "Machine Learning Basics"
tags: [concept, software-analyse, semester-1, software-analyse]
course: "Software Analyse"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: []
---

## One-line Summary
Machine learning is the practice of training algorithms on data to learn patterns and make predictions, with supervised learning being the most common paradigm where models learn from labelled examples.

## Core Intuition
Instead of writing explicit rules for every decision, you give the computer examples of inputs paired with correct outputs and let it figure out the patterns. A spam filter doesn't need a rule like "if the email contains 'Viagra', flag it" — instead, you show it thousands of emails labelled spam/not-spam and it learns which features (words, sender patterns, formatting) predict spam. The key shift is from programming logic to programming with data.

## Formal Definition / Statement

### Supervised Learning
Given a dataset of input-output pairs {(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)}, find a function f such that f(x) ≈ y for unseen inputs.

- **Features (x):** The measurable attributes of each data point (e.g., lines of code, token entropy, cyclomatic complexity)
- **Labels (y):** The correct answer for each data point (e.g., "readable" or "not readable")

### Classification vs. Regression
- **Classification:** Predict a discrete category (Y/N, cat/dog/bird, spam/not-spam)
- **Regression:** Predict a continuous value (temperature, price, score on 1-5 scale)

### Common Algorithms
| Algorithm | Type | Key Idea |
|-----------|------|----------|
| Logistic Regression | Classification | Linear decision boundary with probability output |
| Decision Trees | Both | Recursive feature splitting |
| SVM | Classification | Maximum-margin hyperplane |
| Random Forest | Both | Ensemble of decision trees |
| Neural Networks | Both | Layers of learnable transformations |

## Key Properties / Complexity

### Feature Engineering
The quality of features determines the ceiling of model performance. Raw data must be transformed into informative numerical representations. Domain expertise is crucial — knowing *what to measure* matters more than *which algorithm to use*.

### Training vs. Testing
- **Training set:** Used to learn the model parameters
- **Test set:** Used to evaluate generalisation to unseen data
- **Cross-validation:** Rotate which fold is the test set to get a reliable accuracy estimate with limited data

### Overfitting
A model that memorises training data (including noise) instead of learning true patterns. Symptoms: high training accuracy, low test accuracy. Remedies: regularisation, simpler models, more data.

### Feature Standardisation
Z-score normalisation: (x - μ) / σ. Necessary when features have different scales (e.g., LOC ranges 10-40 while Halstead Volume ranges 0-500+). Without it, large-valued features dominate the model.

## Worked Example
**Code Readability Classification (Scalabrino et al.):**
1. Extract 4 features from each code snippet: LOC, Token Entropy, Halstead Volume, Cyclomatic Complexity
2. Label each snippet as "readable" (mean human rating ≥ 3.6) or "not readable" (< 3.6)
3. Standardise features (z-score)
4. Train logistic regression with ridge regularisation (λ = 10⁻⁶)
5. Evaluate with 10-fold cross-validation
6. Result: ~70-80% accuracy predicting human readability judgements

## Common Pitfalls
- Confusing correlation with causation — ML finds patterns, not explanations
- Using accuracy alone as a metric — with 95% class imbalance, always predicting the majority class gives 95% accuracy but is useless
- Data leakage — letting test information leak into training (e.g., standardising on the full dataset before splitting)
- Assuming more features is better — irrelevant features add noise and overfitting
- Skipping cross-validation — a single train/test split gives unreliable estimates with small datasets

## Connections
- [[readability-classifier]] — Direct application: uses logistic regression to classify code readability
- [[sign-analysis]] — Same course, different project (static analysis for bug finding)
- [[java-for-software-analysis]] — Java ecosystem used for implementing ML pipelines with WEKA
- [[data-flow-analysis]] — Contrast: dataflow analysis is deterministic; ML is probabilistic
- [[confidence-intervals]] — Statistical evaluation of model performance
- [[effect-sizes]] — Measuring practical significance of model improvements

## Open Questions
- How do we choose between interpretability (logistic regression) and accuracy (neural networks)?
- What is the minimum dataset size for reliable classification?
- How do we handle class imbalance beyond simple thresholding?
