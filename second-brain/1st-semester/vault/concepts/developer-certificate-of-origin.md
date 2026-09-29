---
title: "Developer Certificate of Origin"
tags: [concept, reproducibility-engineering, semester-1, git, legal, open-source]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-commit-hygiene]
---

## One-line Summary
The DCO is a lightweight legal certification that a contributor has the right to submit their code, indicated by a `Signed-off-by` trailer in each commit.

## Core Intuition
In open-source and academic projects, provenance matters: who contributed what, and did they have the right to contribute it? The DCO provides a lightweight alternative to Contributor License Agreements (CLAs). By adding `Signed-off-by: Name <email>` to a commit, the contributor certifies that:
1. They wrote the code (or have the right to submit it under the project's licence).
2. They are aware of the project's licence terms.
3. They agree to the DCO terms.

From the lecture: the commit patch shows `Signed-off-by: Jane Doe <jane@doe.com>` as part of the "trail of responsibility" — it documents the chain of accountability from author to committer to reviewer.

## Formal Definition / Statement
The DCO (version 1.1) certifies that the contributor:

> (a) The contribution was created in whole or in part by me and I have the right to submit it under the open source licence indicated in the file; or
> (b) The contribution is based upon previous work that is covered under a different open source licence, and I have the right to submit that work under those licenses; or
> (c) The contribution was provided to me by someone who certified (a), (b), or (c) and I have not modified it.
> (d) I understand this project and contribution are public and a record of the contribution is maintained indefinitely.

Implementation: add `-s` flag to `git commit`:
```bash
git commit -s -m "Implement feature X"
```
This appends: `Signed-off-by: Your Name <your@email.com>`

## Key Properties / Complexity
- **Lightweight**: No paperwork, no CLA — just a trailer in the commit message.
- **Per-commit**: Each commit carries its own certification.
- **Enforceable via CI**: Tools like Probot DCO can check that all commits in a PR have the trailer.
- **Chain of responsibility**: Multiple `Signed-off-by` lines (from author and committer) document the full chain. The lecture shows `Signed-off-by:` from both the author and a second person (e.g., Stefanie Scherzinger).
- **Legal standing**: Used by the Linux kernel, many CNCF projects, and academic research software.

## Worked Example
From the lecture exercise:

```
commit aa09c4f6a54152...
Author: Jane Doe <jane@doe.com>
Committer: John Doe <john@doe.com>

Use salted hashes

Function getHash() is used to hash user passwords. Since adding a salt
value is considered a minimum standard these days, augment computing the
hash with a salting function as devised by Ilsebill et al., Grassian
Letters 27(3), 2022.

Signed-off-by: Jane Doe <jane@doe.com>
Reviewed-by: Jean Doe <jean@doe.com>
Tested-by: Judy Doe <judy@doe.com>
```

The "trail of responsibility":
- **Author** (Jane): wrote the code
- **Committer** (John): applied the commit (could differ from author)
- **Signed-off-by** (Jane): certifies DCO
- **Reviewed-by** (Jean): code review acknowledgment
- **Tested-by** (Judy): testing acknowledgment

## Common Pitfalls
- **Missing email match**: The `Signed-off-by` email should match the `Author` email (or explain the discrepancy with multiple sign-offs).
- **Forgetting `-s`**: Developers often forget to add the flag; CI should catch this.
- **Confusing with GPG signing**: DCO (`-s`) is a legal statement; GPG signing (`-S`) is a cryptographic verification. They are independent.

## Connections
- [[git-commit-hygiene]] — trailers are part of well-structured commit messages
- [[git-patches-and-diffs]] — trailers appear in the metadata block of patches
- [[git-for-reproducibility]] — DCO establishes provenance for reproduction packages

## Open Questions
- How does the DCO interact with AI-generated code (e.g., Copilot)? Can one certify authorship?
- Should reproduction packages for research always include DCO trailers?
