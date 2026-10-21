---
title: "PyTorch Tensors and Automatic Differentiation"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[python-for-deep-learning]]", "[[linear-algebra-for-deep-learning]]"]
---

## One-line Summary

PyTorch gives you NumPy-style array arithmetic on tensors that remember the function they were produced by, so that gradients of any composition of operations come out of a single `backward()` call instead of a hand derivation.

## Core Intuition

The demo notebook, "Introduction to PyTorch", is built on four claims. PyTorch is "Similar to NumPy: a library for array (tensor) operations", it comes "with GPU support", it has an "Automatic differentiation engine", and it ships a "Library of neural network components" plus a "Library of optimization tools". Everything in the notebook follows from the first and third claims combined: if tensors behave like arrays and record how they were computed, then the derivative of a whole neural network is a mechanical consequence rather than a derivation.

The recording mechanism is the *computation graph*. As the notebook puts it: PyTorch "keeps track of the so-called 'computation graph' ... This graph records every operation on (specific) tensors, thus traces the function that the tensors are used in." The graph is dynamic and "updated as the NN manipulates the input", because an NN "manipulat[es] an input by matrix-multiplications with weight matrices and additions with bias vectors; followed by nonlinear activation functions! (else, the network would collapse into a single linear map)".

The practical consequence is stated in the notebook's own summary of why PyTorch exists: "Calculating the gradient manually is cumbersome / Not all equation systems have analytical solutions / Hence, PyTorch helps us by computing gradients automatically and giving us the tools to optimize functions numerically."

## Formal Definition / Statement

**The tensor.** The `torch.Tensor` generalises the NumPy array: 1-D tensor :: vector, 2-D tensor :: matrix. Creation names largely coincide with NumPy — `torch.zeros(size=(n_rows, n_cols))`, `torch.ones_like(input=zeros_torch)`, `torch.arange(24).reshape(4, 6)`.

**Indexing.** `<start:stop:step>` notation with start inclusive and stop exclusive works identically in both libraries, and slicing creates a "view" instead of a copy. `x_np[1:5:2, :]` and `x_torch[1:5:2, :]` both return rows 1 and 3.

**The difference from NumPy.** Indexing a NumPy array yields a Python/NumPy scalar (`numpy.int64`); indexing a tensor yields a 0-dim `torch.Tensor`. `x_torch[0, 0]` prints `tensor(0)`; `x_torch[0, 0].item()` prints `0` as a Python `int`.

**Shape.** `x_np.shape` → `(4, 6)`; `x_torch.shape` → `torch.Size([4, 6])`. `x_torch.size(dim=1)` → `6`, `x_torch.shape[1]` → `6`.

**Conversion and shared memory.** `torch.from_numpy(x_np)` and `x_torch.numpy()` convert both ways — and they share memory, so mutating `x_np[0, 0] = -1000` also changes `x_torch`. The demo notebook's comment points back at the previous exercise: "call/pass by reference".

**Operations.** `x @ x` is matrix multiplication, `x + x` is element-wise addition. In-place variants carry a trailing underscore: `x.add(x)` returns a new tensor and leaves `x` unchanged, `x.add_(x)` modifies `x` in place and saves memory.

**Automatic differentiation.** A tensor participates in gradient computation when it is created with `requires_grad=True`. PyTorch then attaches to every intermediate a `grad_fn` naming the backward rule that produced it: `<SubBackward0>`, `<PowBackward0>`, `<SumBackward0>`, `<AddmmBackward0>`.

**The update rule that autograd feeds.** The notebook states it as

$$w^{(t+1)} \leftarrow w^t - \alpha \cdot \nabla E(w^t)$$

where $t+1$ indicates the weight update (one time step) and $\alpha$ is the learning rate. All gradient descent needs are "the gradient values of the parameters, and access to the parameters itself. We have both with PyTorch."

## Key Properties

- **Devices are explicit and strict.** A tensor lives on a device: `torch.device("cpu")` vs `torch.device("cuda")`. Tensors are moved with `.to(device)` or created with `device=`. "Operations require both tensors to be on the same device" — mixing a CUDA tensor with a CPU tensor raises.
- **GPU economics.** A GPU is "a processor with *many* cores (think thousands), which however are limited in their instruction set" (Kevin Krewell, 2009). CPU: several cores, low latency, good for serial processing, a handful of operations at once. GPU: many cores (the NVIDIA H100 has 456 "Tensor Cores"), high throughput, good for parallel processing, thousands of operations at once. "GPUs can handle tens of thousands of concurrent threads", and since NN operations are highly parallelizable, "Speedup can be up to two magnitudes."
- **Install the right build.** CUDA for NVIDIA GPUs, ROCm for AMD. `torch.cuda.is_available()` reports whether GPU support is compiled in and a GPU is present; the demo's run prints `False`.
- **Only leaf tensors store gradients.** A leaf is a tensor with no further dependencies. The notebook explains why: "The gradient of the loss w.r.t. the weights of the NN is what the optimizer needs. Intermediate computations have no further use once they are propagated back to the input". `a.grad` on a non-leaf prints `None`; `.retain_grad()` is the escape hatch if you truly need it.
- **`backward()` computes, it does not update.** After `loss.backward()` the weight is unchanged: "backward only computes the gradients, it never updates the parameters!"
- **Recording is not free.** "Also, the recording is not free: it takes up memory." `torch.no_grad()` — context manager or function decorator — turns recording off, which is what evaluation needs.
- **The module API.** `nn.Linear(n_features, 1, bias=True)` registers its parameters automatically as trainable (`requires_grad=True`); `named_parameters()` yields `linear.weight` and `linear.bias`; `forward()` defines how input becomes output. `super().__init__()` must come first.

