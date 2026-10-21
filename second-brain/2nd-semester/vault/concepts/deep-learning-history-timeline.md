---
title: "A History of Deep Learning"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[representation-learning]]"]
---

## One-line Summary

Deep learning is eighty years of slow progress, one long winter, one rebranding in 2006, and a data-and-hardware-driven explosion from 2012 onwards.

## Core Intuition

The lecture's history section, summarised from Andreas Geiger's *Deep Learning* lecture 1, is not a
parade of famous papers. It is an argument about causes. Each breakthrough follows from something:
an architecture, a learning procedure, a dataset, a chip. Every entry in the chronology below is
the resolution of a specific obstacle.

The lecture also frames the field's character with a critical edge. Its slide "Application driven"
states that deep learning is "much driven by practical applications", that "practical success is
often valued more than theory and rigor", and asks "More engineering discipline than science?" That
question mark is the professor's, and it belongs in your notes alongside the dates.

## Formal Definition / Statement

**The early years.**

- **1943 - McCulloch and Pitts.** The first model for neural activation: a binary linear threshold
  neuron, +1 when $w^T x \geq 0$, -1 otherwise.
- **1958-1962 - Rosenblatt's Perceptron.** The first algorithm and implementation to train a single
  linear threshold neuron, optimising $E(w) = -\sum_{i \in \mathcal{M}} y_i\, w^T x_i$ over the
  misclassified $\mathcal{M}$.
- **1969 - Minsky and Papert, *Perceptrons*.** Several negative results, famously the XOR problem:
  simple perceptrons cannot learn many functions. The next decade was the (first) "AI Winter", with
  symbolic AI dominating the 70s and 80s.
- **1979 - Fukushima's Neocognitron.** A multilayer network with different cell types, the
  inspiration for modern CNNs.
- **1986 - Backpropagation.** Efficient calculation of gradients in a deep network w.r.t. the network
  weights, enabling gradient-based learning of deep networks. The idea is older (Kelley 1960,
  Linnainmaa 1970, Werbos 1982), but 1986 was the first empirical success and remains the main
  workhorse today (Rumelhart, Hinton and Williams, *Nature*, 1986).
- **1991 / 1997 - LSTM.** Hochreiter demonstrated the vanishing/exploding gradient problem in his
  1991 diploma thesis; that led to long short-term memory for sequence modelling in 1997, with
  feedback and forget/keep gates.
- **1998 - Convolutional Neural Networks.** Like the neocognitron but trained end-to-end with
  backpropagation: spatial invariance via convolutions and max-pooling, weight sharing to reduce
  parameters, tanh/Softmax activations, good MNIST results, but they did not scale up (yet).

**The name, the data, the hardware.**

- **2006 - Hinton et al., *Training Deep Belief Networks*.** The term "Deep Learning" arrives as an
  intentional re-branding: no single new invention, many small improvements and scaling to large
  data.
- **2009 - ImageNet.** More than 14 million images and 20,000 categories; the ILSVRC challenge used
  1.2 million training images and 1000 categories.
- **2009 / 2010 - GPU computation.** Raina and Ciresan train deep neural networks with GPUs; massive
  parallelism enables larger-scale computation.
- **2012 - AlexNet.** A deep CNN trained on GPUs wins ILSVRC, top-5 error 15.3% against 26.2% for
  the runner-up (Krizhevsky, Sutskever, Hinton, NIPS 2012).
- **2013 / 2014 - Word2Vec, GloVe.** Word representations trained self-supervised on a large text
  corpus, reusable for specific tasks with smaller training datasets (transfer learning), and the
  precursor of today's foundation models (the term coined in 2021).
- **Since 2014** deep learning dominates machine learning: first images, then texts, then networks
  and other complex data. 2016 brings WaveNet (speech and music), Style Transfer and AlphaGo, with
  3D deep learning following.
- **2017 / 2018 - Transformers and BERT.** Attention replaces recurrence and convolutions; BERT
  pre-trains language models on unlabelled text; GLUE brings superhuman performance on some
  language understanding tasks (paraphrase, question answering) - but computers still fail in
  dialogue.
- **2020 - GPT-3.** 175 billion parameters, a text-in/text-out interface, use cases from coding
  and poetry to blogging, news articles and chatbots, and controversial discussions.
- **2022 - Instruction Tuning and RLHF (InstructGPT).** A pretrained model only continues text; it does
  not follow instructions or behave like an assistant. InstructGPT closes that gap in three steps -
  supervised fine-tuning (imitating human-written answers), a reward model (predicting human
  preferences among ranked answers), and reinforcement learning (PPO for high predicted reward).
  Labelers preferred the 1.3B-parameter InstructGPT over the 175B-parameter GPT-3 (Ouyang et al.,
  NeurIPS 2022).
- **November 2022 - ChatGPT.** The first large language model with deep societal impact, reaching an
  estimated 100 million users within two months.
- **2023 - Competition.** GPT-4 (text and image input) against Claude and Gemini, with open-weight
  models Llama and Mistral; LLMs become a product category.
- **2024 - Multimodality.** GPT-4o (real-time speech, images, text), Sora (text-to-video), o1
  ("reasoning" by thinking longer before answering), Nobel Prizes for AI research, video with sound
  (Veo 3).
- **2025 - Reasoning and agents.** DeepSeek-R1, an open reasoning model trained with reinforcement
  learning, and agents that use tools, browse the web, and write and run code. Trends: RL
  post-training and test-time compute, a shift from chatting to acting, open models closing the gap.
