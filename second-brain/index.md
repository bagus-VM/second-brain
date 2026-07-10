# second-brain — Master Index

> Maintained by Professor White. Updated after every INGEST and significant QUERY.

**Last updated:** 2026-07-10
**Total pages:** 656 (vault + study; excluding raw/)
**Active courses:** 6

---

## Exam Calendar
| Course | Exam Date | Days Left | Progress |
|--------|-----------|-----------|----------|
| [[multimedia-databases]] | 21 July 2026 | ~13 | **9/9 lectures ✅** + Ex01–Ex09 practice complete ✅ (100+ pages) |
| [[network-science]] | 28 July 2026 | ~20 | **9/9 lectures ✅** + Ex01–Ex08 (139 pages) |
| [[reproducibility-engineering]] | 30 July 2026 | ~22 | **9/9 lectures ✅** + Sheet 1–10 (75+ pages) |
| [[software-analyse]] | 31 July 2026 | ~23 | **11/11 lectures ✅** (100+ pages) |
| [[iot-security]] | 05 Aug 2026 | ~27 | **9/9 lectures ✅** (~80 pages) + 3 papers ingested |
| [[introduction-to-microelectronics]] | 06 Aug 2026 | ~28 | **9/9 lectures ✅** (~65 pages) |

---

## 📚 Multimedia Databases (95 pages)

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
| [[artifact-packaging]] | Packaging research artifacts for reproducibility: fork+patches, Docker, doall.sh | current |

