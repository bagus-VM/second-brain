---
title: "Sampling in MSR Research"
tags: [concept, mining-software-repositories, semester-2, sampling]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Sampling decides which data a study looks at, how that data was drawn, and how far the
resulting claim may travel — and randomness alone does not guarantee representativeness.

## Core Intuition

The lecture opens with the reason sampling exists: "We usually cannot consider all possible data
related to our research in our studies". The examples are the full universes of interest: "All
software projects in existence", "All open-source projects", "All software developers", "All
Python programmers". Instead "we study subsets of this data": "Popular projects", "Projects
with a specific size", "Randomly selected people". "This selection is called sampling."

Three nested sets frame the whole topic:

- **Population** — "all items that are of interest. What these are depends on the research
  question."
- **Sampling frame** — "the items of interest from which we create a sample".
- **Sample** — "the items of falsifiable interest from the sampling frame that we select through
  the sampling".

With the containment relation printed on the slide: **Sample ⊆ Sampling frame ⊆ Population**.
"Sampling methods define how we pick the sample from the sampling frame."

The lecture's own worked instance makes the three sets concrete for the question "What is the
male to female ratio within open-source development?": Population = all open-source developers;
Sampling frame = open-source developers on GitHub; Sample = 10% of the developers on GitHub
selected using simple random sampling.

## Formal Definition / Statement

**Three approaches to sampling**, as the lecture lists them:

1. **Non-probabilistic sampling** — "We select our sample based on fixed criteria such that we
   have all data that meets these criteria".
2. **Probabilistic sampling** — "We use a randomized method to select a sample".
3. **Multi-stage sampling** — "We use multiple steps for sampling, typically combining
   non-probabilistic and probabilistic methods to ensure our sample has certain properties, while
   still looking at a subsample of data".

**Non-probabilistic sampling, the methods.**

- *Convenience sampling*: "Select samples based on availability and/or expedience. E.g., projects
  for which you already have data, human subjects you know or have easy access to. Simplest
  sampling method that usually does not ensure any sample properties."
- *Purposive sampling*: "Select samples based on a defined strategy. The strategy is defined based
  on the research objectives. Criteria are used to operationalize purposive sampling." The criteria
  listed cover "Popularity (e.g., stars on GitHub)", "Activity patterns (e.g., number of commits,
  number of contributors, number of issues)", "Technology (e.g., programming language, build
  tools, static analysis methods, software tests)" and "Development process (e.g., use of code
  reviews, following best practices for linking data)". The slide adds a warning: "These criteria
  should not be based on convenience!"
- *Referral-chain sampling / snowball sampling*: "Requires a starting point, e.g., some samples
  already available or other information. New data points are determined based on their relation
  to this starting point." Example: "Start with core machine learning libraries (e.g.,
  scikit-learn, TensorFlow, PyTorch). Then select that are imported by these libraries. This
  would be a sample representing what these libraries depend on".
- *Respondent-driven sampling*: "Variant of referral-chain sampling for sampling and recruitment
  of human subjects. Start with a small but diverse set of subjects. Each subjects is asked to
  recruit more subjects (e.g., three more people). The idea is, that these recruited people still
  represent the diversity from the initial sample. Repeat until enough subjects are sampled and
  the results are stable. Requires strong mathematical controls that can account for potential
  sampling bias".

**Probabilistic sampling, the methods.**

- *Simple random sampling*: "Each subject as an equal chance of being sampled, i.e., the chance
  of inclusion follows a uniform distribution".
- *Systematic random sampling*: "First order the data points in the sampling frame by some
  attribute. E.g., by popularity, size, age, … Define an interval size, denoted here as
  step_size. Randomly select a starting point start ∈ 1, step_size with a uniform distribution.
  Select the samples start, start + step_size, start + 2·step_size, … Ensures that subjects are
  sampled over the whole range of the ordered attribute".

**Multi-stage sampling, the methods.**

- *Stratified and quota sampling*: the drawback of simple random sampling "is that we cannot
  control what the sample looks [like]. While this is intentional, this also might mean we loose
  [lose] important information." Example: "when we want to study differences between female and
  male developers, a simple random sample would likely have (a lot) more male developers than
  female developers". Procedure: "we first split our data into subsets based on some property.
  This is the first stage of the sampling. E.g., gender, race, bugginess, amount of testing, …
  Afterwards, we sample independently from the subsets. This is the second stage of the sampling.
  If the second stage is probabilistic, this is called stratified sampling. If the second stage is
  non-probabilistic, this is called quota sampling." The benefit: "Allows, e.g., to have the same
  amount of male and female developers in a sample, even if the ratio is not equal in the complete
  data set".
