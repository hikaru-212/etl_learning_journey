# 🧩 Module F — Stack / Queue / Counting
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module focuses on **data-structure simulation** and **counting problems** that are frequently encountered in algorithm practice and ETL logic building.  
It contains **five foundational drills** implemented in Python, each showcasing a core concept such as LIFO/FIFO operations, balanced-symbol checking, and frequency analysis.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **Stack Simulation (LIFO)** | Push / Pop elements according to given ops | List + append / pop |
| P2 | **Queue Simulation (FIFO)** | Enqueue / Dequeue using deque | collections.deque |
| P3 | **Balanced Parentheses Checker** | Determine whether parentheses / brackets are balanced | Stack + mapping |
| P4 | **Word Frequency Counter** | Count how many times each word appears | collections.Counter |
| P5 | **Top-K Frequent Elements** | Return k most frequent numbers from a list | Counter + heapq.nlargest |

All examples are in `quick.py`, using Pythonic APIs such as `append`, `popleft`, `Counter`, and `heapq`.

---

## ⚙️ Multi-Version Structure

Each problem will be implemented in **three versions**, located in the same `drills/` directory:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py)| Clean and Pythonic approach using standard APIs |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Step-by-step control-flow simulation without advanced APIs |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Pointer-style fixed-array implementation similar to C |

Each file defines the same set of functions, e.g.:
```python
def run_P1_stack_simulation(ops: list[str]) -> list[int]:
    ...
```
and ends with a `REGISTRY` mapping:
```python
REGISTRY = {
    "P1": run_P1_stack_simulation,
    "P2": run_P2_queue_simulation,
    "P3": run_P3_balanced_parentheses,
    "P4": run_P4_word_counter,
    "P5": run_P5_topk_frequent,
}
```
This unified interface allows the testing script to automatically locate and execute each exercise.

---

## 🧪 Testing — `tests_drills.py`

`tests_drills.py` is the **automated test runner** for this module.  
It imports every implementation (`quick`, `lowlevel`, `c_like`) and verifies the outputs of all registered problems:

```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": ((["1","2","3","pop","4"],), [1,2,4]),
    "P2": ((["1","2","3","deq","4"],), [2,3,4]),
    "P3": (("({[]})",), True),
    "P4": (("apple banana apple orange banana apple",),
           {"apple":3,"banana":2,"orange":1}),
    "P5": (([1,1,1,2,2,3],2), [1,2]),
}
```

Running:
```bash
pytest -q coding_training/basic/moduleF_stack_queue_count/drills/tests_drills.py
```

✅ automatically checks all problems across all versions,  
so you don’t have to manually `print()` each result.

---

## 🧭 Learning Goals

- Understand LIFO vs FIFO behavior  
- Practice manual control-flow simulation (stack / queue)  
- Learn counting and frequency ranking patterns  
- Prepare for future low-level and C-like implementations  

---

## 🧩 File Structure

```
moduleF_stack_queue_count/
└─ drills/
   ├─ quick.py          ← Pythonic version (working)
   ├─ lowlevel.py       ← Manual control-flow version (WIP)
   ├─ c_like.py         ← C-style simulation (coming soon)
   ├─ tests_drills.py   ← Automated tests for all versions
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Use `if __name__ == "__main__":` inside each file for quick manual debugging,  
> and rely on `pytest` to run bulk verification once multiple versions exist.
