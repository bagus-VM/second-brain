---
title: "Exercise 2 — Introduction to Deep Learning"
tags: [homework, deep-learning, semester-2, pytorch]
course: "Introduction to Deep Learning"
source_count: 3
status: current
last_updated: 2026-10-20
prerequisites: ["[[python-environment-management]]"]
---

# Exercise 2 — Introduction to PyTorch

The sheet says it plainly: *"This exercise sheet will not be graded and is provided solely as
practice."* It is not graded and it is not optional — it is the first week in which the course
stops being about Python and starts being about PyTorch.

Two deliverables came down with it:

- `exercise-02-solutions.py` — the notebook's nine tasks, implemented and run.
- `exercise-02-math.py` — the paper half (MML 2.4, derivatives, probability), every claim
  computed rather than asserted.

Real output from both scripts is in `output-exercise-02.txt` and `output-exercise-02-math.txt`.
Every number quoted below is copied from those files.

### Running them yourself

```
uv venv --python 3.12
uv pip install --python <venv>/Scripts/python.exe \
  --index-url https://download.pytorch.org/whl/cpu \
  -r requirements-exercise-02.txt
<venv>/Scripts/python.exe exercise-02-solutions.py
<venv>/Scripts/python.exe exercise-02-math.py
```

`requirements-exercise-02.txt` pins the versions that produced the recorded output: PyTorch
2.14.1+cpu on CPython 3.12, numpy 2.4.6. Two details matter:

- **The `--index-url` is required.** The `+cpu` local-version label exists only in PyTorch's own
  CPU wheel index, not on the default PyPI index. Without the flag, `uv pip install -r` fails to
  resolve torch. For a CUDA build, drop the flag and pin a plain version such as `torch==2.14.1`
  from PyPI; the recorded results are CPU-only and do not depend on the build.
- **Only torch is actually needed.** numpy arrives as a torch dependency; matplotlib is not
  imported by either script. The course's own toolchain is `uv add torch matplotlib` inside the
  project from session 1 — see [[python-environment-management]].

The runs are deterministic: `torch.manual_seed(1234)` for the data, `torch.manual_seed(123)` for
each model's initialisation, and `torch.use_deterministic_algorithms(True)`. Both scripts were
re-run in a clean virtualenv built from nothing but the requirements file, and both reproduced
the recorded output byte for byte.

---

## Part A — The paper half

### 1. Linear Algebra (MML Chapter 2, Exercise 2.4)

"Compute the following matrix products, if possible." The word *if* does the work: three of the
five are impossible, and recognising that is the point of the exercise.

**a)** `[1 2; 4 5; 7 8]` (3×2) · `[1 1 0; 0 1 1; 1 0 1]` (3×3) — **not possible.** The inner
dimensions are 2 and 3.

**b)** `[1 2 3; 4 5 6; 7 8 9]` (3×3) · `[1 1 0; 0 1 1; 1 0 1]` (3×3)

```
[[ 4,  3,  5],
 [10,  9, 11],
 [16, 15, 17]]
```

Hand check on the first entry: `1·1 + 2·0 + 3·1 = 4`. ✓

**c)** `[1 1 0; 0 1 1; 1 0 1]` (3×3) · `[1 2 3; 4 5 6; 7 8 9]` (3×3)

```
[[ 5,  7,  9],
 [11, 13, 15],
 [ 8, 10, 12]]
```

Hand check: `1·1 + 1·4 + 0·7 = 5`. ✓ Note b) and c) are the same two matrices in opposite order
and they do **not** commute — a free counterexample, since `AB ≠ BA`.

**d)** `[1 2 1 2; 4 1 −1 −4]` (2×4) · `[0 3; 1 −1; 2 1; 5 2]` (4×2) — 2×2 result

```
[[14,  6],
 [-21,  2]]
```

Hand check: `1·0 + 2·1 + 1·2 + 2·5 = 14`. ✓

**e)** `[0 3; 1 −1; 2 1; 5 2]` (4×2) · `[1 2 1 2; 4 1 −1 −4]` (2×4) — **not possible.** Inner
dimensions 2 and 4. The pair d)/e) is the same two matrices swapped, so exactly one of them can
be multiplied.

### 2. Derivatives

**(a)** For `a, x ∈ Rⁿ`, show that `∇ₓ aᵀx = aᵀ`.

