# second-brain — Master Index

> Maintained by Professor White. Updated after every INGEST and significant QUERY.

**Last updated:** 2026-06-22
**Total pages:** 592 (vault: 540 pages + study: 52 practice/flashcards/exam materials; excluding raw/)
**Active courses:** 6

---

## Exam Calendar
| Course | Exam Date | Days Left | Progress |
|--------|-----------|-----------|----------|
| [[multimedia-databases]] | 21 July 2026 | ~37 | **6/6 lectures ✅** + Ex01–Ex08 practice complete ✅ (83+ pages) |
| [[network-science]] | 28 July 2026 | ~44 | **9/9 lectures ✅** + Ex01–Ex07 (138 pages) |
| [[reproducibility-engineering]] | 30 July 2026 | ~46 | **8/8 lectures ✅** + Sheet 1–7 (70+ pages) |
| [[software-analyse]] | 31 July 2026 | ~47 | **8/8 lectures ✅** (85+ pages) |
| [[iot-security]] | 05 Aug 2026 | ~52 | **7/7 lectures ✅** (~70 pages) + 3 papers ingested |
| [[introduction-to-microelectronics]] | 06 Aug 2026 | ~53 | **6/6 lectures ✅** (~45 pages) |

---

## 📚 Multimedia Databases (83 pages)

### L01 — Introduction
| Page | Summary | Status |
|------|---------|--------|
| [[multimedia-definition]] | MHEG classification, strict vs loose multimedia | current |
| [[media-types-discrete-continuous]] | Discrete (text, images) vs continuous (audio, video) | current |
| [[multimedia-system]] | Herrtwich/Steinmetz definition | current |
| [[data-streams]] | Async/sync/isochronous, FBR vs VBR | current |
| [[multimedia-database-intro]] | MMDBMS = DBMS + IR | current |
| [[structured-vs-unstructured-retrieval]] | DBMS vs IR, object-relational unifier | current |
| [[multimedia-query-predicates]] | Attribute, structure, spatial, semantic | current |

### L02 — Colors
| Page | Summary | Status |
|------|---------|--------|
| [[color-perception]] | Visible spectrum, cones, opponent processing | current |
| [[metamers]] | Different spectra, same perceived color (light/material/observer types) | current |
| [[chromatic-adaptation]] | Color constancy: same object looks same under different illuminants | current |
| [[color-models-overview]] | Additive vs subtractive | current |
| [[rgb-color-model]] | Additive color cube, 8-bit quantization | current |
| [[cmyk-color-model]] | Subtractive printing | current |
| [[hsv-color-model]] | Hue/Saturation/Value | current |
| [[cie-chromaticity-diagram]] | CIE XYZ, horseshoe diagram | current |
| [[color-gamut]] | Device gamut as triangle in CIE space | current |
| [[lab-color-space]] | Perceptual uniformity, ΔE distance | current |
| [[yuv-color-space]] | Luminance/chrominance, chroma subsampling | current |

### L03 — Images & Dithering
| Page | Summary | Status |
|------|---------|--------|
| [[image-representation-bitmap]] | Bitmap/raster as 2D pixel arrays | current |
| [[pixel-formats-and-bit-depth]] | 1-bit to 48-bit, ARGB | current |
| [[color-quantization]] | Reducing color count | current |
| [[dithering]] | Noise, pattern, error diffusion | current |
| [[floyd-steinberg-dithering]] | 7/16, 3/16, 5/16, 1/16 kernel | current |
| [[image-file-formats]] | TIFF, GIF, PNG, JPEG comparison | current |
| [[jpeg-compression-pipeline]] | DCT → quantization → entropy encoding | current |
| [[vector-graphics-svg]] | Resolution independence | current |
| [[bezier-curves]] | Bernstein polynomials, Hermite splines | current |
| [[linear-convolution-filters]] | Kernel convolution, Sobel, Gaussian | current |

### L04 — Text/Video/Audio
| Page | Summary | Status |
|------|---------|--------|
| [[ascii-unicode-character-encoding]] | ASCII, Unicode, UTF-8/16/32 | current |
| [[video-formats-container-vs-codec]] | MP4/MKV vs H.264/VP9/AV1 | current |
| [[video-frame-rate-resolution]] | Progressive vs interlaced, PAL/HD/4K | current |
| [[shot-segmentation]] | Hard cut/fade/dissolve detection | current |
| [[audio-sampling-nyquist-theorem]] | Nyquist-Shannon, sampling rates | current |
| [[pcm-digital-audio]] | PCM encoding, CD quality | current |

