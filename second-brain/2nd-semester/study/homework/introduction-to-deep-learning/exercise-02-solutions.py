"""Exercise 2 — Introduction to PyTorch: polynomial regression in PyTorch.

Implements every task of 02-hw-intro-pytorch-tasks.ipynb and prints the real
numbers, so the homework page can quote measured values rather than predicted
ones.

Run:  python exercise-02-solutions.py
"""

import torch
from torch import nn

# ---------------------------------------------------------------- task 1
print("=" * 70)
print("torch version:", torch.__version__)
print("cuda available:", torch.cuda.is_available())

# ---------------------------------------------------------------- task 4/5 data
torch.manual_seed(1234)
torch.use_deterministic_algorithms(True)
if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = False

n_points = 10


def make_targets(x):
    return x + 0.5 * x**2 - 0.25 * x**3 + 0.4 * torch.randn_like(x)


x = torch.linspace(-2, 3, n_points).reshape(-1, 1)
y = make_targets(x)

x_val = torch.linspace(-2, 3, 25).reshape(-1, 1) + 0.1 * torch.randn((25, 1))
y_val = make_targets(x_val)

# ---------------------------------------------------------------- task 2
class PolyRegression(nn.Module):
    """f(x, w) = w_0 + w_1 x + ... + w_q x^q, one input feature."""

    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree
        # q+1 basis functions (1, x, x^2, ..., x^q) become the layer's inputs,
        # one output: the layer's weights ARE the polynomial coefficients.
        self.linear = nn.Linear(degree + 1, 1, bias=True)

    def forward(self, x):
        # (N, 1) -> (N, degree+1): columns x^0 .. x^degree
        powers = torch.cat(
            [torch.pow(x, j) for j in range(self.degree + 1)], dim=1
        )
        return self.linear(powers)  # (N, degree+1) -> (N, 1)


# test the model works (the notebook's own assertion)
model = PolyRegression(3)
out = model(x)
assert out.shape == (n_points, 1), (
    f"Expected output shape {(n_points, 1)}, got {tuple(out.shape)}"
)
print("model(x).shape =", tuple(out.shape))

# ---------------------------------------------------------------- task 3
def train_one_epoch(x, y, model, optimizer, loss_func):
    """Optimizes the parameters of model with one pass over the training data."""
    optimizer.zero_grad()
    prediction = model(x)
    loss = loss_func(prediction, y)
    loss.backward()
    optimizer.step()
    return loss.item()


# ---------------------------------------------------------------- task 4
def evaluate(x, y, model, loss_func):
    """Computes the loss over validation data (no gradient tracking)."""
    with torch.no_grad():
        prediction = model(x)
        loss = loss_func(prediction, y)
    return loss.item()


# ---------------------------------------------------------------- task 5
def train(degree, n_epochs=5000, lr=5e-3, seed=123, check_every=500):
    """Train a degree-q model; report final train and validation loss."""
    torch.manual_seed(seed)
    m = PolyRegression(degree)
    optimizer = torch.optim.Adam(m.parameters(), lr=lr)
    loss_func = nn.MSELoss()

    history = []
    for epoch in range(n_epochs):
        train_loss = train_one_epoch(x, y, m, optimizer, loss_func)
        if (epoch + 1) % check_every == 0:
            val_loss = evaluate(x_val, y_val, m, loss_func)
            history.append((epoch + 1, train_loss, val_loss))

    final_train = train_one_epoch(x, y, m, optimizer, loss_func)  # not used
    return m, history


def full_report(degree, n_epochs=5000, lr=5e-3, seed=123):
    """Train from scratch and return (final train loss, final val loss, model)."""
    torch.manual_seed(seed)
    m = PolyRegression(degree)
    optimizer = torch.optim.Adam(m.parameters(), lr=lr)
    loss_func = nn.MSELoss()

    last_train = None
    for epoch in range(n_epochs):
        last_train = train_one_epoch(x, y, m, optimizer, loss_func)
    last_val = evaluate(x_val, y_val, m, loss_func)
    return last_train, last_val, m


print("=" * 70)
print("task 5: degree-3 model, Adam lr=5e-3")
torch.manual_seed(123)
m3 = PolyRegression(3)
opt3 = torch.optim.Adam(m3.parameters(), lr=5e-3)
lf = nn.MSELoss()
for epoch in range(5000):
    tl = train_one_epoch(x, y, m3, opt3, lf)
    if (epoch + 1) % 1000 == 0:
        vl = evaluate(x_val, y_val, m3, lf)
        print(f"  epoch {epoch+1:5d}  train={tl:.6f}  val={vl:.6f}")
final_train3 = evaluate(x, y, m3, lf)
final_val3 = evaluate(x_val, y_val, m3, lf)
print(f"  degree 3 FINAL: train={final_train3:.6f}  val={final_val3:.6f}")

# ---------------------------------------------------------------- task 8
print("=" * 70)
print("task 8.1: degree 9 (same seed, same optimiser settings)")
tr9, va9, m9 = full_report(9)
print(f"  degree 9 FINAL: train={tr9:.6f}  val={va9:.6f}")

print("task 8.2: degree 1 and degree 2")
tr1, va1, m1 = full_report(1)
print(f"  degree 1 FINAL: train={tr1:.6f}  val={va1:.6f}")
tr2, va2, m2 = full_report(2)
print(f"  degree 2 FINAL: train={tr2:.6f}  val={va2:.6f}")

# converged reference: least squares on the transformed features
print("=" * 70)
print("reference: least-squares optimum for each degree (torch.linalg.lstsq)")
for q in (1, 2, 3, 9):
    P = torch.cat([torch.pow(x, j) for j in range(q + 1)], dim=1)  # (N, q+1)
    sol = torch.linalg.lstsq(P, y.squeeze(1)).solution
    pred = P @ sol
    train_ls = ((pred - y.squeeze(1)) ** 2).mean().item()
    Pv = torch.cat([torch.pow(x_val, j) for j in range(q + 1)], dim=1)
    predv = Pv @ sol
    val_ls = ((predv - y_val.squeeze(1)) ** 2).mean().item()
    print(f"  degree {q}: lstsq train={train_ls:.6f}  val={val_ls:.6f}")

# degree 9 with the default settings did not converge (the notebook's hint 3
# says a higher-degree model must reach a training loss at most as large as
# the degree-3 model, so a HIGHER training loss means the optimisation is
# unfinished). Retry with a smaller learning rate and more epochs.
print("=" * 70)
print("degree 9 retried with lr=1e-4 and 50000 epochs (convergence attempt)")
tr9b, va9b, m9b = full_report(9, n_epochs=50000, lr=1e-4)
print(f"  degree 9 (lr=1e-4, 50000 ep) FINAL: train={tr9b:.6f}  val={va9b:.6f}")

# ---------------------------------------------------------------- task 6
print("=" * 70)
print("task 6: three hyperparameters used in this code")
print("  1. learning rate (5e-3 for Adam)")
print("  2. number of epochs (5000)")
print("  3. polynomial degree q")

# ---------------------------------------------------------------- task 9
print("=" * 70)
print("task 9: task classification")
print("  supervised regression (numeric target, squared-error loss)")
