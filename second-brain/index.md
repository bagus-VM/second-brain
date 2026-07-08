# second-brain — Master Index

> Maintained by Professor White. Updated after every INGEST and significant QUERY.

**Last updated:** 2026-07-08
**Total pages:** 644 (vault + study; excluding raw/)
**Active courses:** 6

---

## Exam Calendar
| Course | Exam Date | Days Left | Progress |
|--------|-----------|-----------|----------|
| [[multimedia-databases]] | 21 July 2026 | ~13 | **9/9 lectures ✅** + Ex01–Ex09 practice complete ✅ (100+ pages) |
| [[network-science]] | 28 July 2026 | ~20 | **9/9 lectures ✅** + Ex01–Ex08 (139 pages) |
| [[reproducibility-engineering]] | 30 July 2026 | ~22 | **9/9 lectures ✅** + Sheet 1–9 (66+ pages) |
| [[software-analyse]] | 31 July 2026 | ~23 | **11/11 lectures ✅** (100+ pages) |
| [[iot-security]] | 05 Aug 2026 | ~35 | **8/8 lectures ✅** (~80 pages) + 3 papers ingested |
| [[introduction-to-microelectronics]] | 06 Aug 2026 | ~28 | **8/8 lectures ✅** (~55 pages) |

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
| [[reproducibility-engineering-sheet-8]] | Sheet 8: tidy data with DuckDB (pivoting, splitting, concatenation) | current |
| [[reproducibility-engineering-sheet-9]] | Sheet 9: JSON, jq, JSON Schema validation, Bowtie meta-validator | current |

---

## 📚 Software Analyse (85 pages)

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

### L09 — Dynamic Analysis
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-9]] | Program traces, instrumentation, AOP/AspectJ, fault localization, delta debugging | current |
| [[aspect-oriented-programming]] | Crosscutting concerns modularized via aspects, pointcuts, advice | current |
| [[fault-localization]] | Rank statements by suspiciousness (Tarantula, Ochiai) | current |
| [[delta-debugging]] | Binary search for minimal failure-inducing input | current |

### L10 — Symbolic Execution
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-lecture-10]] | Symbolic store + path constraint, concolic execution, Ball-Larus path profiling | current |
| [[software-analyse-lecture-11]] | Agentic coding and software quality: AI code generation, QA bottleneck, senior engineer tax, MCP | current |
| [[symbolic-execution]] | Treat inputs as symbols, explore all paths via constraint solving | current |
| [[concolic-execution]] | Concrete + symbolic: execute with real inputs, collect constraints, negate to explore | current |

### Projects
| Page | Summary | Status |
|------|---------|--------|
| [[readability-classifier]] | Code readability ML pipeline: Halstead, entropy, cyclomatic complexity, logistic regression | current |
| [[sign-analysis]] | Interprocedural sign analysis: lattice theory, pairwise decomposition, bytecode dataflow | current |
| [[java-for-software-analysis]] | Java essentials: Maven, JavaParser, ASM, WEKA, picocli, visitor pattern | current |

