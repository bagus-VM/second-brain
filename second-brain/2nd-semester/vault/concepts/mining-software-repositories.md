---
title: "Mining Software Repositories"
tags: [concept, mining-software-repositories, semester-2, msr]
course: "Mining Software Repositories"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
MSR is a pipeline: take the data a repository already records, collect it in a form you can
analyse, analyse it, and end up with either a finding you can defend or a tool somebody can use.

## Core Intuition

The slide that defines the field is a four-cell diagram, and each cell is a place where a study
can fail:

```
Data from software repositories  ->  Data collection  ->  Data analysis  ->  Insights or tools
```

Read it as a chain of obligations. If you have no trustworthy data, no analysis rescues you. If
you collected data nobody can trust — heuristics with 42 % error, links you guessed — then the
analysis is precise about the wrong thing. And the output has to be either an **insight** (a
claim about software development you can state and defend) or a **tool** (something a developer
can act on). A pipeline that produces neither is a data-collection exercise, not MSR.

The reason the field exists at all is that the software industry has been making decisions on
anecdote for decades. The lecture makes the comparison explicitly with evidence-based medicine:
in conventional medicine, a therapy is suggested, then evidence is collected about whether it
works — positive effects, other positive side-effects, negative side-effects, and the likelihood
of each — and only then is the decision about how the therapy may be used made. Software
engineering, by contrast, has "PEPs to guide Python development" that are "not guided by rigorous
evidence, but rather experience and anecdotal evidence". The pipeline is the machinery for closing
that gap.

Two properties of the data make this unusual as an empirical science, and both are stated in the
slides. First, the data is **a by-product of work that was going to happen anyway** — nobody
wrote a commit message for the researcher's benefit, but every commit message exists. Second,
the data is **about people**, not only about artefacts: author names, email addresses, and the
social structure of who talks to whom. That second point is where the ethics live. The slide
names a concrete failure: GHtorrent was repeatedly used to contact developers, which "may lead to
problems"; and any study involving personal data has to check whether ethics approval is
required, with data-protection regulations applying regardless.

The analogy with mining is not decorative. Raw data is like ore in raw form; searching it is like
retrieving ore from a mine; finding useful patterns is like refining ore into metals. Each stage
costs money and each stage can be done badly — over-mining a rich seam exhausts it, and refining
badly produces slag.

## Formal Definition / Statement

The lecture's own definition of MSR is the pipeline equation:

```
MSR = Data from software repositories  +  Data collection  +  Data analysis
      -> Insights or tools
```

**What counts as a software repository**, per ISO/IEC/IEEE 24765:2017, quoted on the slide:

- "collection of all system element or software-related artifacts belonging to a system"
- "location/format in which such a collection is stored"
- "organized and persistent data storage that allows data retrieval"

Kagdi, Collard & Maletic (2007) give the complementary, evolution-side definition: "artifacts
that are produced and archived during software evolution".

And "data mining" is defined from Merriam-Webster as "the practice of searching through large
amounts of computerized data to find useful patterns or trends", with three key aspects the
slide highlights: **large amounts of computerized data**, **searching**, and **finding useful
patterns or trends**.

The data-mining technique taxonomy the slides give is worth memorising because it describes how
the middle stage of the pipeline may be carried out:

| Mode | How data is retrieved |
|---|---|
| Automated | e.g. from a warehouse |
| Manual | e.g. through manual coding of data |
| Semi-automated | e.g. through a human-guided interactive search, or the human augmentation of automatically collected data |

And the analysis techniques the slides list: automated analysis through machine learning (both
supervised and unsupervised), statistical analysis (distributions, statistical tests), anomaly
detection, dimensionality reduction, and visualization.

## Key Properties

- **The data is observational, not experimental.** Repositories record what happened; they do not
  randomise anything. Causal claims therefore need an explicit design argument, not just a
  correlation. See [[evidence-based-software-engineering]] and [[threats-to-validity]].
