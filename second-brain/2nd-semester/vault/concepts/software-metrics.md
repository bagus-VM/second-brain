---
title: "Software Metrics"
tags: [concept, mining-software-repositories, semester-2, measurement]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

A software metric is the operationalization of a measurement: a rule-derived number that
represents an attribute of a product or a process, and the classification grid says whether
that attribute is internal or external.

## Core Intuition

The chapter's second block is titled "Measurements and Software Metrics" and opens with the
reason enrichment exists at all. Raw data is "collected individually for each data source", with
"No linking between sources", "No calculation of indirect information" and "No tagging".
Enrichment adds those things, and it "Does not fit into any specific category within a normal
data science workflow (e.g., pre-processing, data collection, feature engineering)".

Measurement is the bridge from raw events to claims, and the slide's framing sentence, attributed
to DeMarco, is the shortest statement of the whole idea: "You cannot control what you cannot
measure."

The lecture's conceptual move is to insist that measurement is a *rule-governed* activity, not a
number-producing one. Three competing definitions are put on the slide:

- Fenton & Pfleeger: "Measurement is the process by which numbers or symbols are assigned to
  attributes of entities […] in such a way as to describe them accordingly" — to rules that are
  defined in advance.
- Craner & Bond: "Measurement is the empirical, objective assignment of numbers, according to a
  derived rule from a model or theory, to attributes of objects or events".
- Hubbard: "A quantitatively expressed reduction of uncertainty based on one or more
  observations."

The common core is the rule: a number without a rule is not a measurement.

## Formal Definition / Statement

**Measurement terminology (ISO/IEC/IEEE 24765:2017).** Quantification is "turning observations
into numbers". A measure refers to "a method or standard format for measuring something" and is
"a variable to which a value is assigned as the result of measurement". Formally, a measure *m* is
a map *m: O → V* from the object space *O* of the measured objects into a space of measurement
values *V*. *V* may use the NOIR scales: Nominal — categories without order; Ordinal — categories
with order; Interval — numeric scale where differences are well defined but ratios are not
reasonable (e.g., dates); Ratio — numeric scales in which ratios are also well defined.

**Operationalization** is "identifying and implementing a method to measure factors".

**Metrics (ISO/IEC/IEEE 24765:2017).** A metric is a "Quantitative measure of the degree to
which a system, component, or process possesses a given attribute", with a "Defined measurement
method and the measurement scale". A software quality metric is a "function whose inputs are
software data and whose output is a single numerical value that can be interpreted as the degree
to which software possesses a given attribute that affects its quality". The lecture's summary
line: "Metrics are the operationalization of measures!"

**The classification grid.** Metric types and attribute are orthogonal and can be combined:

- *Product metric* — "metric used to measure the characteristics of any intermediate or final
  product of the software development process". *Process metric* — "metric used to measure
  characteristics of the methods, techniques, and tools employed in developing, implementing,
  and maintaining the software system".
- *Internal attribute* — "measurable property of an entity which can be derived purely in terms
  of the entity itself". *External attribute* — "measurable property of an entity which can only
  be derived with respect to how it relates to its environment".

The slide notes "There are also other classifications in the literature that, e.g., consider
resources as well", but the standards' two types are used here.

## Key Properties

**Direct vs indirect measures.** Direct measures "directly quantify the attributes of interest";
examples are costs, time, size. Indirect measures ("also called pseudo-measures, proxies") "measure
something related to the attribute of interest" and are "Used when there is no direct measure or
the direct measurement is too expensive". The proxy must be correlated to the attribute of
interest: "Strong correlation means we have a good indirect measure", "Weak correlation means that
our indirect measure may be problematic". The slide's example: the "Cost of development cannot be
directly quantified because required data about time invested and personal costs is missing", so
one may "Measure size of produced code as proxy for costs" — but "difficult and complex code can
be expensive, but small".

**Types of measures.** *Objective* — "quantification based on objective facts", e.g. counting
the non-empty lines of code. *Subjective* — "quantification may be subjective", e.g. readability.
*Diagnostic* — "measure current state"; *Prognostic* — "measure how the state will be".
*Robust* — "measure cannot be influence by humans"; *Sensitive* — "measure can be influenced to
achieve desired outcomes".

**Quality attributes of measures, part 1.** *Plausibility / validity* — "Does the measure
actually measure the desired property?", following from the representational theory of
measurement: "scales must be mappable to our empirical experiences". *Relevance* — "Is the
measure useful and can it be interpreted in a meaningful way?". *Cost efficiency* — "How much
does a measurement cost?". *Analyzability* — "Is the measure suitable for further downstream
analysis?".

**Quality attributes of measures, part 2.** *Availability* — "Can we measure an attribute at the
time we need the measurement?". *Resolution* — "Can the measure capture meaningful and noticeable
differences?". *Reproducibility* — "Do we get the same results if we apply the measure multiple
times or in different environments?".

## Worked Example

The four cells of the grid each get their own slide of worked examples.

