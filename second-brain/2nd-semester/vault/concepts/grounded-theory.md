---
title: "Grounded Theory for MSR"
tags: [concept, mining-software-repositories, semester-2, qualitative-methods]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Grounded theory builds a theory out of data by coding it inductively — and the lecture's chosen
variant, Straussian grounded theory, works through three coding stages that end in a theory
grounded in the material itself.

## Core Intuition

The lecture motivates grounded theory by contrast with everything that came before it:

- "The research methods we considered so far were based on statistics."
- "Statistics are a powerful method to analyze hypothesis that you already have. This requires
  some existing theory from which the hypotheses are derived. Best suited for confirmatory
  research."
- Statistics "can also be used inductively, but in this case the results are less trustworthy.
  E.g., by running many tests to see if any variables have a relationship without having a theory
  yet what the relationships might be."
- "Statistics assume a positivistic world view, i.e., that we can capture reality through these
  numbers."
- "What we are still lacking are methods for interprevistic research that are suitable to
  generate theories."

Grounded theory fills that gap. Its essential property is that "the theory should be derived from
the data, not from the literature" — the theory is *grounded*, and the derivation is traceable
through codes, memos and categories.

The lecture is also careful about what it does **not** cover: "Note: we do not consider methods
for interprevistic confirmatory research (e.g., triangulation)".

The reference given on the slide is Stol, K. J., Ralph, P., & Fitzgerald, B. (2016, May),
"Grounded theory in software engineering research: a critical review and guidelines", in
*Proceedings of the 38th International Conference on Software Engineering*, pp. 120-131.

## Formal Definition / Statement

**Variants.** "Grounded theory is a set of methods with different variants proposed over the
years":

