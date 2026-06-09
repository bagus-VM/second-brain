---
title: "Multimedia Definition"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Multimedia is any combination of digitally manipulable media types (text, sound, image, animation, video), where a "medium" is ==classified along axes of perception, representation, presentation, storage, and transmission (MHEG/ISO)==.

## Core Intuition
The word "multimedia" is deceptively simple — "multi" + "medium." But "medium" itself is overloaded. The MHEG standard (ISO) disambiguates by classifying media along five axes: how we *==perceive==* it (sight, hearing), how it's ==*represented* internally== (formats), how it's *==presented==* (screen, speakers), how it's *==stored==* (disk, paper), and how it's *==transmitted==* (cable, fiber). Multimedia then means combining media across at least one of these axes. The stricter academic definition (Steinmetz) requires mixing both [[media-types-discrete-continuous|discrete and continuous media]] with some independence between them; the looser practical definition accepts any digital media combination.

## Formal Definition / Statement
- **MHEG Medium classification** (ISO): A medium is a means of distributing and presenting information, classified by perception, presentation, representation, storage, and transmission.
- **General multimedia**: Any combination of digitally manipulable types of media (text, sound, image, animation, video).
- **Strict multimedia**: Requires mixing of both continuous and discrete media with a significant degree of independence between them.

## Key Properties
- **Interactivity**: User controls what is delivered and when (not passive consumption).
- **Linear vs Non-linear**: Linear = single continuous flow (film, radio); non-linear = navigable structure (games, hypermedia).
- **Hypermedia**: Interactive multimedia where elements are linked and navigable (e.g., web pages).
- **Digital-first**: Delivered through web, apps, streaming, AR/VR.
- **AI integration**: Modern multimedia adapts to user behavior (personalized feeds, adaptive learning).
- **Cross-platform**: Accessible on phones, tablets, VR headsets, smart TVs.

## Worked Example
An insurance company's accident file is a multimedia object combining:
- Photographs of the accident scene (discrete, visual)
- Structured text forms (discrete, textual)
- Audio recordings of witness interviews (continuous, auditory)
- Written reports (discrete, textual)

These are independent media objects linked together — satisfying the strict definition.

## Common Pitfalls
- Equating "multimedia" with "video." Multimedia requires *multiple* media types combined.
- Thinking "discrete" and "continuous" refer to the digital encoding. They refer to the *presentation* experience — text *appears* time-independent to the user even though it's stored as digital data.
- Confusing the medium of perception with the medium of representation. A JPEG image is perceived visually (perception) but represented as compressed pixel data (representation).

## Connections
- [[media-types-discrete-continuous]] — discrete vs continuous media classification
- [[multimedia-system]] — what makes a full multimedia system
- [[multimedia-database-intro]] — how multimedia data is managed in databases
- [[data-streams]] — how continuous media is transmitted over networks

## Open Questions
- **RESOLVED:** How does the MHEG classification interact with modern container formats (e.g., MP4)?
	  - An MP4 container holds multiple media streams (video, audio, subtitle tracks). Each stream is classified independently via MHEG's five axes. The container itself is not a medium; it's a physical storage wrapper around multiple media. Example: H.264 video stream (continuous, visual), AAC audio stream (continuous, auditory), timed text subtitles (discrete, visual) — three separate media bundled in one MP4 file.
- **RESOLVED:** Where do interactive 3D models (e.g., WebGL, glTF) fit in the traditional media taxonomy?
	  - glTF is a single visual medium (not multimedia by itself). It encodes geometry, textures, and animations in a complex representation, but all are perceived visually. Multimedia occurs when glTF is combined with a different medium — typically audio (soundtrack, narration), which adds auditory perception. Interactivity is orthogonal to multimedia classification; it describes user control over delivery, not the combination of media types. Key insight: Multimedia requires *different perceptions* (visual + auditory), not just multiple data components within one perception modality.
- **NEW:** If a WebGL scene includes procedural audio synthesis (audio generated in real-time based on user interaction with the 3D model), does this count as multimedia? Why or why not? 
	- it does count as a multimedia because it has multiple medium of perception (hearing + eyesight)
