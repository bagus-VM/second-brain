---
title: "Representation Learning"
tags: [concept, deep-learning, semester-2]
course: "Introduction to Deep Learning"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[machine-learning-basics]]"]
---

## One-line Summary

Representation learning is machine learning in which the features are not handed over but learned from data; deep learning is the part of it that learns those features through many stacked nonlinear layers.

## Core Intuition

A conventional machine learning pipeline has two stages: a human builds the features, then an algorithm learns a mapping from those features to an output. The second stage is the machine learning. The first stage is engineering, and it is where most of the effort goes. Good features are often not directly contained in the raw data — they have to be constructed, and the construction does not generalise to new tasks.

Representation learning removes the first stage from the human's desk. The algorithm learns the features as well as the mapping. In the formulation of Goodfellow et al. (2016, *Deep Learning*, Chapter 1), one "use[s] machine learning to discover not only the mapping from representation to output but also the representation itself". Bengio et al. (2013, *Representation Learning: A Review and New Perspectives*, IEEE TPAMI 35(8)) put the payoff first: "learning representations of the data that make it easier to extract useful information when building classifiers or other predictors".

The lecture's nesting diagram places the subfields inside one another: deep learning is a sub-field of representation learning, which is a sub-field of machine learning, which is a sub-field of artificial intelligence. The professor is blunt about the naming: "Deep Learning is a buzzword! The term 'deep learning' was/is a 'marketing trick'." What was called deep learning used to be called "multilayer artificial neural networks" or "multilayer perceptrons" — the same objects under a new label.

Deep learning is the deep end of that nesting, not a separate idea. Each layer in the network is a function that transforms the last representation into a new representation of the input data; many layers produce a cascade of layers building on top of each other. Zhang et al. (2018, *On Definition of Deep Learning*, WAC) give the definition the lecture quotes: a class of machine learning algorithms that "use a cascade of multiple layers of nonlinear processing units for feature extraction and transformation" and "learn multiple levels of representations that correspond to different levels of abstraction; the levels form a hierarchy of concepts".

## Formal Definition / Statement

Let $\varphi$ be a representation function that maps raw inputs to features, and $g$ the model that maps features to outputs. With learned parameters $\theta$ for $g$ and learned parameters $w$ for $\varphi$, the composite model is

$$y = f(x, \theta) = g(\varphi(x), w)$$

Representation learning means learning *both* $g$ and $\varphi$ from data, rather than fixing $\varphi$ by hand and learning only $g$.

**The four paradigms of "Where does learning happen?"** The lecture arranges the whole field along one axis — how much of the pipeline is learned from data:

| Paradigm | Output is produced by | Features are |
|---|---|---|
| Rule-based systems | a hand-designed program | hand-designed |
| Classic machine learning | a mapping from features to output | hand-designed |
| Representation learning | a mapping from features to output | learned from data |
| Deep learning | a mapping from features to output | more abstract features, learned from data, via more layers |

Adapted from Goodfellow, Bengio, Courville (2016), Fig. 1.5.

**Artificial intelligence as the outer frame.** AI is "Intelligence exhibited by machines or software". The subfields the lecture lists: logic and reasoning, knowledge representation, automated planning and scheduling, and machine learning.

**Feature engineering is the cost representation learning removes.** Hand-constructed features are "time-consuming and labor-intensive" and "often not scalable". Deep learning constructs features automatically from lower-level features, with artificial neural networks.

**The critique to keep in mind.** Gary Marcus, quoted at length in the lecture: such techniques "lack ways of representing causal relationship (...), have no obvious ways of performing logical inferences, and they are also still a long way from integrating abstract knowledge, such as information about what objects are, what they are for, and how they are typically used." The strongest AI systems, he argues, "use techniques like deep learning as just one element in a very complicated ensemble of techniques, ranging from the statistical technique of Bayesian inference to deductive reasoning."

## Key Properties

- **The learned feature pipeline is part of the model.** $\varphi$ has parameters $w$ learned by the same optimiser that learns $g$'s parameters $\theta$. Nothing stops the optimiser from making $\varphi$ useless — and if the loss is minimised well, it will not.
- **Abstraction is a hierarchy, not a metaphor.** Each layer consumes the previous layer's output. "Deep" is a statement about the number of stacked nonlinear transformations, not about semantic depth.
- **Representation is a choice, and choices are not neutral.** The lecture's "Representation matters" slide shows the same point in polar coordinates and in Cartesian coordinates. Which coordinates you use determines which functions are easy to express and which are not; a learned representation is a choice of coordinates made by the data rather than by the designer.
- **Feature engineering scales badly, representations scale with data.** The lecture's framing is economic: hand-crafted features cost human time per task, learned features cost compute per run.
- **The term is marketing.** "Deep learning" names a sub-field, not a method. The honest description of the objects is "multilayer artificial neural networks" / "multilayer perceptrons".
- **The field is application-driven.** The lecture's closing note on the section: deep learning "is much driven by practical applications", "practical success is often valued more than theory and rigor", and — with a question mark that belongs in your notes — "more engineering discipline than science?"

