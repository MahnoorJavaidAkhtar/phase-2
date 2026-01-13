<!--
Sync Impact Report:
- Version: NEW → 1.0.0 (Initial constitution for Evolution of Todo project)
- Modified Principles: N/A (initial creation)
- Added Sections: All sections (initial creation)
- Removed Sections: None
- Templates Status:
  ✅ spec-template.md - Reviewed, aligns with SDD mandate
  ✅ plan-template.md - Reviewed, aligns with constitution check requirement
  ✅ tasks-template.md - Reviewed, aligns with phase-based execution
- Follow-up TODOs: None
-->

# Evolution of Todo Project Constitution

## Core Principles

### I. Spec-Driven Development (MANDATORY)

**No agent may write code without approved specifications and tasks.**

All development work MUST follow this strict sequence:
1. **Constitution** → Defines project-wide principles and constraints
2. **Specification** → Captures user requirements and acceptance criteria
3. **Plan** → Defines technical approach and architecture decisions
4. **Tasks** → Breaks down implementation into testable units
5. **Implementation** → Agents execute approved tasks only

**Rationale**: Spec-Driven Development ensures all work is traceable, intentional, and aligned with user requirements. It prevents scope creep, feature invention, and architectural drift.

**Non-Negotiable Rules**:
- Agents MUST NOT write production code without an approved spec.md and tasks.md
- Agents MUST NOT invent features or requirements not explicitly specified
- All refinements MUST occur at the specification level, not during implementation
- Any deviation from approved specifications requires explicit user approval and spec update

### II. Agent Autonomy & Human Oversight

**Agents execute; humans decide.**

Agents are autonomous executors of approved specifications. Humans provide requirements, approve plans, and make architectural decisions.

**Agent Responsibilities**:
- Execute tasks from approved tasks.md files
- Report blockers and ambiguities immediately
- Suggest architectural decisions but never implement without approval
- Create Prompt History Records (PHRs) for all interactions
- Propose Architecture Decision Records (ADRs) for significant decisions

**Human Responsibilities**:
- Define requirements and acceptance criteria
- Approve specifications, plans, and tasks before implementation
- Make architectural decisions when multiple valid approaches exist
- Resolve ambiguities and provide clarifications
- Review and approve ADRs

**Prohibited Agent Behaviors**:
- Manual coding by humans (agents execute all implementation)
- Feature invention or scope expansion beyond specifications
- Architectural decisions without human approval
- Implementation before spec/plan/tasks approval
- Deviation from approved specifications without explicit consent

**Rationale**: Clear separation of concerns ensures agents work efficiently within defined boundaries while humans maintain strategic control.

### III. Phase Governance

**Each phase is strictly scoped by its specification. Future-phase features MUST NOT leak into earlier phases.**

The Evolution of Todo project spans five phases (Phase I through Phase V). Each phase:
- Has its own specification defining scope and deliverables
- Builds incrementally on previous phases
- MUST NOT include features designated for future phases
- May only evolve architecture through updated specs and plans

**Phase Boundaries**:
- **Phase I**: Core todo functionality (CLI-based, local storage)
- **Phase II**: Web interface and basic API
- **Phase III**: Multi-user support and authentication
- **Phase IV**: Real-time collaboration and notifications
- **Phase V**: Advanced features (AI, integrations, analytics)

**Enforcement Rules**:
- Agents MUST verify current phase before implementing any feature
- Any feature request MUST be validated against current phase scope
- Cross-phase dependencies MUST be explicitly documented in specifications
- Architecture evolution MUST be documented via ADRs and reflected in updated specs

**Rationale**: Strict phase governance prevents premature optimization, maintains focus on current deliverables, and ensures each phase delivers a complete, testable increment.

### IV. Technology Stack Constraints

**Technology choices are fixed to ensure consistency and maintainability.**

**Backend Stack**:
- **Language**: Python 3.11+
- **API Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon DB (PostgreSQL-compatible)
- **Agent Framework**: OpenAI Agents SDK
- **Tool Protocol**: Model Context Protocol (MCP)

**Frontend Stack** (Phase II+):
- **Framework**: Next.js (React)
- **Language**: TypeScript
- **Styling**: TailwindCSS (or as specified in phase specs)

**Infrastructure Stack** (Phase IV+):
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Messaging**: Kafka
- **Service Mesh**: Dapr

**Rationale**: Fixed technology choices reduce decision fatigue, ensure team expertise alignment, and maintain architectural consistency across phases.

**Exceptions**: Technology substitutions require:
1. Documented justification in an ADR
2. User approval
3. Updated constitution and phase specifications
4. Migration plan for existing code

### V. Quality & Architecture Standards

**Clean architecture and stateless services are mandatory where applicable.**

**Architecture Principles**:
- **Clean Architecture**: Separate concerns (domain, application, infrastructure layers)
- **Stateless Services**: Services MUST NOT maintain session state (use external state stores)
- **API-First Design**: All functionality exposed via well-defined APIs
- **Idempotency**: Write operations MUST be idempotent where possible
- **Error Handling**: Explicit error types, structured error responses
- **Observability**: Structured logging, metrics, and tracing required

**Code Quality Standards**:
- **Type Safety**: Full type annotations (Python type hints, TypeScript strict mode)
- **Linting**: Code MUST pass configured linters (ruff, eslint)
- **Formatting**: Consistent formatting (black, prettier)
- **Documentation**: Public APIs MUST have docstrings/JSDoc
- **Complexity**: Cyclomatic complexity <10 per function (justify exceptions in ADRs)

