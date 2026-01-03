"""
Todo service for handling business logic operations.
"""
from typing import List
from src.models.todo import Todo
from src.store.in_memory_store import InMemoryStore


class TodoService:
    """
    Service layer that handles business logic for todo operations.
    """
    def __init__(self, store: InMemoryStore):
        """
        Initialize the todo service with an in-memory store.

        Args:
            store: The in-memory store to manage todos
        """
        self.store = store

    def add_todo(self, title: str) -> int:
        """
        Add a new todo with the given title.

        Args:
            title: The title/description of the todo

        Returns:
            The unique ID of the created todo
        """
        return self.store.add_todo(title)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            List of all todos
        """
        return self.store.get_all_todos()

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the todo was updated, False otherwise
        """
        return self.store.update_todo(todo_id, new_title)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False otherwise
        """
        return self.store.delete_todo(todo_id)

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as completed by its ID.

        Args:
            todo_id: The ID of the todo to mark as complete

        Returns:
            True if the todo was marked complete, False otherwise
        """
        return self.store.mark_complete(todo_id)