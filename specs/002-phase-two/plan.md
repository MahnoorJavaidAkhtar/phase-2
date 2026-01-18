# Implementation Plan: Phase II - Full-Stack Web Application

**Branch**: `002-phase-two` | **Date**: 2026-01-18 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-phase-two/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Phase II transforms the Evolution of Todo application from an in-memory console application (Phase I) into a full-stack web application with user authentication and database persistence. The system will provide RESTful API endpoints for todo CRUD operations, user signup/signin via Better Auth, and a responsive Next.js frontend. All todos are associated with authenticated users, ensuring data isolation and multi-user support. Data persists in Neon Serverless PostgreSQL.

## Technical Context

**Language/Version**: Python 3.11+ (backend), TypeScript (frontend)
**Primary Dependencies**: FastAPI, SQLModel, Better Auth, Next.js, React, TailwindCSS
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest (backend, optional), Jest + React Testing Library (frontend, optional)
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge - last 2 versions) + Linux/Windows server for backend
**Project Type**: Web application (frontend + backend)
**Performance Goals**: API operations complete within 2 seconds, page loads within 2 seconds, support 100 concurrent users
**Constraints**: Mobile responsive (minimum 320px width), <2 second response time for all operations, zero cross-user data leakage
**Scale/Scope**: Multi-user web application with authentication, ~6 user stories, 28 functional requirements, 2 data entities (User, Todo)

**Research Needed**:
- NEEDS CLARIFICATION: Better Auth integration pattern with FastAPI backend
- NEEDS CLARIFICATION: Better Auth client setup in Next.js frontend
- NEEDS CLARIFICATION: Neon PostgreSQL connection configuration and best practices
- NEEDS CLARIFICATION: SQLModel schema migration strategy
- NEEDS CLARIFICATION: Session/token management between frontend and backend
- NEEDS CLARIFICATION: Frontend-backend API communication patterns (CORS, authentication headers)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase Governance (Section III)

- [x] **Phase II Scope**: Feature is within Phase II boundaries (full-stack web application with authentication and database)
- [x] **No Phase III+ Features**: No AI frameworks, agent frameworks, container orchestration, message queues, or service mesh
- [x] **Phase I Complete**: Phase I (in-memory console application) was completed before starting Phase II

### Technology Stack Constraints (Section IV - Phase II Matrix)

**Backend Stack Compliance**:
- [x] **Language**: Python 3.11+ ✅
- [x] **API Framework**: FastAPI ✅
- [x] **Database**: Neon Serverless PostgreSQL ✅
- [x] **ORM/Data Layer**: SQLModel ✅
- [x] **Authentication**: Better Auth (or equivalent Python auth library) ✅
- [x] **Testing**: pytest (optional) ✅

**Frontend Stack Compliance**:
- [x] **Framework**: Next.js (React) ✅
- [x] **Language**: TypeScript ✅
- [x] **Styling**: TailwindCSS ✅
- [x] **Authentication Client**: Better Auth client integration ✅
- [x] **Testing**: Jest, React Testing Library (optional) ✅

**Allowed Technologies Check**:
- [x] REST API endpoints ✅
- [x] Database persistence (Neon PostgreSQL) ✅
- [x] User authentication and authorization ✅
- [x] Web frontend (Next.js/React) ✅
- [x] HTTP clients and servers ✅
- [x] Session management ✅
- [x] Multi-user support ✅

**Prohibited Technologies Check**:
- [x] No AI frameworks (OpenAI SDK, LangChain, etc.) ✅
- [x] No Agent frameworks (OpenAI Agents SDK, AutoGPT, etc.) ✅
- [x] No Container orchestration (Kubernetes, Docker Swarm) ✅
- [x] No Message queues (Kafka, RabbitMQ) ✅
- [x] No Service mesh (Dapr, Istio) ✅
- [x] No Advanced cloud infrastructure ✅

### Quality & Architecture Standards (Section V)

- [x] **Clean Architecture**: Will separate domain, application, and infrastructure layers
- [x] **Stateless Services**: Backend API will be stateless (session state in database/auth system)
- [x] **API-First Design**: All functionality exposed via REST API
- [x] **Error Handling**: Will implement explicit error types and structured error responses
- [x] **Type Safety**: Python type hints (backend) + TypeScript strict mode (frontend)
- [x] **Linting**: Will configure ruff (backend) and eslint (frontend)
- [x] **Formatting**: Will use black (backend) and prettier (frontend)

### Testing & Validation Requirements (Section VI)

- [x] **Testing Policy**: Tests are optional per spec (not explicitly requested)
- [x] **TDD Compliance**: If tests are added later, will follow TDD (Red-Green-Refactor)

### Spec-Driven Development (Section I)

- [x] **Specification Approved**: spec.md created and validated
- [x] **No Feature Invention**: Plan derives only from spec requirements
- [x] **Tasks Required**: tasks.md will be created via /sp.tasks before implementation

### Validation Result

✅ **PASSED** - All constitutional requirements met. No violations. Ready to proceed with Phase 0 research.

## Project Structure

### Documentation (this feature)

```text
specs/002-phase-two/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   ├── auth-api.yaml    # Authentication endpoints
│   └── todo-api.yaml    # Todo CRUD endpoints
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/          # SQLModel data models (User, Todo)
│   ├── services/        # Business logic layer
│   ├── api/             # FastAPI routes and controllers
│   │   ├── auth.py      # Authentication endpoints
│   │   └── todos.py     # Todo CRUD endpoints
│   ├── middleware/      # Auth middleware, CORS, error handling
│   ├── database.py      # Neon PostgreSQL connection
│   └── main.py          # FastAPI application entry point
├── tests/               # Optional tests
│   ├── contract/        # API contract tests
│   ├── integration/     # Integration tests
│   └── unit/            # Unit tests
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variables template

frontend/
├── src/
│   ├── app/             # Next.js App Router pages
│   │   ├── (auth)/      # Auth route group
│   │   │   ├── signup/  # Signup page
│   │   │   └── signin/  # Signin page
│   │   ├── (dashboard)/ # Protected route group
│   │   │   └── todos/   # Todo list page
│   │   └── layout.tsx   # Root layout
│   ├── components/      # React components
│   │   ├── auth/        # Auth-related components
│   │   ├── todos/       # Todo-related components
│   │   └── ui/          # Shared UI components
│   ├── lib/             # Utilities and helpers
│   │   ├── api.ts       # API client for backend communication
│   │   └── auth.ts      # Better Auth client configuration
│   └── types/           # TypeScript type definitions
├── tests/               # Optional tests
├── package.json         # Node dependencies
├── tsconfig.json        # TypeScript configuration
├── tailwind.config.js   # TailwindCSS configuration
└── .env.local.example   # Environment variables template
```

**Structure Decision**: Selected web application structure (Option 2) with separate backend/ and frontend/ directories. This separation enables:
- Independent deployment of frontend and backend
- Clear technology boundaries (Python backend, TypeScript frontend)
- Parallel development of frontend and backend teams
- Simplified dependency management per stack

---

## Phase 0: Research & Technical Decisions

The following research tasks will resolve all NEEDS CLARIFICATION items from Technical Context.
