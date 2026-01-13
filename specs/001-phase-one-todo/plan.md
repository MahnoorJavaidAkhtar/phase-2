# Implementation Plan: Phase I - Basic Todo Console Application

**Branch**: `001-phase-one-todo` | **Date**: 2026-01-13 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-phase-one-todo/spec.md`

## Summary

Phase I delivers a basic in-memory Python console application for managing todo tasks. Users interact through a menu-based CLI to add, view, update, delete, and mark tasks as complete/incomplete. All data is stored in memory with no persistence beyond runtime. The application implements clean separation between data management (task storage and operations) and user interface (CLI menu and input handling).

**Technical Approach**: Single Python module with clean architecture separating domain logic (Task entity, TaskManager service) from infrastructure (CLI interface). In-memory list storage with auto-incrementing IDs. Menu-driven control flow with comprehensive input validation and error handling.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory (Python list)
**Testing**: Optional (not requested in specification)
**Target Platform**: Console/CLI (cross-platform: Windows, Linux, macOS)
**Project Type**: Single project
**Performance Goals**: Instant response (<1 second) for all operations with up to 100 tasks
**Constraints**: No persistence, no external dependencies, no network, single-user only
**Scale/Scope**: Single user, up to 100 tasks per session, 5 core operations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Spec-Driven Development (MANDATORY)
- ✅ **PASS**: Approved specification exists at `specs/001-phase-one-todo/spec.md`
- ✅ **PASS**: Plan derived strictly from specification requirements
- ✅ **PASS**: No new features introduced beyond spec

### II. Agent Autonomy & Human Oversight
- ✅ **PASS**: Plan awaits user approval before implementation
- ✅ **PASS**: No architectural decisions made without specification basis

### III. Phase Governance
- ✅ **PASS**: Strictly Phase I scope (in-memory console application)
- ✅ **PASS**: No Phase II+ features (no web, API, persistence, authentication)
- ✅ **PASS**: No references to future phases in design

### IV. Technology Stack Constraints
- ✅ **PASS**: Python 3.11+ as specified in constitution
- ✅ **PASS**: No unauthorized frameworks or libraries
- ⚠️ **NOTE**: FastAPI, SQLModel, Neon DB not applicable for Phase I (console app, no persistence)

### V. Quality & Architecture Standards
- ✅ **PASS**: Clean architecture with separated concerns (domain, application, infrastructure)
- ✅ **PASS**: Type hints required (Python type annotations)
- ✅ **PASS**: Error handling strategy defined
- ✅ **PASS**: Input validation strategy defined
- ⚠️ **NOTE**: Stateless services principle not applicable (single-user console app with in-memory state)
- ⚠️ **NOTE**: API-First Design not applicable (no API in Phase I)
- ⚠️ **NOTE**: Observability (structured logging) deferred - simple print statements sufficient for Phase I

### VI. Testing & Validation Requirements
- ✅ **PASS**: Tests not requested in specification, therefore optional per constitution
- ✅ **PASS**: If tests added later, TDD will be mandatory

**Constitution Check Result**: ✅ **PASSED** - All applicable principles satisfied

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-one-todo/
├── spec.md              # Feature specification (completed)
├── plan.md              # This file (implementation plan)
├── data-model.md        # Phase 1 output (task entity definition)
├── quickstart.md        # Phase 1 output (how to run the application)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

**Note**: No `research.md` needed - all technical decisions are straightforward for this simple console application. No `contracts/` directory needed - no external APIs or complex interfaces.

### Source Code (repository root)

```text
src/
├── domain/
│   └── task.py          # Task entity (dataclass with ID, description, status)
├── services/
│   └── task_manager.py  # TaskManager service (CRUD operations, ID generation)
├── cli/
│   └── menu.py          # CLI interface (menu display, input handling, output formatting)
└── main.py              # Application entry point (main loop)

tests/                   # Optional - only if tests requested later
└── unit/
    ├── test_task.py
    ├── test_task_manager.py
    └── test_cli.py
