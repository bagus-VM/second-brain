---
title: "Centrality, Laplacian, and Homophily Quick Reference"
tags: [study, network-science, semester-1]
course: "Network Science"
status: current
last_updated: 2026-07-27
---

# Centrality, Laplacian, and Homophily Quick Reference

Worked examples on a toy graph: 5 nodes (A, B, C, D, E), edges A-B, A-C, A-D, D-E.

## Degree Centrality

Formula: C_D(v) = deg(v) / (n-1)

Count edges. Divide by n-1 to normalize.

| Node | deg | C_D |
|------|-----|-----|
| A | 3 | 3/4 = 0.75 |
| B | 1 | 1/4 = 0.25 |
| C | 1 | 1/4 = 0.25 |
| D | 2 | 2/4 = 0.50 |
| E | 1 | 1/4 = 0.25 |

## Closeness Centrality

Formula: C_C(v) = (n-1) / sum of d(v,u) for all u != v

BFS from v, sum distances, divide n-1 by the sum.

| Node | Distances | Sum | C_C |
|------|-----------|-----|-----|
| A | 1,1,1,2 | 5 | 4/5 = 0.80 |
| B | 1,2,2,3 | 8 | 4/8 = 0.50 |
| C | 1,2,2,3 | 8 | 4/8 = 0.50 |
| D | 1,2,2,1 | 6 | 4/6 = 0.67 |
| E | 2,3,3,1 | 9 | 4/9 = 0.44 |

## Harmonic Centrality

Formula: H(v) = sum of 1/d(v,u), with 1/infinity = 0

Same distances, sum reciprocals instead of dividing.

| Node | Distances | Reciprocals | H |
|------|-----------|-------------|---|
| A | 1,1,1,2 | 1+1+1+0.5 | 3.50 |
| B | 1,2,2,3 | 1+0.5+0.5+0.333 | 2.33 |
| C | 1,2,2,3 | 1+0.5+0.5+0.333 | 2.33 |
| D | 1,2,2,1 | 1+0.5+0.5+1 | 3.00 |
| E | 2,3,3,1 | 0.5+0.333+0.333+1 | 2.17 |

Same ranking as closeness. Advantage: if graph is disconnected, unreachable nodes contribute 0 (1/infinity = 0), so it does not break.

## Betweenness Centrality

Formula: C_B(v) = sum over all pairs (s,t), s != v != t, of sigma_st(v) / sigma_st

- sigma_st = total shortest paths from s to t
- sigma_st(v) = how many of those go through v
- Do NOT count paths where v is the start or end

For node A, list all pairs of other nodes (6 pairs):

| Pair | Shortest path | A on it? | Ratio |
|------|--------------|----------|-------|
| B-C | B-A-C | yes | 1/1 |
| B-D | B-A-D | yes | 1/1 |
| B-E | B-A-D-E | yes | 1/1 |
| C-D | C-A-D | yes | 1/1 |
| C-E | C-A-D-E | yes | 1/1 |
| D-E | D-E | no | 0/1 |

Raw betweenness of A = 5. Normalize by (n-1)(n-2)/2 = 6: C_B(A) = 5/6 = 0.83.

When multiple shortest paths exist, split credit. If 2 shortest paths from s to t and 1 goes through v, ratio = 1/2 = 0.5.

## Edge Betweenness

Formula: C_B(e) = sum over all pairs (s,t) of sigma_st(e) / sigma_st

Same idea, but for edges. List all pairs, trace shortest path, tally which edges get crossed. Add 1/sigma_st per path.

Edge scores on the toy graph (one shortest path per pair, so each ratio = 1):

| Edge | Pairs using it | Raw score |
|------|----------------|-----------|
| A-B | AB, BC, BD, BE | 4 |
| A-C | AC, BC, CD, CE | 4 |
| A-D | AD, AE, BD, BE, CD, CE | 6 |
| D-E | AE, BE, CE, DE | 4 |

A-D has highest edge betweenness (bridge to E). Girvan-Newman removes it first.

## Eigenvector Centrality

Formula: Ax = lambda*x, or per node: C_E(v) = (1/lambda) * sum of A_vu * C_E(u)

Important nodes are connected to important nodes. Recursive.

Calculation by power iteration:

1. Build adjacency matrix A.
2. Start with x = [1, 1, 1, ...].
3. Multiply: x_new = A * x_old.
4. Normalize (divide by max element).
5. Repeat until values stabilize.

Adjacency matrix (A, B, C, D, E):

