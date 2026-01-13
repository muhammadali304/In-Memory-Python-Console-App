"""
Input validation and CLI handler functions.

This module handles user input validation and prompting.
"""

from domain.exceptions import InvalidTodoError, TodoNotFoundError


def validate_description(text: str) -> str:
    """
    Validates todo description text.

    Args:
        text: Raw user input

    Returns:
        Validated description text (trimmed)

    Raises:
        InvalidTodoError: If validation fails
    """
    if not text or not text.strip():
        raise InvalidTodoError("Description cannot be empty")

    if len(text) > 200:
        raise InvalidTodoError("Description cannot exceed 200 characters")

    return text.strip()


def validate_numeric_input(text: str, max_value: int) -> int:
    """
    Validates numeric input for todo selection.

    Args:
        text: Raw user input
        max_value: Maximum valid value (length of todo list)

    Returns:
        Validated integer (1-based)

    Raises:
        ValueError: If input is not numeric
        TodoNotFoundError: If number is out of range
    """
    try:
        num = int(text)
    except ValueError:
        raise ValueError("Please enter a valid number")

    if num < 1 or num > max_value:
        raise TodoNotFoundError(f"Todo #{num} not found")

    return num


def prompt_for_description(prompt_text: str = "Enter todo description: ") -> str:
    """
    Prompts user for todo description with validation.

    Args:
        prompt_text: Prompt message to display

    Returns:
        Validated description

    Raises:
        InvalidTodoError: If validation fails
    """
    while True:
        try:
            text = input(prompt_text)
            return validate_description(text)
        except InvalidTodoError as e:
            print(f"Error: {e}")


def prompt_for_todo_number(prompt_text: str, max_value: int) -> int:
    """
    Prompts user for todo number with validation.

    Args:
        prompt_text: Prompt message to display
        max_value: Maximum valid todo number

    Returns:
        Validated todo number (1-based)

    Raises:
        TodoNotFoundError: If number is out of range
    """
    while True:
        try:
            text = input(prompt_text)
            return validate_numeric_input(text, max_value)
        except ValueError as e:
            print(f"Error: {e}")
        except TodoNotFoundError:
            raise
