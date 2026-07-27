# second-brain — Master Index

> Maintained by Professor White. Updated after every INGEST and significant QUERY.

**Last updated:** 2026-07-20
**Total pages:** 657 (vault + study; excluding raw/)
**Active courses:** 6

---

## Exam Calendar
| Course                               | Exam Date    | Days Left | Progress                                                        |
| ------------------------------------ | ------------ | --------- | --------------------------------------------------------------- |
| [[multimedia-databases]]             | 21 July 2026 | ~13       | **9/9 lectures ✅** + Ex01–Ex09 practice complete ✅ (100+ pages) |
| [[network-science]]                  | 28 July 2026 | ~20       | **9/9 lectures ✅** + Ex01–Ex08 (139 pages)                      |
| [[reproducibility-engineering]]      | 30 July 2026 | ~22       | **10/10 lectures ✅** + Sheet 1–10 (80+ pages)                   |
| [[software-analyse]]                 | 31 July 2026 | ~23       | **11/11 lectures ✅** (100+ pages)                               |
| [[iot-security]]                     | 05 Aug 2026  | ~27       | **9/9 lectures ✅** (~80 pages) + 3 papers ingested              |
| [[introduction-to-microelectronics]] | 06 Aug 2026  | ~28       | **9/9 lectures ✅** (~65 pages)                                  |

---

## 📚 Multimedia Databases (95 pages)

### L01 — Introduction
| Page                                     | Summary                                              | Status  |
| ---------------------------------------- | ---------------------------------------------------- | ------- |
| [[multimedia-definition]]                | MHEG classification, strict vs loose multimedia      | current |
| [[media-types-discrete-continuous]]      | Discrete (text, images) vs continuous (audio, video) | current |
| [[multimedia-system]]                    | Herrtwich/Steinmetz definition                       | current |
| [[data-streams]]                         | Async/sync/isochronous, FBR vs VBR                   | current |
| [[multimedia-database-intro]]            | MMDBMS = DBMS + IR                                   | current |
| [[structured-vs-unstructured-retrieval]] | DBMS vs IR, object-relational unifier                | current |
| [[multimedia-query-predicates]]          | Attribute, structure, spatial, semantic              | current |

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

### L07 — Content-Based Image Retrieval
| Page | Summary | Status |
|------|---------|--------|
| [[multimedia-databases-lecture-07]] | L07 topic: CBIR pipeline, QBE/QBF, histograms, distance metrics, DL, evaluation | current |
| [[query-by-example-and-feature]] | QBE (sample image) vs QBF (feature values), interactive query loop | current |
| [[cbir-systems-evaluation]] | Precision, recall, MAP, F-measure, IoU, TRECVID benchmarks | current |

### L08 — Query Languages
| Page | Summary | Status |
|------|---------|--------|
| [[multimedia-databases-lecture-08]] | L08 topic: MMQL history, MOQL/OQL, SQL/MM, MPQF, result presentation, query processing | current |
| [[multimedia-query-languages]] | MMQL overview: history, categories, query types, requirements | current |
| [[moql]] | Multimedia Object Query Language: OQL extension with spatial/temporal predicates | current |
| [[oql]] | Object Query Language: ODMG model, SQL-92 with OO extensions | current |
| [[nested-tables-vs-varrays]] | Oracle collection types: VARRAY (bounded, ordered) vs nested table (unbounded, SQL-queryable) | current |

### L09 — Indexing & Access Structures
| Page | Summary | Status |
|------|---------|--------|
| [[multimedia-databases-lecture-09]] | L09 topic: signature vectors, dimensionality reduction, R-tree family, SR-tree, LSH, GiST | current |
| [[signature-vectors]] | Low-level features as vectors for content-based indexing | current |
| [[dimensionality-reduction]] | Transformations (KLT, FFT, DCT, Wavelet) + space-filling curves (Hilbert, Z-Order) | current |
| [[r-tree]] | R-tree family: R+, R*, SS, SR, TV, X-tree for multidimensional indexing | current |
| [[sr-tree]] | Sphere/Rectangle-tree: intersection of bounding boxes, MINDIST/MINMAXDIST pruning | current |
| [[locality-sensitive-hashing]] | LSH: hash similar items to same bucket for approximate NN search | current |
| [[gist-framework]] | Generalized Search Tree: template index structure for ORDBMS | current |
| [[quadtree-and-kd-tree]] | Main memory spatial structures: quadtree splits, kd-tree one-dimensional splits | current |


