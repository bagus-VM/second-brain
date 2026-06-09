---
title: "Shift-Reduce Parsing"
tags: [concept, software-analyse, semester-1, parsing, bottom-up-parsing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, parse-tree]
---

## One-line Summary

Shift-reduce parsing is a bottom-up parsing strategy that builds the parse tree from leaves to root by repeatedly shifting tokens onto a stack and reducing when the top of the stack matches a production's right-hand side.

## Core Intuition

Imagine you have a stack and an input stream. You can do two things: **shift** (push the next token onto the stack) or **reduce** (if the top of the stack matches the right-hand side of a production A → α, pop α and push A). Keep going until the stack contains only the start symbol and the input is empty. This is the mirror image of top-down parsing — instead of expanding nonterminals downward, you're recognizing and collapsing them upward.

## Formal Definition / Statement

A shift-reduce parser maintains:
- A **stack** of grammar symbols (terminals and nonterminals)
- An **input buffer** of remaining tokens

Two operations:
1. **Shift**: move the next input token onto the top of the stack
2. **Reduce**: if the top k symbols on the stack match the right-hand side of some production A → X₁X₂…Xₖ, pop those k symbols and push A

A successful parse ends with the start symbol on the stack and empty input.

The key challenge is deciding **when** to shift vs. reduce — this is what distinguishes different bottom-up parsing methods (LR, SLR, LALR).

## Key Properties

- Bottom-up parsers handle a larger class of grammars than top-down (LL) parsers
- Left-recursive grammars are naturally handled (no elimination needed)
- LR(1) parsers can handle all deterministic context-free languages
- The parse tree is constructed implicitly through the sequence of reductions
- Each reduction corresponds to constructing a subtree of the final parse tree
- Rightmost derivations in reverse: a bottom-up parse produces a rightmost derivation read backward

## Worked Example

Grammar:
```
E → E + T | T
T → T * F | F
F → ( E ) | id
```

Parsing `id + id * id`:

| Step | Stack | Input | Action |
|------|-------|-------|--------|
| 1 | $ | id + id * id $ | Shift id |
| 2 | $ id | + id * id $ | Reduce F → id |
| 3 | $ F | + id * id $ | Reduce T → F |
| 4 | $ T | + id * id $ | Reduce E → T |
| 5 | $ E | + id * id $ | Shift + |
| 6 | $ E + | id * id $ | Shift id |
| 7 | $ E + id | * id $ | Reduce F → id |
| 8 | $ E + F | * id $ | Reduce T → F |
| 9 | $ E + T | * id $ | Shift * |
| 10 | $ E + T * | id $ | Shift id |
| 11 | $ E + T * id | $ | Reduce F → id |
| 12 | $ E + T * F | $ | Reduce T → T * F |
| 13 | $ E + T | $ | Reduce E → E + T |
| 14 | $ E | $ | Accept |

Each reduce step pops the RHS and pushes the LHS nonterminal, building the parse tree bottom-up.

## Common Pitfalls

- Confusing shift-reduce with recursive descent — they are opposite directions (bottom-up vs. top-down)
- Not realizing that left recursion is **natural** for shift-reduce (unlike [[predictive-parsing|predictive parsing]] which requires [[left-recursion-elimination]])
- Forgetting that the parser needs a **lookahead** to decide shift vs. reduce (LR(k) uses k lookahead tokens)
- Assuming shift-reduce handles all CFGs — it only works for unambiguous grammars that are LR-parseable

## Connections

- [[context-free-grammar]] — the grammar defines what can be reduced
- [[parse-tree]] — reductions build the parse tree from leaves to root
- [[predictive-parsing]] — the opposite approach (top-down); requires grammar transformations that shift-reduce does not
- [[left-recursion-elimination]] — not needed for shift-reduce parsing
- [[operator-precedence-associativity]] — expression grammars naturally use this in shift-reduce parsers
- [[grammar-ambiguity]] — ambiguous grammars cause shift-reduce conflicts (shift/reduce or reduce/reduce)

## Open Questions

- How do SLR, LALR, and canonical LR parsers differ in their conflict resolution?
- What is the relationship between shift-reduce parsing and Earley parsing?
- How do modern parser generators (Bison, Menhir) implement shift-reduce parsing?
