---
title: "Search-Based Software Engineering (the paradigm)"
tags: [concept, search-based-software-engineering, semester-2, foundations]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[metaheuristics]]", "software engineering as a discipline (testing, requirements, design, project management)"]
---

## One-line Summary

Search-based software engineering treats software-engineering problems as optimisation problems —
you define a representation, a fitness function and move operators, and let a metaheuristic search
— and it is not search engines or code search.

## Core Intuition

The lecture's framing is a gap in the engineering disciplines. Bridges have theory (stress, tensile
strength), simulation and optimisation; software engineering has theory (best practices) and, in
the slide's grid, question marks where simulation and optimisation should be, and a "real world"
product column nobody can compute. SBSE is an attempt to fill the optimisation cell by pretending
— honestly — that a program's quality can be measured, so that search can be applied to it.

Two consequences follow, and the course builds on both:

1. **The fitness function is the design problem.** A metaheuristic needs only that "f(x) can be
   computed for all x ∈ S"; so what makes an SBSE problem solvable is a computable measure of
   "how good is this test suite / schedule / refactoring / program".
2. **The measure is usually a proxy.** Coverage, mutation score, distance travelled, defect count —
   never the business outcome. This is the same observation the repository-mining course makes
   about tools built on mined data.

The negative definition matters as much as the positive one: SBSE is "NOT search engines or code
search". It is optimisation applied to software engineering, not the use of search engines in
software engineering.

## Formal Definition / Statement