## Worked Example

**Learned representations, MNIST.** The lecture shows the same handwritten digit represented differently in each layer of a small CNN trained by the professor himself on MNIST: 2 epochs, 96% test accuracy, all 60,000 training images. The point of the slide is what is *absent*: "No feature was designed by hand: all were learned from 60,000 training images". The slide does not say what any individual layer responds to — it says only that the same digit is represented differently in each layer, and that nothing was designed by hand. You did not specify what the layers detect; the error signal specified it.

**Representation matters.** Take one point in the plane. In polar coordinates it is a pair $(r, \theta)$; in Cartesian coordinates it is a pair $(x, y)$. Nothing about the point changed. What changed is the shape of the functions that are easy to write down in that coordinate system: a circle is trivial in one and awkward in the other.

**Where the learning sits, side by side.** For a hand-crafted pipeline: hand-designed features → mapping from features → output, with the bottom arrow labelled "hand-designed". For deep learning the same three boxes appear, but the bottom arrow reads "simple features" and the middle one "more abstract features (more layers)", and both are labelled "learned from data". The pipeline is identical in shape; the label under the first arrow is what changed the field.

## Common Pitfalls

- **Treating "deep learning" as a distinct algorithm family rather than a sub-field of representation learning.** The lecture's diagram is the correction: it sits *inside* representation learning, not beside it.
- **Confusing a representation with a feature.** A feature is one number you chose; a representation is a whole coordinate system or intermediate space, and it may have as many dimensions as the input.
- **Believing the learned representation is interpretable by default.** A learned representation is optimised for prediction, not for human legibility. The Marcus critique points at the gap between statistical success and reasoning.
- **Handing the question "is it deep learning?" back as a yes/no answer.** The naming is a branding decision (2006, Hinton et al., *Training Deep Belief Networks*: "intentional re-branding", "no single new invention", "many small improvements and scaling to large data"). The technical content is the cascade of learned nonlinear transformations.
- **Underestimating the economics.** "Hand-crafted features are time-consuming and labor-intensive" is an argument about the cost of a pipeline, and it is the argument that won, not the argument about elegance.
- **Forgetting the outer frame.** Deep learning is one sub-field of machine learning, which is one sub-field of AI, alongside logic and reasoning, knowledge representation, and automated planning and scheduling. Treating it as the whole of AI is a category error the lecture explicitly stages with the Marcus quote.

## Connections

- [[machine-learning-basics]] — the outer layer of the nesting: representation learning is a sub-field of machine learning, and the lecture's four paradigms only make sense against the definition of learning from training data.
- [[feature-extraction]] — the hand-crafted counterpart; comparing the two isolates exactly what representation learning removes from the pipeline.
- [[feature-vector]] — the algebraic object a representation produces; the difference between a single feature and a feature *vector* is the difference between classic ML and representation learning.
- [[deep-learning-history-timeline]] — the 2006 rebranding and the 2012 breakthrough are the historical reason the field is discussed as a separate thing at all.
- [[pytorch-tensors-and-autograd]] — the mechanism: `nn.Linear` layers plus autograd are how $\varphi$ and $g$ get their parameters optimised together.
- [[neural-network-training-loop]] — the loop that fits both the representation and the model, since every layer's weights are just more parameters.
- [[deep-learning-course-roadmap]] — where this concept sits in the course: the abstraction is introduced in week 1 and cashed out in weeks 5–8.

## Open Questions

- The lecture's "Representation matters" slide credits the deeplearningbook slides and a Glassner visual approach, but the concrete worked example of why one coordinate system helps and another hurts is only shown, not argued. Which property of the data does the optimiser actually exploit when it picks a representation?
- Marcus's critique names three gaps (causal relations, logical inference, abstract knowledge). The lecture offers no answer to whether these are engineering gaps, architectural gaps, or definitional — and the "practical success is often valued more than theory and rigor" note sits uncomfortably close to that question.
- If a representation is learned to make classification easy, the criteria for "easy" are fixed by the loss function. Whether a representation learned under a regression loss transfers to a classification task is not addressed anywhere in the lecture.
- The nesting diagram implies clean containment, yet the Marcus quote describes the strongest systems as ensembles in which deep learning is one element. Which is the better model of practice is left open.
