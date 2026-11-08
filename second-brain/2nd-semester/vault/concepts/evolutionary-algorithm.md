---
title: "Evolutionary Algorithms"
tags: [concept, search-based-software-engineering, semester-2, evolutionary-computation]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[metaheuristics]]", "[[fitness-landscape]]", "basic vocabulary of genetics (gene, allele, chromosome, mutation)"]
---

## One-line Summary

An evolutionary algorithm keeps a population of candidate solutions and iterates
select → recombine → mutate → select, so several regions of the search space are explored in
parallel and worse solutions survive as genetic material rather than as a current state.

## Core Intuition

Local search carries one point. An evolutionary algorithm carries many, and that difference
changes what is possible: a bad individual can persist because it holds half of a good solution,
whereas a hill climber standing on a bad point must walk back downhill to get anywhere.

The lecture spends its first twenty slides on the biology before naming an algorithm, and the
borrowing is literal. Darwin supplies selection under scarcity: "individuals less suited to the
environment are less likely to survive and less likely to reproduce"; "evolutionary pressure (also
known as selection pressure)" is "anything that affects the reproductive success rate". Mendel
supplies the mechanism of inheritance, and the vocabulary that the algorithm then reuses:

- "Each gene encodes a different trait" and "an allele is a concrete value a gene can have".
- "Chromosome: a sequence of genes"; "genome: complete genetic information".
- "Genotype: genetic encoding of an individual"; "phenotype: the characteristic manifested by a
  specific genotype".

That genotype/phenotype split is the one that matters computationally: the search operates on the
encoding (genotype), the fitness function evaluates the decoded solution (phenotype). The lab
states the mapping explicitly for One Max: "a chromosome would in this case be the list, each
number in the list is a gene, and the alleles would be the actual values 0 and 1."

Two counter-theories are presented and then set aside, which is itself a warning about the
metaphor: Lamarck's "heritability of acquired characteristics" (learning during a lifetime being
inherited) is not how the algorithm works, and de Vries's mutationism / saltationism (large
evolutionary jumps) is the failure mode of a mutation operator tuned too aggressively. The
instructive corner case is the **Baldwin effect** — "a trait acquired through learning is replaced
by genetic traits through natural selection over generations" — which is exactly the shape of
genetic improvement and of neuroevolution later in the course.

## Formal Definition / Statement

**The general scheme**, from the lab's opening paragraph, and it is the check-list for any
implementation:

1. "Decide on some (genetic) encoding for our search problem."
2. "The algorithm acts on a population of individuals, initially usually generated randomly."
3. "A strategy of parent selection decides which individuals may reproduce", "usually influenced
   by the fitness of individuals".
4. "Recombination operators describe how parents are recombined, thereby merging genetic material
   from multiple parents."
5. "As part of recombination, mutation on the offspring may occur."
6. "Which of the parents and offspring represent the next generation is determined by a survivor
   selection strategy."
7. "There needs to be some criterion to decide on termination (e.g., fixed time or number of
   fitness evaluations)."

The lab's advice on choosing them: "1. Choose a representation that suits the problem at hand
2. Choose variation operators based on that representation 3. Choose selection operators, which are
independent of representation."

**The naming convention for evolution strategies** is (μ/ρ + λ) or (μ/ρ , λ): μ parents, ρ
individuals involved in recombination, λ offspring, and `+` (parents and offspring both eligible as
survivors) versus `,` (only offspring eligible). The lab derives it in that order: (1+1) → (1+λ) →
(1,λ) → (μ+λ) → (μ,λ) → (μ/2+λ) → (μ/2,λ).

**Evolution strategies** were "developed in the 1960s and 1970s by Ingo Rechenberg and Hans-Paul
Schwefel", and "canonical evolution strategies mainly use selection and mutation". For a bitstring
the mutation is stated exactly: "Given a vector of length n, each element is changed with
probability 1/n. On average, one element will thus be changed. However, it may also happen that
more or fewer elements are changed." The trade-off behind that choice: "If the changes are too
small, this inhibits the exploration aspect of the algorithm; if the changes are too large, this
may inhibit exploitation."

