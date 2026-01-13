# Data Model: Phase I - Basic Todo Console Application

**Feature**: Phase I Todo Application
**Created**: 2026-01-13
**Status**: Design Complete

## Overview

Phase I uses a simple in-memory data model with a single entity (Task) and a service layer (TaskManager) for business operations. No persistence layer is required.

## Entities

### Task

Represents a single todo item in the system.

**Attributes**:

| Attribute | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| id | int | Yes | Auto-generated | Positive integer, unique | Unique identifier assigned at creation, starts at 1 and increments |
| description | str | Yes | None | Non-empty, no whitespace-only | Text describing what needs to be done |
| is_complete | bool | Yes | False | True or False | Completion status of the task |

**Validation Rules**:
- `description` MUST NOT be empty string
- `description` MUST NOT be whitespace-only (e.g., "   ")
- `id` MUST be unique across all tasks
- `id` MUST be positive integer (>= 1)
- `is_complete` defaults to False when task is created

**State Transitions**:
```
[Created] → is_complete = False
    ↓
[Mark Complete] → is_complete = True
    ↓
[Mark Incomplete] → is_complete = False
    ↓
[Mark Complete] → is_complete = True
    (can toggle indefinitely)
```

**Lifecycle**:
1. **Creation**: Task created with auto-generated ID, provided description, is_complete=False
2. **Active**: Task exists in memory, can be viewed, updated, marked complete/incomplete
3. **Deletion**: Task removed from memory, ID not reused
4. **Session End**: All tasks lost when application exits (no persistence)

**Implementation Notes**:
- Use Python `dataclass` for clean, type-safe implementation
- ID generation handled by TaskManager, not Task entity
- Task entity is immutable except for `description` and `is_complete` fields
- Task entity has no methods (pure data structure)

**Example**:
```python
Task(id=1, description="Buy groceries", is_complete=False)
Task(id=2, description="Write report", is_complete=True)
Task(id=3, description="Call dentist", is_complete=False)
```

## Services

### TaskManager

Manages the collection of tasks and provides CRUD operations.

**Responsibilities**:
- Store tasks in memory (Python list)
- Generate unique IDs for new tasks
- Provide CRUD operations (Create, Read, Update, Delete)
- Provide status change operations (mark complete/incomplete)
- Maintain task order (insertion order)

**State**:
- `tasks: List[Task]` - In-memory list of all tasks
- `next_id: int` - Counter for generating next task ID

**Operations**:

| Operation | Input | Output | Description |
|-----------|-------|--------|-------------|
| add_task | description: str | Task | Creates new task with auto-generated ID, returns created task |
| get_all_tasks | None | List[Task] | Returns all tasks in creation order |
| get_task_by_id | id: int | Task \| None | Returns task with given ID, or None if not found |
| update_task | id: int, description: str | bool | Updates task description, returns True if successful, False if not found |
| delete_task | id: int | bool | Removes task from list, returns True if successful, False if not found |
| mark_complete | id: int | bool | Sets is_complete=True, returns True if successful, False if not found |
| mark_incomplete | id: int | bool | Sets is_complete=False, returns True if successful, False if not found |

**Invariants**:
- Task IDs are unique and never reused
- Task IDs are sequential (1, 2, 3, ...)
- Tasks maintain insertion order in the list
- Deleted task IDs are not reassigned

**Error Handling**:
- Operations return None or False for not-found scenarios (no exceptions)
- ID validation performed by caller (CLI layer)
- Description validation performed by caller (CLI layer)

## Data Flow

```
User Input (CLI)
    ↓
Input Validation (CLI)
    ↓
TaskManager Operation
    ↓
Task Entity (if applicable)
    ↓
Return Result
    ↓
Format Output (CLI)
    ↓
Display to User
```

## Storage Strategy

**Phase I**: In-memory storage using Python list
- Simple, fast, no dependencies
- Data lost when application exits
- Suitable for single-user, single-session use

**Future Phases**:
- Phase II: File-based persistence (JSON or SQLite)
- Phase III: Database persistence (PostgreSQL via Neon DB)
- Phase IV+: Distributed storage with replication

## Type Definitions

**Python Type Hints**:
```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Task:
    id: int
    description: str
    is_complete: bool = False

class TaskManager:
    def __init__(self) -> None: ...
    def add_task(self, description: str) -> Task: ...
    def get_all_tasks(self) -> List[Task]: ...
    def get_task_by_id(self, task_id: int) -> Optional[Task]: ...
    def update_task(self, task_id: int, description: str) -> bool: ...
    def delete_task(self, task_id: int) -> bool: ...
    def mark_complete(self, task_id: int) -> bool: ...
    def mark_incomplete(self, task_id: int) -> bool: ...
```

## Constraints from Specification

**From FR-002**: System MUST assign unique numeric ID starting from 1 and incrementing
- ✅ Implemented via `next_id` counter in TaskManager

**From FR-003**: System MUST store tasks in memory
- ✅ Implemented via `List[Task]` in TaskManager

**From FR-004**: System MUST validate descriptions are not empty
- ✅ Validation performed in CLI layer before calling TaskManager

**From FR-005**: System MUST validate task IDs exist before operations
- ✅ Operations return None/False for not-found scenarios

**From FR-009**: System MUST maintain task order based on creation time
- ✅ Python list maintains insertion order

**From FR-012**: System MUST preserve task IDs after deletion (no reuse)
- ✅ Counter never decrements, deleted IDs never reassigned

## Design Rationale

**Why dataclass for Task?**
- Automatic `__init__`, `__repr__`, `__eq__` methods
- Type safety with IDE support
- Clean, readable code
- Immutable by default (can use frozen=True if needed)

**Why list for storage?**
- Maintains insertion order (required by FR-009)
- Simple to implement and understand
- O(1) append for add operations
- O(n) search acceptable for Phase I scale (up to 100 tasks)

**Why separate TaskManager from Task?**
- Single Responsibility Principle: Task is data, TaskManager is logic
- Easier to test each component independently
- Easier to swap storage implementation in future phases
- Clean architecture: domain entity separate from service layer

**Why return None/False instead of exceptions?**
- Not-found is expected behavior, not exceptional
- Simpler error handling in CLI layer
- More Pythonic for optional returns
- Exceptions reserved for truly unexpected errors
