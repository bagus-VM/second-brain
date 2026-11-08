---
title: "Delta Debugging"
tags: [concept, software-analyse, semester-1, debugging]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [testing, debugging]
---

## One-line Summary
Delta debugging is an automated technique that finds the minimal set of changes responsible for a failure by systematically reducing the input using a binary search-like algorithm.

## Core Intuition
"Yesterday my program worked. Today it does not. Why?" Something changed between yesterday and today. Delta debugging takes the changes and systematically removes subsets to find the minimal failure-inducing change. It's like binary search for bugs: split the input in half, check if removing one half still fails, keep the half that causes failure, repeat until minimal.

## Formal Definition / Statement
**Input:**
- Failure-inducing input Δ (set of changes)
- Automated test that checks if failure occurs

**Output:**
- Minimal subset Δ' ⊆ Δ that still causes failure

**Algorithm (ddmin):**
1. Split input into n subsets (initially n=2)
2. For each subset, check if removing it still fails
3. If yes, proceed with that subset (and n := n-1)
4. If no subset removal causes failure, increase granularity: n := min(2n, |input|)
5. Repeat until n > |input| (minimal change found)

**Complexity:** O(|Δ|²) test runs in worst case

## Key Properties / Complexity
- **Minimality**: finds minimal failure-inducing subset
- **Automation**: requires automated test (no manual inspection)
- **Generality**: works on any input representation (HTML, code, configuration)
- **Efficiency:** O(|Δ|²) test runs, much better than exhaustive search O(2^|Δ|)
- **Determinism**: same input → same output

## Worked Example
**Problem**: Mozilla crashes when printing with this HTML input (896 lines)

**Goal**: find minimal failure-inducing subset

**Process:**
1. Split into 2 halves (448 lines each)
2. Remove first half → still crashes → proceed with second half
3. Split second half into 2 (224 lines each)
4. Remove first quarter → still crashes → proceed
5. Continue binary search...
6. Eventually isolate: `<SELECT NAME="op_sys" MULTIPLE SIZE=7>`

**Result**: 896 lines → 1 line (minimal failure-inducing input)

**Benefits:**
- Easier to communicate (1 line vs 896 lines)
- Easier to debug (smaller state, shorter execution)
- Identifies duplicates (simplified cases subsume duplicates)

### Algorithm Walkthrough
```
Input: <SELECT>foo</SELECT> (repeated 8 times)
       [1][2][3][4][5][6][7][8]

Step 1: n=2, split into 2 subsets
        Remove [1-4] → still fails (✘)
        Remove [5-8] → passes (✔)
        → proceed with [1-4], n=2

Step 2: n=2, split [1-4] into 2
        Remove [1-2] → passes (✔)
        Remove [3-4] → still fails (✘)
        → proceed with [3-4], n=2

Step 3: n=2, split [3-4] into 2
        Remove [3] → passes (✔)
        Remove [4] → passes (✔)
        → neither works, increase n: n = min(2*2, 2) = 4

Step 4: n=4 > |[3-4]| = 2, terminate
        Minimal failure-inducing input: [3-4]
```

## Common Pitfalls
- **Requiring automated test**: delta debugging needs automated test, can't do manual inspection
- **Assuming minimality implies causation**: minimal set may not be THE cause (could be interaction)
- **Ignoring dependencies**: if changes are dependent, binary search may not work
- **Confusing with fault localization**: delta debugging finds minimal input; fault localization finds suspicious statements
- **Exponential worst case**: O(|Δ|²) is better than O(2^|Δ|) but still expensive for large inputs

## Connections
- [[fault-localization]] — fault localization ranks statements; delta debugging finds minimal input
- [[testing]] — both require automated tests
- [[debugging]] — both are automated debugging techniques
- [[binary-search]] — delta debugging is essentially binary search on input space
- [[program-traces]] — may use traces to guide debugging

## Open Questions
- How does delta debugging handle dependent changes (not independent subsets)?
- What's the practical limit for delta debugging on very large inputs (millions of lines)?
- How does delta debugging interact with version control (git bisect)?
