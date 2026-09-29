---
title: "Mock Exam — Reproducibility Engineering (40 questions)"
tags: [exam-prep, mock-exam, reproducibility-engineering]
course: "Reproducibility Engineering"
exam_date: "2026-07-30"
format: "Single-best-answer unless marked [Mehrfachauswahl]"
status: current
last_updated: 2026-07-30
prerequisites: []
---

# Mock Exam — Reproducibility Engineering (40 questions)

> 40 questions. Single-best-answer unless marked **[Mehrfachauswahl]**. 90 minutes. No notes.
> 
> Scope: all lecture topics — reproducibility taxonomy, provenance, environments & containers, builds & hashing, randomness & determinism, workflow systems, testing & CI, data management & FAIR, legal/licensing, documentation & sharing, archives & preservation.

---

## Questions

1. The term "repeatability" in computational experiments most closely means:

a) Different team, different setup, same results

b) Same team, same setup, same results

c) Different implementation that yields the same conclusion

d) Same data but different analysis

2. Which equivalence level requires identical bytes across outputs?

a) Behavioral

b) Functional

c) Structural

d) Bitwise

3. [Mehrfachauswahl] Which items are core parts of provenance metadata discussed in lectures?

a) Command-line arguments used

b) Timestamps of execution

c) Researcher’s personal notes in a private notebook

d) Versions of software dependencies

4. A Docker image built from an unpinned base may fail to be reproducible because:

a) Image layers are always identical

b) Upstream package updates change contents over time

c) Dockerfiles include random salts by default

d) Containers prevent access to hardware

5. Semantic versioning (MAJOR.MINOR.PATCH) primarily helps reproducibility by:

a) Guaranteeing bitwise reproducibility across releases

b) Communicating backward-incompatible changes to users

c) Pinning exact package binaries

d) Removing the need for dependency locks

6. Which tool is best for recording execution traces and parameter values retroactively?

a) Static typing checker

b) Retrospective provenance capture (e.g., ReproZip-like)

c) Zip compression

d) Container registry

7. Which practice most reduces the risk of unreproducible randomness?

a) Removing all sources of RNG

b) Seeding all PRNGs deterministically and recording seeds

c) Using system time as seed

d) Relying on hardware RNGs without recording

8. In the Bronze/Silver/Gold reproducibility tiers, Silver typically requires:

a) A findable DOI only

b) A runnable environment artifact (container/VM)

c) Bitwise-identical rebuild instructions

d) Written methods without artifacts

9. [Mehrfachauswahl] Which are FAIR principles relevant to data reuse?

a) Findable

b) Accessible

c) Interoperable

d) Reusable

10. Which hash property is most useful to detect accidental changes in a binary artifact?

a) Preimage resistance

b) Collision resistance

c) Sensitivity (small change → different hash)

d) Homomorphic property

11. Reproducible builds aim to ensure that building from source produces:

a) Functionally equivalent binaries only

b) Bitwise-identical artifacts when built with the same inputs

c) Faster compile times

d) Reduced disk usage

12. What is the principal danger of embedding __TIME__ or __DATE__ macros into builds?

a) They make builds non-deterministic across times

b) They increase the binary size significantly

c) They improve provenance

d) They are required for reproducible hashing

13. Which CI job design helps catch reproducibility regressions early?

a) Running only unit tests locally

b) Adding a nightly job that rebuilds and compares hashes

c) Manual rebuilds by the PI

d) Running tests without installing dependencies

14. The primary purpose of a lockfile (e.g., package-lock.json) is to:

a) Document only declared (loose) dependency ranges

b) Pin exact resolved dependency versions for reproducible installs

c) Replace semantic versioning

d) Seal license information

15. [Mehrfachauswahl] Which are valid methods to archive a reproducible release for long-term preservation?

a) Publishing source and containers to a DOI-enabled archive (Zenodo)

b) Only sharing code via email

c) Storing snapshots in a public repository with a release tag

d) Providing opaque binaries without source

16. Which statement about containers vs VMs is true regarding reproducibility?

a) Containers virtualize hardware, VMs do not

b) VMs include the full OS image while containers share the host kernel

c) Containers always guarantee bitwise reproducibility

d) VMs cannot be archived

17. What does "prospective provenance" record?

a) What actually ran during execution

b) The planned workflow and intended parameter values

c) The researcher’s intentions in natural language

d) The license of the dataset

18. Which license is most permissive for data reuse?

a) CC-BY

b) CC0

c) Proprietary EULA

d) All rights reserved

19. [Mehrfachauswahl] Which practices improve reproducibility of computational notebooks (e.g., Jupyter)?

a) Relying on notebook cells run in arbitrary order

b) Use of explicit execution order, environment capture, and a kernel restart-run-all

c) Recording and committing environment specification (requirements, lockfile)

d) Keeping large raw data blobs inside the notebook file

20. Which is a common cause of non-reproducible floating-point results across platforms?

a) Different CPU instruction ordering and math libraries

b) Identical compiler flags everywhere

c) Using integers only

d) Deterministic hashing

21. What is the value of a reproducibility badge or tier on a paper/repository?

a) Guarantees permanence of data

b) Signals the artifact meets a stated reproducibility standard

c) Replaces peer review

