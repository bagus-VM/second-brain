---
title: "Evidence-Based Software Engineering"
tags: [concept, mining-software-repositories, semester-2, research-methods]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Evidence-based software engineering applies the logic of evidence-based medicine to technical
decisions: gather rigorous evidence first, then decide — and MSR is the instrument that makes
the gathering possible.

## Core Intuition

The introduction lecture opens this thread with a deliberate contrast. Conventional medicine
follows a standard: suggest a therapy (e.g., a new drug), then collect evidence about how it
works — "Does the therapy have the desired positive effect? Does the therapy have other positive
side-effects? Does the therapy have negative side-effects? How likely is each of the above?" —
and only then is "Decisions on how therapy may be used" made. All of this is "(hopefully) based
on rigorous study designs with the goal to demonstrate causal relationships between therapies and
outcomes".

Software engineering, by contrast, is depicted on the next slide as a bare three-step sequence:
"Usually someone suggests something — Some group discusses this — And then a decision is made".
The example given is PEPs to guide Python development, which are "Not guided by rigorous
evidence, but rather experience and anecdotal evidence".

The remedy slide restates the sequence with one substitution: "When someone suggests something
— **We collect evidence** — And then a decision is made about the suggestion", annotated "Guided
by evidence, but requires a lot more effort!". The whole slide deck is built to argue that the
missing middle step is now cheap, because the evidence is a by-product of development work that
was going to happen anyway.

The critical subtlety is that evidence-based medicine is *staged*, and so is EBSE. The medicine
analogy runs through a multi-stage process: lab experiments (in vitro), animal experiments (in
vivo), an initial study with human subjects for safety analysis with a small sample, and a
randomized trial with many subjects — "large sample with treatment and a control group without
treatment". Each stage narrows what is still unknown, and each stage has its own ethics. The
course's contribution is that repository data can stand in for several of these stages at once.

## Formal Definition / Statement

The lecture takes its three definitions of evidence collection from a single source: C. Wohlin,
P. Runeson, M. Höst, M.C. Ohlsson, B. Regnell, and A. Wesslén, *Experimentation in Software
Engineering*, Springer Berlin Heidelberg, 2012, ISBN 9783642290435.

**Survey** — "A survey is a system for collecting information from or about people to describe,
compare or explain their knowledge, attitudes and behavior".

**Case study** — "Case study in software engineering is: an empirical enquiry that draws on
multiple sources of evidence to investigate one instance (or a small number of instances) of a
contemporary software engineering phenomenon within its real-life context" — the definition
continues by making the case-study form obligatory "especially when the boundary between
phenomenon and context cannot be [specified]".

**Experiment** — "Experiment (or controlled experiment) in software engineering is an empirical
enquiry that manipulates one factor or variable of the studied setting. Based in randomization,
different treatments are applied to or by different subjects, while keeping other variables
constant, and measuring the effects on outcome variables. In human-oriented experiments, humans
apply different treatments to objects, while in technology-oriented experiments, different
technical treatments are applied to different objects".

Note what the case-study definition does with the phrase *empirical enquiry*, and note that the
experiment definition rests on two pillars the slides name explicitly: **randomization** and
**holding other variables constant**. A repository study that observes without manipulating
satisfies the case-study half, not the experiment half.

## Key Properties

**The three designs are distinguished by what they manipulate, not by their topic.** A survey
collects from or about people; a case study investigates one instance within its real-life
context; an experiment manipulates one factor with different treatments applied to or by
different subjects. The lecture's mapping for MSR makes this operational: "Can be used both for
case studies and experiments — Depends on the design! Are you only observing a group of subjects
to draw conclusions → case study; Are you looking at different treatment groups or studying
interventions → experiment".

**Surveys from repositories are built from developer profiles.** "Repositories can be used to
create developer profiles — Based on their contributions, e.g., commits, issues, emails, etc."
These profiles "Helps to identify suitable subjects, e.g., developers that fit a certain
profile": familiar with a programming language, familiar with a technology such as a framework,
core developer of a project.

**The lecture fixes the meaning of "developer" for the course.** "Within this lecture, when we
speak of developer, we usually mean that in a broad sense as anybody somehow involved in a
project. Thus, writing code is not a requirement, other activities like issue reporting, or
being part of email or chat conversations is also sufficient. If we instead want to refer to
someone actually writing code, we will make that explicit." Every survey in the course inherits
this population definition.

