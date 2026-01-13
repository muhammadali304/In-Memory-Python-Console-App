# Quickstart Guide: Phase I In-Memory Console Todo Application

**Date**: 2026-01-09
**Feature**: 001-phase1-todo
**Purpose**: Setup, run, and validate the Phase I todo application

## Prerequisites

- Python 3.13 or higher
- UV package manager
- Terminal/console with UTF-8 support
- Git (for cloning repository)

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd Hackathon-II_Phase-I
```

### 2. Checkout Feature Branch

```bash
git checkout 001-phase1-todo
```

### 3. Initialize UV Environment

```bash
# Install UV if not already installed
# See: https://github.com/astral-sh/uv

# Initialize Python environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 4. Verify Python Version

```bash
python --version
# Should show Python 3.13.x or higher
```

## Running the Application

### Start the Application

```bash
uv run python src/main.py
```

### Expected Output

```
=================================
    Todo Application (Phase I)
=================================

Main Menu:
1. Add a todo
2. View all todos
3. Update a todo
4. Delete a todo
5. Mark todo as complete
6. Exit

Enter your choice (1-6):
```

## Using the Application

### 1. Add a Todo

**Steps**:
1. Select option `1` from the main menu
2. Enter todo description (1-200 characters)
3. Press Enter

**Example**:
```
Enter your choice (1-6): 1
Enter todo description: Buy groceries

✓ Todo added successfully!

Your Todos:
1. [TODO] Buy groceries

Main Menu:
...
```

**Validation**:
- Empty input: "Description cannot be empty"
- Whitespace only: "Description cannot be empty"
- Over 200 characters: "Description cannot exceed 200 characters"

---

### 2. View All Todos

**Steps**:
1. Select option `2` from the main menu

**Example (with todos)**:
```
Enter your choice (1-6): 2

Your Todos:
1. [TODO] Buy groceries
2. [DONE] Call dentist
3. [TODO] Finish report

Main Menu:
...
```

**Example (empty list)**:
```
Enter your choice (1-6): 2

Your Todos:
No todos found.

Main Menu:
...
```

---

### 3. Update a Todo

**Steps**:
1. Select option `3` from the main menu
2. Enter todo number (1-based)
3. Enter new description (1-200 characters)
4. Press Enter

**Example**:
```
Enter your choice (1-6): 3

Your Todos:
1. [TODO] Buy groceries
2. [TODO] Call dentist

Enter todo number to update: 1
Enter new description: Buy groceries and milk

✓ Todo updated successfully!

Your Todos:
1. [TODO] Buy groceries and milk
2. [TODO] Call dentist

Main Menu:
...
```

**Validation**:
- Invalid number: "Todo #X not found"
- Non-numeric input: "Please enter a valid number"
- Empty description: "Description cannot be empty"

---

### 4. Delete a Todo

**Steps**:
1. Select option `4` from the main menu
2. Enter todo number (1-based)
3. Press Enter

**Example**:
```
Enter your choice (1-6): 4

Your Todos:
1. [TODO] Buy groceries
2. [TODO] Call dentist
3. [TODO] Finish report

Enter todo number to delete: 2

✓ Todo deleted successfully!

Your Todos:
1. [TODO] Buy groceries
2. [TODO] Finish report

Main Menu:
...
```

**Note**: Remaining todos are automatically renumbered.

**Validation**:
- Invalid number: "Todo #X not found"
- Non-numeric input: "Please enter a valid number"

---

### 5. Mark Todo as Complete

**Steps**:
1. Select option `5` from the main menu
2. Enter todo number (1-based)
3. Press Enter

**Example**:
```
Enter your choice (1-6): 5

Your Todos:
1. [TODO] Buy groceries
2. [TODO] Call dentist

Enter todo number to mark complete: 1

✓ Todo marked as complete!

Your Todos:
1. [DONE] Buy groceries
2. [TODO] Call dentist

Main Menu:
...
```

**Note**: Marking an already complete todo as complete has no effect (idempotent).

**Validation**:
- Invalid number: "Todo #X not found"
- Non-numeric input: "Please enter a valid number"

---

### 6. Exit

**Steps**:
1. Select option `6` from the main menu