### L05 — Compression
| Page | Summary | Status |
|------|---------|--------|
| [[lossless-vs-lossy-compression]] | Entropy vs source coding | current |
| [[entropy-coding-huffman-arithmetic]] | Huffman tree, arithmetic coding | current |
| [[run-length-encoding]] | RLE, JPEG's zero-RLE | current |
| [[lz77-lzw-compression]] | Dictionary-based, Deflate | current |
| [[transform-coding]] | DCT/DWT, energy compaction | current |
| [[mpeg-video-compression]] | I/P/B frames, GOP, motion estimation | current |
| [[h264-avc-video-compression]] | Flexible partitions, CABAC | current |
| [[rate-distortion-theory]] | R(D) function, QP control | current |

### L06 — Modeling
| Page | Summary | Status |
|------|---------|--------|
| [[semantic-gap]] | Features vs human interpretation | current |
| [[sensory-gap]] | Real-world vs recordings | current |
| [[mpeg-7]] | ISO/IEC 15938, 12 parts | current |
| [[mpeg-7-descriptors]] | 20 visual descriptor types | current |
| [[feature-extraction]] | Computing low-level features | current |
| [[content-based-retrieval]] | Searching by content | current |
| [[feature-vector]] | Numerical representation of multimedia content | current |
| [[minkowski-distance]] | L1, L2, L∞ family of distance functions | current |
| [[chi-squared-distance]] | Scale-invariant histogram distance | current |
| [[kolmogorov-smirnov-distance]] | Max cumulative difference for histograms | current |
| [[curse-of-dimensionality]] | Why nearest-neighbour loses meaning in high-D | current |
| [[similarity-measures]] | Quantifying closeness | current |
| [[object-relational-databases]] | Relational DBs extended with objects, inheritance, UDTs | current |
| [[sql-mm]] | ISO/IEC 13249 SQL multimedia extension for content-based queries | current |
| [[mpqf]] | MPEG Query Format: standardized multimedia query expressions | current |


### Practice & Flashcards
| Page | Summary | Status |
|------|---------|--------|
| [[mmdb-ex01]] | Exercise sheet 1: multimedia fundamentals | current |
| [[mmdb-ex02]] | Exercise sheet 2: color models | current |
| [[mmdb-ex03]] | Exercise sheet 3: image processing | current |
| [[mmdb-ex04]] | Exercise sheet 4: compression | current |
| [[mmdb-ex05]] | Exercise sheet 5: retrieval & features | current |
| [[mmdb-ex06]] | Exercise sheet 6: distance metrics | current |
| [[mmdb-ex07]] | Exercise sheet 7: evaluation | current |
| [[mmdb-ex01-flashcards]] | Flashcards for Ex01 | current |
| [[mmdb-ex02-flashcards]] | Flashcards for Ex02 | current |
| [[mmdb-ex03-flashcards]] | Flashcards for Ex03 | current |
| [[mmdb-ex04-flashcards]] | Flashcards for Ex04 | current |
| [[mmdb-ex05-flashcards]] | Flashcards for Ex05 | current |
| [[mmdb-ex06-flashcards]] | Flashcards for Ex06 | current |
| [[mmdb-ex07-flashcards]] | Flashcards for Ex07 | current |
| [[mmdb-ex08]] | Exercise sheet 8: querying, object-relational DBs, SQL/MM, MPQF | current |
| [[mmdb-exam-prediction]] | Exam prediction: 11 archetypes, top-3 targets | current |

---

## 📚 Network Science (138 pages)

### L01 — Introduction
| Page | Summary | Status |
|------|---------|--------|
| [[network-intro]] | Nodes + edges, lossy abstraction | current |
| [[edge-types]] | Directed, undirected, weighted | current |
| [[centrality]] | Degree, closeness, betweenness | current |
| [[network-diffusion]] | SI/SIS/SIR models, R0 | current |
| [[community-structure]] | Dense clusters, modularity | current |

### L02 — Graph Theory
| Page | Summary | Status |
|------|---------|--------|
| [[graph-fundamentals]] | G=(V,E), modeling choices | current |
| [[graph-representations]] | Edge list, adjacency list/matrix | current |
| [[neighbourhood-and-degree]] | N(v), deg(v), handshaking lemma | current |
| [[paths-walks-and-cycles]] | Walk → path → cycle hierarchy | current |
| [[shortest-path-and-diameter]] | dist(u,v), diam(G) | current |
| [[eulerian-path-and-circuit]] | Königsberg, degree parity | current |
| [[breadth-first-search]] | BFS, FIFO, O(|V|+|E|) | current |
| [[depth-first-search]] | DFS, LIFO, cycle detection | current |
| [[dijkstras-algorithm]] | Weighted shortest paths | current |
| [[connectivity-and-components]] | Connected, giant component | current |

