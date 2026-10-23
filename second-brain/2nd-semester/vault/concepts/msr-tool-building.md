---
title: "MSR Tool Building"
tags: [concept, mining-software-repositories, semester-2, tools]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Building an MSR tool is a four-step procedure — fix the goal, fix the data, build, then run an
experiment — and the evidence you end up with is usually a proxy rather than a business or user
metric.

## Core Intuition

The lecture's "Building tools" section starts where every tool-based discipline starts: software
development already runs on tools. "We use tools to aid all aspects of software engineering":
IDEs for writing code, testing tools and code review tools for quality assurance, issue trackers
for requirements and change management. MSR's contribution is to improve those tools from the
outside, using the record they collectively leave behind.

The five improvement targets the slides list are all *decision-support* features rather than
automation of existing work:

- "Rank static analysis warnings based on past fixes of warnings"
- "Provide a risk analysis based on past bugs to guide quality assurance efforts"
- "Identify which developers are well-suited to work on an issue based on past contributions"
- "Identify potential reviewers for pull requests"
- "Aid issue triage by automatically determining the affected components and/or issue type"

Each one converts repository history into a recommendation for a human who is about to act. That
is the shape of the whole discipline: the tool does not do the engineering, it informs the
engineering.

The second core intuition is that a tool is not finished when it runs. The slide "Usual MSR tool
building approach" ends with "Collect more data and conduct an experiment → MSR tool building is
usually combined with evidence regarding how the tools work!". The fourth step is what
distinguishes an MSR tool from a script, and it is where the validity problems live.

## Formal Definition / Statement

The approach, verbatim from the slide:

1. **Identify a goal for the tool**
   - Which part of software development do you want to help?
   - How do you think your tool will be used?
2. **Identify which data you need**
   - Can the data be automatically obtained? How? From where?
   - Does the data need to be updated frequently to avoid concept drift?
   - Do you require regular manual interventions (e.g., in form of labeling) to collect data?
   - How noisy is the data? Will it be good enough?
3. **Collect data and build tool**
4. **Collect more data and conduct an experiment**

The annotation to step 4 is the honest one: "… but the evidence if often not a business metric
(ROI) or even user metric (usability, time saved) but a proxy (e.g., accuracy)".

For machine-learning-based tools the slide gives the pipeline: "Collect data from some
repositories — Build machine learning model — Evaluate model on other repositories — Determine
if/how this would help developers".

## Key Properties

**The tool list is a catalogue of inference problems, not of features.** Every entry requires
linking repository artefacts that are not explicitly linked — past fixes of a warning, past bugs
for a risk analysis, past contributions to suggest an assignee, a pull request to suggest
reviewers, an issue to determine its component and type. All of these are enrichment tasks, so
all of them inherit the error rates of the linking heuristics.

**Goal-first, data-second is a reversal of the usual instinct.** The second step's four
questions are exactly the failure modes the later chapters measure. "How noisy is the data? Will
it be good enough?" is the slide asking the noise question before the tool exists, not after.
"Does the data need to be updated frequently to avoid concept drift?" flags the maintenance
burden of a tool whose data ages. "Do you require regular manual interventions (e.g., in form of
labeling)?" flags the hidden human cost inside an "automatic" tool.

**Not every MSR tool uses machine learning.** The slide lists three non-ML categories: tools that
"Visualize information from repositories — For example, to show how parts of the software interact
with each other or how large the software is"; tools that "Aggregate information from different
repositories into a single repository — For example, as overlay to understand how many open issues
there are when multiple issue trackers are used"; and tools performing "Analysis of repository
contents with standard software engineering techniques, e.g., to detect clones or potential flaws
on a large scale".

**The evaluation step has two halves that are easy to confuse.** "Evaluate model on other
repositories" is a generalization check; "Determine if/how this would help developers" is a
utility check. The slide puts them in sequence, and the caveat about proxy evidence applies to
the second one specifically: accuracy is measurable, time saved is not.

**The examples span three different genres.** **Code City** — Wettel, Lanza & Robbes, "Software
systems as cities: A controlled experiment", ICSE 2011, pp. 551-560 — visualizes "the source code
size, complexity, and package structure". **Tesseract** — Sarma, Maccherone, Wagstrom & Herbsleb,
ICSE 2009, pp. 23-33, "Interactive visual exploration of socio-technical relationships in software
development" — analyzes "who works together on what". **Nudge** — Maddila, Upadrasta, Bansal,
Nagappan, Gousios & van Deursen, "Nudge: Accelerating Overdue Pull Requests Towards Completion",
ACM TOSEM, 2022 — aids "developers to complete tasks".

