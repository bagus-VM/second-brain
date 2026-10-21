---
title: "The Neural Network Training Loop"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[pytorch-tensors-and-autograd]]", "[[linear-regression]]"]
---

## One-line Summary

Training a neural network is a fixed five-step cycle — forward pass, loss, zero the gradients, backpropagate, step the optimiser — repeated until the loss stops moving.

## Core Intuition

The demo notebook does not present the training loop as an algorithm to be optimised, executed fast, or parallelised. It presents it as a contract with four moving parts: a model, a loss function, an optimiser, and the data. The loop is the choreography that keeps those four in agreement, and the demo's value is that it makes every step individually visible and separately removable.

The pedagogy is subtraction. The notebook asks you to "comment out 'optimizer.zero_grad()' and run the cell below multiple times, then explain what u observe", and adds a second task: "observe parameter changes based on learning rate changes". The loop is a five-line block whose failure modes are more instructive than a dozen alternatives. The second additional task in the homework notebook then asks the student to implement the loop inside `train_one_epoch(x, y, model, optimizer, loss_func)`, so that the abstraction is written rather than copied.

The ordering of the five steps is not arbitrary. Steps 1 and 2 compute *values*: the prediction and how bad it is. Steps 3, 4 and 5 compute and apply *changes*: reset the gradient buffers, fill them by backpropagation, move the parameters. The separation between step 4 and step 5 is the one that trips people up: the backward pass computes derivatives and stores them; the optimiser step is what actually moves the weights.

## Formal Definition / Statement

The five general training steps, from the demo notebook:

1. **Forward pass.** `output = model(x)` — evaluate the model on the batch.
2. **Compute loss.** `loss = loss_func(output, y)` — here `nn.MSELoss()`.
3. **Zero the gradients.** `optimizer.zero_grad()` — "reset gradients, i.e., set .grad attribute to None".
4. **Backpropagate.** `loss.backward()` — "Compute gradients (populate .grad attributes again)".
5. **Optimisation step.** `optimizer.step()` — "Optimization step (update parameters)".

The notebook's own code, verbatim in structure:

```python
model_pt = LinearRegressionPyTorch(x.size(-1))

optimizer = torch.optim.SGD(model_pt.parameters(), lr=5e-4)
loss_func = nn.MSELoss()
n_epochs = 20
for epoch in range(n_epochs):
    output = model_pt(x)            # Step 1: Forward pass
    loss = loss_func(output, y)      # Step 2: Compute loss, here: MSE
    optimizer.zero_grad()            # Step 3: reset gradients
    loss.backward()                  # Step 4: Compute gradients
    optimizer.step()                 # Step 5: Optimization step (update parameters)
    print(f"{epoch=}: loss={loss.item()}")
    preds_epochs.append(output.detach())
```

The comment the notebook attaches to step 3 is the conceptual anchor of the whole loop: "PyTorch accumulates (sums) the gradients on subsequent backward passes, thus we set the gradients to zero before we perform backpropagation. Why accumulate? Well, in some cases we want this behavior: e.g., RNNs, compute gradient over loss summed over multiple mini-batches ...". So `zero_grad()` is not a reset of an accident but a decision: the default behaviour of `backward()` is to add into `.grad`, and the loop overrides that by clearing first.

A second boundary condition comes from the same notebook: "backward never updates the parameters - only optimizer.step() does". And a third: the forward pass must be under `torch.no_grad()` when it is an evaluation, because "recording is not free: it takes up memory".

## Key Properties

- **The loop is invariant under batching.** Steps 1–5 are per-batch; the epoch is the outer repetition. `n_epochs` counts passes over the data, and `optimizer.step()` fires once per batch, not once per epoch.
- **Gradients accumulate by default.** `backward()` sums into `.grad`; `zero_grad()` sets the attribute to `None`. The notebook's RNN example shows accumulation is a feature you sometimes want, not a bug you always suppress.
- **`backward()` and `step()` are different acts.** One differentiates; the other moves parameters according to the optimiser's own rule — SGD here, Adam in the homework.
- **`.grad` is storage, not a value.** The optimizer holds references to the model's parameters and writes new values into them. `optimizer.zero_grad()` is the mechanism that keeps `.grad` from meaning "the sum of every gradient since the beginning of time".
- **Loss must be a scalar.** `backward()` on the loss requires a single number. In the demo, `preds.sum()` is used "only because backwards needs a single value... not really a meaningful loss".
- **`output.detach()` is needed to keep history.** Storing the raw output for plotting would otherwise retain the whole computation graph in memory for every epoch.
- **The loop is where the linear algebra meets the optimisation.** Every step is the machinery of [[gradient-descent-for-neural-networks]] run once; the loop exists only to repeat it in the right order.

## Worked Example

**The data.** Synthetic, with a fixed seed for reproducibility:

```python
torch.manual_seed(123)
x = 10 + 20 * torch.rand((30,)).to(dtype=torch.float)
x = x.reshape(-1, 1)
y = 2.7 * x + 2 * torch.randn_like(x) + 5
```

The data-generating process has true intercept 5 and true slope 2.7; the `*2` on the Gaussian noise makes its standard deviation 2, not 1.

**The run.** `SGD(lr=5e-4)`, `MSELoss()`, 20 epochs, printed losses:

