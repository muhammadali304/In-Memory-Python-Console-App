# Tasks: Phase I In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-phase1-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, research.md

**Tests**: Tests are NOT requested in the feature specification. This implementation uses manual console-based validation only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure (src/, src/domain/, src/cli/, src/utils/, tests/manual/)
- [X] T002 Initialize UV environment with Python 3.13+
- [X] T003 [P] Create __init__.py files in src/, src/domain/, src/cli/, src/utils/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Create exception hierarchy in src/domain/exceptions.py (TodoError, InvalidTodoError, TodoNotFoundError)
- [X] T005 [P] Create logger utility in src/utils/logger.py with INFO/WARNING/ERROR levels
- [X] T006 [P] Create input validation functions in src/cli/input_handler.py (validate_description, validate_numeric_input)
- [X] T007 [P] Create output formatting utilities in src/cli/output.py (display_todos, display_message, display_error)
- [X] T008 Create menu display function in src/cli/menu.py (show_menu, get_menu_choice)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can add new todos and view all todos in a list

**Independent Test**: Launch app, add 2-3 todos with different descriptions, view list, verify all todos appear correctly with [TODO] status

### Implementation for User Story 1

- [X] T009 [P] [US1] Create Todo entity dataclass in src/domain/todo.py (description: str, is_complete: bool = False)
- [X] T010 [US1] Create TodoService class with __init__ method in src/domain/todo_service.py (initialize empty list)
- [X] T011 [US1] Implement add_todo method in src/domain/todo_service.py (validate description, create Todo, append to list, log operation)
- [X] T012 [US1] Implement get_all_todos method in src/domain/todo_service.py (return list of (index, todo) tuples with 1-based numbering)
- [X] T013 [US1] Implement add todo CLI handler in src/cli/input_handler.py (prompt for description, validate, call service.add_todo)
- [X] T014 [US1] Implement view todos display in src/cli/output.py (format as "1. [TODO] Description", handle empty list)
- [X] T015 [US1] Create main.py entry point with menu loop (options: 1=Add, 2=View, 6=Exit, auto-display after add)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently (MVP complete)

---

## Phase 4: User Story 2 - Mark Todos as Complete (Priority: P2)

**Goal**: Users can mark any todo as complete, changing status from [TODO] to [DONE]

**Independent Test**: Add 3 todos, mark the 2nd one as complete, view list, verify only #2 shows [DONE] status

### Implementation for User Story 2

- [X] T016 [US2] Implement mark_complete method in src/domain/todo_service.py (validate index, set is_complete=True, log operation, idempotent)
- [X] T017 [US2] Implement mark complete CLI handler in src/cli/input_handler.py (prompt for todo number, validate numeric input, call service.mark_complete)
- [X] T018 [US2] Update main.py to add menu option 5 for mark complete (auto-display after operation)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Todos (Priority: P3)

**Goal**: Users can remove any todo from the list permanently

**Independent Test**: Add 4 todos, delete the 3rd one, view list, verify only 3 todos remain with correct sequential numbering (1, 2, 3)

### Implementation for User Story 3

- [X] T019 [US3] Implement delete_todo method in src/domain/todo_service.py (validate index, remove from list, log operation with description)
- [X] T020 [US3] Implement delete CLI handler in src/cli/input_handler.py (prompt for todo number, validate numeric input, call service.delete_todo)
- [X] T021 [US3] Update main.py to add menu option 4 for delete (auto-display after operation)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo Text (Priority: P4)

**Goal**: Users can edit the description text of any existing todo

**Independent Test**: Add todo "Buy mlk", update it to "Buy milk", view list, verify text changed while status remained unchanged

### Implementation for User Story 4

- [X] T022 [US4] Implement update_todo method in src/domain/todo_service.py (validate index, validate new description, update description, preserve is_complete, log operation)
- [X] T023 [US4] Implement update CLI handler in src/cli/input_handler.py (prompt for todo number, prompt for new description, validate both, call service.update_todo)
- [X] T024 [US4] Update main.py to add menu option 3 for update (auto-display after operation)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T025 [P] Add structured logging to all TodoService methods (add, update, delete, mark_complete)
- [X] T026 [P] Verify error handling for all edge cases (empty list, invalid IDs, whitespace-only input, 201+ characters)
- [X] T027 [P] Create manual test scenarios document in tests/manual/test_scenarios.md
- [X] T028 Code review for PEP 8 compliance (formatting, naming conventions)
- [X] T029 Verify separation of concerns (CLI vs domain logic independence)
- [X] T030 Final validation against all acceptance criteria from spec.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Requires US1 for testing but implementation is independent
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Requires US1 for testing but implementation is independent
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Requires US1 for testing but implementation is independent

