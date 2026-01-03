"""
Integration tests for the update todo flow.
"""
import unittest
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService


class TestUpdateTodoIntegration(unittest.TestCase):
    """
    Integration tests for the update todo flow.
    """

    def setUp(self):
        """Set up a fresh service for each test."""
        self.store = InMemoryStore()
        self.service = TodoService(self.store)

    def test_update_todo_success(self):
        """Test updating a todo successfully."""
        # Add a todo
        todo_id = self.service.add_todo("Original todo")

        # Update the todo
        result = self.service.update_todo(todo_id, "Updated todo")

        # Verify it was updated
        self.assertTrue(result)

        # Verify the new title
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].title, "Updated todo")

    def test_update_todo_non_existing(self):
        """Test updating a non-existing todo."""
        # Try to update a non-existing todo
        result = self.service.update_todo(999, "Updated todo")

        # Verify it returns False
        self.assertFalse(result)

    def test_update_todo_with_empty_title(self):
        """Test updating a todo with empty title."""
        # Add a todo
        todo_id = self.service.add_todo("Original todo")

        # Try to update with empty title
        result = self.service.update_todo(todo_id, "")

        # Verify it returns False
        self.assertFalse(result)

        # Verify the original title is unchanged
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].title, "Original todo")

    def test_update_todo_with_whitespace_only_title(self):
        """Test updating a todo with whitespace-only title."""
        # Add a todo
        todo_id = self.service.add_todo("Original todo")

        # Try to update with whitespace-only title
        result = self.service.update_todo(todo_id, "   ")

        # Verify it returns False
        self.assertFalse(result)

        # Verify the original title is unchanged
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].title, "Original todo")

    def test_update_todo_then_view(self):
        """Test updating a todo and then viewing it."""
        # Add a todo
        todo_id = self.service.add_todo("Original todo")

        # Verify initial title
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].title, "Original todo")

        # Update the todo
        self.service.update_todo(todo_id, "Updated todo")

        # View todos again
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].title, "Updated todo")

    def test_update_multiple_todos(self):
        """Test updating multiple todos."""
        # Add multiple todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")
        id3 = self.service.add_todo("Todo 3")

        # Update some todos
        self.service.update_todo(id1, "Updated Todo 1")
        self.service.update_todo(id3, "Updated Todo 3")

        # Verify updates
        todos = self.service.get_all_todos()
        todo_dict = {todo.id: todo for todo in todos}

        self.assertEqual(todo_dict[id1].title, "Updated Todo 1")
        self.assertEqual(todo_dict[id2].title, "Todo 2")
        self.assertEqual(todo_dict[id3].title, "Updated Todo 3")

    def test_update_todo_integration_with_other_operations(self):
        """Test update works with other operations."""
        # Add todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")

        # Mark one as complete
        self.service.mark_complete(id2)

        # Update the other
        result = self.service.update_todo(id1, "Updated Todo 1")
        self.assertTrue(result)

        # Verify both operations worked
        todos = self.service.get_all_todos()
        todo_dict = {todo.id: todo for todo in todos}

        self.assertEqual(todo_dict[id1].title, "Updated Todo 1")
        self.assertEqual(todo_dict[id1].status, "pending")
        self.assertEqual(todo_dict[id2].title, "Todo 2")
        self.assertEqual(todo_dict[id2].status, "completed")

    def test_update_todo_preserves_status(self):
        """Test that updating a todo preserves its status."""
        # Add a todo and mark it complete
        todo_id = self.service.add_todo("Original todo")
        self.service.mark_complete(todo_id)

        # Verify it's completed
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].status, "completed")

        # Update the todo
        self.service.update_todo(todo_id, "Updated todo")

        # Verify status is still completed
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].status, "completed")
        self.assertEqual(todos[0].title, "Updated todo")


if __name__ == "__main__":
    unittest.main()