```
     A  B  C  D  E
A  [ 0  1  1  1  0 ]
B  [ 1  0  0  0  0 ]
C  [ 1  0  0  0  0 ]
D  [ 1  0  0  0  1 ]
E  [ 0  0  0  1  0 ]
```

Iteration 1: x_0 = [1,1,1,1,1], x_1 = A*x_0 = [3,1,1,2,1], normalize: [1, 0.33, 0.33, 0.67, 0.33]

Iteration 2: x_2 = A*x_1 = [4,3,3,4,2], normalize: [1, 0.75, 0.75, 1, 0.5]

Iteration 3: x_3 = A*x_2 = [10,4,4,6,4], normalize: [1, 0.4, 0.4, 0.6, 0.4]

Converges: A and D highest, B and C equal (symmetric), E lowest. Absolute values do not matter, only ratios.

Exam tip: a full power iteration is too long for an essay. Know the definition, the equation, and the intuition. The professor will likely ask you to explain, compare, or qualitatively rank, not compute exact values.

## Graph Laplacian

Formula: L = D - A

- D = diagonal degree matrix (degrees on the diagonal, zeros elsewhere)
- A = adjacency matrix

Step 1: Adjacency matrix A.

Step 2: Degree matrix D (diagonal only).

```
     A  B  C  D  E
A  [ 3  0  0  0  0 ]
B  [ 0  1  0  0  0 ]
C  [ 0  0  1  0  0 ]
D  [ 0  0  0  2  0 ]
E  [ 0  0  0  0  1 ]
```

Step 3: Subtract entry by entry.

```
      A   B   C   D   E
A  [  3  -1  -1  -1   0 ]
B  [ -1   1   0   0   0 ]
C  [ -1   0   1   0   0 ]
D  [ -1   0   0   2  -1 ]
E  [  0   0   0  -1   1 ]
```

Pattern: diagonal = degrees, off-diagonal = -1 if connected, 0 if not.

Why it matters: eigenvalues of L encode connectivity. Smallest eigenvalue is always 0. Second-smallest (lambda_2) = algebraic connectivity. If lambda_2 = 0, graph is disconnected. Eigenvector of lambda_2 (Fiedler vector) gives spectral partition (positive values one side, negative the other).

## E-I Index and Random Baseline

E-I index = (E - I) / (E + I)

- E = external (cross-group) edges
- I = internal (within-group) edges
- Range: [-1, +1]. Negative = homophily, 0 = neutral, positive = heterophily.

Random baseline: what would EI be if edges formed randomly given group sizes?

Formula for expected cross-group fraction:

    P(cross | random) = 1 - [ sum of (n_i choose 2) ] / (N choose 2)

where (x choose 2) = x*(x-1)/2.

Worked example: 4 CS, 4 Business, N=8.

1. (4 choose 2) = 6 per group. Sum = 12.
2. (8 choose 2) = 28.
3. P(cross) = 1 - 12/28 = 0.57. Under random mixing, 57% of edges would be cross-group.
4. Baseline EI = P_cross - P_within = 0.57 - 0.43 = +0.14.

Observed EI = -0.75 (strong homophily). Baseline = +0.14. The gap is the real homophily signal beyond group sizes.

Skewed example: 90 CS, 10 Business, N=100.

1. (90 choose 2) = 4005, (10 choose 2) = 45. Sum = 4050.
2. (100 choose 2) = 4950.
3. P(cross) = 1 - 4050/4950 = 0.182.
4. Baseline EI = 0.182 - 0.818 = -0.636.

A 90/10 split gives baseline EI = -0.64 for free, without any homophily. If observed is -0.70, the real homophily is small. If observed is -0.95, it is real. Without the baseline you cannot tell.

## Selection, Socialization, Confounding

All three produce the same snapshot: connected people are similar. Cross-sectional data cannot tell them apart.

**Selection**: similarity causes the tie. You became friends because you were already similar.
- Arrow: Attribute -> Tie
- Example: Both like jazz, become friends because of it.
- Test: did similarity exist before the tie?

**Socialization**: the tie causes similarity. You became friends first, then influenced each other.
- Arrow: Tie -> Attribute
- Example: Friend introduces you to classical music, you start liking it.
- Test: did the attribute change after the tie formed?

**Confounding (contextual correlation)**: a third variable causes both. Neither the attribute nor the tie caused the other.
- Arrow: Context -> Attribute AND Context -> Tie
- Example: Two colleagues both use Python and are friends. The workplace caused both.
- Test: does the association vanish when you condition on the shared context?

Key point: what came first? Attribute first = selection. Tie first = socialization. Third factor caused both = confounding. Only longitudinal data or experiments can separate them.