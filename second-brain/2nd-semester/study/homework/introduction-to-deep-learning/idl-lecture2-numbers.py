#!/usr/bin/env python3
"""Computations backing the Introduction to Deep Learning lecture-2 concept pages.

Everything numeric that appears on those pages is produced here. Stdlib only.

Run: python idl-lecture2-numbers.py
"""

from fractions import Fraction as F

# ---------------------------------------------------------------- 1. i.i.d. / shift

# Bot table from slide 5 (15 labelled registrations, 5 features).
BOTS = [
    # id, os, browser, tld, time_to_register_s, posts_per_day, bot
    (1, "Windows", "Browser", "domain", 4, "Yes"),
    (2, "Linux", None, None, 2, "No"),
    (3, None, "Chrome", ".de", 0.5, "No"),
    (4, "Windows", "Firefox", ".de", 17, 12, "No"),
    (5, "Linux", "Firefox", ".com", 412, 1, "No"),
    (6, None, "Chrome", ".fr", 538, 3, "No"),
    (7, "Windows", "Chrome", ".com", 392, 1, "No"),
    (8, "MacOS", "Safari", ".de", 129, 3.5, "No"),
    (9, "Linux", "Firefox", ".com", 245, 2, "No"),
    (10, "Unknown", "Firefox", ".es", 25, 7, "No"),
    (11, "Windows", "Chrome", ".com", 540, 145, "Yes"),
    (12, "Linux", "Firefox", ".de", 58, 2, "Yes"),
    (13, "Linux", "Chrome", ".fr", 89, 5, "No"),
    (14, "Windows", "Chrome", ".com", 6, 0.3, "No"),
    (15, "Linux", "Safari", ".gov", 572, 2, "No"),
]


def covariate_shift():
    print("=" * 74)
    print("1. covariate shift on the bot table")
    print("=" * 74)
    # "posts per day > 100" is a perfect rule on the slide's 15 training rows.
    posts = [(1, 4, "Yes"), (2, 2, "No"), (3, 0.5, "No"), (4, 12, "No"),
             (5, 1, "No"), (6, 3, "No"), (7, 1, "No"), (8, 3.5, "No"),
             (9, 2, "No"), (10, 7, "No"), (11, 145, "Yes"), (12, 2, "Yes"),
             (13, 5, "No"), (14, 0.3, "No"), (15, 2, "No")]
    rule = lambda p: "Yes" if p > 100 else "No"
    correct = sum(1 for _, p, y in posts if rule(p) == y)
    found = sum(1 for _, p, y in posts if y == "Yes" and rule(p) == "Yes")
    bots_train = sum(1 for _, _, y in posts if y == "Yes")
    print(f"  rule 'posts/day > 100' on the 15 training rows: {correct}/15 correct "
          f"= {correct/15:.4f}, recall of bots {found}/{bots_train} = "
          f"{found/bots_train:.4f}")
    # A later batch from a shifted population: new TLDs, and the base rate has
    # fallen from 3/15 bots to 1/15.
    unseen = [(0.3, "No"), (1, "No"), (2, "No"), (3, "No"), (4, "No"),
              (5, "No"), (6, "No"), (7, "No"), (8, "No"), (9, "No"),
              (10, "Yes"), (11, "No"), (12, "No"), (13, "No"), (14, "No")]
    c2 = sum(1 for p, y in unseen if rule(p) == y)
    bots_unseen = sum(1 for _, y in unseen if y == "Yes")
    found2 = sum(1 for p, y in unseen if y == "Yes" and rule(p) == "Yes")
    print(f"  same rule on a shifted 15-row batch with {bots_unseen} bot: {c2}/15 = "
          f"{c2/15:.4f}, recall of bots {found2}/{bots_unseen} = "
          f"{found2/bots_unseen:.4f}")
    print(f"  the base rate moved from {bots_train}/15 = {bots_train/15:.4f} bots to "
          f"{bots_unseen}/15 = {bots_unseen/15:.4f}")
    print("  -> the headline number IMPROVES (0.8667 to 0.9333) while the rule stops "
          "finding bots at all (recall 0.3333 to 0.0000)")
    print(f"     a do-nothing classifier scores {(15-bots_unseen)/15:.4f} on the new "
          f"batch, up from {(15-bots_train)/15:.4f} on the training data")


