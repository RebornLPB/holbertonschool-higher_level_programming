# Python - Serialization

## Description
This project covers serializing and deserializing Python data across four common formats: JSON, Pickle, CSV, and XML. Each task reads data from or writes data to disk, converting between native Python objects and their on-disk representation.

All scripts target **Python 3.8+**.

## 📝 Learning Objectives
* Serialize and deserialize Python data structures with the `json` module.
* Serialize and deserialize a custom Python object with `pickle`.
* Convert tabular CSV data into JSON with `csv.DictReader`.
* Serialize a dictionary to XML and parse it back with `xml.etree.ElementTree`.
* Handle I/O and format errors gracefully (`try`/`except`).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `task_00_basic_serialization.py` | Basic Serialization | `serialize_and_save_to_file(data, filename)` and `load_and_deserialize(filename)` round-trip Python data through JSON. |
| `task_01_pickle.py` | Pickling Custom Objects | `CustomObject` (name, age, is_student) with `serialize()`/`deserialize()` class method using `pickle`, returning `None` on failure. |
| `task_02_csv.py` | CSV to JSON | `convert_csv_to_json(filename)` reads a CSV file with `csv.DictReader` and writes it to `data.json`; returns `True`/`False` on success/failure. |
| `task_03_xml.py` | XML Serialization | `serialize_to_xml(dictionary, filename)` and `deserialize_from_xml(filename)` round-trip a flat dictionary through XML. |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize; \
serialize_and_save_to_file({'a': 1}, 'out.json'); \
print(load_and_deserialize('out.json'))"
```

```bash
pycodestyle task_00_basic_serialization.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
