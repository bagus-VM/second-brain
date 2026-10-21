---
title: "Jupyter Notebook State and the Rerun Trap"
tags: [concept, deep-learning, python, tooling, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[python-environment-management]]"]
---

## One-line Summary

A notebook cell's stored output is a snapshot of one particular execution, not a property of the code beside it — so editing a definition without re-running the cells that depend on it leaves the notebook asserting something false about itself.

## Core Intuition

Jupyter's power and its danger are the same mechanism. Cells execute in order and *keep their state*: a variable defined in cell 3 is still live in cell 40, and rerunning cell 3 does not undo what cell 40 did. That is what makes exploration fast — you can try three ideas without re-running the setup each time.

The cost is that the file can end up lying. A cell that says `y == 4` → `False` is not a claim about the function in the cell above it; it is a claim about what that function returned *the last time this cell was executed*. Change the definition and the output cell does not know. The notebook still displays `False` with full confidence, because nothing invalidated it.

The course's own demo notebook makes the point with a deliberately broken example, and the takeaway it writes down is the rule: *"Notebooks are dangerous unless you run each cell exactly once, in order!"*

## Formal Definition / Statement

**Notebook state** is the set of live names — variables, functions, imported modules, and the current working directory — that exists in the kernel at any moment. A notebook file is a *sequence of operations* to be replayed, not a list of statements to be read.

Three properties follow:

1. **Execution is a prefix, not a set.** A cell can only have run if all cells above it have run. A cell's stored output records the state at the moment of *its* execution, not the state at the end of the notebook.
2. **Editing does not invalidate.** Changing a cell's source leaves every downstream stored output untouched. The kernel is not re-executed by an edit.
3. **Rerunning is not idempotent.** Re-running a cell that mutates state (appending to a list, training a model, writing a file) re-applies that mutation.

**The rule that follows:** to know what a notebook actually computes, restart the kernel and run every cell top to bottom. If the outputs change, the file was describing a history of executions rather than a program.

## Key Properties

- **Outputs are evidence, not documentation.** They are as stale as the last edit to an earlier cell.
- **The kernel is the real program.** The `.ipynb` file is a script for the kernel; the kernel holds the truth about what ran.
- **"Run all" is a different artifact from what you were looking at.** Restart-and-run-all is the only way to make the file's displayed outputs and its source agree.
- **Ordering discipline is the mitigation.** The course's rule — run each cell exactly once, in order — is what keeps the state consistent with the source. It also destroys the "rerun just this one cell" convenience, which is the point.
- **This is a reproducibility failure, not a Python failure.** The same argument that puts execution order in the definition of a reproducible artifact applies to a notebook: an artifact is reproducible only if running it again gives the same result.

## Worked Example

`01-notebook-issue.ipynb` is a four-cell notebook whose title is *"What is going on here?!"*. It defines a function, calls it, and then displays two outputs that do not agree with the source:

```python
def f(x: int) -> int:
    return x + 2          # <- the current source
```

```python
y = f(2)                  # execution_count 2
```

```python
y == 4                    # execution_count 3 -> output: False
```

```python
print(y)                  # execution_count 4 -> output: 5
```

**The puzzle:** by the source as written, `f(2)` is `4`, so `y == 4` must be `True` and `print(y)` must print `4`. The stored outputs say `False` and `5`.

**The resolution:** the outputs are consistent with exactly one earlier version of the function — `f(x) = x + 3`, which gives `f(2) = 5`, so `y == 4` is `False` and `print(y)` is `5`. The function was changed from `x + 3` to `x + 2` after the cells below had already been executed, and those cells were never re-run.

Re-running the notebook in order with the current source gives `y = 4`, `y == 4 → True`, `print(y) → 4` — the outputs the file *should* have displayed. Both output cells are stale, in the same direction, and they are stale for the same reason: one upstream edit, no downstream re-execution.

The exercise is worth doing by hand. Before looking up what `x + 2` returns, ask: *what must the function have been for these two outputs to be true at the same time?* The two outputs constrain each other, and that constraint is what identifies the historical version.

## Common Pitfalls

- **Reading a stored output as the behaviour of the code above it.** This is the exact error the demo notebook is built to provoke.
- **Re-running a single cell and assuming the notebook is still consistent.** A rerun updates *that* cell's output and leaves every other cell's output describing the older world.
- **Mutating state and rerunning.** Appending to a list, training a model, or writing a file in a cell that gets re-run duplicates the effect.
- **Committing a notebook with stale outputs.** Anyone reading it draws conclusions from numbers the code no longer produces.
- **Assuming the kernel matches the file.** Restarting the kernel is what invalidates the assumption that the live state and the file agree — and the notebook survives that, or it does not.
- **Treating "it worked in my session" as evidence.** The session had a particular execution history. The file does not.

## Connections

- [[python-environment-management]] — the toolchain context: `uv`, one environment per project, and the kernel-selection trap. A notebook bound to the wrong kernel is a different failure from a stale notebook, and both cost the same hour.
- [[python-for-deep-learning]] — the lecture's "blessing and curse" framing of Jupyter; this page is the concrete mechanism behind the curse.
- [[deep-learning-course-roadmap]] — week 2 moves to PyTorch, where the same statefulness bites harder: a training cell whose model was rebuilt by a later cell produces results nobody can reproduce.
- [[reproducible-builds]] (Semester 1) — the same argument in a build context: an artifact is only trustworthy if running it again gives the same result.
- [[data-provenance]] (Semester 1) — a stale output is a provenance failure: the number on screen did not come from the code beside it.
- [[ml-pipeline-scikit-learn]] — the `fit` / `transform` contract is the same discipline in a different place: learn from training data, apply learned state elsewhere.

## Open Questions

- The demo notebook shows the trap but does not say whether the course expects notebooks to be re-run from a clean kernel before submission, or whether outputs are checked at all.
- The slides mention Jupyter's statefulness as a curse but propose no remedy beyond the demo's rule. Whether a "run all and commit" workflow is expected is never stated.
- No grading consequence is given for a notebook with stale outputs, while the homework is explicitly not graded — so the stakes of getting this right are unclear.