### L03 — Strong/Weak Ties
| Page | Summary | Status |
|------|---------|--------|
| [[triadic-closure]] | Open triads close into triangles | current |
| [[clustering-coefficient]] | Node-level neighborhood density | current |
| [[bridges-and-local-bridges]] | Bridges disconnect graph | current |
| [[weak-ties-hypothesis]] | Granovetter's theorem | current |
| [[structural-holes]] | Burt's brokerage theory | current |
| [[social-capital]] | Bonding vs bridging | current |

### L04 — Communities
| Page | Summary | Status |
|------|---------|--------|
| [[modularity]] | Q formula, NP-hard, resolution limit | current |
| [[girvan-newman-algorithm]] | Divisive edge-betweenness | current |
| [[louvain-algorithm]] | Local moves + aggregation | current |
| [[leiden-algorithm]] | Refinement before aggregation | current |
| [[graph-partitioning-cut-spectral]] | Min-cut, Fiedler vector | current |
| [[zacharys-karate-club]] | 34-node benchmark | current |

### L05 — Social Context
| Page | Summary | Status |
|------|---------|--------|
| [[homophily]] | Random-mixing baseline, index r | current |
| [[selection-vs-socialization]] | Three mechanisms | current |
| [[affiliation-networks]] | Bipartite, co-occurrence | current |
| [[schelling-segregation-model]] | Threshold, micro-macro gap | current |
| [[echo-chambers]] | Cinelli et al., platform ranking | current |
| [[ei-index]] | (E−I)/(E+I) measure of homophily | current |
| [[triadic-focal-membership-closure]] | Three projection-edge-formation mechanisms in bipartite networks | current |
| [[confounding]] | Third explanation for observed correlation between similarity and tie | current |
| [[experiment-vs-observation]] | Experimental vs observational causal inference | current |
| [[manski-reflection-problem]] | Endogenous vs contextual effects not separately identified | current |
| [[kossinets-watts-2006]] | Empirical evolving network: triadic + focal + membership closure | current |



### L06 — Structural Balance
| Page | Summary | Status |
|------|---------|--------|
| [[signed-graphs]] | Signed graph definition | current |
| [[signed-networks]] | Signed networks: positive/negative edges, Heider | current |
| [[structural-balance-theory]] | Heider's cognitive dissonance; 1946 origin | current |
| [[balanced-triads]] | Four triangle types: (+,+,+) and (+,-,-) balanced under strong | current |
| [[balance-theorem]] | Cartwright-Harary 1956: ≤ 2 camps for balanced complete signed graphs | current |
| [[weak-structural-balance]] | Davis 1967: k-camp relaxation allowing (-,-,-) | current |
| [[frustration-index]] | Min edge flips, NP-hard | current |
| [[cycle-criterion]] | Balance ⟺ every cycle has even number of negatives | current |

### L07 — Small-World Networks
| Page | Summary | Status |
|------|---------|--------|
| [[milgrams-experiment-six-degrees]] | Letter experiment | current |
| [[small-world-property]] | d̄ ∝ log|V| | current |
| [[watts-strogatz-model]] | Regular + random rewiring | current |
| [[kleinberg-decentralized-search]] | Grid model, navigability | current |
| [[random-graphs]] | Erdős-Rényi G(n,p) | current |
| [[scale-free-networks]] | Power-law, hubs | current |
| [[preferential-attachment]] | Barabási-Albert, rich-get-richer | current |

### L08 — Network Dynamics
| Page | Summary | Status |
|------|---------|--------|
| [[simple-contagion]] | Single exposure sufficient | current |
| [[sir-model-network-epidemics]] | S→I→R compartments | current |
| [[basic-reproduction-number-r0]] | R0 = (β/γ)×⟨k⟩ | current |
| [[complex-contagion]] | Social reinforcement needed | current |
| [[threshold-cascades]] | q fraction rule | current |
| [[centola-2010-experiment]] | Clustered > random adoption | current |
| [[sis-model]] | Susceptible-Infected-Susceptible: no permanent immunity | current |
| [[sirs-model]] | SIRS: adds waning immunity (R→S) to SIR | current |
| [[scale-free-epidemic-threshold-vanishes]] | Scale-free networks: epidemic threshold → 0 | current |