d) Prevents legal disputes

22. Which is NOT a typical use of cryptographic signing in reproducibility workflows?

a) Authenticate authorship of a release

b) Ensure integrity of distributed artifacts

c) Preventing reading of the data (encryption is for that)

d) Make builds faster

23. [Mehrfachauswahl] Which of the following are provenance capture levels often discussed?

a) Prospective (workflow plan)

b) Execution/retrospective traces

c) Source-code-only records without execution context

d) Version provenance (git SHA, package versions)

24. Which workflow system feature most directly helps portability across compute clusters?

a) Hardcoded absolute paths in scripts

b) Containerized task execution and abstracted resource specification

c) Using local-only shared filesystems without abstraction

d) Embedding secrets in plaintext

25. What is "bit-for-bit" reproducibility typically required for?

a) Human-readable papers

b) Cryptographic verification and exact archival replication

c) Conceptual demonstrations where outputs may vary

d) Only for images, not code

26. Which test type is most useful to detect subtle nondeterminism introduced by concurrency?

a) Unit tests only

b) Reproducibility integration tests that run full pipelines repeatedly

c) Static code analysis alone

d) Linting

27. Which metadata field is essential to make an artifact findable via DOI?

a) License omitted

b) Title, authors, date, and persistent identifier mapping

c) Only a README without metadata

d) Binary checksum only

28. [Mehrfachauswahl] Which are effective strategies to reduce environment drift over time?

a) Pinning dependency versions and recording lockfiles

b) Avoiding any dependency management

c) Rebuilding images from immutable base layers with pinned packages

d) Periodic rebuilds and automatic tests

29. Which of the following best describes "replication" in the course taxonomy?

a) Same team, same setup

b) Different team, different setup, same research question and conclusions

c) Different implementation that intentionally changes the research question

d) Running the same code twice on the same machine

30. Which of these is the BEST reason to publish a minimal example (minimal reproducible example)?

a) To hide complex parts of the research

b) To allow others to quickly understand and reproduce the core behavior

c) To replace the main repository

d) To reduce the need for tests

31. What is the role of continuous integration (CI) in reproducibility?

a) It automatically enforces reproducibility checks, builds, and tests on commits or PRs

b) It is only for deployment

c) It replaces documentation

d) It verifies legal compliance

32. Which is true about large binary data under FAIR principles?

a) Large data must be publicly downloadable without restriction to be FAIR

b) FAIR allows access-restricted data if metadata and access procedures are clear

c) FAIR forbids sensitive data

d) FAIR is only about licensing

33. Which action can harm reproducibility when modifying a build system?

a) Pinning compilers and flags

b) Introducing non-deterministic timestamps into build outputs

c) Recording full build logs

d) Adding deterministic metadata

34. [Mehrfachauswahl] Which items should be in a reproducible project's README to help others reproduce results?

a) Exact commands to run the analysis

b) Environment specification and how to obtain data

c) Private credentials necessary to access the compute cluster

d) Expected outputs and how to validate them (checksums)

35. Which licensing choice can block downstream open reuse of a dataset?

a) CC-BY

b) CC0

c) Restrictive proprietary license with non-commercial clauses

d) MIT

36. What is a primary benefit of using package registries with imm# Xiaomi Poco X8 Pro Maxutability guarantees (e.g., content-addressed storage)?

a) They always provide the latest versions only

b) They allow retrieving exact artifacts by content hash, aiding reproducible fetches

c) They remove the need for provenance

d) They speed up local computation

37. Which approach best documents the random seeds used during a pipeline run for full reconstruction later?

a) Not recording them and assuming determinism

b) Logging all seeds and RNG states to execution provenance and archiving them with the run

c) Using the same default seed on every machine without recording

d) Using weak, time-based seeds only

38. Which is the correct sequence when preparing a reproducible release?

a) Publish binaries → create DOI → tag source

b) Tag source with release version → build artifacts from tagged source → archive artifacts with DOI and checksums

c) Create DOI then tag source

d) Build from latest master without tagging

39. [Mehrfachauswahl] When reproducing someone else's results, which steps are recommended before running anything?

a) Read the README and methods section

b) Verify licenses and data access conditions

c) Randomly change parameters to see different outcomes

d) Validate checksums and environment specifications

40. Which is the best short justification for investing in reproducibility engineering for academic research?

a) Reproducibility increases citation counts only

b) It strengthens scientific claims, enables reuse, and reduces wasted effort across the community

c) It primarily benefits industry partners only

d) It is a bureaucratic checkbox with no scientific value

---

## Answer Key (brief)

1. b
2. d
3. a, b, d
4. b
5. b
6. b
7. b
8. b
9. a, b, c, d
10. c
11. b
12. a
13. b
14. b
15. a, c
16. b
17. b
18. b
19. b, c
20. a
21. b
22. d (signing not for encryption; c is about encryption)
23. a, b, d
24. b
25. b
26. b
27. b
28. a, c, d
29. b
30. b
31. a
32. b
33. b
34. a, b, d
35. c
36. b
37. b
38. b
39. a, b, d
40. b

*Generated: concise 40-question mock exam covering all lecture topics — use as a timed practice. If you want a version with expanded solutions or to replace the original file, confirm and it will be created/edited accordingly.*
