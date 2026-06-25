---
title: "JSON Schema"
tags: [concept, reproducibility-engineering, semester-1, json, validation, data-integrity]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-25
prerequisites: ["[[reproducibility-engineering-lecture-8]]"]
---

## One-line Summary
Vocabulary for validating JSON document structure.

## Core Intuition
JSON is schemaless by default — any well-formed JSON is valid. This is convenient for rapid prototyping, but it's a reproducibility problem: without a schema, you can't validate that a JSON document conforms to the expected structure. A missing field, a wrong type, or an unexpected key can silently break downstream code.

JSON Schema is a vocabulary for describing the structure of JSON documents. It lets you define the expected types, required fields, value constraints, and nested structure. A JSON document validated against a schema is guaranteed to have the expected structure — a reproducibility tool for data format integrity.

## Formal Definition / Statement
**JSON Schema** is a JSON-based vocabulary for describing the structure and constraints of JSON data. It is defined by the JSON Schema specification (currently Draft 2020-12). A schema is itself a JSON document that describes the valid structure of other JSON documents.

Key keywords:
- `type`: the JSON type (string, number, object, array, boolean, null)
- `properties`: for objects, the allowed keys and their schemas
- `required`: which keys must be present in an object
- `items`: for arrays, the schema of each element
- `$ref`: reference to another schema (for reuse and modularity)
- `minimum`, `maximum`: numeric constraints
- `minLength`, `maxLength`: string length constraints
- `pattern`: regex pattern for strings
- `enum`: allowed values

## Key Properties

### Schema keywords
- **`type`**: specifies the JSON type. Can be a single type (`"type": "string"`) or an array of types (`"type": ["string", "null"]`).
- **`properties`**: for objects, defines the schema for each key. Keys not listed in `properties` are allowed by default (unless `additionalProperties: false`).
- **`required`**: an array of key names that must be present in the object.
- **`items`**: for arrays, defines the schema for each element. Can be a single schema (all elements must match) or an array of schemas (tuple validation).
- **`$ref`**: references another schema by URI. Enables modularity and reuse.

### Used for API contracts, configuration validation
- **API contracts**: a REST API can publish a JSON Schema for its request and response bodies. Clients can validate their requests; servers can validate their responses.
- **Configuration validation**: application configuration files (e.g., `config.json`) can be validated against a schema. This catches typos, missing fields, and wrong types before the application starts.
- **Data exchange**: when exchanging JSON data between systems, a schema ensures both sides agree on the structure.

### Connection to reproducibility: validates data format integrity
- **Schema validation is a reproducibility tool**: if your experiment outputs JSON, a schema ensures the output has the expected structure. A schema violation is a bug — it means the experiment produced malformed data.
- **Schemas are versioned**: you can track schema changes over time. If the schema changes, you know the data format changed.
- **Schemas are machine-readable**: unlike a README, a schema can be validated automatically. You can write a test that validates every JSON output against the schema.

### Schema combinators: allOf, anyOf, oneOf

JSON Schema composes subschemas with three combinators. Each takes an array of subschemas and combines them with a different matching rule.

- **`allOf`**: the instance must satisfy **all** subschemas. Use it to stack constraints, e.g. "must be a string AND at most 5 characters long".
- **`anyOf`**: the instance must satisfy **at least one** subschema.
- **`oneOf`**: the instance must satisfy **exactly one** subschema. If it matches zero, or matches more than one, it fails.

Worked example (from Exercise Sheet 8): combine `{ "type": "string" }` and `{ "maxLength": 5 }`.

`allOf` (both must hold):
```json
{ "allOf": [ { "type": "string" }, { "maxLength": 5 } ] }
```
- `"foo"`: valid (string, length 3 ≤ 5).
- `"a"`: valid (string, length 1 ≤ 5).
- `"1234567890"`: invalid (string, but length 10 > 5).
- `42`: invalid (not a string).

`anyOf` (at least one must hold):
```json
{ "anyOf": [ { "type": "string" }, { "maxLength": 5 } ] }
```
- `"foo"`, `"a"`, `"1234567890"`: valid. All are strings, so each satisfies the first subschema.
- `42`: invalid. It is not a string, and the exercise treats `maxLength` as a string constraint, so a number does not satisfy the second subschema either.