**Example**:
```
Enter your choice (1-6): 6

Thank you for using Todo Application!
Goodbye!
```

**Note**: All todos are lost when the application exits (in-memory only).

---

## Validation Scenarios

### Test Case 1: Empty Todo List Operations

```
1. Start application (empty list)
2. Select "View all todos" → Should show "No todos found"
3. Select "Update a todo" → Enter any number → Should show "Todo #X not found"
4. Select "Delete a todo" → Enter any number → Should show "Todo #X not found"
5. Select "Mark complete" → Enter any number → Should show "Todo #X not found"
```

### Test Case 2: Input Validation

```
1. Add todo with empty text → Should show error and re-prompt
2. Add todo with only spaces → Should show error and re-prompt
3. Add todo with 201 characters → Should show error and re-prompt
4. Add todo with valid text → Should succeed
5. Update todo with invalid number → Should show error and re-prompt
6. Update todo with non-numeric input → Should show error and re-prompt
7. Menu selection with invalid number → Should show error and re-display menu
8. Menu selection with non-numeric input → Should show error and re-display menu
```

### Test Case 3: Sequential Operations

```
1. Add todo "Task 1"
2. Add todo "Task 2"
3. Add todo "Task 3"
4. View todos → Should show 3 todos numbered 1, 2, 3
5. Mark todo #2 complete → Should show [DONE] for #2 only
6. Delete todo #1 → Should show 2 todos numbered 1, 2 (renumbered)
7. Update todo #1 → Should update the former "Task 2"
8. View todos → Should show correct state
```

### Test Case 4: Edge Cases

```
1. Add 10 todos
2. Delete all todos one by one
3. Verify list is empty
4. Add new todo → Should be numbered #1
5. Mark todo complete twice → Should remain complete (idempotent)
6. Try to delete todo #999 → Should show error
7. Try to update todo #-1 → Should show error
```

---

## Troubleshooting

### Application Won't Start

**Issue**: `ModuleNotFoundError` or import errors

**Solution**:
```bash
# Ensure you're in the correct directory
cd Hackathon-II_Phase-I

# Verify Python version
python --version

# Reinstall virtual environment
uv venv --force
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### Invalid Input Handling

**Issue**: Application crashes on invalid input

**Solution**: This should not happen. If it does, it's a bug. Report with:
- Input that caused crash
- Error message
- Steps to reproduce

### Unicode/Character Encoding Issues

**Issue**: Special characters display incorrectly

**Solution**:
```bash
# Ensure terminal uses UTF-8 encoding
# Windows PowerShell:
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Windows CMD:
chcp 65001

# macOS/Linux: Usually UTF-8 by default
```

---

## Expected Behavior

### State Management

- ✅ Todos persist during application session
- ✅ Todos are lost when application exits (expected)
- ✅ Sequential numbering maintained (1, 2, 3...)
- ✅ Automatic renumbering after deletions

### Error Handling

- ✅ Invalid input shows error and re-prompts (no crash)
- ✅ Out-of-range todo numbers show clear error
- ✅ Non-numeric input handled gracefully
- ✅ Empty/whitespace-only descriptions rejected

### Display Format

- ✅ Todos show with 1-based numbering
- ✅ Status shows as [TODO] or [DONE]
- ✅ Menu displays after each operation
- ✅ Updated list displays after modifications

---

## Performance Expectations

- **Add todo**: < 1 second
- **View todos**: < 1 second (up to 1000 todos)
- **Update todo**: < 1 second
- **Delete todo**: < 1 second
- **Mark complete**: < 1 second
- **Session stability**: 1 hour without degradation

---

## Next Steps

After validating Phase I:

1. **Run `/sp.tasks`**: Generate task decomposition
2. **Implement tasks**: Follow agentic workflow (spec → plan → tasks → implementation)
3. **Validate**: Test against acceptance criteria
4. **Prepare for Phase II**: Domain logic ready for database migration

---

## Support

For issues or questions:
- Check specification: `specs/001-phase1-todo/spec.md`
- Review implementation plan: `specs/001-phase1-todo/plan.md`
- Review data model: `specs/001-phase1-todo/data-model.md`
- Review research decisions: `specs/001-phase1-todo/research.md`
