---
title: "Lecture 11 - Agentic Coding and Software Quality"
tags: [lecture, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[software-analyse-lecture-9]], [[software-analyse-lecture-10]], [[static-vs-dynamic-analysis]]
---

## One-line Summary
*AI coding agents can write and fix code autonomously, but they make quality assurance more important, not less.*

## Core Intuition
Agentic coding tools (like Claude Code) run autonomously: they read your codebase, make changes, run tests, and iterate. The promise is speed. The catch is that AI-generated code averages out to "good enough" but introduces subtle quality erosion. Test coverage, code cleanliness, and architectural understanding become the bottleneck. The senior engineers who used to build features now spend their time reviewing AI output. This is the senior engineer tax. The fix is not to stop using AI. It is to keep the codebase clean enough that both AI and humans can understand it, and to use AI itself to close the quality loop: find issues, fix them, run tests, verify.

## Formal Definition / Statement

This is a guest lecture by Dr. Andreas Wilhelm from CQSE, a software quality company in Passau and Munich. It is not a regular course lecture but an industry perspective on how AI agents interact with software quality practices.

### Agentic Coding

AI coding agents autonomously perform development tasks: writing code, reviewing changes, fixing findings, generating tests, running tests. Examples include Claude Code running for 34 minutes on a Rust preprocessor task that would take a human 1-2 months.

The recursive self-improvement loop illustrates the pattern:

```
while true; do claude -p 'Task $RANDOM: Write a 1000 word essay on AI.'; done
```

### Evidence on AI Code Quality

He et al., "Speed at the Cost of Quality" (MSR 2026): AI coding tools accelerate development but erode code quality. More AI-generated code means higher QA demand, because QA becomes the bottleneck for scaling development.

Key findings from the lecture:
- AI performs worse on low-quality code. Keeping code clean helps both AI and humans understand it.
- "Strong engineering foundations amplify AI's benefits and offer protection against its downsides" (Anthropic research).
- "The most experienced people in your organization are being buried. We call it the senior engineer tax." Senior engineers spend time reviewing and fixing AI code instead of building new features.

### Social Aspects

Resistance to quality tools is not new ("I don't have time to fix findings"). But AI agents can also help: closing test gaps, fixing findings, explaining issues. The lecture notes that "LLMs are very good in convincing non-experts (junior developers) in the existence of quality issues."

### Software Intelligence (Teamscale)

CQSE's Teamscale platform combines multiple data sources: code, models, version history, tickets, test coverage, test results, usage data, reviews. It answers questions like: which changes have not been reviewed, which duplicated bugs were fixed only once, where are test gaps, where is technical debt.

### AI Integration with Quality Platforms

Use cases:
- Get refactoring suggestions for findings
- AI reviews code changes in merge requests
- AI explains and summarizes content in Teamscale
- AI agent cleans up findings on local changes
- AI agent executes tests for changed code
- AI generates tests for remaining test gaps

Architecture: collaboration platforms, IDEs, browsers, and issue trackers connect to AI backends via MCP (Model Context Protocol). AI agents sit between the developer and the quality platform, closing the loop from finding to fixing to verification.

### Deep Practice

"Effective learning requires deep practice. You must stretch, fail, notice the mistake, correct it, and repeat." This applies to both human learning and AI agent iteration.

## Key Properties

- AI coding erodes quality (He et al. MSR 2026): speed increases, quality decreases
- Agentic coding shifts the bottleneck from code production to code verification
- AI-generated code trends toward average quality, which accumulates debt in large codebases
- QA becomes the scaling constraint, not development speed
- AI performs worse on low-quality code: clean code is a prerequisite for effective AI assistance
- Senior engineer tax: experienced developers spend disproportionate time reviewing AI output instead of building
- MCP (Model Context Protocol) is the integration layer connecting tools to AI backends
- The quality loop (find, fix, test, verify) can be partially automated by AI agents
- AI is better at convincing junior developers about quality issues than static reports alone

## Worked Example

**Scenario: A team adopts agentic coding for a mid-size Python project.**

Before AI: 5 developers write and review code. QA finds issues in code review. Senior developers spend 20% of time on review.

After AI: 5 developers use Claude Code to generate features. Output doubles. But code review now takes 3x longer because the volume is higher and AI code needs careful checking. Senior developers spend 60% of time on review. This is the senior engineer tax.

**Mitigation with quality platform:** The team connects Teamscale to their CI pipeline. AI agents review merge requests automatically, flag findings, and suggest fixes. Junior developers see AI-generated explanations of quality issues and fix them before review. Senior developers review only what the AI could not resolve. Review time drops back to 25%. The quality loop is partially automated.

The lesson: AI without quality infrastructure makes things worse. AI with quality infrastructure amplifies the team.

## Common Pitfalls

- Assuming AI-generated code is correct because it looks plausible. It is average by construction and needs the same scrutiny as human code.
- Assuming AI-generated code needs less review. The opposite is true: AI averages quality, so edge cases and subtle bugs need human verification.
- Letting AI agents modify code without running tests. The quality loop requires verification, not just generation.
- Believing AI can fix quality issues in already-poor code. AI performs worse on low-quality codebases. Clean first, then automate.
- Ignoring the senior engineer tax. If you do not measure how much time seniors spend reviewing AI output, you will not notice the problem until it is severe.
- Treating quality tools as optional when using AI. Clean code is the prerequisite for AI to work well, not a luxury.
- Expecting AI agents to fully replace QA. They can close part of the loop, but verification still needs human judgment for non-obvious cases.
- "The quality of AI generated code is so good, we no longer need additional quality measures." This is false. Evidence shows the opposite.
- "Software quality is no longer relevant, as AI does all the changes." Also false. No human touching the code means no one understands it, which makes future AI changes worse.
- Skipping the "notice the mistake" step in deep practice. Without honest failure analysis, neither humans nor AI improve.

## Connections

- [[software-analyse-lecture-9]] - Dynamic analysis (traces, instrumentation) connects to AI-driven test generation and fault detection.
- [[software-analyse-lecture-10]] - Symbolic execution explores paths systematically; AI agents explore paths heuristically. Different approaches to the same goal.
- [[static-vs-dynamic-analysis]] - AI agents do both: they read code (static) and run it (dynamic).
- [[testing]] - AI test generation is a direct application of the testing concepts from earlier lectures.
- [[fault-localization]] - AI can rank suspicious statements, connecting to Tarantula and Ochiai.
- [[debugging]] - AI agents automate parts of the debugging loop.
- [[design-patterns]] - Clean code and good architecture help AI agents understand and modify codebases.

## Open Questions

- How reliable are AI agents at fixing findings without introducing regressions? The lecture showed the loop but did not quantify success rates.
- What is the actual error rate of AI-generated merge request reviews compared to senior engineer reviews?
- How does MCP handle security and access control when connecting AI backends to issue trackers and CI systems?
- How does the senior engineer tax scale? As more AI code enters a codebase, does the review burden grow linearly or super-linearly?
- Can AI agents reliably distinguish real quality issues from false positives, or do they need human verification for every finding?
- The MSR 2026 paper measures quality erosion, but what is the long-term effect on codebase maintainability over months or years?
- The lecture cites MSR 2026 evidence that AI erodes quality. Is there counter-evidence that AI improves quality when applied to clean codebases with strong test coverage?
- How do you measure the senior engineer tax quantitatively in a real organization?
