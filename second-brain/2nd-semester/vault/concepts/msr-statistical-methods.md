---
title: "Statistical Methods for MSR"
tags: [concept, mining-software-repositories, semester-2, statistics]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]", "[[statistical-significance]]"]
---

## One-line Summary

The statistics that make an MSR claim defensible: hypothesis testing to decide whether an
observation is likely random, effect sizes to say how big it is, and confidence intervals to say
how uncertain the estimate is.

## Core Intuition

The lecture's foundation slide states the purpose plainly: "A key aspect of scientific research
is to test if a data is consistent with a hypothesis. Statistics provide the means to
operationalize such tests."

Two families are distinguished:

- **Descriptive statistics** — "to understand properties of the data", e.g. mean, median,
  standard deviation, skewness; "Can be used to report properties of results or experiments.
  **Not suitable for generalization as the properties are only about the observed data.**"
- **Inferential statistics** — "tries to understand properties of the probability distribution
  that generated the data", by "fitting probability distributions to data or given estimates for
  parameters of the distribution"; "Suitable for generalization to all data that follows the
  same underlying distribution", which "follows from the representativeness of a sample".

So inference inherits the sampling decision — see [[msr-sampling]].

The lecture scopes itself: three inferential concepts are considered — hypothesis testing, effect
sizes, confidence intervals — while "statistical power, standard errors, Bayesian methods" are
"things we do not consider", and "Linear models are also statistics and considered separately".

## Formal Definition / Statement

**Hypothesis testing.** "Hypothesis testing evaluates assumptions about data. Assumption ==
Hypothesis." The slides ask: "What is the assumption of a test?" and "What does 'rejected at some
level of significance' mean?"

- **Null hypothesis (H₀)**: "Assumption of the test holds and is failed to be rejected at some
  level of significance."
- **Alternative hypothesis (H₁, Hₐ)**: "Assumption of the test does not hold and is rejected at
  some level of significance."

**P-values.** "The probability of the observed data or more extreme data, given the null
hypothesis is true", "calculated using the probability density function of a test statistic".

**Significance level α.** "Probability of rejecting the null hypothesis, given that it is true."
"Depends on domain"; common values "0.05 (de-facto standard)" and "0.005 (currently proposed
newer standard to reduce false positives)". Confidence level = "1 − α". Decision rule as printed:
"If p-value > alpha fail to reject null hypothesis. If p-value ≤ alpha reject the null
hypothesis → significant result".

**Student's t-distribution.** "Test statistic used for estimating mean values for normally
distributed data"; its "probability density function for the location of the deviation of a
sample mean value from the real mean value"; "roughly bell-shaped", with "longer tails than
normal distribution".

**Welch's t-test.** "Also requires calculation of the degrees of freedom, which we omit here."
Null hypothesis: "The means of two independent, normally distributed populations X₁ and X₂ are
equal." The statistic as printed:

```
t = (mean(X₁) − mean(X₂)) / √( sd(X₁)²/N₁ + sd(X₂)²/N₂ )
```

**Null hypotheses of the important tests**, as printed on the slide:

| Test | Null hypothesis as printed |
|---|---|
| Shapiro-Wilk test | "A population of 3 to 5000 independent samples is normally distributed" |
| Anderson-Darling test | (for larger sample sizes) |
| Kolmogorov-Smirnoff test | "Two independent populations have the same probability distribution" |
| Mann-Whitney-U / Wilcoxon-Ranksum | "The values from one population dominate the values of another independent population (more or less difference of means/medians)" |
| Levene's test | "The variances of a group of populations are equal" |
| ANOVA | "The mean values of a group of independent populations are equal" — "Only tells us that there at least one population is different from the others. This is evaluated with a post-hoc test (e.g., Tukey's HSD)." |

**Combinations of tests** — the decision flow on the slide: Shapiro-Wilk test for normality; then
"Both normal → Welch's t-test", "At least one not normal → Mann-Whitney U-test".

**Effect size.** Cohen's *d* as printed:

```
d = (mean(X₁) − mean(X₂)) / s

s = √( ((N₁−1)·sd(X₁)² + (N₂−1)·sd(X₂)²) / (N₁ + N₂ − 2) )
```

