---
title: "Lecture 8: Hierarchical Data Formats"
tags: [topic, reproducibility-engineering, semester-1, hdf5, json, xml, hierarchical-data, visitor-pattern]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-19
prerequisites: ["[[reproducibility-engineering-lecture-7]]", "[[visitor-pattern]]", "[[xml-structured-text]]"]
sources: ["raw/lectures/reproducibility_engineering/Vorlesung/SoSe_2026_RepEng_IC_8___Hierarchical_Data_Formats.pdf", "raw/assets/reproducibility_engineering/Vorlesung/8-Hierarchical_Dataformats/SQLite_Walkthrough.pdf"]
---

## One-line Summary
Hierarchical data formats — XML, JSON, and HDF5 — organise data as trees of nested structures (elements, objects, groups/datasets), and the lecture covers how to validate them (JSON Schema), traverse them (visitor pattern), and attach metadata (attributes with a 64 KB limit), all in service of reproducible scientific data management.

## Core Intuition
Tabular data (the focus of [[reproducibility-engineering-lecture-7|Lecture 7]]) is great for flat, rectangular datasets. But scientific data is often *hierarchical*: a climate simulation has groups for each model component (atmosphere, ocean, ice), each containing datasets for each variable (temperature, pressure, salinity), each with attributes (units, source, creation date). A flat table can't represent this naturally.

The lecture covers three hierarchical formats:
1. **XML** and **JSON** — the universal interchange formats (Jennifer Widom's treatment from Stanford's DB course)
2. **HDF5** — the scientific workhorse for large, multi-dimensional datasets

The unifying theme: hierarchical formats let you organise data *and* metadata in a single self-describing file. This is essential for reproducibility — if the data file doesn't carry its own metadata, you lose the context that makes the data interpretable.

## Key Concepts

### XML and JSON as hierarchical formats (Jennifer Widom's treatment)
**XML**: tree of elements, each with a tag name, attributes, and children. Self-describing but verbose.
```xml
<experiment id="exp-001">
  <epochs>100</epochs>
  <learning_rate>0.01</learning_rate>
</experiment>
```

**JSON**: tree of objects and arrays. Lighter syntax, native to JavaScript, widely used for APIs.
```json
{
  "experiment": "exp-001",
  "epochs": 100,
  "learning_rate": 0.01
}
```

Both are **self-describing** (the structure is in the data) and **hierarchical** (nested objects/elements). Both can represent arbitrary tree structures.

**Key differences**:
- XML has attributes (on elements), JSON does not (everything is a key-value pair)
- XML has a schema language (XSD, DTD), JSON has JSON Schema
- XML is verbose (closing tags), JSON is compact
- XML supports namespaces, JSON does not
- XML is the basis for many scientific formats (e.g., MathML, SVG), JSON is the basis for APIs (REST, GraphQL)

### JSON Schema for validation
JSON Schema is a vocabulary for describing the structure of JSON documents. It lets you define:
- **`type`**: the expected JSON type (string, number, object, array, boolean, null)
- **`properties`**: for objects, the allowed keys and their schemas
- **`required`**: which keys must be present
- **`items`**: for arrays, the schema of each element
- **`$ref`**: reference to another schema (for reuse)

Example:
```json
{
  "type": "object",
  "properties": {
    "experiment": {"type": "string"},
    "epochs": {"type": "integer", "minimum": 1}
  },
  "required": ["experiment", "epochs"]
}
```

This validates that a JSON document has a string `experiment` and an integer `epochs >= 1`. See [[json-schema]] for the concept page.

### HDF5: hierarchical data format for scientific data
HDF5 models data as a filesystem in a file:
- **File** = root group (the container)
- **Groups** = folders (containers for datasets and other groups)
- **Datasets** = multi-dimensional arrays (the actual data)
- **Attributes** = small metadata key-value pairs (attached to groups or datasets)

