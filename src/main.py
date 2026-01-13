"""
Main entry point for the Phase I Todo Application.

This module implements the menu-driven CLI interface.
"""

from domain.todo_service import TodoService
from domain.exceptions import TodoNotFoundError, InvalidTodoError
from cli.menu import show_menu, get_menu_choice
from cli.input_handler import prompt_for_description, prompt_for_todo_number
from cli.output import display_todos, display_message, display_error


def main():
    """Main application loop."""
    service = TodoService()

    print("\nWelcome to Todo Application (Phase I)!")
    print("All data is stored in memory and will be lost when you exit.\n")

    while True:
        show_menu()
        choice = get_menu_choice()

        try:
            if choice == 1:
                # Add a todo
                description = prompt_for_description()
                service.add_todo(description)
                display_message("Todo added successfully!")
                display_todos(service.get_all_todos())

            elif choice == 2:
                # View all todos
                display_todos(service.get_all_todos())

            elif choice == 3:
                # Update a todo
                todos = service.get_all_todos()
                if not todos:
                    display_error("No todos to update")
                    continue

                display_todos(todos)
                todo_num = prompt_for_todo_number("Enter todo number to update: ", len(todos))
                new_description = prompt_for_description("Enter new description: ")
                service.update_todo(todo_num, new_description)
                display_message("Todo updated successfully!")
                display_todos(service.get_all_todos())

            elif choice == 4:
                # Delete a todo
                todos = service.get_all_todos()
                if not todos:
                    display_error("No todos to delete")
                    continue

                display_todos(todos)
                todo_num = prompt_for_todo_number("Enter todo number to delete: ", len(todos))
                service.delete_todo(todo_num)
                display_message("Todo deleted successfully!")
                display_todos(service.get_all_todos())

            elif choice == 5:
                # Mark todo as complete
                todos = service.get_all_todos()
                if not todos:
                    display_error("No todos to mark complete")
                    continue

                display_todos(todos)
                todo_num = prompt_for_todo_number("Enter todo number to mark complete: ", len(todos))
                service.mark_complete(todo_num)
                display_message("Todo marked as complete!")
                display_todos(service.get_all_todos())

            elif choice == 6:
                # Exit
                print("\nThank you for using Todo Application!")
                print("Goodbye!\n")
                break

        except TodoNotFoundError as e:
            display_error(str(e))
        except InvalidTodoError as e:
            display_error(str(e))
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting...")
            break
        except Exception as e:
            display_error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