### L09 — Graph Embeddings
| Page | Summary | Status |
|------|---------|--------|
| [[node-embeddings]] | Three waves of methods | current |
| [[deepwalk]] | Random walks + word2vec | current |
| [[node2vec]] | Biased walks, p/q parameters | current |
| [[graph-neural-networks]] | GCN, GraphSAGE, GAT, GIN | current |
| [[over-smoothing-in-gnns]] | Depth limit at 3-5 layers | current |
| [[link-prediction-via-embeddings]] | Scoring by proximity | current |
| [[pagerank-algorithm]] | Iterative ranking algorithm, damping factor, stationary distribution | current |
| [[six-degrees-of-separation]] | Milgram's experiment, small-world phenomenon | current |
| [[word2vec-skip-gram]] | Skip-gram: predict context from target, basis of DeepWalk | current |
| [[hierarchical-navigable-small-world]] | HNSW: layered graph for approximate nearest-neighbor search | current |



### Practice & Flashcards
| Page | Summary | Status |
|------|---------|--------|
| [[network-science-e01]] | Exercise sheet 1: what is a network? | current |
| [[network-science-e02]] | Exercise sheet 2: graph theory | current |
| [[network-science-e03]] | Exercise sheet 3: strong and weak ties | current |
| [[network-science-e04]] | Exercise sheet 4: centrality | current |
| [[network-science-e05]] | Exercise sheet 5: community detection | current |
| [[network-science-e06]] | Exercise sheet 6: diffusion | current |
| [[network-science-e07]] | Exercise sheet 7: embeddings | current |
| [[network-science-e01-flashcards]] | Flashcards for E01 | current |
| [[network-science-e02-flashcards]] | Flashcards for E02 | current |
| [[network-science-e03-flashcards]] | Flashcards for E03 | current |
| [[network-science-e04-flashcards]] | Flashcards for E04 | current |
| [[network-science-e05-flashcards]] | Flashcards for E05 | current |
| [[network-science-e06-flashcards]] | Flashcards for E06 | current |
| [[network-science-e07-flashcards]] | Flashcards for E07 | current |

### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[network-science-exercise-prep]] | Exercise-based exam prep: NetworkX functions, hand calculations, key formulas | current |

---

## 📚 Reproducibility Engineering (60 pages)

### L01 — Repeat/Reproduce/Replicate
| Page | Summary | Status |
|------|---------|--------|
| [[repeat-reproduce-replicate]] | The three R's | current |
| [[reproducibility-crisis]] | Nature survey, 52% significant | current |
| [[artifact-availability]] | ACM: public repo + DOI | current |
| [[types-of-reproducibility]] | Computational, empirical, statistical | current |

### L02 — Levels & Provenance
| Page | Summary | Status |
|------|---------|--------|
| [[levels-of-reproducibility]] | Availability, repeatability, confirmability | current |
| [[provenance-in-reproducibility]] | Prospective, execution, version | current |
| [[workflow-reproducibility]] | DAG-based workflows | current |
| [[reproducibility-standards-bronze-silver-gold]] | Heil et al. 2021 | current |

### L03 — Hypotheses
| Page | Summary | Status |
|------|---------|--------|
| [[hypothesis-formulation]] | PRECISE, SPECIFIC, UNAMBIGUOUS | current |
| [[null-and-alternative-hypothesis]] | H₀ vs H₁ | current |
| [[p-values]] | P(data≥obs|H₀), misinterpretations | current |
| [[statistical-significance]] | α, Type I/II, Bonferroni | current |
| [[effect-sizes]] | Cohen's d, significance ≠ importance | current |
| [[replication-crisis-and-hypothesis-testing]] | p-hacking, HARKing, PPV | current |

### L04 — Git
| Page | Summary | Status |
|------|---------|--------|
| [[git-dag-structure-and-internals]] | Blob, tree, commit, tag | current |
| [[git-branching-and-merging]] | Fast-forward vs three-way | current |
| [[git-commit-hygiene]] | Atomic commits, trailers | current |
| [[developer-certificate-of-origin]] | Signed-off-by, DCO vs CLA | current |
| [[git-for-reproducibility]] | Snapshot vs clone+patches | current |

### L05 — Reproducible Builds
| Page | Summary | Status |
|------|---------|--------|
| [[reproducible-builds]] | Bit-for-bit identical builds | current |
| [[deterministic-builds]] | Eliminating non-determinism | current |
| [[source-date-epoch]] | SOURCE_DATE_EPOCH env var | current |
| [[diffoscope]] | Deep comparison tool | current |
| [[ci-cd-for-reproducibility]] | Automated verification | current |
| [[make-and-build-systems]] | Make fundamentals | current |
| [[latexmk]] | Automates LaTeX compilation cycle, tracks deps via .fls | current |


