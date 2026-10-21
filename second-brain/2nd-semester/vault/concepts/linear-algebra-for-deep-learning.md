---
title: "Linear Algebra for Deep Learning (Vectors and Matrices in Python)"
tags: [concept, deep-learning, python, linear-algebra, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[python-for-deep-learning]]"]
---

## One-line Summary

The demo notebook implements the linear algebra a neural network does internally — dot product, vector addition, normalisation, matrix multiply — first in plain Python, then in NumPy, so that the same operations can be seen as loops, as a class, and as array arithmetic.

## Core Intuition

The demo states the motivation outright: *"Neural networks do lots of (simple) linear algebra."* A dense layer is a matrix multiply, a loss is a dot product, a normalised input is a division by a norm. Before PyTorch arrives in week 2, the student should recognise these operations when they see them in library code.

Building them by hand in plain Python is the point. A dot product written as a loop makes the cost model visible: you can count the multiplications, see the `zip` truncation that happens when the two vectors have different lengths, and notice the difference between a list comprehension (which materialises a list) and a generator expression (which does not). The library version is then not a black box but the obvious shorthand for code you have already written.

The notebook's second lesson is about **ownership**. Python passes references, not copies, so `b = a` binds a second name to the *same* list, and mutating `b` mutates `a`. Every "my matrix changed and I don't know why" bug in later weeks starts here.

## Formal Definition / Statement

**Dot product.** For vectors `a` and `b`:

```python
def my_dotproduct(a, b):
    n = min(len(a), len(b))
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    return result
```

The `min(len(a), len(b))` is the interesting line. It silently truncates to the shorter vector, so a length-3 and a length-5 input produce a "correct" answer for a length-3 dot product rather than an error. The generator-expression version is the same computation without the intermediate list:

```python
def dotproduct(a, b):
    return sum((ai * bi for ai, bi in zip(a, b)))
```

Note that `zip` itself truncates to the shorter sequence, so the explicit `min` is redundant in the second version but necessary in the first.

**Vector addition and normalisation.**

```python
def add_vecs(a, b):
    return [ai + bi for ai, bi in zip(a, b)]

def add_vecs_normalize(a, b, normalize=True):
    result = add_vecs(a, b)
    sum_of_squares = sum(xi * xi for xi in result)
    length = math.sqrt(sum_of_squares)
    return [xi / length for xi in result]
```

Normalisation is the Euclidean norm: divide each component by `sqrt(sum of squares)`. This is exactly the unit-length output a neural network applies to an activation vector — and the same operation as the `StandardScaler` in [[ml-pipeline-scikit-learn]], though scaling and normalising are different things.

**Matrices as a class.** The notebook implements a `Matrix` type with `matmul` (the triple loop) and `__add__` (element-wise via `zip`):

```python
def matmul(self, other):
    m, n, o = len(self.vals), len(other.vals), len(other.vals[0])
    result = [[0] * o for _ in range(m)]
    for i in range(m):
        for j in range(o):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return Matrix(result)
```

`m × n` times `n × o` gives `m × o` — the notebook's comment states the dimensions explicitly, which is the single most important thing to internalise about matrix multiplication.

**The aliasing pitfall.** Python passes *references*:

```python
a = [1, 2, 3]
b = a
b[0] = 42
print(a, b)          # [42, 2, 3] [42, 2, 3]  -- both changed
```

`copy.deepcopy` fixes it, and the `Matrix` constructor uses `copy.deepcopy(vals)` so that a matrix cannot be mutated from outside after construction. The notebook demonstrates the payoff: after building `mat1` from `vals`, writing `vals[0][0] = 1000` has *no effect* on `mat1`.

**NumPy.** The same three operations in array form: `a + b` (element-wise), `a @ b` (matrix multiply), `a[:, 1]` (column selection, with `:` meaning "all rows"). The colon syntax and the `@` operator are the two things that carry over directly into PyTorch.

## Key Properties

