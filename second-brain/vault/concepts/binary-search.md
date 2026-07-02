---
title: "Binary Search"
tags: [concept, algorithms, semester-1, search]
course: "General CS"
source_count: 1
status: current
last_updated: 2026-07-02
prerequisites: [sorting, arrays]
---

## One-line Summary
Binary search finds a target value in a sorted array by repeatedly dividing the search interval in half, achieving O(log n) time complexity.

## Core Intuition
Binary search is the classic "guess the number" strategy applied to arrays. Instead of checking every element (linear search), you jump to the middle: if the target is smaller, discard the right half; if larger, discard the left half. Each step halves the search space, so even a million elements need only ~20 comparisons. The key insight is that a sorted order lets you make a definitive elimination with every comparison.

## Formal Definition / Statement
**Input:**
- Sorted array A[0..n-1]
- Target value t

**Output:**
- Index i such that A[i] = t, or -1 if not found

**Algorithm (iterative):**
1. Set left = 0, right = n-1
2. While left ≤ right:
   - mid = left + (right - left) / 2 (avoids overflow vs (left + right) / 2)
   - If A[mid] = t → return mid
   - If A[mid] < t → left = mid + 1
   - If A[mid] > t → right = mid - 1
3. Return -1 (not found)

**Complexity:**
- Time: O(log n) — halves search space each step
- Space: O(1) iterative, O(log n) recursive (call stack)

**Precondition:** Array must be sorted.

## Key Properties / Complexity
- **Logarithmic time**: O(log n) — extremely fast even for huge inputs
- **Precondition**: array MUST be sorted; incorrect results otherwise
- **Space**: O(1) iterative, O(log n) recursive
- **Deterministic**: always finds the same result for the same input
- **Not comparison-optimal**: O(log n) comparisons, but each comparison eliminates half the space

## Worked Example
**Problem**: Find target 7 in sorted array [1, 3, 5, 7, 9, 11, 13]

```
Step 1: left=0, right=6, mid=3 → A[3]=7 == 7 → FOUND at index 3
```

**Problem**: Find target 6 in sorted array [1, 3, 5, 7, 9, 11, 13]

```
Step 1: left=0, right=6, mid=3 → A[3]=7 > 6 → search left: right=2
Step 2: left=0, right=2, mid=1 → A[1]=3 < 6 → search right: left=2
Step 3: left=2, right=2, mid=2 → A[2]=5 < 6 → search right: left=3
Step 4: left=3 > right=2 → NOT FOUND (-1)
```

## Common Pitfalls
- **Off-by-one errors**: Using `left < right` instead of `left ≤ right` misses single-element intervals
- **Integer overflow**: `(left + right) / 2` overflows for large indices; use `left + (right - left) / 2`
- **Unsorted input**: Binary search on unsorted data gives wrong answers silently
- **Wrong boundary update**: Must use `mid + 1` and `mid - 1`, not `mid`, to avoid infinite loops
- **Assuming linear search is always slower**: For very small arrays (< ~30 elements), linear search can be faster due to branch prediction and cache locality

## Connections
- [[delta-debugging]] — delta debugging uses binary search as its core search strategy on input space
- [[paths-walks-and-cycles]] — binary search trees relate to graph/tree traversal concepts
- [[depth-first-search]] — recursive binary search is a form of DFS on a virtual tree
- [[locality-sensitive-hashing]] — LSH narrows search space similar to binary search

## Open Questions
- When is binary search worse than linear search? (Answer: when data is unsorted or very small, where cache effects dominate)
- How does interpolation search improve on binary search for uniformly distributed data?
- What are the implications of binary search on modern hardware with branch predictors?
