---
title: "MPEG Video Compression (MPEG-1/2)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lossless-vs-lossy-compression, transform-coding, jpeg-compression-pipeline]
---

## One-line Summary
MPEG video compression combines intra-frame coding (JPEG-like DCT within each frame) with inter-frame coding (motion-compensated prediction between frames) using I, P, and B frames organized in Groups of Pictures (GOPs).

## Core Intuition
Video is a sequence of frames with massive temporal redundancy — consecutive frames are nearly identical except for object motion. Rather than encoding each frame independently (like Motion-JPEG), MPEG exploits this by encoding only the *differences* between frames. A reference frame (I-frame) is coded fully (like JPEG), then subsequent frames (P-frames, B-frames) are predicted from it using motion vectors. Only the prediction error (residual) needs to be stored, dramatically reducing the bitrate.

## Formal Definition / Statement
MPEG-2 compression uses three coding types in a **Group of Pictures (GOP)**:

**I-Frame (Intra-coded)**: Coded independently, no reference to other frames. Uses JPEG-like pipeline: color space conversion → subsampling → DCT (8×8 blocks) → quantization → RLE → Huffman. Serves as random access point and limits error propagation.

**P-Frame (Predictive)**: Coded using motion-compensated prediction from the preceding I or P-frame. For each macroblock (16×16), the encoder searches for the best matching block in the reference frame. Only the motion vector + residual (difference) are stored. Can also contain intra-coded blocks if no good match exists.

**B-Frame (Bi-directional)**: Coded using both preceding AND following I or P-frames as references. Can reference two frames for better prediction. Highest compression but most complex to encode/decode. Not used as reference by other frames.

Typical GOP structure: `I-BB-P-BB-P-BB-P-BB-I-BB...`

**Motion Estimation**: For each macroblock, find the best matching block in the reference frame within a search window. Metrics:
- MSE = ΣΣ(Currentᵢⱼ - Refᵢⱼ)² / N²
- SAE = ΣΣ|Currentᵢⱼ - Refᵢⱼ|

## Key Properties
- **GOP structure**: I-frame starts each GOP; all frames in GOP depend on the first I-frame
  - GOP length: typically 10–250 frames (DVB: 50 frames = 2 seconds)
  - Smallest unit for random access
  - Limits error propagation to one GOP
  - Decoder can discard previous frames at GOP boundary
- **Slices**: macroblocks grouped into independently coded slices — avoid error propagation, enable parallel processing
- **Macroblocks**: 16×16 pixel blocks; each can be intra- or inter-coded independently
- **Motion vectors**: specify displacement of reference block; can reference past (P) or future (B) frames
- **Rate control**: encoder decides whether inter-coding (MV + residual) or intra-coding is more efficient for each block
- **MPEG-1**: VCD quality at ~1.5 Mbit/s. MPEG-1 Layer 3 = MP3 (audio part)
- **MPEG-2**: broadcast quality (NTSC) at 4–6 Mbit/s, HDTV at 15–30 Mbit/s. Supports interlaced video, multiple profiles

## Worked Example
Encoding a sequence of 4 frames with GOP structure I-P-P-I:

**Frame 1 (I-frame)**: Fully encoded like JPEG. Suppose it takes 100 KB.

**Frame 2 (P-frame)**: Encoder divides into 16×16 macroblocks. For each macroblock, searches reference frame (Frame 1) for best match:
- Block at (10,20): best match at (12,21) in Frame 1 → motion vector (2,1), small residual → inter-coded
- Block at (50,50): no good match (new object enters) → intra-coded (like JPEG)
- Result: motion vectors + residuals ≈ 20 KB (much smaller than 100 KB)

**Frame 3 (P-frame)**: Same process, referencing Frame 2. Result ≈ 25 KB.

Compression: Raw 4 frames ≈ 400 KB → compressed ≈ 145 KB (ratio ~2.8:1 just from inter-frame coding; combined with DCT quantization, much higher ratios are achieved).

Comparison of video compression (352×288, 25 fps, 12 seconds):
| Method    | Size    | Ratio |
|-----------|---------|-------|
| Raw RGB   | 87 MB   | 1:1   |
| Raw 4:2:0 | 43.5 MB | 2:1   |
| MJPEG     | 9.6 MB  | 9:1   |
| MPEG-1    | 5.3 MB  | 16:1  |
| MPEG-4    | 4.2 MB  | 20:1  |
| H.264     | ~2 MB   | 43:1  |

## Common Pitfalls
- Confusing I-frames, P-frames, and B-frames — I-frames are independent, P-frames reference past, B-frames reference both directions
- Forgetting that B-frames are never used as references by other frames (they don't propagate errors)
- Thinking motion estimation is specified by the MPEG standard — the standard specifies the *syntax* (and thus decoding), but encoding algorithms are freely chosen
- Overlooking that MV + residual can sometimes be *larger* than intra-coding — the encoder must decide per block
- Not understanding GOP as the unit of random access — seeking to an arbitrary frame requires decoding from the nearest I-frame

## Connections
- [[lossless-vs-lossy-compression]] — MPEG uses both lossy (DCT quantization, motion compensation) and lossless (entropy coding) stages
- [[transform-coding]] — MPEG intra-coding uses 8×8 DCT, same as JPEG
- [[jpeg-compression-pipeline]] — I-frame coding is essentially JPEG compression
- [[h264-avc-video-compression]] — H.264 improves on MPEG-2 with smaller blocks, better prediction, CABAC
- [[entropy-coding-huffman-arithmetic]] — MPEG uses Huffman coding for DCT coefficients
- [[run-length-encoding]] — RLE on zero-valued AC coefficients after quantization
- [[video-formats-container-vs-codec]] — MPEG-1/2 are codecs; containers include MPG, VOB, TS
- [[video-frame-rate-resolution]] — MPEG-2 supports various resolutions and frame rates

## Open Questions
- How does the choice of GOP length affect compression efficiency vs. random access capability?
- What are the tradeoffs between exhaustive and fast motion estimation algorithms?
- How do modern codecs (H.265, AV1) improve on MPEG-2's motion compensation?