- **The operations are the same; only the cost model changes.** The Python loops are O(m·n·o) in interpreted bytecode; the NumPy version pushes the inner loop into C, which is why the course's "Python orchestrates, C computes" rule exists.
- **Aliasing is the default.** Assignment binds a name to an object; it does not copy. `copy`, `copy.deepcopy`, and `.copy()` are three different tools with three different costs.
- **Shape errors are silent in plain Python.** `zip` truncates; a wrong-length dot product returns a number instead of raising. NumPy's shape checking is one of the practical reasons to move to it.
- **`@` is not `*`.** In NumPy `*` is element-wise and `@` is matrix multiply. This single distinction causes most beginner errors when the library changes.
- **Type hints are checked by tools, not at runtime.** The notebook's `add_vecs(a: list[int], b: list[int]) -> list[int]` is a promise to mypy, not an enforcement by Python.

## Worked Example

**The dot product, three ways.** For `vec1 = [1, 0, 0]` and `vec2 = [0, 1, 0]`:

```python
my_dotproduct(vec1, vec2)    # 0
dotproduct(vec1, vec2)       # 0
```

Both give 0, and correctly so: the vectors are orthogonal, which is the simplest possible demonstration that the dot product measures alignment. As a sanity check, `dotproduct(vec1, vec1)` is `1` — the squared length.

**Matrix multiply.** `mat1 = [[1,2],[3,4]]`, `mat2 = [[2,3],[4,5]]`:

- Add: `[[3, 5], [7, 9]]`
- Matmul: `[[1*2+2*4, 1*3+2*5], [3*2+4*4, 3*3+4*5]]` = `[[10, 13], [22, 29]]`

Check by hand: `matmul[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0] = 1*2 + 2*4 = 10`. The `k` loop is the contraction index, and it is the index that the plain-Python implementation makes obvious and NumPy's `@` hides.

**The deep copy, demonstrated.** After `mat1 = Matrix(vals)` with `vals = [[1,2],[3,4]]`:

```python
vals[0][0] = 1000
print(mat1.vals)    # [[1, 2], [3, 4]]  -- unchanged
```

Without the `deepcopy` in the constructor, `mat1.vals` would be the *same list object* as `vals`, and the mutation would show up inside the matrix. The notebook comments this as the "copy pitfall" and the class handles it — a small design decision that is the difference between a value type and a reference type.

## Common Pitfalls

- **Assuming `b = a` copies a list.** It binds a second name. Every later mutation is shared.
- **Passing a mutable object into a class without copying it.** The `Matrix` constructor's `deepcopy` is the pattern; a constructor that stores the caller's list hands out a handle to their data.
- **Using `*` where `@` was meant.** In NumPy, `a * b` is element-wise.
- **Confusing normalisation with scaling.** `add_vecs_normalize` makes a vector unit length; `StandardScaler` makes a column zero-mean and unit-variance. They are different operations with different purposes.
- **Trusting `zip` to catch length mismatches.** It truncates, so mismatched vectors compute something rather than failing.
- **Materialising large intermediate lists.** The generator expression exists to avoid that; in a real model the equivalent difference is the difference between working and swapping your laptop.

## Connections

- [[python-for-deep-learning]] — the language these snippets are written in; the "Python orchestrates, C computes" performance model that motivates NumPy.
- [[jupyter-notebook-state]] — the demo notebook's other lesson, from a different file in the same folder: a notebook can also lie about its own code.
- [[python-environment-management]] — the `uv` environment that makes NumPy available at all, and the kernel trap that decides whether it is.
- [[linear-regression]] — the ML course's version of the same matrix algebra, in closed form: `f(X) = Xw` is exactly the `matmul` above.
- [[ml-pipeline-scikit-learn]] — where `StandardScaler` appears, and the difference between fitting learned statistics and computing them inline.
- [[minkowski-distance]] (Semester 1) — the distance metrics the ML course reuses in KNN; the same vector operations, different context.

## Open Questions

- The demo notebook's `add_many_vecs(a, b, *args)` prints `type(args)` and returns element-wise sums across three vectors, but no output is shown for it in the file. Whether it is meant as a worked example or leftover scaffolding is unclear.
- The notebook defines `add_vecs_normalize(a, b, normalize=True)` but never uses the `normalize` flag — the parameter is accepted and ignored. Whether this is a deliberate illustration of a bad API or an unfinished function is not stated.
- No mention is made of numerical stability for the normalisation when the vector is the zero vector (division by zero), and the course does not yet cover floating-point behaviour in general.
- The notebook ends at NumPy indexing (`a[:, 1]`); whether broadcasting is taught here or deferred to the PyTorch week is not stated.
