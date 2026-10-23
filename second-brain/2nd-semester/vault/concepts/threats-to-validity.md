---
title: "Threats to Validity in MSR"
tags: [concept, mining-software-repositories, semester-2, validity]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Validity is not a feeling but a structured assessment: five dimensions of threats, each with a
named list, each of which makes a result less trustworthy rather than wrong.

## Core Intuition

The lecture opens with a thought experiment: imagine studying the claim "that code based on
pattern matching is easier to read and leads to less bugs than code using traditional if/else
or switch statements". Would you trust results based on "asking two developers? 20? 100?"; on
"showing two code snippet? 20? 100?"; on "the complexity of the examples?"; on "asking first
year students, senior students, junior developers, or senior developers?"

"In science, trust is not based on a feeling, but rather on the validity of results. Consequently,
we need to understand how our methods and data affect the validity of our results with respect
to our research question."

The framing sentence of the chapter: **"Note that a threat does not invalidate (or even falsify)
results. It makes them less trustworthy."** Threats are a graded, reportable property of a
study, not a verdict. The structure comes from Cook et al. and was popularised in software
engineering by Wohlin et al.: "Here, we consider validity in five dimensions".

## Formal Definition / Statement

**The five dimensions**, with the lecture's own definitions:

| Dimension | Definition as printed |
|---|---|
| Construct validity | "to consider if what the study measures or analyzes is representative for the concepts that are studied" |
| Internal validity | "to consider if what we observe is supports causal claims, i.e., that we observe is really causally related to the effects we want to study" |
| External validity | "to consider how the results are generalizable beyond the scope of the study" |
| (Statistical) Conclusion validity | "to consider if the statistical methods used likely yield valid results" — "Only used in case research methods use statistics" |
| Reliability | "to consider if there may be biases introduced by the researchers and if different researchers would reach the same conclusions" — "Only used in case of qualitative research methods" |

Each dimension has its own threat list. Every threat the lecture names is listed below, with the
lecture's example.

**Construct validity — design threats.** "Design threats consider how the study design/methods
affect the validity of the construct."

| Threat | The problem | Example |
|---|---|---|
| Inadequate pre-operational explication of constructs | the concept "is not sufficiently clear, which means that we cannot really know if we measure what we want to" | 'A good process yields high-quality software' |
| Mono-operation bias | a single independent variable, case or subject, so "we do not get the full picture" | one project |
| Mono-method bias | "A single perspective on a concept … has the risk of missing other important aspects" | issue tracker only |
| Confounding construct | "Factors that could also explain observed effects are not considered" | prior programming skills |
| Interaction of different treatments | multiple treatments at the same time "may interact" | — |
| Interaction of testing and treatment | "The study itself may affect the outcomes" | developers know they are studied |
| Restricted generalizability across constructs | side-effects to related constructs "may hinder generalization of positive effects" | AI coding affects feature speed, controlled for maintainability |

**Construct validity — social threats.** "Social threats are issues that may occur even if the
design is valid."

| Threat | The problem | Example |
|---|---|---|
| Hypothesis guessing | participants "might guess what a study is about and alter their behavior to affect the results" | — |
| Evaluation apprehension | humans "may be afraid to be evaluated and behave differently" | raters overly critical for fear of looking bad |
| Experimenter expectancy | researchers "might also consciously or unconsciously bias results based on their expectations" | — |

**Internal validity — single group threats.** "Such threats apply if we do not have a control
group." (The treatment group is where the phenomenon takes place; the control group is "a second
group of data, where this does not happen" — e.g. projects using code review versus projects
without.)

