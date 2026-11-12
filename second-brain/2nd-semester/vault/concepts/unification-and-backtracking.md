---
title: "Unification and Backtracking in Prolog"
tags: [concept, prolog, logic-programming, semester-2, virtual-machines]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[warren-abstract-machine]]"]
---

## One-line Summary
Prolog resolves relational goals by unifying terms, then explores alternative clauses and restores earlier variable bindings when a branch fails or another answer is requested.

## Core Intuition
A Prolog query can have several valid answers. The interpreter must remember not just where to return, but also which variable assignments came from the current attempt. Backtracking undoes those bindings so the next alternative starts from the correct state.

## Formal Definition / Statement
Unification attempts to make two terms syntactically equal by consistently binding their variables. Query resolution selects a clause whose head unifies with a goal, replaces that goal with the clause body, and continues until the goal list is empty or no clause matches. Backtracking revisits a saved alternative after failure or on request for another answer, restoring bindings recorded since that choice point.

## Key Properties
- Facts are clauses with no body; rules have a head and one or more goals in the body.
- A successful query can return multiple variable bindings.
- The WAM uses choice-point instructions such as `try_me_else`, `retry_me_else`, and `trust_me` to manage clause alternatives.
- The trail records variable bindings that must be undone when restoring an earlier state.
- Depth-first clause search is operational behavior; it may affect termination even when the declarative relation has answers.

## Worked Example
Given `edge(a,b)`, `edge(b,c)`, `edge(c,d)` and recursive rules for `path/2`, query `path(S,c)` can produce `S=b` through the direct edge and `S=a` through `a→b→c`. To produce the second answer, Prolog must restore bindings made while exploring the first alternative.

## Common Pitfalls
- Treating a query as a simple Boolean test when it may generate multiple answers.
- Keeping bindings from one alternative while trying another.
- Confusing unification (matching and binding terms) with ordinary assignment.
- Assuming depth-first search is complete for every infinite search tree.

## Connections
- [[warren-abstract-machine]] — implements unification, choice points and the trail with explicit instructions and memory.
- [[virtual-machines-and-runtime-systems-lecture-3]] — source lecture's Prolog examples and WAM discussion.
- [[abstract-machine-semantics]] — distinguishes an operational execution model from a language-semantics specification.

## Open Questions
- The lecture omits full unification and memory-allocation algorithms.
- Occurs-check behavior and its consequences are not discussed in the deck. The slides also do not define the exact fairness or scheduling guarantees of Prolog's depth-first search.
