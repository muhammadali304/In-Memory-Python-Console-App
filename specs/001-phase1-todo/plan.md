# Implementation Plan: Phase I In-Memory Console Todo Application

**Branch**: `001-phase1-todo` | **Date**: 2026-01-09 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-phase1-todo/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a command-line todo application that manages tasks entirely in memory using Python 3.13+ and UV environment. The application provides a menu-driven interface for five core operations: add, view, update, delete, and mark complete. All state is maintained in memory during runtime with no persistence. This phase establishes the foundation for progressive enhancement in future phases by implementing clean separation between CLI interface and domain logic.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory only (Python list/dict structures)
**Testing**: Manual console-based validation for each operation
**Target Platform**: Console/terminal (Windows, macOS, Linux with UTF-8 support)
**Project Type**: Single project (CLI application)
**Performance Goals**: Operations complete in 3-10 seconds, 1-hour session stability without degradation
**Constraints**: No persistence, no external libraries, 200 character limit for todo descriptions, in-memory state only
**Scale/Scope**: Up to 1000 todos per session (no explicit limit enforced)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase I Constraints Compliance

✅ **Console-based input/output only**: Application uses stdin/stdout exclusively (FR-017, FR-018)
✅ **Single executable entry point**: Single main.py or todo.py entry point
✅ **State exists only during runtime**: In-memory storage, no persistence (FR-008)
✅ **No databases, files, or external storage**: Standard library only, no file I/O
✅ **No network calls**: No network dependencies or API calls
✅ **No persistence between runs**: Expected behavior, documented in assumptions

### Core Principles Compliance

✅ **I. Correctness Before Complexity**: Simple in-memory implementation, no premature optimization
✅ **II. Spec-Driven Development**: Complete specification exists with acceptance criteria
✅ **III. Progressive Enhancement**: Domain logic designed to be reusable in Phase II (database layer)
✅ **IV. Separation of Concerns**: Clear separation between CLI layer (input/output) and domain logic (todo operations)
✅ **V. Deterministic Behavior**: All operations are deterministic, no randomness or external dependencies
⚠️ **VI. Observability-Ready Design**: Need to add basic logging for significant operations (add, delete, update, complete)
✅ **VII. Security By Default**: Input validation required (empty text, whitespace, 200 char limit, numeric validation)

### Code Quality Standards Compliance

✅ **Clean, readable, maintainable code**: PEP 8 formatting, single-responsibility functions
✅ **Single-responsibility principle**: Separate modules for domain logic, CLI, validation
✅ **No unused code**: Implement only specified features
✅ **Comments explain "why"**: Code should be self-documenting for "what"

### Architecture Standards Compliance

✅ **Domain logic framework-agnostic**: Todo operations independent of CLI interface
✅ **Storage layer replaceable**: In-memory storage can be swapped for database in Phase II
✅ **No tight coupling**: CLI depends on domain logic, but domain logic is independent
✅ **Interfaces explicit**: Clear function signatures for all operations

### Testing Standards Compliance

✅ **Phase I–II: Manual testing + basic automated tests**: Manual console-based validation specified
✅ **Every feature testable**: All operations have acceptance scenarios
✅ **Tests deterministic**: All operations produce predictable outputs

### Action Items from Constitution Check

1. **Add basic logging**: Implement structured logging for add, delete, update, complete operations (Observability-Ready Design)
2. **Document architecture**: Ensure separation of concerns is explicit in code structure

**GATE STATUS**: ✅ **PASS** (with action item for logging)

## Project Structure

### Documentation (this feature)

```text
specs/001-phase1-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command) - N/A for CLI app
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Entry point with menu loop
├── domain/
│   ├── __init__.py
│   ├── todo.py          # Todo entity (dataclass)
│   └── todo_service.py  # Business logic (add, view, update, delete, complete)
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Menu display and selection
│   ├── input_handler.py # Input validation and prompting
│   └── output.py        # Display formatting (list, messages, errors)
└── utils/
    ├── __init__.py
    └── logger.py        # Basic logging utility

tests/
└── manual/
    └── test_scenarios.md # Manual test scenarios for validation
```

