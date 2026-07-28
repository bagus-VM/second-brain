---
title: "Finite Automata"
tags: [concept, software-analyse, formal-methods, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*Abstract computational models with a finite set of states, used in compiler design, pattern matching, and program analysis.*

## Core Intuition
Finite automata are the simplest computational model — a machine that reads input one symbol at a time and transitions between a finite number of states. Despite their simplicity, they're incredibly powerful: regular expressions, lexical analyzers, network protocols, and many program analyses are all fundamentally finite automata. Understanding them is understanding the foundation of computation theory.

## Formal Definition / Statement
A finite automaton (FA) is a 5-tuple (Q, Σ, δ, q₀, F) where:
- Q = finite set of states
- Σ = input alphabet
- δ = transition function: Q × Σ → Q (deterministic) or Q × Σ → P(Q) (nondeterministic)
- q₀ ∈ Q = initial state
- F ⊆ Q = accepting/final states

**Types:**
1. **DFA (Deterministic FA)**: Exactly one transition per input symbol per state
2. **NFA (Nondeterministic FA)**: Multiple transitions possible; accepts if ANY path accepts
3. **ε-NFA**: NFA with epsilon (empty) transitions
4. **Moore Machine**: Output associated with states
5. **Mealy Machine**: Output associated with transitions

**Equivalence:** DFA ≡ NFA ≡ ε-NFA (all recognise regular languages)

**Key theorems:**
- Kleene's theorem: A language is regular iff it's recognized by a FA
- Pumping lemma: If L is regular, there exists p such that any w ∈ L with |w| ≥ p can be written as w = xyz where |xy| ≤ p, |y| > 0, and xyⁱz ∈ L for all i ≥ 0
- Closure properties: regular languages are closed under union, intersection, complement, concatenation, Kleene star

**Applications in program analysis:**
- Control flow graphs are essentially NFAs
- Dataflow analysis uses lattice-based automata
- Model checking uses Büchi automata (ω-automata for infinite strings)
- Type systems can be modeled as finite automata

## Key Properties / Complexity
- DFA recognition: O(n) time, O(1) space (just current state)
- NFA to DFA conversion: potentially exponential state explosion (2^n states)
- Minimization: every DFA has a unique minimal equivalent DFA
- Regular expressions ≡ NFAs ≡ DFAs (three equivalent representations)
- Cannot count (no memory beyond current state) — cannot recognise {aⁿbⁿ}
- Decidable problems: emptiness, finiteness, equivalence, membership

## Worked Example
Lexical analysis of a simple language using a DFA:

Tokens: `if`, `id` (identifier), `num` (number)

DFA states:
- q0: start state
- q1: reading 'i' (could be 'if' or start of identifier)
- q2: reading 'f' after 'i' → keyword 'if' (accepting)
- q3: reading identifier characters after 'i' (not 'f') → identifier (accepting)
- q4: reading digits → number (accepting)

Input: `if x42`
- q0 → 'i' → q1
- q1 → 'f' → q2 (accept: token = 'if')
- q0 → ' ' → q0
- q0 → 'x' → q3 (accept: token = 'id')
- q3 → '4' → q3
- q3 → '2' → q3 (accept: token = 'id')

## Common Pitfalls
- **DFA vs NFA**: NFAs are easier to construct but DFAs are faster to execute
- **State explosion**: Converting complex regex to DFA can create millions of states
- **Not context-free**: FA cannot handle nested structures (matching parentheses)
- **Over-approximation**: Using FA for program analysis may produce false positives
- **Infinite state systems**: Real programs have potentially infinite state spaces; FA require finite abstraction

## Connections
- [[abstract-interpretation]] — Finite automata are used in abstract interpretation frameworks
- [[basic-block]] — Control flow graphs are automata over program states
- [[data-flow-analysis]] — Dataflow facts propagate through automaton-like structures
- [[monotone-framework]] — Generalizes dataflow analysis using lattice theory
- [[common-subexpression-elimination]] — Uses available-expressions analysis (automaton-based)
- [[liveness-analysis]] — Backward dataflow analysis on control flow automaton

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