- **2026 - Where Are We Now?** Reasoning is standard: models think (chain of thought) before
  answering, and more computation at answer time gives better results in math and science. Agents
  are in production (coding agents, computer use, multi-step workflows), and the length of tasks AI
  agents can complete has doubled roughly every 7 months (Kwa et al., METR, 2025). Open-weight models
  (DeepSeek, Qwen) are close to the frontier at much lower cost, with new frontier models every few
  weeks and massive investment in compute (International AI Safety Report 2026).
- **Recognition.** 2018 Turing Award to Bengio, Hinton and LeCun "for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing". 2024 Nobel Prize in Physics to Hopfield and Hinton "for foundational discoveries and inventions that enable machine learning with artificial neural networks". 2024 Nobel Prize in Chemistry to David Baker (computational protein design) and Demis Hassabis and John Jumper (protein structure prediction, AlphaFold). 2024 Turing Award to Andrew Barto and Richard Sutton (reinforcement learning). Two Turing Awards and two Nobel Prizes in six years - the field's arrival is institutional as well as technical.

## Key Properties

- **The winter was caused by a limitation, not a failure of the idea.** The perceptron could not learn XOR; the field survived because the remedy - multilayer networks trained by gradient descent - arrived seventeen years later, in 1986.
- **Architecture and procedure advance separately and then meet.** The neocognitron (1979) supplied convolutions; backpropagation (1986) supplied the training method; the combination produced CNNs (1998). The 1998 CNNs already had "good results on MNIST" but "did not scale up (yet)".
- **Data and hardware were the binding constraints.** The 2012 result was not a new architecture but a new compute budget - a hardware-and-data story as much as a modelling one.
- **Transfer learning is the through-line to foundation models.** Word2Vec and GloVe in 2013/2014 pretrained representations on large corpora; the 2021 term "foundation model" names the same idea at larger scale.
- **Capability and reliability move at different speeds.** GLUE brought "superhuman performance on some language understanding tasks", yet "computers still fail in dialogue"; the 2024 and 2025 slides carry hallucination, interpretability, robustness, alignment and regulation as unsolved.

## Worked Example

**The perceptron criterion, concretely.** The criterion $E(w) = -\sum_{i \in \mathcal{M}} y_i\, w^T x_i$ penalises only the misclassified examples $\mathcal{M}$. For a misclassified example, $y_i$ and $w^T x_i$ have opposite signs, so each summand is positive; for correctly classified ones the term is absent. Minimising $E$ pushes the weights towards separating the misclassified points - which is why the XOR problem stops the method: no single hyperplane separates the two classes of the XOR configuration.

**The 2012 margin, as a number.** A gap of roughly 11 percentage points, achieved with the same convolutional primitives as 1998 and a GPU instead of 1998-era hardware. The 1998 CNNs "did not scale up (yet)" - the constraint was never the architecture.

**The InstructGPT inversion, as a number.** A model roughly 134 times smaller was judged better by human raters. The gap between a base language model and a useful assistant was closed by three steps of human feedback, not by scale alone.

## Common Pitfalls

- **Reading the timeline as a sequence of genius strokes.** 2006 brought "No single new invention"; the breakthroughs came from "many small improvements and scaling to large data". That paper was about training deep belief networks - the term was the lasting contribution, and a rebranding is not an invention.
- **Attributing the 2012 breakthrough to architecture.** AlexNet's architecture was conventional; the differentiator was GPU training plus ImageNet. The non-architecture milestones - ImageNet (2009), the ILSVRC protocol, GPU training - are infrastructure, and without them the 2012 result is not reproducible.
- **Losing a decade to the "AI Winter".** It was not a gap but a decade of symbolic dominance; the neural network line continued underneath, and the vanishing/exploding gradient problem was demonstrated in 1991, six years before LSTM answered it.
- **Reading the modern slides as a straight line of progress.** The 2017/2018 slide pairs "superhuman performance on some language understanding tasks" with "computers still fail in dialogue", and the 2024/2025 slides carry hallucination, jailbreaks, deepfakes and regulation alongside the capabilities.

## Connections

- [[representation-learning]] - the concept the 2006 rebranding was selling; the history is that sub-field's rise.
- [[deep-learning-course-roadmap]] - where the course follows this arc: week 2 is tooling, weeks 5-8 the core, weeks 9-13 the architectures "in the order they were invented".
- [[word2vec-skip-gram]] - the 2013/2014 word embedding milestone; the first large-scale pretraining-and-transfer recipe.
- [[node-embeddings]] - the same idea on graph data, the "networks / other complex data" the lecture names as deep learning's third phase.
- [[n-gram-language-models]] — the pre-neural baseline that the 2017/2018 language-model milestones displaced.
- [[perplexity-and-entropy]] — the evaluation metrics for the language models that the 2020 and 2022 milestones produced.
- [[machine-learning-basics]] — the outer frame: the "AI Winter" only makes sense against the symbolic AI that displaced the perceptron.
- [[feature-extraction]] - the hand-crafted alternative to learned representations, and what the CNN era displaced.

## Open Questions

- Whether the 2012-2024 record is a theory of deep learning or a sequence of engineering results is unresolved by the slides.
- The timeline records the exponential growth in dataset sizes, model sizes and training compute (Epoch AI data via Our World in Data) but gives no account of what breaks when those curves stop. Whether scaling remains the dominant driver or is overtaken by RL post-training and test-time compute is unsettled.
- The 2026 slide cites the International AI Safety Report and METR's task-length doubling as evidence, but gives no method for reconciling a 7-month doubling rate with the "new frontier models every few weeks" pace.
- The current-challenges slide lists hallucination, interpretability, robustness, alignment, energy cost, data exhaustion, copyright, privacy and the EU AI Act without ranking them, and does not say which are research problems and which are regulatory or economic ones.