| [[multimedia-databases-lecture-01]] | Lecture 01 establishes the foundations: what multimedia is, how media types are  | current |
| [[multimedia-databases-lecture-02]] | Lecture 2 covers how humans perceive color and the mathematical models (RGB, CMY | current |
| [[multimedia-databases-lecture-03]] |  | current |
| [[multimedia-databases-lecture-04]] |  | current |
| [[multimedia-databases-lecture-05]] |  | current |
| [[multimedia-databases-lecture-06]] | Lecture 06 covers multimedia data modeling — how to annotate, describe, and stru | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[audio-quantization-pcm]] | Quantization in audio is the process of mapping continuous amplitude values to a | current |
| [[classification-schemes]] | Classification Schemes (CS) in MPEG-7 are standardized taxonomies that provide c | current |
| [[color-histogram]] | A colour histogram is a feature vector that counts how many pixels of an image ( | current |
| [[color-lookup-table]] | A Color Lookup Table (CLUT) maps small pixel indices to full-color values, enabl | current |
| [[color-space-conversion-ycbcr]] | Color space conversion from RGB to YCbCr separates luminance (brightness) from c | current |
| [[dominant-color]] | Dominant colour is a compact representation of the most prominent colours in an  | current |
| [[hmmd-color-space]] | HMMD (Hue-Max-Min-Diff) is a color space designed to be closer to perceptual uni | current |
| [[image-interpolation]] | Image interpolation computes new pixel values when scaling images, using methods | current |
| [[image-point-operations]] | Image point operations transform each pixel independently based on its value (br | current |
| [[image-resolution-dpi-ppi]] | Image resolution measures how accurately a device or system approximates an imag | current |
| [[jpeg2000-wavelet-compression]] | JPEG2000 replaces the DCT with Discrete Wavelet Transform (DWT), enabling both l | current |
| [[mpeg-7-ddl]] | The Description Definition Language (DDL) is the XML-Schema-based language that  | current |
| [[mpeg-7-indexing-pyramid]] | The MPEG-7 Indexing Pyramid is a 10-level framework for visual indexing that spa | current |
| [[mpeg-7-semantic-description]] | MPEG-7 semantic description tools enable the representation of meaning — events, | current |
| [[mpeg-7-structural-description]] | MPEG-7 structural description tools enable spatial, temporal, spatio-temporal, a | current |
| [[multimedia-annotation]] | Multimedia annotation is the task of associating textual labels or tags to multi | current |
| [[multimedia-main-domains]] | Steinmetz's layered model organizes multimedia into four domains — Basics (encod | current |
| [[multimedia-metadata]] | Multimedia metadata is structured information that describes, explains, or locat | current |
| [[relevance-feedback]] | Relevance feedback is an iterative retrieval technique where the user marks resu | current |
| [[spatial-coherency]] | Spatial coherency is the property that neighbouring pixels in a natural image te | current |
| [[video-hierarchy-shots-scenes]] | Digital video is hierarchically structured from frames (atomic units) through sh | current |
| [[video-summarization-key-frames]] | Video summarization creates a concise overview of video content using key frames | current |
| [[xml-structured-text]] | XML (Extensible Markup Language) is a platform-independent, ==self-describing ma | current |

### Practice & Flashcards
| Page | Summary | Status |
| [[reproducibility-engineering-sheet-10]] | Exercise Sheet 10: Docker secrets, LLM reproducibility (temperature/seed), structured outputs | current |
| [[reproducibility-engineering-sheet-11]] | Exercise Sheet 11: multi-stage Docker builds, remote experiment workflows, HDF5 storage | current |
| [[repeng-prof-ic11]] | In-Class Exercise 11: FAIR principles, legal frameworks (copyright, GDPR, trade secrets, sui generis) | current |
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
| [[mmdb-ex09]] | Exercise sheet 9: indexing (B-tree, hash, R-tree, search algorithms) | current |
| [[multimedia-databases-cheat-sheet]] | **Condensed one-page cheat sheet: all formulas, definitions, algorithms from Ex01–Ex09** | current |
| [[mmdb-exam-prediction]] | Exam prediction: 11 archetypes, top-3 targets | current |
| | [[mmdb-exam-simulation-ss25]] | Answer each sub-question with exactly one choice. | current |


---

## 📚 Network Science (139 pages)

### L01 — Introduction
| Page | Summary | Status |
|------|---------|--------|
| [[network-intro]] | Nodes + edges, lossy abstraction | current |
| [[edge-types]] | Directed, undirected, weighted | current |
| [[centrality]] | Degree, closeness, betweenness | current |
| [[network-diffusion]] | SI/SIS/SIR models, R0 | current |
| [[community-structure]] | Dense clusters, modularity | current |

### L02 — Graph Theory
| Page                            | Summary                          | Status  |
| ------------------------------- | -------------------------------- | ------- |
| [[graph-fundamentals]]          | G=(V,E), modeling choices        | current |
| [[graph-representations]]       | Edge list, adjacency list/matrix | current |
| [[neighbourhood-and-degree]]    | N(v), deg(v), handshaking lemma  | current |
| [[paths-walks-and-cycles]]      | Walk → path → cycle hierarchy    | current |
| [[shortest-path-and-diameter]]  | dist(u,v), diam(G)               | current |
| [[eulerian-path-and-circuit]]   | Königsberg, degree parity        | current |
| [[breadth-first-search]]        | BFS, FIFO, O(\|V\|+\|E\|)        | current |
| [[depth-first-search]]          | DFS, LIFO, cycle detection       | current |
| [[dijkstras-algorithm]]         | Weighted shortest paths          | current |
| [[connectivity-and-components]] | Connected, giant component       | current |

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
| [[small-world-property]] | d̄ ∝ log\|V\| | current |
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



| [[network-science-l01]] | Lecture 1 introduces what networks are, why they matter, and what we can analyze | current |
| [[network-science-l02]] |  | current |
| [[network-science-l03]] | Social ties come in strong and weak varieties; triadic closure shapes how they f | current |
| [[network-science-l04]] | Graph communities are dense subsets with few external links; finding them requir | current |
| [[network-science-l05]] | Lecture 05 adds attributes and context to the graph: nodes carry properties, tie | current |
| [[network-science-l06]] | Lecture 06 adds signs to edges — positive for alliance, negative for rivalry — a | current |
| [[network-science-l07]] | Lecture 07 explains why large networks have short paths (logarithmic distances), | current |
| [[network-science-l08]] | Network dynamics studies how processes (diseases, rumors, behaviors) spread on n | current |
| [[network-science-l09]] | L09 shows how to map every node to a vector in R^d preserving graph structure —  | current |

### Additional Concepts
| Page                                    | Summary                                                                                                   | Status  |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------- |
| [[adjacency-matrix-factorization]]      | A unifying view: spectral embeddings, DeepWalk, and node2vec all implicitly fact                          | current |
| [[algebraic-connectivity]]              | Algebraic connectivity (λ₂) is the second-smallest eigenvalue of the [[graph-laplacian|graph Laplacian]] | current |
| [[betweenness-centrality]]              | Betweenness centrality measures how often a node sits on shortest paths between                           | current |
| [[bipartite-graphs]]                    | A bipartite graph has two disjoint node sets where edges only connect nodes acro                          | current |
| [[centrality-measures]]                 | Centrality measures quantify node importance — but each measure encodes a differ                          | current |
| [[closeness-centrality]]                | Closeness centrality measures how near a node is to all other nodes on average —                          | current |
| [[community-detection]]                 | Community detection partitions a graph into groups of nodes that are densely con                          | current |
| [[community-detection-overview]]        | Community detection finds subsets of nodes with dense internal connections and s                          | current |
| [[conductance]]                         | Conductance measures the fraction of edges that leave a community relative to it                          | current |
| [[configuration-model]]                 | The configuration model generates random graphs with a prescribed degree sequenc                          | current |
| [[connected-component]]                 | A connected component is a maximal set of nodes where every node can reach every                          | current |
| [[degree-centrality]]                   | Degree centrality measures the number of direct contacts a node has — the simple                          | current |
| [[diffusion-of-innovations]]            | Diffusion of innovations studies how new ideas, technologies, and behaviors spre                          | current |
| [[directed-and-undirected-graphs]]      | ==Undirected graphs model symmetric relationships (friendship)==, while directed                          | current |
| [[directed-connectivity]]               | In directed graphs, strong connectivity requires mutual reachability between all                          | current |
| [[edge-betweenness]]                    | Edge betweenness measures how often an edge lies on shortest paths between all p                          | current |
| [[eigenvector-centrality]]              | Eigenvector centrality measures recursive prestige — important nodes are connect                          | current |
| [[embeddedness]]                        | Embeddedness describes a node whose neighbors are themselves densely interconnec                          | current |
| [[embedding-based-community-detection]] | Embedding-based community detection uses node embeddings (from random walks or n                          | current |
| [[global-email-experiment]]             | ==Dodds, Muhamad & Watts (2003)== replicated Milgram's experiment using email ac                          | current |
| [[granovetter-weak-ties]]               | Granovetter's weak-tie hypothesis states that weak ties (acquaintances, not clos                          | current |
| [[graph-laplacian]]                     | The graph Laplacian L = D - A encodes the structure of a graph — its eigenvalues                          | current |
| [[graph-partitioning]]                  | Graph partitioning divides a graph into a fixed number of balanced clusters — un                          | current |
| [[harmonic-centrality]]                 | Harmonic centrality is the disconnected-graph extension of [[closeness-centrality|closeness centrality]] | current |
| [[hierarchical-clustering]]             | Divisive and agglomerative community detection methods produce dendrograms — tre                          | current |
| [[hnsw-indexing]]                       | HNSW is a graph-based approximate nearest-neighbor index that applies Kleinberg'                          | current |
| [[k-balance]]                           | k-balance is the partition structure guaranteed by weak structural balance: a co                          | current |
| [[kernighan-lin-algorithm]]             | Kernighan-Lin is a local-search algorithm for balanced graph partitioning — iter                          | current |
| [[laplacian-eigenmaps]]                 | Laplacian eigenmaps embed each node as a point in R^d using the eigenvectors of                           | current |
| [[maxstc-complexity]]                   | Finding the edge labeling with the most strong edges that satisfies Strong Triad                          | current |
| [[message-passing-framework]]           | The message-passing framework defines how GNNs compute node embeddings: each lay                          | current |
| [[min-cut-max-flow]]                    | Min-cut / Max-flow finds the smallest set of edges whose removal disconnects two                          | current |
| [[modularity-resolution-limit]]         | The resolution limit is a fundamental limitation of [[modularity]] — it cannot d                          | current |
| [[neighborhood-overlap]]                | Neighborhood overlap measures the fraction of neighbors shared by two connected                           | current |
| [[network-autocorrelation]]             | Network autocorrelation is the statistical tendency for connected nodes to share                          | current |
| [[network-effects]]                     | The structure of connections creates outcomes — visibility, influence, lock-in,                           | current |
| [[network-examples]]                    | Networks appear across every domain — social, communication, information, econom                          | current |
| [[normalized-cut]]                      | Normalized cut balances the size of a cut against the total degree (volume) of t                          | current |
| [[online-link-formation]]               | Online data with timestamps turns link formation into a measurable process — emp                          | current |
| [[pagerank]]                            | PageRank extends [[eigenvector-centrality]] with a damping factor — a random sur                          | current |
| [[power-law-distribution]]              | A power-law distribution is a heavy-tailed distribution where a few nodes have v                          | current |
| [[process-structure-interaction-gap]]   | The process-structure interaction gap is the sixth gap in the course: the same n                          | current |
| [[product-space-network]]               | The product space network connects exported products that require similar capabi                          | current |
| [[random-walks]]                        | A random walk on a graph is a stochastic process where a walker moves from node                           | current |
| [[signed-laplacian]]                    | The signed Laplacian L_σ = D − A_σ extends the standard graph Laplacian to signe                          | current |
| [[sparse-dense-and-random-graphs]]      | Graphs differ quantitatively in edge density — from sparse (few edges) to dense                           | current |
| [[spectral-clustering-embeddings]]      | Spectral clustering is k-means applied to Laplacian eigenmaps — nodes in the sam                          | current |
| [[spectral-partitioning]]               | Spectral partitioning uses the eigenvectors of the graph Laplacian to find a nat                          | current |
| [[strong-triadic-closure]]              | If a node has two strong ties, Strong Triadic Closure requires those endpoints t                          | current |
| [[structural-holes-and-brokerage]]      | Structural holes are missing connections between groups; brokers who span them g                          | current |
| [[temporal-networks]]                   | Temporal networks assign activation times to edges, revealing that static aggreg                          | current |
| [[weak-tie-paradox-contagion]]          | The same weak ties and bridges that accelerate simple contagion (rumors, disease                          | current |
| [[web-bow-tie-structure]]               | Broder et al. (2000) found that the Web decomposes into a bow-tie: a strongly co                          | current |
| [[weighted-graphs]]                     | ==A weighted graph assigns a numerical value w(e) to each edge, encoding strengt                          | current |
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
| [[network-science-e08]] | Exercise sheet 8: small-world networks (solutions) | current |
| [[network-science-e01-flashcards]] | Flashcards for E01 | current |
| [[network-science-e02-flashcards]] | Flashcards for E02 | current |
| [[network-science-e03-flashcards]] | Flashcards for E03 | current |
| [[network-science-e04-flashcards]] | Flashcards for E04 | current |
| [[network-science-e05-flashcards]] | Flashcards for E05 | current |
| [[network-science-e06-flashcards]] | Flashcards for E06 | current |
| [[network-science-e07-flashcards]] | Flashcards for E07 | current |

### Exam Prep
|| Page | Summary | Status |
|------|---------|--------|
| [[network-science-exercise-prep]] | Exercise-based exam prep: NetworkX functions, hand calculations, key formulas | current |
| [[exam-prep-network-science-2026-07-28]] | 752-line comprehensive prep: structured questions with equations, 9 open questions, quick-fire recall, priority queue | current |
| [[network-science-exam-battle-plan]] | Day-by-day battle schedule Jul 20-27, coverage map, Professor White mock exam | current |
| [[network-science-cheatsheet]] | Condensed cheatsheet: all formulas, definitions, algorithms from L01-L08 | current |
| [[mock-exam-network-science-2026-07-26]] | Mock exam: 50% Antwort-Wahl-Verfahren (46 Q) + 50% essay (5 Q), solutions in callouts | current |
| [[mock-exam-network-science-2026-07-27]] | Mock exam 2: 48 MCQ + 5 essay, emphasises spectral methods, ER thresholds, SIS, temporal networks, homophily index r | current |

---

## 📚 Reproducibility Engineering (61 pages)

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
| [[multi-stage-docker-build]] | Separate build and runtime stages; ship only the artifact | current |
| [[fair-data-principles]] | FAIR: Findable, Accessible, Interoperable, Reusable -- machine-actionable data | current |
| [[legal-frameworks-research-data]] | Copyright, GDPR, trade secrets, sui generis -- layered legal protection for databases | current |
| [[sui-generis-database-right]] | EU database right protecting substantial investment in data compilation | current |
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

### L09 — LLMs and Reproducibility
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-lecture-9]] | LLMs and reproducibility: local vs remote, structured outputs, constrained decoding, JSON Schema | current |

### L10 — Remote Experiments
| Page | Summary | Status |
|------|---------|--------|
| [[reproducibility-engineering-lecture-10]] | Remote experiment workflows, artifact packaging, SQPolite case study | current |
| [[artifact-packaging]] | Packaging research artifacts for reproducibility: fork+patches, Docker, doall.sh | current |

| [[reproducibility-engineering-lecture-1]] | Lecture 1 establishes the foundational vocabulary (repeat/reproduce/replicate),  | current |
| [[reproducibility-engineering-lecture-2]] |  | current |
| [[reproducibility-engineering-lecture-3]] | How to formulate testable research hypotheses and structure experiments for repr | current |
| [[reproducibility-engineering-lecture-4]] | Lecture 4 covers Git as the fundamental tool for version control and reproducibi | current |
| [[reproducibility-engineering-lecture-5]] | Lecture 5 introduces reproducible builds through hands-on C programming exercise | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[build-environment-isolation]] | Build environment isolation ensures that builds depend only on explicitly declar | current |
| [[computational-reproducibility-in-ml]] | Machine learning experiments face unique reproducibility challenges -- stochasti | current |
| [[confidence-intervals]] | A confidence interval gives a range of plausible values for a parameter, providi | current |
| [[data-provenance]] | Data provenance is the documented lineage of data -- where it came from, how it  | current |
| [[docker-compose]] | Docker Compose is a tool for declaring and running multi-container Docker applic | current |
| [[git-patches-and-diffs]] | A patch (diff) is a structured text representation of changes between two snapsh | current |
| [[git-rebasing-and-history-rewriting]] | Rebasing replays commits onto a new base to create a linear history; interactive | current |
| [[gitignore-and-gitattributes]] | `.gitignore` tells Git which files to exclude from tracking; `.gitattributes` co | current |
| [[levels-of-equivalence]] | When comparing computational experiments, different levels of equivalence define | current |
| [[package-manager-reproducibility]] | Package manager reproducibility ensures that dependency resolution always produc | current |
| [[presenting-experiments]] | A well-structured experiments section separates setup, results, and discussion,  | current |
| [[reprotest]] | ReproTest is a tool that builds a program twice in different simulated environme | current |
| [[research-artifacts]] | The tangible outputs of research—source code, datasets, scripts, configurations, | current |
| [[sqlite-architecture]] | SQLite is a serverless, file-based, single-library database management system —  | current |
| [[vistrails]] | VisTrails is a scientific workflow management system that provides integrated pr | current |
### Practice & Flashcards
| Page | Summary | Status |
| Page | Summary | Status |
| [[repeng-prof-ic01]] | Based on the Nature article on "Reproducibility Crisis" and ACM "Artifact Review | current |
| [[repeng-prof-ic02]] | Based on the VisTrails article and Heil et al. "Reproducibility standards for ma | current |
| [[repeng-prof-ic03]] | Based on Justin Zobel's "Writing for Computer Science". | current |
| [[repeng-prof-ic04]] | Norm committed incomplete/broken code (work-in-progress) and then committed the  | current |
| [[repeng-prof-ic05]] | Reassembled code: | current |
| [[repeng-prof-ic06]] | - User Application → DB Client Library → Network → RDBMS Server | current |
| [[repeng-prof-ic07]] | Based on Hadley Wickham's "Tidy Data" and SQL for Data Science. | current |
| [[repeng-prof-ic08]] | | Feature       | Relational        | XML               | JSON              | | current |
| [[repeng-prof-ic09]] | | Criterion                | Local LLM inside container | Remote API             | current |
| [[repeng-prof-ic10]] | Based on "Nullius in Verba" by Mauerer & Scherzinger, ICDE 2021. | current |
| [[reproducibility-engineering-sheet-1]] | Lab Sessions: April 23/24, 2026 | current |
| [[reproducibility-engineering-sheet-2]] | Lab Sessions: April 30 / May 8, 2026 | current |
| [[reproducibility-engineering-sheet-3]] | Lab Sessions: May 7/15, 2026 | current |
| [[reproducibility-engineering-sheet-4]] | Lab Sessions: May 21/22, 2026 | current |
| [[reproducibility-engineering-sheet-5]] | Lab Sessions: May 28/29, 2026 | current |
| [[reproducibility-engineering-sheet-6]] | 2.2 Comparing different Compilers | current |
| [[reproducibility-engineering-sheet-7]] | The task is to compare the performance of an embedded DBMS (sqlite-architecture) | current |
| [[reproducibility-engineering-sheet-8]] | The table  has columns , , ,  with rows like  and . | current |
| [[reproducibility-engineering-sheet-9]] | -  pretty-prints JSON.  produces compact output.  sorts keys for reliable compar | current |
| Page | Summary | Status |
| [[reproducibility-engineering-sheet-1-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-1 | current |
| [[reproducibility-engineering-sheet-2-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-2 | current |
| [[reproducibility-engineering-sheet-3-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-3 | current |
| [[reproducibility-engineering-sheet-4-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-4 | current |
| [[reproducibility-engineering-sheet-5-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-5 | current |
| [[reproducibility-engineering-sheet-6-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-5 | current |
| [[reproducibility-engineering-sheet-7-flashcards]] | - Lecture topic: reproducibility-engineering-lecture-6 | current |


## 📚 Introduction to Microelectronics (65 pages)

### L01 — Semiconductors
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-1]] | Semiconductors are materials whose electrical conductivity lies between conductors and insulators, d | current |

### L02 — Doping
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-2]] | doping is the deliberate introduction of impurity atoms into a semiconductor crystal to control its  | current |

### L03 — P-N Junctions
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-3]] | A p-n-junction forms when p-type and n-type semiconductor regions meet, creating a built-in electric | current |

### L04 — Diode Circuits
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-4]] | diode circuits are used for rectifier (AC to DC), signal shaping via limiter-circuit and clamper-cir | current |

### L05 — MOSFETs
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-5]] | The mosfet (Metal-Oxide-Semiconductor Field-Effect Transistor) uses a gate-controlled electric field | current |

### L06 — CMOS
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-6]] | CMOS (Complementary MOS) combines an nmos-transistor pull-down network and a pmos-transistor pull-up | current |

### L07 — CMOS Applications
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-7]] | CMOS circuits can store bits (memory) and amplify signals (analog), not just compute logic. | draft |

