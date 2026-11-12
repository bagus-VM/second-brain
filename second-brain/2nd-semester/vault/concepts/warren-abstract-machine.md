---
title: "Warren Abstract Machine"
tags: [concept, prolog, abstract-machines, semester-2, virtual-machines]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[abstract-machine-semantics]]"]
---

## One-line Summary
The Warren Abstract Machine (WAM) is a low-level operational model for executing Prolog, with explicit term storage, argument registers, continuations and backtracking state.

## Core Intuition
Prolog asks whether relations hold and may return several answers. An implementation must preserve alternatives and undo variable bindings when one path fails. The WAM makes that hidden bookkeeping explicit in machine instructions and memory areas.

## Formal Definition / Statement
The WAM is an abstract machine for efficient execution of Prolog programs. In the lecture's model it has a heap (global stack) for terms, a local stack for local variables and saved state, a trail for restoring bindings, X/A registers for temporary values and argument passing, and an S register pointing into a compound term. Terms use REF cells for variables and STR cells for structures.

## Key Properties
- Facts and rules are compiled to code; goals become calls.
- Unification matches terms and creates variable bindings.
- Alternatives require choice points and restoration of bindings on backtracking.
- `try_me_else`, `retry_me_else`, and `trust_me` manage alternative clauses.
- `get_structure` checks or constructs a structure and selects read or write mode.
- The lecture covers 17 of 39 instructions and explicitly omits several implementation details.

## Worked Example
For `path(X,Y) :- edge(X,Z), path(Z,Y).`, the compiled code preserves `Y`, creates a fresh `Z`, calls `edge(X,Z)`, then calls `path(Z,Y)`. If an alternative later fails, the trail restores bindings made since the relevant choice point before the next clause is tried.

## Common Pitfalls
- Confusing Prolog's declarative relation with the WAM's concrete execution order.
- Forgetting that one query can produce multiple answers, not just true/false.
- Reusing variable bindings from a failed alternative instead of restoring them.
- Treating the lecture's simplified instruction list as the complete WAM specification.

## Connections
- [[abstract-machine-semantics]] — abstract models can specify language behavior or operational execution; WAM is the latter.
- [[virtual-machines-and-runtime-systems-lecture-3]] — the lecture source and its C-semantics contrast.
- [[virtual-machines-and-runtime-systems-lecture-3]] — source lecture for the machine's unification and backtracking model.

## Open Questions
- The lecture does not fully define memory allocation, unification, garbage collection, or all 39 instructions.
- The exact treatment of cut and several optimization instructions is outside the presented subset.
