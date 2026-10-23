---
title: "Mining Software Repositories — Lecture 8 Overview (Validity of Results)"
tags: [topic, mining-software-repositories, semester-2, validity]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 8 turns "trust" into a structured assessment: five dimensions of validity, each with
named threat lists, and a reporting discipline that states the threat, judges its strength in
context, and either mitigates it or explains how the results would change.

## Core Map

```
Chapter 8 — Validity of Results
│
├── Aspects of validity
│   ├── Thought experiment: pattern matching vs if/else, and who you ask
│   ├── "A threat does not invalidate (or even falsify) results. It just makes them
│   │       less trustworthy."
│   └── Five dimensions (Cook et al.; Wohlin et al.) -> [[threats-to-validity]]
│
├── Construct validity
│   ├── Design threats: inadequate pre-operational explication, mono-operation bias,
│   │       mono-method bias, confounding construct, interaction of treatments,
│   │       interaction of testing and treatment, restricted generalizability
│   └── Social threats: hypothesis guessing, evaluation apprehension, expectancy
│
├── Internal validity
│   ├── Single-group: history, maturation, testing, instrumentation,
│   │       statistical regression, selection, mortality, ambiguity of causal direction
│   ├── Multiple-group: interaction with selection
│   └── Social: diffusion/imitation of treatment, compensatory rivalry, demoralization
│
├── External validity
│   └── Interaction of selection and treatment; setting and treatment; history
│
├── Conclusion validity
│   ├── Low statistical power, violated assumptions, fishing and error rate,
│   │       reliability of measures, reliability of treatment implementation
│   └── Random irrelevancies, random heterogeneity of subjects
│
├── Reliability
│   └── Insufficient collection details, unclear survey questions, unreliable judgements
│
└── Reporting threats to validity
    ├── Internal and external validity trade off under a fixed budget
    ├── Structure: repeat the method aspect -> state the impact -> state mitigation
    └── Threats vs limitations
```

## Key Concepts at a Glance
| Page | Core idea |
|------|-----------|
| [[threats-to-validity]] | Five dimensions, each with a named threat list, each threat making a result less trustworthy rather than wrong |
| [[msr-sampling]] | The selection threat and representativeness, the basis of the external-validity discussion |
| [[msr-statistical-methods]] | Power, assumption violations, and fishing — the conclusion-validity threats |
| [[grounded-theory]] | The qualitative side, where reliability rather than conclusion validity applies |
| [[qualitative-coding]] | Inter-rater agreement as the evidence behind a reliability claim |
| [[mining-software-repositories]] | The field whose methods this chapter judges |

## Lecture Structure
1. **Trustworthiness** — the pattern-matching versus if/else thought experiment and the four
   probing questions about subjects, snippets, complexity, and experience levels.
2. **Five dimensions** — construct, internal, external, conclusion (only with statistics), and
   reliability (only with qualitative methods), each with the lecture's own definition.
3. **Construct validity, design threats** — inadequate pre-operational explication of constructs
   ("A good process yields high-quality software"), mono-operation bias, mono-method bias,
   confounding construct, interaction of treatments, interaction of testing and treatment, and
   restricted generalizability across constructs.
4. **Construct validity, social threats** — hypothesis guessing, evaluation apprehension, and
   experimenter expectancy, each with its example.
5. **Internal validity, single-group threats** — history, maturation, testing, instrumentation,
   statistical regression, selection, mortality, and ambiguity about causal direction.
6. **Internal validity, multiple-group and social threats** — interaction with selection,
   diffusion or imitation of treatment, compensatory rivalry, resentful demoralization.
7. **External validity** — interaction of selection and treatment (open-source results against
   proprietary projects), of setting and treatment, and of history and treatment.
8. **Conclusion validity** — low statistical power, violated assumptions of tests, fishing and
   error rate, reliability of measures and of treatment implementation, random irrelevancies
   (April 2020 and Covid-19), and random heterogeneity of subjects.
9. **Reliability** — insufficient details about data collection, unclear survey questions, and
   unreliable judgements; low agreement does not mean invalid results.
10. **Reporting** — the trade-off between internal and external validity under a fixed budget;
    the three-step reporting structure (repeat the method aspect, state the impact, state the
    mitigation or expected change); and threats versus limitations.

## Exam-Relevant Points
1. **A threat does not invalidate results; it makes them less trustworthy.** This is the
   chapter's central sentence and the answer to the "no study is perfect" objection.
2. **Five dimensions, and two of them are conditional.** Conclusion validity applies only to
   statistical methods; reliability applies only to qualitative methods.
3. **Construct validity asks what you measure; internal validity asks how you interpret it.**
   The slides note the boundary is often difficult and offer the rule of thumb.
4. **The threat lists are named and enumerable.** A study selects from the list and judges
   relevance instead of inventing threats.
5. **Threat strength must be judged in the context of the results.** A large effect on a small
   sample is a threat to the effect's strength; a small effect on a small sample is a threat to
   the effect's existence.
6. **Fishing is the conclusion-validity counterpart of p-hacking**, and the complexity example
   with twenty related measures shows the mechanism.
7. **Reporting has a fixed structure**: threat, impact, mitigation or expected change, and if
   mitigation was impossible, why.
8. **Threats and limitations are different.** Limitations are about what was not considered, and
   nothing out of scope of the study can be a threat to its validity.
9. **External validity reporting is usually conservative**, restricted to the immediate
   population of the sampling frame, because broader generalization is what reviewers attack.

## Connections
- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-7]] — the methods chapter this chapter assesses.
- [[mining-software-repositories-lecture-6]] — studies whose size proxy carries a threat.
- [[mining-software-repositories-lecture-3]] — the noise in heuristic data, a threat.
- [[mining-software-repositories-lecture-2]] — sampling and instrument choices named as threats.
- [[threats-to-validity]] — the full threat catalogue.
- [[msr-sampling]] — representativeness and the selection threat.
- [[msr-statistical-methods]] — power, assumptions, effect size reporting.
- [[grounded-theory]] — the qualitative studies for which reliability applies.
- [[qualitative-coding]] — inter-rater agreement behind reliability claims.
- [[msr-data-noise]] — noise estimates feeding the threat analysis.

## Open Questions
- **No worked example of a full validity assessment for one MSR study is given**; the reporting
  examples are quotations from published papers rather than an end-to-end walk-through.
- **How to decide that a threat is "relevant" is stated but not operationalized** — the slides
  say "not everything is relevant for every study" without a procedure.
- **The boundary between construct and internal validity is admitted to be difficult**, and only
  a rule of thumb is offered.
- **The relation between this chapter's reliability dimension and the multi-rater agreement
  material in the enrichment chapter is not stated explicitly**.
- **Whether validity must be reported for all five dimensions, or only those with a credible
  threat, is left open**.