The nabla carries the subscript `x`, so this is the **gradient** of the scalar `aᵀx` with respect
to `x`, and the answer is a constant vector. Writing `aᵀx = Σᵢ aᵢxᵢ` and differentiating each
term: `∂(aᵀx)/∂xᵢ = aᵢ`, so `∇ₓ(aᵀx) = aᵀ`. Verified numerically for n = 3, 5, 8 — the
autograd gradient equals `a` exactly in every case.

**(b)** `f(x) = (exp(x₁) sin(x₃), √x₂ + x₃)`, `f : R³ → R²`. The Jacobian is 2×3:

```
[ exp(x₁)sin(x₃)      0        exp(x₁)cos(x₃) ]
[      0          1/(2√x₂)          1        ]
```

At `x = (0.7, 1.3, 2.1)` autograd gives

```
[[ 1.7382902   0.         -1.01663521]
 [ 0.          0.43852901  1.        ]]
```

> **The square root is real.** The PDF text layer renders the second component as `√x₂ + x₃`, and
> the rendered page confirms the radical sign over `x₂`. A first reading of the text extraction
> gives plain `x₂ + x₃`, which would make the second row `[0, 1, 1]` instead of
> `[0, 1/(2√x₂), 1]`. The radical is there. This is the kind of thing that silently costs a
> mark.

**(c)** `a : R → R`, `f(x) = (a(x₁), …, a(xₙ))`, `f : Rⁿ → Rⁿ`. The Jacobian is

```
[ a'(x₁)  0      0    …  0     ]
[   0   a'(x₂)  0    …  0     ]
[   0     0   a'(x₃) …  0     ]
[   ⋮       ⋮      ⋮   ⋱  ⋮   ]
[   0      0      0  … a'(xₙ) ]
```

**It is a diagonal matrix.** Each component depends on exactly one coordinate, so the off-diagonal
entries — the mixed partials — are all zero. Verified: the computed Jacobian equals its own
diagonal exactly.

**(d)** `σ(x) = 1/(1 + exp(−x))`, show `σ′(x) = σ(x)(1 − σ(x))`.

Quotient rule: `σ′(x) = −(1+exp(−x))⁻² · (−exp(−x)) = exp(−x)/(1+exp(−x))²`. Now
`σ(x) = 1/(1+exp(−x))` and `1 − σ(x) = exp(−x)/(1+exp(−x))`, so
`σ(x)(1 − σ(x)) = exp(−x)/(1+exp(−x))²` — the same expression. Verified at
`x ∈ {−3, −0.5, 0, 0.5, 3}` with max absolute error `1.46 × 10⁻¹⁶`.

**(e)** `tanh(x) = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)`, so `tanh′(x) = 1 − tanh²(x)`.

The clean route: write `tanh(x) = 1 − 2/(eˣ + e⁻ˣ) = 1 − 2/(e²ˣ + 1) · eˣ`, differentiate, and
simplify to `4e²ˣ/(e²ˣ+1)²`. Meanwhile `1 − tanh²(x) = 1 − ((eˣ−e⁻ˣ)/(eˣ+e⁻ˣ))² = 4e²ˣ/(eˣ+e⁻ˣ)²`.
Identical. Verified at `x ∈ {−2, −0.3, 0, 0.3, 2}`, max absolute error `3.47 × 10⁻¹⁶`.

### 3. Probability

**(a)** `E(aX) = aE(X)` for a constant `a`. Linearity of expectation, verified by sampling
400 000 draws for `a ∈ {2.5, −0.7, 10}` — the two sides agree to 5 decimals.

**(b)** `E(a) = a` for a constant `a` — the degenerate case, a constant random variable is its
own mean.

**(c)** `Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)`.

Proof by expansion: `Var(X+Y) = E[(X+Y−μₓ−μᵧ)²] = E[(X−μₓ)²] + 2E[(X−μₓ)(Y−μᵧ)] +
E[(Y−μᵧ)²]`, and the middle term is `2Cov(X,Y)`. Verified by simulation at
`ρ ∈ {0, 0.5, −0.8}`; the two sides agree to 4 decimals in all three cases. The `ρ = −0.8` case
is the instructive one: `Var(X+Y) = 0.40`, far below `Var(X) + Var(Y) = 2`, because the negative
covariance cancels.