**Rationale**: Quality standards ensure maintainability, scalability, and team velocity over the project lifecycle.

### VI. Testing & Validation Requirements

**Tests are optional but when included MUST follow Test-Driven Development (TDD).**

**Testing Policy**:
- Tests are OPTIONAL unless explicitly requested in feature specifications
- When tests ARE requested, TDD is MANDATORY:
  1. Write tests FIRST
  2. Ensure tests FAIL (Red)
  3. Implement feature (Green)
  4. Refactor (Refactor)

**Test Categories** (when applicable):
- **Contract Tests**: Verify API contracts and interfaces
- **Integration Tests**: Verify component interactions
- **Unit Tests**: Verify individual function behavior
- **End-to-End Tests**: Verify complete user journeys

**Test Requirements** (when tests are included):
- Tests MUST be written before implementation
- Tests MUST fail before implementation begins
- All tests MUST pass before task completion
- Test coverage targets defined per-phase in specifications

**Rationale**: Optional testing with mandatory TDD when tests are requested balances velocity with quality, allowing rapid prototyping while ensuring rigor when needed.

## Development Workflow

### Specification Workflow

1. **User Input**: User provides feature description or requirement
2. **Specification Creation** (`/sp.specify`): Agent creates spec.md with user stories and acceptance criteria
3. **Clarification** (`/sp.clarify`): Agent identifies ambiguities and asks targeted questions
4. **User Approval**: User reviews and approves specification
5. **Planning** (`/sp.plan`): Agent creates implementation plan with architecture decisions
6. **Task Generation** (`/sp.tasks`): Agent breaks down plan into executable tasks
7. **Implementation** (`/sp.implement`): Agent executes approved tasks
8. **Commit & PR** (`/sp.git.commit_pr`): Agent commits changes and creates pull request

### Prompt History Records (PHRs)

**Every user interaction MUST be recorded in a PHR.**

**PHR Creation Rules**:
- Create PHR after completing any user request
- Route PHRs to appropriate subdirectory:
  - `history/prompts/constitution/` for constitution-related work
  - `history/prompts/<feature-name>/` for feature-specific work
  - `history/prompts/general/` for general queries
- Capture full user input (verbatim, not truncated)
- Include representative agent response
- Fill all metadata fields (stage, date, model, files, tests)

**PHR Stages**:
- `constitution`: Constitution creation/updates
- `spec`: Specification work
- `plan`: Planning and architecture
- `tasks`: Task breakdown
- `red`: Writing failing tests
- `green`: Implementing features
- `refactor`: Code refactoring
- `explainer`: Documentation and explanations
- `misc`: Other feature-related work
- `general`: Non-feature work

### Architecture Decision Records (ADRs)

**Significant architectural decisions MUST be documented in ADRs.**

**ADR Trigger Test** (all three must be true):
1. **Impact**: Does this decision have long-term consequences? (e.g., framework choice, data model, API design, security approach, platform selection)
2. **Alternatives**: Were multiple viable options considered?
3. **Scope**: Is this decision cross-cutting and influential to system design?

**ADR Suggestion Process**:
- Agent detects significant decision during planning or implementation
- Agent suggests: "📋 Architectural decision detected: [brief description]. Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`"
- Wait for user consent
- Never auto-create ADRs

**ADR Storage**: `history/adr/`

## Compliance & Enforcement

### Constitution Supremacy

This constitution supersedes all other practices, guidelines, and conventions. In case of conflict:
1. Constitution principles take precedence
2. Phase specifications must align with constitution
3. Implementation plans must comply with constitution
4. Tasks must enforce constitutional requirements

### Validation Gates

**Pre-Implementation Gates**:
- [ ] Specification approved by user
- [ ] Plan includes Constitution Check section
- [ ] All technology choices comply with Section IV
- [ ] Phase scope verified against Section III
- [ ] Tasks reference approved spec and plan

**Post-Implementation Gates**:
- [ ] All tasks completed as specified
- [ ] Tests pass (if tests were requested)
- [ ] Code quality standards met (Section V)
- [ ] PHR created for the work session
- [ ] ADRs created for significant decisions (if applicable)

### Amendment Process

**Constitution amendments require**:
1. Documented justification (why amendment needed)
2. Impact analysis (what changes across specs/plans/tasks)
3. User approval
4. Version bump following semantic versioning:
   - **MAJOR**: Backward-incompatible changes (principle removal/redefinition)
   - **MINOR**: New principles or materially expanded guidance
   - **PATCH**: Clarifications, wording fixes, non-semantic refinements
5. Migration plan for existing specifications and code
6. Update to all dependent templates and documentation

### Complexity Justification

Any violation of constitutional principles MUST be justified:
- Document in plan.md "Complexity Tracking" section
- Explain why needed
- Explain why simpler alternatives were rejected
- Obtain user approval
- Consider creating an ADR for the decision

## Governance

**Authority**: This constitution is the authoritative governance document for the Evolution of Todo project.

**Scope**: All agents, all phases, all features, all code.

**Enforcement**:
- All pull requests MUST verify constitutional compliance
- All specifications MUST include Constitution Check section
- All plans MUST validate against constitutional principles
- Agents MUST refuse non-compliant requests and cite relevant principle

**Review Cycle**: Constitution reviewed at phase boundaries (before starting new phase).

**Runtime Guidance**: Agents follow `CLAUDE.md` for operational instructions; constitution defines strategic principles.

---

**Version**: 1.0.0 | **Ratified**: 2026-01-13 | **Last Amended**: 2026-01-13
