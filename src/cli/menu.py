"""
Menu display and selection handling.

This module manages the main menu interface.
"""


def show_menu() -> None:
    """Displays the main menu options."""
    print("=" * 40)
    print("    Todo Application (Phase I)")
    print("=" * 40)
    print("\nMain Menu:")
    print("1. Add a todo")
    print("2. View all todos")
    print("3. Update a todo")
    print("4. Delete a todo")
    print("5. Mark todo as complete")
    print("6. Exit")
    print()


def get_menu_choice() -> int:
    """
    Prompts user for menu choice with validation.

    Returns:
        Valid menu choice (1-6)
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Error: Please enter a number between 1 and 6")
        except ValueError:
            print("Error: Please enter a valid number")