### Within Each User Story

- Models before services (T009 before T010-T012 in US1)
- Services before CLI handlers (T010-T012 before T013-T014 in US1)
- CLI handlers before main.py integration (T013-T014 before T015 in US1)
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003)
- All Foundational tasks marked [P] can run in parallel (T004, T005, T006, T007)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel (T009 in US1)
- Polish tasks marked [P] can run in parallel (T025, T026, T027)

---

## Parallel Example: User Story 1

```bash
# After Foundational phase completes, launch US1 tasks:

# Parallel: Create entity and service class structure
Task T009: "Create Todo entity dataclass in src/domain/todo.py"
Task T010: "Create TodoService class with __init__ in src/domain/todo_service.py"

# Sequential: Implement service methods (depend on T010)
Task T011: "Implement add_todo method in src/domain/todo_service.py"
Task T012: "Implement get_all_todos method in src/domain/todo_service.py"

# Parallel: Implement CLI handlers (depend on T011, T012)
Task T013: "Implement add todo CLI handler in src/cli/input_handler.py"
Task T014: "Implement view todos display in src/cli/output.py"

# Sequential: Integrate into main (depends on T013, T014)
Task T015: "Create main.py entry point with menu loop"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (T009-T015)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Manual validation: Add todos, view list, test edge cases (empty input, 201 chars, whitespace)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **MVP Delivered!**
3. Add User Story 2 → Test independently → Mark complete feature added
4. Add User Story 3 → Test independently → Delete feature added
5. Add User Story 4 → Test independently → Update feature added
6. Complete Polish phase → Production ready

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (T009-T015)
   - Developer B: User Story 2 (T016-T018) - waits for US1 completion for testing
   - Developer C: User Story 3 (T019-T021) - waits for US1 completion for testing
   - Developer D: User Story 4 (T022-T024) - waits for US1 completion for testing
3. Stories complete and integrate independently

**Note**: In practice, US2-US4 should wait for US1 to complete since they need the add/view functionality for testing.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- No test tasks included (manual validation only per spec)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Manual Validation Checklist

After completing each user story, perform these manual tests:

### User Story 1 (Add and View)
- [ ] Launch app, verify menu displays with options 1, 2, 6
- [ ] Add todo "Buy groceries", verify confirmation and auto-display
- [ ] Add todo "Call dentist", verify both todos display with [TODO] status
- [ ] Try to add empty todo, verify error and re-prompt
- [ ] Try to add 201-character todo, verify error and re-prompt
- [ ] View todos when list is empty, verify "No todos found" message

### User Story 2 (Mark Complete)
- [ ] Add 3 todos, mark #2 complete, verify only #2 shows [DONE]
- [ ] Mark already complete todo, verify idempotent (no error)
- [ ] Try to mark todo #99, verify error message

### User Story 3 (Delete)
- [ ] Add 4 todos, delete #3, verify 3 remain with correct numbering (1, 2, 3)
- [ ] Delete last remaining todo, verify empty list message
- [ ] Try to delete todo #99, verify error message

### User Story 4 (Update)
- [ ] Add todo "Buy mlk", update to "Buy milk", verify text changed
- [ ] Update todo and verify status preserved (complete stays complete)
- [ ] Try to update with empty text, verify error and re-prompt
- [ ] Try to update todo #99, verify error message

### Edge Cases
- [ ] Non-numeric input for menu choice, verify error and re-prompt
- [ ] Non-numeric input for todo number, verify error and re-prompt
- [ ] Negative number for todo selection, verify error
- [ ] Whitespace-only todo description, verify rejection
- [ ] Sequential operations: add → complete → delete → view
- [ ] Restart app, verify state resets (expected behavior)