### L06 — Database System Architectures
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-lecture-6]] | DB architectures (file-based, client/server), SQLite features, Docker Compose, foreign tables | current |
| [[containerization-for-builds]] | Docker for reproducible environments (prereq from L05) | current |
| [[binary-build-reproducibility]] | Bitwise-identical builds; the 4-snippet question (1 of 4 reproducible) | current |
| [[c-preprocessor]] | `__FILE__`, `__LINE__`, `__TIME__`, `__DATE__` as build-time non-determinism sources | current |
| [[out-of-source-build]] | Build artefacts in a separate dir; `mkdir build && cd build && ../configure` | current |
| [[make-dependency-tracking]] | Make's mtime-based incremental rebuild algorithm; phony targets; parallel builds | current |
| [[client-server-db-architecture]] | Server process + client library + network; the contrast to SQLite | current |
| [[foreign-tables-postgresql]] | Query external files (e.g., /proc/meminfo) as if SQL tables via file_fdw | current |

### L07 — Tidy Data
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-lecture-7]] | Wickham's tidy data, SQL pivoting/unpivoting, metadata workflows | current |
| [[tidy-data]] | Each variable = column, each observation = row, each value = cell | current |

### L08 — Hierarchical Dataformats
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-lecture-8]] | XML/JSON, JSON Schema, HDF5, h5py, visitor pattern | current |
| [[hdf5]] | Hierarchical data format: files/groups/datasets/attributes | current |
| [[json-schema]] | Vocabulary for validating JSON document structure | current |

### Practice & Flashcards
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-sheet-1]] | Sheet 1: repeat/reproduce/replicate | current |
| [[reproducibility-engineering-sheet-2]] | Sheet 2: levels & provenance | current |
| [[reproducibility-engineering-sheet-3]] | Sheet 3: hypotheses & statistics | current |
| [[reproducibility-engineering-sheet-4]] | Sheet 4: workflows & artifacts | current |
| [[reproducibility-engineering-sheet-5]] | Sheet 5: version control & Docker | current |
| [[reproducibility-engineering-sheet-6]] | Sheet 6: CI/CD & automation | current |
| [[reproducibility-engineering-sheet-1-flashcards]] | Flashcards for Sheet 1 | current |
| [[reproducibility-engineering-sheet-2-flashcards]] | Flashcards for Sheet 2 | current |
| [[reproducibility-engineering-sheet-3-flashcards]] | Flashcards for Sheet 3 | current |
| [[reproducibility-engineering-sheet-4-flashcards]] | Flashcards for Sheet 4 | current |
| [[reproducibility-engineering-sheet-5-flashcards]] | Flashcards for Sheet 5 | current |
| [[reproducibility-engineering-sheet-6-flashcards]] | Flashcards for Sheet 6 | current |
| [[reproducibility-engineering-sheet-7]] | Sheet 7: BenchBase lab — SQLite vs PostgreSQL benchmarking | current |
| [[reproducibility-engineering-sheet-7-flashcards]] | Flashcards for Sheet 7 | current |

---

## 📚 Software Analyse (75 pages)

### L01 — Introduction
| Page | Summary | Status |
|------|---------|--------|
| [[software-analysis]] | Structural vs behavioural | current |
| [[static-vs-dynamic-analysis]] | Code without execution vs observing runs | current |
| [[rices-theorem]] | All non-trivial properties undecidable | current |
| [[soundness-and-completeness]] | Over- vs under-approximation | current |
| [[code-clones]] | Types 1-4, detection strategies | current |

### L02 — Tokens & Naturalness
| Page | Summary | Status |
|------|---------|--------|
| [[lexical-analysis]] | Lexer, pattern matching | current |
| [[tokenization-and-token-types]] | Token categories, symbol table | current |
| [[finite-automata-and-regular-expressions]] | Regex ↔ DFA | current |
| [[n-gram-language-models]] | Unigram/bigram/trigram | current |
| [[code-naturalness-hypothesis]] | Hindle et al., code as language | current |
| [[perplexity-and-entropy]] | PP metrics, cross-entropy | current |
| [[smoothing-techniques]] | Laplace, Good-Turing, Kneser-Ney | current |

### L03 — Parsing
| Page | Summary | Status |
|------|---------|--------|
| [[context-free-grammar]] | CFG 4-tuple, productions | current |
| [[parse-tree]] | Concrete syntax trees | current |
| [[abstract-syntax-tree]] | AST construction | current |
| [[grammar-ambiguity]] | Multiple parse trees | current |
| [[predictive-parsing]] | LL(1), recursive descent | current |
| [[shift-reduce-parsing]] | Stack-based bottom-up | current |
| [[syntax-directed-translation]] | Attributes, semantic rules | current |

### L04 — Control Flow
| Page | Summary | Status |
|------|---------|--------|
| [[control-flow-graph]] | Directed graph, execution flow | current |
| [[basic-block]] | Maximal consecutive statements | current |
| [[dominance]] | Iterative fixed-point algorithm | current |
| [[dominator-tree]] | IDom computation | current |
| [[control-dependence]] | CDG construction | current |
| [[natural-loop]] | Back edges, loop identification | current |

