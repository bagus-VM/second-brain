---
title: "RepEng In-Class Exercise 9 — LLMs & Reproducibility"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 9 — LLMs Through the Lens of Reproducibility

---

## Exercise 1 — Local LLM vs Remote API

| Criterion                | Local LLM inside container | Remote API                 |
|--------------------------|---------------------------|----------------------------|
| Self-contained?          | ✓ Yes — everything in the container | ✗ No — depends on external service |
| Container/artifact size  | Very large (GBs for model weights) | Small (just code + API calls) |
| Local hardware requirements | High (GPU, lots of RAM) | Low (just needs internet) |
| Long-term availability   | ✓ Guaranteed (model is archived) | ✗ Risk — API may change/deprecate |
| Cost to re-run           | Hardware cost only | Per-token API cost (may increase) |
| Transparency             | ✓ Full — model weights inspectable | ✗ Limited — model may change without notice |

---

## Exercise 2 — Long-term Reproducibility with Remote LLM

1. **Record the exact model name/version** used (e.g., "gpt-4-turbo-2024-04-09")
2. **Archive API responses** — save the raw LLM outputs in the reproduction package
3. **Log all parameters** — temperature, top_p, seed, max_tokens, system prompt
4. **Pin the model version** — use specific dated snapshots when available
5. **Provide fallback** — include a local model as alternative for future re-runs
6. **Document the API version** — API behavior can change between versions
7. **Store prompts verbatim** — exact prompt text matters for reproducibility

---

## Exercise 3 — Secure API Key Handling

1. **Environment variables:** `OPENAI_API_KEY` set outside the container, injected via `docker run -e OPENAI_API_KEY`
2. **Docker secrets:** Mount the key as a file in `/run/secrets/`
3. **Never hard-code** the key in source code or Dockerfiles
4. **Never commit** `.env` files — add to `.gitignore`
5. **Use `.env` files** locally (excluded from git), injected via `--env-file`

```bash
# In .env (not committed):
OPENAI_API_KEY=sk-...

# Run container:
docker run --env-file .env my-experiment
```

---

## Exercise 4 — Improving LLM Output Reproducibility

**Set sampling temperature to 0** to obtain the most (near-)deterministic results; higher values increase randomness.

**Pass a fixed seed** to pin the pseudo-random choices used during sampling, so that identical requests are sampled the same way.

**(a) Why is exact bitwise reproducibility not guaranteed even with temperature=0 and fixed seed?**

- The API server may distribute requests across different GPU instances with different floating-point behavior
- Model weights may be updated silently by the provider
- Server-side batching can affect computation order
- Different API versions may use different inference code
- Network-level non-determinism in request routing

**(b) What should go into the reproduction package?**

The **raw LLM outputs** (cached responses). Since exact reproduction is impossible, the best strategy is to save all LLM inputs and outputs as data artifacts, so future researchers can analyze the outputs without re-running the model.

---

## Exercise 5 — Prompt Components

| Example Segment | Component |
|----------------|-----------|
| "You are an expert research software engineer." | **Role / System prompt** |
| "Extract the software, datasets, and hardware used in the paper below." | **Task / Instruction** |
| "Focus on the points needed to reproduce the experiment." | **Constraint / Guideline** |
| "Answer with a JSON object, using one property per item." | **Output format specification** |
| "The output is for reviewers assessing reproducibility." | **Context / Audience** |
| "Keep the JSON values concise and factual." | **Style / Tone constraint** |
| "Paper: <text of the paper...>" | **Input data / Content** |

---

## Exercise 6 — Structured Output Techniques

| Technique | Description |
|-----------|-------------|
| **Few-shot prompting** | Show the model correctly formatted outputs so it imitates the format. Simple, but no guarantee. |
| **Scaffolding / Template filling** | Supply the output skeleton yourself (JSON keys, braces) and let the model generate only unknown values. Scaffolding cannot be malformed. |
| **Constrained decoding (Structured outputs)** | Restrict generation to tokens allowed by a grammar/schema, so output is valid by construction. |
| **Validation + retry (Post-hoc repair)** | Validate output (e.g., against JSON Schema); on failure, re-prompt or ask another tool/model to repair it. |

---

## Exercise 7 — Evaluation-Retry Loop

The diagram shows:

1. **Generate** — LLM produces initial JSON output
2. **Validate** — Check against JSON Schema
3. **If valid** → Return result
4. **If invalid** → Send error message back to LLM as context → Go to step 1 (retry)
5. **Max retries reached** → Fail or use fallback

**Fill in the orange boxes:**
- Box 1: "JSON output" or "Generated JSON"
- Box 2: "Valid?" or "Schema validation"
- Box 3: "Error message" or "Validation errors"
- Box 4: "Return result" or "Success"
- Box 5: "Retry" or "Re-prompt with error context"

---

## Exercise 8 — Schema in Prompt vs Constrained Decoding

### (A) Pasting schema into prompt:
- **Pros:** Works with any model, no special API support needed
- **Cons:** No guarantee of validity — model may ignore the schema, produce malformed JSON, add extra fields, use wrong types
- **Retry loop needed** to fix invalid outputs

### (B) Constrained decoding (structured outputs):
- **Pros:** Output is guaranteed valid by construction (grammar-level enforcement)
- **Cons:** Requires API support (OpenAI, Anthropic, llama.cpp have varying support), adds latency, limited schema subset supported
- **No retry needed** — first output is always valid

**Key difference:** (A) is a "please follow this format" request; (B) is a "you can ONLY produce valid output" guarantee.

---

## Exercise 9 — Constrained Decoding Feature Support

| Feature              | OpenAI         | Anthropic       | llama.cpp       |
|----------------------|----------------|-----------------|-----------------|
| additionalProperties | Supported (strict mode) | Limited | Supported |
| Optional properties  | Limited | Limited | Supported |
| minimum, maximum     | Limited | Limited | Supported |
| pattern, format      | Limited | Limited | Supported |
| anyOf                | Limited | Limited | Supported |
| oneOf                | Limited | Limited | Supported |

> **Note:** Feature support evolves rapidly. llama.cpp (via grammar-based sampling) supports the widest range of JSON Schema features. OpenAI's structured outputs support a specific subset (see their docs). Anthropic's support is more limited.

---

## Exercise 10 — Constrained Decoding True/False

- ✓ **The output is syntactically correct JSON.** — Guaranteed by constrained decoding
- ✓ **The output conforms to the declared types and required properties.** — Guaranteed
- ✗ **Numbers and strings are guaranteed to be factually correct.** — No! LLMs hallucinate
- ✗ **Output is guaranteed free of hallucinated content.** — No! Only structure is guaranteed
- ✓ **Semantic constraints not in schema must be checked separately.** — e.g., "end_date > start_date" can't be expressed in JSON Schema type constraints
- ✓ **A schema may be rejected or silently altered** — Each tool supports only a subset of JSON Schema

---

## Exercise 11 — OpenAI API Script

```python
import os
from openai import OpenAI

# Never hard-code the key: read it from the environment.
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # (1)

response = client.chat.completions.create(
    model="gpt-5.5",
    reasoning_effort="none",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Define reproducibility in one sentence."},
    ],
    temperature=0.0,  # (2) most deterministic decoding
    seed=42,          # (3) reproducible sampling
)

print(response.choices[0].message.content)  # (4) the generated text
```

**Blanks:**
1. `os.environ["OPENAI_API_KEY"]`
2. `temperature`
3. `seed`
4. `choices[0].message.content`

---

## Exercise 12 — Structured Outputs Script

```python
schema = {
    "type": "object",
    "properties": {
        "value": {"type": "number"},
        "unit": {"type": "string"},
    },
    "required": ["value", "unit"],           # (1)
    "additionalProperties": False,           # (2)
}

response = client.responses.create(
    model="gpt-5.5",
    reasoning={"effort": "low"},
    input=[{"role": "user",
            "content": "How hot is boiling water at sea level?"}],
    text={
        "format": {
            "type": "json_schema",
            "name": "measurement",
            "schema": schema,
            "strict": True,                  # (3)
        }
    },
)
```

**Blanks:**
1. `["value", "unit"]`
2. `False` — prevents extra properties not in schema
3. `True` — enables strict schema enforcement


---

## Related Resources

### 📖 Lecture 9: LLMs and Reproducibility
- Lecture topic: [[reproducibility-engineering-lecture-9]]

**Key concepts covered:**
- [[types-of-reproducibility]]
- [[levels-of-reproducibility]]
- [[reproducibility-crisis]]
- [[json-schema]]
