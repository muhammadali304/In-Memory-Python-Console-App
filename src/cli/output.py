"""
Output formatting utilities for displaying todos and messages.

This module handles all console output formatting.
"""

from typing import List, Tuple
from domain.todo import Todo


def display_todos(todos: List[Tuple[int, Todo]]) -> None:
    """
    Displays all todos in formatted list.

    Args:
        todos: List of (display_number, todo) tuples
    """
    print("\nYour Todos:")

    if not todos:
        print("No todos found.")
    else:
        for num, todo in todos:
            status = "[DONE]" if todo.is_complete else "[TODO]"
            print(f"{num}. {status} {todo.description}")

    print()


def display_message(message: str) -> None:
    """
    Displays a success or informational message.

    Args:
        message: Message to display
    """
    print(f"\n{message}\n")


def display_error(message: str) -> None:
    """
    Displays an error message.

    Args:
        message: Error message to display
    """
    print(f"\nError: {message}\n")
