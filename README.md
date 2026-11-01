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
- A FastAPI backend with health and rubric-validation endpoints, Pydantic request/response models, and pytest API tests.
- A standalone frontend rubric-score validation utility with unit tests for score bounds, duplicate criteria, and total-point consistency.
- GitHub Actions frontend CI: tests and production build passing.
- GitHub Actions backend CI: pytest API suite passing.

**Engineering focus:** React component design, rubric validation, evidence-first review behavior, unit testing, and CI. The backend is an early foundation without authentication, database persistence, or AI grading; the review interface remains a demo.

### [Neurotrial](https://github.com/CHARITHA6969/neurotrial)
**Neuroscience clinical-trial intelligence interface**

A React prototype for exploring how LLMs can help researchers inspect and reason about clinical-trial information.

- Trial parsing and structured summaries.
- Side-by-side trial comparison.
- Failure analysis and hypothesis exploration.
- Explicitly synthetic demonstration scenarios (not real clinical-trial evidence).
- Data-provenance and research-integrity documentation.
- Security documentation describing why browser-side API keys are unsuitable for production.
- Shared defensive JSON-object parsing for model responses.
- Automated tests for malformed output, fenced JSON, missing inputs, provider errors, and content extraction.
- GitHub Actions CI: JSON parsing/provider tests and production build passing.

**Engineering focus:** structured LLM workflows, research-data provenance, source verification, defensive API handling, and scientific caution. The current prototype uses fictional demo records and still calls the provider from the browser; it must not be used with sensitive data. Its test/build CI workflow now passes in GitHub Actions.

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