`oneOf` (exactly one must hold):
```json
{ "oneOf": [ { "type": "string" }, { "maxLength": 5 } ] }
```
- `"foo"`: invalid. It is a string AND has length 3 ≤ 5, so it matches **both** subschemas. `oneOf` rejects anything matching more than one.
- `"a"`: invalid for the same reason (matches both).
- `"1234567890"`: valid. It is a string (matches subschema 1) but too long for `maxLength` (does not match subschema 2). Exactly one match.
- `42`: invalid (matches neither under the exercise's framing).

The trap with `oneOf` is overlapping subschemas. Short strings satisfy both `{ "type": "string" }` and `{ "maxLength": 5 }`, so `oneOf` rejects them. When the subschemas describe disjoint types (e.g. `{ "type": "integer" }` and `{ "type": "string" }`), `anyOf` and `oneOf` are semantically equivalent, since a value can never be both an integer and a string at once.

## Worked Example

**Schema**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "experiment": {"type": "string"},
    "parameters": {
      "type": "object",
      "properties": {
        "learning_rate": {"type": "number", "minimum": 0},
        "epochs": {"type": "integer", "minimum": 1}
      },
      "required": ["learning_rate", "epochs"]
    },
    "result": {
      "type": "object",
      "properties": {
        "metric": {"type": "string"},
        "value": {"type": "number"}
      },
      "required": ["metric", "value"]
    }
  },
  "required": ["experiment", "parameters", "result"]
}
```

**Valid JSON**:
```json
{
  "experiment": "exp-001",
  "parameters": {"learning_rate": 0.01, "epochs": 100},
  "result": {"metric": "accuracy", "value": 0.95}
}
```

**Invalid JSON** (missing `epochs`, `learning_rate` is a string):
```json
{
  "experiment": "exp-001",
  "parameters": {"learning_rate": "0.01"},
  "result": {"metric": "accuracy", "value": 0.95}
}
```

Validation errors:
- `parameters.learning_rate`: expected `number`, got `string`
- `parameters.epochs`: required property missing

## Common Pitfalls

- **Forgetting `required`**: by default, all properties in `properties` are optional. You must explicitly list required fields in `required`.
- **Confusing `properties` with `additionalProperties`**: `properties` defines the schema for known keys. `additionalProperties: false` rejects unknown keys. By default, unknown keys are allowed.
- **Type confusion**: JSON has only six types (string, number, object, array, boolean, null). JSON Schema's `type: "integer"` is a subset of `number` — it validates that the number has no fractional part.
- **`$ref` resolution**: `$ref` references are resolved relative to the schema's base URI. If you move the schema file, `$ref` may break.
- **Schema evolution**: if you change the schema, old JSON documents may no longer validate. Version your schemas and document breaking changes.
- **Validation is not enforcement**: a schema validates structure, not semantics. A schema can check that `learning_rate` is a number, but not that it's a *reasonable* learning rate.

## Connections
- [[reproducibility-engineering-lecture-8]] — the lecture
- [[reproducibility-engineering-sheet-8]] — Exercise Sheet 8 practices the combinators and validation flow
- [[tidy-data]] — validates structure, analogous to tidy data's structural invariant
- [[hdf5]] — HDF5 attributes are another form of metadata
- [[data-provenance]] — schemas can be part of a provenance chain

## Open Questions
- How do you validate JSON Schema against a meta-schema? (JSON Schema is itself defined by a schema.)
- What is the relationship between JSON Schema and OpenAPI (Swagger)? (OpenAPI uses JSON Schema for request/response bodies.)
- Can you generate code from a JSON Schema? (Yes — tools like `jsonschema2pojo` generate Java classes from a schema.)
- ~~How do you handle polymorphic data (e.g., a field that can be one of several types)?~~ **Resolved**: use `oneOf`, `anyOf`, or `allOf` to compose subschemas. See the Schema Combinators section above and [[reproducibility-engineering-sheet-8]].