```

**Structure Decision**: Single project structure selected. This is a standalone console application with no web frontend, backend API, or mobile components. The structure follows clean architecture principles:

- **domain/**: Core business entities (Task)
- **services/**: Business logic and operations (TaskManager)
- **cli/**: User interface layer (menu, input/output)
- **main.py**: Application orchestration

This structure allows each layer to be developed and tested independently, and provides a foundation for future phases (Phase II can add API layer without modifying domain/services).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations detected. All constitutional principles are satisfied or not applicable to Phase I scope.

## Phase 0: Research & Technical Decisions

**Status**: ✅ **COMPLETE** - No research needed

All technical decisions are straightforward for this simple console application:

### Decision 1: Data Storage Strategy
- **Decision**: Python list with in-memory storage
- **Rationale**: Specification explicitly requires in-memory storage with no persistence. Python list provides O(1) append, O(n) search by ID, and maintains insertion order.
- **Alternatives Considered**:
  - Dictionary (key=ID, value=Task): Faster lookups but doesn't maintain order naturally
  - Rejected because list is simpler and order maintenance is a requirement (FR-009)

### Decision 2: ID Generation Strategy
- **Decision**: Auto-incrementing integer counter starting at 1
- **Rationale**: Specification requires unique numeric IDs starting from 1 (FR-002). Simple counter ensures uniqueness and sequential assignment.
- **Alternatives Considered**:
  - UUID: Overkill for single-user in-memory application
  - Timestamp-based: Could have collisions, not sequential

### Decision 3: Task Entity Representation
- **Decision**: Python dataclass with three fields (id, description, status)
- **Rationale**: Dataclass provides clean, type-safe entity with automatic __init__, __repr__, and __eq__. Matches specification's Key Entities definition.
- **Alternatives Considered**:
  - Dictionary: Less type-safe, no IDE support
  - Named tuple: Immutable, harder to update status

### Decision 4: CLI Control Flow
- **Decision**: Infinite loop with menu display, input capture, operation dispatch, and error handling
- **Rationale**: Standard pattern for menu-driven console applications. Matches specification's menu-based interface requirement (FR-001).
- **Alternatives Considered**:
  - Command-line arguments: Less interactive, doesn't match spec's menu requirement
  - REPL-style: More complex, unnecessary for simple menu

### Decision 5: Error Handling Strategy
- **Decision**: Try-except blocks with user-friendly error messages, return to menu on error
- **Rationale**: Specification requires graceful error handling (FR-006, FR-011) and clear error messages for invalid operations.
- **Alternatives Considered**:
  - Exceptions propagate to top: Would crash application, violates spec
  - Error codes: Less Pythonic, harder to read

### Decision 6: Input Validation Strategy
- **Decision**: Validate at CLI layer before calling service methods
- **Rationale**: Keeps service layer clean, allows CLI to provide immediate feedback. Validates empty descriptions (FR-004) and numeric IDs (FR-005).
- **Alternatives Considered**:
  - Validate in service layer: Mixes concerns, harder to provide user-friendly messages
  - No validation: Violates specification requirements

## Phase 1: Design & Data Model

### Data Model

See [data-model.md](data-model.md) for complete entity definitions.

**Summary**:
- **Task Entity**: id (int), description (str), status (bool)
- **TaskManager Service**: Manages task list, provides CRUD operations, generates IDs
- **CLI Interface**: Handles user interaction, delegates to TaskManager

### Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         main.py                              │
│                   (Application Entry)                        │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      cli/menu.py                             │
│                   (User Interface Layer)                     │
│  - Display menu                                              │
│  - Capture user input                                        │
│  - Validate input                                            │
│  - Format output                                             │
│  - Handle errors                                             │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│               services/task_manager.py                       │
│                   (Business Logic Layer)                     │
│  - add_task(description) -> Task                             │
│  - get_all_tasks() -> List[Task]                             │
│  - get_task_by_id(id) -> Task | None                         │
│  - update_task(id, description) -> bool                      │
│  - delete_task(id) -> bool                                   │
│  - mark_complete(id) -> bool                                 │
│  - mark_incomplete(id) -> bool                               │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   domain/task.py                             │
│                   (Domain Entity Layer)                      │
│  Task:                                                       │
│    - id: int                                                 │
│    - description: str                                        │
│    - is_complete: bool                                       │
└─────────────────────────────────────────────────────────────┘
```

### Control Flow

1. **Application Start**: `main.py` creates TaskManager instance, starts CLI loop
2. **Menu Display**: CLI displays numbered menu options
3. **User Input**: CLI captures user's menu selection
4. **Input Validation**: CLI validates selection is valid menu option
5. **Operation Dispatch**: CLI calls appropriate TaskManager method
6. **Business Logic**: TaskManager performs operation, returns result
7. **Output Formatting**: CLI formats result for display
8. **Error Handling**: CLI catches errors, displays user-friendly messages
9. **Loop**: Return to step 2 unless user selects Exit

### Key Design Decisions

**Separation of Concerns**:
- **Domain Layer** (task.py): Pure data entity, no business logic
- **Service Layer** (task_manager.py): Business logic, no UI concerns
- **Interface Layer** (menu.py): UI logic, no business logic

**Benefits**:
- Each layer can be tested independently
- Easy to add new interfaces (e.g., API in Phase II) without changing business logic
- Clear responsibility boundaries

**Type Safety**:
- All functions use Python type hints
- Task entity uses dataclass for automatic type checking
- Return types explicitly declared (Task, bool, List[Task], Optional[Task])

**Error Handling**:
- Service layer returns None or False for not-found scenarios
- CLI layer translates these to user-friendly messages
- No exceptions for normal error cases (invalid ID, empty list)
- Exceptions only for unexpected errors (caught at top level)

### Quickstart

See [quickstart.md](quickstart.md) for complete setup and usage instructions.

**Quick Summary**:
```bash
# Run the application
python src/main.py

# Menu options:
# 1. Add Task
# 2. View Tasks
# 3. Update Task
# 4. Delete Task
# 5. Mark Complete
# 6. Mark Incomplete
# 7. Exit
```

## Phase 2: Task Breakdown

**Status**: ⏸️ **PENDING** - Use `/sp.tasks` command to generate tasks.md

Task breakdown will be created by the `/sp.tasks` command based on this plan and the specification. Tasks will follow the structure:
- Phase 1: Setup (project structure, dependencies)
- Phase 2: Domain Layer (Task entity)
- Phase 3: Service Layer (TaskManager)
- Phase 4: Interface Layer (CLI menu)
- Phase 5: Integration (main.py, end-to-end testing)

## Next Steps

1. ✅ **Plan Complete**: This implementation plan is ready for review
2. ⏭️ **User Approval**: Review and approve this plan
3. ⏭️ **Generate Tasks**: Run `/sp.tasks` to create tasks.md
4. ⏭️ **Implementation**: Run `/sp.implement` to execute tasks
5. ⏭️ **Commit & PR**: Run `/sp.git.commit_pr` to commit and create pull request

## Architectural Decision Records (ADRs)

No ADRs required for Phase I. All architectural decisions are straightforward and follow standard patterns for console applications. Future phases may require ADRs for:
- Phase II: Web framework selection, API design patterns
- Phase III: Authentication strategy, multi-user data isolation
- Phase IV: Real-time communication protocol, message queue selection