Example structure:
```
climate_sim.h5
├── atmosphere/           (group)
│   ├── temperature       (dataset, shape: 365x720x1440, attrs: units=K)
│   └── pressure          (dataset, shape: 365x720x1440, attrs: units=Pa)
├── ocean/                (group)
│   ├── salinity          (dataset, shape: 365x180x360, attrs: units=PSU)
│   └── current_velocity  (dataset, shape: 365x180x360, attrs: units=m/s)
└── attrs: experiment_id=exp-001, created=2026-06-19
```

See [[hdf5]] for the concept page.

### h5py library: File, Group, Dataset objects
h5py is the Python library for reading and writing HDF5 files. It maps the HDF5 data model to Python objects:
- `h5py.File('name.h5', 'r')` → opens a file (returns a `File` object, which is also the root `Group`)
- `f['group_name']` → returns a `Group` object (dict-like access)
- `f['group_name/dataset_name']` → returns a `Dataset` object
- `dataset[:]` → reads the entire dataset into a NumPy array
- `dataset[0:10, :, :]` → reads a slice (efficient partial I/O)
- `obj.attrs['key']` → gets/sets an attribute (dict-like)

### Visitor pattern applied to HDF5 file traversal
The `visit` and `visititems` methods implement the [[visitor-pattern]] for HDF5:
- `f.visit(callable)` → calls `callable(name)` for every object in the file, depth-first
- `f.visititems(callable)` → calls `callable(name, obj)` for every object, where `obj` is the `Group` or `Dataset`

Example:
```python
def print_structure(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(f"Dataset: {name}, shape: {obj.shape}")
    else:
        print(f"Group: {name}")

f.visititems(print_structure)
```

This separates the traversal logic (in `visititems`) from the action logic (in `print_structure`). You can write different visitors for different purposes (print structure, validate metadata, export to CSV, etc.).

### Attributes as metadata storage
Attributes are small key-value pairs attached to groups or datasets. They are the primary mechanism for storing metadata in HDF5.
- **64 KB limit**: the total size of all attributes on a single object is limited to 64 KB (stored in the object header)
- **Type guessing**: h5py guesses the HDF5 type from the Python type (strings → UTF-8, ints → int64, floats → float64)
- **Dict-like access**: `obj.attrs['key'] = value` to set, `obj.attrs['key']` to get

The 64 KB limit is a common source of errors. If you need to store more metadata, use a dataset (e.g., a JSON string stored as a dataset) instead of attributes.

## Key Properties

### Why hierarchical formats matter for reproducibility
- **Self-describing**: the data carries its own structure and metadata. You don't need a separate README to understand the file.
- **Composable**: groups and datasets can be organised hierarchically, matching the structure of the experiment.
- **Portable**: HDF5 files are cross-platform (same file on Windows, Linux, macOS). XML and JSON are text-based and universally portable.
- **Validatable**: JSON Schema validates JSON structure. HDF5 has a well-defined format specification. XML has XSD/DTD.
- **Efficient**: HDF5 supports chunking, compression, and parallel I/O for large datasets. XML and JSON are less efficient for large data (but more human-readable).

### The visitor pattern as a unifying concept
The visitor pattern (separating traversal from action) appears in:
- HDF5: `visit`/`visititems` for file traversal
- XML: SAX/DOM parsers (traverse the tree, apply actions to elements)
- JSON: recursive traversal of nested objects
- Filesystems: `os.walk()` for directory traversal

This is a general design pattern for hierarchical data: define the traversal once, write different visitors for different purposes.

### The metadata problem
Every dataset needs metadata: what are the units? When was it created? What was the experimental setup? Without metadata, data is uninterpretable. Hierarchical formats solve this by attaching metadata (attributes) directly to the data.

For reproducibility, this means:
- The data file is self-contained — you don't need external documentation
- Metadata travels with the data — if you copy the file, you copy the context
- Metadata is machine-readable — you can validate it, search it, process it programmatically