- *Cluster sampling*: "Sometimes, it is not feasible to study all these subgroups. For example,
  not papers on MSR from all highly ranked conferences (because there are too many), but only from
  a subset of the conferences. In this case, we can apply cluster sampling. First divide the
  sample into subgroups and sample a subset of these subgroups as clusters to study. Then draw
  samples from the selected clusters. If the selection of the clusters and samples are both
  randomized, this is also called cluster random sampling."
- The distinction, as printed: "**Stratified sampling uses all subsets, while cluster sampling
  uses only a subset.**"

**Other sampling methods.**

- *Whole frame sampling*: "simply uses all data from the sampling frame, i.e., there is no
  selection of a subset of data".
- *Panel sampling*: "re-uses a sample multiple times. This is often used to study longitudinal
  effects by observing changes to study subjects. E.g., studying the same sample of projects at
  different points in time".

**Representativeness.** "The representativeness is the degree to which the properties of interest
of a sample resemble these properties within the population." "Representativeness is important for
positivistic research methods" — because positivism "assumes we can objectively observe and
quantify phenomena and thereby generate knowledge though empirical observation of evidence" — and
"important to understand if what we observe in a sample can be generalized to the sampling frame
and the population". By contrast: "Interpretivism is not interested in such generalizations and
rather aims to understand data within its subjective context. Thus, interpretivism rather accepts
that samples may be inherently biased and tries to account for that when interpreting data."

**Randomness vs. representativeness.** The slides call out the conflation directly: "We selected
a random sample, therefore it is representative", "Since the data was not selected randomly, we
doubt whether we can generalize". "While there is a relation, it is not automatic."

**Aspects of representativeness**, as slide bullets:

- "Representative is dimension-specific. A sample can be representative for some properties and
  not representative for other properties."
- "Probability sampling does not guarantee representativeness. A sample can be unlikely and not
  follow expected distributions, or an important criterion was not considered during sampling."
- "Non-probabilistic samples can still be representative. A target selection of suitable samples
  is often helpful, especially for small sample sizes."
- "Representativeness does not only depend on the type of sampling, but also the size of the
  sample. Problems with probabilistic sampling get smaller with large sample sizes, because it is
  less likely to have unlikely samples and it becomes more likely that criteria not actively
  considered during sampling are represented, nevertheless."

**The "Random selection vs. Possible problems" table**, as printed on the slide:

| Random selection argument | Possible problems |
|---|---|
| Size | "Each item in sampling frame as an equal probability of inclusion" |
| Breadth | "Assumes large sample size, good sampling frame, and no bad lack" (as printed) |
| Sample size is so large that no good and no bad subpopulations are missed | "Can still have biases towards or against subpopulations" |
| Parameter matching | "Point estimates (e.g., mean values) may be unreliable, requires large size to be representative" |
| Sample captures a large variance on important parameters | "Sample and sample frame of similar distribution for all parts of covered variance" |
| | "Assumes all important properties are known, matching restricted to sample frame" |
| | "No 'one-fits-all' approach. Needs to be considered and judged in the context of a concrete study!" |

## Key Properties

- **Sampling is a decision about scope, and the frame defines the scope.** The population depends
  on the research question; the frame is its operationalisation.
- **The choice of sampling method is entangled with the choice of paradigm.** Positivism needs
  representativeness; interpretivism can live with bias if it is accounted for.
- **Randomness is not the same as representativeness**, and the slides show why with a concrete
  bimodal example.
- **Representativeness is per-property, not a global verdict on a sample.**
- **Purposive sampling can be legitimate.** It is standard practice in MSR and is defended in
  the validity lecture's external-validity example, which cites Baltes & Ralph (2020) arguing
  "that well-done purposive sampling should also yield generalizable results".
- **Stratified and cluster sampling differ in coverage.** All subsets versus a subset of subsets.
- **Multi-stage sampling is the norm in practice.** The lecture's methods are "typically
  combining non-probabilistic and probabilistic methods".
- **Sample size is a validity lever, not only a power lever.** It changes how likely the sample is
  to be representative.
- **Whole-frame and panel sampling are legitimate options** that sidestep the selection problem,
  at the cost of scope or of generalisation.
