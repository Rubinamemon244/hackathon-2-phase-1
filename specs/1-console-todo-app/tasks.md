---
description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included per plan.md specification (Python unittest framework).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 Create src/models/, src/services/, src/store/, src/cli/ directories
- [X] T003 [P] Create tests/unit/ and tests/integration/ directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo model with id, title, status in src/models/todo.py
- [X] T005 Create in-memory store for todos in src/store/in_memory_store.py
- [X] T006 [P] Create basic CLI controller structure in src/cli/cli_controller.py
- [X] T007 [P] Create main application entry point in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todo items with a description via text-based commands

**Independent Test**: Can be fully tested by running the application, entering the add command with a task description, and verifying the task appears in the list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T008 [P] [US1] Unit test for Todo model in tests/unit/test_todo_model.py
- [X] T009 [P] [US1] Unit test for in-memory store add functionality in tests/unit/test_in_memory_store.py
- [X] T010 [P] [US1] Integration test for add todo flow in tests/integration/test_add_todo.py

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement Todo model with validation in src/models/todo.py
- [X] T012 [US1] Implement add_todo method in src/store/in_memory_store.py
- [X] T013 [US1] Implement add todo functionality in src/services/todo_service.py
- [X] T014 [US1] Implement add command in CLI controller in src/cli/cli_controller.py
- [X] T015 [US1] Add input validation for empty titles in src/cli/cli_controller.py
- [X] T016 [US1] Add success feedback message when todo is added in src/cli/cli_controller.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Display all todo items with their status (pending/completed) and unique identifiers

**Independent Test**: Can be fully tested by adding some tasks and then viewing the list to confirm they appear correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T017 [P] [US2] Unit test for get_all_todos in tests/unit/test_in_memory_store.py
- [X] T018 [P] [US2] Integration test for view todos flow in tests/integration/test_view_todos.py

### Implementation for User Story 2

- [X] T019 [P] [US2] Implement get_all_todos method in src/store/in_memory_store.py
- [X] T020 [US2] Implement get_all_todos method in src/services/todo_service.py
- [X] T021 [US2] Implement view command in CLI controller in src/cli/cli_controller.py
- [X] T022 [US2] Add formatted display of todos with ID, title, and status in src/cli/cli_controller.py
- [X] T023 [US2] Handle empty list case with appropriate message in src/cli/cli_controller.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Complete (Priority: P2)

**Goal**: Allow users to mark todo items as completed by their unique identifier

**Independent Test**: Can be fully tested by adding a task, marking it complete, and verifying its status changes.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US3] Unit test for mark_complete functionality in tests/unit/test_in_memory_store.py
- [X] T025 [P] [US3] Integration test for mark complete flow in tests/integration/test_mark_complete.py

### Implementation for User Story 3

- [X] T026 [P] [US3] Implement mark_complete method in src/store/in_memory_store.py
- [X] T027 [US3] Implement mark_complete method in src/services/todo_service.py
- [X] T028 [US3] Implement mark complete command in CLI controller in src/cli/cli_controller.py
- [X] T029 [US3] Add validation for valid todo ID in src/cli/cli_controller.py
- [X] T030 [US3] Add success feedback when todo is marked complete in src/cli/cli_controller.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Allow users to update the description of existing todo items

**Independent Test**: Can be fully tested by updating a task's description and verifying the change persists.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T031 [P] [US4] Unit test for update_todo functionality in tests/unit/test_in_memory_store.py
- [X] T032 [P] [US4] Integration test for update todo flow in tests/integration/test_update_todo.py

### Implementation for User Story 4

- [X] T033 [P] [US4] Implement update_todo method in src/store/in_memory_store.py
- [X] T034 [US4] Implement update_todo method in src/services/todo_service.py
- [X] T035 [US4] Implement update command in CLI controller in src/cli/cli_controller.py
- [X] T036 [US4] Add validation for valid todo ID and non-empty new title in src/cli/cli_controller.py
- [X] T037 [US4] Add success feedback when todo is updated in src/cli/cli_controller.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to delete todo items by their unique identifier

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T038 [P] [US5] Unit test for delete_todo functionality in tests/unit/test_in_memory_store.py
- [X] T039 [P] [US5] Integration test for delete todo flow in tests/integration/test_delete_todo.py

### Implementation for User Story 5

- [X] T040 [P] [US5] Implement delete_todo method in src/store/in_memory_store.py
- [X] T041 [US5] Implement delete_todo method in src/services/todo_service.py
- [X] T042 [US5] Implement delete command in CLI controller in src/cli/cli_controller.py
- [X] T043 [US5] Add validation for valid todo ID in src/cli/cli_controller.py
- [X] T044 [US5] Add success feedback when todo is deleted in src/cli/cli_controller.py

**Checkpoint**: All 5 core user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T045 [P] Add error handling for invalid commands in src/cli/cli_controller.py
- [X] T046 [P] Add comprehensive error handling for all edge cases in src/cli/cli_controller.py
- [X] T047 [P] Implement main menu and command loop in src/cli/main.py
- [X] T048 [P] Add help command to show available commands in src/cli/cli_controller.py
- [X] T049 [P] Add clear formatting and user-friendly messages across all commands in src/cli/cli_controller.py
- [X] T050 [P] Add validation for all user inputs across all commands in src/cli/cli_controller.py
- [X] T051 [P] Run quickstart validation to ensure all functionality works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/unit/test_todo_model.py"
Task: "Unit test for in-memory store add functionality in tests/unit/test_in_memory_store.py"
Task: "Integration test for add todo flow in tests/integration/test_add_todo.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with validation in src/models/todo.py"
Task: "Implement add_todo method in src/store/in_memory_store.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence