---
title: "Lecture 11: Agentic Coding and Software Quality"
tags: [concept, semester-1, software-analyse]
course: "Software Analysis"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites: [[software-analyse-lecture-9]], [[software-analyse-lecture-10]]
---

## One-line Summary
AI agents that autonomously write and fix code can accelerate development but erode software quality unless disciplined engineering practices hold the line.

## Core Intuition
Agentic coding means AI does more than suggest snippets. It runs loops, edits files, runs tests, and reviews its own output. The problem: AI-generated code tends toward the average, and average code accumulates quality debt fast. The bottleneck shifts from writing code to verifying it. Senior engineers end up reviewing and fixing AI output instead of building new things. The fix is not to stop using AI. It is to keep the codebase clean enough that both AI and humans can understand it, and to use AI itself to close the quality loop: find issues, fix them, run tests, verify.

## Formal Definition / Statement

**Agentic coding** refers to AI agents that autonomously write, review, and fix code across multi-step workflows. Example: Claude Code running for 34 minutes autonomously on a Rust preprocessor. A recursive self-improvement loop illustrates the concept:

```
while true; do claude -p 'Task $RANDOM: Write a 1000 word essay on AI.'; done
```

**Impact on software quality.** Evidence from He et al., "Speed at the Cost of Quality" (MSR 2026) shows that AI-assisted coding increases output volume while degrading average code quality. Key observations:

- More AI generating average code increases QA demand. QA becomes the bottleneck for scaling development.
- AI performs worse on low-quality code. Clean code helps both AI and humans understand and modify it.
- "Strong engineering foundations amplify AI's benefits and offer protection against its downsides." (Anthropic research)
- "The most experienced people in your organization are being buried. We call it the senior engineer tax." Senior engineers spend time reviewing and fixing AI-generated code instead of building new features.

**Social aspects.** Developers resist quality tools ("I don't have time to fix findings"). AI agents can help close test gaps and fix findings automatically. LLMs are effective at convincing junior developers that quality issues exist, which helps adoption.

**Software Intelligence platform (Teamscale).** Combines code, models, version history, tickets, test coverage, test results, usage data, and reviews into a unified quality view.

**AI integration with quality platforms.** Use cases include: refactoring suggestions, AI review of merge requests, explaining findings, AI agents that clean up findings, executing tests, and generating tests. The architecture connects collaboration platforms, IDEs, browsers, and issue trackers to AI backends via MCP (Model Context Protocol). AI agents can close the loop: find issues, fix them, run tests, verify.

**Deep practice.** "You must stretch, fail, notice the mistake, correct it, and repeat." Quality improvement, whether by humans or AI, requires this cycle.

**Context:** This is a guest lecture by Dr. Andreas Wilhelm from CQSE, a software quality company based in Passau and Munich. It is not part of the regular course sequence.

## Key Properties / Complexity

- Agentic coding shifts the bottleneck from code production to code verification
- AI-generated code trends toward average quality, which accumulates debt in large codebases
- Senior engineer tax: experienced developers spend disproportionate time reviewing AI output
- Clean code is a prerequisite for effective AI assistance, not a nice-to-have
- QA becomes the scaling constraint, not development speed
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
- Ignoring the senior engineer tax. If you do not measure how much time seniors spend reviewing AI output, you will not notice the problem until it is severe.
- Treating quality tools as optional when using AI. Clean code is the prerequisite for AI to work well, not a luxury.
- Expecting AI agents to fully replace QA. They can close part of the loop, but verification still needs human judgment for non-obvious cases.
- Skipping the "notice the mistake" step in deep practice. Without honest failure analysis, neither humans nor AI improve.

## Connections

[[software-analyse-lecture-9]] - Dynamic analysis techniques connect to AI-driven test generation and automated test execution.
[[software-analyse-lecture-10]] - Symbolic execution explores paths systematically, while AI agents explore paths heuristically. The two approaches complement each other.
[[static-vs-dynamic-analysis]] - AI agents can perform both static analysis (finding issues in code) and dynamic analysis (running tests, observing behavior), blurring the traditional boundary.
[[testing]] - AI agents generate, execute, and verify tests, making testing a central use case for agentic quality workflows.
[[fault-localization]] - AI agents can localize faults by correlating findings from multiple sources, which is what Teamscale's combined data view enables.
[[debugging]] - The find-fix-test-verify loop is an automated debugging workflow that AI agents can execute.
[[design-patterns]] - Clean code with recognizable patterns helps AI agents understand and modify code more effectively.

## Open Questions

- How reliable are AI agents at fixing findings without introducing regressions? The lecture showed the loop but did not quantify success rates.
- What is the actual error rate of AI-generated merge request reviews compared to senior engineer reviews?
- How does MCP handle security and access control when connecting AI backends to issue trackers and CI systems?
- The MSR 2026 paper measures quality erosion, but what is the long-term effect on codebase maintainability over months or years?
- How do you measure the senior engineer tax quantitatively in a real organization?
