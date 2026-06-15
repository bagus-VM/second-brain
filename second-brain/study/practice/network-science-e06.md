---
title: "Exercise Sheet 6 — Social Context"
tags:
  - practice
  - network-science
  - semester-1
course: "Network Science"
status: current
last_updated: 2026-06-02
---

# Exercise Sheet 6 — Social Context

## Exercises

### 6.A Homophily and Measurement

**Exercise 6.A.1: Measuring Homophily by Hand**

A friendship network of 8 students: 4 study CS (C1–C4) and 4 study Business (B1–B4).
Edges: C1–C2, C1–C3, C2–C3, C3–C4, C4–B1, B1–B2, B2–B3, B3–B4.

1. Count edges within CS, within Business, and across departments.
2. Compute the E-I index: (E − I)/(E + I), ranging from −1 (pure homophily) to +1 (pure heterophily).
3. Is this network homophilic, heterophilic, or neutral with respect to department?
4. What would the E-I index be if ties formed randomly regardless of department?

---

**Exercise 6.A.2: Homophily vs. Confounding**

Using `nx.karate_club_graph()` with the "club" attribute as the group label:

1. Count within-faction and cross-faction edges.
2. Compute the E-I index for faction.
3. Compute the expected cross-faction edge fraction under random mixing.
4. Is the network homophilic? By how much relative to random?

### 6.B Affiliation and Similarity

**Exercise 6.B.1: Three Closure Types**

Affiliation network: students S1, S2, S3, S4 and courses C1, C2, C3.
Enrolments: S1–C1, S1–C2, S2–C1, S3–C2, S3–C3, S4–C3.

1. Project onto the student layer (two students connected if they share a course).
2. Identify one example each of: (a) triadic closure, (b) focal closure, (c) membership closure.
3. If S2 joins C2, does this enable any new closure?
4. What information is lost when projecting?

---

**Exercise 6.B.2: Bipartite Projection in Python**

Implement the affiliation network from 6.B.1 in NetworkX and compute a weighted projection onto the student layer.

### 6.C Social Dynamics and Causal Inference

**Exercise 6.C.1: Distinguishing Social Forces**

For each scenario, state whether it is best explained by selection, socialization, or confounding:

1. Two students both like jazz, become friends, and a year later both discover classical music.
2. Two colleagues at a tech startup both use Python; their friendship forms day 1.
3. Students in the same dormitory become friends and all prefer the same pizza place.
4. A smoker quits after befriending non-smokers.

For each: what data (cross-sectional vs. longitudinal, observational vs. experimental) is needed to identify the mechanism?

---

**Exercise 6.C.2: Designing a Study**

You want to know whether students in the same study group become more similar in performance (socialization) or whether similar students form study groups together (selection).

1. What cross-sectional data would you collect?
2. What longitudinal data is needed to separate the mechanisms?
3. What would an ideal experimental design look like?
4. What would you observe if both mechanisms operate?

### 6.D Spatial Segregation

**Exercise 6.D.1: Schelling Model Analysis**

In Schelling's model, agents on a grid prefer at least k of 8 neighbours to be the same type. Dissatisfied agents move.

1. If k = 1, do you expect strong segregation? Why?
2. If k = 5 (majority), what outcome do you predict?
3. Why is it surprising that mild preferences (k = 3 or k = 4) can still produce strong global segregation?
4. How does this connect to homophily? What is the "network" in Schelling's model?

---

**Exercise 6.D.2: Schelling Simulation**

Implement a 1D Schelling model: agents in a line; each needs at least threshold fraction of left+right neighbours to be the same type. Unhappy agents swap with random unhappy agents of the opposite type.

1. Implement and run for 100 steps.
2. Visualise initial and final states.
3. Vary threshold from 0.1 to 0.9 and plot average run-length at convergence.
4. At what threshold does strong segregation emerge?

---

## Related Lectures

- [[network-science-l06]]
- [[network-science-l07]]
- [[network-science-l08]]
- [[ei-index]] — the (E−I)/(E+I) measure of homophily
- [[triadic-focal-membership-closure]] — three mechanisms for projected-edge formation
- [[confounding]] — the third explanation for observed similarity
- [[selection-vs-socialization]] — the two causal mechanisms being disentangled
- [[homophily]] — the broader phenomenon
- [[affiliation-networks]] — the bipartite source for focal/membership closure
