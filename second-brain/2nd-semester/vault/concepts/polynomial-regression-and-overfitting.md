---
title: "Polynomial Regression and Overfitting"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[neural-network-training-loop]]", "[[linear-regression]]"]
---

## One-line Summary

Polynomial regression fits a linear model to the powers of the features, so it is linear regression on transformed inputs — and the degree of the polynomial is a capacity knob whose excess produces overfitting.

## Core Intuition

The homework notebook's framing is precise: "Instead of modeling the outcome as a linear combination of the features, polynomial regression models it as a linear combination of powers of the features". That single substitution changes the model class without changing the learning procedure. The model is still fitted by minimising a squared error; the parameters are still linear coefficients; the optimisation is still gradient descent. What changes is the space of functions the model can express.

The key observation the notebook makes explicit: "Note that although $f$ is nonlinear in $x$, it is still *linear in the weights* $w$: polynomial regression is linear regression on the transformed features $(x, x^2, \dots, x^q)$." This is why polynomial regression is the right first exercise for a student meeting PyTorch for the first time: the code has the shape of a neural network (a `torch.nn.Module` with trainable parameters and a `forward` method) while the mathematics remains the linear algebra already known.

The exercise is therefore an experiment on model capacity. The degree $q$ is the single knob; the ground truth is a degree-3 polynomial; the data is small (10 training points) and noisy. Increase $q$ and the model can fit the training points better while fitting the true function worse. That gap between training and validation loss is overfitting, and task 8 asks you to measure it rather than eyeball the plot.

## Formal Definition / Statement

**Single feature.** For $x \in \mathbb{R}$:

$$f(x, w) = w_0 + w_1 x + w_2 x^2 + w_3 x^3 + \dots + w_q x^q$$

**Multiple features.** For $x \in \mathbb{R}^p$, the simple version the notebook uses:

$$f(x, w) = w_0 + \sum_{i=1}^{p} \sum_{j=1}^{q} w_{ij} x_i^j$$

A full polynomial model of degree $q$ would additionally contain interaction terms such as $x_1 x_2$ or $x_1^2 x_3$; the notebook omits them.

**The linearity that matters.** $f$ is nonlinear in $x$ but linear in $w$. Gradient descent on $E(w) = \sum_i (f(x_i, w) - y_i)^2$ is therefore the same problem as for linear regression, and the closed-form normal equations still apply to the transformed feature matrix.

**Required implementation.** A class `PolyRegression` inheriting from `torch.nn.Module`:

- `__init__` takes an integer degree argument. "The weights can be created with a `torch.nn.Linear` layer, but you can also look at different approaches like using `torch.nn.parameter.Parameter`. Do not forget to call the `__init__` of the parent class first."
- `forward` receives inputs of shape `(N, 1)`, returns predictions of shape `(N, 1)`, and implements $f(x,w) = w_0 + w_1 x + \dots + w_q x^q$. Hint: "`torch.pow` can be used to raise a tensor to a power."

The notebook's own test asserts the shape contract: `assert out.shape == (n_points, 1)`.

**The data.**

```python
torch.manual_seed(1234)
torch.use_deterministic_algorithms(True)
n_points = 10

def make_targets(x):
    return x + 0.5 * x**2 - 0.25 * x**3 + 0.4 * torch.randn_like(x)

x = torch.linspace(-2, 3, n_points).reshape(-1, 1)
y = make_targets(x)

x_val = torch.linspace(-2, 3, 25).reshape(-1, 1) + 0.1 * torch.randn((25, 1))
y_val = make_targets(x_val)
```

The ground truth is a degree-3 polynomial, $x + 0.5x^2 - 0.25x^3$, plus Gaussian noise with standard deviation 0.4. There are 10 training points and 25 validation points; all tensors have shape `(n, 1)`.

**Training configuration.** `torch.optim.Adam` with `lr=5e-3`, checking the validation loss on `x_val, y_val` "from time to time, e.g., every 500 epochs" to see whether you are overfitting.

## Key Properties

- **The degree is the capacity.** $q$ bounds the model's expressive power. Degree 1 cannot represent curvature; degree 9 can represent almost anything on a bounded interval, including the noise.
- **Every degree-3 polynomial is also a degree-9 polynomial**, with the extra weights set to zero. "After convergence, a higher-degree model must therefore reach a training loss at most as large as the degree-3 model. If your training loss is higher, the optimization has not converged yet." This is a free consistency check on your own training run.
- **Feature scale explodes with degree.** "$x$ takes values up to 3, so the feature $x^q$ quickly becomes large ($3^9 \approx 20\,000$). This makes gradient-based optimization of high-degree models slow and sensitive to the learning rate." Conditioning degrades with $q$ even before overfitting sets in.
- **Overfitting is measured by the gap, not the loss.** Training loss can only go down as $q$ rises; validation loss is the honest number. "Compare the final training *and* validation losses, not just the plots."
- **Underfitting is the opposite failure.** A degree-1 or degree-2 model on degree-3 data has both training and validation loss high, and cannot be improved by training longer — the model class is wrong, not the optimisation.
- **The task is supervised regression.** Question 9 asks how to classify it "in the scheme of slide 6 in deck 2", the ML task taxonomy: regression — a numeric target predicted from features — with the qualification that the model is linear in its parameters.

## Worked Example

