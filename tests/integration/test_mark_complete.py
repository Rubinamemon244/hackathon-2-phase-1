"""
Integration tests for the mark complete flow.
"""
import unittest
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService


class TestMarkCompleteIntegration(unittest.TestCase):
    """
    Integration tests for the mark complete flow.
    """

    def setUp(self):
        """Set up a fresh service for each test."""
        self.store = InMemoryStore()
        self.service = TodoService(self.store)

    def test_mark_complete_success(self):
        """Test marking a todo as complete successfully."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo")

        # Mark it as complete
        result = self.service.mark_complete(todo_id)

        # Verify it was marked complete
        self.assertTrue(result)

        # Verify the status is updated
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].status, "completed")

    def test_mark_complete_non_existing_todo(self):
        """Test marking a non-existing todo as complete."""
        # Try to mark a non-existing todo as complete
        result = self.service.mark_complete(999)

        # Verify it returns False
        self.assertFalse(result)

    def test_mark_complete_then_view(self):
        """Test marking a todo as complete and then viewing it."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo")

        # Verify initial status
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].status, "pending")

        # Mark as complete
        self.service.mark_complete(todo_id)

        # View todos again
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].status, "completed")

    def test_mark_multiple_todos_complete(self):
        """Test marking multiple todos as complete."""
        # Add multiple todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")
        id3 = self.service.add_todo("Todo 3")

        # Mark some as complete
        self.service.mark_complete(id1)
        self.service.mark_complete(id3)

        # Verify statuses
        todos = self.service.get_all_todos()
        todo_dict = {todo.id: todo for todo in todos}

        self.assertEqual(todo_dict[id1].status, "completed")
        self.assertEqual(todo_dict[id2].status, "pending")
        self.assertEqual(todo_dict[id3].status, "completed")

    def test_mark_already_completed_todo(self):
        """Test marking an already completed todo."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo")

        # Mark it as complete
        result1 = self.service.mark_complete(todo_id)
        self.assertTrue(result1)

        # Mark it as complete again
        result2 = self.service.mark_complete(todo_id)
        self.assertTrue(result2)  # Should still return True

        # Verify it's still completed
        todos = self.service.get_all_todos()
        self.assertEqual(todos[0].status, "completed")

    def test_mark_complete_integration_with_other_operations(self):
        """Test mark complete works with other operations."""
        # Add todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")

        # Update a todo
        self.service.update_todo(id1, "Updated Todo 1")

        # Mark a todo as complete
        result = self.service.mark_complete(id2)
        self.assertTrue(result)

        # Verify both operations worked
        todos = self.service.get_all_todos()
        todo_dict = {todo.id: todo for todo in todos}

        self.assertEqual(todo_dict[id1].title, "Updated Todo 1")
        self.assertEqual(todo_dict[id1].status, "pending")
        self.assertEqual(todo_dict[id2].title, "Todo 2")
        self.assertEqual(todo_dict[id2].status, "completed")


if __name__ == "__main__":
    unittest.main()