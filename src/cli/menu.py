"""CLI menu interface for the Todo application.

This module provides the command-line interface for user interaction.
"""

from typing import Optional
from src.services.task_manager import TaskManager


def get_task_id_input(prompt: str) -> Optional[int]:
    """Get and validate numeric task ID input from user.

    Args:
        prompt: The prompt message to display to the user

    Returns:
        The task ID as an integer, or None if input is invalid
    """
    try:
        task_id_input = input(prompt)
        return int(task_id_input)
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def display_menu() -> None:
    """Display the main menu with all available options."""
    print("\n=== Todo Application ===\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Mark Incomplete")
    print("7. Exit")
    print()


def get_menu_choice() -> int:
    """Get and validate user's menu choice.

    Returns:
        Valid menu choice (1-7)
    """
    while True:
        try:
            choice = input("Enter your choice (1-7): ")
            choice_num = int(choice)
            if 1 <= choice_num <= 7:
                return choice_num
            else:
                print("Error: Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")


def add_task_flow(task_manager: TaskManager) -> None:
    """Handle the add task workflow.

    Args:
        task_manager: TaskManager instance to add task to
    """
    while True:
        description = input("Enter task description: ")
        # Validate non-empty and not whitespace-only
        if description.strip():
            task = task_manager.add_task(description)
            print(f"Success: Task added successfully! (ID: {task.id})")
            break
        else:
            print("Error: Description cannot be empty. Please enter a valid description.")


def view_tasks_flow(task_manager: TaskManager) -> None:
    """Handle the view tasks workflow.

    Args:
        task_manager: TaskManager instance to get tasks from
    """
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("No tasks found. Add a task to get started!")
        return

    print("\n=== Your Tasks ===")
    for task in tasks:
        status_marker = "[X]" if task.is_complete else "[ ]"
        print(f"{task.id}. {status_marker} {task.description}")

    # Count complete and incomplete tasks
    complete_count = sum(1 for task in tasks if task.is_complete)
    incomplete_count = len(tasks) - complete_count
    print(f"\nTotal: {len(tasks)} tasks ({complete_count} complete, {incomplete_count} incomplete)")


def mark_complete_flow(task_manager: TaskManager) -> None:
    """Handle the mark task complete workflow.

    Args:
        task_manager: TaskManager instance to mark task in
    """
    tasks = task_manager.get_all_tasks()
    if not tasks:
        print("Error: No tasks available. Add a task first.")
        return

    while True:
        try:
            task_id_input = input("Enter task ID to mark complete: ")
            task_id = int(task_id_input)
            if task_manager.mark_complete(task_id):
                print("Success: Task marked as complete!")
                break
            else:
                print("Error: Task not found. Please check the ID and try again.")
                break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            break


def mark_incomplete_flow(task_manager: TaskManager) -> None:
    """Handle the mark task incomplete workflow.

    Args:
        task_manager: TaskManager instance to mark task in
    """
    tasks = task_manager.get_all_tasks()
    if not tasks:
        print("Error: No tasks available. Add a task first.")
        return

    while True:
        try:
            task_id_input = input("Enter task ID to mark incomplete: ")
            task_id = int(task_id_input)
            if task_manager.mark_incomplete(task_id):
                print("Success: Task marked as incomplete!")
                break
            else:
                print("Error: Task not found. Please check the ID and try again.")
                break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            break


def update_task_flow(task_manager: TaskManager) -> None:
    """Handle the update task workflow.

    Args:
        task_manager: TaskManager instance to update task in
    """
    tasks = task_manager.get_all_tasks()
    if not tasks:
        print("Error: No tasks available. Add a task first.")
        return

    while True:
        try:
            task_id_input = input("Enter task ID to update: ")
            task_id = int(task_id_input)

            # Check if task exists before prompting for new description
            if not task_manager.get_task_by_id(task_id):
                print("Error: Task not found. Please check the ID and try again.")
                break

            # Prompt for new description
            while True:
                new_description = input("Enter new description: ")
                if new_description.strip():
                    if task_manager.update_task(task_id, new_description):
                        print("Success: Task updated successfully!")
                    else:
                        print("Error: Task not found. Please check the ID and try again.")
                    return
                else:
                    print("Error: Description cannot be empty. Please enter a valid description.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            break


def delete_task_flow(task_manager: TaskManager) -> None:
    """Handle the delete task workflow.

    Args:
        task_manager: TaskManager instance to delete task from
    """
    tasks = task_manager.get_all_tasks()
    if not tasks:
        print("Error: No tasks available. Add a task first.")
        return

    while True:
        try:
            task_id_input = input("Enter task ID to delete: ")
            task_id = int(task_id_input)
            if task_manager.delete_task(task_id):
                print("Success: Task deleted successfully!")
                break
            else:
                print("Error: Task not found. Please check the ID and try again.")
                break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            break





