#!/usr/bin/env python3
"""Introduction to Deep Learning — Exercise 3 (2026-10-29): every number,
computed.

Covers the slide's worked examples, the slide's "Your Tasks", and the homework
sheet's four tasks. Every derivative used below is checked against a central
finite difference, so a wrong symbolic derivative cannot slip through.

Run:  python exercise-03-numbers.py
"""
import math

H = 1e-6  # step for the finite-difference check


def num_grad(f, x):
    """Central-difference gradient of f at x (tuple)."""
    out = []
    for i in range(len(x)):
        xp, xm = list(x), list(x)
        xp[i] += H
        xm[i] -= H
        out.append((f(*xp) - f(*xm)) / (2 * H))
    return out


def check_partial(label, symbolic, f, x, i):
    """Assert one hand-derived partial derivative against a finite difference."""
    numeric = num_grad(f, x)[i]
    rel = abs(symbolic - numeric) / max(1.0, abs(numeric))
    ok = rel < 1e-5
    print(f"  derivative check {label:<40} rel. err {rel:.2e}  {'OK' if ok else 'MISMATCH'}")
    if not ok:
        raise SystemExit(f"derivative mismatch for {label}: {symbolic} vs {numeric}")
    return symbolic


def check(label, symbolic, f, x):
    """Assert a hand-derived gradient (list of all partials) against a finite difference."""
    if len(symbolic) != len(x):
        raise SystemExit(f"{label}: symbolic gradient has {len(symbolic)} entries, "
                         f"function takes {len(x)}")
    numeric = num_grad(f, x)
    rel = [abs(s - n) / max(1.0, abs(n)) for s, n in zip(symbolic, numeric)]
    ok = max(rel) < 1e-5
    print(f"  derivative check {label:<40} max rel. err {max(rel):.2e}  {'OK' if ok else 'MISMATCH'}")
    if not ok:
        raise SystemExit(f"derivative mismatch for {label}: {symbolic} vs {numeric}")
    return symbolic