### L05 — Data Flow
| Page | Summary | Status |
|------|---------|--------|
| [[data-flow-analysis]] | Gen/kill, IN/OUT equations | current |
| [[reaching-definitions]] | Forward may | current |
| [[available-expressions]] | Forward must | current |
| [[live-variable-analysis]] | Backward may | current |
| [[very-busy-expressions]] | Backward must | current |
|| [[iterative-data-flow-analysis]] | Worklist algorithm | current |

### L06 — Abstract Interpretation (Data Flow Part 2)
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-6]] | Lattice theory, MOP vs MFP, abstract interpretation, Zero Analysis | current |
| [[lattice]] | Partial order, join, meet, top, bottom, distributivity | current |
| [[mop-vs-mfp]] | MOP precise/undecidable vs MFP computable/sound; equal for distributive | current |
| [[distributive-framework]] | When transfer functions distribute over join; four classic analyses | current |
| [[minimal-fixed-point-algorithm]] | Worklist-based MFP computation algorithm | current |
| [[abstract-interpretation]] | Concrete→abstract domain, Galois connection, sound over-approximation | current |
| [[zero-analysis-worked-example]] | The lecture's running example: Z/NZ/MZ lattice, division-by-zero detection | current |

### L07 — Interprocedural and Heap Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-7]] | Interprocedural limits, context sensitivity, points-to, Steensgaard/Andersen | current |
| [[interprocedural-analysis]] | Beyond one function: call/return nodes, MVP ideal, context sensitivity | current |
| [[context-sensitivity]] | Distinguishing call contexts: 4 techniques (cloning, inlining, call strings, summaries) | current |
| [[cloning-context-sensitivity]] | Duplicate procedure per call site — most precise, code-size explosion | current |
| [[inlining-context-sensitivity]] | Substitute body at call site — perfect, but no termination for recursion | current |
| [[call-strings]] | Tag each call with sequence of call sites; k-bounded for termination | current |
| [[procedure-summaries]] | Compose transfer function for procedure; apply at every call site | current |
| [[valid-paths]] | Interprocedural paths respecting call-return matching | current |
| [[meet-over-valid-paths]] | Precise but undecidable interprocedural ideal (MVP) | current |
| [[points-to-analysis]] | Which heap objects each pointer can refer to | current |
| [[steensgaards-points-to-analysis]] | Fast equality-based, O(nα(n,n)) via Union-Find, imprecise | current |
| [[andersens-points-to-analysis]] | Precise subset-based, O(n³), inclusion-based constraints | current |
| [[heap-analysis]] | Family of analyses for heap memory; design space of 9 axes | current |
| [[aliasing]] | Two names for same memory location; alias sets from points-to | current |
| [[union-find-data-structure]] | Partition into equivalence classes; ~O(1) per op with path compression | current |

### L08 — Program Slicing
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-8]] | SSA form, PDG, slicing, interprocedural slicing, dynamic slicing | current |
| [[static-single-assignment]] | Each variable assigned once; phi functions at merge points | current |
| [[phi-function]] | Pseudo-assignment merging definitions from different control paths | current |
| [[program-dependence-graph]] | CFG nodes + control + data dependence edges = complete dependence map | current |
| [[program-slicing]] | Backward/forward slice via PDG reachability | current |
| [[system-dependence-graph]] | PDG extended to multiple procedures for interprocedural slicing | current |
| [[dynamic-slicing]] | Slice for specific input + execution trace | current |

### Projects
| Page | Summary | Status |
|------|---------|--------|
| [[readability-classifier]] | Code readability ML pipeline: Halstead, entropy, cyclomatic complexity, logistic regression | current |
| [[sign-analysis]] | Interprocedural sign analysis: lattice theory, pairwise decomposition, bytecode dataflow | current |
| [[java-for-software-analysis]] | Java essentials: Maven, JavaParser, ASM, WEKA, picocli, visitor pattern | current |

### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-codebase-defense]] | Exam defense prep: walk through both project codebases, explain design decisions, articulate concepts | current |
| [[software-analyse-projects-overview]] | Both projects overview, comparison, and study strategy | current |
| [[visitor-pattern]] | Design pattern for AST traversal, double dispatch | current |
| [[machine-learning-basics]] | Supervised learning, features, labels, classification | current |

---

## 📚 IoT Security (~60 pages)

