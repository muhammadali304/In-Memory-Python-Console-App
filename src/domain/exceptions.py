"""
Exception hierarchy for todo operations.

This module defines custom exceptions for domain-level errors.
"""


class TodoError(Exception):
    """Base exception for all todo-related errors."""
    pass


class InvalidTodoError(TodoError):
    """Raised when todo validation fails (empty, too long, whitespace-only)."""
    pass


class TodoNotFoundError(TodoError):
    """Raised when todo index is out of range."""
    pass
