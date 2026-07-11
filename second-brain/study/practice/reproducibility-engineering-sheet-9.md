---
title: "Exercise Sheet 9: JSON and JSON Schema"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-11
---

# Exercise Sheet 9: JSON and JSON Schema

## 2 JSON and JSON Schema

### 2.1 Docker Environment

> [!note]- Solution
> ```bash
> cd LabSession9
> docker build -t lab9-json .
> docker run -it lab9-json
> ```
>
> The container has `jq` for querying and pretty-printing JSON, `check-jsonschema` for schema validation, and the data files `births.json` and `births_schema.json`.

### 2.2 Pretty-Printing JSON

> [!note]- Solution
> Pretty-printing reformats JSON with consistent indentation:
>
> ```bash
> jq . births.json > births_pretty.json
> ```
>
> The `.` filter is the identity filter — it passes the input through unchanged, but `jq` formats the output with indentation by default.
>
> Compacting is the inverse — strips all insignificant whitespace:
>
> ```bash
> jq -c . births_pretty.json
> ```
>
> Both directions preserve the underlying data; only the formatting changes.
>
> **When is each useful?** Pretty-printed for human readability (debugging, code review). Compact for storage, network transfer, or piping through shell commands.

### 2.3 Querying JSON with jq

> [!note]- Solution
> Using the examples as templates:
>
> **(a)** Print only the `year` field of every record:
>
> ```bash
> jq '.[].year' births.json
> ```
>
> **(b)** Print the total for August:
>
> ```bash
> jq '.[] | select(.month == "August") | .total' births.json
> ```
>
> `select(.month == "August")` filters for the August record, and `.total` extracts the total field.

### 2.4 Comparing JSON Documents

> [!note]- Solution
> **1.** Why `diff births.json births_reordered.json` is unhelpful:
>
> `diff` compares files line by line as text. JSON formatting differences (indentation, line breaks) and key ordering both cause `diff` to report changes even when the documents are structurally identical.
>
> **2.** A better approach — sort keys with `jq -S` before comparing:
>
> ```bash
> diff <(jq -S . births.json) <(jq -S . births_reordered.json)
> ```
>
> `jq -S` sorts object keys alphabetically. Both files are normalised to the same key order and formatting, so `diff` only reports genuine structural differences.

### 2.5 Writing JSON Schema

> [!note]- Solution
> ```json
> {
>   "$schema": "http://json-schema.org/draft/2020-12/schema",
>   "title": "Births Schema",
>   "description": "Schema for Births data",
>   "type": "array",
>   "items": {
>     "type": "object",
>     "properties": {
>       "year": { "type": "integer" },
>       "month": {
>         "type": "string",
>         "enum": [
>           "January", "February", "March", "April",
>           "May", "June", "July", "August",
>           "September", "October", "November", "December"
>         ]
>       },
>       "male": { "type": "integer", "minimum": 1 },
>       "female": { "type": "integer", "minimum": 1 },
>       "total": { "type": "integer", "minimum": 1 }
>     },
>     "required": ["year", "month", "male", "female", "total"],
>     "additionalProperties": false
>   }
> }
> ```
>
> The schema describes an **array of birth records**. Each record is an object with:
> - `year` — integer, required.
> - `month` — string restricted to the 12 month names via `enum`, required.
> - `male`, `female`, `total` — positive integers (`minimum: 1`), all required.
> - `additionalProperties: false` rejects any extra keys not listed in `properties`.
>
> The `enum` constraint on `month` is stricter than `"type": "string"` alone — it prevents typos like `"Jan"` or `"january"`. The `minimum: 1` on counts prevents nonsensical zero or negative birth numbers.

### 2.6 Validating JSON against a Schema

> [!note]- Solution
> **(a)** Validate `births.json`:
>
> ```bash
> check-jsonschema --schemafile births_schema.json births.json
> ```
>
> If the result is not "ok", refine the schema until the document is valid. Common issues: missing required properties, wrong types, or `additionalProperties` rejecting fields that exist in the data.
>
> **(b)** Validate the broken files:
>
> ```bash
> check-jsonschema --schemafile births_schema.json births_broken_1.json
> check-jsonschema --schemafile births_schema.json births_broken_2.json
> ```
>
> If the result is "ok" for a broken file, tighten the schema (e.g., add `minimum`, `enum`, or `additionalProperties: false`) until the broken file fails while `births.json` still passes.
>
> The tool reports which specific constraint was violated and in which record, making it easy to diagnose the problem.

### 2.7 Reproducible Validation with Containers: Bowtie

> [!note]- Solution
> Bowtie is a meta-validator — it runs multiple JSON Schema validators in separate Docker containers, each pinned to a specific version.
>
> ```bash
> # List supported implementations
> bowtie filter-implementations
>
> # Validate with one implementation
> bowtie validate -i python-jsonschema \
>     births_schema.json births.json | bowtie summary
>
> # Compare two implementations
> bowtie validate -i python-jsonschema -i js-ajv \
>     births_schema.json births.json | bowtie summary
> ```
>
> **Why pinned containers are preferable for reproducibility:**
>
> - Different validators support different subsets of JSON Schema. A schema that passes one validator may fail another.
> - Validators are software, and they change over time. A schema that validates today may fail tomorrow if the validator is updated.
> - Bowtie pins each validator to a specific version in a Docker image, so the validation environment is frozen and reproducible.
> - Running multiple validators exposes implementation differences, so you know whether your schema relies on behaviour that is universal or implementation-specific.