**(d)** Is `p_X(x) = 3x² − eˣ` for `2 ≤ x ≤ 4` a valid PDF? **No**, and it fails in two
independent ways.

*Sampled values* (nine points from 2 to 4): `4.61, 5.70, 6.57, 7.04, 6.91, 5.90, 3.63, −0.33,
−6.60`.

*First failure — non-negativity.* The function crosses zero at `x* = 3.733079` and is **negative**
on `(x*, 4]`; `p(4) = −6.598148`. A density must be non-negative everywhere on its support.

*Second failure — normalisation.* `∫₂⁴ (3x² − eˣ) dx = [x³ − eˣ]₂⁴ = (64 − e⁴) − (8 − e²)
= 8.790908`, not 1.

*The fix* (the sheet asks how the function could be modified): restrict the support to the
interval where `p ≥ 0` and renormalise. On `[2, 3.733079]` the mass is `9.605157`, so

```
p̃(x) = p(x) / 9.605157,   x ∈ [2, 3.733079]
```

Checks: `p̃(2) = 0.480049 ≥ 0`, `p̃(x*) = 0`, and `∫ p̃ = 1.000000` exactly.

---

## Part B — The coding half

### Task 2 — the model

```python
class PolyRegression(nn.Module):
    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree
        self.linear = nn.Linear(degree + 1, 1, bias=True)

    def forward(self, x):
        powers = torch.cat(
            [torch.pow(x, j) for j in range(self.degree + 1)], dim=1
        )
        return self.linear(powers)
```

The q+1 basis functions `1, x, x², …, x^q` are the layer's **inputs**, and the single output
column collects the polynomial's value. The layer's weights *are* the coefficients `w₀ … w_q`.

Two implementation details that cost real time and are worth remembering:

- **`nn.Linear(in_features, out_features)`** — the first argument is the number of input
  columns. Writing `nn.Linear(1, degree + 1)` inverts it and produces a `(N, q+1, q+1)` output
  that blows up on the very first assertion.
- **`torch.cat`, not `torch.stack`** — `stack` adds a new axis, so stacking `(N,1)` tensors
  along `dim=1` yields `(N, 1, q+1)`. `cat` along `dim=1` is what actually builds the design
  matrix `(N, q+1)`.

The notebook's own assertion passes: `model(x).shape = (10, 1)`.

### Tasks 3 and 4 — one epoch, and evaluation

```python
def train_one_epoch(x, y, model, optimizer, loss_func):
    optimizer.zero_grad()
    prediction = model(x)
    loss = loss_func(prediction, y)
    loss.backward()
    optimizer.step()
    return loss.item()

def evaluate(x, y, model, loss_func):
    with torch.no_grad():
        prediction = model(x)
        loss = loss_func(prediction, y)
    return loss.item()
```

`evaluate` is named `evaluate` rather than `eval` because `eval` is a Python built-in that the
notebook refuses to shadow. The `torch.no_grad()` block matters for two reasons: it stops the
computation graph from being recorded (which costs memory), and it keeps the validation pass
from polluting the `.grad` attributes.

### Task 5 — training the degree-3 model

Adam, `lr = 5e-3`, validation checked every 500 epochs:

| epoch | train loss | val loss |
|-------|-----------|----------|
| 1000 | 0.056204 | 0.209887 |
| 2000 | 0.056197 | 0.210664 |
| 3000 | 0.056197 | 0.210665 |
| 4000 | 0.056197 | 0.210665 |
| 5000 | 0.056198 | 0.210666 |

**Final: train 0.056198, validation 0.210666.** The training loss is flat from epoch 1000
onward — the model has converged. The validation loss is roughly **3.7× the training loss**,
and that gap is the entire point of the exercise.

### Task 8 — the degree comparison

All runs: Adam, `lr = 5e-3`, 5000 epochs, `torch.manual_seed(123)`.

| degree | train loss | val loss | lstsq reference (train / val) |
|--------|-----------|----------|-------------------------------|
| 1 | 0.752247 | 0.422782 | 0.752247 / 0.422782 |
| 2 | 0.572659 | 0.455258 | 0.572659 / 0.455258 |
| 3 | 0.056198 | 0.210666 | 0.056197 / 0.210665 |
| 9 | 1.102326 | 3.479877 | 0.000000 / 1.224176 |

