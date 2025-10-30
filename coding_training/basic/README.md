# 🧭 Basic Level Overview

## 🎯 Purpose
The `basic/` directory serves as a **foundational training zone** for developing strong Python fundamentals before progressing to full ETL workflows.  
It focuses purely on Python programming, algorithmic thinking, and problem-solving skills used in data engineering and ETL contexts.

---

## 🧩 Folder Structure
```
basic/
├─ moduleA_control_flow/
│   ├─ drills/      ← Basic syntax exercises
│   └─ leetcode/    ← Extended algorithm problems
├─ moduleB_list_dict/
├─ moduleC_strings/
├─ moduleD_iteration_enumeration/
├─ moduleE_comprehensions/
├─ moduleF_stack_queue/
└─ moduleG_functions_recursion/
```

Each module focuses on a distinct set of Python concepts and contains both **drills** (for syntax mastery) and optional **LeetCode-style exercises** (for applied logic training).

---

## 📘 Quick Navigation
Click any module name below to view its individual exercises and explanations.

| Module | Theme | Training Focus |
|---------|--------|----------------|
| [**A. Control Flow**](moduleA_control_flow/drills/README.md) | `if` / `for` / `while` / `return` | Mastering basic logic and flow control |
| [**B. List & Dict Operations**](moduleB_list_dict/drills/README.md) | append / update / get | Mutable container operations |
| [**C. String Processing**](moduleC_strings/drills/README.md) | split / join / strip | String cleaning and manipulation |
| [**D. Iteration & Enumeration**](moduleD_iteration_enumeration/drills/README.md) | enumerate / zip / any / all | Iteration patterns and data traversal |
| [**E. Comprehensions**](moduleE_comprehensions/drills/README.md) | list / dict / set comprehensions | Pythonic and expressive patterns |
| [**F. Stack & Queue**](moduleF_stack_queue/drills/README.md) | append / pop / deque / Counter | Data structure simulation and logic |
| [**G. Functions & Recursion**](moduleG_functions_recursion/drills/README.md) | def / return / recursion | Function design and recursive thinking |

---

## 🧩 File Types
| File | Description |
|------|--------------|
| `quick.py` | Pythonic, concise version of each exercise |
| `lowlevel.py` | Manual loop-based implementations (no high-level API) |
| `c_like.py` | C-style index-based implementations (no list helpers) |
| `tests_drills.py` | Automated testing for all problem variants |
| `README.md` | Explanation and overview for each module |

---

## 🧪 Testing Framework
All exercises follow a unified registry system to enable automated testing.

Example:
```python
REGISTRY = {
    "P1": run_P1_example,
    "P2": run_P2_example,
    ...
}
```

Each module’s `tests_drills.py` can import this registry and automatically validate all functions across different versions (`quick`, `lowlevel`, and `c_like`).

---

## 🧭 Learning Path
> The sequence from Module A → G gradually builds your understanding from control flow to functional abstraction.  
> Once completed, you’ll have a solid Python foundation ready for real-world ETL scripting and data pipeline automation.

---

## ⚙️ Notes
- This project is focused entirely on **Python ETL training**.  
- Its goal is to strengthen **core programming fundamentals** and ensure readiness for **data engineering practice**.
