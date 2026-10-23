---
title: "Qualitative Coding and Inter-Rater Agreement"
tags: [concept, mining-software-repositories, semester-2, qualitative-methods, coding]
course: "Mining Software Repositories"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

Coding is the assignment of labels to data by humans, and the machinery that makes such labels
trustworthy — multiple raters, agreement statistics, and the choice between closed and open coding
— is what separates qualitative data from anecdotes.

## Core Intuition

The lecture's own framing is that MSR has been doing qualitative coding all along without naming
it. "Coding of data means to assigned codewords (=labels) to data. We already did this! Validation
if an issue is a bug is a type of coding." The rest of the chapter is the quality engineering of
that act.

The first intuition is that coding is a *human* activity and therefore inherits human failure
modes. The slide "Dealing with human biases and noise" lists three: "Humans are imperfect"; "We
make random mistakes"; "We make actual mistakes — Due to lack of skill or missing important
information". And a fourth that is not a mistake at all: "Reasoning and interpretation may be
different between individuals — Does not automatically mean that one may be right". Hence the
requirement: "Needs to be accounted for when humans code data!"

The second intuition is that one rater is not enough. "Using multiple raters to conduct the same
tasks helps to prevent noise and deal with biases." The third is that agreement between raters is
itself a *measurement*: "How often raters agree with each other important to understand validity of
data. Many agreements mean that the likelihood of noise and bias is reduced — (Unless all raters
would make the same mistakes and have the same biases)."

The fourth intuition is the choice between fixing the categories in advance and letting them
emerge: deductive coding "works with a fixed and pre-defined codebook", inductive coding "works
with a dynamic code book that can be extended by the raters".

## Formal Definition / Statement

**The objects.** "Qualitative analysis considers the interpretation of data (e.g., text, images) by
humans." "Coding of data means to assigned codewords (=labels) to data." "The codewords are
maintained in a codebook." "Humans assigning the codewords to data are called raters."

**Multiple-rater strategies.** The slide names four, and "Many strategies possible, depend on data,
task, and required accuracy of data":

1. *Majority label.* Raters "assign labels for the same task and assign the majority label". It
   "Works well if there are few labels (ideally binary)"; with many categories, "many raters per
   label" are needed to find a reasonable majority.
2. *Agreement threshold.* Raters "define a requirement for agreement — E.g., use four raters and
   require that at least three raters agree". It "Needs to define what happens with data without
   agreement".
3. *Consensus meeting.* Raters "assign label if all agree and require additional meeting to achieve
   consensus for all others" — a "Very strict criterion that should greatly reduce noise", but
   "Effort is higher than for other strategies, because achieving consensus requires meetings".
4. *Mean over a Likert scale.* "When labels can be mapped to a Likert scale, it may also be
   possible to calculate a mean value over multiple raters as final label."

**Inter-rater agreement.** "Statistical approaches to measure inter-rater agreement exist."
Disagreements have "various reasons": "Difficult task with a high error rate"; "Active disagreement
between raters, because they judge data differently"; "Biases affect ratings leading to
differences". "Studying where disagreements occur can also be an interesting research subject — E.g.,
for which aspects developers agree and where (and why?) they disagree." The related but distinct
concept is "intra-rater agreement, i.e., how robust is the rating by a person", with the scope note
"We do not consider the differences between inter- and intra-rater reliability in this lecture".

**Cohen's κ.** "Measures the agreement between two raters when assigning k different nominal
labels." With N the number of ratings and n_i^j the number of ratings in category i by rater j:
p₀ = agreements / N; p_e = (1/k) Σᵢ₌₁ᵏ (n_i¹ n_i²) / N²; and
κ = (p₀ − p_e) / (1 − p_e) (Cohen 1960).

**Interpretation of κ.** "Usually based on a table from Landis and Koch" — "Not universally
accepted!" — because it "Does not take into account that agreement is usually higher with less
categories". As printed: κ ≤ 0 "Poor agreement"; (0, 0.2] "Slight agreement"; (0.2, 0.4] "Fair
agreement"; (0.4, 0.6] "Moderate agreement"; (0.6, 0.8] "Substantial agreement"; (0.8, 1.0] "Almost
perfect agreement" (Landis & Koch 1977).

**Beyond Cohen's κ.** "Fleiss' κ generalizes the concept of Cohen's κ to more than two raters";
"Krippendorf's α generalizes the concept of Cohen's κ to any number of raters, incomplete data, and
different scales (e.g., ordinal, interval, ratio)"; "Cronbach's α is a correlation-based approach
that can take the difference between ratings into account" — 8 is more similar to 7 than to 1.

