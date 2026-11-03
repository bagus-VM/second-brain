---
title: "Exercise 1 — Python Basics (Solutions)"
tags: [homework, deep-learning, python, semester-2]
course: "Introduction to Deep Learning"
source_count: 4
status: current
last_updated: 2026-10-20
---

# Introduction to Deep Learning — Exercise 1 solutions

Source: `01-hw-intro-py-tasks.ipynb`, `01-slides.pdf`, `01-homework.pdf` (15.10.2026).
Runnable script with the same answers: `exercise-01-solutions.py` in this folder. Every output below is copied from an actual run of that script.
Cross-checked against the professor's own `01-hw-intro-py-solutions.ipynb` (added 2026-10-20) — see the correction in task 1.

## Setup (homework sheet task 1 and 2)

```bash
uv init intro-dl
cd intro-dl
uv add jupyter numpy
```

This creates `intro-dl/.venv/`. Then in VS Code: install the Python, Jupyter, and Ruff extensions, set `"notebook.formatOnSave.enabled": true` and `"editor.defaultFormatter": "charliermarsh.ruff"`, and **select the `.venv` interpreter as the notebook kernel** — without that step the packages installed with `uv` are invisible to the notebook.

Run notebooks either in VS Code or with `uv run jupyter lab` from the project directory.

---

## Exercise 0 — Python basics

**1. Use Python as a calculator.**
The cell reads "compute 256²" — a superscript, not a digit run. The official solution notebook
(`01-hw-intro-py-solutions.ipynb`) states it in words: *"compute 256 times 256"*, and computes

```python
256 * 256   # 65536
```

**Correction (2026-10-20).** An earlier version of this page read the cell as "2562" and offered two
guesses (`25 ** 62`, `2 ** 56`). Both were wrong. The superscript ² survived the export as a Unicode
character; it is a squared, not a lost digit. The official solution settles it.

**2. Two strings, concatenated.**

```python
a = "Hello"
b = "World!"
print(a + " " + b)      # Hello World!
```

**3. List of four strings, add a fifth.**

```python
lst = ["alpha", "beta", "gamma", "delta"]
lst.append("epsilon")   # ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
```

**4. Sublist of the first three.**

```python
lst[:3]                 # ['alpha', 'beta', 'gamma']
```

**5. Star pattern with for loops.**

```python
n = 5
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)
```

Output:

```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

**6. Product of three parameters.**

```python
def product(x, y, z):
    return x * y * z

product(2, 3, 4)        # 24
```

**7/8. Primality test and the primes up to 100.**

```python
def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:          # only test divisors up to sqrt(x)
        if x % d == 0:
            return False
        d += 1
    return True

primes = [x for x in range(2, 101) if is_prime(x)]
```

Results: `is_prime(1) = False`, `is_prime(2) = True`, `is_prime(97) = True`, `is_prime(100) = False`.
25 primes between 2 and 100: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]`.

The `d*d <= x` bound is the point of the exercise: testing all divisors up to x works but is O(x); the square-root bound makes it O(√x).

**9. Dice rolls.**

```python
import random

def dice_rolls(n):
    counts = {}
    for _ in range(n):
        r = random.randint(1, 6)
        counts[r] = counts.get(r, 0) + 1
    return counts
```

One run of `dice_rolls(6000)`: `{1: 1000, 2: 1007, 3: 1011, 4: 985, 5: 992, 6: 1005}` — each face near the expected 1000.

**10. Merge two dictionaries, adding common keys.**

```python
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

merged = {}
for k in set(d1) | set(d2):
    merged[k] = d1.get(k, 0) + d2.get(k, 0)
# {'a': 400, 'b': 400, 'd': 400, 'c': 300}
```

One-liner with `Counter`: `dict(Counter(d1) + Counter(d2))` — `Counter.__add__` drops keys with value ≤ 0, so it adds values for common keys as required.

**11. Lengths of sublists.**

```python
lists = [[1, 2, 3], [], [4], list(range(10))]
[len(l) for l in lists]   # [3, 0, 1, 10]
```