# ------------------------------------------------- 2. soft classification / EV

def soft_and_ev():
    print("=" * 74)
    print("2. calibration and the 80/20 bet")
    print("=" * 74)
    n, p = 100, 0.8
    print(f"  perfectly calibrated at p = {p}: of {n} predictions, "
          f"about {p*n:.0f} are correct")
    # betting at even odds: win 1 if right, lose 1 if wrong
    ev = p * 1 + (1 - p) * (-1)
    print(f"  even-money bet at p = {p}: EV = {ev:+.2f} per unit staked")
    for q in (0.5, 0.6, 0.8, 0.9):
        print(f"    at p = {q}: EV = {q*1 + (1-q)*(-1):+.2f}")
    # an uncalibrated model that always says 0.8 on a 50/50 population
    print("  always-0.8 model on a 50/50 population: claimed confidence 0.8, "
          "actual hit rate 0.50")
    print(f"    reported expected correct = {0.8*n:.0f}/100, actual = {0.5*n:.0f}/100, "
          f"overconfidence = {0.8-0.5:+.2f}")
    # expected calibration error over the single bin
    print(f"    ECE for that single bin = |0.8 - 0.5| = {abs(0.8-0.5):.2f}")


# ------------------------------------------------- 3. loss functions

def losses():
    print("=" * 74)
    print("3. empirical risk: 0-1 loss vs squared error")
    print("=" * 74)
    y = [1, 1, 0, 0, 1]
    modelA = [0.51, 0.51, 0.49, 0.49, 0.51]   # right on every row, but barely
    modelB = [1.0, 1.0, 0.0, 0.0, 0.0]        # four exact, one confidently wrong
    for name, yh in (("A", modelA), ("B", modelB)):
        zero_one = sum(1 for a, b in zip(yh, y) if (a >= 0.5) != bool(b)) / len(y)
        sq = sum((a - b) ** 2 for a, b in zip(yh, y)) / len(y)
        acc = 1 - zero_one
        print(f"  model {name}: predictions {yh}")
        print(f"    0-1 loss = {zero_one:.2f} (accuracy {acc:.2f}), "
              f"squared error = {sq:.4f}")
    print("  -> 0-1 loss prefers A (0.00 vs 0.20); squared error prefers B "
          "(0.2000 vs 0.2401)")
    print("     A is right everywhere with no confidence; B is exactly right four "
          "times and maximally wrong once. The two losses disagree about which is "
          "the better model, and neither is wrong")
    print("  0-1 loss gradient: piecewise constant, so zero wherever it is defined "
          "(and undefined at the threshold) — nothing to descend")


# ------------------------------------------------- 4. double descent demo

