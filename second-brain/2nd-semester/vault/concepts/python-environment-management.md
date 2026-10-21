---
title: "Python Environment Management"
tags: [concept, deep-learning, python, tooling, semester-2]
course: "Introduction to Deep Learning"
source_count: 2
status: current
last_updated: 2026-10-19
prerequisites: ["[[python-for-deep-learning]]"]
---

## One-line Summary
A virtual environment is a per-project box holding one Python interpreter and one exact set of packages; `uv` creates that box, installs into it, and runs code inside it.

## Core Intuition
The lecture's example: `project1.py` needs numpy 1.13, `project2.py` needs numpy 2.0. No single global installation satisfies both, and downgrading on every switch is not a workflow. The same holds for the interpreter — two projects may need different Python versions, and only one can be "the" Python on your PATH. An environment gives each project its own isolated package directory, so installing for one cannot break the other.

The third reason is reproducibility: a declared dependency set means the code still runs in six months, on another machine.

## Formal Definition / Statement
An environment manager creates and maintains an isolated Python installation per project. The course standardises on `uv`; installing Python from python.org is explicitly not recommended.

```bash
uv init intro-dl      # create subdirectory, initialise as a Python project
cd intro-dl
uv add jupyter numpy  # install dependencies
```

This creates `intro-dl/.venv/` and installs Jupyter and NumPy into it. Later packages, from inside the project directory: `uv add PACKAGENAME`.

`uv run` executes inside the environment: `uv run fizzbuzz.py`, `uv run jupyter lab`. The second is the no-IDE path — Jupyter starts out of the project environment, so the kernel is right by construction.

**IDE setup (optional, recommended).** VS Code with Python and Jupyter (both Microsoft) and Ruff (Astral) for formatting. Format-on-save, inside the user settings JSON:

```json
"notebook.formatOnSave.enabled": true,
"[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff"
}
```

## Key Properties
- **Isolation** — installs are scoped to one project, not the machine.
- **Declared dependencies** — `uv add` records what the project needs; that record is what makes setup reproducible.
- **Interpreter included** — the environment can pin Python, not only packages.
- **One command to run** — no activation step to forget, and none to get wrong.
- **Kernel binding is separate** — the environment existing is not the same as a notebook using it.

**Jupyter sits on top of it.** Notebooks run and rerun cells while keeping state, interleave code with Markdown and plots, and make exploration fast. The lecture calls them a blessing and a curse: that same statefulness easily produces spaghetti code and bad habits, because execution order stops matching the file.

## Worked Example
1. Install `uv` per the Astral instructions.
2. `uv init intro-dl`, then `cd intro-dl`.
3. `uv add jupyter numpy`.
4. Download `01-hw-intro-py-tasks.ipynb` from Stud.IP into `intro-dl/`.
5. In VS Code: File → Open Folder, open the notebook, **Select Kernel** (top right) → Python Environments → the interpreter under `.venv`.
6. Run `import numpy as np`. It works because of step 5.

Skip step 5 and step 6 raises `ModuleNotFoundError` although `uv add numpy` succeeded. The notebook is attached to a different interpreter.

## Common Pitfalls
- **The kernel trap.** Without the `.venv` kernel, packages installed with `uv` are invisible in the notebook — the standard way to lose an hour in week 1.
- **Global installs** reintroduce the numpy 1.13 / 2.0 conflict environments exist to prevent.
- **`uv add` from the wrong directory** modifies a different project's environment.
- **Stale kernels.** A notebook remembers its kernel; a file opened months later may point elsewhere.
- **Environment ≠ kernel.** One is a directory on disk, the other a process bound to it, configured in two different places.

## Connections
- [[python-for-deep-learning]] — the language these environments exist to hold.
- [[deep-learning-course-roadmap]] — week 1 is the only week teaching tooling; later coding homework assumes it works.
- [[introduction-to-deep-learning]] — course page and session logistics.

## Open Questions
- The slides show the xkcd "standards" comic beside "many options for environment managers" without naming alternatives. Why `uv` over conda or poetry is asserted, not argued.
- Whether the exam expects commands like `uv add` and `uv run` to be reproduced is not stated.
- With the IDE optional and homework ungraded, it is unclear whether unformatted code is penalised.
