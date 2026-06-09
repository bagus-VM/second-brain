1|# second-brain — Activity Log
2|
3|> Append-only. Professor White writes here; student reads here.
4|> Format: `## [YYYY-MM-DD] OPERATION | title | details`
5|> Grep tip: `grep "^\#\# \[" log.md | tail -10` → last 10 entries
6|
7|---
8|
9|## [2026-06-01] BOOTSTRAP | Vault initialized | Professor White is online.
10|
11|The second-brain vault has been set up and Professor White is ready.
12|
13|**Vault structure created:**
14|- `raw/` — drop lecture slides, papers, textbook chapters here
15|- `vault/` — compiled knowledge lives here (Professor White writes this)
16|- `study/` — flashcards, practice problems, exam prep (Professor White generates this)
17|- `courses/` — one folder per course
18|- `projects/` — projects, seminar papers, thesis ideas
19|
20|**Next steps:**
21|1. Drop your first lecture slide into `raw/lectures/`
22|2. Tell Professor White: "ingest [filename]"
23|3. Watch the vault grow.
24|
25|*"The chemistry must be perfect."*
26|
27|---
28|
29|## [2026-06-01] INGEST | ALL lectures × 4 courses (parallel batches) | 294 pages created
30|
31|Full ingestion of all lecture material for the four nearest-exam courses:
32|
33|**Multimedia Databases** — 6 lectures, 73 pages
34|  L01: Introduction (MMDBMS, query predicates, retrieval types)
35|  L02: Colors (RGB, HSV, CIE, gamut, L*a*b*, YUV)
36|  L03: Images & Dithering (bitmap, JPEG/JPEG2000, SVG, Bézier, convolution)
37|  L04: Text/Video/Audio (Unicode, containers, Nyquist, PCM, shot segmentation)
38|  L05: Compression (Huffman, RLE, LZ77, MPEG, H.264, rate-distortion)
39|  L06: Modeling (MPEG-7, semantic gap, feature extraction, similarity)
40|
41|**Network Science** — 9 lectures, 128 pages
42|  L01: Introduction (networks, centrality, diffusion, communities)
43|  L02: Graph Theory (BFS, DFS, Dijkstra, Eulerian, connectivity)
44|  L03: Strong/Weak Ties (Granovetter, triadic closure, structural holes)
45|  L04: Communities (modularity, Louvain/Leiden, spectral partitioning)
46|  L05: Social Context (homophily, selection vs socialization, echo chambers)
47|  L06: Structural Balance (Heider, signed graphs, frustration index)
48|  L07: Small-World (Watts-Strogatz, Kleinberg, scale-free, preferential attachment)
49|  L08: Network Dynamics (SIR, R0, complex contagion, threshold cascades)
50|  L09: Graph Embeddings (DeepWalk, Node2Vec, GNNs, spectral methods)
51|
52|**Reproducibility Engineering** — 5 lectures, 44 pages
53|  L01: Repeat/Reproduce/Replicate (definitions, crisis, artifacts)
54|  L02: Levels & Provenance (VisTrails, bronze/silver/gold, workflow reproducibility)
55|  L03: Hypotheses (p-values, confidence intervals, effect sizes, replication crisis)
56|  L04: Git (DAG, branching, merging, patches, DCO, reproducibility)
57|  L05: Reproducible Builds (deterministic, source-date-epoch, diffoscope, CI/CD)
58|
59|**Software Analyse** — 5 lectures, 49 pages
60|  L01: Introduction (static vs dynamic, abstract interpretation, Rice's theorem)
61|  L02: Tokens & Naturalness (lexing, n-gram models, code naturalness, perplexity)
62|  L03: Parsing (CFG, AST, LL/LR, shift-reduce, syntax-directed translation)
63|  L04: Control Flow (CFG, basic blocks, dominance, CDG, natural loops)
64|  L05: Data Flow (gen/kill, reaching definitions, live variables, worklist algorithm)
65|
66|Total: 294 vault pages across 4 courses. All cross-linked with [[wikilinks]].
67|All course pages updated with full ingestion status.
68|
69|*\"294 pages. That's not a study vault — that's a weapon. Say it back to me:
70|what are the three key ideas from each course?\"*
71|
72|---
73|
74|## [2026-06-01] INGEST | Lecture 1 × 4 courses (parallel) | 32 pages created
75|
76|First batch ingestion — Lecture 1 from all four nearest-exam courses:
77|
78|**Multimedia Databases L01** — 8 concept pages + 1 topic overview
79|  Concepts: multimedia definition, discrete vs continuous media, multimedia system,
80|  data streams (async/sync/isochronous), MMDBMS intro, structured vs unstructured retrieval,
81|  multimedia query predicates, main domains
82|
83|**Network Science L01** — 8 concept pages + 1 topic overview
84|  Concepts: network intro, real-world examples, edge types, network effects,
85|  connected components, community structure, network diffusion (SI/SIS/SIR), centrality
86|
87|**Reproducibility Engineering L01** — 5 concept pages + 1 topic overview
88|  Concepts: repeat/reproduce/replicate, reproducibility crisis, artifact availability,
89|  research artifacts, types of reproducibility
90|
91|**Software Analyse L01** — 7 concept pages + 1 topic overview
92|  Concepts: software analysis, static vs dynamic, abstract interpretation,
93|  Rice's theorem, soundness/completeness, hierarchy of analysis, code clones
94|
95|Total: 32 new pages. All cross-linked with [[wikilinks]].
96|All course pages updated with ingestion status.
97|
98|*\"Four lectures, four courses, one pass. That's how you build momentum.\"*
99|
100|---
101|
102|## [2026-06-01] COURSES | All 6 courses registered | exam dates locked in
103|
104|Exam calendar:
105|- Multimedia Databases — 21/07/2026 (nearest)
106|- Network Science — 28/07/2026
107|- Reproducibility Engineering — 30/07/2026
108|- Software Analyse — 31/07/2026
109|- IoT Security — 05/08/2026
110|- Introduction to Microelectronics — 06/08/2026
111|
112|Course pages created in `courses/` with full syllabus tracking.
113|66 raw source files registered. Vault at 0 compiled pages.
114|Priority order established by exam proximity.
115|
116|*\"The sooner we cook, the sooner you eat.\"*
117|
118|---
119|
120|## [2026-06-01] SETUP | Full directory structure created | 13 folders, 14 guide notes
121|
122|All directories and guide notes in place:
123|
124|**raw/** — 4 subfolders (lectures, papers, textbooks, assets) + guide notes explaining what goes where
125|**vault/** — 4 subfolders (concepts, algorithms, topics, connections) + guide notes with page format
126|**study/** — 3 subfolders (flashcards, practice, exams) + guide notes with format descriptions
127|**courses/** — ready for course folders
128|**projects/** — ready for project folders
129|
130|Each subfolder has a markdown guide note that explains its purpose and shows up in Obsidian's file explorer. The vault is ready for content.
131|
132|*"Let's cook."*
133|
134|---

## [2026-06-02] INGEST | IoT Security - Lectures 1-5 | 34 pages created

Source: 5 lecture PDFs (IoTsec1-5_2026.pdf) + extraction analysis
Professor: Dr. Nikolaos Athanasios Anagnostopoulos, University of Passau

29 concept pages: internet-of-things, iot-architecture, iot-connectivity-protocols, cia-triad, information-assurance, iot-attack-taxonomy, mirai-botnet, krack-attack, zigbee-pairing-vulnerability, threat-modelling, security-by-design, attack-tree, fault-tree, devops-security, operational-security-lifecycle, attack-surface-analysis, physical-unclonable-functions, trusted-platform-module, secure-development-lifecycle, iot-2.0, iot-compliance-frameworks, resilience-iot, ota-updates, iot-firewalling, device-memory-attack-surface, physical-interface-attack-surface, firmware-security, web-interface-vulnerabilities, ecosystem-communications-security

5 topic pages: iot-security-landscape, iot-common-attacks, iot-secure-design, iot-attack-surfaces, iot-security-hardware

1 course page: courses/iot-security/course.md

Coverage: IoT fundamentals, connectivity protocols, information assurance, 9 attack categories, threat modelling, DevOps security, operational lifecycle, Miessler's 15 attack surface classes, hardware security (PUFs/TPMs), compliance frameworks.

---

## [2026-06-02] INGEST | Introduction to Microelectronics - Lectures 1-5 | 39 pages created

Source: 5 lecture PDFs (Microelectronics1-5_2026.pdf) + extraction analysis
Professor: Dr. Nikolaos Athanasios Anagnostopoulos, University of Passau
Textbook: Sedra, Smith, Carusone and Gaudet, Microelectronic Circuits, OUP 2019

34 concept pages: electronics, microelectronics, nanoelectronics, semiconductor, silicon, bandgap, valence-band, conduction-band, intrinsic-semiconductor, doping, n-type-semiconductor, p-type-semiconductor, p-n-junction, depletion-region, diode, zener-diode, zener-breakdown, avalanche-breakdown, rectifier, half-wave-rectifier, full-wave-rectifier, bridge-rectifier, clamper-circuit, limiter-circuit, transistor, mosfet, mos-capacitor, threshold-voltage, nmos-transistor, pmtransistor, mosfet-operating-regions, ion-implantation, thermal-diffusion, photolithography

5 topic pages: semiconductor-physics, doping-and-extrinsic-semiconductors, p-n-junction-overview, diode-applications, mos-transistors

1 course page: courses/introduction-to-microelectronics/course.md

Coverage: semiconductor physics, band theory, doping methods, P-N junction behavior, diode applications (rectifiers/clampers/limiters), Zener/avalanche breakdown, MOSFET structure and operating regions (nMOS/pMOS cutoff/linear/saturation). Lectures 6-10 (CMOS, op-amps, digital circuits, AI-assisted design, post-CMOS) not yet covered - awaiting raw material.

## [2026-06-02] REFACTOR | Lecture Naming Standardization | 10 pages renamed

Renamed IoT Security and Microelectronics concept pages to standardized lecture format:

**IoT Security (5 pages):**
- iot-security-landscape.md → iot-lecture-1.md
- iot-common-attacks.md → iot-lecture-2.md
- iot-attack-surfaces.md → iot-lecture-3.md
- iot-secure-design.md → iot-lecture-4.md
- iot-security-hardware.md → iot-lecture-5.md

**Introduction to Microelectronics (5 pages):**
- semiconductor-physics.md → microelectronics-lecture-1.md
- doping-and-extrinsic-semiconductors.md → microelectronics-lecture-2.md
- p-n-junction-overview.md → microelectronics-lecture-3.md
- diode-applications.md → microelectronics-lecture-4.md
- mos-transistors.md → microelectronics-lecture-5.md

All internal wikilinks [[updated]] to match new filenames. Now consistent with multimedia-databases-lecture-NN, network-science-lNN, reproducibility-engineering-lecture-N, software-analyse-lecture-N naming convention.

## [2026-06-02] INGEST | Übung Sheets — 3 courses, 17 sheets | 34 files created

Source: 17 exercise PDFs + 10 solution PDFs across 3 courses.

Practice pages (17 files in study/practice/):
- MMDB: mmdb-ex01.md through mmdb-ex06.md (Ex01-Ex05 with collapsible solutions, Ex06 without)
- Network Science: network-science-e01.md through network-science-e06.md (e01-e05 with solutions, e06 without)
- Reproducibility Engineering: reproducibility-engineering-sheet-1.md through sheet-5.md (no solutions available)

Flashcard decks (17 files in study/flashcards/):
- 3-5 Q&A cards per sheet, collapsible callout format
- All using [!question]-Question / [!answer]-Answer blocks

Course pages updated: all exercises marked **ingested** ✅
Coverage: 44 total exercises across 17 sheets. IoT Security, Software Analyse, Microelectronics have no Übung files.

## [2026-06-04] REPAIR | Broken wikilinks fixed | 46 concept pages created, 7 source files fixed

Problem: 70 broken wikilinks across the vault — topic pages referenced concept pages that didn't exist.

**IoT Security (12 new pages):**
common-criteria, etsi-en-303-645, fips-140-2, iec-62443, nist-iot-cybersecurity, owasp-iot-top-10, tcg-specifications, secure-boot-chain, key-management-lifecycle, risk-assessment-frameworks, security-principles, principle-of-least-privilege

**IoT Security (additional 8 pages):**
iot-common-attacks, iot-secure-design, iot-security-hardware, iot-security-landscape, iot-attack-surfaces, denial-of-service, small-world-networks, dataflow-analysis, availability

**Microelectronics (4 new pages by subagent + 16 additional):**
germanium, band-theory, electricity, capacitor, analog-amplifier, cmos-inverter, common-source-amplifier, conductor, digital-logic, etching, insulator, power-supply, mask-alignment, + 3 more

**Network Science (5 new pages):**
network-science-graph-fundamentals, spectral-clustering, hierarchical-navigable-small-world, signed-networks, word2vec-skip-gram

**Network Science (additional 5 pages):**
network-community-structure-l06, network-centrality-l04, network-dynamics-l08, network-navigation-small-worlds-l07, network-science-l01-overview, scale-free-epidemic-threshold-vanishes, sis-model, sirs-model, weak-ties-and-bridges

**Software Analyse (5 new pages):**
common-subexpression-elimination, dead-code-elimination, liveness-analysis, monotone-framework, register-allocation, finite-automata, widening-narrowing

**Source files fixed (7 files):**
- microelectronics-lecture-1.md through lecture-5.md: case normalization (Silicon→silicon, Diode→diode, etc.)
- Removed [[page-1]] and [[page-2]] placeholder links from Vault.md and AGENTS.md

**Result:** 0 real broken wikilinks remaining (16 are intentional example text in wikilinks.md). Total concept pages: 184.

---

## [2026-06-05] QUERY | Software Analyse projects deep study | 3 new pages created

**Student request:** "Explain both codebases so I can study them, and help me study Java."

**Pages created (3):**
1. `vault/concepts/readability-classifier.md` — Deep study guide for Project 1: all four metrics (Halstead volume, token entropy, cyclomatic complexity, LOC) with theory, formulas, worked examples, ML pipeline explanation, common exam questions.
2. `vault/concepts/sign-analysis.md` — Deep study guide for Project 2: lattice theory, bitmask encoding, pairwise decomposition, transfer functions, inter-procedural analysis, fixpoint iteration, test cases to trace by hand.
3. `vault/concepts/java-for-software-analysis.md` — Java survival guide: classes, enums, generics, interfaces, static methods, annotations, streams/lambdas, exceptions, Maven, JavaParser (AST/visitors), ASM (bytecode/interpreter), WEKA (ML), picocli (CLI), JUnit, design patterns (visitor, strategy, template method).

**Also updated:**
- `projects/software-analyse/SOFTWARE_ANALYSE_PROJECTS.md` — Added cross-links to the three new deep study pages.
- `index.md` — Added "Projects" subsection under Software Analyse with all 4 project pages. Updated page count to 376.

---

## [2026-06-05] LINT | Full vault scan | 9 contradictions resolved, 2 pages created, 36 study pages linked

**Scan results:**
- 513 .md files scanned
- 107 broken wikilinks found
- 73 orphan pages (14%)
- 7 duplicate concept pairs + 2 near-duplicates (contradictions)
- 72 concepts with source_count: 0
- 149 pages with empty Open Questions sections

**Fixes applied:**

1. MERGED 7 DUPLICATE PAIRS (vault/ root → vault/concepts/):
   - centrality-measures, girvan-newman-algorithm, louvain-algorithm, modularity, leiden-algorithm, hierarchical-clustering, zacharys-karate-club
   - Unique content from root versions merged into concepts/ versions
   - Root copies deleted (7 files)

2. MERGED 2 NEAR-DUPLICATES:
   - threat-modelling.md + threat-modeling.md → threat-modeling.md (16 wikilinks updated across 10 files)
   - dataflow-analysis.md + data-flow-analysis.md → data-flow-analysis.md (2 wikilinks updated across 2 files)
   - Obsolete copies deleted (2 files)

3. CREATED [[electron-hole]] page:
   - vault/concepts/electron-hole.md — Quasiparticle concept for Microelectronics L01

4. LINKED 36 ORPHAN STUDY PAGES:
   - vault/study-materials-index.md created — master index linking all 18 flashcard decks + 18 practice problem sets
   - Added to index.md under new "Study Materials" section

**Net result:** 9 files deleted, 2 files created. Page count: 376 → 369. All contradictions resolved.

---

## [2026-06-05] LINT | Network Science orphan pages linked | 7 pages connected, 34 wikilinks added

**Problem:** 7 Network Science content pages had zero inbound wikilinks — completely disconnected from the vault graph.

**Fixes applied (19 files modified):**
- edge-betweenness.md → 6 inbound links (from betweenness-centrality, girvan-newman, centrality-measures, community-detection, l04)
- embedding-based-community-detection.md → 7 inbound links (from community-detection, louvain, leiden, node2vec, graph-neural-networks, l04, community-detection-overview)
- graph-partitioning.md → 5 inbound links (from community-detection, community-detection-overview, kernighan-lin, graph-partitioning-cut-spectral, l04)
- modularity-resolution-limit.md → 6 inbound links (from modularity, community-detection, louvain, leiden, community-detection-overview, l04)
- network-autocorrelation.md → 6 inbound links (from homophily, selection-vs-socialization, echo-chambers, affiliation-networks, l05)
- presenting-experiments.md → 5 inbound links (from reproducibility-lecture-3, hypothesis-formulation, effect-sizes, confidence-intervals, reproducibility course)
- product-space-network.md → 4 inbound links (from community-detection, community-detection-overview, modularity, l04)

Also added outbound links from embedding-based-community-detection to node2vec and graph-neural-networks.

**Result:** All 7 pages now have 4-7 inbound links. Zero orphan content pages remaining in Network Science.

## [2026-06-08] QUERY | IoT Security Exam Format Ingested | 1 page created, 1 updated

Ingested email from Dr. Nikolas detailing IoT Security exam structure:
- Written exam, 60–90 minutes
- Three question types: definitions, use case scenarios, security solutions
- Definitions: own wording acceptable, must be valid
- Use case scenarios: assets → threats → attacks → countermeasures → CIA mapping → cost/expertise
- Security solutions: explain *how* a mechanism works (digital signature confirmed as example)

**Pages affected:**
- Created: `study/exams/iot-security-exam-format.md` — full exam format breakdown with worked example
- Updated: `courses/iot-security.md` — added exam format section, linked to prep page
- Updated: `index.md` — noted exam format confirmed

## [2026-06-08] QUERY | Digital Signatures concept page | 1 page created, 5 pages connected

Created `vault/concepts/digital-signatures.md` — full concept page covering:
- KeyGen/Sign/Verify model, hash-then-sign workflow
- RSA, ECDSA, Ed25519 comparison (all three referenced in IoT lectures for firmware signing)
- Worked example: firmware update signature verification
- Pitfalls: nonce reuse, MAC vs signature confusion, forgetting certificate verification

**Inbound connections added from:**
- `iot-security-exam-format.md` — confirmed exam question
- `firmware-security.md` — firmware signing mechanism
- `iot-lecture-4.md` (IoT Secure Design) — Goal 3 firmware integrity
- `trusted-platform-module.md` — TPM signing operations
- `ota-updates.md` — signed firmware updates

## [2026-06-09] LINT | Full vault audit + repair | 17 pages created, 2 fixed, 525 total

**Formatting fixes:**
- Fixed bare wikilink prerequisites in readability-classifier.md and sign-analysis.md
- No line prefix corruption, no date issues, no merged delimiters

**Pages created (17):**
- 5 Microelectronics topic overviews: semiconductor-physics, doping-and-extrinsic-semiconductors, p-n-junction-overview, diode-applications, mos-transistors
- 2 Microelectronics concepts: digital-circuit-design, vlsi-design
- 1 Microelectronics concept: pmos-transistor (sibling to nmos-transistor)
- 1 Software Analyse overview: software-analyse-projects-overview
- 4 Cross-course concepts: machine-learning-basics, pagerank-algorithm, six-degrees-of-separation, visitor-pattern
- 4 IoT Security concepts: actuators, authentication, non-repudiation, sensors

**Study materials:**
- Updated study-materials-index.md with all 39 study pages

**Remaining (non-blocking):**
- 5 broken links to future lectures (MMDB L07-L08, ReproEng L06-L08) — resolve on ingestion
- 15 broken links in raw/ (immutable, informational)
- 73 unsourced pages (source_count: 0) — need verification against raw lectures
- 429 empty Open Questions — systemic, low priority