### Practice & Flashcards
| Page | Summary | Status |
| [[reproducibility-engineering-sheet-10]] | Exercise Sheet 10: Docker secrets, LLM reproducibility (temperature/seed), structured outputs | current |
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
| [[mmdb-exam-prediction]] | Exam prediction: 11 archetypes, top-3 targets | current |

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
| Page | Summary | Status |
|------|---------|--------|
| [[graph-fundamentals]] | G=(V,E), modeling choices | current |
| [[graph-representations]] | Edge list, adjacency list/matrix | current |
| [[neighbourhood-and-degree]] | N(v), deg(v), handshaking lemma | current |
| [[paths-walks-and-cycles]] | Walk → path → cycle hierarchy | current |
| [[shortest-path-and-diameter]] | dist(u,v), diam(G) | current |
| [[eulerian-path-and-circuit]] | Königsberg, degree parity | current |
| [[breadth-first-search]] | BFS, FIFO, O(\|V\|+\|E\|) | current |
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
| Page | Summary | Status |
|------|---------|--------|
| [[adjacency-matrix-factorization]] | A unifying view: spectral embeddings, DeepWalk, and node2vec all implicitly fact | current |
| [[algebraic-connectivity]] | Algebraic connectivity (λ₂) is the second-smallest eigenvalue of the [[graph-laplacian\|graph Laplacian]] | current |
| [[betweenness-centrality]] | Betweenness centrality measures how often a node sits on shortest paths between  | current |
| [[bipartite-graphs]] | A bipartite graph has two disjoint node sets where edges only connect nodes acro | current |
| [[centrality-measures]] | Centrality measures quantify node importance — but each measure encodes a differ | current |
| [[closeness-centrality]] | Closeness centrality measures how near a node is to all other nodes on average — | current |
| [[community-detection]] | Community detection partitions a graph into groups of nodes that are densely con | current |
| [[community-detection-overview]] | Community detection finds subsets of nodes with dense internal connections and s | current |
| [[conductance]] | Conductance measures the fraction of edges that leave a community relative to it | current |
| [[configuration-model]] | The configuration model generates random graphs with a prescribed degree sequenc | current |
| [[connected-component]] | A connected component is a maximal set of nodes where every node can reach every | current |
| [[degree-centrality]] | Degree centrality measures the number of direct contacts a node has — the simple | current |
| [[diffusion-of-innovations]] | Diffusion of innovations studies how new ideas, technologies, and behaviors spre | current |
| [[directed-and-undirected-graphs]] | ==Undirected graphs model symmetric relationships (friendship)==, while directed | current |
| [[directed-connectivity]] | In directed graphs, strong connectivity requires mutual reachability between all | current |
| [[edge-betweenness]] | Edge betweenness measures how often an edge lies on shortest paths between all p | current |
| [[eigenvector-centrality]] | Eigenvector centrality measures recursive prestige — important nodes are connect | current |
| [[embeddedness]] | Embeddedness describes a node whose neighbors are themselves densely interconnec | current |
| [[embedding-based-community-detection]] | Embedding-based community detection uses node embeddings (from random walks or n | current |
| [[global-email-experiment]] | ==Dodds, Muhamad & Watts (2003)== replicated Milgram's experiment using email ac | current |
| [[granovetter-weak-ties]] | Granovetter's weak-tie hypothesis states that weak ties (acquaintances, not clos | current |
| [[graph-laplacian]] | The graph Laplacian L = D - A encodes the structure of a graph — its eigenvalues | current |
| [[graph-partitioning]] | Graph partitioning divides a graph into a fixed number of balanced clusters — un | current |
| [[harmonic-centrality]] | Harmonic centrality is the disconnected-graph extension of [[closeness-centrality\|closeness centrality]] | current |
| [[hierarchical-clustering]] | Divisive and agglomerative community detection methods produce dendrograms — tre | current |
| [[hnsw-indexing]] | HNSW is a graph-based approximate nearest-neighbor index that applies Kleinberg' | current |
| [[k-balance]] | k-balance is the partition structure guaranteed by weak structural balance: a co | current |
| [[kernighan-lin-algorithm]] | Kernighan-Lin is a local-search algorithm for balanced graph partitioning — iter | current |
| [[laplacian-eigenmaps]] | Laplacian eigenmaps embed each node as a point in R^d using the eigenvectors of  | current |
| [[maxstc-complexity]] | Finding the edge labeling with the most strong edges that satisfies Strong Triad | current |
| [[message-passing-framework]] | The message-passing framework defines how GNNs compute node embeddings: each lay | current |
| [[min-cut-max-flow]] | Min-cut / Max-flow finds the smallest set of edges whose removal disconnects two | current |
| [[modularity-resolution-limit]] | The resolution limit is a fundamental limitation of [[modularity]] — it cannot d | current |
| [[neighborhood-overlap]] | Neighborhood overlap measures the fraction of neighbors shared by two connected  | current |
| [[network-autocorrelation]] | Network autocorrelation is the statistical tendency for connected nodes to share | current |
| [[network-effects]] | The structure of connections creates outcomes — visibility, influence, lock-in,  | current |
| [[network-examples]] | Networks appear across every domain — social, communication, information, econom | current |
| [[normalized-cut]] | Normalized cut balances the size of a cut against the total degree (volume) of t | current |
| [[online-link-formation]] | Online data with timestamps turns link formation into a measurable process — emp | current |
| [[pagerank]] | PageRank extends [[eigenvector-centrality]] with a damping factor — a random sur | current |
| [[power-law-distribution]] | A power-law distribution is a heavy-tailed distribution where a few nodes have v | current |
| [[process-structure-interaction-gap]] | The process-structure interaction gap is the sixth gap in the course: the same n | current |
| [[product-space-network]] | The product space network connects exported products that require similar capabi | current |
| [[random-walks]] | A random walk on a graph is a stochastic process where a walker moves from node  | current |
| [[signed-laplacian]] | The signed Laplacian L_σ = D − A_σ extends the standard graph Laplacian to signe | current |
| [[sparse-dense-and-random-graphs]] | Graphs differ quantitatively in edge density — from sparse (few edges) to dense  | current |
| [[spectral-clustering-embeddings]] | Spectral clustering is k-means applied to Laplacian eigenmaps — nodes in the sam | current |
| [[spectral-partitioning]] | Spectral partitioning uses the eigenvectors of the graph Laplacian to find a nat | current |
| [[strong-triadic-closure]] | If a node has two strong ties, Strong Triadic Closure requires those endpoints t | current |
| [[structural-holes-and-brokerage]] | Structural holes are missing connections between groups; brokers who span them g | current |
| [[temporal-networks]] | Temporal networks assign activation times to edges, revealing that static aggreg | current |
| [[weak-tie-paradox-contagion]] | The same weak ties and bridges that accelerate simple contagion (rumors, disease | current |
| [[web-bow-tie-structure]] | Broder et al. (2000) found that the Web decomposes into a bow-tie: a strongly co | current |
| [[weighted-graphs]] | ==A weighted graph assigns a numerical value w(e) to each edge, encoding strengt | current |
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
| Page | Summary | Status |
|------|---------|--------|
| [[network-science-exercise-prep]] | Exercise-based exam prep: NetworkX functions, hand calculations, key formulas | current |

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
| [[reproducibility-engineering-lecture-9]] | LLMs and reproducibility: local vs remote, structured outputs, constrained decoding, JSON Schema | current |
| [[hdf5]] | Hierarchical data format: files/groups/datasets/attributes | current |
| [[json-schema]] | Vocabulary for validating JSON document structure | current |

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

## 📚 Introduction to Microelectronics (65 pages)

### L09 — Integrators, Differentiators & Memories
| Page | Summary | Status |
|------|---------|--------|
| [[microelectronics-lecture-9]] | OpAmp integrators/differentiators, voltage adder, voltage follower, SRAM/DRAM/ROM/Flash | current |
| [[opamp-integrator]] | Inverting amplifier with capacitor feedback: Vout = -(1/RC) ∫ Vin dt | current |
| [[opamp-differentiator]] | Inverting amplifier with capacitor input: Vout = -RC dVin/dt | current |
| [[weighted-summer]] | Multiple inputs summed through resistors: Vout = -Rf × Σ(Vi/Ri) | current |
| [[voltage-follower]] | Unity-gain buffer for impedance transformation (gain = 1) | current |
| [[sram-cell]] | 6-transistor bistable latch: fast, volatile, used for caches | current |
| [[dram-cell]] | 1-transistor + 1-capacitor: dense, volatile, needs refresh | current |
| [[sense-amplifier]] | Detects tiny voltage differences on memory bit lines | current |
| [[flash-memory]] | Floating gate transistor: non-volatile, block-erasable, limited endurance | current |