| [[software-analyse-lecture-1]] | Lecture 1 introduces software analysis as a field, its fundamental limitations ( | current |
| [[software-analyse-lecture-2]] | Lecture 2 bridges compiler front-ends (lexical analysis, tokenization) with NLP  | current |
| [[software-analyse-lecture-3]] | Lecture 3 covers syntax-based analysis: defining language structure with context | current |
| [[software-analyse-lecture-4]] | Lecture 4 introduces control flow analysis: representing program execution as di | current |
| [[software-analyse-lecture-5]] | Lecture 5 introduces data flow analysis — a family of compile-time techniques th | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[binary-search]] | O(log n) search on sorted arrays; core of delta debugging | current |
| [[buggy-code-naturalness]] | Buggy code tends to be less "natural" (higher cross-entropy) than non-buggy code | current |
| [[ccfinder]] | CCFinder is a token-based [[code-clones|code clone]] detection tool that convert | current |
| [[common-subexpression-elimination]] | If the same calculation appears twice and nothing changed in between, the compil | current |
| [[constant-propagation]] | Constant propagation is a [[data-flow-analysis|data flow analysis]] that tracks, | current |
| [[dead-code-elimination]] | Dead code elimination removes statements that can never affect the program's out | current |
| [[debugging]] | Debugging is the process of finding and fixing defects, supported by automated t | current |
| [[design-patterns]] | Design patterns are reusable, catalogued solutions to common software design pro | current |
| [[du-chains-ud-chains]] | DU-chains (definition-use chains) connect each variable definition to all uses i | current |
| [[dynamic-analysis]] | Dynamic analysis observes actual program executions to collect traces, enabling  | current |
| [[finite-automata]] | Abstract computational models with a finite set of states, used in compiler desi | current |
| [[first-sets]] | FIRST(α) is the set of terminal symbols that can appear as the first token of an | current |
| [[galois-connection]] | A Galois connection C ⇄ A between a concrete domain C and an abstract domain A i | current |
| [[gen-kill-analysis]] | Gen and kill sets are the local transfer functions that describe how each statem | current |
| [[hierarchy-of-analysis]] | Program analysis uses four reasoning paradigms — deduction (static), observation | current |
| [[left-factoring]] | Left factoring is a grammar transformation that eliminates common prefixes among | current |
| [[left-recursion-elimination]] | Left recursion elimination is a grammar transformation that rewrites left-recurs | current |
| [[lex-and-flex]] | Lex (and its GNU successor Flex) are lexer generators that automatically convert | current |
| [[liveness-analysis]] | Liveness analysis figures out, for every point in a program, which variables sti | current |
| [[monotone-framework]] | The monotone framework is the abstract mathematical skeleton that all data flow  | current |
| [[object-oriented-programming]] | Object-oriented programming organizes code around objects — instances of classes | current |
| [[operator-precedence-associativity]] | Operator precedence and associativity are encoded into a grammar by introducing  | current |
| [[path-profiling]] | Path profiling counts how often each execution path through a function runs, usi | current |
| [[post-dominance]] | Node d post-dominates node n (d pdom n) if every path from n to the exit node pa | current |
| [[program-traces]] | Program traces record the executed instructions and runtime attributes (data sta | current |
| [[register-allocation]] | Register allocation maps program variables to a limited number of CPU registers, | current |
| [[surprisal-and-code-prediction]] | Surprisal (information content) measures how unexpected a specific token is give | current |
| [[test-generation]] | Test generation creates concrete input values that exercise specific program pat | current |
| [[testing]] | Software testing validates program behaviour against expected outcomes and provi | current |
| [[widening-narrowing]] | Operators in abstract interpretation that accelerate fixpoint computation (widen | current |
### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[software-analyse-codebase-defense]] | Exam defense prep: walk through both project codebases, explain design decisions, articulate concepts | current |
| [[software-analyse-projects-overview]] | Both projects overview, comparison, and study strategy | current |
| [[visitor-pattern]] | Design pattern for AST traversal, double dispatch | current |
| [[machine-learning-basics]] | Supervised learning, features, labels, classification | current |

---

## 📚 IoT Security (~70 pages)

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

### L08 — Compliance, IoT 2.0, and Advanced Threats
| Page | Summary | Status |
|------|---------|--------|
| [[iot-lecture-8]] | Compliance monitoring, risk assessments, governmental attacks, IoT 2.0, defence-in-depth | current |

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

| [[iot-lecture-1]] | A comprehensive overview of the IoT security domain spanning fundamentals, appli | current |
| [[iot-lecture-2]] | A comprehensive taxonomy of attack types targeting IoT systems, organized into n | current |
| [[iot-lecture-3]] | A systematic enumeration of IoT [[attack-surface-analysis]] based on Daniel Mies | current |
| [[iot-lecture-4]] | Design goals and best practices for building secure IoT systems, covering automa | current |
| [[iot-lecture-5]] | Hardware-based security mechanisms for IoT devices, covering [[physical-unclonable-functions\|PUFs]] | current |

### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[availability]] | The assurance that systems and data are accessible to authorized users when need | current |
| [[ble-security]] | Bluetooth Low Energy (BLE) security covers the pairing modes, encryption mechani | current |
| [[coap-security]] | CoAP (Constrained Application Protocol) security covers DTLS for transport encry | current |
| [[common-criteria]] | An international standard for evaluating the security properties of IT products  | current |
| [[course]] |  | current |
| [[defense-in-depth]] | Defence-in-depth layers multiple defensive mechanisms so that if one layer fails | current |
| [[denial-of-service]] | Attacks that make IoT devices or services unavailable to legitimate users, rangi | current |
| [[device-provisioning]] | Device provisioning is the process of giving each IoT device its unique identity | current |
| [[etsi-en-303-645]] | A European standard defining 13 provisions for consumer IoT security, forming th | current |
| [[fips-140-2]] | US government standard for validating the security of cryptographic modules in h | current |
| [[gdpr-compliance]] | GDPR is EU law governing personal data processing — for IoT, it mandates data mi | current |
| [[healthcare-iot-security]] | Healthcare IoT (IoMT) security covers connected medical devices — insulin pumps, | current |
| [[iec-62443]] | The international standard series for securing industrial automation and control | current |
| [[industrial-iot-security]] | Industrial IoT (IIoT) security covers SCADA systems, PLCs, and operational techn | current |
| [[iot-communication-protocols]] | IoT communication protocols — MQTT, CoAP, Zigbee, BLE, LoRaWAN, and Thread/Matte | current |
| [[iot-data-lifecycle]] | The IoT data lifecycle — collection, transmission, storage, processing, and rete | current |
| [[iot-device-fundamentals]] | IoT device fundamentals covers the hardware and software building blocks — micro | current |
| [[iot-network-architecture]] | IoT network architecture is the three-tier model — perception (devices), network | current |
| [[iot-security-overview]] | IoT security spans the full lifecycle of connected devices — from threat modelin | current |
| [[key-management-lifecycle]] | The complete lifecycle of cryptographic keys from generation through distributio | current |
| [[mqtt-security]] | MQTT security covers TLS encryption, authentication methods, access control list | current |
| [[network-security-fundamentals]] | Network security fundamentals — firewalls, IDS/IPS, VPNs, and segmentation — are | current |
| [[networking-fundamentals]] | Networking fundamentals — the OSI model, TCP/IP, addressing, and routing — are t | current |
| [[nist-iot-cybersecurity]] | NIST's framework for IoT device cybersecurity, defining baseline capabilities an | current |
| [[owasp-iot-top-10]] | The ten most critical IoT security vulnerabilities, providing a prioritized taxo | current |
| [[penetration-testing-methodology]] | IoT penetration testing methodology covers the phases — reconnaissance, enumerat | current |
| [[pki]] | PKI is a framework for managing digital certificates and public-key encryption — | current |
| [[principle-of-least-privilege]] | Every component, user, and process should have only the minimum permissions nece | current |
| [[privacy-by-design]] | Privacy by Design embeds data minimization, consent, and anonymization into IoT  | current |
| [[risk-assessment-frameworks]] | Structured methodologies for identifying, analyzing, and evaluating security ris | current |
| [[secure-boot-chain]] | A verification chain from ROM bootloader through OS to application where each st | current |
| [[security-principles]] | The foundational principles that guide all security design decisions: defense in | current |
| [[side-channel-attacks]] | Side-channel attacks extract cryptographic keys and internal state from IoT devi | current |
| [[smart-city-infrastructure]] | Smart city infrastructure covers IoT deployments in traffic management, utilitie | current |
| [[smart-home-security]] | Smart home security covers consumer IoT threat models — voice assistants, smart  | current |
| [[tcg-specifications]] | TCG defines hardware-based security standards including TPM, DICE, and TRNG for  | current |
| [[zero-trust-architecture]] | Zero Trust Architecture — "never trust, always verify" — replaces perimeter-base | current |
| [[zigbee-security-model]] | Zigbee security relies on a Trust Center that distributes network keys and AES-1 | current |

### Exam Prep
| Page | Summary | Status |
|------|---------|--------|
| [[iot-security-exam-format]] | Written exam format: definitions, short answers, scenarios | current |

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
| [[microelectronics-lecture-7]] | L07: CMOS Applications - Flip-Flops (SRAM/DRAM) and Amplifiers (CS/CG/CD) | current |
| [[microelectronics-lecture-8]] | L08: OpAmps - Inverting and Non-Inverting Amplifiers | current |


### Additional Concepts
| Page | Summary | Status |
|------|---------|--------|
| [[analog-amplifier]] | A circuit that increases the amplitude of an analog signal using active componen | current |
| [[avalanche-breakdown]] | Avalanche breakdown is a carrier multiplication mechanism that occurs at high re | current |
| [[band-theory]] | Band theory explains how electrons in solids occupy continuous ranges of allowed | current |
| [[bridge-rectifier]] | A full-wave rectifier using four diodes in a bridge configuration that eliminate | current |
| [[capacitor]] | A capacitor is a two-terminal component that stores energy in an electric field  | current |
| [[clamper-circuit]] | A clamper (DC restorer) shifts the DC level of a signal without changing its wav | current |
| [[cmos-inverter]] | The fundamental building block of CMOS digital circuits: an NMOS and PMOS transi | current |
| [[cmos-logic-gates]] | The CMOS logic family builds every Boolean function as a *complementary* pair of | current |
| [[cmos-nand-gate]] | A CMOS NAND gate uses two nMOS in series (pull-down) and two pMOS in parallel (p | current |
| [[cmos-nor-gate]] | A CMOS NOR gate uses two nMOS in parallel (pull-down) and two pMOS in series (pu | current |
| [[cmos-xor-gate]] | The XOR function (A ⊕ B = AB̄ + ĀB) cannot be implemented in a single stage of s | current |
| [[common-source-amplifier]] | A MOSFET amplifier configuration where the source is grounded, providing voltage | current |
| [[conductor]] | A material with high electrical conductivity due to free charge carriers (typica | current |
| [[digital-circuit-design]] | Digital circuit design is the art of combining MOS transistors into logic gates, | current |
| [[digital-logic]] | The representation and manipulation of information using discrete voltage levels | current |
| [[diode-applications]] | Diodes are one-way valves for current — by combining them with resistors and cap | current |
| [[doping-and-extrinsic-semiconductors]] | Doping means adding tiny amounts of specific impurity atoms to silicon to create | current |
| [[electricity]] | Electricity is the flow of electric charge (carried by electrons or holes), gove | current |
| [[etching]] | The process of selectively removing material from a wafer surface using chemical | current |
| [[full-wave-rectifier]] | A full-wave rectifier uses two or four diodes to pass both halves of the AC wave | current |
| [[germanium]] | Germanium was the first semiconductor used in transistors but was largely replac | current |
| [[half-wave-rectifier]] | A half-wave rectifier uses a single diode to pass only one half of the AC wavefo | current |
| [[insulator]] | A material with very low electrical conductivity due to a large bandgap that pre | current |
| [[limiter-circuit]] | A limiter clips the voltage waveform at a specified threshold, preventing it fro | current |
| [[mask-alignment]] | The process of precisely positioning a photomask over a wafer so that new patter | current |
| [[mos-capacitor]] | The MOS capacitor is the fundamental structure beneath the MOSFET gate — a metal | current |
| [[mos-transistors]] | A MOSFET is a transistor where a voltage on a gate electrode controls current fl | current |
| [[mosfet]] | A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a voltage-contro | current |
| [[mosfet-operating-regions]] | MOSFETs operate in three distinct regions — Cutoff, Linear (Triode), and Saturat | current |
| [[nmos-transistor]] | An nMOS transistor has N-type source and drain regions in a P-type substrate, us | current |
| [[p-n-junction-overview]] | A p-n junction is where p-type and n-type semiconductors meet — the built-in ele | current |
| [[pmos-transistor]] | A pMOS transistor has P-type source and drain regions in an N-type substrate, us | current |
| [[pmtransistor]] | A pMOS transistor has P-type source and drain regions in an N-type substrate, us | current |
| [[power-supply]] | The source of electrical energy that powers electronic circuits, converting AC m | current |
| [[rectifier]] | A rectifier is a circuit that converts alternating current (AC) to direct curren | current |
| [[semiconductor-physics]] | Semiconductors are materials whose electrical conductivity falls between conduct | current |
| [[threshold-voltage]] | The threshold voltage (VTH) is the minimum gate-to-source voltage required to cr | current |
| [[transistor]] | A transistor is a three-terminal semiconductor device that can amplify signals o | current |
| [[vlsi-design]] | VLSI (Very Large Scale Integration) is the discipline of designing chips with mi | current |
| [[zener-breakdown]] | Zener breakdown is a quantum mechanical tunnelling mechanism that occurs in heav | current |
| [[zener-diode]] | A Zener diode is a heavily doped diode designed to operate reliably in the rever | current |