| Threat | The problem | Example |
|---|---|---|
| History | multiple treatments over time, so "when this takes place might affect the results" | one-week intervals before vs. after holidays |
| Maturation | "Treatments may have a different effect over time" | — |
| Testing | "Data might change if the test subjects know that a test is occurring, especially if this is repeated" | developers raise cyclomatic complexity when the metric judges their difficulty |
| Instrumentation | modifying the measurement object "might have an effect" | a CI system updated more often than usual, or with more bugs |
| Statistical regression | selecting data by prior results "could affect what is possible to observe" | top-10 performers unlikely to improve, bottom-10 unlikely to get worse |
| Selection | "How samples are selected may affect how representative they are" | — |
| Mortality | "Study subjects might drop out during a study making the final sample less representative" | project activity decreases or stops |
| Ambiguity about direction of causal influence | "Whenever we study correlations we need to ensure direction of causality" | complex code and defects both caused by problem complexity |

**Internal validity — multiple group threats.** "Control groups are often used within study
designs to study to mitigate internal threats. However, using multiple groups (e.g., control
group, treatment group, different treatments) can also lead to validity problems."

| Threat | The problem | Example |
|---|---|---|
| Interaction with selection | "Any of the above threats might interact with the group selection" | a control group without code review matures faster, giving a decreasing defect rate |

**Internal validity — social threats.**

| Threat | The problem | Example |
|---|---|---|
| Diffusion or imitation of treatment | one group "might learn about a treatment of another group and try to imitate this because they suppose there is a positive effect" | a project without static-analysis reporting starts using it locally |
| Compensatory rivalry | "A group that gets a less desirable treatment might be motivated by this and affect the outcome" | the non-AI group tries to outperform AI-supported development |
| Resentful demoralization | "Opposite of compensatory rivalry" | — |

**External validity — threats.** "Threats to external validity consider if we can apply our
results in contexts different from the study and thus consider how the context can vary."

| Threat | The problem | Example |
|---|---|---|
| Interaction of selection and treatment | "the selected sample is not representative for the population we want to generalize to" | open-source MSR studies vs. proprietary, closed-source, industrial projects |
| Interaction of setting and treatment | the setting "may have an impact on the observed effects" | modern inner-source tooling vs. dated tooling with more friction |
| Interaction of history and treatment | "the timing of the experiment might affect the general representativeness, similar to the internal threat 'history'" | measuring activity in August for regions in their summer holiday season |

**Conclusion validity — threats.** "Threats to the conclusion validity arise from the
probabilistic nature of statistics. Thus, they consider aspects that lead increase or lead to a
high probability of (meaningful) errors in the results."

| Threat | The problem | Example |
|---|---|---|
| Low statistical power | "the likelihood of accepting the null hypothesis is high" | sample size or effect size too small |
| Violated assumptions of statistical tests | "Assumptions on the distribution of data are not completely fulfilled" | data looks almost normal, so a Cohen's d is used for its high interpretability |
| Fishing and error rate | "we continue to look at different aspects, until we find a result that supports our hypothesis", often "an inadvertently increased error rate due to repeated tests" | twenty related complexity measures for complexity vs. post-release defects |
| Reliability of measures | "measurements that have a high uncertainty … affects downstream statistical results" | an unstable Likert scale for judging readability of mined code |
| Reliability of treatment implementation | a treatment "that does not always yield the same outcome" | AI support used to generate database queries or implement requirements |
| Random irrelevancies in the experimental setting | "Results can be affected by external effects that randomly occur" | any MSR measurement in April 2020 has an effect due to Covid-19 |
| Random heterogeneity of subjects | "unlucky with our sampling due to the natural heterogeneity within groups" | 20 random students unrepresentative of a diverse population |

**Reliability — threats.** "Threats to the reliability are the result of methods that rely on the
expertise of researchers, but do not have safeguards or checks to prevent biases from these
researchers to affect the data."

| Threat | The problem | Example |
|---|---|---|
| Insufficient details about data collection | "Details about the data collection are missing such that a replication might collect different data leading to a different sample strategy" | open coding of code comment types not describing how codes are harmonized between raters |
| Unclear survey questions | questions "are not clearly worded and require interpretation by the researcher leading to different formulations" | 'How would you judge complexity?' at file, class, or function/method level |
| Unreliable judgements | "Raters might have biases or judgements may be difficult" | one researcher labelling affected components (UI, database, networking) is likely to mislabel some |

