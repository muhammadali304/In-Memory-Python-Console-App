# Data Model: Phase I In-Memory Console Todo Application

**Date**: 2026-01-09
**Feature**: 001-phase1-todo
**Purpose**: Define entities, validation rules, and service layer interfaces

## Entity: Todo

### Definition

```python
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
```

### Field Specifications

| Field | Type | Required | Default | Validation Rules |
|-------|------|----------|---------|------------------|
| `description` | `str` | Yes | N/A | - Length: 1-200 characters<br>- Not empty<br>- Not whitespace-only<br>- Single-line text |
| `is_complete` | `bool` | No | `False` | - Must be boolean<br>- `False` = incomplete ([TODO])<br>- `True` = complete ([DONE]) |

### Validation Rules

**Description Validation**:
```python
def validate_description(text: str) -> str:
    """
    Validates todo description text.

    Args:
        text: Raw user input

    Returns:
        Validated description text

    Raises:
        InvalidTodoError: If validation fails
    """
    if not text or not text.strip():
        raise InvalidTodoError("Description cannot be empty")

    if len(text) > 200:
        raise InvalidTodoError("Description cannot exceed 200 characters")

    return text.strip()
```

**Index Validation**:
```python
def validate_index(index: int, max_index: int) -> int:
    """
    Validates todo index (1-based user input).

    Args:
        index: User-provided index (1-based)
        max_index: Maximum valid index (length of todo list)

    Returns:
        Validated index (0-based for list access)

    Raises:
        TodoNotFoundError: If index is out of range
    """
    if index < 1 or index > max_index:
        raise TodoNotFoundError(f"Todo #{index} not found")

    return index - 1  # Convert to 0-based
```

---

## Service Layer: TodoService

### State Management

```python
class TodoService:
    """
    Manages todo operations and in-memory state.

    State is maintained in a Python list with sequential indexing.
    Todos are displayed with 1-based numbering to users.
    """

    def __init__(self):
        self._todos: list[Todo] = []
```

### Service Methods

#### 1. Add Todo

```python
def add_todo(self, description: str) -> None:
    """
    Adds a new todo to the list.

    Args:
        description: Todo text (must be validated before calling)

    Raises:
        InvalidTodoError: If description is invalid

    Side Effects:
        - Appends todo to internal list
        - Logs operation at INFO level
    """
```

**Behavior**:
- Validates description (1-200 chars, non-empty, no whitespace-only)
- Creates new Todo with `is_complete=False`
- Appends to internal list
- Logs: `"Todo added: {description}"`

---

#### 2. Get All Todos

```python
def get_all_todos(self) -> list[tuple[int, Todo]]:
    """
    Returns all todos with their display numbers.

    Returns:
        List of (display_number, todo) tuples where display_number is 1-based

    Example:
        [(1, Todo("Buy milk", False)), (2, Todo("Call dentist", True))]
    """
```

**Behavior**:
- Returns list of tuples: `(1-based index, Todo object)`
- Empty list returns `[]`
- No logging (read-only operation)

---

#### 3. Update Todo

```python
def update_todo(self, index: int, new_description: str) -> None:
    """
    Updates the description of an existing todo.

    Args:
        index: Todo number (1-based, as displayed to user)
        new_description: New todo text (must be validated)

    Raises:
        TodoNotFoundError: If index is out of range
        InvalidTodoError: If new_description is invalid

    Side Effects:
        - Modifies todo description in place
        - Preserves is_complete status
        - Logs operation at INFO level
    """
```

**Behavior**:
- Validates index (1-based, within range)
- Validates new description
- Updates description, preserves completion status
- Logs: `"Todo {index} updated: {old} -> {new}"`

---

#### 4. Delete Todo

```python
def delete_todo(self, index: int) -> None:
    """
    Deletes a todo from the list.

    Args:
        index: Todo number (1-based, as displayed to user)

    Raises:
        TodoNotFoundError: If index is out of range

    Side Effects:
        - Removes todo from internal list
        - Remaining todos are automatically renumbered (list behavior)
        - Logs operation at INFO level
    """
```

**Behavior**:
- Validates index (1-based, within range)
- Removes todo from list at position `index - 1`
- Automatic renumbering (list indices shift)
- Logs: `"Todo {index} deleted: {description}"`

---

#### 5. Mark Todo Complete

```python
def mark_complete(self, index: int) -> None:
    """
    Marks a todo as complete.

    Args:
        index: Todo number (1-based, as displayed to user)

    Raises:
        TodoNotFoundError: If index is out of range

    Side Effects:
        - Sets is_complete to True
        - Idempotent (marking complete todo as complete has no effect)
        - Logs operation at INFO level
    """
```

**Behavior**:
- Validates index (1-based, within range)
- Sets `is_complete = True`
- Idempotent operation (no error if already complete)
- Logs: `"Todo {index} marked complete"`

---

## Exception Hierarchy

```python
class TodoError(Exception):
    """Base exception for all todo-related errors."""
    pass

class InvalidTodoError(TodoError):
    """Raised when todo validation fails (empty, too long, whitespace-only)."""
    pass

class TodoNotFoundError(TodoError):
    """Raised when todo index is out of range."""
    pass
```

---

## Storage Strategy

### In-Memory List

**Structure**: `list[Todo]`

**Indexing**:
- Internal: 0-based (Python list standard)
- User-facing: 1-based (natural numbering: 1, 2, 3...)
- Conversion: `list_index = user_index - 1`

**Renumbering After Deletion**:
- Automatic (list behavior)
- No manual renumbering required
- Example:
  ```
  Before delete #2: [Todo1, Todo2, Todo3]
  After delete #2:  [Todo1, Todo3]
  Display:          1. Todo1, 2. Todo3
  ```

**Capacity**:
- No explicit limit enforced
- Expected scale: up to 1000 todos per session
- Memory usage: ~200 bytes per todo (negligible for expected scale)

---

## Display Format

### Todo List Display

```
Your Todos:
1. [TODO] Buy groceries
2. [DONE] Call dentist
3. [TODO] Finish report
```

**Format Specification**:
- Line format: `{number}. [{status}] {description}`
- Number: 1-based sequential
- Status: `[TODO]` for incomplete, `[DONE]` for complete
- Description: As entered by user (trimmed)

**Empty List Display**:
```
Your Todos:
No todos found.
```

---

## Phase II Migration Notes

### What Changes in Phase II

**Storage Layer**:
- Replace `list[Todo]` with database (SQLModel + Neon DB)
- Add `id` field (UUID or auto-increment)
- Add `created_at`, `updated_at` timestamps

**Service Layer**:
- Same method signatures (add, get_all, update, delete, mark_complete)
- Internal implementation uses database queries instead of list operations
- Validation logic remains unchanged

**Domain Logic**:
- Todo entity gains additional fields
- Core business rules remain unchanged
- Validation rules remain unchanged

### What Stays the Same

- Todo entity concept (description, completion status)
- Service method signatures
- Validation rules (1-200 chars, non-empty, no whitespace-only)
- Exception types
- Display format ([TODO]/[DONE] prefixes)
- 1-based user-facing numbering

**Migration Strategy**: Domain logic (TodoService) is framework-agnostic and can be reused with minimal changes. Only storage implementation changes.
