---
title: "Mining Software Repositories — Lecture 7 Overview (Methods: Paradigms, Sampling, Statistics, Grounded Theory)"
tags: [topic, mining-software-repositories, semester-2, research-methods]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 7 is the methods chapter: the paradigm decides how a question is framed, sampling decides
which data the claim rests on, statistics decide whether an observation is more than noise, and
grounded theory is offered for the interpretivist studies statistics cannot serve.

## Core Map

```
Chapter 7 — Methods
│
├── Research paradigms
│   ├── Positivism / Interpretivism / Pragmatism; pragmatism is flexible
│   ├── RQ framing: positivist = hypotheses, interpretivist = open exploration
│   ├── Hypothesis: confirmatory (deductive) vs exploratory (inductive)
│   └── Falsifiability: "nesting depth unrelated to readability" is trivially falsifiable
│           -> [[msr-research-paradigms]] [[null-and-alternative-hypothesis]]
│
├── Sampling
│   ├── Population ⊇ sampling frame ⊇ sample
│   ├── Non-probabilistic: convenience, purposive, snowball, respondent-driven
│   ├── Probabilistic: simple random, systematic random
│   ├── Multi-stage: stratified / quota, cluster; other: whole frame, panel
│   └── Representativeness is dimension-specific; randomness ≠ representativeness
│           -> [[msr-sampling]]
│
├── Basic statistics
│   ├── Descriptive vs inferential; p-values, significance level alpha, decision rule
│   ├── Test families: Welch's t, Shapiro-Wilk, Mann-Whitney-U, Levene, ANOVA
│   ├── Effect sizes (Cohen's d) and their interpretation
│   ├── Type I / Type II errors, family-wise error rate, Bonferroni correction
│   └── Multiple variables: dependent, independent, confounding; linear models,
│           omnibus + post-hoc coefficient tests, GLM, GAM, ML
│           -> [[msr-statistical-methods]] [[statistical-significance]]
│              [[effect-sizes]] [[confidence-intervals]] [[p-values]]
│
└── Grounded theory
    ├── Straussian variant; open -> axial -> selective coding -> forming theory
    ├── Memoing as the backbone of inductive reasoning
    ├── Research questions may develop during coding
    ├── Literature as secondary source (contrast with Glaserian)
    └── Theoretical sampling until saturation
            -> [[grounded-theory]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[msr-research-paradigms]] | The paradigms decide question framing, method choice, and what counts as knowledge |
| [[msr-sampling]] | Population, frame, sample — and why randomness is not representativeness |
| [[msr-statistical-methods]] | Hypothesis testing, effect size, and confidence interval as the three inferential concepts used |
| [[grounded-theory]] | Straussian grounded theory: open, axial, selective coding, memos, saturation |
| [[p-values]] | The probability of the observed data given the hypothesis |
| [[confidence-intervals]] | An interval expected with probability C% to contain the parameter |
| [[effect-sizes]] | Cohen's d: the distance between means relative to pooled standard deviation |

## Lecture Structure
1. **Paradigms** — the three definitions, the "measure to learn objective truth" versus
   "understand individuals to learn subjective perspectives" contrast, pragmatism's flexibility,
   and how each paradigm maps onto quantitative, qualitative, or mixed MSR research.

2. **Formulating research questions** — hypothesis versus open exploration, inductive and
   deductive reasoning, the exploratory-confirmatory diagram.
3. **Falsifiability** — the requirement that falsification teach something; the trivially
   falsifiable nesting-depth hypothesis and its better-framed replacement.
4. **Sampling** — the role of sampling, the nested sets with a worked example on the male-to-female
   ratio in open source, non-probabilistic, probabilistic, and multi-stage methods.
5. **Representativeness** — its definition, its importance for positivism and its irrelevance for
   interpretivism, and the bimodal example separating randomness from representativeness.
6. **Foundations of statistics** — descriptive versus inferential, the three inferential concepts
   the course covers and the three it excludes, hypothesis testing with the table of null
   hypotheses, the decision rule, and the problems: no binary results and p-hacking.
7. **Effect sizes and confidence intervals** — Cohen's d and the interpretation scale, the z_C
   table, the worked interval example, and the correct versus wrong interpretations.
8. **Errors and repeated experiments** — Type I and Type II errors, the family-wise error rate
   with the 0.95^k figures, Bonferroni correction, and a worked two-test example.
9. **Independent and paired data** — the two designs for studying code review, the paired
   difference population and the paired t-test.
10. **Multiple variables** — dependent, independent, and confounding variables; the linear model
    and its parameters; two-stage coefficient testing; generalized linear models; additive
    models; and machine learning models that cannot say whether a relationship is significant.

11. **Grounded theory** — the motivation against statistics, the three variants and the choice
    of Straussian, the coding pipeline, memoing, theoretical sampling, and saturation.

## Exam-Relevant Points

1. **The paradigm determines the method, not the other way round.** Positivism asks for
   measurable variables and causal relations; interpretivism asks for meanings and perceptions.
2. **A hypothesis must be falsifiable in a way that teaches something.** The nesting-depth
   example is the slide's own demonstration of a badly framed hypothesis.
3. **Sample ⊆ sampling frame ⊆ population**, and the three sets change with the research
   question.
4. **Randomness does not imply representativeness.** The bimodal example shows a small sample
   that reproduces the overall mean while representing neither subgroup.
5. **The decision rule is one-sided**: p > alpha means fail to reject; p ≤ alpha means reject.
   "Accept" is not the alternative to "fail to reject".
6. **Effect size and significance answer different questions**, and Cohen's d of 1 means the
   difference of means is one pooled standard deviation.
7. **The confidence interval reading is a trap**: the correct statement is about future
   replications falling into the interval, not about the true value lying inside it.
8. **Repeated tests inflate the error rate.** With alpha = 0.05 and twenty tests, the probability
   of no false positive is about 0.36; Bonferroni adjusts alpha or the p-value.
9. **Paired data require paired difference tests**, and the design choice trades efficiency
   against carry-over effects.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-6]] — the studies whose statistics this chapter
  formalizes.
- [[mining-software-repositories-lecture-8]] — validity, the chapter that judges these methods.
- [[msr-research-paradigms]] — the paradigm frame.
- [[msr-sampling]] — sampling and representativeness.
- [[msr-statistical-methods]] — the statistical toolkit.
- [[grounded-theory]] — the qualitative alternative.
- [[null-and-alternative-hypothesis]] — hypothesis testing in detail.
- [[p-values]] — the probability statement, and why it is not a score.
- [[confidence-intervals]] — the interval construction and its interpretation.

## Open Questions
- **Statistical power is explicitly excluded** from the course scope, though it is named as
  something to consider when planning sample sizes.
- **Bayesian methods are excluded** without explanation, so the lectures offer one inferential
  tradition only.
- **Linear models are "considered separately"**, and that treatment is not referenced in this
  chapter.
- **Whether the grounded theory research question may be fixed in advance** is stated as
  permitted, but no criterion for the choice is given.
- **The threshold between exploratory and confirmatory research is described, not decided**.
