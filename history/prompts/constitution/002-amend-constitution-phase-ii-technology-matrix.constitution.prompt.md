---
id: 002
title: Amend constitution Phase II technology matrix
stage: constitution
date: 2026-01-18
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-phase-one-todo
user: user
command: /sp.constitution
labels: ["constitution", "phase-governance", "technology-stack", "phase-ii"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Amend the global constitution technology matrix to reflect Phase II requirements as follows:

Phase II:
- Backend: Python REST API
- Database: Neon Serverless PostgreSQL
- ORM/Data layer: SQLModel or equivalent
- Frontend: Next.js (React, TypeScript)
- Authentication: Better Auth (signup/signin)
- Architecture: Full-stack web application

Phase I remains:
- In-memory console application only

Phase III and later:
- Advanced cloud infrastructure, agents, AI, orchestration

Rules:
- Authentication is allowed starting Phase II
- Web frontend is allowed starting Phase II
- Neon PostgreSQL is allowed starting Phase II
- No AI or agent frameworks until later phases

This amendment must preserve phase isolation and act as the authoritative technology policy.

## Response snapshot

Constitution amended from version 1.0.0 to 1.1.0 (MINOR version bump).

**Changes Made**:

1. **Section III (Phase Governance)**: Restructured phase boundaries to clearly define:
   - Phase I: In-memory console application (no web, no database, no auth)
   - Phase II: Full-stack web application (REST API, Neon PostgreSQL, Next.js, Better Auth)
   - Phase III+: Advanced cloud infrastructure (AI, agents, orchestration)

   Added explicit "Technology Allowances by Phase" subsection.

2. **Section IV (Technology Stack Constraints)**: Complete restructure into phase-specific technology matrices:
   - **Phase I Matrix**: Python console only, in-memory storage, explicitly prohibits web frameworks, databases, ORMs, authentication, file persistence, AI/agent frameworks
   - **Phase II Matrix**: Full backend stack (FastAPI, Neon PostgreSQL, SQLModel, Better Auth) + frontend stack (Next.js, TypeScript, TailwindCSS), explicitly prohibits AI frameworks, agent frameworks, container orchestration, message queues
   - **Phase III+ Matrix**: Adds AI/ML frameworks, agent frameworks, Docker, Kubernetes, Kafka, service mesh, observability tools, cloud platforms

   Added "Technology Exception Process" with clear requirements for substitutions.

3. **Sync Impact Report**: Updated at top of file documenting version change, modified sections, and template validation status.

4. **Version Metadata**: Updated footer to version 1.1.0, last amended 2026-01-18.

**Validation**: All templates (spec-template.md, plan-template.md, tasks-template.md) reviewed and confirmed no changes required as they remain technology-agnostic and reference constitution checks appropriately.

## Outcome

- ✅ Impact: Constitution now serves as authoritative technology policy with phase-specific matrices enforcing strict technology discipline
- 🧪 Tests: N/A (documentation change)
- 📁 Files: 1 file modified (.specify/memory/constitution.md)
- 🔁 Next prompts: Ready for Phase II specification and planning work with clear technology boundaries
- 🧠 Reflection: MINOR version bump appropriate as this adds materially expanded guidance without removing or redefining existing principles. Phase isolation now enforced through explicit allow/prohibit lists.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
