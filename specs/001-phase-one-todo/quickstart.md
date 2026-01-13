# Quickstart Guide: Phase I Todo Application

**Feature**: Phase I - Basic Todo Console Application
**Created**: 2026-01-13
**Target Users**: Developers and end users

## Prerequisites

- Python 3.11 or higher
- No external dependencies required (uses Python standard library only)

## Installation

### 1. Verify Python Version

```bash
python --version
# Should show Python 3.11.x or higher
```

If you don't have Python 3.11+, download it from [python.org](https://www.python.org/downloads/).

### 2. Clone Repository

```bash
git clone <repository-url>
cd mahnoor-kiro
```

### 3. Checkout Feature Branch

```bash
git checkout 001-phase-one-todo
```

## Running the Application

### Start the Application

```bash
python src/main.py
```

You should see the main menu:

```
=== Todo Application ===

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

Enter your choice (1-7):
```

## Usage Guide

### Adding a Task

1. Select option `1` from the main menu
2. Enter a task description when prompted
3. The task will be created with a unique ID and marked as incomplete

**Example**:
```
Enter your choice (1-7): 1
Enter task description: Buy groceries
✓ Task added successfully! (ID: 1)
```

**Validation**:
- Description cannot be empty
- Description cannot be whitespace only
- If validation fails, you'll see an error and can try again

### Viewing All Tasks

1. Select option `2` from the main menu
2. All tasks will be displayed with their ID, description, and status

**Example**:
```
Enter your choice (1-7): 2

=== Your Tasks ===
1. [ ] Buy groceries
2. [✓] Write report
3. [ ] Call dentist

Total: 3 tasks (1 complete, 2 incomplete)
```

**Legend**:
- `[ ]` = Incomplete task
- `[✓]` = Complete task

**Empty List**:
```
Enter your choice (1-7): 2
No tasks found. Add a task to get started!
```

### Updating a Task

1. Select option `3` from the main menu
2. Enter the task ID you want to update
3. Enter the new description

**Example**:
```
Enter your choice (1-7): 3
Enter task ID: 1
Enter new description: Buy groceries and milk
✓ Task updated successfully!
```

**Validation**:
- Task ID must exist
- New description cannot be empty
- If validation fails, you'll see an error

### Deleting a Task

1. Select option `4` from the main menu
2. Enter the task ID you want to delete
3. The task will be permanently removed

**Example**:
```
Enter your choice (1-7): 4
Enter task ID: 2
✓ Task deleted successfully!
```

**Note**: Deleted task IDs are not reused. If you delete task 2, the next task created will still get the next sequential ID (e.g., 4 if 3 already exists).

### Marking a Task Complete

1. Select option `5` from the main menu
2. Enter the task ID you want to mark as complete
3. The task status will change to complete

**Example**:
```
Enter your choice (1-7): 5
Enter task ID: 1
✓ Task marked as complete!
```

### Marking a Task Incomplete

1. Select option `6` from the main menu
2. Enter the task ID you want to mark as incomplete
3. The task status will change to incomplete

**Example**:
```
Enter your choice (1-7): 6
Enter task ID: 1
✓ Task marked as incomplete!
```

**Note**: You can toggle task status as many times as needed.

### Exiting the Application

1. Select option `7` from the main menu
2. The application will exit

**Example**:
```
Enter your choice (1-7): 7
Goodbye!
```

**Warning**: All tasks will be lost when you exit. Phase I does not persist data.

## Common Workflows

### Workflow 1: Basic Task Management

```
1. Start application
2. Add task: "Buy groceries" (ID: 1)
3. Add task: "Write report" (ID: 2)
4. View tasks (see both tasks)
5. Mark task 2 complete
6. View tasks (see task 2 marked complete)
7. Exit
```

### Workflow 2: Task Correction

```
1. Start application
2. Add task: "Buy milk" (ID: 1)
3. Update task 1: "Buy milk and bread"
4. View tasks (see updated description)
5. Exit
```

### Workflow 3: Task Cleanup

```
1. Start application
2. Add task: "Task A" (ID: 1)
3. Add task: "Task B" (ID: 2)
4. Add task: "Task C" (ID: 3)
5. Delete task 2
6. View tasks (see tasks 1 and 3 only)
7. Exit
```

## Error Handling

### Invalid Menu Choice

```
Enter your choice (1-7): 9
✗ Invalid choice. Please enter a number between 1 and 7.
```

### Invalid Task ID

```
Enter task ID: 999
✗ Task not found. Please check the ID and try again.
```

### Empty Description

```
Enter task description:
✗ Description cannot be empty. Please enter a valid description.
```

### Non-Numeric Input

```
Enter task ID: abc
✗ Invalid input. Please enter a number.
```

## Troubleshooting

### Problem: "python: command not found"

**Solution**: Python is not installed or not in your PATH. Install Python 3.11+ from python.org.

### Problem: "No module named 'src'"

**Solution**: Make sure you're running the command from the repository root directory (mahnoor-kiro/).

### Problem: Application crashes on startup

**Solution**:
1. Verify Python version: `python --version` (must be 3.11+)
2. Check that all source files exist in `src/` directory
3. Review error message for specific issue

### Problem: Tasks disappear after closing

**Expected Behavior**: Phase I does not persist data. All tasks are stored in memory only and are lost when the application exits. This is by design for Phase I.

## Limitations (Phase I)

- **No Persistence**: Tasks are lost when application exits
- **Single User**: No user accounts or authentication
- **No Search**: Cannot search or filter tasks
- **No Categories**: Cannot organize tasks into categories
- **No Due Dates**: Cannot set deadlines for tasks
- **No Priorities**: All tasks have equal priority
- **No Undo**: Cannot undo operations

These limitations will be addressed in future phases (Phase II through Phase V).

## Next Steps

After using Phase I, you can:
- Provide feedback on the user experience
- Request features for Phase II (web interface, persistence)
- Report bugs or issues
- Review the specification at `specs/001-phase-one-todo/spec.md`

## Development

### Running Tests (Optional)

If tests are added in the future:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/unit/test_task_manager.py

# Run with coverage
pytest --cov=src tests/
```

### Code Structure

```
src/
├── domain/
│   └── task.py          # Task entity
├── services/
│   └── task_manager.py  # Business logic
├── cli/
│   └── menu.py          # User interface
└── main.py              # Application entry point
```

### Modifying the Code

1. **Add new menu option**: Edit `src/cli/menu.py`
2. **Add new task operation**: Edit `src/services/task_manager.py`
3. **Change task attributes**: Edit `src/domain/task.py`

## Support

For issues or questions:
- Review the specification: `specs/001-phase-one-todo/spec.md`
- Review the implementation plan: `specs/001-phase-one-todo/plan.md`
- Check the data model: `specs/001-phase-one-todo/data-model.md`

## Version Information

- **Phase**: I (Basic Console Application)
- **Version**: 1.0.0
- **Branch**: 001-phase-one-todo
- **Python**: 3.11+
- **Dependencies**: None (standard library only)
