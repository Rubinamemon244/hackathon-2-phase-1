# Todo API Contracts

## Overview
This document defines the internal service contracts for the Console Todo Application. These contracts represent the interface between the CLI controller and the Todo service layer.

## Todo Service Interface

### Add Todo
- **Method**: `add_todo(title: str) -> int`
- **Input**: Todo title/description (string)
- **Output**: Unique ID of the created todo (integer)
- **Preconditions**: Title is not empty or whitespace-only
- **Postconditions**: New todo is added to the in-memory store with "pending" status
- **Error cases**: Raises ValueError if title is empty or whitespace-only

### View Todos
- **Method**: `get_all_todos() -> List[dict]`
- **Input**: None
- **Output**: List of todo objects with id, title, and status
- **Preconditions**: None
- **Postconditions**: Returns all todos in the store
- **Error cases**: None

### Update Todo
- **Method**: `update_todo(todo_id: int, new_title: str) -> bool`
- **Input**: Todo ID (integer) and new title (string)
- **Output**: Boolean indicating success (true) or failure (false)
- **Preconditions**: Todo with given ID exists, new title is not empty
- **Postconditions**: Todo title is updated if successful
- **Error cases**: Returns false if todo ID doesn't exist or title is invalid

### Delete Todo
- **Method**: `delete_todo(todo_id: int) -> bool`
- **Input**: Todo ID (integer)
- **Output**: Boolean indicating success (true) or failure (false)
- **Preconditions**: Todo with given ID exists
- **Postconditions**: Todo is removed from the store if successful
- **Error cases**: Returns false if todo ID doesn't exist

### Mark Complete
- **Method**: `mark_complete(todo_id: int) -> bool`
- **Input**: Todo ID (integer)
- **Output**: Boolean indicating success (true) or failure (false)
- **Preconditions**: Todo with given ID exists
- **Postconditions**: Todo status is updated to "completed" if successful
- **Error cases**: Returns false if todo ID doesn't exist

## Data Contracts

### Todo Object
```python
{
    "id": int,           # Unique identifier
    "title": str,        # Task description
    "status": str        # "pending" or "completed"
}
```

### Error Response
```python
{
    "success": bool,     # False for errors
    "message": str,      # Error description
    "data": optional     # Additional data if applicable
}
```

### Success Response
```python
{
    "success": bool,     # True for successful operations
    "message": str,      # Optional success message
    "data": any          # Operation result data
}
```