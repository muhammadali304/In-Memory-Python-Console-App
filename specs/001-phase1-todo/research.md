# Research: Phase I In-Memory Console Todo Application

**Date**: 2026-01-09
**Feature**: 001-phase1-todo
**Purpose**: Resolve technical decisions and establish implementation patterns for Phase I

## Research Questions & Findings

### 1. Data Structure for In-Memory Todo Storage

**Decision**: Python list with sequential indexing

**Rationale**:
- Maintains insertion order naturally (Python 3.7+ guarantee)
- Simple sequential indexing matches user mental model (numbered list: 1, 2, 3...)
- Easy to renumber after deletions (list comprehension or enumerate)
- Minimal memory overhead for expected scale (up to 1000 todos)
- Direct support for iteration and display operations

**Alternatives Considered**:
- **Dict with numeric keys**: Adds unnecessary complexity, requires manual key management, no benefit over list
- **Dict with UUID keys**: Overkill for in-memory application, complicates user interaction (users expect numbers, not UUIDs)
- **OrderedDict**: Redundant since Python 3.7+ dicts maintain insertion order, and list is simpler

**Implementation Details**:
- Store todos in a Python list: `todos: list[Todo] = []`
- Display with 1-based indexing to users: `enumerate(todos, start=1)`
- Convert user input (1-based) to list index (0-based): `index = user_input - 1`
- Renumbering after deletion is automatic (list indices shift)

---

### 2. Menu-Driven CLI Patterns in Python

**Decision**: While loop with menu display, input validation, and operation dispatch

**Rationale**:
- Standard pattern for console applications, widely understood
- Matches clarified specification (menu-driven loop)
- Provides clear user guidance (self-explanatory interface per SC-009)
- Easy to test and maintain
- Supports error recovery with re-prompting

**Alternatives Considered**:
- **Command parser (argparse/click)**: Rejected during specification clarification, requires users to remember command syntax
- **REPL-style interface**: Too complex for simple todo app, unnecessary abstraction
- **Single-operation mode**: Rejected during specification clarification, poor user experience for multiple operations

**Implementation Pattern**:
```python
while True:
    display_menu()
    choice = get_menu_choice()  # Validates numeric input

    if choice == 1:
        add_todo()
    elif choice == 2:
        view_todos()
    # ... other operations
    elif choice == 6:
        break  # Exit
    else:
        display_error("Invalid choice")
```

**Error Recovery**:
- Invalid menu choice: Display error, re-display menu (stay in loop)
- Invalid operation input: Display error, re-prompt within operation (per clarification)
- Non-numeric input: Catch ValueError, display error, re-prompt

---

### 3. Input Validation Patterns

**Decision**: Validation at CLI boundary, domain layer assumes valid input

**Rationale**:
- Separation of concerns: CLI handles user interaction, domain handles business logic
- Domain logic remains clean and testable without UI concerns
- Validation rules centralized in input_handler module
- Easier to replace CLI layer in Phase II (web API will have its own validation)

**Alternatives Considered**:
- **Validation in domain layer**: Couples domain logic to UI concerns, makes domain less reusable
- **Validation in both layers**: Redundant, violates DRY principle
- **No validation**: Violates security by default principle, allows invalid state

**Validation Rules**:
1. **Todo description**:
   - Not empty: `if not text.strip()`
   - Not whitespace-only: `if text.strip() == ""`
   - Length 1-200 characters: `if not (1 <= len(text) <= 200)`

2. **Todo number (for update/delete/complete)**:
   - Numeric input: `try: int(input) except ValueError`
   - Positive integer: `if num < 1`
   - Within range: `if num > len(todos)`

3. **Menu choice**:
   - Numeric input: `try: int(input) except ValueError`
   - Valid range (1-6): `if not (1 <= choice <= 6)`

**Implementation Location**:
- `cli/input_handler.py`: Contains validation functions
- Returns validated data or raises custom exception
- CLI layer catches exceptions and re-prompts

---

### 4. Logging Approach for Phase I

**Decision**: Python standard library `logging` module with basic configuration

**Rationale**:
- Standard library (no external dependencies)
- Structured logging with levels (INFO, WARNING, ERROR)
- Can be enhanced in Phase II without code changes
- Supports multiple handlers (console, file) for future phases
- Minimal performance overhead

**Alternatives Considered**:
- **Print statements**: Not structured, hard to filter, not scalable to Phase II
- **Third-party library (loguru, structlog)**: Violates "no external dependencies" constraint
- **No logging**: Violates observability-ready design principle

**Configuration**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
```

**What to Log**:
- **INFO**: Successful operations (add, update, delete, complete)
- **WARNING**: Invalid input attempts (for debugging)
- **ERROR**: Unexpected errors (should not occur in normal operation)

**Log Messages**:
- `logger.info(f"Todo added: {description}")`
- `logger.info(f"Todo {index} marked complete")`
- `logger.info(f"Todo {index} deleted")`
- `logger.info(f"Todo {index} updated")`

**Phase II Considerations**:
- Same logging calls will work with web API
- Can add file handler for persistent logs
- Can add structured logging (JSON) for log aggregation
- Domain logic logging is framework-agnostic

---

## Additional Technical Decisions

### 5. Todo Entity Design

**Decision**: Python dataclass with two fields

**Rationale**:
- Dataclass provides automatic `__init__`, `__repr__`, `__eq__`
- Immutable by default (frozen=True) prevents accidental modification
- Type hints improve code clarity and IDE support
- Minimal boilerplate

**Implementation**:
```python
from dataclasses import dataclass

@dataclass
class Todo:
    description: str
    is_complete: bool = False
```

**Alternatives Considered**:
- **Regular class**: More boilerplate, no benefit
- **NamedTuple**: Immutable but less flexible for Phase II extensions
- **Dict**: No type safety, error-prone

---

### 6. Error Handling Strategy

**Decision**: Custom exception types for domain errors, try-except at CLI boundary

**Rationale**:
- Domain layer raises semantic exceptions (InvalidTodoError, TodoNotFoundError)
- CLI layer catches and displays user-friendly messages
- Separation between domain errors and UI presentation

**Exception Hierarchy**:
```python
class TodoError(Exception):
    """Base exception for todo operations"""
    pass

class InvalidTodoError(TodoError):
    """Raised when todo validation fails"""
    pass

class TodoNotFoundError(TodoError):
    """Raised when todo index is out of range"""
    pass
```

**CLI Error Handling**:
```python
try:
    todo_service.update_todo(index, new_description)
except TodoNotFoundError:
    display_error(f"Todo #{index} not found")
except InvalidTodoError as e:
    display_error(str(e))
```

---

## Summary

All research questions resolved with decisions that:
1. ✅ Meet Phase I requirements (in-memory, console-only, no external dependencies)
2. ✅ Follow constitution principles (separation of concerns, observability, security)
3. ✅ Enable Phase II migration (domain logic is framework-agnostic)
4. ✅ Support testing and validation (deterministic, testable patterns)

**Ready for Phase 1**: Design artifacts (data-model.md, quickstart.md)
