# Research Summary: Console Todo App

## Decision: Testing Approach
The application will use Python's built-in `unittest` framework for testing, which is part of the standard library and aligns with the constraint of using only standard library components.

## Rationale:
- Uses standard library only (satisfies constraints)
- Provides comprehensive testing capabilities
- Familiar to Python developers
- Supports both unit and integration testing
- No external dependencies required

## Alternatives Considered:
1. **pytest**: More feature-rich but requires external dependency
2. **doctest**: Simpler but less comprehensive for this application
3. **nose**: Third-party tool, violates constraint of standard library only

## Technical Context Updates:
Based on this research, the testing approach in the technical context should be updated to:
- **Testing**: Python unittest framework (standard library)

## Architecture Decisions:
- Todo Model: Simple data class with id, title, and status fields
- In-memory Store: Dictionary-based storage with auto-incrementing IDs
- Todo Service: Encapsulates all business logic for CRUD operations
- CLI Controller: Handles user input parsing and command routing