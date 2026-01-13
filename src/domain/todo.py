"""
Todo entity - represents a single todo item.

This module defines the core Todo dataclass.
"""

from dataclasses import dataclass


@dataclass
class Todo:
    """
    Represents a single todo item.

    Attributes:
        description: The todo text (1-200 characters, non-empty, no whitespace-only)
        is_complete: Completion status (defaults to False for new todos)
    """
    description: str
    is_complete: bool = False