- **Collection, analysis and enrichment are separate stages with separate quality problems.**
  Enrichment — turning raw events into labelled, linked, measurable entities — is where the
  noise enters. See [[repository-link-enrichment]] and [[msr-data-noise]].
- **The enrichment step is where validity is won or lost.** A study that does not state how its
  labels were produced cannot be evaluated by anyone else.
- **Not every MSR project needs machine learning.** The slides are explicit: some tools merely
  visualize repository information (Code City), or aggregate information across repositories, or
  apply standard SE techniques such as clone detection at scale.
- **The evidence a tool produces is usually a proxy.** "the evidence is often not a business
  metric (ROI) or even a user metric (usability, time saved) but a proxy (e.g., accuracy)". The
  gap between proxy and reality is a validity threat, and it is the tool-builder's problem, not
  the tool-user's.
- **Tool building and evidence gathering are one project.** The slide's approach: identify the
  goal → identify the data → collect data and build the tool → collect more data and conduct an
  experiment. The last step is not optional decoration.
- **The repository is not the only data source.** Forges combine source control, issue tracking,
  code review, CI and social data in one place; for an MSR study the forge is "ideal" but the
  raw sources underneath are separable — see [[software-repositories]].
- **The subject of an MSR study is usually people, and the slides say so.** "when we speak of
  developer, we usually mean that in a broad sense as anybody somehow involved in a project";
  writing code is not required, issue reporting or being part of a chat is enough. The slides
  insist on making the narrower "actually writing code" case explicit when they mean it. This
  is a definitional distinction that matters for every social-network analysis in the course.
- **The pipeline is where the ethics sit.** Collecting developer profiles from contributions
  carries the risk that made GHtorrent's repeated outreach problematic, and personal data brings
  data-protection law regardless of how ethically the study was designed.
- **A finding and a tool are different deliverables.** The slide splits the final stage into
  "Insights or tools", and the tool-building lecture spends a full lecture on how to move from
  one to the other.

## Worked Example

The lecture's four motivating examples are each a different *use* of the same pipeline, and each
one lands on a different final cell:

1. **GitHub Copilot** — "Data about code changes is used to train AI models." The pipeline's
   output here is a *tool* (an assistant), and the repository is the training corpus. This is the
   example where the "insights" stage is skipped entirely: the data is the model.
2. **Insights into development processes** — "Data can be used to understand the impact of best
   practices and tools." Here the output is an *insight*, and the interesting part is that a
   tool's effect can be measured from the repository afterwards, without any instrumentation.
3. **Social networks** — "Data can be used to understand social aspects of software
   development." The pipeline needs enrichment to build the network at all: who counts as a node,
   what an edge means. See [[developer-social-networks]].
4. **Insights into bugs and failures** — "Data can be used to understand how to avoid or find
   problems." This is the application that consumes the defect-prediction machinery of
   [[defect-prediction]].

A concrete tool example closes the chain. The lecture lists several MSR tools that exist as
products or research systems, and one of them is used *inside* another: **Nudge** accelerates
overdue pull requests towards completion; **Tesseract** lets a developer explore who works
together on what; **Code City** visualizes source-code size, complexity and package structure as
a city map. **Teamscale** is the commercial case — a company whose product is the analysis of
code repositories, and where "others were acquired and integrated into larger products". That
last detail is the strategic point of the lecture: MSR output has market value, which is why
"MSR as a Product" is a slide heading.

The tool-building slide then shows the full cycle with a warning embedded in it. Suppose the
goal is "rank static analysis warnings based on past fixes of warnings". The data needed is the
history of warnings and the commits that fixed them — obtainable from the repository, but noisy.
The model is trained on some repositories, evaluated on others, and then the question that
decides whether the tool is worth anything is asked: "Determine if/how this would help
developers". The slide's honest footnote is that the evidence will usually be a proxy (accuracy),
not a user metric (time saved) or a business metric (ROI).

## Common Pitfalls

- **Treating the pipeline as one step.** Collecting data and analysing it are separate
  obligations with separate failure modes; a beautiful analysis of badly collected data is
  still badly collected data.
