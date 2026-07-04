# 🚀 Catalyst

Catalyst is an AI-powered interview intelligence platform that transforms technical interview recordings and transcripts into structured insights, automated summaries, analytics, and searchable knowledge to help engineering organizations improve hiring quality.

---

## Why Catalyst?

Engineering organizations conduct hundreds of technical interviews every month, but most interview feedback is subjective, inconsistent, and difficult to analyze at scale.

Catalyst transforms interview recordings and transcripts into structured insights using AI, enabling teams to:

- Evaluate candidate performance consistently
- Identify interviewer bias and inconsistencies
- Generate interview summaries automatically
- Measure hiring quality using analytics
- Build searchable interview knowledge bases

---

## Key Features

- 🤖 AI-powered interview analysis
- 🎙️ Transcript processing
- 📝 Automated interview summaries
- 📊 Candidate evaluation analytics
- 📈 Interviewer quality & bias metrics
- 🔍 Semantic search
- ☸️ Cloud-native microservice architecture
- 🔐 Authentication & RBAC

---


## Current Progress

### ✅ Milestone 1: Project Foundation

* Project structure established
* Dependency management with `uv`
* Code quality tooling configured
* Continuous Integration (CI) pipeline implemented
* Initial project documentation

### ✅ Milestone 2: Backend Foundation

* FastAPI application factory pattern
* Environment-based configuration using `pydantic-settings`
* Structured logging with Loguru
* Health check endpoint
* API versioning structure
* CORS middleware
* Global exception handling
* Application lifespan management
* PostgreSQL integration with SQLAlchemy 2.0 (Async)
* Database engine and session management
* Dependency injection for database sessions
* Alembic migration infrastructure
* Async Alembic configuration
* Reusable declarative `Base` model
* Reusable `TimestampMixin`
* First production domain model (`Interview`)
* First production database migration

### Tech Stack

* Python 3.11+
* FastAPI
* SQLAlchemy 2.0
* Alembic
* PostgreSQL
* Pydantic v2
* Loguru
* uv
