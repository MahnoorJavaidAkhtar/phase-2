"""Main entry point for the Todo application.

This module provides the main function that orchestrates the application flow.
"""

from src.services.task_manager import TaskManager
from src.cli.menu import (
    display_menu,
    get_menu_choice,
    add_task_flow,
    view_tasks_flow,
    mark_complete_flow,
    mark_incomplete_flow,
    update_task_flow,
    delete_task_flow
)


def main() -> None:
    """Main application entry point."""
    try:
        task_manager = TaskManager()

        print("Welcome to Todo Application!")
        print("Manage your tasks with ease.")

        while True:
            display_menu()
            choice = get_menu_choice()

            if choice == 1:
                add_task_flow(task_manager)
            elif choice == 2:
                view_tasks_flow(task_manager)
            elif choice == 3:
                update_task_flow(task_manager)
            elif choice == 4:
                delete_task_flow(task_manager)
            elif choice == 5:
                mark_complete_flow(task_manager)
            elif choice == 6:
                mark_incomplete_flow(task_manager)
            elif choice == 7:
                print("Goodbye!")
                break
            else:
                print("This feature is not yet implemented.")
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {e}")
        print("The application will now exit.")


if __name__ == "__main__":
    main()