**Deductive coding (closed coding).** "Works with a fixed code book" and "Requires good knowledge
about categories before execution of the coding — E.g., rate sentiment as happy, sad, or neutral."
It "Makes definition of the categories part of the study design"; in that example, "other
sentiments, like anger, would be ignored". It "Helps to focus coding to specific tasks" but
"Limits coding to foreseen values which may lead to overlooking relevant aspects."

**Inductive coding (open coding).** "Raters can add new codes", from an initial codebook that is
extended or from an empty one. "Raters need guidance what sort of codes should be used → Key part of
the study design, otherwise anything could be result." "Codes can be flexibly adjusted based on what
is within the data", and there is "Usually more effort than closed coding."

**Harmonizing open codes.** "Two raters may use different codes to describe the same concept" — one
calls teaching materials PowerPoint, the other Slides. This leads to "underestimation of inter-rater
agreement" and to "overlooking aspects in subsequent analysis, because data is in different
categories when it should be the same". "Harmonizing codes means that such differences are resolved
by replacing codes with a unified representation." It "Requires discussion between raters", and can
be done "at fixed intervals" or "after the fact". Raters can also initialize the codebook together
by rating a percentage of the data together, which "pre-fills codebook with entries that will be
used consistently, but no independent ratings for these elements".

**Axial coding.** "Process of relating codes to each other. Can be interpreted as coding of codes."
"Models the relationships between codes. Requires a strategy, same as the initial coding." Grouping
codes "on the same level of abstraction as alternative to harmonization" preserves the original code
works; grouping on "different levels of abstraction to interpret information — E.g., group codes
Slides and Coding Exercise into code Materials". "This is the core concept on which the qualitative
analysis methodology grounded theory is build".

**From the methods lecture.** Open coding is to "Analyze the data and inductively identify concepts …
Concepts are described by code words"; axial coding is to "Identify relationships between the
categories". A Straussian research question "could be Developed during the coding process; Defined
beforehand based on a clear objective; Derived from existing literature", and such questions "are
typically more open and generic than those for positivitic research". Coding can reveal "the need for
more data … To get more data for specific categories" — "theoretical sampling", "a type of purposive
sampling" — which "stops once theoretical saturation is reached".

## Key Properties

- **Coding is a labelling act with a documented vocabulary.** The codebook is the artefact that
  makes the labelling reproducible; without it, the labels are private.
- **Reliability is a design decision, not a post-hoc statistic.** Which of the four rater strategies
  is used determines both cost and error profile: majority voting is cheap but needs few
  categories, consensus meetings are strict and expensive, thresholds need an explicit rule for
  non-agreement, and Likert means need an ordinal scale.
- **Agreement is a measure of the data's validity, and it has a stated limit.** Many agreements
  reduce the likelihood of noise and bias "Unless all raters would make the same mistakes and have
  the same biases" — shared bias is invisible to the statistic.
- **κ is a chance-corrected statistic for two raters and nominal labels.** Its weakness is
  structural: chance correction is weaker with fewer categories, which is why the interpretation
  table is "Not universally accepted".
- **Disagreement is diagnostic.** The three listed causes are distinguishable in principle — task
  difficulty, genuine interpretive difference, bias — and the lecture treats disagreement locations
  as a research topic in their own right.
- **Closed and open coding trade focus against coverage.** Closed coding "Helps to focus coding to
  specific tasks" but "Limits coding to foreseen values"; open coding is more flexible but "Usually
  more effort" and, without study-design guidance, risks anything being coded.
- **Harmonisation is a distinct act from coding, needed precisely because the codebook is
  dynamic.** Two codes for one concept understate agreement and hide the data from later analysis.
  Axial coding is the related move: "Process of relating codes to each other", which "turns a bag
  of labels into a structure".

## Worked Example

Take the deck's teaching-materials example and run it through the mechanics.

*Step 1 — coding.* Two raters read the same teaching materials. Each assigns codewords. Under
**closed coding**, the codebook is fixed beforehand (say: happy, sad, neutral) and the sentence
"the lecturer was furious" is coded as neutral or left awkward, because "other sentiments, like
anger, would be ignored". Under **open coding**, the rater finds that no code covers it and
extends the codebook. The study design must bound this: "codes related to sentiment should be
assigned", otherwise "anything could be result".

