---
title: "Reproducibility Engineering - Exercise Sheet 5"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| Exercises 2–3 — Basic Git & Tracking Contributions | [[git-commit-hygiene]] · [[git-dag-structure-and-internals]] |
| Exercises 4–5 — Rewriting Histories & Patches | [[git-rebasing-and-history-rewriting]] · [[git-patches-and-diffs]] |
| Exercise 6 — Git MC | [[git-for-reproducibility]] · [[git-branching-and-merging]] |

# Exercise Sheet 5 — Git Basics, History Rewriting & Patches

> **Note:** No official solutions available.

Lab Sessions: May 28/29, 2026

## Exercises

### 1. Preparation
Update your local RepEng repository: `git pull`

### 2. Basic Git

Copy and enter the lab folder:
```
cp -r RepEng/LabSession5 MyLabSession5
cd MyLabSession5
```

Tasks:
- **(a)** Initialize a new Git repository: `git init`
- **(b)** Add all files to staging: `git add .`
- **(c)** Make an initial commit: `git commit -m "..."`
- **(d)** Tag the latest commit: `git tag LabSession5-v1`
- **(e)** Create and check out branch "MyLabSession5": `git checkout -b MyLabSession5`
- **(f)** Change the shell script output to "Hello from Lab Session 5"
- **(g)** Check status — `hello.sh` should be modified but not staged
- **(h)** Stage the changed file: `git add hello.sh`
- **(i)** Check status — `hello.sh` should be modified and staged
- **(j)** Commit the change
- **(k)** Create `todos.txt` with `touch todos.txt` and ensure it's ignored by Git (add to `.gitignore`)
- **(l)** Check status — `.gitignore` untracked, `todos.txt` ignored

### 3. Tracking Contributions

- **(a)** Clone and enter the repository: `https://github.com/looselytyped/gitanjali-aref-wedding-plans`
- **(b)** Run `git blame drinks.md` — learn to read the output (commit hash, author, date, line content)
- **(c)** Use `git blame` on `appetizers.md`:
  - (i) How many authors contributed?
  - (ii) When was the last edit?
  - (iii) Who last edited line 5?

### 4. Rewriting Histories

- **(a)** Clone: `git clone https://github.com/ReproEng/LabSession2`
- **(b)** Inspect `git log` on branch `master` — decide which commits to preserve vs. squash
- **(c)** Interactive rebase: `git rebase -i <commit>` to merge commits into readable history
  - Use `git reflog` and `git reset --hard <commit>` to recover from mistakes
- **(d)** Check out a new branch, merge `i18n` branch, resolve merge conflicts
- **(e)** Create a new branch with linear history including i18n changes as a separate commit
- **(f)** Review all commit messages; use reword to fix inaccurate messages

### 5. Rewriting History: Working with Patches

- **(a)** Enter `RepEng/LabSession5/`
- **(b)** Copy `hello.c` to `hello_new.c` and modify to print "Hello World"
- **(c)** Create a diff patch:
  ```
  diff -u hello.c hello_new.c > hello.patch
  ```
  Edit the Dockerfile to apply the patch and compile:
  - `patch <file> <patch_file>`
  - `gcc -o <output_file> <source_file>`
- **(d)** Build and run the Docker container with the compiled program

### 6. Git (Multiple Choice)

**Git Logs** (based on provided `git log` output):

**(a)** Who authored the latest code changes?
- **Alice Miller** (she is the Author of the HEAD commit)

**(b)** How many different persons authored code changes?
- **3** (Alice Miller, Ben Carter, Dana Smith)

**(c)** How many commits delete a file?
- **0** (no commit shows deletions-only; all show insertions)

**(d)** Which file has undergone the most changes in total (lines of code)?
- **src/register.js** (18+4=22 lines changed across commits, plus initial 24 = most total)

**Git Diffs** (based on provided `git diff` output):

**(e)** How many of these lines are present in the latest version starting at line 5?
- `## Languages`, `English (native)`, `Klingon (fluent)` — **3 lines** (Romulan was replaced)

**(f)** After committing and checking out `other-branch`, how many of these lines are present?
- `2018-2020, Federation Starship Atlantis - Communications Ensign`, `Routed incoming subspace communications to the correct officer` — **2 lines** (other-branch has the original content)


---

## Related Resources

### 📖 Reproducibility Engineering - Lecture 5: Reproducible Builds
- Lecture topic: [[reproducibility-engineering-lecture-5]]

**Key concepts covered:**
- [[diffoscope]]
- [[deterministic-builds]]
- [[build-environment-isolation]]
- [[source-date-epoch]]
- [[ci-cd-for-reproducibility]]
- [[containerization-for-builds]]
- [[package-manager-reproducibility]]
- [[make-and-build-systems]]
- [[c-preprocessor]]
