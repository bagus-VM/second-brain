---
title: "Basic Blocks"
tags: [concept, software-analyse, semester-1, control-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph]
---

## One-line Summary

A basic block is a maximal sequence of statements that must execute consecutively — control enters only at the first statement and exits only at the last, making it the fundamental unit of [[control-flow-graph|control flow analysis]].

## Core Intuition

Many analyses don't care about the fine-grained flow *within* a straight-line sequence of statements — they only care about where branching happens. Collapsing consecutive non-branching statements into a single basic block reduces the graph size dramatically and simplifies algorithms like [[dominance]] and data flow analysis.

## Formal Definition / Statement

A **basic block** is a maximal sequence of consecutive statements such that:
1. Flow enters at the first statement in the block (the **leader**)
2. Flow leaves at the last statement in the block (no intermediate exit)
3. No statement inside the block (except possibly the last) can be the target of a jump
4. No statement inside the block (except possibly the last) can cause a jump

**Leaders** (first statement of a basic block):
1. The first statement in the procedure
2. Every statement that is the target of a branch (conditional or unconditional)
3. Every statement that immediately follows a branch or return

## Key Properties

- Every statement in a program belongs to exactly one basic block
- Basic blocks partition the [[control-flow-graph|CFG]] into a smaller graph where nodes are blocks and edges represent control flow between blocks
- Inside a basic block, execution is strictly sequential — no decisions are made
- The last statement in a block determines which block(s) execute next (branch, fall-through, or return)
- Many compiler optimisations operate at the basic block level (dead code elimination within a block, constant folding, etc.)

## Worked Example

```java
public int foo(int y) {
    int x = 0;              // ← Leader 1: first statement
    int z = y * 2;
    if(y == x + z) {        // ← Leader 2: branch target potential
        System.out.println(y);  // ← Leader 3: target of branch
        z++;
        bar();
    }
    return z;               // ← Leader 4: follows the branch
}
```

Basic blocks:
```
Block 1: [int x = 0;  int z = y*2;  if(y == x+z)]  → leader: statement 2
Block 2: [println(y);  z++;  bar();]                 → leader: statement 5 (branch target)
Block 3: [return z;]                                 → leader: statement 9 (follows branch)
```

CFG at block level:
```
Start → [Block 1] → [Block 2] → [Block 3] → End
              ↓ (false)
         [Block 3]
```

## Common Pitfalls

- Forgetting that a statement *following* a branch is also a leader (it's the fall-through target)
- Not treating method calls that may throw exceptions as implicit exits — in Java, `bar()` could throw, breaking the "must execute consecutively" assumption
- Conflating basic blocks with [[natural-loop|loops]] — a loop body may span multiple basic blocks
- In switch statements without `break`, multiple cases can fall through into the same block

## Connections

- [[control-flow-graph]] – basic blocks are the standard way to simplify CFGs for analysis
- [[dominance]] – dominance algorithms are typically run on the block-level CFG
- [[natural-loop]] – loop bodies are composed of basic blocks; the loop header is always the start of a basic block
- Data flow analysis (transfer functions are defined per basic block)
- [[post-dominance]] – post-dominance is computed over basic blocks

## Open Questions

- How do we handle basic blocks in the presence of exception handlers (Java's try/catch)?
- When is it beneficial to *split* a basic block (e.g., for fine-grained instrumentation)?
