# Tasks: Phase I - Basic Todo Console Application

**Input**: Design documents from `/specs/001-phase-one-todo/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md (required)

**Tests**: Tests are NOT requested in the specification, therefore no test tasks are included per constitutional principle VI.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, at repository root
- Paths shown below use single project structure per plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (src/, src/domain/, src/services/, src/cli/)
- [x] T002 Create .gitignore file with Python patterns (__pycache__/, *.pyc, .venv/, venv/, .env*, .DS_Store)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Create Task entity dataclass in src/domain/task.py with id, description, is_complete attributes and type hints per data-model.md
- [x] T004 Create TaskManager class skeleton in src/services/task_manager.py with __init__ method, tasks list, and next_id counter

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View and Add Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks and view the task list in a console interface

**Independent Test**: Launch application, add 2-3 tasks with different descriptions, view list to confirm they appear with IDs, descriptions, and status

**Specification Reference**: spec.md User Story 1, FR-001, FR-002, FR-003, FR-004, FR-007, FR-008, FR-009

**Plan Reference**: plan.md Phase 1 Design & Data Model, Control Flow steps 1-9

### Implementation for User Story 1

- [x] T005 [US1] Implement add_task method in src/services/task_manager.py that creates Task with auto-incremented ID, validates description is provided, appends to tasks list, and returns Task
- [x] T006 [US1] Implement get_all_tasks method in src/services/task_manager.py that returns copy of tasks list in creation order
- [x] T007 [US1] Create CLI menu skeleton in src/cli/menu.py with display_menu function showing 7 numbered options per FR-001
- [x] T008 [US1] Implement get_menu_choice function in src/cli/menu.py that captures user input, validates it's 1-7, handles invalid input per FR-011, and returns choice
- [x] T009 [US1] Implement add_task_flow function in src/cli/menu.py that prompts for description, validates non-empty per FR-004, calls TaskManager.add_task, displays success message with ID
- [x] T010 [US1] Implement view_tasks_flow function in src/cli/menu.py that calls TaskManager.get_all_tasks, formats output with ID/description/status per FR-007, uses [✓] and [ ] markers per FR-008, handles empty list per spec edge cases
- [x] T011 [US1] Create main.py with main function that instantiates TaskManager, displays welcome message, starts infinite menu loop calling display_menu and get_menu_choice, dispatches to add_task_flow and view_tasks_flow for options 1-2, handles option 7 (Exit) per FR-010

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Tasks Complete or Incomplete (Priority: P2)

**Goal**: Enable users to toggle task completion status to track progress

**Independent Test**: Add 2 tasks, mark one complete, view list to confirm status changed, mark it incomplete again to verify toggle works

**Specification Reference**: spec.md User Story 2, FR-005, FR-006, FR-008

**Plan Reference**: plan.md Phase 1 Design & Data Model, TaskManager operations

### Implementation for User Story 2

- [x] T012 [US2] Implement get_task_by_id method in src/services/task_manager.py that searches tasks list for matching ID and returns Task or None if not found
- [x] T013 [US2] Implement mark_complete method in src/services/task_manager.py that calls get_task_by_id, sets is_complete=True if found, returns bool success status
- [x] T014 [US2] Implement mark_incomplete method in src/services/task_manager.py that calls get_task_by_id, sets is_complete=False if found, returns bool success status
- [x] T015 [US2] Implement mark_complete_flow function in src/cli/menu.py that prompts for task ID, validates numeric input, calls TaskManager.mark_complete, displays success or error message per FR-006
- [x] T016 [US2] Implement mark_incomplete_flow function in src/cli/menu.py that prompts for task ID, validates numeric input, calls TaskManager.mark_incomplete, displays success or error message per FR-006
- [x] T017 [US2] Update main.py menu loop to dispatch option 5 to mark_complete_flow and option 6 to mark_incomplete_flow

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Descriptions (Priority: P3)

**Goal**: Enable users to edit task descriptions without deleting and recreating

**Independent Test**: Add task "Buy milk", update to "Buy milk and bread", view list to confirm description changed while ID and status remained same

**Specification Reference**: spec.md User Story 3, FR-004, FR-005, FR-006

**Plan Reference**: plan.md Phase 1 Design & Data Model, TaskManager operations

### Implementation for User Story 3

- [x] T018 [US3] Implement update_task method in src/services/task_manager.py that calls get_task_by_id, updates description if found, returns bool success status
- [x] T019 [US3] Implement update_task_flow function in src/cli/menu.py that prompts for task ID, validates numeric input, prompts for new description, validates non-empty per FR-004, calls TaskManager.update_task, displays success or error message per FR-006
- [x] T020 [US3] Update main.py menu loop to dispatch option 3 to update_task_flow

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Enable users to remove tasks that are no longer relevant

**Independent Test**: Add 3 tasks, delete the second one by ID, view list to confirm only 2 remain and deleted task is gone

**Specification Reference**: spec.md User Story 4, FR-005, FR-006, FR-012

**Plan Reference**: plan.md Phase 1 Design & Data Model, TaskManager operations

### Implementation for User Story 4

- [x] T021 [US4] Implement delete_task method in src/services/task_manager.py that calls get_task_by_id, removes task from list if found per FR-012 (IDs not reused), returns bool success status
- [x] T022 [US4] Implement delete_task_flow function in src/cli/menu.py that prompts for task ID, validates numeric input, calls TaskManager.delete_task, displays success or error message per FR-006
- [x] T023 [US4] Update main.py menu loop to dispatch option 4 to delete_task_flow

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and validation

- [x] T024 Add error handling wrapper in main.py to catch unexpected exceptions, display user-friendly message, and prevent crashes per FR-006
- [x] T025 Add input validation helper in src/cli/menu.py for numeric input that handles ValueError for non-numeric input per spec edge cases
- [x] T026 Verify all functions have Python type hints per plan.md Quality Standards
- [x] T027 Test complete application flow: start app, add 3 tasks, mark one complete, update one description, delete one task, view final list, exit cleanly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on get_task_by_id from T012 but otherwise independent
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on get_task_by_id from T012 but otherwise independent
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Depends on get_task_by_id from T012 but otherwise independent

**Note**: User Stories 2, 3, and 4 all need get_task_by_id (T012), so T012 should be implemented first among those stories.

### Within Each User Story

- Service layer methods before CLI flows
- CLI flows before main.py integration
- All tasks within a story must complete before story is considered done

### Parallel Opportunities

- **Setup tasks**: T001 and T002 can run in parallel (different concerns)
- **Foundational tasks**: T003 and T004 can run in parallel (different files)
- **User Story 1**: T005 and T006 can run in parallel (different methods in same file, but independent)
- **User Story 2**: T013 and T014 can run in parallel (different methods), T015 and T016 can run in parallel (different functions)
- **Once T012 is complete**: User Stories 2, 3, and 4 can be worked on in parallel by different developers

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T004) - CRITICAL
3. Complete Phase 3: User Story 1 (T005-T011)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Application is now minimally functional (can add and view tasks)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T005-T011) → Test independently → MVP complete!
3. Add User Story 2 (T012-T017) → Test independently → Can now track completion
4. Add User Story 3 (T018-T020) → Test independently → Can now edit tasks
5. Add User Story 4 (T021-T023) → Test independently → Can now delete tasks
6. Add Polish (T024-T027) → Final validation → Production ready
7. Each story adds value without breaking previous stories

### Sequential Execution (Recommended for Single Developer)

**Strict Order**:
1. T001 → T002 (Setup)
2. T003 → T004 (Foundational - MUST complete before user stories)
3. T005 → T006 → T007 → T008 → T009 → T010 → T011 (User Story 1 - MVP)
4. T012 → T013 → T014 → T015 → T016 → T017 (User Story 2)
5. T018 → T019 → T020 (User Story 3)
6. T021 → T022 → T023 (User Story 4)
7. T024 → T025 → T026 → T027 (Polish)

**Total**: 27 tasks

---

## Notes

- No [P] markers used because tasks are designed for sequential execution by single developer
- [Story] labels (US1-US4) map tasks to specific user stories for traceability
- Each user story should be independently completable and testable
- No test tasks included - tests are optional per specification and constitution
- Commit after each completed user story phase for incremental progress
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Validation Checklist

- ✅ All tasks follow checkbox format: `- [ ] T### [Story?] Description with file path`
- ✅ Tasks organized by user story (Phase 3-6)
- ✅ Each user story has clear goal and independent test criteria
- ✅ Setup phase (T001-T002) creates project structure
- ✅ Foundational phase (T003-T004) creates base entities before user stories
- ✅ User Story 1 (T005-T011) implements MVP (add and view tasks)
- ✅ User Story 2 (T012-T017) implements completion tracking
- ✅ User Story 3 (T018-T020) implements task editing
- ✅ User Story 4 (T021-T023) implements task deletion
- ✅ Polish phase (T024-T027) adds error handling and validation
- ✅ All tasks reference specific file paths
- ✅ All tasks reference specification requirements (FR-###)
- ✅ All tasks reference plan sections
- ✅ Dependencies clearly documented
- ✅ No test tasks (not requested in specification)
- ✅ Total: 27 atomic, executable tasks