```
epoch=0: loss=5910.3193359375
epoch=1: loss=1652.3736572265625
epoch=2: loss=465.6243896484375
epoch=3: loss=134.8601837158203
epoch=4: loss=42.671321868896484
epoch=5: loss=16.976774215698242
epoch=6: loss=9.81511116027832
epoch=7: loss=7.818855285644531
epoch=8: loss=7.262251853942871
epoch=9: loss=7.106907844543457
epoch=10: loss=7.063401699066162
epoch=11: loss=7.0510687828063965
epoch=12: loss=7.0474042892456055
epoch=13: loss=7.046181678771973
epoch=14: loss=7.045633792877197
epoch=15: loss=7.045263767242432
epoch=16: loss=7.044958591461182
epoch=17: loss=7.044651508331299
epoch=18: loss=7.044351100921631
epoch=19: loss=7.044068813323975
```

The trajectory itself is the lesson: the loss falls by roughly two orders of magnitude in the first six epochs and then flattens into a slow crawl towards roughly 7.044. That plateau is **not** the noise floor. The target carries Gaussian noise with standard deviation 2, so the irreducible MSE of a perfect linear fit is 2² = 4, and the closed-form fit on the same data reaches 4.164. The demo's SGD run stops at 7.044 with parameters `tensor([[2.9045]])` for the weight and `tensor([0.2494])` for the bias — the weight is close to the true 2.7, but the bias is nowhere near the true 5, and 20 epochs of `lr=5e-4` have not moved it there. The plateau is slow convergence, not the floor.

**What the closed form would have given.** The demo contrasts this with the NumPy route, where the same data is fitted by `w = np.linalg.inv(X.T @ X) @ X.T @ y` and the parameters come out as `[[2.67754453], [5.42394903]]` — close to the generating values $[2.7, 5]$. The notebook's verdict: "Calculating the gradient manually is cumbersome / Not all equation systems have analytical solutions / Hence, PyTorch helps us by computing gradients automatically and giving us the tools to optimize functions numerically."

**The exercise the notebook sets.** Delete `optimizer.zero_grad()` and rerun the cell. The gradient at step $t$ becomes the sum of the gradients of all previous steps, so the effective step size grows without bound; the loss stops descending monotonically and eventually diverges or oscillates. The second exercise, varying the learning rate, shows the same loop with `lr=5e-4` versus, say, `lr=5e-2`: same code, and the parameter update is scaled by $\alpha$ in the update rule $w^{(t+1)} \leftarrow w^t - \alpha \nabla E(w^t)$.

## Common Pitfalls

- **Believing `loss.backward()` trains the model.** It computes gradients and writes them into `.grad`. If you never call `optimizer.step()`, the parameters never move and the loss curve is flat even though gradients exist.
- **Forgetting `optimizer.zero_grad()`.** Gradients accumulate; the effective learning rate silently increases every step and training destabilises.
- **Zeroing gradients after the backward pass instead of before.** The order in the loop is not a style choice: the reset must precede the backward pass that fills the buffers.
- **Calling `backward()` on a non-scalar output.** It raises; the loss must be reduced to a single number first.
- **Evaluating without `torch.no_grad()`.** The graph is built and kept for no reason, and the memory cost grows with every epoch.
- **Storing graph-connected outputs in a list.** `output.detach()` is what keeps the epoch-by-epoch predictions cheap to hold.
- **Reading the plateau as the noise floor.** It is not. The floor for this data-generating process is 4 (noise variance 2²); the demo's 7.044 sits above it because 20 epochs of `lr=5e-4` leave the bias far from its true value. A loss curve's *shape* is a property of the optimiser and the schedule, not of SGD in general.
- **Forgetting that the demo prints the loss computed *before* the update.** The value printed at epoch $t$ reflects the parameters as they were at the start of epoch $t$.

## Connections

- [[pytorch-tensors-and-autograd]] — steps 1 and 4 depend on it: the forward pass records a graph, and `backward()` walks it to fill `.grad`.
- [[gradient-descent-for-neural-networks]] — `optimizer.step()` is the implementation of the update rule; the loop is that rule repeated in the right order.
- [[linear-regression]] — the model in the demo is a linear regression with two parameters; the loop turns the closed-form solution into an iterative one.
- [[polynomial-regression-and-overfitting]] — the homework asks you to reimplement this loop inside `train_one_epoch` and to add validation checks for overfitting.
- [[feature-normalization]] — the demo's `x` spans $[10, 30)$ while the polynomial homework's `x` spans $[-2, 3)$; feature scaling is what makes learning rates transferable between them.
- [[ml-pipeline-scikit-learn]] — the scikit-learn counterpart: `fit` in one call versus five explicit steps, and why the explicit version teaches you more.
- [[deep-learning-course-roadmap]] — week 2 of fifteen: the loop is introduced here and refined in weeks 4, 5 and 8 (autodiff and SGD, MLPs, optimisers and regularisation).

## Open Questions

- The printed final parameters (`tensor([[2.9045]])` and `tensor([0.2494])`) do not match the generating values $[2.7, 5]$, and the plateau of roughly 7.04 sits well above the noise floor of 4 that the closed form reaches. The likely cause is simply 20 epochs of `lr=5e-4` being too few to move the bias from its random initialisation, but the notebook does not say, and it does not record a longer run.
- The additional task asks you to comment out `zero_grad()` and "explain what u observe", but no expected answer is recorded. The precise failure mode — divergence, oscillation, or silent degradation — depends on the learning rate and is not stated.
- The notebook uses the whole dataset in every epoch, with no mini-batching, so `optimizer.step()` fires 20 times in total. Whether the "epoch" concept changes once mini-batches are introduced is not addressed.
- The demo stores `preds_epochs` for plotting but never uses a validation split. How the loop should be structured to detect overfitting is left to the homework.