## 3 JSON and JSON Schema (Multiple Choice)

> [!note]- Solution
> **(a)** Schema:
> ```json
> {
>   "type": "object",
>   "additionalProperties": false,
>   "required": ["id", "score"],
>   "properties": {
>     "id":    { "type": "integer", "minimum": 1 },
>     "name":  { "type": "string" },
>     "score": { "type": "number", "minimum": 0, "maximum": 100 }
>   }
> }
> ```
>
> Instances:
> 1. `{"id":1,"name":"Ada","score":90}` — valid ✓
> 2. `{"id":0,"name":"Bob","score":50}` — **invalid** ✗ (`id` is 0, violates `minimum: 1`)
> 3. `{"id":3,"name":"Cy","score":80,"x":1}` — **invalid** ✗ (`additionalProperties: false` rejects `x`)
> 4. `{"id":4,"score":100}` — valid ✓ (`name` is optional, `score: 100` satisfies `maximum: 100`)
>
> **Answer: 2** (instances 1 and 4 are valid)
>
> ---
>
> **(b)** Same schema, new instances:
> 1. `{"id":5,"score":95}` — valid ✓
> 2. `{"id":6,"name":"Finn","score":"95"}` — **invalid** ✗ (`score` is a string, not a number)
> 3. `{"id":7,"name":"Gus","score":60.5}` — valid ✓ (`number` includes floats)
> 4. `{"id":8,"name":"Hank","score":0}` — valid ✓ (`score: 0` satisfies `minimum: 0`)
>
> **Answer: 3** (instances 1, 3, and 4 are valid)
>
> ---
>
> **(c)** Schema with `oneOf`:
> ```json
> {
>   "type": "object",
>   "required": ["hero", "level"],
>   "properties": {
>     "hero":     { "type": "string" },
>     "level":    { "type": "integer", "minimum": 1, "maximum": 100 },
>     "gadget":   { "type": "string" },
>     "mutation": { "type": "string" }
>   },
>   "oneOf": [
>     { "required": ["gadget"] },
>     { "required": ["mutation"] }
>   ]
> }
> ```
>
> `oneOf` means exactly one sub-schema must match.
>
> Instances:
> 1. `{"hero":"Volt","level":42,"gadget":"taser"}` — valid ✓ (matches `required: ["gadget"]` only)
> 2. `{"hero":"Blaze","level":9,"mutation":"fire"}` — valid ✓ (matches `required: ["mutation"]` only)
> 3. `{"hero":"Rex","level":50,"gadget":"claw","mutation":"speed"}` — **invalid** ✗ (matches **both** sub-schemas; `oneOf` requires exactly one)
> 4. `{"hero":"Zed","level":0,"gadget":"net"}` — **invalid** ✗ (`level: 0` violates `minimum: 1`)
>
> **Answer: 2** (instances 1 and 2 are valid)
>
> ---
>
> **(d)** Same `oneOf` schema, new instances:
> 1. `{"hero":"Nova","level":100,"mutation":"gravity"}` — valid ✓ (matches `required: ["mutation"]` only)
> 2. `{"hero":"Gale","level":30,"gadget":"boots","city":"Metro"}` — **invalid** ✗ (`additionalProperties` is not set to `false`, so `city` is allowed... but wait, the schema doesn't have `additionalProperties: false`, so extra properties are allowed. However, this matches only `required: ["gadget"]`. Let me re-check.)
>
> Actually, the schema does **not** have `additionalProperties: false`, so `city` is allowed. Instance 2 has `gadget` but not `mutation`, so it matches exactly one sub-schema. **Valid** ✓.
>
> 3. `{"hero":"Ping","level":25}` — **invalid** ✗ (matches neither `required: ["gadget"]` nor `required: ["mutation"]`; `oneOf` requires exactly one)
> 4. `{"hero":"Ace","level":77,"mutation":"cloak"}` — valid ✓ (matches `required: ["mutation"]` only)
>
> **Answer: 3** (instances 1, 2, and 4 are valid)

## Key Takeaways

- `jq .` pretty-prints JSON. `jq -c` produces compact output. `jq -S` sorts keys for reliable comparison.
- `diff` on raw JSON is unreliable because formatting and key order cause false differences. Normalise with `jq -S` first.
- JSON Schema declares types, required properties, and optional properties. `check-jsonschema` validates instances against schemas.
- Bowtie runs multiple validators in pinned Docker containers, exposing implementation differences and making validation reproducible.
- `oneOf` requires exactly one sub-schema to match; instances matching zero or more than one are invalid.

## Related Vault Pages

- [[json-schema]]
- [[reproducibility-engineering-lecture-8]]
- [[reproducibility-engineering-lecture-9]]
