---
title: "Reproducibility Engineering - Sheet 5 Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 5

## Flashcards

> [!question]- What is the difference between Author and Committer in Git?
> [!answer]- The **Author** is the person who originally wrote the code changes. The **Committer** is the person who last applied the commit to the repository (e.g., via cherry-pick or rebase). `git log --format=fuller` shows both separately.

> [!question]- What is an interactive rebase and when would you use it?
> [!answer]- `git rebase -i <commit>` lets you reorder, squash, edit, or reword commits. Use it to clean up history before sharing — e.g., merging "fix typo" commits into meaningful ones, making the history more readable for reproducers.

> [!question]- How do you create and apply a diff patch in Git?
> [!answer]- Create: `diff -u original.c modified.c > changes.patch`. Apply: `patch <target_file> <changes.patch`. In a Dockerfile, you can copy the patch into the container and apply it during build to modify third-party source code transparently.

> [!question]- What does `.gitignore` do and how do you verify it's working?
> [!answer]- `.gitignore` lists file patterns that Git should not track. After adding a file matching a pattern (e.g., `todos.txt`), `git status` should NOT list it as untracked. Only `.gitignore` itself appears as untracked until committed.

> [!question]- What is `git reflog` used for?
> [!answer]- `git reflog` lists all previous HEAD positions known to Git, including states before resets or rebases. It's a safety net: if you make a mistake during a rebase, you can find the previous good commit hash and reset to it with `git reset --hard <hash>`.


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