### L08 — OpAmps
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-8]] | Two OpAmp circuits (inverting and non-inverting) set their gain using external resistors, thanks to  | draft |

### L09 — Integrators, Differentiators & Memories
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-9]] | By swapping resistors for capacitors in OpAmp feedback networks you get integrators and differentiat | draft |
| [[opamp-integrator]] | Replace the feedback resistor with a capacitor, and the OpAmp outputs the integral of the input sign | current |
| [[opamp-differentiator]] | Replace the input resistor with a capacitor, and the OpAmp outputs the derivative of the input signa | current |
| [[weighted-summer]] | Multiple input signals, each with its own resistor, are summed by the OpAmp into a single output. | current |
| [[voltage-follower]] | The output follows the input exactly — no amplification, no inversion — but it isolates the source f | current |
| [[sram-cell]] | Six transistors form a bistable latch that holds one bit as long as power is supplied — fast but lar | current |
| [[dram-cell]] | One transistor and one capacitor store a bit as charge — tiny, dense, but the charge leaks and needs | current |
| [[sense-amplifier]] | A sense amplifier detects the tiny voltage difference on a memory's bit lines and amplifies it to fu | current |
| [[flash-memory]] | A floating gate traps electrons to store data permanently — no power needed, but writes wear out the | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[analog-amplifier]] | A circuit that increases the amplitude of an analog signal using active components like transistors  | current |
| [[avalanche-breakdown]] | Avalanche breakdown is a carrier multiplication mechanism that occurs at high reverse voltages, wher | current |
| [[band-theory]] | Band theory explains how electrons in solids occupy continuous ranges of allowed energies (bands) se | current |
| [[bandgap]] | The bandgap is the energy difference between the valence band and conduction band that determines wh | current |
| [[bridge-rectifier]] | A full-wave rectifier using four diodes in a bridge configuration that eliminates the need for a cen | current |
| [[capacitor]] | A capacitor is a two-terminal component that stores energy in an electric field between two conducti | current |
| [[clamper-circuit]] | A clamper (DC restorer) shifts the DC level of a signal without changing its waveform shape, using a | current |
| [[cmos-inverter]] | The fundamental building block of CMOS digital circuits: an NMOS and PMOS transistor that switch com | current |
| [[cmos-logic-gates]] | The CMOS logic family builds every Boolean function as a complementary pair of networks: an nMOS pul | current |
| [[cmos-nand-gate]] | A CMOS NAND gate uses two nMOS in series (pull-down) and two pMOS in parallel (pull-up) to compute ¬ | current |
| [[cmos-nor-gate]] | A CMOS NOR gate uses two nMOS in parallel (pull-down) and two pMOS in series (pull-up) to compute ¬( | current |
| [[cmos-xor-gate]] | The XOR function (A ⊕ B = AB̄ + ĀB) cannot be implemented in a single stage of static complementary  | current |
| [[common-source-amplifier]] | A MOSFET amplifier configuration where the source is grounded, providing voltage gain with 180° phas | current |
| [[conduction-band]] | The conduction band is the energy band above the valence band where excited electrons become free to | current |
| [[conductor]] | A material with high electrical conductivity due to free charge carriers (typically electrons) that  | current |
| [[depletion-region]] | The depletion region is the charge-carrier-free zone at a p-n junction where electrons and holes hav | current |
| [[digital-circuit-design]] | Digital circuit design is the art of combining MOS transistors into logic gates, and logic gates int | current |
| [[digital-logic]] | The representation and manipulation of information using discrete voltage levels (HIGH/LOW) through  | current |
| [[diode]] | A diode is a two-terminal semiconductor device based on a p-n junction that allows current to flow p | current |
| [[diode-applications]] | Diodes are one-way valves for current — by combining them with resistors and capacitors, you can con | current |
| [[doping]] | Doping is the process of intentionally introducing impurity atoms into a semiconductor to modify its | current |
| [[doping-and-extrinsic-semiconductors]] | Doping means adding tiny amounts of specific impurity atoms to silicon to create an excess of either | current |
| [[electricity]] | Electricity is the flow of electric charge (carried by electrons or holes), governed by fundamental  | current |
| [[electron-hole]] | A hole is the absence of an electron in the valence band that behaves like a positively charged part | current |
| [[electronics]] | Electronics is the scientific field concerned with manipulating electrons and other electrically cha | current |
| [[etching]] | The process of selectively removing material from a wafer surface using chemical or physical methods | current |
| [[full-wave-rectifier]] | A full-wave rectifier uses two or four diodes to pass both halves of the AC waveform, producing puls | current |
| [[germanium]] | Germanium was the first semiconductor used in transistors but was largely replaced by silicon due to | current |
| [[half-wave-rectifier]] | A half-wave rectifier uses a single diode to pass only one half of the AC waveform, producing pulsat | current |
| [[impedance-matching]] | Impedance matching means designing circuits so that a source can deliver maximum power to a load, or | current |
| [[insulator]] | A material with very low electrical conductivity due to a large bandgap that prevents free charge ca | current |
| [[intrinsic-semiconductor]] | An intrinsic semiconductor is a pure semiconductor material with no added impurities, where charge c | current |
| [[ion-implantation]] | Ion implantation is a doping technique that uses an electron gun to accelerate dopant ions to high e | current |
| [[limiter-circuit]] | A limiter clips the voltage waveform at a specified threshold, preventing it from exceeding a maximu | current |
| [[mask-alignment]] | The process of precisely positioning a photomask over a wafer so that new patterns align correctly w | current |
| [[microelectronics]] | Microelectronics is the subfield of electronics dealing with very small electronic components at the | current |
| [[mos-capacitor]] | The MOS capacitor is the fundamental structure beneath the MOSFET gate — a metal-oxide-semiconductor | current |
| [[mos-transistors]] | A MOSFET is a transistor where a voltage on a gate electrode controls current flow between two termi | current |
| [[mosfet]] | A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a voltage-controlled transistor wher | current |
| [[mosfet-operating-regions]] | MOSFETs operate in three distinct regions — Cutoff, Linear (Triode), and Saturation — determined by  | current |
| [[n-type-semiconductor]] | An n-type semiconductor is a semiconductor doped with electron donor atoms (P, As), creating an abun | current |
| [[nanoelectronics]] | Nanoelectronics is the subfield of electronics that exploits nanotechnology and quantum mechanical p | current |
| [[negative-feedback]] | Negative feedback takes a portion of the output signal and feeds it back to the input in opposite ph | current |
| [[nmos-transistor]] | An nMOS transistor has N-type source and drain regions in a P-type substrate, using electrons as cha | current |
| [[opamp-basics]] | An operational amplifier is a high-gain differential amplifier that, combined with negative feedback | current |
| [[p-n-junction]] | A p-n junction is the boundary formed when p-type and n-type semiconductors meet, creating a depleti | current |
| [[p-n-junction-overview]] | A p-n junction is where p-type and n-type semiconductors meet — the built-in electric field at this  | current |
| [[p-type-semiconductor]] | A p-type semiconductor is a semiconductor doped with electron acceptor atoms (B, Al), creating an ab | current |
| [[photolithography]] | Photolithography is the pattern-transfer process in semiconductor fabrication that uses light to sel | current |
| [[pmos-transistor]] | A pMOS transistor has P-type source and drain regions in an N-type substrate, using holes as charge  | current |
| [[pmtransistor]] | A pMOS transistor has P-type source and drain regions in an N-type substrate, using holes as charge  | current |
| [[power-supply]] | The source of electrical energy that powers electronic circuits, converting AC mains or battery volt | current |
| [[rectifier]] | A rectifier is a circuit that converts alternating current (AC) to direct current (DC) using diodes  | current |
| [[semiconductor]] | A semiconductor is a material with medium resistivity that can act as either a conductor or insulato | current |
| [[semiconductor-physics]] | Semiconductors are materials whose electrical conductivity falls between conductors and insulators,  | current |
| [[silicon]] | Silicon is the dominant semiconductor material in microelectronics due to its abundance, controllabl | current |
| [[thermal-diffusion]] | Thermal diffusion is a doping method where silicon wafers are heated in the presence of dopant vapor | current |
| [[threshold-voltage]] | The threshold voltage (VTH) is the minimum gate-to-source voltage required to create a conducting in | current |
| [[transistor]] | A transistor is a three-terminal semiconductor device that can amplify signals or act as a switch, f | current |
| [[valence-band]] | The valence band is the highest energy band occupied by electrons in a non-excited atom, representin | current |
| [[vlsi-design]] | VLSI (Very Large Scale Integration) is the discipline of designing chips with millions to billions o | current |
| [[zener-breakdown]] | Zener breakdown is a quantum mechanical tunnelling mechanism that occurs in heavily doped p-n juncti | current |
| [[zener-diode]] | A Zener diode is a heavily doped diode designed to operate reliably in the reverse breakdown region, | current |

---
## 📚 IoT Security (~80 pages)

### L01 — Introduction to IoT Security
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-1]] | A comprehensive overview of the IoT security domain spanning fundamentals, applications, information | current |