**MSR output can be a product.** The slide "MSR as a Product" states: "There are companies that
specialize in the analysis of code repositories" (Teamscale), and "Others were acquired and
integrated into larger products". Such tools "combine analysis with integration into a
repository/company ecosystem". The strategic implication is that a tool can have market value
independent of the research that produced it.

## Worked Example

Follow the four steps through the first example, ranking static analysis warnings.

*Goal.* Which part of software development? Quality assurance — the developer faces a list of
static analysis warnings and must decide which to fix first. How will it be used? Interactively
or in a CI report, ranking warnings by past evidence.

*Data.* The history of warnings and the commits that fixed them. Can it be obtained
automatically? Partly — static analysis tools produce warnings, and the VCS records the fixes;
but linking the two requires enrichment, and the answer to "how noisy is the data" depends
entirely on that linking quality. Does it need frequent updates? Yes: warnings change as the
codebase changes, which is the concept-drift concern the slide names. Does it require manual
interventions? Possibly, to validate which fixes actually addressed which warning.

*Build and evaluate.* Train on some repositories, evaluate on others, then answer "Determine
if/how this would help developers". The slide's footnote is where this example lands: the
evidence will be a proxy such as accuracy — the ranking is measurably correct — and not the
business metric (ROI) or the user metric (usability, time saved) that would settle whether the
tool is worth adopting.

## Common Pitfalls

- **Skipping step four.** A tool with no experiment produces a mechanism, not a finding.
- **Reporting the proxy as the goal.** Accuracy is not developer productivity; the lecture flags
  this asymmetry explicitly.
- **Treating "collect more data" as "collect more of the same data."** The fourth step's data is
  for evaluation, and the two sets have different quality requirements.
- **Ignoring concept drift.** A tool trained on yesterday's data may be answering a question
  about a codebase that no longer exists.
- **Hiding the manual labelling cost.** "Do you require regular manual interventions" is a
  question about the tool's operating cost, and tools that need continuous human labelling
  cannot be described as automatic.
- **Assuming machine learning is required.** Visualization, cross-repository aggregation and
  scaled standard SE techniques are legitimate MSR tools.
- **Underestimating the noise question.** "How noisy is the data? Will it be good enough?" is
  asked before building; answering it after building means the tool may already be unsound.
- **Confusing a research system with a product.** Tesseract is a research system, Teamscale is a
  product, and "others were acquired and integrated into larger products" — the slide
  distinguishes them deliberately.

## Connections

- [[msr-tool-building]] — this page; the four-step approach and the proxy-evidence caveat.
- [[mining-software-repositories]] — the pipeline whose final cell the tool occupies.
- [[repository-link-enrichment]] — the linking work every improvement target above depends on.
- [[msr-data-noise]] — the measured error rates behind the "how noisy is the data?" question.
- [[defect-prediction]] — the model class behind the risk-analysis and warning-ranking targets.
- [[software-metrics]] — the measurement layer behind accuracy-style proxies.
- [[defect-prediction-cost-model]] — the bridge from accuracy to the cost of acting on a warning.
- [[developer-social-networks]] — the machinery behind "identify potential reviewers" and behind
  Tesseract.
- [[threats-to-validity]] — where a tool's evaluation can go wrong.
- [[msr-statistical-methods]] — the tests the experiment step usually needs.

## Open Questions

- **No criterion is given for how good is good enough.** The slide asks "How noisy is the data?
  Will it be good enough?" but the lecture never supplies a threshold, and the noise chapter
  that follows supplies error rates without a decision rule.
- **The proxy gap is named but no bridging method is offered.** "the evidence if often not a
  business metric (ROI) or even user metric (usability, time saved) but a proxy (e.g.,
  accuracy)" — the deck states the problem and stops.
- **The four-step approach does not say where the goal comes from.** "Which part of software
  development do you want to help?" presupposes a development problem that someone else has
  identified, and the lecture does not discuss how such problems are found.
- **The relationship between a research tool and a product is asserted, not analysed.** "Others
  were acquired and integrated into larger products" records an outcome; it does not say what
  changes about the tool, its data, or its validation when it becomes a product.
