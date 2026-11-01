# Hi, I'm Charitha Pittala 👋

**AI Engineer | Backend Systems | Applied Machine Learning**

I build practical software at the intersection of **AI, backend engineering, and cloud infrastructure**. I enjoy taking a problem from an initial idea to a working application: understanding the workflow, designing the system, implementing the interface and services, and improving reliability through testing and iteration.

My current interests are LLM-powered applications, retrieval-augmented generation (RAG), AI-assisted workflows, model inference, and the engineering practices needed to make intelligent systems useful and maintainable.

[![GitHub](https://img.shields.io/badge/GitHub-CHARITHA6969-181717?logo=github)](https://github.com/CHARITHA6969)
[![Email](https://img.shields.io/badge/Email-charitha696969%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:charitha696969@gmail.com)

---

## Engineering interests

| Area | What I'm interested in building |
|---|---|
| **Applied AI & LLMs** | RAG pipelines, document intelligence, AI agents, structured outputs, evaluation, and human-in-the-loop workflows |
| **ML engineering** | Model development, inference optimization, quantization, model serving, and reproducible experiments |
| **Backend systems** | Python services, REST APIs, asynchronous jobs, validation, error handling, and reliable data flows |
| **Cloud & platform engineering** | Containerized applications, deployment automation, observability, and scalable infrastructure |
| **Data engineering** | Data preparation, exploratory analysis, SQL, embeddings, and vector search |

## Selected projects

### [GradeFlow](https://github.com/CHARITHA6969/gradeflow)
**AI-assisted assessment and grading workflow prototype**

A React + FastAPI application exploring instructor and student workflows around assignments, rubric-based assessment, submission review, and feedback.

- Instructor-facing dashboard concepts for assignments, rubric criteria, and submission review.
- Student-facing views for grades, score breakdowns, and feedback.
- A demo review flow that refuses to invent a grade when no submission evidence is attached.
- A FastAPI backend with assignment CRUD foundations, SQLAlchemy models, PostgreSQL configuration, Alembic migrations, rubric validation, and pytest API tests.
- React instructor dashboard integration for listing and creating persisted assignments.
- A standalone frontend rubric-score validation utility with unit tests for score bounds, duplicate criteria, and total-point consistency.
- GitHub Actions frontend CI: tests and production build passing.
- GitHub Actions backend CI: pytest API suite passing.

**Engineering focus:** React component design, rubric validation, evidence-first review behavior, unit testing, and CI. The backend now includes SQLAlchemy persistence, PostgreSQL configuration, Alembic migrations, and assignment endpoints; authentication and submission workflows remain future work.

### [Neurotrial](https://github.com/CHARITHA6969/neurotrial)
**Neuroscience clinical-trial intelligence interface**

A React + FastAPI prototype for exploring how LLMs can help researchers inspect and reason about clinical-trial information.

- Trial parsing and structured summaries.
- Side-by-side trial comparison.
- Failure analysis and hypothesis exploration.
- Explicitly synthetic demonstration scenarios (not real clinical-trial evidence).
- Data-provenance and research-integrity documentation.
- A server-side FastAPI analysis gateway that reads Anthropic credentials from the backend environment; the browser no longer handles provider keys.
- Security documentation describing the remaining authentication, rate-limit, and privacy requirements.
- Shared defensive JSON-object parsing for model responses.
- Automated tests for malformed output, fenced JSON, missing inputs, provider errors, and content extraction.
- GitHub Actions CI: JSON parsing/provider tests and production build passing.

**Engineering focus:** structured LLM workflows, research-data provenance, source verification, defensive API handling, and scientific caution. The prototype uses fictional demo records and now routes AI requests through a FastAPI service with server-side credentials. Authentication, rate limits, and privacy review are still required before public use. Its frontend and backend CI workflows run tests and a production build.

## Additional project work

### Enterprise Claims QA LLM Pipeline
**Document question-answering and claims intelligence**

An applied LLM workflow concept for extracting and answering questions over enterprise claims documents, using retrieval and grounded response generation.

- **Technical areas:** Python, FastAPI, embeddings, FAISS / Pinecone, LoRA / QLoRA, Azure ML, AKS, Key Vault.
- **Reported project outcomes:** approximately 40% lower inference latency and 30% lower serving cost in the described implementation; benchmark methodology should accompany these figures in a technical case study.
- **Engineering focus:** document ingestion, retrieval quality, source-grounded answers, model adaptation, secure deployment, and latency/cost evaluation.
- **Status:** Portfolio project experience; the public GradeFlow and Neurotrial repositories are separate implementations.

### Vision-Based Retail Shrink Prevention
**Edge AI and computer vision for retail operations**

A proposed edge-intelligence platform for identifying potential retail shrink patterns by combining visual signals with contextual sensor data.

- **Technical areas:** computer vision, edge AI, sensor fusion, behavioral analytics, event processing.
- **Engineering focus:** low-latency inference, privacy-aware event design, false-positive reduction, and operational alert workflows.
- **Status:** Architecture / project concept; not represented as a deployed customer system.

### Second Nature Brands — ML Inference Optimization
**Efficient model serving and runtime performance**

Applied model-serving and optimization work focused on improving inference efficiency for production-oriented ML workloads.

- **Technical areas:** PyTorch, TensorRT, OpenVINO, quantization, dynamic batching, Docker, Kubernetes, AWS / Azure.
- **Reported project outcome:** approximately 40% inference-latency reduction using quantization and TensorRT.
- **Engineering focus:** latency profiling, throughput, memory utilization, deployment reliability, and reproducible benchmarking.
- **Status:** Project / professional experience described in the portfolio; include benchmark hardware, model, workload, and baseline when presenting the metric.

### Computer Vision and Time-Series ML
**Applied machine-learning experiments**

- **Face-mask detection:** MobileNetV2, TensorFlow, and OpenCV for image classification.
- **Bitcoin price prediction:** recurrent neural network / LSTM experiments on historical time-series data.
- **Engineering focus:** data preparation, model training, evaluation metrics, and experiment reproducibility.

## Technical toolkit

**Languages**  
Python · JavaScript · SQL · Java · C/C++

**AI / Machine Learning**  
PyTorch · TensorFlow · scikit-learn · Hugging Face · LangChain · RAG · Embeddings · LLM evaluation

**Backend & APIs**  
FastAPI · Node.js · REST APIs · asynchronous workflows

**Data & Retrieval**  
Pandas · NumPy · FAISS · vector databases · data preprocessing

**Cloud & DevOps**  
AWS · Azure · Docker · Kubernetes · Terraform · GitHub Actions

**Engineering Practices**  
Git · testing · CI/CD · Linux · API design · debugging · documentation

## How I approach engineering

- **Start with the problem:** understand the user, workflow, constraints, and expected outcome before choosing tools.
- **Build in small, verifiable steps:** prefer working increments over large, difficult-to-debug changes.
- **Make systems understandable:** document setup, architecture, assumptions, and trade-offs.
- **Treat AI outputs carefully:** distinguish source-grounded facts from model-generated interpretation and make uncertainty visible.
- **Improve reliability continuously:** add validation, tests, error handling, observability, and secure configuration as systems mature.

## What I'm working toward

- Building end-to-end AI products with clear evaluation criteria.
- Strengthening Python backend and distributed-systems fundamentals.
- Designing secure, maintainable LLM applications.
- Improving deployment, testing, and production-readiness practices.

## Connect

- **GitHub:** [@CHARITHA6969](https://github.com/CHARITHA6969)
- **Email:** [charitha696969@gmail.com](mailto:charitha696969@gmail.com)

---

*I care about useful products, sound engineering decisions, and making complex systems easier to understand and operate.*
