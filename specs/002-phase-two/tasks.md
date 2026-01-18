# Tasks: Phase II - Full-Stack Web Application

**Input**: Design documents from `/specs/002-phase-two/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - not explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below follow the web application structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure (backend/src/models/, backend/src/services/, backend/src/api/, backend/src/middleware/)
- [x] T002 Create frontend directory structure (frontend/src/app/, frontend/src/components/, frontend/src/lib/, frontend/src/types/)
- [x] T003 [P] Initialize Python project with requirements.txt (fastapi, sqlmodel, psycopg2-binary, alembic, python-jose, passlib, python-multipart, pydantic-settings, uvicorn)
- [x] T004 [P] Initialize Next.js project with package.json (next, react, react-dom, typescript, tailwindcss)
- [x] T005 [P] Create backend/.env.example with DATABASE_URL, SECRET_KEY, CORS_ORIGINS placeholders
- [x] T006 [P] Create frontend/.env.local.example with NEXT_PUBLIC_API_URL placeholder
- [x] T007 [P] Configure TailwindCSS in frontend/tailwind.config.js
- [x] T008 [P] Configure TypeScript in frontend/tsconfig.json with strict mode

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Create Neon PostgreSQL database and obtain pooled connection string
- [x] T010 Configure database connection in backend/src/database.py (SQLModel engine with pool_size=5, pool_pre_ping=True, pool_recycle=3600)
- [x] T011 Initialize Alembic in backend/alembic/ directory
- [x] T012 Configure Alembic env.py to use SQLModel.metadata and Neon connection string
- [x] T013 [P] Create User model in backend/src/models/user.py (id, email, password_hash, created_at, updated_at)
- [x] T014 [P] Create Todo model in backend/src/models/todo.py (id, user_id, title, description, is_complete, created_at, updated_at)
- [x] T015 Create initial Alembic migration for users and todos tables
- [x] T016 Apply Alembic migration to Neon database (alembic upgrade head)
- [x] T017 [P] Create password hashing utilities in backend/src/services/auth_utils.py (hash_password, verify_password using passlib)
- [x] T018 [P] Create JWT token utilities in backend/src/services/auth_utils.py (create_access_token, decode_token using python-jose)
- [x] T019 Create auth dependency in backend/src/middleware/auth.py (get_current_user dependency for protected routes)
- [x] T020 Configure CORS middleware in backend/src/main.py (allow_origins from env, allow_credentials=True)
- [x] T021 Create FastAPI app instance in backend/src/main.py with title and version
- [x] T022 [P] Create API client in frontend/src/lib/api-client.ts (custom fetch-based client with auth header support)
- [x] T023 [P] Create TypeScript types in frontend/src/types/index.ts (User, Todo, TodoCreate, TodoUpdate interfaces)

**Checkpoint**: ✅ Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable users to sign up, sign in, and sign out with JWT authentication

**Independent Test**: Complete signup flow, sign out, sign back in, verify session management

### Implementation for User Story 1

- [x] T024 [P] [US1] Create signup endpoint POST /auth/signup in backend/src/api/auth.py (validate email, hash password, create user)
- [x] T025 [P] [US1] Create login endpoint POST /auth/token in backend/src/api/auth.py (validate credentials, return JWT, set HTTP-only cookie)
- [x] T026 [P] [US1] Create logout endpoint POST /auth/logout in backend/src/api/auth.py (clear auth cookie)
- [x] T027 [P] [US1] Create get current user endpoint GET /auth/me in backend/src/api/auth.py (return authenticated user info)
- [x] T028 [US1] Register auth routes in backend/src/main.py
- [x] T029 [P] [US1] Create signup page in frontend/src/app/(auth)/signup/page.tsx (email/password form, call signup API)
- [x] T030 [P] [US1] Create signin page in frontend/src/app/(auth)/signin/page.tsx (email/password form, call login API, redirect to todos)
- [x] T031 [P] [US1] Create auth utilities in frontend/src/lib/auth.ts (login, logout, getCurrentUser functions)
- [x] T032 [US1] Implement auth state management in frontend/src/app/layout.tsx (check auth status, redirect logic)
- [x] T033 [US1] Create protected route wrapper in frontend/src/components/auth/ProtectedRoute.tsx (redirect to signin if not authenticated)
- [x] T034 [US1] Add error handling for auth failures in frontend/src/components/auth/ (display error messages)
- [ ] T035 [US1] Test signup flow: create account, verify user in database, verify auto-signin
- [ ] T036 [US1] Test signin flow: login with credentials, verify JWT token, verify redirect to todos page
- [ ] T037 [US1] Test logout flow: sign out, verify cookie cleared, verify redirect to signin page
- [ ] T038 [US1] Test protected route access: attempt to access /todos without auth, verify redirect to signin

**Checkpoint**: ✅ Backend authentication complete and tested. Frontend pages created. Ready for manual testing.

---

## Phase 4: User Story 2 - View Personal Todo List (Priority: P2)

**Goal**: Display all todos for authenticated user with empty state handling

**Independent Test**: Sign in, view todo list page, verify only user's todos displayed, test empty state

### Implementation for User Story 2

- [ ] T039 [US2] Create GET /api/todos endpoint in backend/src/api/todos.py (fetch todos for current user, filter by user_id)
- [ ] T040 [US2] Implement user-scoped query in backend/src/services/todo_service.py (query todos WHERE user_id = current_user.id)
- [ ] T041 [US2] Register todos routes in backend/src/main.py
- [ ] T042 [US2] Create todo list page in frontend/src/app/(dashboard)/todos/page.tsx (fetch and display todos)
- [ ] T043 [P] [US2] Create TodoList component in frontend/src/components/todos/TodoList.tsx (render list of todos)
- [ ] T044 [P] [US2] Create TodoItem component in frontend/src/components/todos/TodoItem.tsx (display single todo with title, description, status)
- [ ] T045 [US2] Create EmptyState component in frontend/src/components/todos/EmptyState.tsx (display when no todos exist)
- [ ] T046 [US2] Implement responsive layout in frontend/src/app/(dashboard)/layout.tsx (mobile-friendly, min 320px width)
- [ ] T047 [US2] Add loading state in frontend/src/components/todos/TodoList.tsx (show spinner while fetching)
- [ ] T048 [US2] Test view todos: sign in, create todos via API, verify todos displayed on page
- [ ] T049 [US2] Test empty state: sign in with no todos, verify empty state message displayed
- [ ] T050 [US2] Test data isolation: create two users, verify each sees only their own todos
- [ ] T051 [US2] Test responsive design: resize to 320px width, verify UI remains usable

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Create New Todos (Priority: P3)

**Goal**: Enable users to add new todos with title and optional description

**Independent Test**: Sign in, create todo with title and description, verify it appears in list and persists in database

### Implementation for User Story 3

- [ ] T052 [US3] Create POST /api/todos endpoint in backend/src/api/todos.py (create todo, associate with current user)
- [ ] T053 [US3] Implement create todo logic in backend/src/services/todo_service.py (validate title, set user_id, save to database)
- [ ] T054 [US3] Add title validation in backend/src/api/todos.py (ensure title is not empty, max 500 chars)
- [ ] T055 [P] [US3] Create AddTodoForm component in frontend/src/components/todos/AddTodoForm.tsx (title and description inputs)
- [ ] T056 [P] [US3] Create AddTodoButton component in frontend/src/components/todos/AddTodoButton.tsx (trigger form modal/inline)
- [ ] T057 [US3] Implement form submission in frontend/src/components/todos/AddTodoForm.tsx (call POST /api/todos, refresh list)
- [ ] T058 [US3] Add client-side validation in frontend/src/components/todos/AddTodoForm.tsx (require title, show error if empty)
- [ ] T059 [US3] Add success feedback in frontend/src/components/todos/AddTodoForm.tsx (show success message, clear form)
- [ ] T060 [US3] Test create todo with title and description: verify todo appears in list immediately
- [ ] T061 [US3] Test create todo with title only: verify todo created with empty description
- [ ] T062 [US3] Test validation: attempt to create todo without title, verify error message displayed
- [ ] T063 [US3] Test persistence: create todo, refresh page, verify todo still appears

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Toggle Todo Completion Status (Priority: P4)

**Goal**: Allow users to mark todos as complete or incomplete

**Independent Test**: Create todo, toggle to complete, verify visual change and persistence, toggle back to incomplete

### Implementation for User Story 4

- [ ] T064 [US4] Create POST /api/todos/{id}/toggle endpoint in backend/src/api/todos.py (toggle is_complete status)
- [ ] T065 [US4] Implement toggle logic in backend/src/services/todo_service.py (flip is_complete boolean, update updated_at)
- [ ] T066 [US4] Add authorization check in backend/src/api/todos.py (verify todo belongs to current user)
- [ ] T067 [US4] Add checkbox UI in frontend/src/components/todos/TodoItem.tsx (clickable checkbox for completion status)
- [ ] T068 [US4] Implement toggle handler in frontend/src/components/todos/TodoItem.tsx (call POST /api/todos/{id}/toggle)
- [ ] T069 [US4] Add visual distinction in frontend/src/components/todos/TodoItem.tsx (strikethrough or different color for completed todos)
- [ ] T070 [US4] Add optimistic UI update in frontend/src/components/todos/TodoItem.tsx (update UI immediately, rollback on error)
- [ ] T071 [US4] Test toggle to complete: mark todo complete, verify visual change, verify persists on refresh
- [ ] T072 [US4] Test toggle to incomplete: mark completed todo incomplete, verify visual change reverts
- [ ] T073 [US4] Test authorization: attempt to toggle another user's todo, verify 403 error

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Edit Existing Todos (Priority: P5)

**Goal**: Enable users to update todo title and description

**Independent Test**: Create todo, edit title and description, verify changes saved and displayed

### Implementation for User Story 5

- [ ] T074 [US5] Create PUT /api/todos/{id} endpoint in backend/src/api/todos.py (update todo title and description)
- [ ] T075 [US5] Implement update logic in backend/src/services/todo_service.py (validate title, update fields, set updated_at)
- [ ] T076 [US5] Add authorization check in backend/src/api/todos.py (verify todo belongs to current user)
- [ ] T077 [P] [US5] Create EditTodoForm component in frontend/src/components/todos/EditTodoForm.tsx (pre-filled form with title and description)
- [ ] T078 [P] [US5] Create EditTodoButton component in frontend/src/components/todos/EditTodoButton.tsx (trigger edit mode)
- [ ] T079 [US5] Implement edit mode toggle in frontend/src/components/todos/TodoItem.tsx (switch between view and edit modes)
- [ ] T080 [US5] Implement form submission in frontend/src/components/todos/EditTodoForm.tsx (call PUT /api/todos/{id}, update list)
- [ ] T081 [US5] Add cancel button in frontend/src/components/todos/EditTodoForm.tsx (revert to view mode without saving)
- [ ] T082 [US5] Add client-side validation in frontend/src/components/todos/EditTodoForm.tsx (require title, show error if empty)
- [ ] T083 [US5] Test edit todo: modify title and description, verify changes saved and displayed
- [ ] T084 [US5] Test validation: clear title during edit, verify error message, verify changes not saved
- [ ] T085 [US5] Test cancel: start editing, make changes, cancel, verify original values remain
- [ ] T086 [US5] Test authorization: attempt to edit another user's todo, verify 403 error

**Checkpoint**: At this point, User Stories 1-5 should all work independently

---

## Phase 8: User Story 6 - Delete Todos (Priority: P6)

**Goal**: Allow users to permanently delete todos

**Independent Test**: Create todo, delete it, verify it no longer appears in list and is removed from database

### Implementation for User Story 6

- [ ] T087 [US6] Create DELETE /api/todos/{id} endpoint in backend/src/api/todos.py (delete todo from database)
- [ ] T088 [US6] Implement delete logic in backend/src/services/todo_service.py (remove todo record)
- [ ] T089 [US6] Add authorization check in backend/src/api/todos.py (verify todo belongs to current user)
- [ ] T090 [P] [US6] Create DeleteTodoButton component in frontend/src/components/todos/DeleteTodoButton.tsx (delete button with confirmation)
- [ ] T091 [P] [US6] Create ConfirmDialog component in frontend/src/components/ui/ConfirmDialog.tsx (reusable confirmation modal)
- [ ] T092 [US6] Implement delete handler in frontend/src/components/todos/TodoItem.tsx (call DELETE /api/todos/{id}, remove from list)
- [ ] T093 [US6] Add confirmation prompt in frontend/src/components/todos/DeleteTodoButton.tsx (show "Are you sure?" dialog)
- [ ] T094 [US6] Add optimistic UI update in frontend/src/components/todos/TodoItem.tsx (remove from list immediately, rollback on error)
- [ ] T095 [US6] Test delete todo: delete todo, verify it disappears from list immediately
- [ ] T096 [US6] Test persistence: delete todo, refresh page, verify todo does not reappear
- [ ] T097 [US6] Test confirmation: click delete, cancel confirmation, verify todo remains
- [ ] T098 [US6] Test authorization: attempt to delete another user's todo, verify 403 error

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T099 [P] Add structured error responses in backend/src/middleware/error_handler.py (consistent error format)
- [ ] T100 [P] Add request logging in backend/src/middleware/logging.py (log all API requests)
- [ ] T101 [P] Create error boundary in frontend/src/components/ErrorBoundary.tsx (catch React errors)
- [ ] T102 [P] Create toast notification system in frontend/src/components/ui/Toast.tsx (success/error messages)
- [ ] T103 [P] Add loading spinner component in frontend/src/components/ui/Spinner.tsx (reusable loading indicator)
- [ ] T104 Implement global error handling in frontend/src/lib/api-client.ts (handle network errors, 401, 403, 500)
- [ ] T105 Add API health check endpoint GET /health in backend/src/main.py (verify database connectivity)
- [ ] T106 Configure backend linting with ruff in backend/pyproject.toml
- [ ] T107 Configure backend formatting with black in backend/pyproject.toml
- [ ] T108 Configure frontend linting with eslint in frontend/.eslintrc.json
- [ ] T109 Configure frontend formatting with prettier in frontend/.prettierrc
- [ ] T110 Update quickstart.md with actual setup steps and troubleshooting
- [ ] T111 Test complete user journey: signup → signin → create todo → toggle → edit → delete → logout
- [ ] T112 Test responsive design across all pages (320px to 1920px width)
- [ ] T113 Test error scenarios: network failures, invalid inputs, unauthorized access
- [ ] T114 Verify zero cross-user data leakage: create multiple users, verify complete isolation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5 → P6)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories (but logically follows US1 for auth)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - No dependencies on other stories

**Note**: While user stories are technically independent after Foundational phase, the logical flow is US1 (auth) → US2 (view) → US3 (create) → US4 (toggle) → US5 (edit) → US6 (delete) for a complete user experience.

### Within Each User Story

- Backend endpoints before frontend UI
- Models and services before API routes
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Within each user story, tasks marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch backend auth endpoints in parallel:
Task T024: "Create signup endpoint POST /auth/signup in backend/src/api/auth.py"
Task T025: "Create login endpoint POST /auth/token in backend/src/api/auth.py"
Task T026: "Create logout endpoint POST /auth/logout in backend/src/api/auth.py"
Task T027: "Create get current user endpoint GET /auth/me in backend/src/api/auth.py"

# Launch frontend auth pages in parallel:
Task T029: "Create signup page in frontend/src/app/(auth)/signup/page.tsx"
Task T030: "Create signin page in frontend/src/app/(auth)/signin/page.tsx"
Task T031: "Create auth utilities in frontend/src/lib/auth.ts"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Authentication)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Authentication)
   - Developer B: User Story 2 (View Todos) - can work on UI while A does auth
   - Developer C: User Story 3 (Create Todos)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Tests are OPTIONAL (not requested in spec) - focus on implementation
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
