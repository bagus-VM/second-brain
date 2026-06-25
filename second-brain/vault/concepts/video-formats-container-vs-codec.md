---
title: "Video Formats: Container vs Codec"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A video file format (container) defines the file structure and multiplexing of streams, while a codec defines the compression algorithm — the same container can hold video compressed with different codecs.

## Core Intuition
Think of a container like a shipping box and the codec like the way the contents are compressed inside. An AVI file (container) could contain video compressed with MPEG-1, MPEG-4, or even uncompressed video. The container handles multiplexing (combining video, audio, subtitles into one file), metadata, and seeking. The codec handles the actual compression and decompression of the media data. This separation is crucial: it means you can upgrade compression without changing the file format, and vice versa.

## Formal Definition / Statement
- **Container format** (file format): Defines the architecture/structure of a file — header data, stream interleaving, metadata storage, seeking information. Examples: MPG, VOB, AVI, ASF, MKV, MP4, WebM, MOV, FLV.
- **Codec** (coder-decoder): The compression/decompression algorithm applied to the media stream. Examples: H.264/AVC, H.265/HEVC, VP8, VP9, AV1, MPEG-1, MPEG-2.
- A container can hold streams encoded with *different* codecs (e.g., an MKV file might contain H.265 video + AAC audio + SRT subtitles).
- Some formats blur the line (e.g., MPEG can refer to both the container and the codec family).

## Key Properties
- **Container responsibilities**: multiplexing streams, storing metadata (duration, chapters), enabling seeking/random access, supporting subtitles and multiple audio tracks.
- **Codec responsibilities**: reducing file size through compression (lossy or lossless), encoding/decoding the actual pixel and audio data.
- **WebM**: Open standard by Google (BSD license). Uses VP8 video codec + Vorbis audio codec. Available as a free codec for the HTML5 `<video>` tag.
- **Common container-codec pairings**:
  - MP4 container + H.264 video + AAC audio (most common on the web)
  - MKV container + H.265 video + AAC/FLAC audio (flexible, open)
  - AVI container + various codecs (legacy Windows format)
  - WebM container + VP8/VP9 video + Vorbis/Opus audio (open web standard)

## Worked Example
A single video encoded two different ways:
1. `lecture.mp4` — MP4 container, H.264 codec (video), AAC codec (audio)
   - File size: 500 MB, good compatibility, hardware decoding support
2. `lecture.mkv` — MKV container, VP9 codec (video), Opus codec (audio)
   - File size: 350 MB, better compression, but less universal hardware support

Both play the same content. The container determines what streams can be bundled and how they're accessed; the codec determines quality-per-bit.

## Common Pitfalls
- Using "format" ambiguously — saying "MP4 format" could mean the container *or* H.264 codec. Always distinguish container from codec.
- Assuming a file extension tells you the codec — an `.avi` file could use almost any video codec.
- Confusing container compatibility with codec support — a device may support the MP4 container but not the AV1 codec inside it.
- Thinking MPEG is a single thing — MPEG-1, MPEG-2, MPEG-4 are different generations of compression standards, each with different capabilities.

## Connections
- [[video-frame-rate-resolution]] — the raw video data *before* codec compression has specific frame rates and resolutions
- [[video-hierarchy-shots-scenes]] — video content structure exists regardless of container/codec choice
- [[shot-segmentation]] — shot detection algorithms may work in compressed domain (using codec properties like macroblocks) or uncompressed domain
- [[audio-sampling-nyquist-theorem]] — audio streams are also encoded with codecs (e.g., AAC, MP3, Vorbis) and multiplexed in the container
- [[multimedia-database-intro]] — MMDBMS must handle video storage and streaming regardless of container/codec

## Open Questions
- How does the choice of container/codec affect video indexing and random access in a multimedia database?
- What are the tradeoffs between H.265/HEVC and AV1 in terms of compression efficiency vs. encoding speed?
- How do adaptive streaming protocols (HLS, DASH) relate to container formats?