### L01 — IoT Fundamentals
| Page | Summary | Status |
|------|---------|--------|
| [[internet-of-things]] | Definition and architecture of IoT | current |
| [[iot-architecture]] | Three-segment architecture: sensors, processing, actuators | current |
| [[iot-connectivity-protocols]] | Wi-Fi, LoRaWAN, BLE, ZigBee, CAN comparison | current |
| [[cia-triad]] | Confidentiality, Integrity, Availability foundation | current |
| [[information-assurance]] | CIA triad + authentication, non-repudiation, resilience, safety | current |

### L02 — Attack Landscape
| Page | Summary | Status |
|------|---------|--------|
| [[iot-attack-taxonomy]] | 9 categories of IoT attacks with examples | current |
| [[mirai-botnet]] | 2016 botnet exploiting default passwords for DDoS | current |
| [[krack-attack]] | 2017 Key Reinstallation Attack against WPA2 | current |
| [[zigbee-pairing-vulnerability]] | Sniffing network keys during ZigBee pairing | current |

### L03 — Threat Modelling & Secure Design
| Page | Summary | Status |
|------|---------|--------|
| [[threat-modeling]] | Process of identifying assets, threats, probability ratings | current |
| [[security-by-design]] | Integrating security from the start of system design | current |
| [[attack-tree]] | Structured diagram modeling attacker paths to a goal | current |
| [[fault-tree]] | Structured diagram modeling failure paths to hazardous state | current |
| [[devops-security]] | Blending development, QA, and operations for security | current |
| [[operational-security-lifecycle]] | Define, implement, operate, dispose phases | current |
| [[attack-surface-analysis]] | Miessler's 15 attack surface classes for IoT | current |

### L04 — Hardware Security & Compliance
| Page | Summary | Status |
|------|---------|--------|
| [[physical-unclonable-functions]] | Hardware security primitives using manufacturing variations | current |
| [[trusted-platform-module]] | Dedicated security hardware for crypto and key storage | current |
| [[secure-development-lifecycle]] | Security from scratch in system development framework | current |
| [[iot-2.0]] | Next-gen IoT with 5G/6G, AI, edge computing, blockchain | current |
| [[iot-compliance-frameworks]] | ENISA, DHS, FDA, US IoT Cybersecurity Improvement Act | current |
| [[resilience-iot]] | Anticipate, withstand, recover, evolve framework | current |

### L05 — Operational & Attack Surface Deep-Dive
| Page | Summary | Status |
|------|---------|--------|
| [[ota-updates]] | Over-the-air firmware update security requirements | current |
| [[iot-firewalling]] | Packet filtering for resource-constrained IoT devices | current |
| [[device-memory-attack-surface]] | Cleartext credentials and keys in device memory | current |
| [[physical-interface-attack-surface]] | JTAG, firmware extraction, privilege escalation via physical access | current |
| [[firmware-security]] | Hardcoded passwords, sensitive URLs, encryption keys in firmware | current |
| [[web-interface-vulnerabilities]] | SQL injection, XSS, weak passwords in IoT web UIs | current |
| [[ecosystem-communications-security]] | Health checks, heartbeats, decommissioning exploitation | current |

### L06 — Cryptography and Lightweight Security Primitives
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-6]] | Cryptography (symmetric, asymmetric, hash, MAC, sig) + PUFs, TPMs, TRNGs, ASCON | current |
| [[symmetric-encryption]] | AES, DES, Blowfish, Twofish, CAST-128, Camellia, IDEA; modes (ECB, CBC, GCM, CCM) | current |
| [[asymmetric-encryption]] | RSA + ECC; PKCS#1/OAEP padding; quantum-broken; X25519/Ed25519 | current |
| [[hashing]] | SHA-256, SHA-3, MD5/SHA-1 broken; HMAC construction; pre-image/collision resistance | current |
| [[message-authentication-code]] | HMAC-SHA256, CMAC, GMAC; integrity+authentication, no non-repudiation | current |
| [[random-number-generator]] | TRNG vs PRNG vs DRBG; memory-based TRNGs; von Neumann correction | current |
| [[aes]] | FIPS 197; 128-bit blocks, 128/192/256-bit keys, 10/12/14 rounds | current |
| [[hmac]] | RFC 2104; H(k⊕opad ‖ H(k⊕ipad ‖ m)); defeats length extension | current |
| [[ascon]] | NIST lightweight crypto winner (Feb 2023); 320-bit permutation, AEAD + hash | current |
| [[lightweight-cryptography]] | NIST process 2015–2023; PRESENT, GIFT, ChaCha20, ASCON for constrained IoT | current |
| [[dolev-yao-attacker-model]] | Standard cryptographic adversary: controls network, cannot break primitives | current |
| [[iot-2-0]] | Next-gen IoT with 5G/6G, AI/ML, edge computing, blockchain, Industry 4.0 | current |

