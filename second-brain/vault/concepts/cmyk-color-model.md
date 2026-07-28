---
title: "CMYK Color Model"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-models-overview]
---

## One-line Summary
CMYK is a subtractive colour model using Cyan, Magenta, Yellow, and Key (Black) ink channels, forming the technical basis of four-colour printing.

## Core Intuition
Inks absorb (subtract) light rather than emit it. Cyan ink absorbs red, magenta absorbs green, yellow absorbs blue. Combining all three theoretically yields black, but real inks produce muddy brown, so a separate K (black) channel is added for dark tones and sharpness.

## Formal Definition / Statement
- Subtractive colour model with four channels: C, M, Y, K
- Each channel typically in range [0%, 100%]
- Relationship to RGB (idealized): C = 1−R, M = 1−G, Y = 1−B
- K = min(C, M, Y) in undercolor removal; CMY values adjusted accordingly
- Complementary to RGB: cyan ↔ red, magenta ↔ green, yellow ↔ blue

## Key Properties / Complexity
- The CMYK gamut is typically smaller than RGB gamut — monitors can reproduce highly saturated colours that printers cannot
- Different paper types and inks yield different gamuts
- Required for physical reproduction (books, posters), not for screen display

## Worked Example
**To print a green leaf: the printer applies high cyan and yellow ink (absorbing red and blue light), reflecting green.** For dark shadows, the K channel adds black ink rather than over-saturating with CMY.

## Common Pitfalls
- Assuming CMYK = "just invert RGB" — real conversion depends on ICC colour profiles
- Ignoring that the CMYK gamut is strictly smaller than RGB, so clipping occurs for saturated colours

## Connections
- Complementary to [[rgb-color-model]]
- Gamut comparison shown in [[color-gamut]] diagrams
- Less relevant for multimedia databases (digital domain) but critical for print output

## Open Questions
- How should multimedia databases handle gamut mapping between RGB and CMYK?