- **Confusing a proxy with the thing you care about.** "accuracy" is not "developer productivity".
  The slides flag this explicitly and it is the most common way an MSR tool over-claims.
- **Skipping the enrichment step and pretending raw events are the data you want.** A commit is
  not a defect; a diff is not a bug-fixing change; an issue is not automatically a bug. Each of
  those conversions needs a heuristic, and each heuristic has a measured error rate.
- **Using "developer" without saying which sense.** The slides use the broad sense (anybody
  involved in the project) unless they say otherwise. A social-network study that silently
  means "committers only" has changed its population.
- **Reading the ethical slide as optional.** Repositories contain email addresses, and contacting
  developers repeatedly is a documented incident in this field.
- **Assuming the data can be collected without cost.** The lecture's exercise materials
  themselves are built on the same constraint: GitHub applies a rate limit on unauthenticated API
  requests, and large repository clones are expensive enough that tools like PyDriller are given
  a "clone repo to" parameter purely to avoid re-cloning on every run.
- **Treating "optional" exercises as free.** The slides are careful: the exercises are optional
  in the sense that you do not automatically fail without them, but they are *not* optional in
  the sense that you can expect a good grade without solving them.
- **Calling anything that touches a GitHub API "data mining".** Mining is the *practice of
  searching through large amounts of computerized data to find useful patterns or trends* —
  the definition has a purpose in it. Data collection alone is not the same activity.

## Connections

- [[software-repositories]] — what the pipeline's input actually is, and the many kinds there
  are.
- [[evidence-based-software-engineering]] — the motivation, and the survey/case-study/experiment
  distinction.
- [[msr-tool-building]] — the second half of the lecture's output stage.
- [[software-metrics]] — the measurement layer that sits between raw events and claims.
- [[repository-link-enrichment]] — how commits, issues and pull requests are linked.
- [[msr-data-noise]] — the price of the heuristic enrichment step.
- [[developer-social-networks]] — the social application, and the modelling choices it forces.
- [[defect-prediction]] — the bug application, and the prediction models built on repository
  data.
- [[msr-statistical-methods]] — the statistical machinery that makes an insight defensible.
- [[threats-to-validity]] — the checklist that says whether a conclusion survives.
- [[msr-research-paradigms]] — the philosophical stance that decides the method.
- [[git-dag-structure-and-internals]] — the Semester 1 page on Git's object model; the
  data-collection lecture relies on it.
- [[statistical-significance]] — the Semester 1 page on significance testing.

## Open Questions

- **The slide's own "MSR + data mining" equation is a pipeline, not a formal definition.** There
  is no criterion in the material for when something stops being MSR and becomes ordinary data
  analysis on repository dumps.
- **The mining analogy is never used quantitatively.** Ore, seam, refining and slag appear as an
  illustration; the material gives no cost model, no notion of exhaustion, and no account of what
  happens when the rich seam (the popular open-source repositories) is mined out.
- **The definition of a repository is three bullet points from a standard**, and the slide does
  not reconcile them with Kagdi et al.'s evolution-side definition. Whether "location/format in
  which such a collection is stored" counts a local checkout as a repository is not addressed.
- **"Insights or tools" is an either/or that is never resolved.** Several slides mix the two —
  Tesseract is a research system and a product; Code City is a visualization technique. The
  material does not say whether a tool *is* an insight in another form.
- **The evidence gap is identified but not quantified.** "the evidence is often not a business
  metric … but a proxy" — the slides do not say how to bridge the proxy gap, only that it exists.
- **The ethics slide names a failure but no procedure.** "Any study that involves personal data
  needs to check if an ethics approval is required" — but who checks, against what criteria, and
  what an approval obliges, is not in the material.
- **The exercise materials are in tension with the pipeline framing.** Both exercise sheets carry
  an explicit instruction from their owner that they are not to be solved with AI assistance.
  Whether that applies to the practical components of the course's own exercises is a question
  the slides do not address, and it is recorded on the course page rather than resolved here.