**Reporting threats to validity — the procedure.** For construct validity:

1. "First repeat the aspect of the method that leads to a threat."
2. "Then state what the impact of the threat could be."
3. "Then state if there are any mitigating aspects in your method or how you took this into
   account when interpreting data." If there are none, "you need to instead state how you would
   expect results to possibly change. You can possibly also state why a mitigation was not
   possible or not used. E.g., due to effort or because this would lead to other problems".

**Threats to validity vs. limitations.** Limitations "are rather regarding things that are
important but not yet considered — could be other populations, could be other perspectives on the
problem, could be other, related research questions or other aspects of a theory that were not yet
studied sufficiently." Threats "are only for the scope of the current study and do not go beyond
this scope. Notably, nothing that is out of scope of the study (e.g., other research questions)
can be a threat to the validity. However, there is certainly an overlap. E.g., other populations
that need to be studied are directly related to the external validity".

## Key Properties

- **A threat reduces trustworthiness; it does not falsify.**
- **The five dimensions divide by method.** Conclusion validity applies to statistical studies;
  reliability applies to qualitative ones.
- **Validity is relative to the research question.**
- **Design threats concern the study's own construction; social threats concern human behaviour.**
- **Validity dimensions trade off under a fixed budget.** "you can increase internal validity by
  looking at more possible confounding factors … However, given a fixed budget this effort is at
  the cost of external validity as fewer data points can be considered".
- **No study is perfect; the deliverable is openness.** "Studies can and should be open about
  threats to validity … not everything is relevant for every study."
- **Threat strength must be judged in context.** "if you have a large effect size on a small
  sample, it is likely that there is an effect with a larger sample … the threat is rather towards
  the strength of the effect, not the effect itself. However, if you have a small effect size and
  a small sample, the threat is directly to the effect which may be a false positive."
- **Construct and internal validity are often hard to separate.** "it is rather regarding what you
  measure, it is construct validity. If it is rather how you interpret your findings, it is
  internal validity."
- **External validity is reported conservatively.** "Reporting of external validity is almost
  always done with respect to the sample … restricts the scope of where findings can be applied to
  the immediate population of the sampling frame."

## Worked Example

