"""
Integration tests for the delete todo flow.
"""
import unittest
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService


class TestDeleteTodoIntegration(unittest.TestCase):
    """
    Integration tests for the delete todo flow.
    """

    def setUp(self):
        """Set up a fresh service for each test."""
        self.store = InMemoryStore()
        self.service = TodoService(self.store)

    def test_delete_todo_success(self):
        """Test deleting a todo successfully."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo")

        # Delete the todo
        result = self.service.delete_todo(todo_id)

        # Verify it was deleted
        self.assertTrue(result)

        # Verify the todo is gone
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_todo_non_existing(self):
        """Test deleting a non-existing todo."""
        # Try to delete a non-existing todo
        result = self.service.delete_todo(999)

        # Verify it returns False
        self.assertFalse(result)

    def test_delete_one_todo_from_multiple(self):
        """Test deleting one todo from multiple todos."""
        # Add multiple todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")
        id3 = self.service.add_todo("Todo 3")

        # Verify all exist
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 3)

        # Delete one todo
        result = self.service.delete_todo(id2)
        self.assertTrue(result)

        # Verify only two remain
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 2)

        # Verify the right todo was deleted
        todo_ids = [todo.id for todo in todos]
        self.assertIn(id1, todo_ids)
        self.assertNotIn(id2, todo_ids)
        self.assertIn(id3, todo_ids)

    def test_delete_todo_then_view(self):
        """Test deleting a todo and then viewing the list."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo")

        # Verify it exists
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 1)

        # Delete the todo
        self.service.delete_todo(todo_id)

        # Verify it's gone
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_all_todos(self):
        """Test deleting all todos."""
        # Add multiple todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")
        id3 = self.service.add_todo("Todo 3")

        # Delete all
        self.service.delete_todo(id1)
        self.service.delete_todo(id2)
        self.service.delete_todo(id3)

        # Verify none remain
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_todo_integration_with_other_operations(self):
        """Test delete works with other operations."""
        # Add todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")
        id3 = self.service.add_todo("Todo 3")

        # Update a todo
        self.service.update_todo(id1, "Updated Todo 1")

        # Mark a todo as complete
        self.service.mark_complete(id2)

        # Delete a todo
        result = self.service.delete_todo(id3)
        self.assertTrue(result)

        # Verify remaining todos are correct
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 2)

        # Verify the updated and completed todo still exist with correct properties
        todo_dict = {todo.id: todo for todo in todos}
        self.assertEqual(todo_dict[id1].title, "Updated Todo 1")
        self.assertEqual(todo_dict[id1].status, "pending")
        self.assertEqual(todo_dict[id2].title, "Todo 2")
        self.assertEqual(todo_dict[id2].status, "completed")

    def test_delete_todo_with_special_characters(self):
        """Test deleting a todo with special characters in title."""
        # Add a todo with special characters
        todo_id = self.service.add_todo("Test todo with special chars: !@#$%^&*()")

        # Delete the todo
        result = self.service.delete_todo(todo_id)

        # Verify it was deleted
        self.assertTrue(result)

        # Verify the todo is gone
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_then_add_new_todo(self):
        """Test deleting a todo and then adding a new one."""
        # Add a todo
        old_id = self.service.add_todo("Old todo")

        # Delete the todo
        result = self.service.delete_todo(old_id)
        self.assertTrue(result)

        # Add a new todo
        new_id = self.service.add_todo("New todo")

        # Verify the new todo exists
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, "New todo")
        # Note: New ID should be old_id + 1 due to how our store works
        self.assertEqual(todos[0].id, old_id + 1)


if __name__ == "__main__":
    unittest.main()