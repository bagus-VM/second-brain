---
title: "RepEng In-Class Exercise 4 — Git"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 4 — Git Best Practices

---

## Exercise 1 — Norm's Commit History Problem

Norm committed incomplete/broken code (work-in-progress) and then committed the fix separately. His project manager is not amused because:

**What Norm should have done:**
1. **Don't commit broken code.** Use `git stash` to save work-in-progress without committing.
2. **Interactive rebase** (`git rebase -i`) to squash the fix into the original commit before pushing.
3. **Amend** the commit (`git commit --amend`) to fold the fix into the WIP commit.
4. Use a **feature branch** for development, then merge a clean history into main.

**Key principle:** Each commit should represent a logical, working unit of change. The public history should tell a clear story of what was done and why — not the messy chronology of how you actually worked.

---

## Exercise 2 — Reconstructing a File from `git log -p`

The git log shows commits in reverse chronological order (newest first). Reconstructing `saucy.md`:

Starting from the oldest commit (`5db2b68` — "first attempt"):

```markdown
# Call me Cilly

## Ingredients
1/2 cup - Plain yogurt
3-4 cloves - Garlic
2 cups - Chopped cilantro
1/4 cup - Olive oil
1/4 cup - Lime juice
1 pinch - Salt

## Instructions
Add all ingredients to a blender. Mix until smooth.
```

Then `4cca5a7` ("make it spicy") changed:
- `1 pinch - Salt` → `2 pinches - Salt`
- `1 - Jalapeno, deseeded` → `2 - Jalapenos, deseeded`
- `Mix until smooth.` → `Mix until desired consistency.`

Then `8d670e9` ("update recipe name") changed the title:
- `# Call me Cilly` → `# Spicy Green Mean Machine`

**Current content of saucy.md:**

```markdown
# Spicy Green Mean Machine

## Ingredients
1/2 cup - Plain yogurt
3-4 cloves - Garlic
2 cups - Chopped cilantro
1/4 cup - Olive oil
1/4 cup - Lime juice
2 pinches - Salt
2 - Jalapenos, deseeded

## Instructions
Add all ingredients to a blender. Mix until desired consistency.
```

---

## Exercise 3 — Commit Metadata & Patch Structure

The commit has:

- **commit hash:** Unique identifier for this snapshot (aa09c4f...)
- **Author:** Jane Doe — who wrote the change (may differ from committer)
- **Committer:** John Doe — who applied the change to the repository
- **Commit message:** Describes *what* was changed and *why* (not just *how*)
  - **Subject line:** "Use salted hashes" — concise summary
  - **Body:** Explains the motivation, references the academic source (Ilsebill et al.)
- **Trail of responsibility:**
  - `Signed-off-by:` — certifies the author agrees to the Developer Certificate of Origin
  - `Reviewed-by:` — documents code review by Jean Doe
  - `Tested-by:` — documents testing by Judy Doe
- **Diff:** The technical change
  - `diff --git a/sec/hash.c b/sec/hash.c` — file path
  - `@@ -1,7 +1,7 @@` — hunk header (context)
  - `-hash = getHash(val);` — removed line
  - `+hash = getSaltedHash(val, salt());` — added line

**Why this matters for reproducibility:** The trail creates accountability, traceability, and context. Anyone can see *who* changed *what*, *why* (with references), and *who* reviewed and tested it.

---

## Exercise 4 — Snapshot vs Clone vs Fork

### Option 1: Just the latest snapshot (zip/tar)
**Pros:**
- Simple, small file size
- No git history baggage
- Easy for reviewers to download

**Cons:**
- Loses all commit history, blame, and evolution context
- No easy way to track upstream changes
- Can't verify what changes you made vs original

### Option 2: Clone + add changes (e.g., git patch stack)
**Pros:**
- Preserves full upstream history
- Your changes are clearly separated as patches
- Reviewers can see exactly what you modified
- Can rebase onto upstream updates

**Cons:**
- More complex setup
- Patch stacks may not apply cleanly to upstream updates
- Requires understanding of git rebase/cherry-pick

### Option 3: Fork + work on your fork
**Pros:**
- Full GitHub integration (PRs, issues, CI)
- Easy to sync with upstream via `git fetch upstream`
- Clear attribution and contribution workflow
- Can submit PRs back to original project

**Cons:**
- Depends on the hosting platform (GitHub)
- Fork may diverge significantly over time
- Repository might be large with full history

**Best practice:** Fork (option 3) for active projects with CI/CD integration. Clone + patches (option 2) for archival/reproduction packages. Snapshot (option 1) only as last resort.

---

## Exercise 5 — Restructuring Git History

The original history reads bottom-to-top as:
1. Kick-Off (initial README)
2. Add build infrastructure (Makefile, .gitignore)
3. Add code proper (hello.c with `void main()`)
4. fixup: Actually improve code quality (fix `void main()` → `int main()`)
5. fixup: Ensure that build system sets highest standards (fix CFLAGS)

**Restructured history (interactive rebase squash):**

1. **"Kick-Off: hello world program"** — README, initial hello.c
2. **"Add build infrastructure"** — Makefile, .gitignore (with correct CFLAGS from the start)
3. **"Implement hello world"** — hello.c with correct `int main()` and `return 0`

**How:** `git rebase -i` to squash fixups into their parent commits. The result is 3 clean, logical commits instead of 5 messy ones.


---

## Related Resources

### 📖 Reproducibility Engineering — Lecture 4: Git
- Lecture topic: [[reproducibility-engineering-lecture-4]]

**Key concepts covered:**
- [[git-dag-structure-and-internals]]
- [[developer-certificate-of-origin]]
- [[git-branching-and-merging]]
- [[git-rebasing-and-history-rewriting]]
- [[git-commit-hygiene]]
- [[gitignore-and-gitattributes]]
- [[git-patches-and-diffs]]
- [[git-for-reproducibility]]
- [[data-provenance]]
- [[computational-reproducibility-in-ml]]