### L02 — Attack Taxonomy
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-2]] | A comprehensive taxonomy of attack types targeting IoT systems, organized into nine categories spann | current |

### L03 — Attack Surfaces
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-3]] | A systematic enumeration of IoT attack-surface-analysis based on Daniel Miessler's 15 attack surface | current |

### L04 — Secure Design
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-4]] | Design goals and best practices for building secure IoT systems, covering automated attack mitigatio | current |

### L05 — Hardware Security
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-5]] | Hardware-based security mechanisms for IoT devices, covering physical-unclonable-functions (PUFs) fo | current |

### L06 — Cryptography for IoT
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-6]] | Cryptography gives IoT devices the four basic security services — confidentiality (encryption), inte | current |

### L07 — Identity & Privacy
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-7]] | Identity lifecycle management (from device bootstrapping through deactivation) and privacy engineeri | current |

### L08 — Compliance & Monitoring
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-8]] | IoT security requires ongoing compliance monitoring, periodic risk assessments, and defence-in-depth | current |

### L09 — DRAM-PUF Protocol
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-9]] | A concrete IoT authentication protocol that uses DRAM retention decay as a Physical Unclonable Funct | current |

### Papers
| Page | Summary | Status |
|------|---------|--------|
| [[paper-iot-lightweight-hardware-architecture]] | Mexis, Anagnostopoulos, Chen, Bambach, Arul, Katzenbeisser (2021), "A Lightweight Architecture for H | current |
| [[paper-iot-mexis-2021-poster]] | Mexis, Anagnostopoulos, Chen, Bambach, Arul, Katzenbeisser (2021), "A Design for a Secure Network of | current |
| [[paper-zhou-iot-2-0]] | Zhou, Makhdoom, Shariati, Raza, Keshavarz, Lipman, Abolhasan, Jamalipour (2021), "Internet of Things | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[actuators]] | Actuators are IoT components that perform physical actions in response to commands — motors, valves, | current |
| [[aes]] | AES is the dominant symmetric block cipher, standardised as FIPS 197 in 2001 after winning the NIST  | current |
| [[ascon]] | ASCON is the algorithm family selected by NIST in February 2023 as the winner of the lightweight cry | current |
| [[asymmetric-encryption]] | Asymmetric encryption uses a public/private key pair — the public key encrypts, the private key decr | current |
| [[attack-surface-analysis]] | Daniel Miessler's 15 attack surface classes (DefCon 2023) provide a comprehensive framework for syst | current |
| [[attack-tree]] | An attack tree is a structured diagram modelling how an attacker could achieve a specific security g | current |
| [[authentication]] | Authentication is the process of verifying the identity of a user, device, or system — proving you a | current |
| [[availability]] | The assurance that systems and data are accessible to authorized users when needed, forming the 'A'  | current |
| [[ble-security]] | Bluetooth Low Energy (BLE) security covers the pairing modes, encryption mechanisms, and known vulne | current |
| [[cia-triad]] | The CIA Triad — Confidentiality, Integrity, Availability — is the foundational model of information  | current |
| [[coap-security]] | CoAP (Constrained Application Protocol) security covers DTLS for transport encryption, OSCORE for en | current |
| [[common-criteria]] | An international standard for evaluating the security properties of IT products through structured a | current |
| [[course]] | This course covers security solutions for the Internet of Things (IoT), spanning from foundational c | current |
| [[defense-in-depth]] | Defence-in-depth layers multiple defensive mechanisms so that if one layer fails, others remain — fo | current |
| [[denial-of-service]] | Attacks that make IoT devices or services unavailable to legitimate users, ranging from simple resou | current |
| [[device-memory-attack-surface]] | The device memory attack surface class covers sensitive data stored in IoT device memory — including | current |
| [[device-provisioning]] | Device provisioning is the process of giving each IoT device its unique identity, credentials, and i | current |
| [[devops-security]] | DevOps blends development, QA, and operations into rapid, collaborative delivery — and in IoT securi | current |
| [[digital-signatures]] | A digital signature is a cryptographic mechanism that proves a message was created by a specific sen | current |
| [[dolev-yao-attacker-model]] | The Dolev-Yao attacker model (1983) is the standard adversary model for cryptographic protocol analy | current |
| [[ecosystem-communications-security]] | Ecosystem communications security covers the attack surface of inter-component messaging in IoT ecos | current |
| [[etsi-en-303-645]] | A European standard defining 13 provisions for consumer IoT security, forming the basis for the EU C | current |
| [[fault-tree]] | A fault tree is a structured diagram modelling how system failures can lead to a hazardous state — u | current |
| [[fips-140-2]] | US government standard for validating the security of cryptographic modules in hardware and software | current |
| [[firmware-security]] | Firmware security covers vulnerabilities in IoT device firmware — including hardcoded passwords, sen | current |
| [[gdpr-compliance]] | GDPR is EU law governing personal data processing — for IoT, it mandates data minimization, purpose  | current |
| [[hashing]] | A cryptographic hash H maps arbitrary-length input to a fixed-length digest with three security prop | current |
| [[healthcare-iot-security]] | Healthcare IoT (IoMT) security covers connected medical devices — insulin pumps, pacemakers, patient | current |
| [[hmac]] | HMAC (Hash-based MAC, RFC 2104) is the standard construction for a message-authentication-code using | current |
| [[iec-62443]] | The international standard series for securing industrial automation and control systems (IACS), cov | current |
| [[industrial-iot-security]] | Industrial IoT (IIoT) security covers SCADA systems, PLCs, and operational technology networks where | current |
| [[information-assurance]] | Information Assurance extends the CIA Triad with Authentication, Non-repudiation, Resilience, and Sa | current |
| [[internet-of-things]] | The Internet of Things is a network of physical devices embedded with sensors, software, and connect | current |
| [[iot-2-0]] | IoT 2.0 is the next generation of the Internet of Things, integrating 5G/6G, machine learning, edge  | current |
| [[iot-2.0]] | IoT 2.0 is the next-generation IoT concept integrating 5G/6G connectivity, machine learning and AI,  | current |
| [[iot-applications]] | IoT applications span a wide range of domains — smart home, smart city, industrial automation, healt | current |
| [[iot-architecture]] | IoT architecture consists of three main segments — sensors/data aggregators, actuators/agents, and p | current |
| [[iot-attack-surfaces]] | Systematic enumeration of all points where an IoT system can be attacked, from physical interfaces t | current |
| [[iot-attack-taxonomy]] | IoT attacks span nine major categories — from scanning and eavesdropping to physical tampering and p | current |
| [[iot-common-attacks]] | A taxonomy of the most frequently observed attack types targeting IoT devices, networks, and ecosyst | current |
| [[iot-communication-protocols]] | IoT communication protocols — MQTT, CoAP, Zigbee, BLE, LoRaWAN, and Thread/Matter — are the language | current |
| [[iot-compliance-frameworks]] | IoT compliance frameworks — including the US IoT Cybersecurity Improvement Act, ENISA recommendation | current |
| [[iot-connectivity-protocols]] | IoT uses a huge diversity of connectivity solutions — Wi-Fi, LoRaWAN, Bluetooth, Ethernet, Serial, C | current |
| [[iot-data-lifecycle]] | The IoT data lifecycle — collection, transmission, storage, processing, and retention — defines wher | current |
| [[iot-device-fundamentals]] | IoT device fundamentals covers the hardware and software building blocks — microcontrollers, SBCs, R | current |
| [[iot-firewalling]] | IoT firewalling filters network traffic directed at resource-constrained IoT devices that cannot run | current |
| [[iot-identity-lifecycle]] | The cradle-to-grave management of device identities from bootstrapping through deactivation. | current |
| [[iot-network-architecture]] | IoT network architecture is the three-tier model — perception (devices), network (connectivity), and | current |
| [[iot-privacy-concerns]] | The unique privacy challenges posed by IoT's pervasive sensing, metadata leakage, and complex data s | current |
| [[iot-secure-design]] | Security-by-design principles and practices for building IoT systems that are resistant to attacks f | current |
| [[iot-security-exam-format]] | Written exam (60–90 min) with three question types: definitions, use-case scenarios, and security so | current |
| [[iot-security-hardware]] | Hardware security components and architectures that provide root of trust, secure storage, and tampe | current |
| [[iot-security-landscape]] | A comprehensive overview of the IoT security domain spanning device fundamentals, communication prot | current |
| [[iot-security-overview]] | IoT security spans the full lifecycle of connected devices — from threat modeling and secure design  | current |
| [[key-management-lifecycle]] | The complete lifecycle of cryptographic keys from generation through distribution, storage, use, rot | current |
| [[krack-attack]] | The Key Reinstallation Attack (KRACK, 2017) exploits the WPA2 protocol itself, forcing devices to re | current |
| [[lightweight-cryptography]] | Lightweight cryptography is the design space of cryptographic primitives that fit on the most resour | current |
| [[message-authentication-code]] | A Message Authentication Code (MAC) is a symmetric-key tag that proves a message came from a holder  | current |
| [[mirai-botnet]] | The Mirai Botnet (2016) exploited default passwords on IP cameras and routers to build a botnet of m | current |
| [[mqtt-security]] | MQTT security covers TLS encryption, authentication methods, access control lists, and broker harden | current |
| [[network-security-fundamentals]] | Network security fundamentals — firewalls, IDS/IPS, VPNs, and segmentation — are the defensive tools | current |
| [[networking-fundamentals]] | Networking fundamentals — the OSI model, TCP/IP, addressing, and routing — are the prerequisite know | current |
| [[nist-iot-cybersecurity]] | NIST's framework for IoT device cybersecurity, defining baseline capabilities and a labeling approac | current |
| [[non-repudiation]] | Non-repudiation ensures that a party cannot deny having performed an action — providing cryptographi | current |
| [[operational-security-lifecycle]] | The operational security life cycle for IoT spans four phases — Define, Implement/Integrate, Operate | current |
| [[ota-updates]] | Over-The-Air (OTA) updates are the mechanism for remotely updating IoT device firmware and software  | current |
| [[owasp-iot-top-10]] | The ten most critical IoT security vulnerabilities, providing a prioritized taxonomy for threat mode | current |
| [[penetration-testing-methodology]] | IoT penetration testing methodology covers the phases — reconnaissance, enumeration, exploitation, a | current |
| [[physical-interface-attack-surface]] | The physical interface attack surface covers all hardware interfaces (JTAG, UART, USB, serial) on Io | current |
| [[physical-unclonable-functions]] | Physical Unclonable Functions (PUFs) are hardware security primitives that exploit manufacturing var | current |
| [[pki]] | PKI is a framework for managing digital certificates and public-key encryption — enabling device aut | current |
| [[principle-of-least-privilege]] | Every component, user, and process should have only the minimum permissions necessary to perform its | current |
| [[privacy-by-design]] | Privacy by Design embeds data minimization, consent, and anonymization into IoT systems from the sta | current |
| [[random-number-generator]] | Cryptographic keys, nonces, and IVs must come from unpredictable, high-entropy sources — True Random | current |
| [[resilience-iot]] | Resilience in IoT means maintaining state awareness and an accepted level of operational normalcy in | current |
| [[risk-assessment-frameworks]] | Structured methodologies for identifying, analyzing, and evaluating security risks specific to IoT s | current |
| [[secure-boot-chain]] | A verification chain from ROM bootloader through OS to application where each stage cryptographicall | current |
| [[secure-development-lifecycle]] | The Secure Development Life Cycle (SDLC) integrates security into every phase of software/system dev | current |
| [[security-by-design]] | Security by Design means integrating security from the very beginning of system design rather than a | current |
| [[security-principles]] | The foundational principles that guide all security design decisions: defense in depth, least privil | current |
| [[sensors]] | Sensors are IoT components that detect and measure physical phenomena — temperature, motion, pressur | current |
| [[side-channel-attacks]] | Side-channel attacks extract cryptographic keys and internal state from IoT devices by measuring phy | current |
| [[smart-city-infrastructure]] | Smart city infrastructure covers IoT deployments in traffic management, utilities, surveillance, and | current |
| [[smart-home-security]] | Smart home security covers consumer IoT threat models — voice assistants, smart locks, cameras, and  | current |
| [[symmetric-encryption]] | Symmetric encryption uses a single shared secret key to both encrypt and decrypt data — it is fast ( | current |
| [[tcg-specifications]] | TCG defines hardware-based security standards including TPM, DICE, and TRNG for establishing root of | current |
| [[threat-modeling]] | Threat modeling — using frameworks like STRIDE, DREAD, and attack trees — systematically identifies  | current |
| [[trusted-platform-module]] | A Trusted Platform Module (TPM) is a dedicated security hardware chip (or firmware implementation) p | current |
| [[web-interface-vulnerabilities]] | IoT web interface vulnerabilities — SQL injection, XSS, username enumeration, weak passwords, accoun | current |
| [[zero-trust-architecture]] | Zero Trust Architecture — "never trust, always verify" — replaces perimeter-based security with iden | current |
| [[zigbee-pairing-vulnerability]] | ZigBee's device pairing procedure was designed for ease of setup but lacked security configuration,  | current |
| [[zigbee-security-model]] | Zigbee security relies on a Trust Center that distributes network keys and AES-128-CCM encryption, b | current |

### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[iot-security-exam-format]] | Written exam (60–90 min) with three question types: definitions, use-case scenarios, and security so | current |

---
## 📚 Software Analyse (110 pages)

### L01 — Introduction
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-1]] | Lecture 1 introduces software analysis as a field, its fundamental limitations (Rice's theorem), the | current |

### L10 — Dynamic Symbolic Execution
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-10]] | Symbolic execution explores all program paths by treating inputs as symbols rather than concrete val | current |

