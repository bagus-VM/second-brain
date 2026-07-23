---
title: "RepEng In-Class Exercise 3 — Hypotheses"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| Exercises 1–2 — Hypotheses | [[hypothesis-formulation]] |
| Exercises 3–4 — Case Studies & Occam's Razor | [[hypothesis-formulation]] · [[presenting-experiments]] |
| Exercises 5–6 — Presenting Experiments | [[presenting-experiments]] |
| Exercises 7–9 — Levels of Equivalence | [[levels-of-equivalence]] |
| Exercise 10 — Algorithm Runtime Comparison | [[levels-of-equivalence]] · [[presenting-experiments]] |
| Exercise 11 — Comparing Methods | [[presenting-experiments]] |

# In-Class Exercise Sheet 3 — Hypotheses & Experimental Design

Based on Justin Zobel's "Writing for Computer Science".

---

## Exercise 1 — Word Puzzle

Words characterizing a good research hypothesis: **PRECISE, SPECIFIC, UNAMBIGUOUS**

Words that do NOT characterize a good hypothesis: LOOSE, CONTRADICTORY, LIMITATIONS (though acknowledging limitations separately is important)

---

## Exercise 2 — True/False on Hypothesis Guidelines

**(a)** "The more loose a concept is, the easier it is to validate experimentally."
→ **False.** Loose concepts are harder to measure and validate precisely. A vague hypothesis cannot be clearly confirmed or rejected.

**(b)** "A hypothesis should be stated so precisely that two readers interpret it in the same way."
→ **True.** This is exactly Zobel's point — unambiguous interpretation is essential for reproducibility.

**(c)** "A good hypothesis should make clear what is not being claimed."
→ **True.** Setting clear boundaries (scope limitations) prevents misunderstanding and makes the hypothesis falsifiable.

---

## Exercise 3 — Case Studies on Hypotheses

**(a) Hypothesis A:** "Our system improves database performance."
→ **Violates guidelines.** Too vague: "improves" by how much? "Performance" — throughput? latency? Which workload? Under what conditions? Not falsifiable.

**(b) Hypothesis B:** "Our system reduces average query latency by at least 20% on TPC-C workloads under high contention."
→ **Follows guidelines.** Specific metric (query latency), quantified improvement (20%), defined benchmark (TPC-C), defined condition (high contention). Falsifiable and measurable.

**(c) Hypothesis C:** "Our system improves performance in most realistic scenarios."
→ **Violates guidelines.** "Most realistic scenarios" is undefined and unfalsifiable. "Performance" is vague. No quantification.

---

## Exercise 4 — Occam's Razor

"Where two hypotheses fit the observations equally well and one is clearly simpler than the other, the simpler should be chosen."

This principle is known as **Occam's Razor** (or the principle of parsimony).

---

## Exercise 5 — Presenting Experiments (True/False)

**(a)** A clear experiments section separates setup, results, and interpretation. → **True**
**(b)** The experimental setup should explain datasets, baselines, and evaluation metrics. → **True**
**(c)** A figure should be accompanied by an explanation of what it shows and why it matters. → **True**
**(d)** It is important to state limitations clearly. → **True**
**(e)** The experiments section should only present positive outcomes. → **False** — negative or null results should also be reported for scientific integrity.

---

## Exercise 6 — Coffee Recommendation Case Study

**(a)** "We evaluate our method on data collected from five campus cafés and compare it against two baselines."
→ **Setup** — describes what is being evaluated and the comparison framework.

**(b)** "Our method reduces the average search time by 23% compared with the popularity-based baseline."
→ **Result** — reports a specific quantitative finding.

**(c)** "This suggests that personalization is especially useful when users have strong dietary preferences."
→ **Discussion** — interprets results and draws conclusions.

**(d)** "We measure recommendation quality using click-through rate and normalized discounted cumulative gain."
→ **Setup** — defines the evaluation metrics.

**(e)** "The gains are smaller late in the day, possibly because several cafés have fewer items available."
→ **Discussion** — explains a pattern in the results with a possible reason.

**(f)** "Figure 3 shows that the proposed method remains faster than all baselines as the number of users increases."
→ **Result** — presents a specific finding from a figure.

---

## Exercises 7 & 8 — Levels of Equivalence

### Definitions:
- **Bitwise identity:** Byte-for-byte identical (same MD5 hash)
- **Structural equivalence:** Same content, different order/formatting
- **Functional equivalence:** Same outputs for same inputs
- **Behavioral equivalence:** Same observable behavior including I/O, timing, side effects

### Exercise 8: Identify the strongest equivalence

**(a)** Two JPEG files with identical MD5 hashes.
→ **Bitwise identity** — MD5 collision is extremely unlikely, so identical hashes imply identical bytes.

**(b)** Two JSON files with same properties but different order.
→ **Structural equivalence** — same content, different representation order.

**(c)** Two XML files with same entities but different order.
→ **Structural equivalence** — same content, different element ordering.

**(d)** Java and Python programs produce identical outputs for all tested inputs.
→ **Functional equivalence** — same outputs for same inputs, but different implementations.

---

## Exercise 9 — f(x) = x · 2 vs g(x) = x + x

Are f and g functionally equivalent?

**Yes, for integer arithmetic.** Both functions return 2x for all inputs. They are mathematically identical.

**However:** For floating-point arithmetic, they might NOT be functionally equivalent. Multiplication (`x * 2`) and addition (`x + x`) can produce slightly different results due to floating-point rounding. Example: for very large or very small floating-point numbers, the intermediate representations may differ.

**For integer types:** Functionally equivalent. For floating-point: potentially not.

---

## Exercise 10 — Algorithm Runtime Comparison

The table shows runtimes for Algorithms A and B over multiple runs.

**(a)** Can we directly compare the averages?
→ **Not reliably.** We need to consider:
- Variance/standard deviation (Algorithm B has much higher variance: 90, 200, 95 ms)
- The outlier in run 2 for Algorithm B (200ms vs ~90-95ms in other runs)
- Sample size is too small (only 3 runs)
- We should use statistical tests (e.g., Wilcoxon signed-rank) rather than just comparing means

**(b)** Better way to compare runtimes:
- Run more iterations (e.g., 30+ runs)
- Report median and interquartile range (more robust to outliers)
- Use statistical hypothesis testing (e.g., Mann-Whitney U test)
- Report confidence intervals
- Control for system load and warmup effects

---

## Exercise 11 — Comparing Methods (English Writing)

> *Write a comparison using irregular comparatives, less/fewer/more/much/many, and at least two adverbs.*

**Example answer:**

In both methods, the length of the study was the same (four months). However, Method A had **more** participants (375 vs 421 — wait, B had more). Let me redo:

Method B had **more** participants (421) than Method A (375). However, **fewer** words were learned actively in Method B (456) compared to Method A (500). Method A enabled learners to understand **many more** words (3,000 vs 1,500). On the other hand, Method B taught **more** tenses (8 vs 5) and led to **much** better writing ability. Method B also produced **fewer** speaking errors (**efficiently** reducing them to 15% vs 35%). Overall, Method A performed **significantly** better for vocabulary acquisition, while Method B worked **more** effectively for grammar and accuracy.


---

## Related Resources

### 📖 Reproducibility Engineering – Lecture 3: Hypotheses
- Lecture topic: [[reproducibility-engineering-lecture-3]]

**Key concepts covered:**
- [[hypothesis-formulation]]
- [[presenting-experiments]]
- [[levels-of-equivalence]]
- [[reproducibility-crisis]]
- [[repeat-reproduce-replicate]]
- [[computational-reproducibility-in-ml]]
- [[research-artifacts]]
