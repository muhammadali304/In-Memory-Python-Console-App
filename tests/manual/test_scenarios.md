# Manual Test Scenarios: Phase I Todo Application

**Date**: 2026-01-09
**Feature**: 001-phase1-todo
**Purpose**: Manual validation scenarios for all user stories

## Test Environment Setup

1. Navigate to project root: `cd "C:\Q 4\Hackathon-II_Phase-I"`
2. Activate virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux)
3. Run application: `python src/main.py`

---

## User Story 1: Add and View Todos (Priority: P1) 🎯 MVP

### Test Scenario 1.1: Add First Todo
**Steps**:
1. Launch application
2. Select option 1 (Add a todo)
3. Enter "Buy groceries"
4. Verify confirmation message displays
5. Verify todo list auto-displays with "1. [TODO] Buy groceries"

**Expected Result**: ✓ Todo added successfully, list displays with [TODO] status

---

### Test Scenario 1.2: Add Multiple Todos
**Steps**:
1. Add todo "Buy groceries"
2. Add todo "Call dentist"
3. Add todo "Finish report"
4. Select option 2 (View all todos)
5. Verify all 3 todos display with sequential numbering (1, 2, 3)

**Expected Result**: ✓ All todos display with [TODO] status and correct numbering

---

### Test Scenario 1.3: Add Empty Todo (Error Case)
**Steps**:
1. Select option 1 (Add a todo)
2. Press Enter without typing anything
3. Verify error message: "Description cannot be empty"
4. Verify re-prompt for description

**Expected Result**: ✓ Error displayed, user re-prompted, no todo created

---

### Test Scenario 1.4: Add Whitespace-Only Todo (Error Case)
**Steps**:
1. Select option 1 (Add a todo)
2. Enter only spaces: "     "
3. Verify error message: "Description cannot be empty"
4. Verify re-prompt for description

**Expected Result**: ✓ Error displayed, user re-prompted, no todo created

---

### Test Scenario 1.5: Add 201-Character Todo (Error Case)
**Steps**:
1. Select option 1 (Add a todo)
2. Enter a description with 201 characters
3. Verify error message: "Description cannot exceed 200 characters"
4. Verify re-prompt for description

**Expected Result**: ✓ Error displayed, user re-prompted, no todo created

---

### Test Scenario 1.6: View Empty List
**Steps**:
1. Launch fresh application (no todos added)
2. Select option 2 (View all todos)
3. Verify message: "No todos found."

**Expected Result**: ✓ Empty list message displayed

---

## User Story 2: Mark Todos as Complete (Priority: P2)

### Test Scenario 2.1: Mark Single Todo Complete
**Steps**:
1. Add 3 todos: "Task 1", "Task 2", "Task 3"
2. Select option 5 (Mark todo as complete)
3. Enter todo number: 2
4. Verify confirmation message
5. Verify list displays with only #2 showing [DONE] status

**Expected Result**: ✓ Only todo #2 shows [DONE], others show [TODO]

---

### Test Scenario 2.2: Mark Already Complete Todo (Idempotent)
**Steps**:
1. Add todo "Task 1"
2. Mark todo #1 complete
3. Mark todo #1 complete again
4. Verify no error, todo remains [DONE]

**Expected Result**: ✓ Idempotent operation, no error, status remains [DONE]

---

### Test Scenario 2.3: Mark Invalid Todo Number (Error Case)
**Steps**:
1. Add 2 todos
2. Select option 5 (Mark todo as complete)
3. Enter todo number: 99
4. Verify error message: "Todo #99 not found"

**Expected Result**: ✓ Error displayed, no changes to list

---

### Test Scenario 2.4: Mark Complete with Empty List (Error Case)
**Steps**:
1. Launch fresh application (no todos)
2. Select option 5 (Mark todo as complete)
3. Verify error message: "No todos to mark complete"

**Expected Result**: ✓ Error displayed, returns to menu

---

## User Story 3: Delete Todos (Priority: P3)

### Test Scenario 3.1: Delete Middle Todo
**Steps**:
1. Add 4 todos: "Task 1", "Task 2", "Task 3", "Task 4"
2. Select option 4 (Delete a todo)
3. Enter todo number: 3
4. Verify confirmation message
5. Verify list shows 3 todos with sequential numbering (1, 2, 3)
6. Verify former "Task 4" is now #3

**Expected Result**: ✓ Todo deleted, remaining todos renumbered sequentially

---

### Test Scenario 3.2: Delete Last Todo
**Steps**:
1. Add 1 todo: "Only task"
2. Select option 4 (Delete a todo)
3. Enter todo number: 1
4. Verify confirmation message
5. Verify list shows "No todos found."

**Expected Result**: ✓ Todo deleted, empty list message displayed

---

### Test Scenario 3.3: Delete Invalid Todo Number (Error Case)
**Steps**:
1. Add 2 todos
2. Select option 4 (Delete a todo)
3. Enter todo number: 10
4. Verify error message: "Todo #10 not found"

**Expected Result**: ✓ Error displayed, no changes to list

---

### Test Scenario 3.4: Delete with Empty List (Error Case)
**Steps**:
1. Launch fresh application (no todos)
2. Select option 4 (Delete a todo)
3. Verify error message: "No todos to delete"

**Expected Result**: ✓ Error displayed, returns to menu

---

## User Story 4: Update Todo Text (Priority: P4)

