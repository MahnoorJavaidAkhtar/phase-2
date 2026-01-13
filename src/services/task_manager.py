"""TaskManager service for managing todo tasks.

This module provides the TaskManager class that handles CRUD operations
and status management for tasks.
"""

from typing import List, Optional
from src.domain.task import Task


class TaskManager:
    """Manages the collection of tasks and provides CRUD operations.

    Attributes:
        tasks: In-memory list of all tasks
        next_id: Counter for generating next task ID
    """

    def __init__(self) -> None:
        """Initialize TaskManager with empty task list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, description: str) -> Task:
        """Create a new task with auto-incremented ID.

        Args:
            description: Text describing what needs to be done

        Returns:
            The newly created Task object
        """
        task = Task(id=self.next_id, description=description, is_complete=False)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in creation order.

        Returns:
            Copy of the tasks list to prevent external modification
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find and return a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was found and marked complete, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.is_complete = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was found and marked incomplete, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.is_complete = False
            return True
        return False

    def update_task(self, task_id: int, description: str) -> bool:
        """Update a task's description.

        Args:
            task_id: The ID of the task to update
            description: New description for the task

        Returns:
            True if task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.description = description
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task from the list.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was found and deleted, False otherwise

        Note:
            Task IDs are never reused after deletion (per FR-012)
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