## Worked Example: HDF5 Climate Simulation

```python
import h5py
import numpy as np

# Create a file with hierarchical structure
with h5py.File('climate_sim.h5', 'w') as f:
    # Root-level metadata
    f.attrs['experiment_id'] = 'exp-001'
    f.attrs['created'] = '2026-06-19'
    
    # Atmosphere group
    atmosphere = f.create_group('atmosphere')
    temp = atmosphere.create_dataset(
        'temperature',
        data=np.random.rand(365, 720, 1440).astype(np.float32),
        compression='gzip'
    )
    temp.attrs['units'] = 'K'
    temp.attrs['source'] = 'ERA5'
    
    # Ocean group
    ocean = f.create_group('ocean')
    sal = ocean.create_dataset(
        'salinity',
        data=np.random.rand(365, 180, 360).astype(np.float32)
    )
    sal.attrs['units'] = 'PSU'

# Traverse the file using the visitor pattern
with h5py.File('climate_sim.h5', 'r') as f:
    def visitor(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, shape: {obj.shape}")
            for key, val in obj.attrs.items():
                print(f"  {key}: {val}")
        else:
            print(f"Group: {name}")
    
    f.visititems(visitor)
```

**Output**:
```
Group: atmosphere
Dataset: atmosphere/temperature, shape: (365, 720, 1440)
  units: K
  source: ERA5
Group: ocean
Dataset: ocean/salinity, shape: (365, 180, 360)
  units: PSU
```

## Common Pitfalls

- **Confusing XML attributes with XML elements**: XML has two ways to store data — attributes (on the element tag) and child elements. They are not interchangeable. Attributes are for metadata, elements are for data.
- **Thinking JSON Schema is a standard**: JSON Schema is a draft standard (currently Draft 2020-12). It is widely used but not yet an official RFC.
- **Forgetting the 64 KB attribute limit**: attributes are stored in the object header, which has a fixed size. If you exceed 64 KB, you get an error. Use a dataset for large metadata.
- **Type guessing surprises**: h5py guesses the HDF5 type from the Python type. Strings become variable-length UTF-8, integers become int64. When in doubt, specify the type explicitly.
- **Confusing hard and soft links**: a hard link keeps the object alive; a soft link does not. If you delete the target of a soft link, the link becomes dangling.
- **XML is not always the right choice**: XML is verbose and slow for large data. For scientific data, HDF5 is usually better. For APIs, JSON is usually better.
- **The visitor pattern is depth-first**: `visititems` traverses in depth-first order. If you need breadth-first or a different order, you must implement your own traversal.
- **HDF5 is not a database**: you can't query an HDF5 file with SQL. It's a file format, not a query engine.

## Connections
- [[reproducibility-engineering-lecture-7]] — tidy data (tabular) vs hierarchical data
- [[visitor-pattern]] — the design pattern underlying file traversal
- [[xml-structured-text]] — XML as a hierarchical format
- [[json-schema]] — the concept page for JSON Schema validation
- [[hdf5]] — the concept page for HDF5
- [[data-provenance]] — attributes are a natural place to store provenance metadata
- [[tidy-data]] — hierarchical data can be tidy (each dataset = one variable)
- [[artifact-packaging]] — the SQLite Walkthrough supplement demonstrates packaging research artifacts (SQPolite, patches, doall.sh)

## Open Questions
- How do you version-control an HDF5 file? (It's binary — you need a separate versioning system or export to text.)
- What is the relationship between HDF5 and the FAIR data principles (Findable, Accessible, Interoperable, Reusable)?
- Can you automatically validate HDF5 metadata against a schema? (HDF5 doesn't have a built-in schema language like JSON Schema.)
- How do you handle schema evolution in HDF5? (If you add a new dataset to a group, old code may break.)
- What is the relationship between XML namespaces and HDF5 groups? (Both are mechanisms for organising hierarchical data.)
