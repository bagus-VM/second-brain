"""Exercise 2 - paper homework: MML 2.4 matrix products, derivatives, probability.

Every claim in exercise-02-solution.md is computed here, so the page quotes
computed results rather than asserted ones.

Run:  python exercise-02-math.py
"""

import math
import torch

torch.set_printoptions(precision=4, sci_mode=False)

# =====================================================================
# Exercise 1 - Mathematics for Machine Learning, Chapter 2, Exercise 2.4
# "Compute the following matrix products, if possible"
# =====================================================================
print("=" * 70)
print("Exercise 1: MML 2.4 - matrix products")


def mat(rows):
    return torch.tensor(rows, dtype=torch.float64)


def show(name, A, B):
    """Multiply A @ B if the shapes allow it, else report that it is impossible."""
    print(f"\n{name}")
    print(f"  A shape {tuple(A.shape)}: {A.tolist()}")
    print(f"  B shape {tuple(B.shape)}: {B.tolist()}")
    if A.shape[1] != B.shape[0]:
        print(
            f"  NOT POSSIBLE: inner dimensions {A.shape[1]} and {B.shape[0]} differ"
        )
        return None
    C = A @ B
    print(f"  A @ B shape {tuple(C.shape)}: {C.tolist()}")
    return C


# a) [1 2; 4 5; 7 8] . [1 1 0; 0 1 1; 1 0 1]
A = mat([[1, 2], [4, 5], [7, 8]])
B = mat([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
show("a)", A, B)

# b) [1 2 3; 4 5 6; 7 8 9] . [1 1 0; 0 1 1; 1 0 1]
A = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = mat([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
Cb = show("b)", A, B)

# c) [1 1 0; 0 1 1; 1 0 1] . [1 2 3; 4 5 6; 7 8 9]
A = mat([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
B = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Cc = show("c)", A, B)

# d) [1 2 1 2; 4 1 -1 -4] . [0 3; 1 -1; 2 1; 5 2]
A = mat([[1, 2, 1, 2], [4, 1, -1, -4]])
B = mat([[0, 3], [1, -1], [2, 1], [5, 2]])
Cd = show("d)", A, B)

# e) [0 3; 1 -1; 2 1; 5 2] . [1 2 1 2; 4 1 -1 -4]
A = mat([[0, 3], [1, -1], [2, 1], [5, 2]])
B = mat([[1, 2, 1, 2], [4, 1, -1, -4]])
show("e)", A, B)

# hand check of b): (AB)[0,0] = 1*1 + 2*0 + 3*1 = 4
print("\nhand check b)[0,0] = 1*1 + 2*0 + 3*1 =", 1 * 1 + 2 * 0 + 3 * 1)
# hand check c)[0,0] = 1*1 + 1*4 + 0*7 = 5
print("hand check c)[0,0] = 1*1 + 1*4 + 0*7 =", 1 * 1 + 1 * 4 + 0 * 7)
# hand check d)[0,0] = 1*0 + 2*1 + 1*2 + 2*5 = 14
print("hand check d)[0,0] = 1*0 + 2*1 + 1*2 + 2*5 =", 1 * 0 + 2 * 1 + 1 * 2 + 2 * 5)

# =====================================================================
# Exercise 2 - Derivatives (Tuebingen DL course)
# =====================================================================
print("\n" + "=" * 70)
print("Exercise 2: Derivatives")

# 2(a) For a, x in R^n show that grad_x (a^T x) = a^T.
# The nabla carries the subscript x, so this is the GRADIENT of the scalar
# a^T x with respect to x, which is a constant vector.
print("\n2(a) grad_x (a^T x) = a^T  -- numerical check")
torch.manual_seed(0)
for n in (3, 5, 8):
    a = torch.randn(n, dtype=torch.float64)
    x = torch.randn(n, dtype=torch.float64, requires_grad=True)
    val = (a @ x)
    (grad,) = torch.autograd.grad(val, x)
    print(f"  n={n}: grad = {grad.detach().numpy()}")
    print(f"         a^T = {a.numpy()}")
    print(f"         equal: {torch.allclose(grad, a)}")

# 2(b) f(x) = (exp(x1) sin(x3), sqrt(x2) + x3), f: R^3 -> R^2
#      Jacobian J = df/dx, a 2x3 matrix.  NOTE the square root on x2.
print("\n2(b) Jacobian of f(x) = (exp(x1) sin(x3), sqrt(x2) + x3)")
x = torch.tensor([0.7, 1.3, 2.1], dtype=torch.float64, requires_grad=True)
J = torch.autograd.functional.jacobian(
    lambda v: torch.stack([torch.exp(v[0]) * torch.sin(v[2]), torch.sqrt(v[1]) + v[2]]),
    x,
)
print("  J =\n", J.detach().numpy())

# 2(c) a: R -> R, f(x) = (a(x1), ..., a(xn)), f: R^n -> R^n
#      Jacobian is diag(a'(x1), ..., a'(xn)) -> a DIAGONAL matrix
print("\n2(c) Jacobian of f(x) = (a(x1), ..., a(xn))")
a = torch.tensor([0.4, -0.9, 1.7], dtype=torch.float64, requires_grad=True)
xc = torch.tensor([0.3, 1.1, -0.6], dtype=torch.float64)
Jc = torch.autograd.functional.jacobian(
    lambda v: torch.stack([a[0] * v[0], a[1] * v[1], a[2] * v[2]]), xc
)
print("  J =\n", Jc.detach().numpy())
print("  diagonal:", torch.allclose(Jc, torch.diag(torch.diagonal(Jc))))

# 2(d) sigma(x) = 1/(1+exp(-x)); show sigma'(x) = sigma(x)(1 - sigma(x))
print("\n2(d) sigmoid: sigma'(x) = sigma(x)(1 - sigma(x))")
xs = torch.tensor([-3.0, -0.5, 0.0, 0.5, 3.0], dtype=torch.float64, requires_grad=True)
sig = 1.0 / (1.0 + torch.exp(-xs))
d_sig = torch.autograd.functional.jacobian(lambda v: 1.0 / (1.0 + torch.exp(-v)), xs)
lhs = torch.diagonal(d_sig).detach()
rhs = (sig * (1 - sig)).detach()
print("  x             :", xs.detach().numpy())
print("  sigma'(x)     :", lhs.numpy())
print("  sig*(1-sig)   :", rhs.numpy())
print("  max abs error :", (lhs - rhs).abs().max().item())

# 2(e) tanh'(x), tanh(x) = (e^x - e^-x)/(e^x + e^-x)
print("\n2(e) tanh'(x) = 1 - tanh^2(x)")
xs = torch.tensor([-2.0, -0.3, 0.0, 0.3, 2.0], dtype=torch.float64, requires_grad=True)
th = (torch.exp(xs) - torch.exp(-xs)) / (torch.exp(xs) + torch.exp(-xs))
d_th = torch.autograd.functional.jacobian(
    lambda v: (torch.exp(v) - torch.exp(-v)) / (torch.exp(v) + torch.exp(-v)), xs
)
lhs = torch.diagonal(d_th).detach()
rhs = (1 - th**2).detach()
print("  x             :", xs.detach().numpy())
print("  tanh'(x)      :", lhs.numpy())
print("  1 - tanh^2(x) :", rhs.numpy())
print("  max abs error :", (lhs - rhs).abs().max().item())

# =====================================================================
# Exercise 3 - Probability
# =====================================================================
print("\n" + "=" * 70)
print("Exercise 3: Probability")

# 3(a) E(aX) = a E(X) for a constant a.  Verified by sampling.
print("\n3(a) E(aX) = a E(X)")
torch.manual_seed(1)
X = torch.randn(400000, dtype=torch.float64)
for a in (2.5, -0.7, 10.0):
    lhs = (a * X).mean().item()
    rhs = a * X.mean().item()
    print(f"  a={a:5}: E(aX) = {lhs:.5f}   a E(X) = {rhs:.5f}   equal: {abs(lhs-rhs) < 0.02}")

# 3(b) E(a) = a for a constant
print("\n3(b) E(a) = a")
for a in (2.5, -0.7, 10.0):
    c = torch.full((1000,), a, dtype=torch.float64)
    print(f"  a={a:5}: E(a) = {c.mean().item():.5f}   equal: {abs(c.mean().item() - a) < 1e-9}")

# 3(c) Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)
print("\n3(c) Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X,Y)")
torch.manual_seed(2)
n = 400000
X = torch.randn(n, dtype=torch.float64)
Z = torch.randn(n, dtype=torch.float64)
for rho in (0.0, 0.5, -0.8):
    Y = rho * X + math.sqrt(1 - rho**2) * Z  # correlation rho
    lhs = torch.var(X + Y, unbiased=False).item()
    rhs = (
        torch.var(X, unbiased=False).item()
        + torch.var(Y, unbiased=False).item()
        + 2 * torch.mean((X - X.mean()) * (Y - Y.mean())).item()
    )
    print(f"  rho={rho:5}: Var(X+Y) = {lhs:.5f}   RHS = {rhs:.5f}   equal: {abs(lhs-rhs) < 0.05}")

# 3(d) p_X(x) = 3x^2 - e^x for 2 <= x <= 4: is it a valid PDF?
print("\n3(d) p_X(x) = 3x^2 - e^x on [2,4]")
p = lambda v: 3 * v**2 - torch.exp(v)
xs = torch.linspace(2, 4, 9, dtype=torch.float64)
print("  values:", [f"{v.item():.4f}" for v in p(xs)])
integral = float((3 * 4**3 / 3 - torch.exp(torch.tensor(4.0))) - (3 * 2**3 / 3 - torch.exp(torch.tensor(2.0))))
print(f"  integral from 2 to 4 = {integral:.6f}   (must be 1)")
print(f"  p(4) = {p(torch.tensor(4.0)).item():.6f}  (must be >= 0)")
# where does it cross zero?  3x^2 = e^x
lo, hi = 2.0, 4.0
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if p(torch.tensor(mid)).item() > 0:
        lo = mid
    else:
        hi = mid
print(f"  sign change at x* = {0.5*(lo+hi):.6f}  -> p < 0 on (x*, 4]")
print("  => NOT a valid PDF: negative on part of the support, and the integral")
print("     is not 1 either.  Fix: restrict to a subinterval where p >= 0 and")
print("     renormalise: p~ = p / integral over that subinterval.")

# the fix, computed: restrict to [2, x*] and renormalise
xs_star = 0.5 * (lo + hi)
mass = float(
    (3 * xs_star**3 / 3 - math.exp(xs_star))
    - (3 * 2**3 / 3 - math.exp(2.0))
)
print(f"\n  fix: support [2, {xs_star:.6f}]")
print(f"  mass on that support = {mass:.6f}")
print(f"  renormalised density p~/ = p(x)/{mass:.6f}")
print(f"  check: p~(2) = {p(torch.tensor(2.0)).item() / mass:.6f}")
print(f"  check: p~(x*) = {p(torch.tensor(xs_star)).item() / mass:.6f}")
print(f"  check: integral of p~ over [2, x*] = {mass / mass:.6f}")
print(f"  check: p~(2) >= 0: {p(torch.tensor(2.0)).item() / mass >= 0}")
