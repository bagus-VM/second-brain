---
title: "Research Paradigms in MSR"
tags: [concept, mining-software-repositories, semester-2, research-paradigms]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[mining-software-repositories]]"]
---

## One-line Summary

The paradigm you adopt — positivism, interpretivism or pragmatism — decides how you frame the
research question, which methods you reach for, and what kind of answer counts as knowledge.

## Core Intuition

The lecture's opening statement is that "Research methods follow principal paradigms that shape
how we select methods and interpret data". The paradigm is not philosophy for its own sake; it
determines the shape of the study before any data is touched.

The three paradigms are given as short definitional sets:

**Positivism**
- "Reality is singular and can be objectively observed and quantified"
- "Knowledge is generated through the empirical observation of evidence"
- "Research should be value-free and only based on the results"

**Interpretivism**
- "Assumes that reality can only be partially known and is – to some degree – constructed in the
  minds of people"
- "Aims to understand subjective meanings that individual attach to their experiences"
- "Research should aim to gain a deep understanding of individual perspectives"

**Pragmatism**
- "Use methods best suited for problem"
- "Possibly also mix methods typically associated with positivism or interpretivism"

And a scope note: "We do not consider other paradigms (e.g., constructivism or critical realism)
here."

The relationship slide draws the distinction in a memorable pair of phrases: **"Measure to learn
objective truth"** for positivism, **"Understand individuals to learn subjective perspectives"**
for interpretivism, and for pragmatism **"Use whichever methods and perspectives are best suited
to address a research question"**. The same slide states: "While positivism and interpretivism
are mutually exclusive, pragmatism is flexible".

That flexibility is the pragmatic payoff: a pragmatist is allowed to do both halves of the
Chapter 7 methods block — statistics *and* grounded theory — within one research programme.

## Formal Definition / Statement

**MSR and the paradigms, as the lecture states it.**

*MSR research is typically positivistic:* "We collect data to measure properties of software
development. We analyze this data with the intend to come to some objective conclusions →
Typically quantitative research methods", e.g. "measuring the survival rate of developers within a
project to characterize turnover" and "measuring factors of developer involvement to characterize
survival rate".

*MSR research can also be interpretivist:* "We collect data about human behavior. We interpret
the data in its context to understand this behavior → Typically qualitative research methods",
e.g. "understanding how developers react to criticism in code reviews by analyzing review
comments" and "characterizing contributions of developers over time to understand their focus and
determine reasons why people left a project".

*Pragmatic MSR research allows for the combination:* "E.g., to create a quantitative model of
the survival rate and understand individual reasons for leaving projects".

**Formulating research questions.** "The way we formulate our research questions are
fundamentally tied to our research paradigms."

- Positivist research "frames research questions as hypothesis or variables to measure. The goal
  is to establish causal relationships or correlations between observed factors."
- Interpretivist research "typically has a rather open framing with the indent [intent] to rather
  explore meanings, experiences, and perceptions. The goal is to understand human behavior in a
  given context."
- "Pragmatism allows for both and their combination. E.g., trying to quantify behavioral patterns
  and establish causal relations and at the same time explore the human perspective on this
  relationship."

**Hypothesis and reasoning.** "A hypothesis is a testable statement that is derived from observed
data or an existing theory."

- *Confirmatory research* "tries to determine if a hypothesis holds. Deductive reasoning, i.e.,
  make predictions based on a hypothesis and see if these predictions holds. Typically
  positivistic, e.g., through the collection of data and testing if this data agrees with the
  hypothesis."
- *Exploratory research* "tries to understand a phenomon with the intent to derive new
  hypotheses. Inductive reasoning, i.e., make inferences from data and try to find generalizations
  that lead to hypothesis. Can be interpretivist or positivistic. Depends on the philosophical
  distinction if the resulting hypothesis should be generally true or rather about individual
  perspectives."

The slide diagrams this as a ladder: **Inductive reasoning** leads to *Exploratory research* →
*Observation or experiment* → *Generalization* → *Prediction* → *Confirmatory research*, with
*Deductive reasoning* running the other way.

**Falsifiability.** "A key property of scientific theories (and, as a consequence, hypotheses
derived from theories) is whether they are falsifiable." Consistent means "they agree with the
predictions of a theory"; inconsistent means "they cannot be explained by the theory".

The lecture's worked contrast on this point:

- Weak: "Nesting depth of source code is unrelated to readability of source code". "For this
  hypothesis, a single instance of spaghetti code with many loops and conditions would be
  sufficient to falsify this. However, we would not really have learned anything."
- Strong: "Nesting depth of source code is unrelated to the readability of source code by experts
  if it is less than or equal to two. This would study if a shallow nesting levels hinder the
  understanding of code by experts."

"Defining hypothesis in a manner that they are both falsifiable and such that this
falsification/non-falsification through observations is a critical tasks of the researcher!"

**Paradigm, theory, or hypothesis.** The slide carries this as a heading with the ladder
diagram and the word "hypothesis", positioning the three as levels on the inductive-to-deductive
axis: a paradigm frames the study, a theory supplies the mechanisms, a hypothesis is the testable
statement derived from it.

## Key Properties

- **The paradigm is upstream of the method, not a label applied afterwards.** "Research methods
  follow principal paradigms that shape how we select methods and interpret data."
- **Positivism and interpretivism are mutually exclusive; pragmatism is the escape hatch.**
- **Positivism is the default for MSR.** "MSR research is typically positivistic."
- **Interpretivism is explicitly available and not a lesser method.** It has its own example
  studies and its own framing style.
- **The two paradigms differ in their attitude to generalisation.** This becomes explicit in the
  sampling block: positivism needs representativeness; interpretivism "rather accepts that samples
  may be inherently biased and tries to account for that when interpreting data".
