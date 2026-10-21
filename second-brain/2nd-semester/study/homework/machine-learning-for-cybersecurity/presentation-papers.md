---
title: "Student Paper Presentations — Network Intrusion Detection"
tags: [homework, ml-security, semester-2, presentations]
course: "Machine Learning for Cybersecurity"
source_count: 2
status: current
last_updated: 2026-10-20
---

# ML for Cybersecurity — paper presentations (L3, slide 36)

**Task (as printed on L3 slide 36):** "Select one of the following papers and present the key insights (20 minutes) on Nov 3 (or Oct 29)." Topic: *Network intrusion detection*.

Sources: the three papers' own abstracts (arXiv, NDSS and the authors' PDF of the ACM CCS paper), plus the course slides `03_ML_Intro.pdf` (L3). Where an abstract could not be fetched, that is stated plainly below.

**Format:** 20 minutes, key insights. That is a talk, not a paper reading — roughly 12–15 slides, and the audience has not read the paper.

## Index

1. [Paper 1 — SoK: Pragmatic Assessment of ML for NID](#paper-1--sok-pragmatic-assessment-of-ml-for-nid)
2. [Paper 2 — HyperVision](#paper-2--hypervision)
3. [Paper 3 — The Emperor has no Clothes](#paper-3--the-emperor-has-no-clothes)
4. [Comparison: what the three disagree about](#comparison-what-the-three-disagree-about)
5. [What a good 20-minute talk of each must cover](#what-a-good-20-minute-talk-of-each-must-cover)
6. [How to prepare](#how-to-prepare)
7. [Open questions](#open-questions)

---

## Paper 1 — SoK: Pragmatic Assessment of ML for NID

**Apruzzese, Laskov, Schneider.** *SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection.* IEEE EuroS&P 2023 (8th IEEE European Symposium on Security and Privacy). DOI 10.1109/EuroSP57164.2023.00042. Slide URL: https://arxiv.org/pdf/2305.00550 (arXiv:2305.00550, submitted 30 Apr 2023, cs.CR).

**Research question.** Practitioners are sceptical of ML for network intrusion detection (NID) even though the science keeps advancing. The SoK asks *why* the disconnect exists and *how the evaluation methodology in the literature should change* so that the operational value of an ML-based NID method can actually be estimated.

**Method.** The paper elucidates which "factors" influence real deployment, then defines **pragmatic assessment** as the evaluation notion that accounts for them. The authors then *perform* that assessment themselves: re-evaluating existing ML methods for NID (focusing on classification of malicious network traffic) across **hundreds of configuration settings, diverse adversarial scenarios, and four hardware platforms**, with large and reproducible evaluations, and validating the conclusions through a **user study with security practitioners**.

**Headline finding.** "The state-of-research hardly allows one to estimate the value of ML for NID." Method papers that mainly aim to show they "outperform" prior work overlook the practical implications of deploying the solution, and the value of ML for NID depends on factors such as hardware that the scientific literature neglects.

**Why it matters here.** This is the framing paper of the set and the one closest to the course's own message. The lecture's credit-card example demonstrates that a model can look excellent on one metric and be operationally useless ([[classification-metrics]]); this paper makes the same argument at the level of *evaluation methodology* for intrusion detection. It is also the paper that best answers "should I believe a published NID result?" — the answer it gives is "only if the paper measured the things that deployment depends on".

---

## Paper 2 — HyperVision

**Fu, Li, Xu.** *Detecting Unknown Encrypted Malicious Traffic in Real Time via Flow Interaction Graph Analysis.* NDSS 2023 (Network and Distributed System Security Symposium, San Diego, 27 Feb – 3 Mar 2023). DOI 10.14722/ndss.2023.23080. Slide URL: https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023_s80_paper.pdf

**Research question.** Internet traffic is widely encrypted, and attackers exploit that to conceal malicious behaviour. Because encrypted malicious traffic has feature statistics similar to benign flows, it evades traditional detection; and because existing encrypted-traffic detectors are *supervised*, they depend on prior knowledge of known attacks and labelled datasets. The open problem the paper names: **detecting unknown encrypted malicious traffic in real time, without prior domain knowledge**.

**Method.** HyperVision is a real-time **unsupervised** ML detection system. It builds a compact in-memory graph over traffic flows and uses the graph's *structural* features — connectivity, sparsity and statistical properties — rather than features of specific known attacks. It then detects abnormal interaction patterns via an unsupervised graph-learning method. The paper also establishes an information-theory model showing that the information preserved by the graph approaches the ideal theoretical bound.

**Headline finding.** On real-world experiments with **92 datasets, including 48 attacks with encrypted malicious traffic**, HyperVision achieves **at least 0.92 AUC and 0.86 F1**, significantly outperforming state-of-the-art methods; **more than 50% of the attacks in the experiments evade all of those methods**. Operationally it sustains at least **80.6 Gb/s detection throughput** with an **average detection latency of 0.83 s**. The justification for a flow-interaction view is that multi-step attacks produce flow-interaction footprints distinct from benign interaction patterns even when a single flow looks benign.

**Why it matters here.** Two direct links to the course. First, it is the *unsupervised* counterpart to the supervised credit-card workflow in [[ml-learning-paradigms]] — the point where labels run out. Second, its headline metrics are AUC and F1, not accuracy, and it is evaluated on *AUC* — the quantity [[roc-curve]] is about — with 48 attacks whose individual flows are indistinguishable from benign traffic. It is also the most *system* paper of the three: throughput and latency are reported next to detection quality, which is exactly the "pragmatic" concern of paper 1.

---

## Paper 3 — The Emperor has no Clothes

**Jacobs, Beltiukov, Willinger, Ferreira, Gupta, Granville.** *AI/ML for Network Security: The Emperor has no Clothes.* ACM CCS 2022 (SIGSAC Conference on Computer and Communications Security, Los Angeles, 7–11 Nov 2022). DOI 10.1145/3548606.3560609. Slide URL: https://sites.cs.ucsb.edu/~arpitgupta/pdfs/trustee.pdf (also available at https://dl.acm.org/doi/abs/10.1145/3548606.3560609 and https://trusteeml.github.io/)

**Research question.** Many research efforts propose ML-based solutions that detect complex patterns in network traffic, but network operators are reluctant to deploy black-box models because they cannot see *how* the models decide. The paper asks: how can an operator determine whether a deployed model is actually trustworthy, i.e. whether its success comes from essential structure in the data or from accidental inductive biases?

**Method.** The paper names the failure mode **underspecification** — "the failure to specify a model in adequate detail" — and identifies three concrete instances: **shortcut learning**, **spurious correlations**, and **vulnerability to out-of-distribution samples**. Its artefact is **Trustee** (TRUSt-oriented decision TreE Extraction): it takes an existing black-box model plus its training dataset and returns (a) a high-fidelity, low-complexity **decision tree** that explains the black box, and (b) a **trust report**. The tree is optimised for a three-way balance of *fidelity* to the black box, *complexity* (size and explicitness of the rules, checked against operator domain knowledge) and *stability* (rules must not flip depending on which samples were used to select them — implemented by choosing the candidate tree with the highest mean agreement). Evaluations use published, fully reproducible ML models.

**Headline finding.** Using Trustee on reproducible published models, practitioners can identify those three instances of underspecification — evidence of shortcut learning, of overfitting / reliance on spurious correlations, and of inability to generalise out of distribution. The trust report points at which components of the ML pipeline (training data, model selection) need to change.

**On the framing of the title.** The "emperor has no clothes" is the paper's ironic verdict on a *state of trust*, not a claim that ML does not work. Read precisely, the paper says the operators' reluctance to deploy black-box network-security ML is *justified* — the models are "naked" because nobody can inspect them — and then contributes the tool for putting clothes on them. The paper is a diagnostic-and-remediation paper, not a "ML for network security is oversold" paper. The oversold claim would be a straw man: the paper's own conclusion is that practitioners can use Trustee to *establish* that a model generalises as expected, which is the opposite of dismissing the field. If you present this paper, attribute the scepticism about *black-box deployment* to it, and do not present it as "ML does not work for network security".

**Why it matters here.** It is the direct answer to the L2/L3 habit of reporting a single accuracy number. The credit-card model in [[lab-1-basics]] scores 99.92% accuracy — and nothing in that number says whether the model is using a spurious correlation, a shortcut, or a distribution it has never seen. Trustee's output is a *readable rule set* that an operator can audit, which is the same demand the course's metrics discussion makes: a number nobody can interrogate is not yet a result you can deploy.

---

## Comparison: what the three disagree about

| | Paper 1 (SoK, EuroS&P 2023) | Paper 2 (HyperVision, NDSS 2023) | Paper 3 (Emperor, CCS 2022) |
|---|---|---|---|
| **Question it answers** | How should ML-for-NID papers be evaluated so the value is estimable? | How can *unknown* encrypted malicious traffic be detected in real time? | How can an operator tell whether a black-box model is trustworthy? |
| **Evidence it uses** | Re-evaluation of existing methods over hundreds of configs, several adversarial scenarios, 4 hardware platforms + practitioner user study | 92 real-world datasets, 48 encrypted attacks, comparison against state of the art, throughput and latency measurements | Reproducible published models, tree extraction with fidelity/complexity/stability, trust reports |
| **Headline number** | qualitative: literature "hardly allows" estimation of value | ≥ 0.92 AUC, ≥ 0.86 F1, > 50% of attacks evade all baselines, 80.6 Gb/s, 0.83 s latency | not a single metric: a decision tree + a trust report |
| **Position on the field** | sceptical of *current evaluation practice*, constructive (proposes and runs the alternative) | optimistic and ambitious — pushes detection to where labels do not exist | sceptical of *uninspectable deployment*, constructive (proposes Trustee) |
| **Key concept for the course** | pragmatic assessment | unsupervised detection, flow interaction graph, AUC | underspecification, shortcut learning, spurious correlation, o.o.d. |

**Where they agree.** All three assume ML-based network security is worth deploying and ask what it would take to believe it: paper 1 that the evaluation measures deployment-relevant factors, paper 2 that the detection survives attacks nobody labelled, paper 3 that the model can be shown to generalise.

**Where they disagree.** Paper 1 argues the *evaluation literature* is inadequate; papers 2 and 3 are examples of the better practice paper 1 argues for — paper 2 measures hardware and latency, paper 3 measures fidelity and inspectability. Paper 2 is the only one that assumes the model will run; paper 3 is the only one that assumes the model may be broken and looks for evidence. Paper 1 and paper 3 also differ in locus: the SoK indicts the research community's method, while the CCS paper indicts the *operator's* ability to see inside a model, and offers a tool rather than a methodology.

---

## What a good 20-minute talk of each must cover

**For paper 1:** the question (why practitioners distrust NID ML) and the answer (evaluation ignores deployment factors such as hardware); the definition of pragmatic assessment; the scale of the re-evaluation (hundreds of configurations, four hardware platforms, adversarial scenarios); the user study with practitioners; and one concrete example of a factor that changes the ranking of methods. Finish on the "So what": for someone about to use a published NID result, here is the checklist of what to look for.

**For paper 2:** why encryption breaks both signature and supervised-ML detection; why a *single* flow is not enough and flow *interaction* is the signal; how the compact in-memory graph is built and why the graph structural features (connectivity, sparsity, statistics) generalise to unknown attacks; what "unsupervised" buys and what it costs; the numbers (≥ 0.92 AUC, ≥ 0.86 F1, > 50% of attacks evading all baselines, 80.6 Gb/s, 0.83 s); and the information-theory bound. Be ready to say what "detecting unknown attacks" means operationally — an anomaly score, not a label.

**For paper 3:** the operational problem (operators will not deploy what they cannot read); underspecification defined precisely; the three instances (shortcut learning, spurious correlations, o.o.d. vulnerability); how Trustee works (extraction, the fidelity/complexity/stability objective, the mean-agreement stability heuristic); the trust report and how it points at pipeline components; and one case study. Close by returning to the title's irony correctly — the paper is not saying ML fails, it is saying unverified deployment is naked.

**Common to all three:** define the terms you use (NID, encrypted traffic, o.o.d., fidelity), never show a metric without saying which class it is about, and connect to the course's own examples — the credit-card model's 99.92% accuracy with 0.68 recall in [[lab-1-basics]] is a good illustration of paper 3's problem statement, and the slides' "accuracy on imbalanced data" trap is paper 1's target.

---

## How to prepare

1. **Read the abstract and the introduction of the real paper, and the conclusion.** For paper 2, the PDF at the NDSS link is openly readable; for paper 3, the author-hosted PDF is open; for paper 1, the arXiv PDF is open. Do not present from the abstract alone.
2. **Pick one message and three supporting slides.** 20 minutes is about 15 slides; a paper read out loud is 20 minutes of nobody listening.
3. **Prepare one number per claim.** For each headline claim, have the exact figure and its conditions (which dataset, which metric, which class).
4. **Prepare the counter-argument.** Each paper is criticisable: paper 1's re-evaluation is itself a big experiment with its own scope limits; paper 2's "unknown attacks" are still from a curated dataset of 48 attacks; paper 3's fidelity is fidelity *to the black box*, which a broken model faithfully explains.
5. **Rehearse against the clock**, and leave the last 2–3 minutes for questions. The most common failure here is spending 18 minutes on the method and 2 on the finding.
6. **Check the date.** The slide says Nov 3 **or** Oct 29 — confirm your slot with the lecturer before you build the slide deck.

---

## Open questions

- **Which slot applies to me?** The slide says "on Nov 3 (or Oct 29)" without saying what distinguishes them. Ask.
- **Slide 36 says "20 minutes"** — unclear whether that includes questions. Plan for 18 minutes of material.
- **Do the three papers agree on a threat model?** They use different datasets, different traffic views (packet-level, flow-level, encrypted-flow) and different notions of a "detection". A talk that only compares their headline numbers would be misleading; the comparison has to be about questions and evidence.
- **Does any of them evaluate a model trained on the credit-card-style tabular data?** None of the three, as far as the abstracts show — the gap between the course's toy tabular example and real intrusion detection is not bridged by any of the assigned papers.
- **No paper here reports a "solved" claim**, and the abstracts do not say how their results were validated against each other. Whether Trustee-style auditing has been applied to HyperVision-style models is not visible from the abstracts.