**Genetic algorithms** differ from evolution strategies in the lab's own accounting: "evolution
strategies manipulate the phenotype directly … genetic algorithms traditionally act on a genetic
encoding (usually binary encoding), and the fitness is evaluated on the decoded phenotype"; and
"in our evolution strategies, parents are chosen uniformly at random … and the deterministic
truncation survivor selection (keep the best μ) is what drives the search. In a canonical, simple
Genetic Algorithm, parent selection instead is fitness-based and probabilistic, typically applied
to larger populations."

**Terminology of the schedule** used in the lab: generational GA (a whole offspring population
replaces the parents) versus steady-state GA ("one offspring (or pair of offspring) is generated
per generation and one member of population is replaced"); elitism ("a certain share of the best
individuals of one generation survives unchanged"); tournament selection ("for a given number of
individuals (the tournament size) we randomly select individuals from the population … the best of
these individuals wins the tournament").

## Key Properties

**History is a straight line of named contributions**, worth knowing because the course asks for
origins: 1948 Turing proposes "genetical or evolutionary search"; 1962 Bremermann, optimisation
through evolution and recombination; 1964 Rechenberg, evolution strategies; 1965 Fogel, Owens and
Walsh, evolutionary programming; 1975 Holland, genetic algorithms; 1992 Koza, genetic programming.

**Comma selection is preferred in practice, for two stated reasons.** "The (μ,λ)-selection is often
preferred in practice because it is better at leaving local optima as well as following moving
optima." The cost is stated with it: the lab notes the caveat that with comma selection the
best-so-far value "may differ from the fitness of the current population" — the current population
can be worse than anything seen before, so the reported result must be the best evaluated
candidate, not the best final individual.

**Genotype/phenotype separation is a design decision, not a given.** For One Max "the difference is
rather irrelevant, since our phenotype is a bitstring" — but genetic programming (later in the
course) searches programs, where the encoding and the evaluated artifact are the same object.

**Measured result on One Max (n = 100, 1000 evaluations, 30 runs):** "the (1+1)ES and the (μ/2+μ)ES
both reach a higher final fitness than the GA over 30 runs; both differences are significant, with
large effect sizes (A12 of about 0.95 and 0.85). Between the (1+1)ES and the (μ/2+μ)ES, the test
finds no significant difference, and the A12 interval includes 0.5. This does not mean that they
perform the same: we simply have no evidence of a difference. We only looked at one particular
configuration of search operators for the GA, and varying the parameters and operators may lead to
entirely different results."

## Worked Example

**The (1+1)ES in full**, since it is the smallest complete evolutionary algorithm:

- Population of two: "the current point (parent) and the result of its mutation (offspring)".
- "Parent selection is therefore easy – there is only one parent."
- "Survivor selection chooses the mutant as the next parent if its fitness is at least as good as
  the parent's fitness, otherwise the parent survives and the mutant is disregarded."
- Mutation: each of the n bits flipped with probability 1/n.

Note what this is: a hill climber on a random 1-bit neighbourhood, with equal-fitness acceptance.
That is the reason the course introduces it first — it makes the evolutionary machinery visible
without the population.

**The generational GA's parameters**, as the lab sets them:

| Parameter | Value | What it controls |
|---|---|---|
| population size | 20 | how many basins are held in parallel |
| elite size | int(20 · 0.05) = 1 | best individual survives unchanged |
| P_xover | 0.7 | probability that two parents are recombined rather than copied |
| parent selection | tournament, size 5 | how strongly fitness biases reproduction |
| crossover | single-point | where genetic material is cut and swapped |