The slide's definition, verbatim: SBSE is "a large movement(?) that seeks to apply various
optimisation techniques to software engineering problems (NOT search engines or code search)",
"still relatively young (by academic standards)", with the SEBASE publications repository
(http://crestweb.cs.ucl.ac.uk/resources/sbse_repository/) as its literature index.

**The founding paper** is presented as such: Webb Miller and David L. Spooner, "Automatic
Generation of Floating-Point Test Data", *IEEE Transactions on Software Engineering*, Vol. SE-2,
No. 3, September 1976. Its own abstract states the strategy: "it may be that large savings of time
and storage are made possible by using numerical maximization methods instead of symbolic
execution to generate test data", and it is "heuristic" in the sense "that it is not guaranteed to
produce a set of test data executing a given path whenever such data exist". That is SBSE in 1976:
a software-engineering task (test-data generation) reformulated as numerical optimisation.

**The key ingredients**, which the lecture states on one slide and then reuses for every example:
"what are we going to try this time? (representation)"; "how is it different from what we tried
before? (operators)"; "how well did we do this time? (fitness/objective function)"; and "minor (but
critical) ingredients: constraints".

**The problem domains the deck surveys**, with the slide's own examples:

| Domain | The problem as the slide states it |
|---|---|
| Structural testing | automatic test-data generation — the 1976 origin |
| Search-based testing (SBST) | Daimler's autonomous parking system: input space width, gap, space length, dist2space → a fitness driven from "collision" towards "critical" over generations |
| Requirements engineering | next release problem — "given cost and benefit (expected revenue) for each feature, what is the best subset of features to be released for budget B?" — which "is 0-1 Knapsack (NP-complete)", though "release decisions are more political than NP-complete" |
| Project management and planning | quantitatively simulate the communication overhead (linear? logarithmic?) and "search for the tradeoff between overrun risk, project duration, and amount of overtime assignment" (Harman, Mansouri & Zhang, *Search-based software engineering: trends, techniques and applications*, ACM CSUR 45(1), 2012) |
| Design / architecture / refactoring | "cluster software models to achieve certain structural properties (cohesion/coupling)" |
| Genetic improvement | "given a source code, can we automatically improve its non-functional properties (such as speed)?" |
| Code transplantation | "software X has feature A, which you want to have in software Y. Can we automatically extract and transplant feature A from X to Y?" (Barr, Harman, Jia, Marginean & Petke, ISSTA 2015) |
| SBSE + LLMs | FunSearch (Romera-Paredes et al., *Mathematical discoveries from program search with large language models*, Nature, 2023) and AlphaEvolve |

## Key Properties

**Every domain is reframed, not solved.** The parking example's fitness is not "is the car
parked?" but a graded function that starts at "collision" and moves towards "critical" over
generations — a distance, exactly as in the artificial x + y = 10 example. The requirements
example's fitness is revenue under a budget constraint. The refactoring example's fitness is
cohesion/coupling. In each case the software-engineering artifact supplies the representation and
the metric supplies the gradient.

**The proxy problem is inherited from measurement, not from search.** "Testing: quality of
submission — your responsibility (i.e., write test cases!)", and "part of the grade for an
assignment will be determined by testing (e.g. coverage, mutation score)". The course grades its
own assignments with the same class of measure it teaches.

**FunSearch is the modern shape of the idea, and it is a search over programs.** The Nature paper's
own summary in the deck: FunSearch "combines a pretrained (frozen) LLM, whose goal is to provide
creative solutions, with an evaluator, which guards against confabulations and incorrect ideas";
"in contrast to most computer search approaches, FunSearch searches for programs that describe how
to solve a problem, rather than what the solution is." The evaluator is the fitness function, and
its role — guarding against plausible-but-wrong output — is the same role the fitness function
plays in every other SBSE application.

**Baldwin-style learning-to-genes is the mechanism behind genetic improvement** (see
[[evolutionary-algorithm]] for the Baldwin effect): a fix discovered by a developer, encoded into
the program, becomes heritable material for the next search.

## Worked Example

**The Daimler parking system, as the deck presents it.** The input space is parameterised (space
width, gap, space length, dist2space); a fitness function is defined over it; search proceeds by
generation, and the slides show the population moving from "Generation 0" through 10 and 20 as the
fitness improves from "collision" towards "critical". The point of the example is not the algorithm
— it is that a physical, safety-relevant system behaviour was turned into a number that a
metaheuristic can climb, which is what makes it a *search-based* testing problem.

**The same three ingredients across two representations** (Super Mario, from the introduction):
search over input tuples (button, start_time, end_time) with operators that change the button type
or shift the times; or search over a neural network with operators that change weights or
structure. Identical fitness — "the distance you travelled without dying" — and a completely
different search space. That is the paradigm in one slide: representation is a free choice, and the
only thing tying the variants together is the measurable objective.

## Common Pitfalls

- **Confusing SBSE with code search or search engines.** The slide's parenthetical exists because
  the confusion is common.
- **Reporting coverage or mutation score as if it were the goal.** It is the proxy; a test suite can
  maximise it and still be useless for the failure you care about.
- **Assuming NP-hardness is the interesting part.** The requirements slide says it directly:
  "release decisions are more political than NP-complete" — the hard part is often the objective,
  not the combinatorics.
- **Forgetting constraints.** They are labelled "minor (but critical)": an unconstrained optimum is
  usually not a deliverable (a test suite that violates the budget, a schedule with no resources).
- **Treating LLM-based program search as a different field.** FunSearch/AlphaEvolve are presented
  as this paradigm with a generative operator, guarded by an evaluator.
- **Believing the fitness function is neutral.** It defines what the search will exploit; a badly
  designed one is optimised into nonsense.

## Connections

- [[metaheuristics]] — the algorithms the paradigm borrows.
- [[fitness-landscape]] — the geometry a chosen representation and fitness create.
- [[evolutionary-algorithm]] — the workhorse used by genetic improvement, neuroevolution and
  FunSearch.
- [[search-based-software-engineering-lecture-1]] — the deck this page summarises.
- [[mining-software-repositories]] — the sibling course that also turns software artifacts into
  measurable data; MSR measures, SBSE optimises.
- [[machine-learning-for-cybersecurity]] — another course where a proxy metric (classification
  accuracy, ROC) stands in for the real objective.
- [[evidence-based-software-engineering]] — the same insistence that decisions be measurable.

## Open Questions

- **The slide calls SBSE "a large movement(?)"** with the question mark printed — the deck itself
  is unsure whether the field coheres, and nothing in the material resolves that.
- **No mapping is given from a software-engineering problem to a fitness function**; every example
  arrives with its metric already chosen.
- **The validity of the proxy metrics** (coverage, mutation score) is asserted, not examined, in
  this course — though the same questions appear in [[threats-to-validity]] elsewhere in the
  semester.
- **AlphaEvolve is named without a citation or a description** in the extracted slides, unlike
  FunSearch.
- **What "constraints" means operationally for each domain** is never spelled out beyond the word.