**Structure Decision**: Single project structure selected because this is a standalone CLI application with no web/mobile components. The structure separates domain logic (`domain/`), CLI interface (`cli/`), and utilities (`utils/`) to enable clean separation of concerns and facilitate Phase II migration where domain logic will be reused with a web API layer.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations requiring justification. The observability action item (adding logging) is an enhancement, not a violation.

## Phase 0: Research & Technical Decisions

### Research Questions

1. **Data structure for in-memory todo storage**: List vs Dict, indexing strategy
2. **Menu-driven CLI patterns in Python**: Best practices for input loops and error recovery
3. **Input validation patterns**: Strategies for validating text length, whitespace, numeric input
4. **Logging approach for Phase I**: Minimal logging that can scale to Phase II

### Research Findings

*(To be filled in research.md)*

## Phase 1: Design Artifacts

### Data Model

*(To be filled in data-model.md)*

**Key Entity**: Todo
- Fields: description (str), is_complete (bool)
- Validation: 1-200 characters, no whitespace-only
- Storage: List with sequential indexing (1-based for user display)

### API Contracts

**N/A for Phase I**: CLI application has no API endpoints. Internal function signatures will be documented in data-model.md.

### Quickstart Guide

*(To be filled in quickstart.md)*

**Setup**: UV environment initialization
**Run**: `uv run python src/main.py`
**Operations**: Menu-driven interface with 6 options (add, view, update, delete, complete, exit)

## Phase 2: Task Decomposition

**Note**: Task decomposition is handled by `/sp.tasks` command, not `/sp.plan`.

Tasks will be organized by user story priority:
- P1: Add and View Todos (MVP)
- P2: Mark Todos as Complete
- P3: Delete Todos
- P4: Update Todo Text

## Implementation Notes

### Key Architectural Decisions

1. **List-based storage with 1-based indexing**: Use Python list for todos, display with 1-based numbering to users, convert to 0-based internally
2. **Menu-driven loop**: Continuous loop showing menu after each operation until user exits
3. **Auto-display after modifications**: Show updated todo list after add/delete/update/complete operations
4. **Re-prompt on errors**: Display error and re-prompt within same operation context (no return to menu)
5. **Status display format**: [TODO] for incomplete, [DONE] for complete

### Tradeoffs

**Simplicity vs Extensibility**:
- **Chosen**: Simple list-based storage with sequential indexing
- **Rationale**: Meets Phase I requirements, easy to understand and test
- **Future**: Phase II will replace in-memory list with database, domain logic remains unchanged

**Menu-driven vs Command-driven**:
- **Chosen**: Menu-driven loop (clarified in spec)
- **Rationale**: More user-friendly for console application, self-explanatory interface
- **Alternative rejected**: Command-driven would require users to remember command syntax

**Auto-display vs Manual view**:
- **Chosen**: Auto-display list after modifications (clarified in spec)
- **Rationale**: Immediate visual feedback, reduces need for manual "view" operations
- **Alternative rejected**: Manual view only would require extra steps after each change

### Error Handling Strategy

1. **Input validation**: Validate before processing (empty text, whitespace, length, numeric)
2. **Error messages**: Clear, user-friendly messages (no technical details)
3. **Recovery**: Re-prompt within same operation context (no crash, no return to menu)
4. **Edge cases**: Handle empty list, invalid IDs, out-of-range numbers, non-numeric input

### Testing Strategy

**Manual Console-Based Validation**:
1. Launch application and verify menu displays
2. Test each operation with valid inputs
3. Test each operation with invalid inputs (empty, whitespace, too long, invalid IDs)
4. Test edge cases (empty list, single item, many items)
5. Test sequential operations (add → complete → delete → view)
6. Verify state resets on restart (expected behavior)

**Code Review Criteria**:
1. PEP 8 compliance (formatting, naming)
2. Separation of concerns (CLI vs domain logic)
3. Single-responsibility functions
4. Clear function signatures
5. Input validation at boundaries
6. No unused code

## Next Steps

1. ✅ Complete Phase 0: Create research.md with technical decisions
2. ✅ Complete Phase 1: Create data-model.md, quickstart.md
3. ⏭️ Run `/sp.tasks` to generate task decomposition
4. ⏭️ Implement tasks following agentic workflow
5. ⏭️ Validate against acceptance criteria
