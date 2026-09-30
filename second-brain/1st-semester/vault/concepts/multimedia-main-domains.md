---
title: "Multimedia Main Domains"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [multimedia-system]
---

## One-line Summary
Steinmetz's layered model organizes multimedia into four domains — Basics (encoding/sampling), System (QoS, processing, storage, communication), Services (synchronization, security, content analysis), and Usage (applications/UI) — from low-level signal processing to user-facing applications.

## Core Intuition
Multimedia is a big field. The Steinmetz model gives you a mental map: at the bottom are the fundamentals (how audio/video is digitized), then the system infrastructure (how it's stored and transmitted with quality guarantees), then services that build on that infrastructure (synchronization, security, content analysis), and finally the applications users actually see. Each layer depends on the ones below it. This structure also maps directly to the [[multimedia-database-intro|MMDBMS]] — which sits at the System and Services layers.

## Formal Definition / Statement
Four layers (bottom-up):

**1. Basics**
- Fundamental principles for processing digital audio/video data
- Nyquist-Shannon sampling theorem and Pulse Code Modulation (PCM)
- Techniques specialized per medium: audio technology (music, speech), video technology (based on digital TV)
- Also covers single images, graphics, animations, text
- Efficient, quality-preserving compression (MP3, JPEG, etc.)
- Goal: fully digital systems

**2. System**
- Central aspect: **Quality of Service (QoS)** — defined, controllable system behaviour with measurable parameters
- Three basic functionalities:
  - **Processing**: OS and programming environment provide abstracted hardware interfaces; abstraction via MM-OS, programming language, or OO class hierarchy
  - **Storage**: Specific storage devices; media managed by media servers or DBMS
  - **Communication**: High bandwidth + high reliability to meet time constraints (video streaming)

**3. Services**
Ready-to-use integrated functions for applications:
- **Communication**: Email, video conferencing, joint editing — must respect multimedia constraints
- **Synchronization**: Temporal relations between multimedia data items (e.g., games)
- **Security**: Measures to prevent attacks
- **Documents**: Structuring different media into a coherent "whole" (MM document)
- **Content analysis**: Considers semantics of contents; enables effective access and new application types

**4. Usage**
- Applications and user interfaces — the user-perceivable aspects
- MM-specific design considerations
- Examples: e-teaching, e-learning
- Growing areas: MM application development tools, project management for MM development
- Note: MM systems encompass more than just application development

## Key Properties / Complexity
- **Bottom-up dependency**: Each layer builds on the one below. You can't do content analysis without storage; you can't do storage without encoding.
- **QoS is the system layer's central concept**: It bridges technical implementation with user-perceivable quality.
- **Content analysis is the bridge to [[multimedia-database-intro|databases]]**: Extracting and indexing content features is what enables retrieval.
- **The model is descriptive, not prescriptive**: Real systems may blur layer boundaries.

## Worked Example
**Building a video streaming platform:**
1. **Basics**: Video encoded with H.265, audio with AAC — using sampling theorem and compression
2. **System**: Servers with sufficient storage, CDN for communication, QoS guarantees (buffering, adaptive bitrate)
3. **Services**: Synchronization of audio/video tracks, DRM for security, thumbnail generation for content analysis
4. **Usage**: Netflix-style UI with search, recommendations, playback controls

Each layer's design choices constrain and enable the layers above.

## Common Pitfalls
- Thinking the layers are separate systems. They're aspects of a single multimedia system — a video player touches all four layers simultaneously.
- Ignoring the Basics layer. Without understanding sampling, compression, and encoding, the higher layers are built on shaky foundations.
- Confusing "Services" with "Usage." Services are *infrastructure* functions (sync, security); Usage is the *user-facing* application layer.

## Connections
- [[multimedia-system]] — the System layer is where the multimedia system definition lives
- [[multimedia-database-intro]] — MMDBMS sits at the System/Services boundary
- [[data-streams]] — streaming is a System-layer communication concern
- [[media-types-discrete-continuous]] — Basics layer handles encoding of both media types
- [[multimedia-definition]] — the full definition informs all layers

## Open Questions
- How has cloud computing changed the System layer? Are processing/storage/communication now all "services"?
- Where does AI/ML fit in this model — primarily in Content Analysis (Services), or does it span multiple layers?