**Internal product metrics** measure size, complexity and internal quality. Size via Source Lines
Of Code (SLOC) — "Lines of code without empty lines and comments" — with variants Comment LOC
(CLOC) and Test LOC (TLOC); "Measurement can be part of raw data collection with static analysis
tools!". Complexity via Cyclomatic Complexity (CC), "Also known as McCabe's Complexity", which
"Measures the number of branches in code". Object-oriented metrics such as the Chidamber &
Kemerer suite, "defined with six metrics to measure aspects of object-oriented software proposed
in the 90s", e.g. Weighted Method per Class (WMC, sum of CC of all methods in a class) and
Response For a Class (RFC, number of objects that a class calls). Self-admitted technical debt by
counting TODO comments. Summary: "Internal product metrics are often related to how maintainable
a software product is".

**External product metrics** measure how users experience the software. Mean Time To Response
(MTRR) — "Quantifies how long a user needs to wait for a response, e.g., of a Web service" —
"inferred by analyzing log data". Mean Time Between Failures (MTBF) — "Quantifies how much time
passes between two outages of a system", likewise from log data. Defect density — "the ratio of
number of bugs and size", which "Quantifies the external quality of the code" and "Can be
inferred by analyzing commit messages and/or issues for bugs and code for size". Summary:
"External product metrics are often related to how users perceive software quality".

**Internal process metrics** measure progress inside the development process. Development
velocity — "Used by SCRUM to estimate how much work can be done within in sprint", "Usually
measured by the number of story points completed within a sprint", "Can be inferred from the
issue tracker". Mean Time to Resolve — "Important metric to track if the development can keep up
with the amount of reported issues", in two variants "for all issues or only for bugs". Code
Review Coverage — "The amount of code review conducted is an indicator for the adherence to
quality assurance best practices".

**External process metrics** measure the process from outside the team. Deviation from schedule
— "Can be inferred if the project plan is available within the repository", and "Can also use
data from issue tracking to see if issues were deferred to later releases". Customer Support
Response Time — "Can be inferred from issue tracking data", with the warning "Not to be mixed up
with the internal aspect of actually addressing concerns" — it "considers the time to respond;
Response could also be that something will be addressed at a later time". Post-release defects —
"Defects after the release should be prevented by the development process" and "Many defects are
an indicator that the process has a low quality".

**MSR as the operationalization engine.** "At its core, MSR provides data about software
engineering — The data can be used as foundation for measurements — MSR suitable to obtain
measurements for all four kinds of software metrics", e.g. "code quality based on collected source
code", "mean time to fix a bug based on issue tracking data". The closing line: "Collection of
software metrics about raw data enriches data!"

## Common Pitfalls

- **Reporting a number without its rule.** A measurement without rules defined in advance is not
  a measurement by the Fenton & Pfleeger definition.
- **Using a proxy without checking correlation.** Size as a cost proxy fails for "difficult and
  complex code … but small".
- **Confusing internal and external attributes.** Defect density is external product; complexity
  is internal product.
- **Confusing diagnostic and prognostic measures.** A measure of the current state does not
  predict the future.
- **Ignoring sensitivity.** A measure "can be influenced to achieve desired outcomes" — e.g. an
  activity metric that developers can game.
- **Ignoring reproducibility and availability.** A measure that cannot be recomputed, or
  computed when needed, fails two named quality attributes.
- **Comparing LOC variants as if they were one measure.** SLOC, CLOC and TLOC measure different
  things, and the terminology slide separates quantification, measure and metric.

## Connections

- [[software-metrics]] — this page; measurement theory, the classification grid, and the four
  worked cells.
- [[mining-software-repositories]] — the pipeline that supplies the raw data metrics are
  computed from.
- [[repository-link-enrichment]] — where the labels and links that metrics depend on come from.
- [[msr-data-noise]] — the error rates that make a metric's validity questionable.
- [[developer-social-networks]] — centrality measures as network-level metrics.
- [[community-smells]] — structural counts (number of silos, lone wolfs, black clouds,
  bottlenecks) as process-level measures.
- [[defect-prediction]] — the model-based counterpart to counting defects.
- [[msr-statistical-methods]] — what a metric needs before it can be tested.
- [[statistical-significance]] — the Semester 1 page on significance testing.
- [[threats-to-validity]] — where a measure's quality attributes fail in practice.

## Open Questions

- **The grid is presented as orthogonal, but no slide says how the two dimensions interact.**
- **The slide acknowledges alternative classifications and then sets them aside** ("There are
  also other classifications in the literature that, e.g., consider resources as well").
- **The quality attributes are listed without thresholds.** Validity, relevance, cost
  efficiency, analyzability, availability, resolution and reproducibility have no pass criteria,
  so "good enough" for a metric is undefined.
- **The relationship between the three definitions of measurement is left unresolved.** They
  differ in what they require — rules, model or theory, reduction of uncertainty — and the slide
  does not say which governs.
