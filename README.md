# From Math to Data Engineering  
*A Hands-on ETL Learning Journey*

> 🚧 **Status Note (狀態說明)**:  
> This project is in its **early development phase** (currently focusing on Stage 0 & Stage 1).  
> Documents and code are being added step by step. Structure may change frequently.  
>  
> 本專案正處於積極開發的早期階段（目前專注於 Stage 0 與 Stage 1）。  
> 文件與程式將逐步補上，架構可能會頻繁變動。  

---

This repository documents my journey of learning ETL/ELT step by step.  
Built after just **two months of self-learning with AI assistance**, it evolves from the simplest MVP to more advanced, production-like features.  

The goal is to make the **evolution of data engineering practices** explicit and easy to follow.

---

## Core vs Enablers
I see data engineering as built around two essential layers:  

- **Core (the essence):** Data transformation itself — the heart of ETL/ELT.  
- **Enablers (the safeguards):** Validation, orchestration, permissions, monitoring. They don't alter the core logic, but they ensure the pipeline is reliable, maintainable, and scalable.  

👉 For the detailed philosophy behind this framework, see [docs/philosophy.md](./docs/philosophy.md).

---

## Project Stages
- **Stage 0: Why MVP (Mindset) (in progress)** → Lessons learned from over-ambition → importance of starting small.  
- **Stage 1: Core MVP (File-based) (in progress)** → Prove a minimal ETL flow is viable using only files.  
- **Stage 2: Database Integration & Modularity (planned)** → Transition to database-driven ETL and split code into modular components.  
- **Stage 3: Enablers — Validation & Reliability (planned)** → Add data validation, idempotency, and logging for robustness.  
- **Stage 4: Enablers — Orchestration & Permissions (planned)** → Introduce Docker, scheduling, and role-based access.  
- **Stage 5: Scaling & ETL vs ELT (design + local PoC) (planned)** → Outline a benchmarking method, run a local proof-of-concept, and prepare for re-run on a cloud data warehouse.

---

## Roadmap

- [ ] Stage 0: Why MVP 
- [ ] Stage 1: File-based MVP  
- [ ] Stage 2: Database integration  
- [ ] Stage 3: Data validation + idempotency  
- [ ] Stage 4: Orchestration + permissions  
- [ ] Stage 5: Scaling + ELT comparison  

## 📊 Visual Roadmap 

```mermaid
flowchart LR
    A[Stage 0: Why MVP] --> B[Stage 1: File-based MVP]
    B --> C[Stage 2: Database Integration]
    C --> D[Stage 3: Validation & Reliability]
    D --> E[Stage 4: Orchestration & Permissions]
    E --> F[Stage 5: Scaling & ETL vs ELT]
```

---

## Planned Development 
This repository is still in its very early stage.  
At the moment, there is **no working pipeline yet** — the focus so far has been on documenting the philosophy and staging plan.  

Upcoming milestones: 
- Document the motivation and lessons in **Stage 0: Why MVP (Mindset)**  
- Build the first local MVP pipeline (file-based)  
- Migrate outputs into a database (Postgres)  
- Add validation, idempotent writes, and logging  
- Introduce containerization and orchestration with Airflow  
- Experiment with scaling to larger datasets  
- Prepare for eventual migration to a cloud data warehouse  

The long-term goal is to evolve this into a **cloud-ready data pipeline**,  
while keeping the philosophy of logical, minimal, and purposeful design.


---

## Why This Repo Exists

This project is more than just code.  
It documents the **learning journey** of someone with a mathematics background,  
who decided to explore data engineering and build an ETL pipeline from scratch.  

- For myself: it serves as a record of growth, decisions, and mistakes learned along the way.  
- For others: It’s a testament that you don’t need years of experience to start building. You can begin small, question everything, and incrementally build towards more complex systems.

If you are also learning ETL, or transitioning from another field,  
I hope this repo provides a reference point — and maybe the encouragement to start your own journey.  

---

## Author’s Note: Why a "Second Round"?

My first project successfully demonstrated the concept of an ETL pipeline. However, upon completion, I realized that most of the code was provided by AI. Although I understood what the code did, I lacked the 'implementation fluency' that only comes from building it yourself. 

This second iteration is my attempt to bridge the gap between conceptual understanding and true internalization.The **core insights and frameworks remain the same**, as they came from genuine problem-solving. But now, I'm translating them into cleaner code and deeper technical understanding.

This second iteration focuses on:  
- Translating my architectural understanding into cleaner code  
- Deepening my hands-on experience with each component  
- Documenting not just what I built, but **why I made each design choice**  
 
---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 📖 Curious about the deeper story?  
👉 Dive into [docs/philosophy.md](./docs/philosophy.md).

---
### Connect with me
- LinkedIn: [YenhuaChen's LinkedIn](https://www.linkedin.com/in/yh-Chen-data)