def polyfit(xs, ys, degree):
    """Least squares by normal equations, solved with fraction-free Gaussian elim."""
    n = degree + 1
    A = [[sum(x ** (i + j) for x in xs) for j in range(n)] for i in range(n)]
    b = [sum((x ** i) * y for x, y in zip(xs, ys)) for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        if abs(A[col][col]) < 1e-12:
            return None  # singular: interpolation threshold region
        for r in range(col + 1, n):
            f = A[r][col] / A[col][col]
            for c in range(col, n):
                A[r][c] -= f * A[col][c]
            b[r] -= f * b[col]
    coef = [0.0] * n
    for r in range(n - 1, -1, -1):
        coef[r] = (b[r] - sum(A[r][c] * coef[c] for c in range(r + 1, n))) / A[r][r]
    return coef


def polyval(coef, x):
    return sum(c * x ** i for i, c in enumerate(coef))


def double_descent():
    print("=" * 74)
    print("4. the interpolation threshold: polynomials on noisy samples of sin(2*pi*x)")
    print("=" * 74)
    import math
    import random
    rng = random.Random(42)
    f = lambda x: math.sin(2 * math.pi * x)
    npts = 15
    xs = [i / (npts - 1) for i in range(npts)]            # 15 training points
    ys = [f(x) + rng.gauss(0, 0.15) for x in xs]
    xt = [i / 400 for i in range(401)]
    yt = [f(x) for x in xt]
    # Fit in a centred basis (x' = 2x - 1). Without centring the monomial moment
    # matrix loses numerical rank around degree 10 and the fit is not computable
    # in double precision at all.
    xc = [2 * x - 1 for x in xs]
    xtc = [2 * x - 1 for x in xt]

    print(f"  {npts} training points; basis x' = 2x - 1; noise sd 0.15")
    print(f"  {'degree':>6} {'params':>7} {'train MSE':>12} {'test MSE':>12}  note")
    rows = []
    for d in range(1, 16):
        coef = polyfit(xc, ys, d)
        if coef is None:
            print(f"  {d:>6} {d+1:>7} {'singular':>12} {'':>12}  basis exhausted")
            continue
        tr = (sum((polyval(coef, x) - y) ** 2 for x, y in zip(xc, ys)) / len(xs))
        te = (sum((polyval(coef, x) - y) ** 2 for x, y in zip(xtc, yt)) / len(xt))
        note = ""
        if tr < 1e-10:
            note = "<- interpolates, train error is exactly 0"
        rows.append((d, d + 1, tr, te))
        print(f"  {d:>6} {d+1:>7} {tr:>12.3e} {te:>12.3e}  {note}")

    best = min(rows, key=lambda r: r[3])
    print(f"\n  minimum test error at degree {best[0]} "
          f"({best[1]} parameters): test MSE {best[3]:.3e}")
    interp = [r for r in rows if r[2] < 1e-10]
    if interp:
        print(f"  interpolation threshold: degree {interp[0][0]}, which has "
              f"{interp[0][1]} parameters for {npts} training points")
        print(f"  test MSE at the threshold: {interp[0][3]:.3e} — "
              f"{interp[0][3]/best[3]:.0f} times the minimum")
    print("\n  HONEST RESULT: this demo reproduces the rise toward the interpolation")
    print("  threshold and the blow-up at it, and it does NOT reproduce a second")
    print("  descent. The reason is structural rather than numerical: a degree-(n-1)")
    print("  polynomial with n points is fully determined, so the model class ends")
    print("  exactly at the threshold. There is no further degree to grow into, and")
    print("  'more parameters than data points' is not reachable in a fixed")
    print("  polynomial basis. The double-descent curves in Belkin et al. (2019) and")
    print("  Nakkiran et al. (2020) are neural-network curves, where the parameter")
    print("  count can pass the number of training points without the function class")
    print("  being exhausted. The slide's own caption calls its curves schematic.")


# ------------------------------------------------- 5. decision trees

def decision_tree():
    print("=" * 74)
    print("5. the slide's tree, traced over the slide's table")
    print("=" * 74)
    rows = [(1, 23, "Family", "high"), (2, 17, "Sport", "high"),
            (3, 43, "Sport", "high"), (4, 68, "Family", "low"),
            (5, 32, "Truck", "low")]

    def slide_tree(age, cartype):
        if cartype == "Truck":
            return "low"
        return "low" if age > 60 else "high"

    ok = 0
    for i, age, car, actual in rows:
        pred = slide_tree(age, car)
        ok += pred == actual
        print(f"  row {i}: car={car:<7} age={age:<3} -> {pred:<5} "
              f"actual {actual:<5} {'OK' if pred == actual else 'WRONG'}")
    print(f"  slide tree training accuracy: {ok}/5 = {ok/5:.2f}")
    # is there a smaller consistent tree? try single-attribute stumps
    for attr in ("age", "cartype"):
        if attr == "age":
            for thr in sorted({r[1] for r in rows}):
                for hi, lo in (("high", "low"), ("low", "high")):
                    acc = sum((hi if r[1] > thr else lo) == r[3] for r in rows)
                    if acc == 5:
                        print(f"  one-attribute stump: age > {thr} -> {hi}, "
                              f"else {lo}: {acc}/5 = 1.00 (depth 1 beats depth 2)")
        else:
            for v in sorted({r[2] for r in rows}):
                acc = sum((("low" if r[2] == v else "high") == r[3]) for r in rows)
                if acc == 5:
                    print(f"  one-attribute stump: cartype == {v} -> low, "
                          f"else high: {acc}/5 = 1.00")


# ------------------------------------------------- 6. SVM margins

def svm():
    print("=" * 74)
    print("6. maximum margin on a tiny 2-D case")
    print("=" * 74)
    import math
    A = [(1.0, 1.0), (2.0, 2.0)]       # class +1
    B = [(4.0, 1.0), (5.0, 2.0)]       # class -1

    def margin(w1, w2, b):
        vals = [w1 * x + w2 * y + b for x, y in A + B]
        if not (max(vals[:2]) < min(vals[2:])):
            return None
        return min(abs(v) / math.hypot(w1, w2) for v in vals)

    cands = {
        "x - 3 = 0   (vertical, midway)": (1.0, 0.0, -3.0),
        "x + 0.5y - 4 = 0  (tilted)": (1.0, 0.5, -4.0),
        "2x - 7 = 0  (vertical, shifted)": (2.0, 0.0, -7.0),
        "x + y - 5 = 0  (45 degrees)": (1.0, 1.0, -5.0),
    }
    best = None
    for name, (w1, w2, b) in cands.items():
        m = margin(w1, w2, b)
        if m is None:
            print(f"  {name:<34} does not separate the classes")
            continue
        w = math.hypot(w1, w2)
        print(f"  {name:<34} margin = {m:.4f}, width 2/||w|| = {2/w:.4f}")
        if best is None or m > best[1]:
            best = (name, m, w)
    print(f"  largest margin: {best[0]} (margin {best[1]:.4f})")
    print("  margin width = 2 / ||w||; for w = (1,0), ||w|| = 1 and the width is "
          f"{2/1:.4f}, matching the 2 units between the two clusters")
    print("  the support vectors are the points that touch the margin: (2,2) for the "
          "positive class and (4,1) for the negative one")


# ------------------------------------------------- 7. ensembles

def ensembles():
    print("=" * 74)
    print("7. majority voting on the slide's table")
    print("=" * 74)
    truth = [+1, +1, +1, -1, -1]
    C = [[+1, +1, +1, +1, -1],
         [+1, +1, -1, -1, -1],
         [-1, -1, +1, -1, -1]]
    for k, c in enumerate(C, 1):
        acc = sum(a == b for a, b in zip(c, truth)) / len(truth)
        print(f"  classifier {k}: {c}  accuracy {acc:.1f}")
    maj = [+1 if sum(c[i] for c in C) > 0 else -1 for i in range(5)]
    acc = sum(a == b for a, b in zip(maj, truth)) / len(truth)
    print(f"  majority vote: {maj}  accuracy {acc:.1f}")
    # Under independence with the classifiers' own per-instance correctness rates.
    from itertools import product
    p = [0.8, 0.6, 0.6]

    def maj_prob(pv):
        pr = 0.0
        for bits in product([0, 1], repeat=3):
            if sum(bits) < 2:
                continue
            pr_i = 1.0
            for k, b in enumerate(bits):
                pr_i *= pv[k] if b else (1 - pv[k])
            pr += pr_i
        return pr

    print(f"  if the three classifiers were independent with per-instance correctness "
          f"{p}:")
    print(f"    P(majority correct) = {maj_prob(p):.4f} per instance, i.e. an "
          f"expected accuracy of {maj_prob(p):.4f}")
    print("    (the table gives 1.0 because the three error patterns are exactly "
          "complementary — that is the mechanism working perfectly, not a law)")


# ------------------------------------------------- 8. class imbalance

def imbalance():
    print("=" * 74)
    print("8. class imbalance on the slide's example")
    print("=" * 74)
    total, positives = 10000, 100
    # trivial classifier
    acc_trivial = (total - positives) / total
    print(f"  trivial 'never a bot': accuracy {acc_trivial:.4f}, recall 0, "
          f"precision undefined (0/0)")
    TP, FP, FN, TN = 80, 40, 20, 9860
    acc = (TP + TN) / total
    prec = TP / (TP + FP)
    rec = TP / (TP + FN)
    f1 = 2 * prec * rec / (prec + rec)
    print(f"  better classifier: TP={TP} FP={FP} FN={FN} TN={TN}")
    print(f"    accuracy  = {TP+TN}/{total} = {acc:.4f}")
    print(f"    precision = {TP}/{TP+FP} = {prec:.4f}")
    print(f"    recall    = {TP}/{TP+FN} = {rec:.4f}")
    print(f"    F1        = {f1:.4f}")
    print(f"  accuracy floor from the base rate alone: {acc_trivial:.4f} "
          f"-> the classifier adds only {acc - acc_trivial:+.4f}")


# ------------------------------------------------- 9. regression metrics

def regression_metrics():
    print("=" * 74)
    print("9. MAE vs MSE disagreeing about two models")
    print("=" * 74)
    y = [10] * 10
    A = [9] * 10                      # every prediction off by exactly 1
    B = [10] * 5 + [11.5] * 5         # five exact, five off by 1.5
    for name, yh in (("A", A), ("B", B)):
        errs = [a - b for a, b in zip(yh, y)]
        mae = sum(abs(e) for e in errs) / len(y)
        mse = sum(e * e for e in errs) / len(y)
        print(f"  model {name}: {len(yh)} predictions, errors {sorted(set(errs))}")
        print(f"    MAE = {mae:.4f}   MSE = {mae**2 if False else mse:.4f}")
    maeA = sum(abs(a - b) for a, b in zip(A, y)) / 10
    mseA = sum((a - b) ** 2 for a, b in zip(A, y)) / 10
    maeB = sum(abs(a - b) for a, b in zip(B, y)) / 10
    mseB = sum((a - b) ** 2 for a, b in zip(B, y)) / 10
    print(f"  MAE prefers {'B' if maeB < maeA else 'A'} "
          f"({maeB:.4f} vs {maeA:.4f});  "
          f"MSE prefers {'B' if mseB < mseA else 'A'} "
          f"({mseB:.4f} vs {mseA:.4f})")
    print("  -> opposite verdicts on the same two models: MAE rewards B for having "
          "five perfect predictions, MSE punishes B for the size of its errors")
    print("  the slide gives MAE and MSE only — no RMSE, no R-squared, no MAPE")


# ------------------------------------------------- 10. clustering

def clustering():
    print("=" * 74)
    print("10. six points, two distances, two answers")
    print("=" * 74)
    pts = [(0.0, 0.0), (0.5, 0.2), (1.0, 1.0), (5.0, 5.0), (5.2, 4.8), (9.0, 1.0)]
    import math

    def kmeans(pts, k, dist, iters=20):
        centroids = [pts[i] for i in range(k)]
        assign = [0] * len(pts)
        for _ in range(iters):
            new = [min(range(k), key=lambda c: dist(p, centroids[c])) for p in pts]
            if new == assign and _ > 0:
                break
            assign = new
            for c in range(k):
                members = [p for p, a in zip(pts, assign) if a == c]
                if members:
                    centroids[c] = (sum(m[0] for m in members) / len(members),
                                    sum(m[1] for m in members) / len(members))
        return assign

    euclid = lambda a, b: math.hypot(a[0] - b[0], a[1] - b[1])
    manhattan = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    for k in (2, 3):
        for name, d in (("Euclidean", euclid), ("Manhattan", manhattan)):
            a = kmeans(pts, k, d)
            groups = {}
            for p, c in zip(pts, a):
                groups.setdefault(c, []).append(p)
            print(f"  k={k} {name:<10} -> " +
                  " | ".join(f"{sorted(g)}" for _, g in sorted(groups.items())))
    print("  no ground truth exists for which of these is 'right'; the lecture's "
          "point on slide 11 is exactly that")
    print()
    print("  where the distance metric DOES change the answer — nearest neighbour of "
          "the origin among two candidates:")
    cands = [(1.0, 1.0), (1.5, 0.0)]
    for name, d in (("Euclidean", euclid), ("Manhattan", manhattan)):
        dists = [(p, d((0.0, 0.0), p)) for p in cands]
        dists.sort(key=lambda t: t[1])
        print(f"    {name:<10} distances "
              f"{[(p, round(v, 4)) for p, v in dists]} -> nearest {dists[0][0]}")
    print("    the two metrics disagree about which point is closest, so 'the k "
          "nearest neighbours' is only defined once the metric is fixed")


if __name__ == "__main__":
    covariate_shift()
    soft_and_ev()
    losses()
    double_descent()
    decision_tree()
    svm()
    ensembles()
    imbalance()
    regression_metrics()
    clustering()