**The reporting example (construct validity)**, from the Herbold, Trautsch & Ledel et al. paper
quoted on the slide (*Empirical Software Engineering* 27, 125 (2022),
https://doi.org/10.1007/s10664-021-10083-5), following the threat → impact → mitigation
structure:

- Threat: the authors "differentiate not only between bug fixing lines and other lines, but use a
  more detailed differentiation of changes into whitespaces only, documentation changes, test
  changes, refactorings, and unrelated improvements."
- Impact: "This could have influenced our results. Most notably, this could have inflated the
  number of lines without consensus."
- Mitigation: "We counter this threat by differentiating between lines without consensus with at
  least one bug fix label, and other lines without consensus."

**The reporting example (internal validity)**, same paper, with the structure "Threat (red),
mitigation or analysis of threat (green)": "Our decision to label data on a line level and not
the character or statement level may affect the validity of our conclusions … such changes are
very rare … our participants reported that this happened only rarely. Thus, any noise we missed
this way is likely to have only a negligible effect on our results." The slide's note:
"Differentiation between construct and internal validity often difficult".

**The reporting example (external validity)**, same paper: results "may not generalize to other
languages or software with less mature development processes than those of the Apache projects";
the sample "may not be representative for mature Java projects as well, as we did not conduct
random sampling, but re-used data from Herbold et al. (2019) who used a purposive sampling
approach (Patton 2014)"; but "Baltes and Ralph (2020) argue that well-done purposive sampling
should also yield generalizable results"; and results "may not generalize to closed-source
software", though "there are many industrial contributors in the projects we studied".

**The reporting example (conclusion validity)**: the ideal is "There are no threats to the
conclusion validity of our study. All statistical tests are suitable for our data, we correct our
results to err on the side of caution, and the pre-registration ensured that we did not tailor our
statistical analysis in a way to artificially find coincidental results, e.g., through subgroup
analysis." The imperfect version: "We report the effect size using Cohen's d. While our data is
not perfectly normal, it also does not have severe outliers, so we prefer the clear interpretation
of Cohen's d over the slightly more appropriate, but less accessible non-parametric effect size
measures." (Second citation on that slide: Herbold, Hautli-Janisz, Heuer et al., "A large-scale
comparison of human-written versus ChatGPT-generated essays", *Sci Rep* 13, 18617 (2023).)

**The reporting example (reliability)** cites Schulte, Ledel & Herbold, "Studying the explanations
for the automated prediction of bug and non-bug issues using LIME and SHAP", *Empirical Software
Engineering* 29, 93 (2024), https://doi.org/10.1007/s10664-024-10469-1: "We cannot rule out that
the results of our study are due to the participants we recruited as fellow researchers. However,
our participants are very diverse: they are working on all continents except Africa and
Antarctica, the experience ranges from graduate students to full professors … the overall
consensus ratios are relatively high for all participants and Fleiss' κ indicates substantial
agreement among our participants."

## Common Pitfalls

- **Reading a threat as a refutation.** "a threat does not invalidate (or even falsify) results".
- **Reporting every threat in every list.** "not everything is relevant for every study".
- **Failing to state the impact.** The procedure is threat → impact → mitigation; a bare list of
  threat names is not a report.
- **Confusing limitations with threats.** Limitations are about what was not studied; threats are
  about the current study's scope only.
- **Confusing construct with internal validity.** What you measure vs. how you interpret.
- **Ignoring social threats because the design is sound.** "Social threats are issues that may
  occur even if the design is valid."

## Connections

- [[mining-software-repositories]] — the pipeline whose results must survive this checklist.
- [[msr-sampling]] — the "selection" internal threat and the main external-validity threat.
- [[msr-statistical-methods]] — power, test assumptions and the effects that conclusion validity
  checks.
- [[grounded-theory]] — the qualitative method for which reliability is the relevant dimension.
- [[qualitative-coding]] — rater reliability, which is what the reliability threats measure.
- [[msr-research-paradigms]] — why some threats are irrelevant under a given paradigm.
- [[defect-prediction]] — an observational MSR setting where selection and maturation bite.
- [[developer-social-networks]] — social threats (imitation, evaluation apprehension) in
  practice.
- [[mining-software-repositories-lecture-8]] — the source lecture for this page.

## Open Questions
- **The threat lists are inherited from a general experimental-methods tradition, not tailored to
  MSR.** No MSR-specific threat (e.g. enrichment error, link heuristic error) appears in any of
  the five categories, although earlier lectures contain documented MSR-specific noise sources.

- **The distinction between the "testing" and "interaction of testing and treatment" threats is
  not made crisp.** Both are listed — the former under internal validity, the latter under
  construct validity — and the internal-validity one is annotated "(note: related to social
  biases)", but the slides do not say which applies when.

- **No severity scale or threshold is provided.** The lecture says to "judge how strong the threat
  is", but offers no categories, no decision rule, and no template for expressing severity.

- **The "no threats" example relies on pre-registration**, which is mentioned once, in a quoted
  example, and never discussed as a practice in the lecture itself.

- **Reliability is scoped to qualitative methods**, but the sampling and coding lectures produce reliability concerns for quantitative work too; the slides do not say where such concerns should be reported.

- **The external-validity discussion is almost entirely about the sample**, and the slide admits this ("Reporting of external validity is almost always done with respect to the sample"). The reporting guidance for the setting and history threats is not given.

- **The trade-off between validity dimensions is asserted but not bounded.** The lecture says internal validity can be increased by looking at more confounding factors, "given a fixed budget this effort is at the cost of external validity as fewer data points can be considered", but never says when a study should sacrifice which dimension.