**12. Exceptions.**

```python
def my_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 1
```

`my_division(10, 2) = 5.0`, `my_division(10, 0) = 1`.

**Same behaviour without catching an exception:** check the divisor before dividing.

```python
def my_division_no_exception(x, y):
    if y == 0:
        return 1
    return x / y
```

The exception version is the idiomatic Python answer (EAFP — easier to ask forgiveness than permission); the check-first version (LBYL — look before you leap) avoids the exception machinery but duplicates the condition at every call. In this trivial case they are equivalent; with concurrent code the check-first version is racy while the exception version is not.

**13. File handling.**

```python
def letter_counts(letter, path):
    return [line.count(letter) for line in open(path, encoding="utf-8")]
```

`ftest.txt` contains `a / ab / baba / abba / ba`.
`letter_counts("a", "ftest.txt") = [1, 1, 2, 2, 1]`.
`letter_counts("b", "ftest.txt") = [0, 1, 2, 2, 1]`.

**14. Change please!**

```python
def pay_options(amount, coins):
    coins = sorted(coins, reverse=True)
    out = []

    def rec(remaining, i, acc):
        if remaining == 0:
            out.append(list(acc))
            return
        if i == len(coins):
            return
        c = coins[i]
        for k in range(remaining // c + 1):
            rec(remaining - k * c, i + 1, acc + [c] * k)

    rec(amount, 0, [])
    return out
```

`pay_options(10, [200,100,50,20,10,5,2,1])` returns **11** options — exactly the 11 listed in the exercise (this implementation emits them in ascending denomination-of-first-coin order; the sheet lists them the other way round, the set is identical):

```
[1,1,1,1,1,1,1,1,1,1]   [2,1,1,1,1,1,1,1,1]   [2,2,1,1,1,1,1,1]
[2,2,2,1,1,1,1]         [2,2,2,2,1,1]         [2,2,2,2,2]
[5,1,1,1,1,1]           [5,2,1,1,1]           [5,2,2,1]
[5,5]                   [10]
```

Why the recursion avoids duplicates: it never revisits a denomination. At each step it decides *how many* coins of the current denomination to use and moves on, so `[5,5]` and `[5,5]` cannot both appear.

---

## NumPy

**16. Zeros.**

```python
zeros = np.zeros((20, 10))      # shape (20, 10), sum 0.0
```

**17. All natural numbers 0–199 in the same shape.**

```python
nat = np.arange(200).reshape(20, 10)
# nat[0, :5] = [0 1 2 3 4] ; nat[-1, -1] = 199
```

**18. 4-dimensional array, 16 elements, random integers < 5.**

```python
four = np.random.randint(0, 5, size=(2, 2, 2, 2))
```

`2·2·2·2 = 16` elements — the shape has to multiply out to exactly 16. One run:

```
[[[[4 1] [1 0]] [[3 1] [3 0]]]
 [[[0 4] [3 4]] [[3 4] [4 4]]]]
```

**19. Mean of that array.** `four.mean()` — `2.4375` for the run above. (It varies: the array is random.)

**20. A sub-array with exactly two elements.**

```python
four[0, 0]        # or: four[0].reshape(-1)[:2]
```

Slicing dimensions with integer indices removes them, so `four[0, 0]` is shape `(2, 2)` — 4 elements. To get exactly two: `four[0, 0, 0]` (shape `(2,)`).

**21. Elements greater than 100.**

```python
big = np.arange(0, 200, 7)
big[big > 100]    # [105 112 119 126 133 140 147 154 161 168 175 182 189 196]
```

`big[big > 100]` is boolean masking: the comparison produces a boolean array of the same shape, which is then used as an index.

---

## What to actually take away

- `uv` + one environment per project, and the kernel selection trap.
- Python indentation is syntax; blocks must be indented consistently.
- Everything in the "optional" section (deque, Counter, defaultdict, heapq) is standard-library knowledge that makes week 2–4 homework shorter.
- The homework is not graded and tests do not count towards the grade — but the schedule moves fast (PyTorch in week 2), so this week is the only slack in the plan.