### L07 — Identity Lifecycle & Privacy
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-7]] | IAM, bootstrapping, PKI, OAuth 2.0, privacy by design, GDPR | current |
| [[iot-identity-lifecycle]] | Device identity from bootstrapping through deactivation | current |
| [[iot-privacy-concerns]] | Pervasive sensing, metadata leakage, complex data sharing chains | current |
| [[iot-applications]] | Smart home, IIoT, healthcare, transportation, smart grid, space — use cases | current |

### 📄 IoT Security Papers (3 ingested)
| Page | Summary | Status |
|------|---------|--------|
| [[paper-iot-lightweight-hardware-architecture]] | Mexis et al. 2021 (JETC): DRAM PUF + HMAC-SHA-256 + AES-128-CBC + MQTT for SoS | current |
| [[paper-iot-mexis-2021-poster]] | Mexis et al. 2021 (SIGCOMM poster): same architecture, demonstrator focus | current |
| [[paper-zhou-iot-2-0]] | Zhou et al. 2021 (IEEE Access): IoT 2.0 across 7 dimensions; 6→8 layer architecture | current |

### 🗺️ IoT Security Topics
| Page | Summary | Status |
|------|---------|--------|
| [[iot-security-landscape]] | Overview tying all 5 IoT Security lectures together | current |
| [[iot-common-attacks]] | 9 attack categories: scanning, protocol, eavesdropping, crypto, spoofing, OS/app, DoS, physical, access control | current |
| [[digital-signatures]] | Cryptographic mechanism for authentication, integrity, non-repudiation (hash→sign→verify) | current |
| [[iot-secure-design]] | 8 secure design goals + best practices for IoT | current |
| [[iot-attack-surfaces]] | Miessler's 15 attack surface classes from DefCon 2023 | current |
| [[iot-security-hardware]] | PUFs, TPMs, security co-processors overview | current |
| [[sensors]] | IoT sensor categories, spoofing attacks, sensor fusion | current |
| [[actuators]] | Motors, valves, solenoids — the "doing" part of IoT | current |
| [[authentication]] | Identity verification: passwords, certificates, biometrics, MFA | current |
| [[non-repudiation]] | Cannot deny having performed an action, digital signatures | current |

---

## 📚 Microelectronics (~45 pages)

### L01 — Semiconductor Basics
| Page | Summary | Status |
|------|---------|--------|
| [[electronics]] | Field manipulating electrons and charged particles | current |
| [[microelectronics]] | Sub-micrometre electronic components using semiconductors | current |
| [[nanoelectronics]] | Electronics exploiting quantum mechanical properties | current |
| [[semiconductor]] | Medium resistivity material with controllable conduction | current |
| [[silicon]] | Dominant semiconductor: abundant, forms SiO₂, 4 valence electrons | current |
| [[bandgap]] | Energy gap between valence and conduction bands | current |
| [[valence-band]] | Energy levels of outermost non-excited electrons | current |
| [[conduction-band]] | Energy levels of excited/freed electrons | current |
| [[intrinsic-semiconductor]] | Pure semiconductor material with no added impurities | current |
| [[electron-hole]] | Quasiparticle: absence of electron in valence band, acts as positive charge carrier | current |

### L02 — Doping & Extrinsic Semiconductors
| Page | Summary | Status |
|------|---------|--------|
| [[doping]] | Adding impurities to modify semiconductor electrical properties | current |
| [[n-type-semiconductor]] | Doped with electron donors (P, As), electron majority carriers | current |
| [[p-type-semiconductor]] | Doped with electron acceptors (B), hole majority carriers | current |
| [[ion-implantation]] | Accelerated ion doping method, precise but needs annealing | current |
| [[thermal-diffusion]] | Heat-based doping, primary method until 1960s | current |
| [[photolithography]] | Pattern transfer masking for selective doping/etching | current |

### L03 — The P-N Junction
| Page | Summary | Status |
|------|---------|--------|
| [[p-n-junction]] | N-type and p-type contact, depletion region, diode behavior | current |
| [[depletion-region]] | Charge carrier depletion at p-n junction contact | current |
| [[diode]] | Two-terminal device, unidirectional current from p-n junction | current |

### Lecture Topic Pages
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-1]] | L01: Semiconductor Physics | current |
| [[microelectronics-lecture-2]] | L02: Doping and Extrinsic Semiconductors | current |
| [[microelectronics-lecture-3]] | L03: P-N Junction Overview | current |
| [[microelectronics-lecture-4]] | L04: Diode Applications — rectifiers, limiters, clampers | current |
| [[microelectronics-lecture-5]] | L05: MOS Transistors — MOSFET structure and operation | current |
| [[microelectronics-lecture-6]] | L06: CMOS Logic Gates and Digital Circuits | current |