- **Grounded theory's theoretical sampling is a special case of purposive sampling** — see
  [[grounded-theory]].

## Worked Example

**Randomness vs. representativeness, worked.** The slide assumes the sampling frame's project
sizes are bimodal: "we have projects that are small (mean=2000) and large (mean=10000)". A small
random sample from that frame is "representative for the overall mean, but not for the small and
large projects"; a large random sample is "representative for the mean and for both small and
large projects". So a sample can be representative on one statistic while being badly
unrepresentative on the strata it was drawn from — and "we selected a random sample, therefore
it is representative" is wrong as an inference.

**The gender-ratio example, walked through.** RQ: male-to-female ratio in open-source
development. Population: all open-source developers. Frame: open-source developers on GitHub.
Sample: 10% of GitHub developers via simple random sampling. Under this design a simple random
sample "would likely have (a lot) more male developers than female developers" — which is the
stated motivation for a two-stage design: split the data into subsets first (by gender, race,
bugginess, amount of testing, …), then sample independently from each subset.

**The snowball example, walked through.** Start from "core machine learning libraries (e.g.,
scikit-learn, TensorFlow, PyTorch)", then select what is imported by these libraries. The result
is "a sample representing what these libraries depend on". Note the direction of
representativeness: the sample represents the *dependency neighbourhood* of the seed libraries,
not open-source software at large.

**Cluster sampling in practice.** "Not papers on MSR from all highly ranked conferences (because
there are too many), but only from a subset of the conferences": divide into conference clusters,
sample some conferences, then draw papers from the selected clusters.

## Common Pitfalls

- **Assuming a random sample is representative.** "While there is a relation, it is not
  automatic." The frame is a subset of the population, and that difference is exactly where
  selection bias lives — so read the frame as the population only by accident.
- **Letting purposive criteria become convenience criteria.** "These criteria should not be based
  on convenience!"
- **Confusing the sampling designs.** "Stratified sampling uses all subsets, while cluster
  sampling uses only a subset." A random sample from a skewed population may under-represent the
  group you care about, which is when strata matter.
- **Treating representativeness as a requirement for interpretivist work.** Interpretivism
  "rather accepts that samples may be inherently biased and tries to account for that when
  interpreting data".
- **Omitting the sampling description from the paper.** The validity lecture's reliability
  threat is explicit: "Details about the data collection are missing such that a replication
  might collect different data leading to a different sample strategy".

## Connections

- [[msr-statistical-methods]] — inference inherits the representativeness of the sample.
- [[msr-research-paradigms]] — why positivism and interpretivism treat representativeness
  differently.
- [[grounded-theory]] — theoretical sampling and saturation as a purposive variant.
- [[threats-to-validity]] — sampling appears there as the "selection" internal-validity threat
  and the main external-validity threat.
- [[developer-social-networks]] — a population of developers whose sampling frame is a forge's
  user base.
- [[community-smells]] — studies that sample projects by popularity or activity patterns.
- [[evidence-based-software-engineering]] — the survey/case-study/experiment framing.
- [[mining-software-repositories-lecture-7]] — the source lecture for this page.

## Open Questions
- **The sampling methods are presented without any statistical guidance on sample size.** No
  power calculation and no rule of thumb for how many projects or developers a study needs
  appears.

- **"Bimodal" is used in the randomness-vs-representativeness example without being defined**, and
  the example gives means (2000 and 10000) rather than a distribution, so the exact conclusion
  about which sample is representative cannot be recomputed from the material.

- **The argument/problem table is partially garbled in the extracted slide text.** The "Breadth"
  row prints "Assumes large sample size, good sampling frame, and no bad lack", and several rows
  are misaligned between the two columns; the argument-to-problem pairing cannot be reconstructed
  with certainty from the slide as printed.

- **No criterion is given for when purposive sampling is "well-done"**, even though the validity
  lecture relies on that phrase (attributed there to Baltes & Ralph 2020) to defend a
  generalisability claim.

- **The boundary between stratified and quota sampling is drawn by the second stage's randomness**, but the slides never say what to do when the strata themselves are drawn non-randomly — the common case in practice.

- **Respondent-driven sampling's "strong mathematical controls" are named but not specified**, and no correction formula is given, so the slide cannot be acted on directly.

- **No guidance is given on sampling the *population* rather than the frame** — that is, on the case where the frame is itself a convenience artefact (e.g. GitHub for open-source developers), which is where the male/female example's sampling problem originates.