### L11 — Agentic Coding
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-11]] | AI coding agents can write and fix code autonomously, but they make quality assurance more important | draft |

### L02 — Lexical Analysis & NLP
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-2]] | Lecture 2 bridges compiler front-ends (lexical analysis, tokenization) with NLP applied to source co | current |

### L03 — Syntax-Based Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-3]] | Lecture 3 covers syntax-based analysis: defining language structure with context-free grammars, buil | current |

### L04 — Control Flow Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-4]] | Lecture 4 introduces control flow analysis: representing program execution as directed graphs (contr | current |

### L05 — Data Flow Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-5]] | Lecture 5 introduces data flow analysis — a family of compile-time techniques that track how informa | current |

### L06 — Abstract Interpretation
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-6]] | The monotone-framework is grounded in a lattice of facts, a join operator, and monotone transfer fun | current |

### L07 — Interprocedural Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-7]] | Lecture 7 extends data-flow-analysis beyond a single function: it explains why intraprocedural analy | current |

### L08 — Program Slicing
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-8]] | Program slicing extracts the subset of program statements that may affect (backward slice) or be aff | current |

### L09 — Dynamic Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-9]] | Dynamic analysis observes actual program executions to collect traces, enabling instrumentation, fau | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[SOFTWARE_ANALYSE_PROJECTS]] | You have two distinct projects in this course: | current |
| [[abstract-interpretation]] | Abstract interpretation is the general theoretical framework for soundly approximating the semantics | current |
| [[abstract-syntax-tree]] | An abstract syntax tree (AST) is a condensed form of the parse tree that discards syntactic details  | current |
| [[aliasing]] | Aliasing occurs when multiple names (variables, references, pointers) refer to the same memory locat | current |
| [[andersens-points-to-analysis]] | Andersen's points-to analysis is a precise, subset-based (inclusion-based) algorithm for points-to-a | current |
| [[aspect-oriented-programming]] | Aspect-oriented programming modularizes crosscutting concerns (logging, security, database access) t | current |
| [[available-expressions]] | Available expressions determines, for each program point, which expressions have been computed on ev | current |
| [[basic-block]] | A basic block is a maximal sequence of statements that must execute consecutively — control enters o | current |
| [[buggy-code-naturalness]] | Buggy code tends to be less "natural" (higher cross-entropy) than non-buggy code, suggesting that co | current |
| [[call-strings]] | A call string is a sequence of call sites that records the calling context of a procedure invocation | current |
| [[ccfinder]] | CCFinder is a token-based code-clones detection tool that converts programs to token sequences and f | current |
| [[cloning-context-sensitivity]] | Cloning is the most precise context-sensitivity technique: physically duplicate a procedure's body,  | current |
| [[code-clones]] | Code clones are identical or similar code fragments in source files, detected using text, token, gra | current |
| [[code-naturalness-hypothesis]] | Source code written by humans exhibits statistical regularities similar to natural language — it is  | current |
| [[common-subexpression-elimination]] | If the same calculation appears twice and nothing changed in between, the compiler reuses the first  | current |
| [[concolic-execution]] | Concolic execution (concrete + symbolic) combines real program execution with symbolic constraint co | current |
| [[constant-propagation]] | Constant propagation is a data-flow-analysis that tracks, for each variable, whether its value is a  | current |
| [[context-free-grammar]] | A context-free grammar (CFG) is a 4-tuple (tokens, nonterminals, productions, start symbol) that def | current |
| [[context-sensitivity]] | Context sensitivity is the property of an interprocedural-analysis that distinguishes different call | current |
| [[control-dependence]] | Statement b is control dependent on statement a if a's evaluation directly determines whether b will | current |
| [[control-flow-graph]] | A Control Flow Graph (CFG) is a directed graph G=(N,E) where nodes represent statements (or basic-bl | current |
| [[data-flow-analysis]] | Data flow analysis is a compile-time technique that tracks how data (definitions, expressions, varia | current |
| [[dead-code-elimination]] | Dead code elimination removes statements that can never affect the program's output — code that comp | current |
| [[debugging]] | Debugging is the process of finding and fixing defects, supported by automated techniques like dynam | current |
| [[delta-debugging]] | Delta debugging is an automated technique that finds the minimal set of changes responsible for a fa | current |
| [[design-patterns]] | Design patterns are reusable, catalogued solutions to common software design problems, categorized i | current |
| [[distributive-framework]] | A data flow framework is distributive when its transfer functions distribute over the join operator  | current |
| [[dominance]] | Node a dominates node b (a dom b) if every path from the entry node to b passes through a — a founda | current |
| [[dominator-tree]] | The dominator tree is a tree where each node's parent is its dominance, providing a compact represen | current |
| [[du-chains-ud-chains]] | DU-chains (definition-use chains) connect each variable definition to all uses it can reach; UD-chai | current |
| [[dynamic-analysis]] | Dynamic analysis observes actual program executions to collect traces, enabling instrumentation, fau | current |
| [[dynamic-slicing]] | Slice computed for a specific input and execution trace, capturing only statements that actually aff | current |
| [[fault-localization]] | Fault localization ranks program statements by suspiciousness based on which statements are executed | current |
| [[finite-automata]] | Abstract computational models with a finite set of states, used in compiler design, pattern matching | current |
| [[finite-automata-and-regular-expressions]] | Regular expressions define token patterns formally, and finite automata (state diagrams) implement t | current |
| [[first-sets]] | FIRST(α) is the set of terminal symbols that can appear as the first token of any string derived fro | current |
| [[galois-connection]] | A Galois connection C ⇄ A between a concrete domain C and an abstract domain A is a pair of monotone | current |
| [[gen-kill-analysis]] | Gen and kill sets are the local transfer functions that describe how each statement creates or inval | current |
| [[grammar-ambiguity]] | A grammar is ambiguous if at least one string in its language has more than one valid parse tree, me | current |
| [[heap-analysis]] | Heap analysis is the family of static analyses that reason about heap-allocated memory — determining | current |
| [[hierarchy-of-analysis]] | Program analysis uses four reasoning paradigms — deduction (static), observation (dynamic), inductio | current |
| [[inlining-context-sensitivity]] | Inlining is a context-sensitivity technique that substitutes a procedure's body at every call site,  | current |
| [[interprocedural-analysis]] | Interprocedural analysis extends data-flow-analysis beyond a single function so that information flo | current |
| [[iterative-data-flow-analysis]] | Iterative data flow analysis is the standard worklist algorithm that solves data flow equations by r | current |
| [[java-for-software-analysis]] | Everything you need to know about Java, Maven, and the libraries used in both Software Analyse proje | current |
| [[lattice]] | A lattice is a partially ordered set in which every two elements have a unique least upper bound (jo | current |
| [[left-factoring]] | Left factoring is a grammar transformation that eliminates common prefixes among alternatives of a p | current |
| [[left-recursion-elimination]] | Left recursion elimination is a grammar transformation that rewrites left-recursive productions into | current |
| [[lex-and-flex]] | Lex (and its GNU successor Flex) are lexer generators that automatically convert regular expression  | current |
| [[lexical-analysis]] | Lexical analysis is the first phase of compilation that converts a character stream into a sequence  | current |
| [[live-variable-analysis]] | Live variable analysis determines, for each program point, which variables may be read on some futur | current |
| [[liveness-analysis]] | Liveness analysis figures out, for every point in a program, which variables still have a future use | current |
| [[machine-learning-basics]] | Machine learning is the practice of training algorithms on data to learn patterns and make predictio | current |
| [[meet-over-valid-paths]] | The Meet Over Valid Paths (MVP) is the interprocedural analogue of mop-vs-mfp — the precise but unde | current |
| [[minimal-fixed-point-algorithm]] | The Minimal Fixed Point (MFP) algorithm is the iterative, worklist-based implementation of the monot | current |
| [[monotone-framework]] | The monotone framework is the abstract mathematical skeleton that all data flow analyses share — it  | current |
| [[mop-vs-mfp]] | The Meet Over All Paths (MOP) is the precise but undecidable data flow solution (join over the exact | current |
| [[n-gram-language-models]] | N-gram language models estimate the probability of a token sequence by conditioning each token on th | current |
| [[natural-loop]] | A natural loop is a set of nodes in a control-flow-graph identified by a back edge (an edge from a n | current |
| [[object-oriented-programming]] | Object-oriented programming organizes code around objects — instances of classes that bundle data (f | current |
| [[operator-precedence-associativity]] | Operator precedence and associativity are encoded into a grammar by introducing separate nonterminal | current |
| [[parse-tree]] | A parse tree (concrete syntax tree) is a tree representation of a derivation where the root is the s | current |
| [[path-profiling]] | Path profiling counts how often each execution path through a function runs, using the Ball-Larus al | current |
| [[perplexity-and-entropy]] | Perplexity and cross-entropy are metrics for evaluating language models — perplexity measures how "c | current |
| [[points-to-analysis]] | Points-to analysis computes, for every pointer variable, the set of heap objects it may point to — t | current |
| [[post-dominance]] | Node d post-dominates node n (d pdom n) if every path from n to the exit node passes through d — the | current |
| [[predictive-parsing]] | Predictive parsing is a top-down parsing method where a single lookahead token unambiguously determi | current |
| [[procedure-summaries]] | A procedure summary is a single transfer function that captures a procedure's net effect on the abst | current |
| [[program-slicing]] | Extract the subset of statements that may affect (backward) or be affected by (forward) a variable a | current |
| [[program-traces]] | Program traces record the executed instructions and runtime attributes (data state, call stack, obje | current |
| [[reaching-definitions]] | Reaching definitions determines, for each program point, which variable definitions may have occurre | current |
| [[readability-classifier]] | Extract static metrics from code snippets, train a logistic regression classifier, predict whether h | current |
| [[register-allocation]] | Register allocation maps program variables to a limited number of CPU registers, and when there aren | current |
| [[rices-theorem]] | Rice's theorem states that all non-trivial semantic properties of programs are undecidable — no algo | current |
| [[shift-reduce-parsing]] | Shift-reduce parsing is a bottom-up parsing strategy that builds the parse tree from leaves to root  | current |
| [[sign-analysis]] | Track the sign (−, 0, +) of every integer value in Java bytecode to find division-by-zero and negati | current |
| [[smoothing-techniques]] | Smoothing techniques redistribute probability mass from seen to unseen n-grams, preventing zero prob | current |
| [[software-analyse-projects-overview]] | An overview of the two Software Analyse projects: a readability classifier that predicts code qualit | current |
| [[software-analysis]] | Software analysis is the process of automatically extracting information about a program from its so | current |
| [[soundness-and-completeness]] | Sound analysis reports all errors (but may include false alarms); complete analysis reports only rea | current |
| [[static-vs-dynamic-analysis]] | Static analysis examines code without running it (reasoning about all possible executions); dynamic  | current |
| [[steensgaards-points-to-analysis]] | Steensgaard's points-to analysis is a fast, equality-based algorithm for points-to-analysis that run | current |
| [[surprisal-and-code-prediction]] | Surprisal (information content) measures how unexpected a specific token is given its context — high | current |
| [[symbolic-execution]] | Symbolic execution treats program inputs as symbolic variables rather than concrete values, explorin | current |
| [[syntax-directed-translation]] | Syntax-directed translation augments a CFG with attributes and semantic rules so that parsing also c | current |
| [[test-generation]] | Test generation creates concrete input values that exercise specific program paths, primarily throug | current |
| [[testing]] | Software testing validates program behaviour against expected outcomes and provides the oracle that  | current |
| [[tokenization-and-token-types]] | Tokenization splits source code into categorized units (tokens) such as identifiers, literals, opera | current |
| [[union-find-data-structure]] | Union-Find (also called Disjoint Set Union) is a data structure that maintains a partition of elemen | current |
| [[valid-paths]] | A valid path in an interprocedural control flow graph is a path that respects call-return matching — | current |
| [[very-busy-expressions]] | Very busy expressions determines, for each program point, which expressions will definitely be evalu | current |
| [[visitor-pattern]] | The Visitor pattern separates an algorithm from the object structure it operates on by letting you d | current |
| [[widening-narrowing]] | Operators in abstract interpretation that accelerate fixpoint computation (widening) and improve pre | current |
| [[zero-analysis-worked-example]] | Zero Analysis is the lecture's running example of abstract-interpretation: track for each variable w | current |
| [[binary-search]] | Binary search finds a target value in a sorted array by repeatedly dividing the search interval in h | current |
| [[phi-function]] | Pseudo-assignment in SSA form that merges variable definitions from different control flow paths. | current |
| [[program-dependence-graph]] | Graph combining control and data dependence edges over CFG nodes — the complete dependence map of a  | current |
| [[static-single-assignment]] | Intermediate representation where each variable is assigned exactly once, making data dependencies e | current |
| [[system-dependence-graph]] | Extension of PDG to multiple procedures, enabling interprocedural slicing. | current |


### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-codebase-defense]] | Format: Multiple choice | current |
| [[software-analyse-exam-prep]] | Format: Multiple choice | current |
| [[zero-analysis-worked-example]] | Zero Analysis is the lecture's running example of abstract-interpretation: track for each variable w | current |

---
