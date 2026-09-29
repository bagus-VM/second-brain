---
title: "Software Analyse — Lecture 2: Tokens and Naturalness of Code"
tags: [topic, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [code-clones]
---

## One-line Summary
Lecture 2 bridges compiler front-ends (lexical analysis, tokenization) with NLP applied to source code, introducing n-gram language models and the code naturalness hypothesis.

## Core Intuition
This lecture connects two worlds: (1) how compilers convert raw characters into tokens (the engineering), and (2) how those tokens exhibit statistical regularities similar to natural language (the science). The token stream — produced by the [[lexical-analysis]] phase — is not just input for the parser but also for statistical models that can predict code, detect bugs, and measure quality.

## The Big Picture

### Compiler Front-End
The lecture opens with the compiler toolchain context:
- Preprocessor → Compiler → Assembler → Linker
- Compilation = analysis (→ AST) + synthesis (→ target code)
- Interpretation vs compilation (including bytecode + JVM)

### Lexical Analysis
[[lexical-analysis]] — the first phase of compilation:
- A pattern matcher for character strings
- Converts character stream → token stream
- Mathematically: a [[finite-automata-and-regular-expressions|finite automaton]] based on regular grammar
- Separated from parsing for simplicity, efficiency, portability

### Tokenization
[[tokenization-and-token-types]] — the output of the lexer:
- Token = category name (IDENT, INT-LIT, ASSIGN-OP, …)
- Lexeme = actual character string ("result", "42", "=")
- Reserved words handled via table lookup on IDENT tokens

### Regular Expressions and Finite Automata
[[finite-automata-and-regular-expressions]] — the mathematical foundation:
- Regular expressions define token patterns
- Finite automata (DFA/NFA) implement the matching
- Every regex ↔ equivalent DFA (regular language equivalence)

### Lex/Flex
[[lex-and-flex]] — practical lexer generators:
- Regex specifications → DFA-based C code
- Three-section format: declarations, rules, C code
- Longest match + first rule tie-breaking

### CCFinder
[[ccfinder]] — token-based code clone detection:
- Convert programs → flat token sequences
- Parameterized tokens (`$p` for identifiers) for type-2 clone detection
- Find longest common subsequences

### N-Gram Language Models
[[n-gram-language-models]] — the statistical foundation:
- Estimate P(token | previous n-1 tokens) via frequency counting
- Unigram (n=1), bigram (n=2), trigram (n=3), …
- Markov assumption: only the last n-1 tokens matter
- Maximum likelihood estimation from corpus counts

### Perplexity and Entropy
[[perplexity-and-entropy]] — model evaluation metrics:
- Perplexity = weighted average branching factor (lower = better)
- Cross-entropy = average surprisal in bits
- PP = 2^H

### Surprisal
[[surprisal-and-code-prediction]] — individual token surprise:
- surprisal(aᵢ) = -log₂ P(aᵢ | context)
- High surprisal → unexpected token → potential complexity or bug

### Smoothing
[[smoothing-techniques]] — handling unseen n-grams:
- Add-one (Laplace), Good-Turing, Kneser-Ney, …
- Redistributes probability mass from seen to unseen events
- Essential for practical model deployment

### Code Naturalness Hypothesis
[[code-naturalness-hypothesis]] — the key research finding:
- Hindle et al. (2016): source code is statistically similar to natural language
- Code has comparable or lower cross-entropy than English
- Enables NLP techniques for software engineering

### Buggy Code Naturalness
[[buggy-code-naturalness]] — Ray et al. (2016):
- Buggy code has higher cross-entropy than non-buggy code
- Naturalness metrics can help prioritize code review
- Statistical, not deterministic

## Key Concepts Summary

| Concept | Core Idea |
|---------|-----------|
| Lexical analysis | Character stream → token stream (first compiler phase) |
| Token | Category name for a set of lexemes (IDENT, INT-LIT, …) |
| Lexeme | Actual character string matching a token pattern |
| Regular expression | Formal notation for token patterns |
| Finite automaton | DFA/NFA implementing regex matching |
| Lex/Flex | Tools that generate lexers from regex specifications |
| N-gram model | P(token \| previous n-1 tokens) via frequency counting |
| Markov assumption | Token depends only on previous n-1 tokens |
| MLE | P = count(context+token) / count(context) |
| Perplexity | Weighted branching factor (model quality metric) |
| Cross-entropy | Average surprisal in bits (lower = more natural) |
| Surprisal | -log₂ P(token \| context) (individual surprise) |
| Smoothing | Redistributing probability to unseen n-grams |
| Code naturalness | Source code is statistically similar to natural language |

## Connections to Other Lectures
- [[software-analyse-lecture-1]] — Lecture 1 introduced code clones; this lecture deepens token-level analysis
- [[code-clones]] — CCFinder uses token sequences for clone detection (Lecture 1 → Lecture 2 connection)
- [[abstract-interpretation]] — Later lectures build on the analysis pipeline; tokens are the lowest level

## Exam-Relevant Points
- Explain the role of lexical analysis in the compiler pipeline
- Distinguish token vs lexeme with examples
- Describe how regular expressions and finite automata relate to lexer construction
- Explain n-gram language models: formula, MLE, Markov assumption
- Calculate bigram probabilities from corpus counts
- Define and calculate perplexity and cross-entropy
- Explain the code naturalness hypothesis and its evidence
- Describe how smoothing addresses the sparsity problem
- Explain why buggy code might have higher cross-entropy
- Know the key papers: Hindle et al. (2016), Ray et al. (2016), Rahman et al. (2019)