*Step 2 — harmonising.* Rater A wrote *PowerPoint* for a deck; rater B wrote *Slides* for the same
deck. Left unresolved, inter-rater agreement is underestimated, and the materials sit in two
categories when they belong in one. The fix is a discussion between raters replacing one codeword
with the other. The alternative is not to replace but to relate: axial coding groups *Slides* and
*Coding Exercise* under a new, more abstract code *Materials*, keeping both codewords intact.

*Step 3 — rating with agreement.* Suppose the categories are the three labels and the data is
judged by four raters. The threshold strategy applies: "use four raters and require that at least
three raters agree", and the study must state "what happens with data without agreement". If the
labels are instead "how much does this applies" on a Likert scale, the final label is the mean
over raters.

*Step 4 — measuring agreement.* With two raters and k nominal labels, compute p₀ and p_e, then
κ = (p₀ − p_e)/(1 − p_e). The Landis–Koch table maps the result onto "Poor agreement" through
"Almost perfect agreement". With more than two raters, or with ordinal scales, or with incomplete
data, the slide points to Fleiss' κ, Krippendorf's α and Cronbach's α instead.

*Step 5 — collecting more data.* Where the coding reveals a gap — a category with two ratings, a
question the data does not answer — the study collects more data for that category. That is
theoretical sampling, and it ends when new data "is no longer added information and leading to
revisions of the theory".

## Common Pitfalls

- **Coding with one rater and calling the result data.** "Humans also make mistakes. Usually
  requires multiple people to clean to data, to achieve best results. Otherwise, some bias may be
  left."
- **Using the majority strategy with many categories.** With many labels, "many raters per label"
  are needed to find a reasonable majority — the strategy degrades as the codebook grows.
- **Leaving the non-agreement case undefined.** A threshold strategy without a rule for unratable
  data silently drops the hardest items, which are usually the interesting ones.
- **Reading κ as a quality score without its assumptions.** Two raters, nominal labels, chance
  correction; a high value with two categories means less than with five.
- **Treating high agreement as proof of correctness.** Agreement is reduced by noise and bias
  "Unless all raters would make the same mistakes and have the same biases".
- **Running open coding without study-design guidance.** "Key part of the study design, otherwise
  anything could be result".
- **Forgetting harmonisation because the codebook was dynamic.** Two spellings of one concept
  corrupt both the agreement statistic and the downstream analysis.
- **Confusing intra-rater agreement with inter-rater agreement.** "How robust is the rating by a
  person" is a different question, and the lecture explicitly excludes it.
- **Using Cohen's κ where Fleiss' κ, Krippendorf's α or Cronbach's α is needed.** The extensions
  exist for more raters, for incomplete data, and for non-nominal scales.
- **Calling the sum of steps a theory.** Building theory from coded data is the job of the
  grounded-theory method, covered on [[grounded-theory]].

## Connections

- [[qualitative-coding]] — this page.
- [[grounded-theory]] — the method that uses open and axial coding to build a theory.
- [[msr-data-noise]] — manual cleaning as an option for handling heuristic noise.
- [[mining-software-repositories]] — the pipeline whose enrichment step depends on coded labels.
- [[threats-to-validity]] — where rater disagreement enters the validity argument.
- [[msr-sampling]] — the sampling frame that manual validation and theoretical sampling draw on.
- [[msr-statistical-methods]] — the statistical machinery behind the agreement coefficients.
- [[community-smells]] — the smells first identified through open and axial coding of interviews.
- [[evidence-based-software-engineering]] — the evidence framing that motivates measurement
  quality.
- [[msr-research-paradigms]] — the positivist/interpretivist split the coding styles belong to.

## Open Questions

- **The lecture reports no κ values of its own.** The formula and the interpretation table are
  given, but no worked dataset with raters, no computed κ, and no example of an agreement level
  considered acceptable for a study.
- **No guidance is given on choosing between the four rater strategies.** The strategies are listed
  with their trade-offs, but no rule maps "required accuracy of data" or task type onto a
  strategy, and the number of raters is left to the researcher.
- **The intra-rater agreement question is deliberately left open.** The lecture states it will not
  consider the differences between inter- and intra-rater reliability, so the stability of a single
  rater over time is not addressed anywhere in the source.
- **The Landis–Koch threshold is borrowed, not defended.** The slide says the table is "Not
  universally accepted" and explains why, but offers no alternative criterion for the same
  decision, and harmonisation's cost is left unquantified.
