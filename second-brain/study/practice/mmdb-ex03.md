---
title: "MMDB Exercise 3 — Color Models"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: Color Perception

1. Given the Spectral Power Distribution figure, roughly plot the SPD for: Daylight, incandescent bulb, mercury fluorescent bulb.
2. Plot a graph of the spectral sensitivities of the S, M and L cones in the human eye. For each cone mark the wavelength of maximum absorption.
3. What are Metamers?
4. A piece of paper when viewed under daylight or indoors under an incandescent bulb appears to be white in both cases, even though the irradiance differs (white light vs yellower light). Explain this phenomenon.

### Task 2: Color Models

1. What is a color model?
2. Describe the main properties of the following color models: RGB, CMYK, HSV.
3. Given a colour represented in RGB colour space as R=0.2, G=0.6, B=0.3, what is its representation in the CMYK and HSV colour models?

### Task 3: Color Spaces

1. What is the rationale behind the color difference when reducing video resolution to 240p?
2. How does the CIE Lab color space differ from CIE XYZ?

## Solutions

### Task 1: Color Perception

> [!note]- Solution
> **1.1) Spectral Power Distribution:** Daylight has a broad, relatively flat SPD across visible wavelengths. Incandescent bulb has a warm, red-heavy SPD (blackbody radiation peaking in infrared). Mercury fluorescent has sharp spectral peaks at specific wavelengths.
>
> **1.2) Cone sensitivities:** S-cones (short/blue, peak ~420nm), M-cones (medium/green, peak ~530nm), L-cones (long/red, peak ~560nm). All three overlap significantly.
>
> **1.3) Metamers:** Metamers are **colors** that have different **spectral power distributions** (wavelength compositions) but are perceived as identical by the human eye due to the trichromatic nature of vision. Types include light metamers, material metamers, and observer metamers.
>
> **1.4) Chromatic Adaptation:** Human visual system's ability to adjust to changes in illumination to preserve the appearance of object colors."

### Task 2: Color Models

> [!note]- Solution
> **2.1) Color model:** An abstract method for representing color information that makes use of the characteristics of the human vision system. Two types: additive and subtractive.
>
> **2.2) Main properties:**
> - **RGB (Additive):** 
> - Lights produce colors. 
> - Black=(0,0,0), White=(1,1,1). Primary: R, G, B. Secondary: Cyan, Magenta, Yellow. 
> - Used in monitors, TVs, projectors.
> 
> - **CMYK (Subtractive):** 
> - Pigments/dyes produce colors. 
> - White=(0,0,0), Black=(1,1,1). Primary: C, M, Y. K=Key (black) for deeper black and ink savings. Inversely related to RGB: C=1-R, M=1-G, Y=1-B. 
> - Used in printers.
> 
> - **HSV:** 
> - Hue (color, 0-360°), 
> - Saturation (0=gray, 1=full color), Value/Brightness (0=black, 1=white). Designed to approximate human color perception. 
> - HS and B treated separately.
>
> **2.3) Conversion of R=0.2, G=0.6, B=0.3:**
> - **CMYK:** C=1-0.2=0.8, M=1-0.6=0.4, Y=1-0.3=0.7, K=min(C,M,Y)=0.4 → adjusted: C=(0.8-0.4)/(1-0.4)=0.667, M=(0.4-0.4)/(1-0.4)=0, Y=(0.7-0.4)/(1-0.4)=0.5, K=0.4
> - **HSV:** W=min(0.2,0.6,0.3)=0.2. R'=0, G'=0.4, B'=0.1. Since R'=0: H=(0.1×120/0.5)+120=144°, S=(0.6-0.2)/0.6=0.667=66.7%, V=0.6=60%

### Task 3: Color Spaces

> [!note]- Solution
> **3.1) Color difference at 240p:** Video is stored in YCbCr color space. When resolution is reduced, the player may use incorrect conversion coefficients (e.g. BT.601 for SD vs BT.709 for HD), causing color shifts. The chroma subsampling also changes with resolution.
>
> **3.2) CIE XYZ vs CIE L\*a\*b\*:**
> - **CIE XYZ:** Additive, linear light color space useful for calculating color mixtures, but NOT perceptually uniform. Distance between two colors does not relate to how similar/different they appear. Chromatic adaptation not well represented.
> - **CIE L\*a\*b\*:** Oriented towards physiological properties of human color perception. Distance between colors accurately predicts perceived similarity. All colors chromatically adapted to D50 (5000K) for consistent comparison across conditions.

## Related Lectures

- [[multimedia-databases-lecture-03]]
- [[multimedia-databases-lecture-04]]