"s is the pooled standard deviation"; "d = 1 means that the difference of means is 'one standard
deviation'". "Measures the distance between central tendency with respect to the variance." The
slides also name "Hedges' g*, Glass' Δ that all use a similar concept". Interpretation table (Cohen
and Sawilowsky; "Designed for social sciences. Should be used with care, but is broadly used in
many domains"): d < 0.01 Negligible; d < 0.2 Very Small; d < 0.5 Small; d < 0.8 Medium; d < 1.2
Large; d < 2.0 Very Large; d ≥ 2.0 Huge.

**Confidence intervals.** "A C% confidence interval θ for some parameter p is an interval that is
expected with probability C% to contain p." For the mean of normally distributed data with known
standard deviation:

```
θ = [ mean(X) − z_C · sd(X)/√n ,  mean(X) + z_C · sd(X)/√n ]
```

z_C is "chosen such that [−z_C, z_C] is the C% confidence interval of the standard normal
distribution": 90% → 1.645; 95% → 1.96; 99% → 2.58; 99.5% → 2.807; 99.9% → 3.291.

**Errors and repeated experiments.** Type I error (false positive) = wrongly rejecting the null;
its probability for a single test is the significance level α. Type II error (false negative) =
wrongly accepting the null; its probability is "power" β, which "depends on the sample size and
the size of the effect". With α = 0.05 and *k* statistical tests, "the probability of having no
false positive is (1 − α)^k", e.g. "0.95¹⁰ ≈ 0.60 for k = 10" and "0.95²⁰ ≈ 0.36 for k = 20". This
is the **family-wise error rate (FWER)**. Bonferroni correction (Bonferroni-Dunn) "achieves this
for k experiments as follows": "Either by adjusting the significance level: α_FWER = α/k" or "by
adjusting the outcome of the test: p-value_FWER = p-value · k". "This correction can also be
applied to the calculation of confidence intervals."

**Paired data.** For paired data "we use paired difference tests". Paired t-test null hypothesis
as printed: "The means of two paired, normally distributed populations X₁ = x₁¹, …, xₙ¹¹ and X₂ =
x₁², …, xₙ²² are equal." A new population is the difference, `X_Δ = x₁¹ − x₁², …, xₙ¹¹ − xₙ²²`, and
then a one-sample t-test: `t = mean(X_Δ) / (sd(X_Δ)/√n)`. "This tests if the difference is
significantly different from zero."

**Between- and within-subjects designs.** Between-subjects: "every sample (i.e., our subjects) is
used only once"; "Independence makes design often simpler", "Subjects have single role, avoids
carry-over effects", but it "Requires good controls that the different groups of subjects are
sufficiently similar". Within-subjects: "every sample is used multiple times under different
conditions", it "naturally produce[s] paired data, i.e., pairing by subject", "Often more
efficient as fewer unique samples are required", "Enables direct comparison which can help to
avoid confounding effects", but "More considerations required when human subjects are used, as
there may be carry-over effects".

**Multiple variables.** Dependent variable `Y` ("Outcome of interest for the study");
independent variables `X₁, …, X_p` ("Variables that we expect that influence the dependent
variable"); confounding/control variables `Z₁, …, Z_q` ("Variables that we believe may be related
to both dependent and independent variables", used "to control that the relationship between
dependent/independent variables is really between these variables and not explained by the
confounding variable"). Linear model as printed:

```
Y = β₀ + Σ_{i=1..p} β_i·X_i + Σ_{j=1..q} γ_j·Z_j + ε
ε = Y − β₀ − Σ_{i=1..p} β_i·X_i − Σ_{j=1..q} γ_j·Z_j
```

The error term "models the residual error in the prediction" and is "often not written as part of
the model but rather computed after fitting". β₀ "can be interpreted as the value of the
dependent variable, if all independent and confounding variables are zero".

**Significance of coefficients — a two-stage procedure.** First the **omnibus test**
("is there any difference?"): "does the model explain the dependent variable or is the result not
much better than randomness?" H₀: "The coefficients of the independent and confounding variables
are equal to zero"; H₁: "At least one coefficient is not equal to zero"; evaluated "e.g., by using
an ANOVA test", which "further assumes the data for all variables is independent and normal".
Second, if H₀ is rejected, the **post-hoc test** ("what are the difference?"): "These are
multiple tests (one for each coefficient) and require correction", e.g. Tukey's HSD — "basically a
computation of confidence intervals that corrects for considering all pairs of variables";
"Coefficient is significant, if zero is not in the confidence interval".

**Generalized linear models.** Linear models "assume that the relationship between the variables
is linear, and that the response variable is continuous", and further "assume independence
between the variable". GLMs "introduce a link function g":

```
g(Y) = β₀ + Σ_{i=1..p} β_i·X_i + Σ_{j=1..q} γ_j·Z_j + ε
```

"The link function can be interpreted as a transformation of the dependent variable. One example
for a link function is the logistic function that is used for logistic regression. This allows the
use of linear models with binary response variables." "Other assumptions (linear relationship with
respect to link function, problems with correlations) stay the same."

**Non-linear models.** GAMs "can be seen as an extension of linear models in which we also apply
functions to the independent/confounding variables"; they "require a manual modeling of the
non-linearities" — "these must be known and are not 'learned'". Machine learning "allows the
discovery of complex relationships", interpretable (decision trees) or "black boxes (e.g., random
forests, neural networks)"; XAI techniques named are LIME and SHAP. "The main drawback of using
machine learning models is that it is in general not possible to know if relationships are
significant or rather random correlations found by the learning algorithm."

## Key Properties

- **Significance is probabilistic, not binary.** "Results are probabilistic, i.e., you can
  reject/fail to reject the null hypothesis with a certain probability, but you cannot make binary
  claims."
- **Significant ≠ important.** A dedicated slide says it, and effect size is the answer.
- **p-hacking is a real and often inadvertent practice.** "Re-running tests with different data
  until a desired result is found. Often inadvertent, e.g., due to subgroup analysis."
- **The test must match the data.** The Shapiro-Wilk gate is what makes Welch vs. Mann-Whitney a
  choice rather than a preference.
- **ANOVA is an omnibus test.** It says "at least one population is different", never which.
- **Multiple testing inflates the false-positive rate**, and the FWER formula quantifies it
  before the correction is applied.
- **The linear model is the multi-variable workhorse**, and the lecture flags that the
  gender/community-smell study in Chapter 5 was already an instance of it.
- **Machine learning cannot tell significance from coincidence.** That is the reason the
  Chapter 6 cost study is introduced as "an example for this approach".

## Worked Example

**Example for using statistics in MSR.** The RQ: "is there an impact of experience on the length
and complexity of solutions for a coding task". Two groups of developers: Group 1 = 20 developers
with at least 5 years of experience; Group 2 = 20 with at most 5 years. For both groups "the
lines of code (LOC) and the cyclomatic complexity (CC) of the solutions" are measured, so "we
have two populations with sample sizes n₁ = n₂ = 20". Two null hypotheses: "H0-LOC: The mean
values for LOC are the same for both groups"; "H1-CC: The mean values for CC are the same for both
groups" (printed as H1-CC; both are stated as null hypotheses in the text). Type I error rate
wanted: 5%. "Since we have two tests, we use α_FWER = 0.05/2 = 0.025". Then: run two suitable
statistical tests (e.g., t-test if data is normal) to get p-values and accept/reject based on
α_FWER; compute effect sizes for the mean differences if significant; compute confidence
intervals for all mean values "to report the uncertainty about this point estimate".

**The paired-data table.** The lecture's table has projects 1, n, n+1, 2n with "#Loc" values 30,
25, 32, 22 and a "Used" column (Yes/No). Design 1 (independent): projects split into those that
used code review and those that did not, "each project appears only once". Design 2 (paired): for
projects that introduced code review at some point, "we collect the number of bugs once before
code review was introduced and once afterwards", so "we have each project twice in our data". The
slides reshape the same table three ways — Project/Used/#Loc; Project/#Loc with "Used" and "Not
Used" as column headers (1: 30 / 32, n: 25 / 22); and Project/#Loc with "#Loc / Used" and "#Loc
|/ Used No" plus a Difference column (1: 30, 32 → 2; n: 25, 22 → −3). Annotations: the middle
table "Leads to two populations where the samples are unrelated with each other → Independent
data!"; the last "Leads to two populations where each sample has a counterpart in the other
population → Paired data".

**The confidence interval example** (repeated on two slides): twenty data sources; train on five
and test on the other fifteen; "the mean value of the 15 test values is 0.83, the standard
deviation is 0.13". Then: "How accurate is the estimated mean value?" Using
θ = mean ± z_C · sd/√n with n = 15: 90% → [0.775, 0.885]; 95% → [0.764, 0.896]; 99% → [0.743,
0.916]; 99.5% → [0.736, 0.924]; 99.9% → [0.720, 0.940].

**Interpretation of confidence intervals** is a separate slide because the standard misreadings
are common. Correct: "C% chance that results of future replications fall into θ"; "No statistical
difference from estimated parameter with C% confidence"; "There is a 1 − C% probability of the
observed data, if the true value for the estimate is outside of θ". Wrong: "The true value lies
with C% probability in θ"; "C% of the observed data is in θ".

## Common Pitfalls

- **Reading a p-value as the probability of the hypothesis.** "Given the hypothesis, how likely
  is the data? Not the same as given my data, how likely is the hypothesis!"
- **Using p-values as scores.** "Scoring makes no sense!" — p-values "describe the likelihood of
  the data, given the hypothesis"; "Never use p-values as scores!"
- **Saying "accept the null hypothesis".** The slides put it in the margin: "fail to reject"
  instead of "accept".
- **Reporting only significance.** "Significant ≠ important".
- **Ignoring the multiple-comparison problem.** Ten tests at α = 0.05 give a 0.60 chance of at
  least one false positive.
- **Applying a parametric test to non-normal data** without the Shapiro-Wilk gate, or an
  independent-samples test on paired data. For paired data the difference population is the
  point.
- **Treating ANOVA as a statement about which group differs.** It says "at least one" — and the
  lecture itself shows a post-hoc test applied for that.
- **Interpreting a confidence interval as containing the true value with probability C%.** Listed
  as a wrong interpretation on the slide.

## Connections

- [[statistical-significance]] — the Semester 1 treatment of significance testing.
- [[effect-sizes]] — the Semester 1 treatment of Cohen's d and its relatives.
- [[confidence-intervals]] — the Semester 1 treatment of interval estimation.
- [[null-and-alternative-hypothesis]] — H₀/H₁ formulation and the rejection rule.
- [[p-values]] — the p-value definition and its misuse.
- [[msr-sampling]] — representativeness decides which data inference may be extended to.
- [[msr-research-paradigms]] — why interpretivist work accepts bias rather than correcting it.
- [[threats-to-validity]] — where a statistically sound result still fails to generalise.
- [[mining-software-repositories-lecture-7]] — the source lecture for this page.

## Open Questions
- **The degree-of-freedom calculation for Welch's t-test is omitted by the slides themselves**
  ("Also requires calculation of the degrees of freedom, which we omit here"), so the material
  does not support computing the test end to end.

- **The example slide labels one of its two null hypotheses inconsistently.** The text reads "We
  define two suitable null hypothesis" and then lists "H0-LOC: The mean values for LOC are the
  same for both groups" and "H1-CC: The mean values for CC are the same for both groups" — both
  statements are null hypotheses in the wording, and the H1 label is presumably a slide typo.

- **The confidence interval example does not state n for the interval arithmetic.** The example
  gives the mean of the 15 test values and the standard deviation, and the intervals for n = 15,
  but the slides do not label the n used in the formula.

- **The lecture's own "Example for running tests" slide has no visible numbers.** It is
  presented as a worked example, but the extracted slide carries only the margin note "fail to
  reject instead of accept", so the specific test, data and outcome are not recoverable.

- **The Mann-Whitney-U null hypothesis is stated informally.** "The values from one population dominate the values from another independent population (more or less difference of means/medians)" is not the usual formulation, and no test statistic or p-value procedure is given.

- **Tukey's HSD is presented as a post-hoc test for coefficients**, but the slides do not connect it to the α/k adjustment discussed for repeated experiments.
