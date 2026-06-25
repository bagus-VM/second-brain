---
title: "HDF5"
tags: [concept, reproducibility-engineering, semester-1, hierarchical-data, scientific-computing, metadata]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-25
prerequisites: ["[[reproducibility-engineering-lecture-8]]", "[[visitor-pattern]]"]
---

## One-line Summary
Hierarchical data format for large scientific datasets, modeled as files/groups/datasets/attributes.

## Core Intuition
Scientific data is often multi-dimensional, heterogeneous, and accompanied by rich metadata. A flat table can't represent a climate simulation with groups for atmosphere/ocean/ice, each containing multi-dimensional arrays with units, sources, and creation dates. HDF5 solves this by modelling data as a *filesystem in a file*: groups are directories, datasets are files, attributes are metadata, and the entire tree lives in a single cross-platform binary file.

HDF5 is the de facto standard in scientific computing — used by particle accelerators (CERN), climate models (NASA, NOAA), neuroscience (Allen Brain Atlas), astronomy (Hubble, JWST), and many others. The format is maintained by the HDF Group, and the library is open source.

## Formal Definition / Statement
**HDF5** (Hierarchical Data Format version 5) is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data.

The HDF5 data model consists of:
- **Files**: the root container. An HDF5 file (`.h5` or `.hdf5`) contains a tree of objects.
- **Groups**: containers that hold datasets and other groups. Analogous to directories in a filesystem.
- **Datasets**: multi-dimensional arrays of data elements. Analogous to files in a filesystem. Datasets have a type (e.g., `float32`), a shape (e.g., `1000×1000`), and data.
- **Attributes**: small metadata key-value pairs attached to groups or datasets. Limited to 64 KB total per object.

## Key Properties

### File = root group
An HDF5 file is itself a group — the root group. You can attach attributes to the root group (e.g., experiment ID, creation date), and it can contain subgroups and datasets.

### Groups = folders
Groups are containers. They can contain datasets and other groups, forming a tree structure. Groups support dict-like access (`group['name']`), iteration, and traversal methods (`visit`, `visititems`).

### Datasets = arrays
Datasets are multi-dimensional arrays. They support NumPy-style slicing (`dataset[0:10, :]`), chunking (for efficient partial I/O), compression (e.g., gzip, LZF), and parallel I/O (with MPI).

### Attributes = metadata
Attributes are small key-value pairs attached to groups or datasets. They are the primary mechanism for storing metadata in HDF5. Key properties:
- **64 KB limit**: the total size of all attributes on a single object is limited to 64 KB (by default). This is because attributes are stored in the object header, which has a fixed size.
- **Type guessing**: h5py guesses the HDF5 type from the Python type. Strings become variable-length UTF-8, integers become `int64`, floats become `float64`.
- **Dict-like access**: `obj.attrs['key'] = value` to set, `obj.attrs['key']` to get.

### Hard links vs soft links
- **Hard link**: a direct reference to an object. Multiple hard links can point to the same object. The object is deleted only when all hard links are removed.
- **Soft link** (symbolic link): a reference by name. If the target is deleted, the soft link becomes dangling.

### visit/visititems for tree traversal (visitor pattern)
The `visit` and `visititems` methods implement the [[visitor-pattern]] for HDF5 files:
- `f.visit(callable)`: calls `callable(name)` for every object in the file, in depth-first order.
- `f.visititems(callable)`: calls `callable(name, obj)` for every object. `obj` is the `Group` or `Dataset` object.

This separates the traversal logic (in `visititems`) from the action logic (in the callable).

### 64KB attribute limit
Attributes are stored in the object header, which has a fixed size. If you exceed 64 KB, you get an error. Workarounds:
- Use a dataset for large metadata (e.g., a JSON string stored as a dataset).
- Increase the file's "object header message" size (a file creation property).
- Store large metadata in a separate file and reference it by path.

### Real-world use: particle accelerators, climate data, neuroscience
- **Particle accelerators** (CERN, Fermilab): HDF5 stores detector data from particle collisions. Each event is a dataset; metadata (beam conditions, detector calibration) are attributes.
- **Climate data** (NASA, NOAA): HDF5 stores multi-dimensional arrays of temperature, pressure, salinity over time, latitude, longitude. Groups organise by model component (atmosphere, ocean, ice).
- **Neuroscience** (Allen Brain Atlas): HDF5 stores brain imaging data. Each dataset is a 3D volume; attributes store metadata (subject ID, imaging parameters, processing steps).
- **Astronomy** (Hubble, JWST): HDF5 stores image data from telescopes. Each dataset is an image; attributes store metadata (exposure time, filter, pointing).

## Worked Example