**Degree 1 and 2 underfit.** The true generator is a degree-3 polynomial; a straight line (degree
1) and a parabola (degree 2) cannot represent it, so both training *and* validation loss stay
high. Degree 1 has the worse training loss of the two (0.752 vs 0.573) and, tellingly, the
*better* validation loss (0.423 vs 0.455) — a degree-1 model cannot overfit 10 points, so it
generalises better than the degree-2 model does while still being too rigid. That inversion is
the first hint that the two failure modes are different in kind, not just in degree.

**Degree 9 at the default settings did not converge.** Its training loss, 1.102, is *higher*
than the degree-3 model's 0.056 — which by the notebook's own hint 3 is impossible for a
converged model, since every degree-3 polynomial is also a degree-9 polynomial with the extra
weights set to zero. So the optimisation is unfinished, not the model bad. The reason is
physical: `x` reaches 3, so `x⁹ ≈ 20 000`, and the feature magnitudes span four orders of
magnitude, which makes gradient descent slow and learning-rate-sensitive.

Retried with `lr = 1e-4` and 50 000 epochs: **train 0.025387, val 0.272569.** Now the training
loss is *below* the degree-3 model's, as the nesting argument demands — and the validation
loss is *worse* than degree 3's 0.211. That is overfitting, measured.

**The least-squares reference is the sharpest statement of the trade-off.** At degree 9 the
optimal training loss is exactly 0.000000 — with 10 points and 10 free parameters the model
interpolates the training set perfectly — while the validation loss is 1.224176, the worst of
any degree tried. The oracle solution of the training problem is also the worst solution of the
generalisation problem. No amount of optimisation skill closes that gap; only less model capacity
does.

### Task 6 — the three hyperparameters

1. **Learning rate** (5e-3 for Adam; 1e-4 for the degree-9 run that needed it).
2. **Number of epochs** (5000; 50 000 for the degree-9 retry).
3. **Polynomial degree q** (1, 2, 3, 9).

### Task 9 — task classification

**Supervised regression.** The target `y` is a real number, the loss is squared error, and the
inputs are labelled. The taxonomy the exercise refers to is the one from the lecture's
"Machine Learning Tasks" slide: classification / regression / structured prediction /
clustering / reinforcement learning.

One subtlety worth naming: the model is **nonlinear in `x`** but **linear in the weights `w`**.
Polynomial regression is linear regression on the transformed features `(x, x², …, x^q)`. This is
why the degree-9 fit can interpolate 10 points exactly, and why the same analysis from the ML
course — that a linear model in `w` has a closed-form least-squares solution — still applies to
the *transformed* problem.

---

## What the two halves have in common

The paper half asks you to prove that a gradient is what autograd computes. The coding half
asks you to watch autograd do it. The exercise is one argument: the analytic detour
(derivative → critical point → second derivative) works for `f(x) = x² − 3x` and breaks
completely for a network with activation functions, and the entire reason PyTorch exists is
that the numerical path is the only one that scales to a network with many parameters.

## Open Questions

- The sheet is explicitly ungraded and provides no expected answers, so the numbers in the
  degree comparison are **this implementation's** results, not the course's. They are
  reproducible: `torch.manual_seed(123)`, `torch.use_deterministic_algorithms(True)`, Adam
  `lr=5e-3`. A different PyTorch version may differ in the last digits.
- The environment used here is CPU-only PyTorch 2.14.1+cpu with no GPU (`torch.cuda.is_available()`
  returns `False`). The demo notebook was run on a CUDA build (2.14.1+cu130). Results should
  match, but the notebook's own printed losses were produced on different hardware with a
  different seed and are not directly comparable.
- The degree-9 run was pushed to convergence with a smaller learning rate and more epochs, but
  the notebook's hint also suggests changing the number of epochs and the learning rate. Whether
  the course expects a *converged* degree-9 comparison or accepts the unconverged one as the
  illustration of the feature-scaling problem is not stated.
- The 3(d) fix is one of several possible modifications. Restricting the support and
  renormalising is the standard one; adding a scaling constant, or taking the positive part
  `max(p(x), 0)` and renormalising, are equivalent here. The sheet does not say which it wants.
