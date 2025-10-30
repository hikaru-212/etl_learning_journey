# 🧩 Module B — List & Dictionary Operations
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module focuses on **list and dictionary manipulation**, providing the foundation for handling structured data in Python.  
You’ll practice creating, updating, merging, and reversing data containers — key skills in ETL, data transformation, and general programming.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **Remove Value** | Remove all occurrences of a value from a list | Filtering + list construction |
| P2 | **Reverse List** | Reverse the list in place | List method `.reverse()` |
| P3 | **Word Count** | Count word frequencies in a string | Dictionary counting with `.get()` |
| P4 | **Invert Dictionary** | Swap dictionary keys and values | `dict.items()` iteration |
| P5 | **Merge Dictionaries** | Combine two dicts, overriding duplicates | `copy()` + `update()` |

All solutions are implemented in `quick.py` using Python’s built-in methods.

---

## ⚙️ Multi-Version Structure

Each problem will have **three levels of implementation**, organized under the `drills/` directory:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Uses built-ins and Pythonic syntax |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Manual control with `for` loops and conditionals |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py)  | Memory-oriented logic using index-based iteration |

Each file maintains a consistent **registry** for unified access:
```python
REGISTRY = {
    "P1": run_P1_remove_val,
    "P2": run_P2_reverse_list,
    "P3": run_P3_word_count,
    "P4": run_P4_invert_dict,
    "P5": run_P5_merge_dicts,
}
```

This allows for centralized testing and batch execution.

---

## 🧪 Testing — `tests_drills.py`

This module’s test suite runs all registered functions automatically across implementations.  

Example test configuration:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": (([3,2,2,3,4,3],3), [2,2,4]),
    "P2": (([1,2,3,4,5],), [5,4,3,2,1]),
    "P3": (("apple banana apple orange banana apple",),
           {'apple':3, 'banana':2, 'orange':1}),
    "P4": (({"a":1,"b":2,"c":3},), {1:"a",2:"b",3:"c"}),
    "P5": (({"a":1,"b":2},{"b":3,"c":4}), {"a":1,"b":3,"c":4}),
}
```

Run with:
```bash
pytest -q coding_training/basic/moduleB_list_dict/drills/tests_drills.py
```

✅ Outputs from each implementation are validated automatically.

---

## 🧭 Learning Goals

- Build a solid understanding of **mutable containers** (lists, dicts)  
- Learn when to use built-in methods vs. manual iteration  
- Practice data transformations relevant to ETL workflows  
- Strengthen logic for merging, counting, and filtering patterns

---

## 🧩 File Structure

```
moduleB_list_dict/
└─ drills/
   ├─ quick.py          ← Pythonic implementations (working)
   ├─ lowlevel.py       ← Expanded loop-based versions (WIP)
   ├─ c_like.py         ← C-style versions (coming soon)
   ├─ tests_drills.py   ← Centralized automated testing
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Dictionaries are the backbone of structured data in Python.  
> Understanding how to iterate, merge, and invert them efficiently prepares you for working with **JSON**, **ETL schemas**, and **database transformations**.