- Classic / **Glaserian** grounded theory (Glaser and Strauss, 1967)
- **Straussian** grounded theory (Strauss and Corbin, 1990; "Within this lecture, we focus on
  Straussian grounded theory as published in 1998")
- **Constructivist** grounded theory (Charmaz, 2000)

Their differences as the lecture states them: "Glaserian grounded theory puts a stronger focus on
the emergence of a theory only from the data without prior knowledge, biases and expectations";
"Constructivist grounded theory is somewhere in the middle, while also allowing for a
constructivist stance". And: "The variants also have difference between the way data is analyzed
and the terminology, including between evolution of variants."

**The Straussian overview**, as the slide prints it:

```
Input: (Usually textual) data — In MSR, e.g., issues or code reviews collected from a repository

Open coding       -> Analyze the data and inductively identify concepts
                     Concepts are described by code words
Axial coding      -> Identify relationships between the categories
                     This is based on the context, conditions, actions/interaction strategies, and consequences
Selective coding  -> Determine overarching major categories that all other can link to
                     Should be abstract and suitable to develop hypotheses

Forming theory    -> Formulate a theory that explains the identified relationships
                     Theory should be based on the (major) categories

Output: Theory that is developed based on the data — E.g., a theory about how developers interact within code reviews
```

**Memoing.** "Throughout the process, researchers keep and update notes called memos. The memos
can be diverse and support the analysis activities." Examples given: "Explanations why a certain
category was assigned", "Explanations for the codes that describe the categories", "Diagrams
showing relationships between categories", "Gaps within the current data, categories,
relationships, or theory". And: "Memos are crucial for all grounded theory activities and form
the backbone of the inductive reasoning. The memoing should be on a sufficient level of detail
such that other researchers can follow all reasoning steps."

**Development of research questions.** "The positivistic research methods we considered earlier
assume that there are clear research questions. Grounded theory breaks with this assumption.
Within Straussian grounded theory, the research question could be

- Developed during the coding process
- Defined beforehand based on a clear objective
- Derived from existing literature, e.g., as an open questions about a topic or something that
  should be confirmed

This enables grounded theory as a method for confirmatory research." And: "Research questions for
grounded theory are typically more open and generic than those for positivistic research.
Positivism typically comes with an expectation, at least on the hypothesis level. The
interpretivistic grounded theory (usually) does not have such expectations but rather lets this be
guided by the data."

**The role of literature.** "A key aspect of grounded theory is that the theory should be derived
from the data, not from the literature. Exposure to literature means that existing knowledge and
theory influence the researcher and, consequently, also the developed theory. Can lead to
confirmation bias." The historical line: "The original Glaserian variant of grounded theory
suggested not to consider literature at the beginning at all. Later variants, including
Straussian grounded theory allow for early considerations of literature, including before the
start of a study for the development of research questions. Straussian grounded theory allows the
use of literature throughout the process to help with a better theoretical understanding, as
secondary data source." Final line: "All variants state that literature should be used to enhance
the emerging theories."

**Theoretical sampling and saturation.** "As part of grounded theory, researchers can identify
the need for more data

- To get further information about gaps found in the already collected data
- To get more data for specific categories

This process of additional data collection based on the needs to develop the theory is called
theoretical sampling. This is a type of purposive sampling. This data collection stops once
theoretical saturation is reached. Achieved when all components of the theory are well supported.
New data is no longer added information and leading to revisions of the theory."

**Notes on terminology.** Other variants use different coding names: "theoretical coding
(Glaserian, constructivist), which is similar to axial coding"; "initial coding (constructivist),
which is similar to open coding"; "focused coding (constructivist), which is similar to selective
coding but rather focuses on the most frequent categories". And on categories: "Some source first
develop initial codes, which are then grouped into concepts, which are further refined into
categories. When this terminology is used, the concepts are typically the result of the open coding
and the categories the result of the axial coding."

## Key Properties

- **It is a theory-generation method, not a testing method.** The statistics comparison is
  explicit: statistics are "best suited for confirmatory research"; grounded theory generates the
  theory in the first place.
- **The output is a theory grounded in the data**, not a set of findings about variables.
- **Three coding stages, in order, each with a stated purpose.** Open → concepts via code words;
  axial → relationships using "context, conditions, actions/interaction strategies, and
  consequences"; selective → "overarching major categories that all other can link to" that are
  "abstract and suitable to develop hypotheses".
- **The research question can be an output of the method.** Grounded theory "breaks with" the
  positivist assumption of clear prior questions — and can also be confirmatory if the question is
  defined beforehand.
- **Memos are the audit trail of the inductive reasoning**, and must be detailed enough that
  "other researchers can follow all reasoning steps".
- **Literature use is allowed but is a bias risk.** Straussian permits it throughout as a
  secondary data source; Glaserian forbids it at the start.
- **Data collection is driven by theory needs, not by a fixed plan.** Theoretical sampling is
  purposive sampling with the purpose of filling gaps and supporting categories.
- **The stop rule is theoretical saturation**: "all components of the theory are well supported"
  and new data no longer adds information or forces revisions.
- **Terminology varies across variants**, so a paper must state which variant it uses.

## Worked Example

**The lecture's worked example is the code-review theory.** The input is textual data — "In MSR,
e.g., issues or code reviews collected from a repository" — and the output on the slide is "a
theory about how developers interact within code reviews".

Running the pipeline on that input: the coder reads review comments and assigns code words to
concepts (open coding); axial coding relates those into categories using context, conditions,
actions and consequences; selective coding lifts one or a few overarching categories that
everything else links to, which must be "abstract and suitable to develop hypotheses"; then the
theory is formed to explain the identified relationships, based on the major categories. Memos
record why each category was assigned, which codes describe it, diagrams of the relationships,
and the gaps still open.

**The feedback loop is the point.** Open coding surfaces gaps; the researcher identifies "the need
for more data" — "to get further information about gaps found in the already collected data" or
"to get more data for specific categories" — and collects it (theoretical sampling, a type of
purposive sampling). The loop stops at saturation. This is what distinguishes grounded theory
from a one-pass qualitative description: the corpus grows in response to the analysis.

**Contrast with the statistical route.** The lecture's framing gives the alternative explicitly:
running many tests "to see if any variables have a relationship without having a theory yet what
the relationships might be" is inductive use of statistics, and "in this case the results are
less trustworthy". Grounded theory is the same inductive goal reached through codes and memos,
and it also supports the follow-up step — the selective coding stage produces categories
"suitable to develop hypotheses", which is how a grounded-theory study hands off to confirmatory
work.

**The terminology translation, worked.** A constructivist study that reports "initial codes →
concepts → categories" is reporting open coding → open coding → axial coding; a study that
reports "focused coding" is reporting selective coding "but rather focuses on the most frequent
categories". Both are the same three-stage machinery under different names, and the slide's
terminology note is the key that lets you read across papers.

## Common Pitfalls

- **Using grounded theory to test a pre-existing hypothesis and calling it grounded.** The
  method's defining property is that the theory is derived from the data.
- **Skipping memos.** They "form the backbone of the inductive reasoning"; without them the
  analysis is not reconstructible, and the reliability threat "Insufficient details about data
  collection" is the consequence.
- **Reading literature before coding and not declaring it.** It "can lead to confirmation bias",
  and Straussian permits it only as a declared secondary data source.
- **Stopping data collection at a fixed sample size instead of at saturation.**
- **Confusing the coding stages.** Open coding identifies concepts; axial coding relates
  categories; selective coding finds the overarching categories. A study that reports only open
  codes has not built a theory.
- **Calling the theory "generalizable" without qualification.** Grounded theory produces
  interpretations of a corpus; the sampling lecture's point that interpretivism "rather accepts
  that samples may be inherently biased" applies.
- **Confusing the three coding names used by different variants.**
- **Ignoring the axis of the analysis as decorative.** Axial coding is "based on the context,
  conditions, actions/interaction strategies, and consequences" — that is the analysis framework,
  not a label.

## Connections

- [[msr-research-paradigms]] — the interpretivist stance that makes grounded theory the right
  tool.
- [[qualitative-coding]] — the coding mechanics (open, axial, harmonization, inter-rater
  agreement) that grounded theory builds on.
- [[msr-sampling]] — theoretical sampling as a purposive variant, and saturation as its stop rule.
- [[msr-statistical-methods]] — the confirmatory machinery grounded theory hands off to.
- [[threats-to-validity]] — reliability and construct validity for interpretive studies.
- [[community-smells]] — the first community smells were identified this way, "based on open and
  axial coding of the interview responses".
- [[developer-social-networks]] — where the interaction data that theories are built from comes
  from.
- [[mining-software-repositories-lecture-7]] — the source lecture for this page.

## Open Questions

- **The theory-building criterion is never made operational.** "Formulate a theory that explains
  the identified relationships" and "Theory should be based on the (major) categories" are
  criteria, not procedures; the slides give no test for whether a theory is adequately formed.
- **Saturation has no operational measurement.** "Achieved when all components of the theory are
  well supported. New data is no longer added information and leading to revisions of the theory"
  — the slide does not say who judges "well supported", or how much new data is enough.
- **The number of coding rounds is unconstrained.** Nothing states how many times a concept is
  revised, or whether axial and selective coding interleave with new data collection in a fixed
  order.
- **Coding reliability within grounded theory is not addressed.** The slides on multiple raters
  and inter-rater agreement come from the data-enrichment chapter, and the grounded theory slides
  do not say whether two coders may both open-code, or what happens when they produce different
  codes.
- **The relation between memos and the reliability threat is left implicit.** The validity
  lecture's example — "An open coding of code comment types does not describe if and how codes
  are harmonized between raters" — is exactly the grounded-theory situation, but the two lectures
  do not connect.
- **The "interpretivistic grounded theory" phrase is used without definition.** It is not said
  whether this refers to the constructivist variant or to a general stance, and the variants
  slide names constructivist as one of three but never ties it to that phrase.