**Fitting the ground truth.** The generating function is $x + 0.5x^2 - 0.25x^3$, so a degree-3 model has exactly the right capacity. With Adam at `lr=5e-3` and enough epochs, the model should converge to weights near $(0, 1, 0.5, -0.25)$ in the order $(w_0, w_1, w_2, w_3)$. The measured result is training loss 0.056 and validation loss 0.211, against a noise variance of $0.4^2 = 0.16$ per point. The training loss lands well below the noise level — four parameters fit to ten points can absorb some of the noise — and the validation loss above it, which is the expected direction for a model that is slightly overfitting the sample it was given.

**Raising the degree to 9.** With $q = 9$, the model has ten parameters for ten training points. It can drive the training loss towards zero by interpolating the noise, while the validation loss stays at the noise floor or rises above it — the classic overfitting signature. The training-loss check from the notebook applies: if your degree-9 training loss comes out *above* your degree-3 training loss, you have not converged, and you should not conclude that a higher degree fits worse.

**The scaling problem, concretely.** At $x = 3$, the feature $x^9 \approx 20\,000$, while $x^3 = 27$ and $x = 3$. A parameter change on the $w_9$ coefficient moves the prediction by tens of thousands, and the gradient with respect to that coefficient is proportional to $x^9$ as well. The optimiser needs either a much smaller learning rate or many more epochs ("You may need to change the number of epochs and the learning rate of the optimizer").

**Dropping to degree 1 or 2.** A degree-1 model is a straight line fitted to a curved target; a degree-2 model captures the $0.5x^2$ term but misses $-0.25x^3$. Both are underfitting: high training loss *and* high validation loss, with a visible systematic pattern in the residuals rather than random scatter. The distinction to state in the answer is this: underfitting shows up in the training loss, overfitting shows up in the gap between training and validation.

**The training and evaluation functions.** `train_one_epoch(x, y, model, optimizer, loss_func)` "implements the five general training steps" and returns the training loss of that epoch; `evaluate(x, y, model, loss_func)` "Computes the loss over validation data" and "should use the `torch.no_grad` function decorator or the `torch.no_grad` context manager". The notebook names it `evaluate` rather than `eval` because "`eval` is a built-in Python function that we do not want to shadow".

**A minimal implementation.** Using `torch.pow` as the hint suggests:

```python
class PolyRegression(torch.nn.Module):
    def __init__(self, degree):
        super().__init__()
        self.degree = degree
        self.linear = torch.nn.Linear(degree, 1, bias=True)

    def forward(self, x):                      # (N, 1) -> (N, 1)
        feats = torch.cat([torch.pow(x, j) for j in range(1, self.degree + 1)], dim=1)
        return self.linear(feats)              # (N, q) -> (N, 1)
```

The `super().__init__()` call is not optional: without it the `nn.Linear` parameters are never registered as trainable and the optimiser has nothing to update.

## Common Pitfalls

- **Forgetting `super().__init__()`.** The parameters are not registered, the optimiser receives nothing, and the loss never moves.
- **Getting the feature order or the bias wrong.** `nn.Linear` supplies the intercept itself; constructing the feature vector as $(x, x^2, \dots, x^q)$ and letting the layer add $w_0$ is the clean route.
- **Comparing only training losses across degrees.** Training loss always improves with capacity. The comparison the task demands includes validation loss.
- **Concluding "degree 9 fits worse" because the training loss is higher.** That is a convergence failure, not a capacity result — see hint 3.
- **Ignoring the learning rate for high degrees.** With $x^9 \approx 20\,000$, `lr=5e-3` may be far too aggressive. The task explicitly permits changing epochs and learning rate.
- **Not seeding before each model.** "Hint 1: Call `torch.manual_seed(123)` before creating each model so that your runs are reproducible." Without it, degree 3 and degree 9 differ in initialisation as well as in capacity, and the comparison is meaningless.
- **Evaluating without `no_grad`.** The validation forward pass builds a graph that is never used and wastes memory.
- **Shadowing `eval`.** `evaluate` avoids the collision with the Python builtin.
- **Reporting the task as classification.** It is regression; the transformed features do not change the task type.

## Connections

- [[linear-regression]] — the direct parent: the same loss, the same update rule, the same closed form, applied to a transformed feature matrix.
- [[neural-network-training-loop]] — the five general training steps that `train_one_epoch` implements, and the `no_grad` discipline that `evaluate` requires.
- [[gradient-descent-for-neural-networks]] — why the optimisation is iterative at all, and what $\alpha$ does when the features grow to $20\,000$.
- [[pytorch-tensors-and-autograd]] — `torch.nn.Module`, `super().__init__()`, parameter registration, and `torch.pow` on tensors.
- [[ml-task-taxonomy]] — the slide-6 scheme that question 9 asks you to classify the task with: regression, not classification.
- [[feature-normalization]] — the direct answer to the conditioning problem: $x^q$ on $[-2, 3]$ is exactly the kind of feature that scaling is meant to tame.
- [[representation-learning]] — polynomial regression is the hand-designed version of what a network learns: the features $(x, x^2, \dots, x^q)$ are chosen by a human here and by the data there.
- [[classification-metrics]] — the counterpart for the regression case: how you would judge a fit numerically when the task is not a classification.

## Open Questions

- The ground-truth function has degree 3, but the validation set is generated from the same `make_targets` function with additional input jitter of `0.1 * torch.randn((25, 1))`. Whether the validation points still span $[-2, 3]$ after jitter is not stated.
- The interaction terms are omitted from the multivariate formula. Whether the same overfitting behaviour appears in the multivariate case with interactions included is left open.
- `torch.use_deterministic_algorithms(True)` and the manual seeding make runs reproducible, but the note that a "current version of PyTorch" should be version 2.9 while the demo ran 2.14.1 leaves open whether results are bit-identical across versions.
