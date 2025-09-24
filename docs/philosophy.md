# Philosophy & Learning Notes

> This document complements the [README](../README.md).  
> If the README tells the *summary of a project*, this file tells the *journey of a learner*.  
> 
> Inside, you’ll find:  
> - The motivation behind switching from actuarial work to data engineering  
> - The "Core vs Enablers" mindset inspired by mathematics  
> - How AI became a **conversational encyclopedia**, not just a source of answers

---

## 1. Motivation: Why I Started
My journey into data engineering, particularly ETL/ELT, began unexpectedly during my time as an **Actuarial Specialist**.  
I frequently encountered the term *ETL* in business contexts, yet it was often treated as a black box.  
Driven by curiosity and a desire to explore new career paths, I decided to study it from first principles.  

This project was built after just **two months of self-learning**, with AI as my main partner.  
But unlike how many treat AI—as a passive generator of code or text—I used it differently.

---

## 2. AI as a Conversational Encyclopedia
I approached AI not as a static encyclopedia, but as an interactive one.  
Instead of copy-pasting answers, I treated it like a mentor for dialogue:  

1. Ask for definitions and minimal working examples.  
2. Challenge inconsistencies or incomplete explanations.  
3. Explore alternatives and edge cases.  
4. Refine understanding through back-and-forth reasoning.  

This process turned AI into a **thought accelerator**, not a crutch.  
It helped me quickly spot flaws in reasoning, converge on accurate conceptualizations, and maintain logical consistency.  

In short: the value of AI was not in *providing answers*, but in *shaping my thinking*.

---

## 3. Mathematical Philosophy
My academic background is in **pure mathematics**, and I carried this mindset into engineering.  
In mathematics, every assumption in a proof must serve a purpose:  

- If an assumption is never used, it is unnecessary.  
- If a step does not contribute to the result, it should not exist.  

I applied the same logic to ETL/ELT:  

- Every module, script, or validation step must justify its existence.  
- If removing a step makes no difference, it does not belong.  
- Each addition must improve maintainability, scalability, or reliability.  

This discipline ensured the project did not devolve into a random collection of scripts, but instead evolved logically and coherently.

---

## 4. Core vs Enablers
Through this lens, I began to classify components into two layers:  

- **Core (the essence):**  
  Data transformation itself — the beating heart of ETL/ELT.  
  Without transformation, there is no pipeline.  

- **Enablers (the safeguards):**  
  Validation, orchestration, permissions, monitoring. They don't alter the core logic, but they ensure the pipeline is reliable, maintainable, and scalable.   

This framing avoids the common misconception that these features are "optional."
They are not decorations; they are what makes a system production-grade.

### 💡 Important Note:  
The distinction between Core and Enabler is not absolute. As projects scale, teams grow, or system stability demands increase, what was once considered an “Enabler” — such as workflow orchestration or access control — may become **Core** in a new stage because of its critical impact on reliability and maintainability.  

👉 This distinction became the backbone of my project’s design and staging.

---

## 5. Project Staging Philosophy
Each stage in the project is designed to illustrate a **specific learning milestone**:

- **Stage 0: Why MVP** (to be documented in `learning_journey/stage0_mindset.md`)

  👉 Goal: Explain the motivation for starting with a Minimum Viable Product (MVP).

- **Stage 1: Core MVP (in progress)**  
  👉 Goal: Prove that a minimal ETL flow is viable using only files.  

- **Stage 2: Database Integration & Modularity (planned)**  
  👉 Goal: Transition from file-based outputs to a database-driven ETL while introducing modular code structure.  

- **Stage 3: Enablers — Validation & Reliability (planned)**  
  👉 Goal: Guarantee data quality and reliability with validation, idempotency, and logging.  

- **Stage 4: Enablers — Orchestration & Permissions (planned)**  
  👉 Goal: Add governance and automation through Docker, scheduling, and role-based permissions.  

- **Stage 5: Scaling & ELT Comparison (planned)**  
  👉 Goal: Benchmark ETL vs ELT under larger data volumes to evaluate trade-offs.  

---

## 6. Why Local ELT Often Looks “Underwhelming”
The core value of ELT is not the “load-then-transform” step by itself—it’s the ability to **push down** heavy transforms into a **cloud data warehouse** that executes them with **columnar storage, vectorized operators, and MPP parallelism**.

On a single local machine, even with Docker + Postgres, you’re bounded by:
- **Compute**: limited CPU cores; complex JOIN/GROUP BY can saturate a single node.  
- **Memory/I/O**: large intermediates spill; RAM and disk become bottlenecks.  
- **Lack of MPP**: no distributed execution; limited parallel scan/join strategies.  

**Conclusion:** A local ELT is a valuable **proof of concept** for logic and structure (APIs, schemas, SQL correctness), but it fundamentally cannot demonstrate ELT’s true power at scale. 
That’s why Stage 5 is defined as **“design + local PoC → rerun on cloud MPP”**.

### Planned Methodology (high level)
1. Define identical source data and business rules.  
2. **ETL**: transform outside the warehouse → load results.  
3. **ELT**: load raw → transform via warehouse SQL (dbt).  
4. Measure **latency, cost (if on cloud), data quality, and operational complexity**.  
5. Compare on **local** first (document limitations), then **repeat on cloud MPP** for a fair view.

---

## 7. Beyond ETL: A Broader Mindset
Although this project focuses on ETL/ELT, the deeper lesson is about **thinking like an engineer**:  

- Start from the core.  
- Add only what is necessary.  
- Question the purpose of every assumption.  
- Treat tools (like AI) as accelerators, not crutches.  

This mindset ensures that future projects—whether in cloud engineering, data pipelines, or other domains—are grounded in clarity, logic, and discipline.

---

✦ This file is meant for readers who want the *complete story*.  
If you landed here from the README, thank you for diving deeper into my thought process.
