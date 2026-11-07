---
title: "Evaluating and Comparing Search Algorithms"
tags: [concept, search-based-software-engineering, semester-2, statistics]
course: "Search-Based Software Engineering"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[metaheuristics]]", "basic hypothesis testing (null hypothesis, p-value)"]
---

## One-line Summary

A randomised algorithm produces a distribution, not a number — so comparing two of them requires
repeated independent runs, a significance test on the distributions, an effect size, a confidence
interval, and a correction when several comparisons are made at once.

## Core Intuition

"A randomised algorithm may be strongly affected by chance: it may find an optimal solution
quickly or may never converge towards an acceptable solution. Running a randomised algorithm twice
on the same instance of a software engineering problem usually produces different results." Every
claim of the form "technique A is better than B" is therefore a claim about two probability
distributions, and it needs evidence proportional to that.

The lecture's motivating experiment is deliberately tiny and deliberately inconclusive: fault
finding on crashing Android apps, n = 10 runs, technique A = random testing with a 70 % success
rate (7 of 10 runs found a crash), technique B = tabu search with 50 % (5 of 10). "Is A better
than B?" — the slide then plots the probability of obtaining exactly those counts at n = 10 and
n = 100, which is the answer: at n = 10 the outcome is unremarkable under either hypothesis.

The second intuition is that significance is not the same as importance. "With a large enough n,
one can obtain statistically significant differences even if they are so small as to be of no
practical value. Therefore, in addition to statistical difference, it is crucial to assess the
magnitude of the improvement, i.e. the effect size."

## Formal Definition / Statement

**The procedure**, as the slide lays it out: "When comparing algorithms A and B we need to decide
on a measure M, e.g. code coverage or execution time. We run both A and B a large enough number
(n) of times, in an independent way, to collect information on the probability distribution of M
for each algorithm. Statistical test to assess whether there is enough empirical evidence to claim
that there is a difference between the two algorithms (e.g. A is better than B)."

**Hypotheses and errors.**

- "Null Hypothesis H₀: there is no difference between A and B." The test aims to decide whether H₀
  should be rejected. "What aspect of the probability distribution is being compared depends on the
  used statistical test" — e.g. "a t-test compares the mean values of two distributions, whereas
  other tests focus on the median or proportions".
- "Type I: H₀ is rejected although it is true" (claiming a difference that is not there).
- "Type II: H₀ is accepted when it is false" (claiming equivalence when there is a difference).
- "The p-value of a statistical test denotes the probability of a Type I error. The significance
  level of a test is the highest p-value one accepts for rejecting H₀. A typical value … is
  α = 0.05. The use of α = 0.05 is much debated."