**Surveys from repositories carry an explicit ethics caveat.** "Not without ethical issues and
risks: Repeated requests for survey participation may lead to problems — Happened when GHtorrent
was repeatedly used to contact developers". And: "Any study that involves personal data needs to
check if an ethics approval is required — Even with ethical approach, data protection
regulations my still apply!" (typo in the original slide). The deck links the incident to the
GHtorrent blog post about issue thirty-two.

**Case studies from repositories have breadth of purpose.** "Software repositories contain huge
amounts of data — This data can be used for many research purposes": to study code reviews one can
view them on GitHub or Gerrit; to study code quality, code is available in the source code
versioning system and information about defects in issue trackers; to study how developers in
different time-zones interact, "Who contributes to the same parts of a software can be
reconstructed from repositories".

**The cost asymmetry is the motivation.** The evidence-based slide marks the middle step as
"requires a lot more effort!", and the mining lecture's own framing is that repository data is
"a by-product of work that was going to happen anyway".

## Worked Example

The lecture's example of evidence in software engineering is the PEPs to guide Python
development (peps.python.org): a real decision-making body whose practice the slide characterises
as guided by "experience and anecdotal evidence" rather than rigorous evidence. It is the
canonical instance of "someone suggests something — some group discusses this — and then a
decision is made", and the canonical gap the course wants to close.

The second worked example is the GHtorrent case, presented as a cautionary tale inside the
survey branch of the framework. The mechanism is specific: a research instrument (GHtorrent) was
repeatedly used to contact developers to recruit survey participants, and the slide states that
this "may lead to problems". The example is not about data quality at all; it is about the step
where a repository-derived profile becomes a human subject. That step is where the medicine
analogy's staged structure and the ethics-approval requirement intersect: a study that recruits
people has crossed from observation into intervention.

## Common Pitfalls

- **Calling an observational study an experiment.** The lecture's test is explicit: if you only
  observe a group of subjects and draw conclusions, it is a case study. Repository data collected
  after the fact is observational by construction.
- **Treating "developer" as "committer".** The course uses the broad sense by default — anybody
  somehow involved in a project — and narrows it only when it says so explicitly.
- **Skipping the ethics check because the data is public.** "Any study that involves personal
  data needs to check if an ethics approval is required", and data protection regulations apply
  "even with ethical approach".
- **Assuming a large repository sample is a survey.** A survey needs a defined instrument
  collecting from or about people; mining commits produces a population description, not a
  survey instrument, unless the study designs one.
- **Confusing anecdotes with evidence without acknowledging the gap.** PEPs are the deck's
  example of evidence-free decision making, so an EBSE study must state explicitly what its
  evidence is.
- **Overstating what the medicine analogy licenses.** The analogy is a motivation for rigor; the
  deck does not claim that repository data satisfies randomization for a study that needs it.
- **Ignoring the population definition.** A profile built from issues and emails and one built
  from commits contain different people; the two are not interchangeable as subjects.

## Connections

- [[evidence-based-software-engineering]] — this page; the survey/case-study/experiment
  distinction and the medicine analogy.
- [[mining-software-repositories]] — the pipeline whose output is meant to be evidence.
- [[msr-research-paradigms]] — the neighbouring philosophical frame the lecture gestures at.
- [[threats-to-validity]] — where the case-study design's weaknesses get named.
- [[software-repositories]] — the raw material for building developer profiles.
- [[developer-social-networks]] — one concrete way "who contributes to the same parts of a
  software" is reconstructed.
- [[msr-statistical-methods]] — the machinery for the "rigorous study designs" the analogy
  demands.
- [[statistical-significance]] — the Semester 1 page on significance testing.
- [[qualitative-coding]] — the other route to evidence, used when the phenomenon is not
  quantifiable.
- [[grounded-theory]] — the qualitative alternative the lecture does not develop but which its
  coding material parallels.

## Open Questions

- **The staged structure of evidence-based medicine is not mapped onto EBSE.** The medicine
  slides give in vitro, in vivo, initial human safety trial and randomized trial; the EBSE
  slides give survey, case study and experiment — three items, not four — and no slide explains
  how the analogy's stages correspond.
- **The lecture does not say when an observational repository study needs ethics approval.** It
  says any study involving personal data "needs to check if an ethics approval is required", but
  the criterion for the check is not given.
- **The effort asymmetry is asserted, not measured.** "requires a lot more effort!" is a
  qualitative claim; the deck gives no comparison of the cost of evidence collection against
  anecdotal decision making.
- **The boundary between "broad-sense developer" and "person involved in a project" is not
  operationally settled.** An automated scraper can distinguish committers from commenters, but
  a lurker is indistinguishable from an outsider.
