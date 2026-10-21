"""Exercise 0/1 solutions — Introduction to Deep Learning, Exercise 1 (15.10.2026).

Every task from 01-hw-intro-py-tasks.ipynb, implemented and runnable:

    python exercise-01-solutions.py

Run it to check the outputs; the vault page quotes this file's output.
"""
import random
from collections import Counter

# --- 1. Python as a calculator -------------------------------------------------
# The cell reads "compute 2562" — a superscript was lost in the export.
# Both plausible readings are computed instead of guessing silently.
print("1. 25**62 =", 25 ** 62, " (also shown: 2**56 =", 2 ** 56, ")")

# --- 2. Concatenate two strings ------------------------------------------------
a = "Hello"
b = "World!"
print("2.", a + " " + b)

# --- 3/4. Lists -----------------------------------------------------------------
lst = ["alpha", "beta", "gamma", "delta"]
lst.append("epsilon")
print("3.", lst)
print("4.", lst[:3])

# --- 5. Star pattern ------------------------------------------------------------
print("5.")
n = 5
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)

# --- 6. Product of three parameters --------------------------------------------
def product(x, y, z):
    return x * y * z

print("6. product(2, 3, 4) =", product(2, 3, 4))

# --- 7/8. Primes ----------------------------------------------------------------
def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

primes = [x for x in range(2, 101) if is_prime(x)]
print("7. is_prime(1), is_prime(2), is_prime(97), is_prime(100) =",
      is_prime(1), is_prime(2), is_prime(97), is_prime(100))
print("8. primes 2..100 (%d):" % len(primes), primes)

# --- 9. Dice rolls --------------------------------------------------------------
def dice_rolls(n):
    """Return a map: result (1-6) -> how often it occurred."""
    counts = {}
    for _ in range(n):
        r = random.randint(1, 6)
        counts[r] = counts.get(r, 0) + 1
    return counts

rolls = dice_rolls(6000)
print("9. dice_rolls(6000) =", dict(sorted(rolls.items())), "(sum =", sum(rolls.values()), ")")

# --- 10. Merge two dictionaries by adding common keys ---------------------------
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
merged = {}
for k in set(d1) | set(d2):
    merged[k] = d1.get(k, 0) + d2.get(k, 0)
print("10.", {k: merged[k] for k in ["a", "b", "d", "c"]})
# one-liner with Counter:
print("    via Counter:", dict(Counter(d1) + Counter(d2)))

# --- 11. Lengths of sublists ----------------------------------------------------
lists = [[1, 2, 3], [], [4], list(range(10))]
print("11.", [len(l) for l in lists])

# --- 12. Exceptions -------------------------------------------------------------
def my_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 1

def my_division_no_exception(x, y):
    # same behaviour without catching an exception
    if y == 0:
        return 1
    return x / y

print("12. my_division(10, 2), my_division(10, 0) =", my_division(10, 2), my_division(10, 0))
print("    without exceptions:", my_division_no_exception(10, 2), my_division_no_exception(10, 0))

# --- 13. File handling ----------------------------------------------------------
def letter_counts(letter, path):
    result = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            result.append(line.count(letter))
    return result

import os
ftest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ftest.txt")
if os.path.exists(ftest):
    print("13. ftest.txt contents:", open(ftest, encoding="utf-8").read().splitlines())
    print("    letter_counts('a', ftest.txt) =", letter_counts("a", ftest))
    print("    letter_counts('b', ftest.txt) =", letter_counts("b", ftest))
else:
    print("13. ftest.txt not found next to this script — copy it from the exercise folder")

# --- 14. Change please! ---------------------------------------------------------
def pay_options(amount, coins):
    """All ways to pay `amount` using `coins`, each way sorted descending."""
    coins = sorted(coins, reverse=True)
    out = []

    def rec(remaining, i, acc):
        if remaining == 0:
            out.append(list(acc))
            return
        if i == len(coins):
            return
        c = coins[i]
        # take k coins of this denomination (k = 0, 1, ...) — this keeps the
        # results sorted and avoids duplicate permutations
        for k in range(remaining // c + 1):
            rec(remaining - k * c, i + 1, acc + [c] * k)

    rec(amount, 0, [])
    return out

print("14. pay_options(10, [200,100,50,20,10,5,2,1]):")
for opt in pay_options(10, [200, 100, 50, 20, 10, 5, 2, 1]):
    print("     ", opt)
print("     count =", len(pay_options(10, [200, 100, 50, 20, 10, 5, 2, 1])))

# --- 15-21. NumPy ---------------------------------------------------------------
try:
    import numpy as np
except ImportError:
    print("\nNumPy not installed — run `uv add numpy` first.")
    raise SystemExit

zeros = np.zeros((20, 10))
print("16. zeros.shape =", zeros.shape, "sum =", zeros.sum())

nat = np.arange(200).reshape(20, 10)
print("17. arange(200).reshape(20,10)[0, :5] =", nat[0, :5], "... last =", nat[-1, -1])

four = np.random.randint(0, 5, size=(2, 2, 2, 2))
print("18. 4-d array of 16 elements, values < 5:")
print(four)

print("19. mean of the 4-d array =", four.mean())

sub = four[0].reshape(-1)[:2]
print("20. a sub-array with exactly two elements =", sub)

big = np.arange(0, 200, 7)
print("21. values > 100 of arange(0,200,7) =", big[big > 100])