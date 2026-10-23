---
title: "Mining Software Repositories — Lecture 3 Overview (Enriching Raw Data)"
tags: [topic, mining-software-repositories, semester-2, data-enrichment]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
Chapter 3 covers the step between raw collection and analysis: operationalizing raw events into
metrics, linking artefacts across repositories, collecting defect data with SZZ, measuring how
much noise the heuristics introduce, and controlling human bias with coding and inter-rater
agreement.

## Core Map

```
Chapter 3 — Enriching Raw Data
│
├── Reasons for enrichment
│   ├── Raw data: no linking, no indirect info, no tagging
│   ├── Often infeasible during collection -> "only possible after collection"
│   └── Enrichment fits no single category of a data-science workflow
│
├── Measurements and software metrics
│   ├── Three definitions (Fenton & Pfleeger; Craner & Bond; Hubbard)
│   ├── DeMarco: "You cannot control what you cannot measure."
│   ├── Measure m: O -> V, NOIR scales, operationalization
│   ├── Direct vs indirect measures (proxies) and their correlation requirement
│   └── Metrics = operationalization; internal/external x product/process
│           -> [[software-metrics]]
│
├── Links between repositories
│   ├── Explicit metadata links
│   ├── Textual links to identifiers (regular expressions; JIRA, Bugzilla, GitHub)
│   └── Risks of missing/additional links; noise must be estimated
│           -> [[repository-link-enrichment]]
│
├── Collecting defect data
│   ├── Error -> fault/bug -> failure -> defect vocabulary
│   ├── Keyword labelling: recall/precision trade-off
│   ├── Link-based labelling: depends on project practice
│   ├── Blame-based approach and its assumptions
│   └── SZZ: two phases, candidates/suspects/hard suspects -> [[szz-algorithm]]
│
├── Noise in heuristic MSR data
│   ├── SZZ link noise, 42% mislabelled issue types, tangled changes
│   ├── Noise in bug-introducing-change detection (~70% correct last change)
│   └── Five responses: ignore, account in collection, account in analysis,
│           manual cleaning, improve heuristics -> [[msr-data-noise]]
│
└── Coding of data
    ├── Raters, codebooks, deductive vs inductive coding
    ├── Multiple-rater strategies and inter-rater agreement
    ├── Cohen's kappa, Fleiss' kappa, Krippendorff's alpha, Cronbach's alpha
    └── Harmonizing codes; axial coding -> [[grounded-theory]]
              [[qualitative-coding]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[software-metrics]] | A metric is the operationalization of a measure; the grid splits product/process against internal/external |
| [[repository-link-enrichment]] | Explicit, textual, and implicit links between repositories, and the noise each introduces |
| [[szz-algorithm]] | Two phases: find bug fixes by issue linking, then blame each changed line to a candidate introduction |
| [[msr-data-noise]] | Noise is measurable and has a direction; five responses exist, none free |
| [[qualitative-coding]] | Human labelling with codebooks, raters, agreement statistics, code harmonization |
| [[grounded-theory]] | Open, axial, and selective coding as the machinery behind theory building |

## Lecture Structure

1. **Why enrichment exists** — raw data is collected per source with no linking, no derived
   information, and no tagging; linking needs full data, so it is only possible after collection,
   and it fits no single category of a standard data-science workflow.
2. **Measurement** — three competing definitions, the DeMarco framing, ISO terminology including
   the NOIR scales, operationalization, and direct versus indirect measures, where a proxy must
   correlate with the attribute of interest.
3. **Quality of measures and metrics** — plausibility/validity, relevance, cost efficiency,
   analyzability, availability, resolution, reproducibility; then the ISO metric definitions, the
   four-cell grid, and worked examples: SLOC and cyclomatic complexity for internal product
   metrics; MTRR and defect density for external; development velocity for internal process.
4. **Links between repositories** — explicit metadata, textual identifiers with concrete regular
   expressions, hyperlinks, and implicit inference through time, people, and text similarity
   (ReLink); then the risks and the case for manual validation.
5. **Defect data** — the error/fault/failure/defect vocabulary; four kinds of defect information;
   keyword labelling and its false positives; link-based labelling and its dependence on project
   practice; the blame-based approach; SZZ's two phases and three suspect classes.
6. **Noise** — the measured figures (one in five bug-fixing commits missed by SZZ, about half of
   identified commits not actually bug fixing, 42 % median mislabelling of issue types, roughly
   70 % correct last-change attribution) and two root causes: simplified assumptions and
   misaligned interests.
7. **Coding of data** — deductive versus inductive coding, four multi-rater strategies, Cohen's
   kappa with the Landis and Koch table, the generalizations beyond it, harmonizing open codes,
   and axial coding.

## Exam-Relevant Points

1. **Enrichment is by definition post-collection.** Linking, metrics, tagging, and annotation all
   need data from one or more complete sources.
2. **The measurement definitions share one thing: a rule in advance.** A number without a rule is
   not a measurement.
3. **The proxy requirement.** An indirect measure is acceptable only if it correlates with the
   attribute of interest; complexity correlates with size on a large scale, so size is often a
   poor proxy.
4. **The metric grid is orthogonal.** Product and process combine with internal and external, and
   MSR can supply data for all four.
5. **Link detection is fault-prone by nature**, so measure its error rate and validate manually
   where the study depends on accuracy.
6. **SZZ rests on assumptions that often do not hold** — numbers in commit messages are usually
   issue references, developers label issues correctly, every line touched in a fix is related
   to the bug, and the last change to a line caused it.
7. **Noise has a direction.** Randomly distributed noise is easier to handle than noise with many
   false positives and few false negatives, which biases results.
8. **Training on noisy data and evaluating on noisy data differ.** Evaluation on noise leads to
   overfitting on noise and wrong performance estimates.

## Connections

- [[mining-software-repositories]] — the course page.
- [[mining-software-repositories-lecture-2]] — the raw data this chapter enriches.
- [[mining-software-repositories-lecture-6]] — defect prediction, which consumes the defect data.
- [[mining-software-repositories-lecture-7]] — the statistics and grounded theory the coding
  material feeds.
- [[mining-software-repositories-lecture-8]] — validity, where noise becomes a threat.
- [[software-metrics]] — the measurement vocabulary in detail.
- [[repository-link-enrichment]] — the linking task and its heuristics.
- [[szz-algorithm]] — the algorithm whose noise the chapter quantifies.

## Open Questions

- **The noise figures come from different studies with different bases** (18,721 validated links,
  11,295 linked issues, 289,904 lines); comparability is not addressed.
- **The quality attributes of measures are listed without any weighting or trade-off.**
- **"Median of 42 % mislabeled as bug"** comes without naming the projects or the judging
  procedure behind the ground truth.
- **No noise-handling strategy is recommended for a specific research question**; the five
  options come without a decision procedure.
- Whether the Cohen's kappa table (Landis and Koch) is endorsed or only reported is unclear.
