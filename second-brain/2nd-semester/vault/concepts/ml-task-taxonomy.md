---
title: "ML Task Taxonomy: Six Families and Their Security Uses"
tags: [concept, ml-security, semester-2, ml-basics]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[ml-learning-paradigms]]"]
---

## One-line Summary

L1 reduces machine learning to six task families — regression, classification, clustering, association rules, dimensionality reduction, generative models — each with a slide definition, a security example, and a list of algorithms.

## Core Intuition

A task is defined by the *shape of the output*, not by the algorithm. Regression returns a number, classification a label from a known set, clustering groups whose labels you do not have, association rules co-occurrence statements, dimensionality reduction a smaller feature space, generative models new data. Because the shape matters, one algorithm family can serve several tasks and every task has many implementations — hence the algorithm column on each slide.

In security it pays off differently: the six tasks recur in every domain, but the *features* never do. Recognising "this is a clustering problem" tells you what data you need, not what to measure.

## Formal Definition / Statement

| Task | Slide definition | Cybersecurity example | ML algorithms | DL algorithms |
|---|---|---|---|---|
| **Regression (prediction)** | predicting a continuous numerical value based on input data | predict the next user action, detect outliers such as credit-card fraud | linear, polynomial, ridge regression, decision trees, random forest, support vector regression (SVR) | ANN, RNN, neural Turing machine (NTM), differentiable neural computer (DNC) |
| **Classification** | separating things into different categories/classes | a spam filter separating spam from other messages | logistic regression, k-nearest neighbours, SVM, kernel SVM, decision tree, random forest | ANN, CNN |
| **Clustering** | ≈ classification but with unknown classes; grouping by similarity | anomaly detection in an IDS; grouping malware samples by similar characteristics | Bayesian, k-means, mixture model (LDA), Gaussian mixture model, mean-shift | self-organising maps (SOM) / Kohonen networks |
| **Association rule learning** | recommending something based on previous experience | incident response (learn a response type); risk management (risk scores for vulnerabilities from their description) | Apriori, Eclat, FP-Growth | deep restricted Boltzmann machine, deep belief network, stacked autoencoder |
| **Dimensionality reduction (generalisation)** | searching common and most important features in multiple examples | face recognition | PCA, SVD, t-SNE, linear discriminant analysis, LSA, factor analysis, ICA, NMF | — (no DL column on the slide) |
| **Generative models** | creating something based on previous knowledge of a distribution | offensive use: generate input parameters to test an application for injection vulnerabilities | Markov chains, genetic algorithms | variational autoencoders, GANs, Boltzmann machines |

## Key Properties

- **Task ≠ algorithm ≠ paradigm.** The six tasks are one axis, the approaches on [[ml-learning-paradigms]] another. A spam filter can be naive Bayes, logistic regression, an SVM or k-NN; it is still classification.
- **Deep learning is not a seventh task.** It is a column of *implementations* for four of the six; dimensionality reduction has none.
- **Clustering is often a pipeline step, not the answer.** To cope with heterogeneous devices, cluster them first, then classify traffic inside each class.
- **Dimensionality reduction is "usually one task in a more complex pipeline"**, for when there are too many features to cluster.
- **Generative models alone produce data rather than a judgement**, which is why the example is offensive.
- **Two different LDAs.** "Mixture model (LDA)" under clustering is latent Dirichlet allocation; "Linear Discriminant Analysis (LDA)" is another method sharing the abbreviation.

## Worked Example

A network of workstations, servers, PLCs and IoT devices. Cluster devices by similarity first, because one model across device types averages away the differences (SOM or k-means). Inside each cluster, train a classifier on labelled traffic — scan, spoof, DoS. If the feature space is too wide, reduce it with PCA first. When an incident is confirmed, association rules suggest a response type. Four of the six appear in one deployment; none replaces the others.

## Common Pitfalls

- **Calling clustering "classification without labels".** There is no ground truth, so "accuracy" is undefined.
- **Assuming the fanciest algorithm wins.** The slide lists decision trees next to neural networks in the same column; nothing there ranks them.
- **Forgetting the evaluation mismatch.** Regression is judged on prediction error, classification on precision and recall, clustering on whether a human finds the groups useful.
- **Treating association rules as prediction.** They state co-occurrence in past data, not causation.

## Connections

- [[ml-learning-paradigms]] — the orthogonal axis: how the model is trained, not what it outputs.
- [[ml-for-security-domains]] — the same six tasks instantiated per domain.
- [[naive-bayes-text-classification]] — classification, worked end to end.
- [[classification-metrics]] — how the classification column is scored.

## Open Questions

- The slides give no criteria for choosing among algorithms in a column. Is the answer "whatever scikit-learn makes easiest"?
- Dimensionality reduction carries a face-recognition example that is never developed; whether it is examinable as a security use case is unclear.
