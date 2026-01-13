"""
TodoService - manages todo operations and in-memory state.

This module implements the business logic for todo operations.
"""

from typing import List, Tuple
from domain.todo import Todo
from domain.exceptions import InvalidTodoError, TodoNotFoundError
from utils.logger import setup_logger


class TodoService:
    """
    Manages todo operations and in-memory state.

    State is maintained in a Python list with sequential indexing.
    Todos are displayed with 1-based numbering to users.
    """

    def __init__(self):
        """Initialize the service with an empty todo list."""
        self._todos: List[Todo] = []
        self._logger = setup_logger(__name__)

    def add_todo(self, description: str) -> None:
        """
        Adds a new todo to the list.

        Args:
            description: Todo text (must be validated before calling)

        Raises:
            InvalidTodoError: If description is invalid
        """
        # Validate description
        if not description or not description.strip():
            raise InvalidTodoError("Description cannot be empty")

        if len(description) > 200:
            raise InvalidTodoError("Description cannot exceed 200 characters")

        # Create and add todo
        todo = Todo(description=description.strip(), is_complete=False)
        self._todos.append(todo)
        self._logger.info(f"Todo added: {description.strip()}")

    def get_all_todos(self) -> List[Tuple[int, Todo]]:
        """
        Returns all todos with their display numbers.

        Returns:
            List of (display_number, todo) tuples where display_number is 1-based
        """
        return [(i + 1, todo) for i, todo in enumerate(self._todos)]

    def mark_complete(self, index: int) -> None:
        """
        Marks a todo as complete.

        Args:
            index: Todo number (1-based, as displayed to user)

        Raises:
            TodoNotFoundError: If index is out of range
        """
        # Validate index
        if index < 1 or index > len(self._todos):
            raise TodoNotFoundError(f"Todo #{index} not found")

        # Mark complete (idempotent)
        list_index = index - 1
        self._todos[list_index].is_complete = True
        self._logger.info(f"Todo {index} marked complete")

    def delete_todo(self, index: int) -> None:
        """
        Deletes a todo from the list.

        Args:
            index: Todo number (1-based, as displayed to user)

        Raises:
            TodoNotFoundError: If index is out of range
        """
        # Validate index
        if index < 1 or index > len(self._todos):
            raise TodoNotFoundError(f"Todo #{index} not found")

        # Delete todo
        list_index = index - 1
        description = self._todos[list_index].description
        del self._todos[list_index]
        self._logger.info(f"Todo {index} deleted: {description}")

    def update_todo(self, index: int, new_description: str) -> None:
        """
        Updates the description of an existing todo.

        Args:
            index: Todo number (1-based, as displayed to user)
            new_description: New todo text (must be validated)

        Raises:
            TodoNotFoundError: If index is out of range
            InvalidTodoError: If new_description is invalid
        """
        # Validate index
        if index < 1 or index > len(self._todos):
            raise TodoNotFoundError(f"Todo #{index} not found")

        # Validate new description
        if not new_description or not new_description.strip():
            raise InvalidTodoError("Description cannot be empty")

        if len(new_description) > 200:
            raise InvalidTodoError("Description cannot exceed 200 characters")

        # Update todo
        list_index = index - 1
        old_description = self._todos[list_index].description
        self._todos[list_index].description = new_description.strip()
        self._logger.info(f"Todo {index} updated: {old_description} -> {new_description.strip()}")