- **Paradigm choice propagates into the research question's syntax.** Hypotheses and variables
  versus open exploration of meanings and perceptions.
- **Exploratory and confirmatory are different reasoning directions, not different rigour.**
  Inductive reasoning builds generalizations from data; deductive reasoning tests predictions.
- **A hypothesis can be confirmatory or exploratory; it is not tied to one paradigm.**
  Exploratory reasoning "can be interpretivist or positivistic".
- **Falsifiability has a quality requirement beyond testability.** A hypothesis must be
  falsifiable *in a way that yields knowledge* — the spaghetti-code example is falsifiable and
  uninformative.
- **The exploratory path is itself a legitimate research design.** The lecture suggests it as an
  alternative to a badly framed hypothesis: "one could use an exploratory approach first to
  quantify the relationship between nesting and readability and then formulate a detailed
  hypothesis based on the results for a subsequent confirmatory study".
- **Grounded theory sits at the interpretivist end and relaxes the research-question
  requirement** — see [[grounded-theory]].

## Worked Example

**The same research problem under two paradigms.** Take "why do developers leave a project?".

- Positivist framing: measure the survival rate of developers within a project to characterize
  turnover, then measure factors of developer involvement to characterize that survival rate. The
  output is a model with an outcome variable, and the claim is about the population.
- Interpretivist framing: characterize contributions of developers over time to understand their
  focus and determine the reasons why people left a project — analysing review comments and other
  data "in its context". The output is an understanding of reasons from the inside.

**The pragmatic combination** is the slide's own example: "to create a quantitative model of the
survival rate and understand individual reasons for leaving projects". Note what it buys: the
quantitative part answers "how often", the qualitative part answers "why" — neither alone
answers both.

**The nesting-depth hypothesis** is the lecture's worked example of hypothesis quality. The weak
version ("Nesting depth of source code is unrelated to readability of source code") is falsified
by one piece of spaghetti code; the strong version adds two conditions — "by experts" and "if it
is less than or equal to two" — which turns it into a study of whether shallow nesting hinders
understanding of code by experts. The added qualifiers are what make the falsification
informative.

**The ladder** (inductive reasoning → exploratory research → observation or experiment →
generalization → prediction → confirmatory research) is the lecture's structural answer to "which
of these do I do first?" A study that starts from data and generalises upward is exploratory; a
study that starts from a prediction and works down is confirmatory.

## Common Pitfalls

- **Mixing paradigms in one study without saying so.** "While positivism and interpretivism are
  mutually exclusive", a study that is quietly both needs to be declared as pragmatic.
- **Writing a research question in the wrong register.** A positivist question phrased as "explore
  how developers experience X" has no measurable dependent variable; an interpretivist question
  phrased as "does X cause Y" ignores context.
- **Treating exploratory research as a weaker confirmatory study.** They use different reasoning
  directions; the inductive one is legitimate on its own terms.
- **Formulating trivially falsifiable hypotheses.** The lecture's example: one spaghetti-code
  instance refutes a sweeping claim, and "we would not really have learned anything".
- **Forgetting the role of the researcher when collecting data.** Under positivism research
  "should be value-free and only based on the results"; under interpretivism the researcher's
  interpretation is the instrument.
- **Assuming MSR must be quantitative.** The slides give qualitative MSR examples with the same
  status.
- **Skipping the exploratory phase to reach a crisp hypothesis.** The lecture recommends the
  exploratory-then-confirmatory sequence as a legitimate alternative to guessing.
- **Using grounding in literature as a neutral act.** Under interpretivism, exposure to theory
  shapes what is noticed; this is the problem [[grounded-theory]] is built around.
- **Confusing a paradigm with a method.** Statistics and grounded theory are methods; positivism,
  interpretivism and pragmatism are paradigms that select among methods.

## Connections

- [[msr-sampling]] — representativeness matters to positivism and is a non-issue to
  interpretivism.
- [[grounded-theory]] — the interpretivist theory-generation method the lecture selects.
- [[qualitative-coding]] — the mechanics of the human interpretation interpretivism relies on.
- [[msr-statistical-methods]] — the positivistic method family, and its assumptions.
- [[threats-to-validity]] — the structured way to check whether a study's claims survive.
- [[evidence-based-software-engineering]] — the survey/case-study/experiment framing the
  paradigm choice feeds into.
- [[developer-social-networks]] — a quantitative MSR area that is typically positivistic.
- [[mining-software-repositories]] — the course-level framing this page refines.
- [[mining-software-repositories-lecture-7]] — the source lecture for this page.

## Open Questions

- **The slides do not state how to choose a paradigm.** The choice is presented as upstream of
  everything else, yet no criterion for selection is given, and the pragmatic option blurs the
  distinction it is meant to solve.
- **"Paradigm, theory, or hypothesis" is a heading with no content.** The slide carries the
  ladder diagram and the word "hypothesis", but the lecture never defines what distinguishes a
  paradigm from a theory in operational terms, so the level structure has to be inferred.
- **The mutual exclusivity of positivism and interpretivism is asserted, not demonstrated.** No
  argument or citation is given for why the two cannot coexist within a single study, beyond
  pragmatism being the stated resolution.
- **The examples given for each paradigm are illustrative but not worked through.** No data,
  analysis or resulting claim is shown for the interpretivist examples, so it is not possible to
  see from the slides what an interpretivist "result" looks like in practice.
- **The exploratory-then-confirmatory sequence is recommended without a cost or design
  constraint.** Nothing states how the two studies should share data, whether the second is a
  separate sample, or what would count as a successful replication of the exploratory finding.
- **The falsifiability discussion is given entirely in the context of positivist hypotheses.** It
  is not said what the interpretivist equivalent of falsifiability is, even though the
  interpretivist framing is stated to be "rather open".