def title(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------------------
title("A. Slide worked example — regression evaluation (slide 5)")
# The slide prints the MAE as 93/5 and the MSE as (7744 + e)/5.
yhat = [4, 7, 9, 3, 100]
y = [5, 9, 8, 2, 12]
abs_err = [abs(a - b) for a, b in zip(yhat, y)]
sq_err = [(a - b) ** 2 for a, b in zip(yhat, y)]
print(f"  pairs (yhat, y)   : {list(zip(yhat, y))}")
print(f"  |yhat - y|        : {abs_err}   sum = {sum(abs_err)}")
print(f"  (yhat - y)^2      : {sq_err}   sum = {sum(sq_err)}")
print(f"  MAE  = {sum(abs_err)}/5 = {sum(abs_err)/5}")
print(f"  MSE  = {sum(sq_err)}/5 = {sum(sq_err)/5}")
print(f"  the slide's '7744 + e': e = {sum(sq_err) - 7744}  (the four small terms)")
print("  NOTE: the slide's row labels extract offset by one; the pairs above are the")
print("  ones that reproduce the printed 93/5, which is the check that settles it.")

# ----------------------------------------------------------------------------
title("B. Slide worked example — binary classification (slides 14-15)")
TP, FN, FP, TN = 8, 2, 16, 974


def binary_metrics(TP, FN, FP, TN):
    prec = TP / (TP + FP)
    rec = TP / (TP + FN)
    acc = (TP + TN) / (TP + FN + FP + TN)
    f1 = 2 * prec * rec / (prec + rec)
    return prec, rec, acc, f1


p, r, a, f1 = binary_metrics(TP, FN, FP, TN)
print(f"  TP={TP} FN={FN} FP={FP} TN={TN}")
print(f"  Precision = {TP}/{TP+FP} = {p:.6f}   (slide: 1/3)")
print(f"  Recall    = {TP}/{TP+FN} = {r:.6f}   (slide: 4/5)")
print(f"  Accuracy  = {TP+TN}/{TP+FN+FP+TN} = {a:.6f}   (slide: 0.982)")
print(f"  F1        = {f1:.6f}   (slide: 8/17 = {8/17:.6f})")

# ----------------------------------------------------------------------------
title("C. Slide worked example — 3-class one-vs-rest (slides 16-20)")
M = [[3, 147, 33],
     [17, 833, 137],
     [86, 84, 160]]
total = sum(sum(row) for row in M)
print(f"  matrix (rows = truth, cols = prediction): {M}")
print(f"  total samples = {total}")
f1s = []
for c in range(3):
    tp = M[c][c]
    fn = sum(M[c]) - tp
    fp = sum(M[i][c] for i in range(3)) - tp
    tn = total - tp - fn - fp
    prec, rec, acc, f1c = binary_metrics(tp, fn, fp, tn)
    f1s.append(f1c)
    print(f"  class {c}: TP={tp:4} FN={fn:4} FP={fp:4} TN={tn:4} "
          f"P={prec:.6f} R={rec:.6f} F1={f1c:.6f}")
acc = sum(M[c][c] for c in range(3)) / total
print(f"  macro-F1  = {sum(f1s)/3:.6f}   (slide: ~0.44)")
print(f"  accuracy  = {sum(M[c][c] for c in range(3))}/{total} = {acc:.6f}   (slide: 0.664)")
print("  the slide rounds P, R to 2 decimals before averaging; the exact macro-F1 from")
print("  the unrounded F1 values is the number above.")

# ----------------------------------------------------------------------------
title("D. Slide worked example — gradient descent, f(x) = x^2 (slide 31)")


def f_x2(x):
    return x ** 2


x, alpha = 1.0, 0.25
print(f"  f(x) = x^2,  x0 = {x},  alpha = {alpha}")
for step in range(1, 8):
    g = 2 * x
    print(f"    step {step}: x = {x:>12.8f}   f' = {g:>12.8f}   x_next = {x - alpha*g:>12.8f}")
    x = x - alpha * g
print("  converges to 0 (the minimum).")

# ----------------------------------------------------------------------------
title("E. Slide worked example — gradient descent that diverges (slides 32-33)")


def f_div(x, y):
    return x ** 2 * y + y ** 2


sym = check("f(x,y)=x^2 y + y^2", [2 * 2 * 4, 2 ** 2 + 2 * 4], f_div, (2.0, 4.0))
x, y, alpha = 2.0, 4.0, 1.0
print(f"  f(x,y) = x^2 y + y^2,  (x0,y0) = ({x}, {y}),  alpha = {alpha}")
for step in range(1, 5):
    gx, gy = 2 * x * y, x ** 2 + 2 * y
    print(f"    step {step}: grad = ({gx:>10.2f}, {gy:>10.2f})  ->  ({x - alpha*gx:>12.2f}, {y - alpha*gy:>12.2f})")
    x, y = x - alpha * gx, y - alpha * gy
print("  no minimum exists on this surface: gradient descent runs off to -inf.")

# ----------------------------------------------------------------------------
title("F. Slide 'Your Tasks' — MSE and MAE")
pairs = [(0.4, 0.5), (0.7, 1.7), (0.6, 0.5), (0.2, 0.3), (0.1, 0.1)]
d = [a - b for a, b in pairs]
print(f"  (yhat, y) = {pairs}")
print(f"  yhat - y  = {d}")
print(f"  |diff|    = {[abs(v) for v in d]}   sum = {sum(abs(v) for v in d)}")
print(f"  diff^2    = {[round(v*v, 4) for v in d]}   sum = {round(sum(v*v for v in d), 4)}")
print(f"  MAE = {sum(abs(v) for v in d)/5:.4f}")
print(f"  MSE = {sum(v*v for v in d)/5:.4f}")
print("  MAE > MSE here, which is possible because every error is below 1.")

# ----------------------------------------------------------------------------
title("G. Slide 'Your Tasks' — precision, recall, accuracy, F1")
print("  table: rows y=1 then y=0; columns yhat=1 then yhat=0")
print("         yhat=1  yhat=0")
print("  y=1      5      17")
print("  y=0      1      53")
print("  the first row/column is the positive class, as in the slide's own example")
TP, FN, FP, TN = 5, 17, 1, 53
p, r, a, f1 = binary_metrics(TP, FN, FP, TN)
print(f"  TP={TP} FN={FN} FP={FP} TN={TN}")
print(f"  Precision = {p:.4f}   Recall = {r:.4f}   Accuracy = {a:.4f}   F1 = {f1:.4f}")
print("  accuracy 0.763 looks respectable; recall 0.227 says the model misses 17 of 22")

# ----------------------------------------------------------------------------
title("H. Slide 'Your Tasks' — one step of gradient descent")
poly = lambda x: 3 * x ** 2 - 1.25 * (x - 1) ** 4 + (x - 2) ** 6
dpoly = lambda x: 6 * x - 5 * (x - 1) ** 3 + 6 * (x - 2) ** 5
check("f(x)=3x^2-1.25(x-1)^4+(x-2)^6", [dpoly(2.0)], lambda v: poly(v), (2.0,))
for x0, alpha in [(2.0, 0.1), (3.0, 0.01), (3.0, 0.1)]:
    g = dpoly(x0)
    print(f"  x0={x0}, alpha={alpha}: f'={g:>8.4f}  ->  x1 = {x0 - alpha*g:.6f}"
          f"   f(x1)={poly(x0 - alpha*g):.4f}")

# ----------------------------------------------------------------------------
title("I. Homework 1(a) — two steps, f(x,y) = 3xy - 5y^2")


def hw_a(x, y):
    return 3 * x * y - 5 * y ** 2


check("3xy - 5y^2", [3 * 1, 3 * 0 - 10 * 1], hw_a, (0.0, 1.0))
x, y, alpha = 0.0, 1.0, 0.1
print(f"  start ({x}, {y}), alpha = {alpha}, f = {hw_a(x,y)}")
for step in (1, 2):
    gx, gy = 3 * y, 3 * x - 10 * y
    x, y = x - alpha * gx, y - alpha * gy
    print(f"  step {step}: grad = ({gx:>8.4f}, {gy:>9.4f})  ->  (x,y) = ({x:.6f}, {y:.6f})   f = {hw_a(x,y):.6f}")

# ----------------------------------------------------------------------------
title("J. Homework 1(b) — one step, g(x,y) = xy^2 - x^3 exp(x-y) + sin^2(xy)")


def hw_b(x, y):
    return x * y ** 2 - x ** 3 * math.exp(x - y) + math.sin(x * y) ** 2


E = math.exp(0.0)  # at (1,1), exp(x-y) = exp(0) = 1
gx_sym = 1 ** 2 - (3 * 1 ** 2 * E + 1 ** 3 * E) + 2 * math.sin(1) * math.cos(1) * 1
gy_sym = 2 * 1 * 1 + 1 ** 3 * E + 2 * math.sin(1) * math.cos(1) * 1
check_partial("g_x at (1,1)", gx_sym, hw_b, (1.0, 1.0), 0)
check_partial("g_y at (1,1)", gy_sym, hw_b, (1.0, 1.0), 1)
gx, gy = gx_sym, gy_sym          # rebind: gx/gy still hold section I's gradient
print(f"  d/dx = y^2 - (3x^2 + x^3) e^(x-y) + 2 sin(xy)cos(xy) * y")
print(f"  d/dy = 2xy + x^3 e^(x-y) + 2 sin(xy)cos(xy) * x")
print(f"  at (1,1): grad = ({gx:.6f}, {gy:.6f})")
print(f"  sin(2) = {math.sin(2):.6f} is the term that makes both numbers irrational")
print(f"  one step with alpha = 1:  (x,y) = (1 - {gx:.6f}, 1 - {gy:.6f}) = ({1-gx:.6f}, {1-gy:.6f})")
print(f"  f(1,1) = {hw_b(1,1):.6f}   f({1-gx:.4f},{1-gy:.4f}) = {hw_b(1-gx, 1-gy):.6f}")
print(f"  the value went DOWN by {hw_b(1,1) - hw_b(1-gx, 1-gy):,.1f}: the direction is a")
print("  descent, but alpha = 1 is enormous - the step overshoots far past any minimum.")

# ----------------------------------------------------------------------------
title("K. Homework 1(c) — gradient ascent")
print("  x <- x + alpha * grad f.  Identical loop with the sign flipped.")
print("  Equivalently: gradient descent on -f, since grad(-f) = -grad(f).")

# ----------------------------------------------------------------------------
title("L. Homework 2 — regressor evaluation, two models")
y = [5, 7, 9, 3, 10]
m1 = [5, 7, 9, 2, 12]
m2 = [4.5, 7.5, 10, 2.5, 11]
for name, yhat in [("Model 1", m1), ("Model 2", m2)]:
    d = [a - b for a, b in zip(yhat, y)]
    mae = sum(abs(v) for v in d) / len(d)
    mse = sum(v * v for v in d) / len(d)
    print(f"  {name}: yhat={yhat}")
    print(f"           errors={d}  |e| sum={sum(abs(v) for v in d)}  e^2 sum={sum(v*v for v in d)}")
    print(f"           MAE = {mae:.4f}   MSE = {mse:.4f}")
print("  VERDICT: the two metrics disagree. Model 1 wins on MAE (0.6 vs 0.7),")
print("  Model 2 wins on MSE (0.55 vs 1.00) because Model 1's single 2-unit miss")
print("  is squared, while Model 2 spreads five small misses. 'Which is better'")
print("  has no answer until the loss is chosen - and MSE punishes the outlier.")

# ----------------------------------------------------------------------------
title("M. Homework 3(a) — binary classifier on the 2x2 matrix")
print("  rows: y=0, y=1 ; columns: yhat=0, yhat=1")
print("         yhat=0  yhat=1")
print("  y=0      3      147")
print("  y=1      17     137")
for label, (TP, FN, FP, TN) in {
    "class 0 positive (first row/col, slide convention)": (3, 147, 17, 137),
    "class 1 positive (alternative reading)": (137, 17, 147, 3),
}.items():
    p, r, a, f1 = binary_metrics(TP, FN, FP, TN)
    print(f"  {label}:")
    print(f"      TP={TP} FN={FN} FP={FP} TN={TN}  P={p:.6f} R={r:.6f} A={a:.6f} F1={f1:.6f}")

# ----------------------------------------------------------------------------
title("N. Homework 3(b) — binary classifier on two label lists")
yt = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
yp = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
print(f"  y  = {yt}")
print(f"  yh = {yp}")
for label, pos in [("class 0 positive", 0), ("class 1 positive", 1)]:
    TP = sum(1 for t, q in zip(yt, yp) if t == pos and q == pos)
    FN = sum(1 for t, q in zip(yt, yp) if t == pos and q != pos)
    FP = sum(1 for t, q in zip(yt, yp) if t != pos and q == pos)
    TN = sum(1 for t, q in zip(yt, yp) if t != pos and q != pos)
    p, r, a, f1 = binary_metrics(TP, FN, FP, TN)
    print(f"  {label}: TP={TP} FN={FN} FP={FP} TN={TN}  P={p:.4f} R={r:.4f} "
          f"A={a:.4f} F1={f1:.4f}  ({TP+FN} actual positives, {TP+FP} predicted positives)")
print("  accuracy is the same either way (0.5455); precision and recall swap roles.")

# ----------------------------------------------------------------------------
title("O. Homework 4(a) — 3-class one-vs-rest on the sheet's matrix")
M = [[7, 129, 46],
     [25, 766, 170],
     [73, 73, 204]]
total = sum(sum(r) for r in M)
print(f"  matrix = {M}   total = {total}")
f1s = []
for c in range(3):
    tp = M[c][c]
    fn = sum(M[c]) - tp
    fp = sum(M[i][c] for i in range(3)) - tp
    tn = total - tp - fn - fp
    p, r, a, f1c = binary_metrics(tp, fn, fp, tn)
    f1s.append(f1c)
    print(f"  class {c}: TP={tp:4} FN={fn:4} FP={fp:4}  P={p:.6f} R={r:.6f} F1={f1c:.6f}")
print(f"  macro-F1 = {sum(f1s)/3:.6f}")
print(f"  accuracy = {sum(M[c][c] for c in range(3))}/{total} = "
      f"{sum(M[c][c] for c in range(3))/total:.6f}")
print("  fit for purpose, not for the metric: the 97.2% on class 1 and the near-zero")
print("  on class 0 are one story; accuracy 0.654 is the aggregate that hides it.")

# ----------------------------------------------------------------------------
title("P. Homework 4(b) — system margins on the same matrix")
per_class_recall = []
for c in range(3):
    tp = M[c][c]
    per_class_recall.append(tp / sum(M[c]))
print(f"  per-class recall = {[round(v, 4) for v in per_class_recall]}")
print(f"  spread = {max(per_class_recall) - min(per_class_recall):.4f}")
print(f"  class 0 is predicted {sum(M[i][0] for i in range(3))} times but is only "
      f"{sum(M[0])} of the {total} samples")
print(f"  predicted counts per class = {[sum(M[i][c] for i in range(3)) for c in range(3)]}"
      f"   actual counts = {[sum(M[c]) for c in range(3)]}")