The loop is: elitism seeds the next population → repeat {draw two parents by tournament, cross
them with probability P_xover, mutate each child, evaluate} until the new population is full →
replace. Evaluation budget is shared with initialisation, and "every call counts, even for a
repeated bitstring."

**The comparison that fails to separate two variants, and what the lab says about it**: the
steady-state GA replaces "the worst member of the population, but only if the offspring is at
least as good as it, so the population's best individual is never lost", and on One Max the test
cannot distinguish it from the generational GA (p = 0.3549, A12 = 0.56 with interval [0.43, 0.70]).

**One Max versus Leading Ones, measured.** Both are unimodal; the difference is neutrality. At
fitness 10 on n = 100: One Max has 90 improving, 0 neutral, 10 worsening neighbours; Leading Ones
has 1 improving, 89 neutral, 10 worsening. "At k leading ones its probability of improvement is
exactly" the probability that mutation flips the first zero and preserves the leading ones, so
"for n = 100, the expected wait for an improvement ranges from 100 evaluations near the start to
about 270 near the optimum" — against steepest-ascent hill climbing's 100 evaluations per
accepted move. And the summary statistic: "One Max: median neutral fraction 0.000, median
autocorrelation 0.980; Leading Ones: median neutral fraction 0.980, median autocorrelation 0.971."

## Common Pitfalls

- **Reporting the best member of the final population.** With comma selection that is not the
  best solution found; the result is the best evaluated candidate.
- **Losing the best individual.** Without elitism (or without the "only replace if at least as
  good" rule of the steady-state GA) the population's best can be overwritten.
- **Mutation rate confused with mutation operator.** In the ES the rate is inside the operator
  (1/n per gene); in the GA it is a separate parameter. Mixing the two makes experiments
  incomparable.
- **Charging selection for fitness evaluations.** Tournament selection should compare stored
  scores: "Tournament selection returns an (individual, score) pair and compares the stored scores,
  so selection uses no additional fitness evaluations."
- **Assuming a population solves neutrality.** The Leading Ones result shows an ES spending most
  of its budget on neutral moves; population size does not create a gradient.
- **Tuning parameters on one instance and generalising.** The lab's own caveat: "We only looked at
  one particular configuration of search operators for the GA."
- **Believing the biology is the algorithm.** Lamarckism and saltationism are described precisely
  so that the differences are visible; the algorithm is Darwinian and gradualist.

## Connections

- [[metaheuristics]] — the general properties, plus the representation/operator/fitness triad.
- [[fitness-landscape]] — neutrality, autocorrelation and the One Max vs Leading Ones contrast are
  landscape measurements.
- [[hill-climbing]] — the (1+1)ES is a stochastic hill climber; the comparison is direct.
- [[search-algorithm-evaluation]] — every claim in the "Measured result" section comes from that
  procedure (30 runs, common seeds, Mann-Whitney, Â12, Holm).
- [[sbse-paradigm]] — where genetic improvement, code transplantation, neuroevolution and FunSearch
  fit.
- [[search-based-software-engineering-lecture-3]] — the deck and lab that present this.

## Open Questions

- **The lecture's slides stop at the history of evolutionary computation** — the deck
  (`4_EvolutionaryAlgorithms_Part1.pdf`, 26 slides) covers Lamarck, Darwin, Mendel, genetics,
  mutation, drift, memetics and the timeline, and the algorithm content lives only in the Jupyter
  lab. There is no slide-level statement of selection operators to revise from.
- **Parameter defaults (population 20, elite 5 %, P_xover 0.7, tournament 5) are labelled "common
  default values"** without a source, and the tuning chapter is still to come.
- **Whether steady-state or generational is preferable** is not decided by the One Max experiment.
- **The genotype/phenotype distinction's cost** (decoding overhead, invalid phenotypes after
  crossover) is asserted to be irrelevant here and is not discussed for cases where it is not.
- **No repair operator** is described for offspring that violate constraints, although
  metaheuristics generally require feasible solutions.