**One- vs two-tailed.** A one-tailed test assumes a direction ("a new sophisticated algorithm A is
better than a naive algorithm B"); a two-tailed test rejects when the two differ in either
direction. The historical example: checking the gold content of coins, where an under-weight coin
is fraud but an over-weight one is not, so a one-tailed test is legitimate; and the verdict for
this field — "In software engineering there are hardly any cases where a one-tailed test would be
used; two-tailed tests should be used."

**Parametric vs non-parametric.** "A parametric test makes assumptions on the underlying
distribution of the data. E.g., the t-test assumes normality and equal variance of the two data
samples. A nonparametric test makes no assumptions about the distribution of the data.
Nonparametric tests are usually less powerful than parametric ones when the latter's assumptions
are fulfilled. Mann-Whitney U Test / Wilcoxon Rank-Sum Test." The decisive sentence: "The
assumptions of the t-test are, in general, not met."

**Sample size.** "In general, one cannot know how many data points (n) one needs to reach reliable
results. A rule of thumb is to have at least n = 30 for each data sample. This rule of thumb
originates from behavioural science, we don't really know if it is effective for randomised
algorithms in software engineering."

**Deterministic baselines.** "If one of them is deterministic, it is still important to use
statistical testing. Use the nonparametric one-sample Wilcoxon test. Given m_B (the performance
measure of the deterministic algorithm B), a one-sample Wilcoxon test would verify whether the
performance of A is symmetric around m_B — that is, whether by using A, one is as likely to obtain
a value lower than m_B as otherwise."

**Effect sizes.** "Unstandardised effect sizes are dependent on the unit of measurement.
Standardised are independent of the unit of measurement." The d family: "d = (μ_A − μ_B)/σ", with
the stated problem "assumes normality of the data, and strong departures can make it meaningless".
The non-parametric alternative: Vargha and Delaney's **Â12**, "the probability that running
algorithm A yields higher M values than running another algorithm B", with "if the two algorithms
are equivalent, then Â12 = 0.5" and "Â12 = 0.7 entails one would obtain better results 70% of the
time with A". Computed from a rank sum: "Â12 = (R₁/m − (m+1)/2)/n", where m and n are the two
sample sizes ("usually m = n") and R₁ is the rank sum of the first group.

**Odds ratio** for dichotomous results: given a = number of times A finds an optimal solution and
b for B, the ratio uses a constant ρ (e.g. 0.5) "to avoid problems with zero occurrences"; ψ = 1
means no difference, ψ > 1 favours A.

**Confidence intervals.** "A (1 − α) CI is a set of values for which there is (1 − α) probability
that the value of the effect size lies in that range." The slide's example is printed with a typo
worth noticing: "Â12 = 0.54 and a (1 − α) CI with range [0.49, 59]" — 59 is not a probability and
must be 0.59.

## Key Properties

**Multiple comparisons inflate the error rate, and the lab quantifies it.** "Each of these tests
has a 5% chance of a false alarm … With six tests these chances add up: if all six null hypotheses
were true and the tests were independent, the probability of at least one false alarm would be
1 − 0.95⁶ ≈ 26%" (computed: 0.2649). The lab's response is a Holm correction across the whole
family of six comparisons, decided before looking at the numbers: "Decide what counts as one
family of comparisons before looking at the numbers, and correct across the whole family."

**Correction changes the verdict only in the middle.** The lab's reading: "All comparisons
involving random search or hillclimbing have p-values so small that multiplying them by up to six
changes nothing … the correction mainly affects middling p-values. A p-value of 10⁻⁸ stays
negligible however many tests we run, and 0.5 was not significant anyway; but among six tests, a
p-value of 0.02 can become 0.12. This matters most for small experiments: with five runs per
algorithm, even perfect separation (every run of one algorithm beats every run of the other) gives
p = 0.008 at best, which after the correction is at best 0.048."

**Never compare two batches of the same algorithm and call it a difference.** The notebook runs a
control: "We can watch this happen with our two batches of simulated annealing, where we know that
there is no real difference … The observed difference is one that shuffling produces all the time
(in 73% of the shuffles), and the Mann-Whitney test agrees (p = 0.49). Most pairings are ties, and
wins and losses roughly balance: A12 = 0.53. This is how much two batches of the same algorithm
differ by chance alone; a difference between two algorithms has to be clearly larger than this."

**Ties matter for Â12.** On n-queens many runs reach the same fitness, so most pairings are ties;
that is why the reported Â12 values sit near 0.5 despite dramatic p-values for other pairs, and why
the bootstrap interval is reported alongside.

## Worked Example

**Â12 from the lecture's own numbers.** Data X = {42, 11, 7} and Y = {1, 20, 5}. Pooled and
ranked ascending (1, 5, 7, 11, 20, 42) gives X the ranks {6, 4, 3} with rank sum R₁ = 13, and Y the
ranks {1, 5, 2}. With m = n = 3:

Â12 = (R₁/m − (m+1)/2)/n = (13/3 − 2)/3 = (4.3333 − 2)/3 = 0.7778

So A is expected to beat B about 78 % of the time on this sample. Checked against the definition by
enumeration: of the 9 cross pairs, A wins 7 (42 beats 1, 20 and 5; 11 beats 1 and 5; 7 beats 1 and
5) and loses 2 (20 > 11, 20 > 7), so 7/9 = 0.777… — the formula and the definition agree.

**The lab's six-way comparison on n-queens**, 30 runs each, Holm-corrected, with bootstrap CIs:

| Comparison | p (raw) | Holm p | Â12 [95 % bootstrap] |
|---|---|---|---|
| Random Search vs Hill Climbing | 6e-12 | 3e-11 | 0.00 |
| Random Search vs Tabu Search | 5e-08 | 1e-07 | 0.12 |
| Random Search vs Simulated Annealing | 1.5e-12 | — | — |
| Hill Climbing vs Tabu Search | 4.9e-08 | — | — |
| Hill Climbing vs Simulated Annealing | 4.3e-09 | — | — |
| Tabu Search vs Simulated Annealing | 0.5 | — | interval includes 0.5 |

The reading the course draws from it: random search loses to everything (which is what the
baseline is for); hill climbing and tabu search both beat random search; and tabu search versus
simulated annealing is not decidable on this data — "we simply have no evidence of a difference",
which is not the same as evidence of sameness.

## Common Pitfalls

- **Reporting means only.** "Looking at averages can be misleading, as randomised algorithms can
  yield very complex and high variance probability distributions."
- **Using a t-test by default.** Its assumptions "are, in general, not met" for these measures.
- **One-tailed tests to make a result significant.** The p-value drops mechanically; the field's
  guidance is two-tailed.
- **n = 5 runs and a conclusion.** The lab computes the ceiling: perfect separation at n = 5 gives
  p = 0.008, which after Holm correction is 0.048 — and not significant at all once ties exist.
- **Quoting a p-value without an effect size.** Significance says "some difference exists";
  Â12 or the odds ratio says whether anyone should care.
- **Comparing a deterministic baseline with a two-sample test.** Use the one-sample Wilcoxon
  against m_B.
- **Uncorrected families of comparisons.** Six tests at α = 0.05 carry a 26 % chance of at least
  one false alarm.
- **Reading a failed test as proof of equality.** Not rejecting H₀ is absence of evidence.

## Connections

- [[hill-climbing]], [[tabu-search]], [[simulated-annealing]], [[evolutionary-algorithm]] — the
  algorithms being compared, and every p-value above comes from this page's procedure.
- [[metaheuristics]] — why the question "which is better" is unavoidably statistical.
- [[msr-statistical-methods]] — the repository-mining course's version of the same machinery
  (Welch's t-test, effect sizes, paired designs).
- [[threats-to-validity]] — the broader question of what an experiment can support; a single
  instance and a single configuration is a narrow claim.
- [[statistical-significance]] and [[effect-sizes]] — the Semester 1 foundations this lecture
  applies.
- [[search-based-software-engineering-lecture-2]] — where the lecture delivers it.

## Open Questions

- **The slide's confidence-interval example is printed as [0.49, 59]**, which cannot be an Â12
  interval; it is reproduced here with the correction noted, but the intended numbers are unknown.
- **The odds-ratio slide's formula is missing from the extracted text** (the ρ term appears without
  the expression it belongs to), so the exact estimator used is not recoverable from this deck.
- **No power analysis is offered** — the course says one cannot know the required n, then gives a
  rule of thumb of 30 with a caveat.
- **Which correction to use** (Holm, Bonferroni, or none) is demonstrated in the lab but never
  prescribed in the lecture.
- **Whether ties should be handled by a different Â12 variant** is not addressed, although the
  n-queens results are dominated by ties.