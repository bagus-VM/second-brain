---
title: "Video Frame Rate and Resolution"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A video's frame rate (frames per second) and resolution (pixel dimensions) determine its temporal smoothness and spatial detail, with the choice between progressive and interlaced scanning affecting motion portrayal.

## Core Intuition
Video is a sequence of still images (frames) displayed rapidly enough to create the illusion of motion. Frame rate controls temporal resolution (how smooth motion appears), while spatial resolution controls image detail. The interlaced vs. progressive distinction is historical: interlacing was invented to double perceived frame rate without doubling bandwidth by sending alternating rows (fields) — but it introduces artifacts with fast motion. Modern displays prefer progressive scanning.

## Formal Definition / Statement
- **Frame rate**: Number of frames displayed per second (fps). Standard values: 24 fps (cinema), 25 fps (PAL TV), 29.97/30 fps (NTSC TV), 50/60 fps (high frame rate / HDTV).
- **Progressive scan (p)**: Each frame is captured/displayed as a complete image in a single pass. E.g., 720p = 1280×720 pixels, progressive.
- **Interlaced scan (i)**: Each frame is split into two *fields* — field 1 contains odd-numbered lines, field 2 contains even-numbered lines. Fields are displayed alternately. E.g., 1080i = 1920×1080 pixels, interlaced (50 half-images per second).
- **Spatial resolution**: Pixel dimensions (width × height). Determined by the video standard.

**Common resolutions:**

| Standard | Resolution | Frame Rate | Notes |
|----------|-----------|------------|-------|
| 576i (PAL) | 720×576 | 50 fields/s | DVD, DVB-S/T |
| 720p (HDTV) | 1280×720 | 60 fps | Blu-ray, DVB-S2 (HD Ready) |
| 1080p/i (Full HD) | 1920×1080 | 24/50/60p or 50/60i | Blu-ray, DVB-S2 |
| 2K (Digital Cinema) | 2048×1080 | 24 fps | Cinema projection |
| 4K (UHD) | 3840×2160 or 4096×2160 | 24–60 fps | Consumer and cinema |
| 8K (UHDTV) | 7680×4320 | 60 fps | Next-gen broadcast |

## Key Properties
- **Interlacing artifact**: Fast-moving objects appear with a "comb" or "staircase" effect because odd and even lines are captured at slightly different times (wrong alignment effect).
- **Temporal resolution vs. bandwidth**: Interlacing doubles perceived temporal resolution (50 fields/s vs 25 frames/s) using the same bandwidth — a clever analog-era optimization.
- **Film vs. video frame rates**: Cinema uses 24 fps (film look); PAL TV uses 25 fps; NTSC uses 29.97 fps (slightly off 30 for historical color TV compatibility reasons).
- **Deinterlacing**: Converting interlaced video to progressive for modern displays. Methods include line doubling, interpolation, and motion-adaptive algorithms.

## Worked Example
Calculating uncompressed video data rate for 1080p at 30 fps with 24-bit color:
- Resolution: 1920 × 1080 = 2,073,600 pixels/frame
- Bits per frame: 2,073,600 × 24 = 49,766,400 bits = ~5.93 MB/frame
- Data rate: 5.93 MB × 30 fps = **177.9 MB/s** ≈ **1.42 Gbps**

This is why compression (codecs) is essential — raw HD video at 30 fps produces over 1 Gbps of data.

## Common Pitfalls
- Confusing fields per second with frames per second: 1080i at "50i" means 50 *fields* per second = 25 *frames* per second, not 50 full frames.
- Assuming higher fps is always better: 24 fps gives a "cinematic" feel; 60 fps looks "too real" or "soap opera-like" to some viewers.
- Ignoring the difference between 29.97 fps and 30 fps: this tiny difference matters for audio-video sync in broadcast systems.
- Confusing resolution standards: "4K" can mean 3840×2160 (UHD-1, consumer) or 4096×2160 (DCI 4K, cinema) — different aspect ratios.

## Connections
- [[video-formats-container-vs-codec]] — frame rate and resolution define the raw video parameters; codecs compress this data
- [[video-hierarchy-shots-scenes]] — frame is the atomic unit of the video hierarchy
- [[shot-segmentation]] — shot detection algorithms operate on consecutive frames, sensitive to frame rate
- [[audio-sampling-nyquist-theorem]] — analogous concept: temporal sampling (video frames) vs. amplitude quantization
- [[multimedia-databases-lecture-03]] — image resolution (DPI/PPI) from lecture 3 is the spatial resolution of a single frame

## Open Questions
- How does frame rate affect shot segmentation accuracy — does higher fps help or hurt?
- What are the storage implications for a multimedia database handling 8K video at 60 fps?
- Is interlacing still relevant for modern content delivery, or has it been fully superseded by progressive scanning?