## Worked Example

**Tracing the chain by hand.** The notebook defines $c(v) = \sum_i (v_i - 2)^2$:

```python
v = torch.ones(3, requires_grad=True)
a = v - 2
b = a**2
c = b.sum()
```

The prints show the graph attached: `tensor([-1., -1., -1.], grad_fn=<SubBackward0>)`, `tensor([1., 1., 1.], grad_fn=<PowBackward0>)`, `tensor(3., grad_fn=<SumBackward0>)`.

By the chain rule, $\frac{\partial c}{\partial v_i} = \frac{\partial c}{\partial b_i}\frac{\partial b_i}{\partial a_i}\frac{\partial a_i}{\partial v_i}$, with $\frac{\partial a_i}{\partial v_i} = 1$, $\frac{\partial b_i}{\partial a_i} = 2a_i$, $\frac{\partial c}{\partial b_i} = 1$. Hence $\frac{\partial c}{\partial v_i} = 2(v_i - 2) = -2$ for $v_i = 1$. `c.backward()` then populates `.grad`, and `print(v.grad)` gives

```
tensor([-2., -2., -2.])
```

which matches the derivation to the digit. `print(a.grad)` prints `None` — `a` is not a leaf.

**A module and its graph.** `LinearRegressionPyTorch` wraps a single `nn.Linear`:

```python
class LinearRegressionPyTorch(nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.linear = nn.Linear(n_features, 1, bias=True)  # x*A^T + b

    def forward(self, x):
        return self.linear(x)
```

`named_parameters()` prints `linear.weight` as `tensor([[0.0740]], requires_grad=True)` and `linear.bias` as `tensor([0.6886], requires_grad=True)`. After a forward pass the output's last line ends in `grad_fn=<AddmmBackward0>`, "which shows that PyTorch stored the matrix multiply-add in the comp graph". After `preds.sum().backward()`, the weight is *still* `tensor([[0.0740]], requires_grad=True)` while `weight.grad` holds `tensor([[629.5720]])` — the gradient exists, the parameter has not moved.

**Evaluating without recording.** Under `with torch.no_grad():` the same model produces an output with no `grad_fn`, and `model_pt.linear.weight.grad` prints `None`; without the context manager it prints `tensor([[629.5720]])`. The notebook's decorated helper follows the same pattern:

```python
@torch.no_grad()
def eval(model, x_val, y_val):
    pred = model(x_val)
    return (pred - y_val).sum()
```

## Common Pitfalls

- **Expecting `backward()` to change the weights.** It computes gradients; only `optimizer.step()` updates parameters. The demo makes this point twice.
- **Treating `x_torch[0, 0]` as a number.** It is a 0-dim tensor; `.item()` converts it to a Python `int`.
- **Forgetting that `torch.from_numpy` shares memory.** The demo mutates `x_np[0, 0] = -1000` and watches `x_torch` change underneath it — the same reference semantics as the previous exercise.
- **Assuming slicing copies.** Slicing creates a view; writing into the view writes into the original.
- **Reading `a.grad` on a non-leaf tensor** and concluding autograd failed. It returns `None` by design; use `.retain_grad()` if you need it.
- **Leaving recording on during evaluation.** It wastes memory and produces a graph you never backpropagate through.
- **Mixing devices.** `cuda` tensor plus `cpu` tensor is an error, not a silent cast.
- **Forgetting `super().__init__()`** in an `nn.Module` subclass, which breaks parameter registration.
- **Assuming the demo's hardware.** `torch.__version__` prints `2.14.1+cu130` and `torch.cuda.is_available()` prints `False` on the machine that ran the notebook; your machine may differ.

## Connections

- [[python-for-deep-learning]] — the Python on which PyTorch and the `uv add torch` install run; the reference-passing semantics behind the shared-memory demo.
- [[linear-algebra-for-deep-learning]] — the operations PyTorch tensors perform: `x @ x` is the matmul written by hand in week 1, now in library form.
- [[neural-network-training-loop]] — autograd produces the gradients that the five-step loop consumes; `backward()` is step 4 of that loop.
- [[gradient-descent-for-neural-networks]] — the update rule `$w^{(t+1)} \leftarrow w^t - \alpha \nabla E(w^t)$` that the gradients feed directly.
- [[python-environment-management]] — the `uv` project and the CUDA-versus-CPU build decision that determines whether `torch.cuda.is_available()` is `True`.
- [[jupyter-notebook-state]] — the demo notebook's own failure mode: the output you read may not be the output your kernel produces.
- [[representation-learning]] — the conceptual payoff: every layer's weights are learned parameters, so the representation is trained by the same machinery.

## Open Questions

- The demo computes a gradient of `629.5720` for the weight by backpropagating `preds.sum()` on uninitialised predictions, and calls that "not really a meaningful loss". Which loss function's gradient would give a sensible step here, and how much does the choice matter at initialisation?
- The notebook states the chain rule for a scalar loss $c$ but does not say how `backward()` handles a non-scalar output, which is what a mean-squared-error loss on a batch of predictions is.
- `torch.cuda.is_available()` is `False` in the stored output and the CUDA cell raises `RuntimeError: Found no NVIDIA driver on your system`. Whether the course expects GPU work later, or whether the whole semester fits on CPU, is not stated.
- The graph is described as "dynamic" and "updated as the NN manipulates the input". How the memory of the graph is released, and whether it can be detached and rebuilt, is not covered in the demo.
