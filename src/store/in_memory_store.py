"""
In-memory store for managing todos during application runtime.
"""
from typing import List, Optional, Dict, Any
from src.models.todo import Todo


class InMemoryStore:
    """
    In-memory store that manages the lifecycle of todos during runtime.
    """
    def __init__(self):
        """Initialize the in-memory store with an empty list of todos."""
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add_todo(self, title: str) -> int:
        """
        Add a new todo with the given title to the store.

        Args:
            title: The title/description of the todo

        Returns:
            The unique ID of the created todo

        Raises:
            ValueError: If the title is empty or whitespace-only
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty or whitespace-only")

        todo_id = self._next_id
        self._next_id += 1
        todo = Todo(id=todo_id, title=title.strip(), status="pending")
        self._todos[todo_id] = todo
        return todo_id

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the store.

        Returns:
            List of all todos
        """
        return list(self._todos.values())

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo if found, None otherwise
        """
        return self._todos.get(todo_id)

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the todo was updated, False if not found or invalid title
        """
        if not new_title or not new_title.strip():
            return False

        if todo_id in self._todos:
            self._todos[todo_id].title = new_title.strip()
            return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as completed by its ID.

        Args:
            todo_id: The ID of the todo to mark as complete

        Returns:
            True if the todo was marked complete, False if not found
        """
        if todo_id in self._todos:
            self._todos[todo_id].complete()
            return True
        return False

    def clear_all(self):
        """
        Clear all todos from the store.
        """
        self._todos.clear()
        self._next_id = 1