```python
import h5py
import numpy as np

# Create a file
with h5py.File('climate_sim.h5', 'w') as f:
    # Create groups
    atmosphere = f.create_group('atmosphere')
    ocean = f.create_group('ocean')
    
    # Create datasets
    temp_data = np.random.rand(365, 720, 1440).astype(np.float32)
    temp = atmosphere.create_dataset('temperature', data=temp_data)
    temp.attrs['units'] = 'K'
    temp.attrs['source'] = 'ERA5'
    
    sal_data = np.random.rand(365, 180, 360).astype(np.float32)
    sal = ocean.create_dataset('salinity', data=sal_data)
    sal.attrs['units'] = 'PSU'
    
    # Add metadata to the root group
    f.attrs['experiment_id'] = 'exp-001'
    f.attrs['created'] = '2026-06-19'

# Traverse the file
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

## HDF5 vs XML vs JSON

HDF5, XML, and JSON all model hierarchical data, but they fit different workloads.

**Prefer HDF5 for:**
- Large numerical arrays, especially multi-dimensional ones (climate grids, detector reads, image volumes).
- Scientific data with rich metadata that belongs in a hierarchy (groups for components, datasets for variables, attributes for units and provenance).
- Datasets that need chunking, compression, or parallel I/O for efficient partial reads.

**Prefer XML or JSON for:**
- Human-readable data that people will inspect or edit by hand.
- Web APIs and configuration files, where text-based tools and broad language support matter.
- Small to medium structured records exchanged between systems.

HDF5 is binary and compact but opaque to text tools. XML and JSON are readable and universal but inefficient for large numerical arrays. Match the format to the data shape and the workflow.

### Worked Example: Weather Stations (Exercise Sheet 8)

Two weather stations (15 and 20) collect temperature and wind readings with per-station metadata (sampling delta, start time, unit). Stored as CSV, this needs three joined tables plus a fragile metadata table. In HDF5 the hierarchy mirrors the physical setup: one group per station, one dataset per measurement, and attributes for the metadata.

```python
import numpy as np
import h5py

temperature_station_15 = np.array([18.2, 18.4, 18.7, 19.0, 19.1])
wind_station_15 = np.array([3.1, 3.3, 2.8, 4.0, 3.7])
temperature_station_20 = np.array([64.0, 65.0, 66.1, 65.8])
start_time = 0  # Should be a proper timestamp.

with h5py.File("weather.hdf5", "w") as f:
    # Station 15: h5py creates the intermediate group "/15" automatically.
    f["/15/temperature"] = temperature_station_15
    f["/15/temperature"].attrs["delta"] = 5.0
    f["/15/temperature"].attrs["start time"] = start_time
    f["/15/temperature"].attrs["temp unit"] = "degree Celsius"

    f["/15/wind"] = wind_station_15
    f["/15/wind"].attrs["delta"] = 5.0
    f["/15/wind"].attrs["start time"] = start_time
    f["/15/wind"].attrs["wind unit"] = "m/s"

    # Station 20.
    f["/20/temperature"] = temperature_station_20
    f["/20/temperature"].attrs["delta"] = 10.0
    f["/20/temperature"].attrs["start time"] = start_time
    f["/20/temperature"].attrs["temp unit"] = "degree Fahrenheit"

    f.attrs["description"] = "Weather station data (temperature and wind)"
```

Units now travel with the data, so station 20's Fahrenheit values cannot be confused with station 15's Celsius values. One self-describing file replaces three loosely coupled CSV tables.

## Common Pitfalls

- **Forgetting to close the file**: HDF5 files buffer writes. If you don't close the file (or use `with`), data may not be flushed to disk. Always use `with h5py.File(...) as f:`.
- **Exceeding the 64 KB attribute limit**: if you try to store a large string or array as an attribute, you'll get an error. Use a dataset instead.
- **Type guessing surprises**: h5py's automatic type conversion can produce unexpected HDF5 types. When in doubt, specify the type explicitly with `dtype=...`.
- **Confusing hard and soft links**: a hard link keeps the object alive; a soft link does not. If you delete the target of a soft link, the link becomes dangling.
- **Reading an entire dataset into memory**: `dataset[:]` loads the entire dataset. For large datasets, use slicing: `dataset[0:100, :, :]`.
- **Not using chunking for large datasets**: HDF5 stores datasets contiguously by default. For large datasets that you access in subsets, enable chunking: `create_dataset(..., chunks=(100, 100, 100))`.
- **The visitor pattern is depth-first**: `visititems` traverses in depth-first order. If you need a different order, you must implement your own traversal.
- **HDF5 is not a database**: you can't query an HDF5 file with SQL. It's a file format, not a query engine.

## Connections
- [[reproducibility-engineering-lecture-8]] — the lecture
- [[visitor-pattern]] — the design pattern underlying `visit`/`visititems`
- [[data-provenance]] — HDF5 attributes are a natural place to store provenance metadata
- [[xml-structured-text]] — XML is another hierarchical format
- [[json-schema]] — validates JSON structure, analogous to HDF5's self-describing nature
- [[tidy-data]] — hierarchical data can be tidy (each dataset = one variable)
- [[reproducibility-engineering-sheet-8]] — Exercise Sheet 8 builds the weather station HDF5 file

## Open Questions
- How does HDF5 compare to Parquet for columnar data? (Parquet is better for tabular data; HDF5 is better for multi-dimensional arrays.)
- Can you version-control an HDF5 file? (No — it's binary. You need a separate versioning system or export to text.)
- What is the relationship between HDF5 and the FAIR data principles (Findable, Accessible, Interoperable, Reusable)?
- How do you handle schema evolution in HDF5? (If you add a new dataset to a group, old code may break.)
