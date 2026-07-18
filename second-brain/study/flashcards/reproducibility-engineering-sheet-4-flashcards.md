---
title: "Reproducibility Engineering - Sheet 4 Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 4

## Flashcards

> [!question]- What are the four XPath equality notions and how do they differ?
> [!answer]- **`eq`** (value comparison): compares exact text of single nodes. **`deep-equal()`** (structural comparison): checks identical structure including attributes and children. **`is`** (node comparison): checks if two expressions point to the same physical node. **`=`** (general comparison): handles sequences, true if any values match.

> [!question]- Why is TinyTeX preferred over TeX Live for Docker-based LaTeX compilation?
> [!answer]- TinyTeX is a lightweight distribution that installs only the packages you explicitly specify via `tlmgr install`. This keeps Docker image sizes small and makes builds deterministic (no on-the-fly package downloads), unlike full TeX Live which installs thousands of unnecessary packages.

> [!question]- Why might two PDFs compiled from identical LaTeX source and data have different MD5 hashes?
> [!answer]- LaTeX may embed timestamps, random UUIDs, or other non-deterministic metadata in the PDF. Font subsetting order, compression, and `\pdfcreationdate` can vary between runs. This means the PDF is not bitwise-repeatable even though it's semantically identical.

> [!question]- What does `pdflatex -interaction=nonstopmode -halt-on-error` do?
> [!answer]- `-interaction=nonstopmode` prevents pdflatex from stopping for user input on errors. `-halt-on-error` makes it exit immediately on the first error. Together they enable fully automated compilation in CI/Docker pipelines where no human is available to interact.

> [!question]- How does using `pip install` without version pinning in a Dockerfile affect reproducibility?
> [!answer]- `pip install` fetches the latest version of a package at build time. Over months, new releases may introduce breaking changes or API differences, causing the image to build differently. Pinning versions (e.g., `pip install pandas==2.2.0`) ensures deterministic builds.


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