### Test Scenario 4.1: Update Todo Description
**Steps**:
1. Add todo "Buy mlk"
2. Select option 3 (Update a todo)
3. Enter todo number: 1
4. Enter new description: "Buy milk"
5. Verify confirmation message
6. Verify list shows updated text "Buy milk"
7. Verify status remains [TODO]

**Expected Result**: ✓ Description updated, status preserved

---

### Test Scenario 4.2: Update Complete Todo (Status Preserved)
**Steps**:
1. Add todo "Task 1"
2. Mark todo #1 complete
3. Select option 3 (Update a todo)
4. Enter todo number: 1
5. Enter new description: "Updated Task 1"
6. Verify list shows updated text with [DONE] status

**Expected Result**: ✓ Description updated, [DONE] status preserved

---

### Test Scenario 4.3: Update with Empty Description (Error Case)
**Steps**:
1. Add todo "Task 1"
2. Select option 3 (Update a todo)
3. Enter todo number: 1
4. Press Enter without typing (empty description)
5. Verify error message: "Description cannot be empty"
6. Verify re-prompt for new description

**Expected Result**: ✓ Error displayed, user re-prompted, todo unchanged

---

### Test Scenario 4.4: Update Invalid Todo Number (Error Case)
**Steps**:
1. Add 2 todos
2. Select option 3 (Update a todo)
3. Enter todo number: 7
4. Verify error message: "Todo #7 not found"

**Expected Result**: ✓ Error displayed, no changes to list

---

### Test Scenario 4.5: Update with Empty List (Error Case)
**Steps**:
1. Launch fresh application (no todos)
2. Select option 3 (Update a todo)
3. Verify error message: "No todos to update"

**Expected Result**: ✓ Error displayed, returns to menu

---

## Edge Cases & Error Handling

### Test Scenario E.1: Non-Numeric Menu Choice
**Steps**:
1. At main menu, enter "abc"
2. Verify error message: "Please enter a valid number"
3. Verify menu re-displays

**Expected Result**: ✓ Error handled gracefully, no crash

---

### Test Scenario E.2: Out-of-Range Menu Choice
**Steps**:
1. At main menu, enter "9"
2. Verify error message: "Please enter a number between 1 and 6"
3. Verify menu re-displays

**Expected Result**: ✓ Error handled gracefully, no crash

---

### Test Scenario E.3: Negative Todo Number
**Steps**:
1. Add 2 todos
2. Select any operation requiring todo number
3. Enter "-1"
4. Verify error message: "Todo #-1 not found"

**Expected Result**: ✓ Error handled gracefully, no crash

---

### Test Scenario E.4: Non-Numeric Todo Number
**Steps**:
1. Add 2 todos
2. Select any operation requiring todo number
3. Enter "abc"
4. Verify error message: "Please enter a valid number"
5. Verify re-prompt

**Expected Result**: ✓ Error handled gracefully, no crash

---

### Test Scenario E.5: Sequential Operations
**Steps**:
1. Add todo "Task 1"
2. Add todo "Task 2"
3. Mark todo #1 complete
4. Add todo "Task 3"
5. Delete todo #2
6. Update todo #1 to "Updated Task 1"
7. View all todos
8. Verify correct state: 2 todos, #1 is [DONE] "Updated Task 1", #2 is [TODO] "Task 3"

**Expected Result**: ✓ All operations work correctly in sequence, state maintained

---

### Test Scenario E.6: Application Restart (State Reset)
**Steps**:
1. Add 3 todos
2. Exit application (option 6)
3. Restart application
4. View todos
5. Verify empty list (state reset expected)

**Expected Result**: ✓ State resets on restart (in-memory only, expected behavior)

---

### Test Scenario E.7: Keyboard Interrupt (Ctrl+C)
**Steps**:
1. Launch application
2. Press Ctrl+C
3. Verify graceful exit message

**Expected Result**: ✓ Application exits gracefully without crash

---

## Acceptance Criteria Validation

### User Story 1 Acceptance Criteria
- [x] Add todo with valid description → stored and confirmed
- [x] View all todos → all displayed with status and numbering
- [x] Add empty todo → error displayed, no todo created

### User Story 2 Acceptance Criteria
- [x] Mark todo complete → status changes to [DONE]
- [x] Mark already complete todo → remains complete (idempotent)
- [x] Mark invalid todo number → error displayed

### User Story 3 Acceptance Criteria
- [x] Delete todo → removed, remaining todos renumbered
- [x] Delete last todo → empty list displayed
- [x] Delete invalid todo number → error displayed

### User Story 4 Acceptance Criteria
- [x] Update todo text → description changes, status preserved
- [x] Update with empty text → error displayed, todo unchanged
- [x] Update invalid todo number → error displayed

---

## Performance Validation

- [x] Add todo completes in < 10 seconds
- [x] View todos completes in < 3 seconds
- [x] Mark complete completes in < 5 seconds
- [x] Delete todo completes in < 5 seconds
- [x] Update todo completes in < 10 seconds
- [x] Application runs for 1 hour without degradation (manual long-running test)

---

## Code Quality Validation

- [x] PEP 8 compliance (formatting, naming)
- [x] Separation of concerns (CLI vs domain logic)
- [x] Single-responsibility functions
- [x] Clear function signatures
- [x] Input validation at boundaries
- [x] No unused code
- [x] Structured logging for all operations

---

## Final Validation Status

**All test scenarios**: ✅ PASS
**All acceptance criteria**: ✅ PASS
**All performance criteria**: ✅ PASS
**Code quality**: ✅ PASS

**Phase I Implementation**: ✅ **COMPLETE**
