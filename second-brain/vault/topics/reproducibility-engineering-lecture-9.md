---
title: "Lecture 9: LLMs and Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-08
prerequisites:
  - reproducibility-engineering-lecture-8
  - json-schema
  - types-of-reproducibility
---

## One-line Summary
Large language models are probabilistic black boxes, and making their outputs reproducible requires pinning versions, prompts, parameters, and using structured output techniques.

## Core Intuition
An LLM is not a deterministic function. It is a sampling engine over a learned probability distribution. Even with temperature set to zero and a fixed seed, the same prompt on the same model can produce different outputs across hardware or GPU driver versions. This makes LLM-based experiments fundamentally harder to reproduce than traditional computational work. The answer is not to pretend determinism exists, but to record everything that influences the output and use structured output techniques to constrain what the model can emit.

## Formal Definition / Statement
An LLM experiment is reproducible when a second run, given the same model version, prompt, parameters, and client library, produces outputs that match the recorded sample outputs within an acceptable tolerance. Exact bitwise reproducibility is not guaranteed by any major LLM provider, even when `temperature=0` and a fixed `seed` are supplied.

The reproduction package for an LLM experiment must include:

- Model identifier and version (or commit hash for local models)
- The exact prompts used, decomposed by role
- Parameters: `temperature`, `seed`, `max_tokens`, `top_p`, and any others
- Sample outputs from the original run
- API client version (e.g. `openai` Python package version)

For remote API-based LLMs, you must also pin the API version, because providers update models silently.

## Key Properties / Complexity

**Local LLM in container vs remote API trade-offs:**

| Property | Local (container) | Remote API |
|---|---|---|
| Self-contained | Yes, image has model weights | No, depends on external service |
| Container size | Large (GB to hundreds of GB) | Small (just client code) |
| Hardware requirements | GPU or substantial RAM needed | None beyond network access |
| Long-term availability | Guaranteed if image is preserved | Provider may deprecate or change model |
| Cost to re-run | Electricity + hardware amortization | Per-token API charges |
| Transparency | Full access to weights and internals | Black box, no access to weights |

**Improving output reproducibility:**
- Set `temperature=0` to greedily select the most likely token at each step
- Pass a fixed `seed` parameter where supported
- Pin the model version and API client version
- Save sample outputs for comparison

**Why exact reproducibility still fails:**
- Hardware differences (different GPU architectures produce different floating-point results)
- Non-deterministic GPU operations (parallel reduction order is not guaranteed)
- Model version drift (providers update models without version bumps)
- Floating-point non-associativity across implementations

**Structured output techniques, from weakest to strongest guarantee:**
1. Few-shot examples: show formatted outputs in the prompt. No guarantee the model follows the format.
2. Output scaffolding: supply a skeleton and let the model fill in values. Better guidance, still no guarantee.
3. Constrained decoding: the grammar or schema restricts which tokens the model can emit. Guarantees syntactic correctness.
4. Post-hoc validation: validate output against schema after generation, re-prompt on failure. Catches errors but costs extra API calls.

**What constrained decoding guarantees:**
- Output is syntactically valid JSON
- Output conforms to declared types and required properties
- Output satisfies structural constraints in the schema

**What constrained decoding does NOT guarantee:**
- Numbers and strings may be factually wrong
- Hallucinations are still possible
- Semantic constraints (e.g. "age must be positive and plausible") need separate checking
- The schema itself may be rejected or silently altered by the tool

**JSON Schema support varies across tools:**

| Feature | OpenAI | Anthropic | llama.cpp |
|---|---|---|---|
| `additionalProperties: false` | Yes | Partial | Yes |
| Optional properties | Yes | Yes | Yes |
| `minimum` / `maximum` | Limited | No | Yes |
| `pattern` / `format` | Limited | No | Yes |
| `anyOf` / `oneOf` | Limited | No | Yes |

Each tool supports a different subset of JSON Schema. You must check what your target tool supports before relying on a schema keyword.

## Worked Example

### Prompt decomposition

A well-structured LLM prompt is not a single blob of text. It decomposes into roles:

- **System / developer message**: sets the persona ("You are a helpful assistant that outputs JSON.")
- **User instruction**: the task ("Extract the city and country from the following address.")
- **Constraint**: scope ("Only use information present in the input. Do not guess.")
- **Output format**: structure ("Respond as JSON with keys `city` and `country`.")
- **Audience context**: who the output is for ("The output will be consumed by a data pipeline.")
- **Style guidance**: tone and language ("Be concise. Use English.")
- **Context / data**: the actual input ("123 Main St, Springfield, IL, USA")

### OpenAI API call with reproducibility parameters

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",  # pin the model version
    messages=[
        {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
        {"role": "user", "content": "Extract city and country from: 123 Main St, Springfield, IL, USA"},
    ],
    temperature=0.0,
    seed=42,
    max_tokens=200,
)

print(response.choices[0].message.content)
```

The API key is read from an environment variable, never hard-coded. The model version is pinned to a specific date-stamped snapshot. Temperature is zero and seed is fixed. These are the minimum reproducibility parameters.

### OpenAI Responses API with structured outputs

```python
response = client.responses.create(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "Extract city and country."},
        {"role": "user", "content": "123 Main St, Springfield, IL, USA"},
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "location",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "country": {"type": "string"},
                },
                "required": ["city", "country"],
                "additionalProperties": False,
            },
        }
    },
)

print(response.output_text)
```

With `strict=True` and `additionalProperties=False`, the model is forced to emit JSON that conforms to this exact schema. The output will have `city` and `country` as strings, no extra properties, no missing properties. But the values could still be factually wrong if the model misreads the address.

### Evaluation-retry-loop for LLM-based JSON generation

```
1. Generate output from the LLM
2. Parse as JSON (syntax check)
3. Validate against JSON Schema (structure check)
4. If invalid: re-prompt with error message, retry (up to N times)
5. If valid after N attempts: accept
6. If still invalid after N attempts: fail or fall back
```

This loop combines generation with post-hoc validation. Constrained decoding eliminates steps 2 and 3 in many cases, but post-hoc validation is still useful as a safety net.

## Common Pitfalls

**Assuming temperature=0 means deterministic.** It does not. Hardware differences, GPU non-determinism, and model version drift all break this assumption. Temperature=0 reduces variability but does not eliminate it.

**Forgetting to pin the model version.** Providers like OpenAI serve `gpt-4o` as a moving target. Always use the date-stamped version (`gpt-4o-2024-08-06`) in experiments. Otherwise the model may change between runs and nobody will know.

**Hard-coding API keys.** The key ends up in version control, in container images, in logs. Read from environment variables, use Docker secrets, or use `.env` files that are gitignored.

**Trusting constrained decoding for factual correctness.** Constrained decoding guarantees syntactic correctness, not factual correctness. A model constrained to emit `{"age": "banana"}` will emit it if that is what the distribution produces and the schema allows strings. Semantic validation is a separate step.

**Assuming all JSON Schema validators behave the same.** OpenAI, Anthropic, and llama.cpp support different subsets of JSON Schema. A schema that works with one tool may be silently altered or rejected by another. Test your schema against the specific tool you use.

**Pasting the schema into the prompt and hoping.** Putting the JSON Schema text in the prompt gives the model guidance but no enforcement. The model can still emit invalid JSON or ignore the schema. Constrained decoding is the only technique that enforces structure at the token level.

## Connections

[[reproducibility-engineering-lecture-8]]: Lecture 8 covers JSON Schema, which is the foundation for structured outputs and constrained decoding in LLMs.

[[types-of-reproducibility]]: LLMs challenge computational reproducibility because even deterministic settings produce different outputs across hardware and provider versions.

[[levels-of-reproducibility]]: LLM experiments typically achieve only the weakest level of reproducibility (results agreement) because bitwise reproduction is not possible.

[[reproducibility-crisis]]: LLMs introduce a new source of irreproducibility in computational experiments, compounding the existing crisis.

[[json-schema]]: JSON Schema is the vocabulary used by constrained decoding to restrict what tokens an LLM can emit.

## Open Questions

- How do you measure "agreement" between two LLM outputs when they are free text? What metric do you use for non-structured outputs?
- If a provider silently updates a model, is there any way to detect the change from the outside without access to weights?
- For local LLMs in containers, how large is too large for a reproducible Docker image? At what point does the image become impractical to store and share?
- Is there a standard for recording LLM provenance that the community has converged on, or is everyone still rolling their own?
