"""
Integration tests for the view todos flow.
"""
import unittest
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService


class TestViewTodosIntegration(unittest.TestCase):
    """
    Integration tests for the view todos flow.
    """

    def setUp(self):
        """Set up a fresh service for each test."""
        self.store = InMemoryStore()
        self.service = TodoService(self.store)

    def test_view_todos_empty_store(self):
        """Test viewing todos when the store is empty."""
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_view_todos_single_todo(self):
        """Test viewing todos when there's a single todo."""
        # Add a todo
        self.service.add_todo("Test todo")

        # View todos
        todos = self.service.get_all_todos()

        # Verify the todo is returned
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, "Test todo")
        self.assertEqual(todos[0].status, "pending")

    def test_view_todos_multiple_todos(self):
        """Test viewing todos when there are multiple todos."""
        # Add multiple todos
        self.service.add_todo("First todo")
        self.service.add_todo("Second todo")
        self.service.add_todo("Third todo")

        # View todos
        todos = self.service.get_all_todos()

        # Verify all todos are returned
        self.assertEqual(len(todos), 3)
        self.assertEqual(todos[0].title, "First todo")
        self.assertEqual(todos[1].title, "Second todo")
        self.assertEqual(todos[2].title, "Third todo")

    def test_view_todos_after_modifications(self):
        """Test viewing todos after adding, updating, and marking complete."""
        # Add todos
        id1 = self.service.add_todo("Todo 1")
        id2 = self.service.add_todo("Todo 2")

        # Update one todo
        self.service.update_todo(id1, "Updated Todo 1")

        # Mark one as complete
        self.service.mark_complete(id2)

        # View todos
        todos = self.service.get_all_todos()

        # Verify modifications are reflected
        self.assertEqual(len(todos), 2)

        # Find the updated todo
        updated_todo = next((t for t in todos if t.id == id1), None)
        self.assertIsNotNone(updated_todo)
        self.assertEqual(updated_todo.title, "Updated Todo 1")
        self.assertEqual(updated_todo.status, "pending")

        # Find the completed todo
        completed_todo = next((t for t in todos if t.id == id2), None)
        self.assertIsNotNone(completed_todo)
        self.assertEqual(completed_todo.title, "Todo 2")
        self.assertEqual(completed_todo.status, "completed")

    def test_view_todos_consistency_with_store(self):
        """Test that viewing todos returns the same data as the store."""
        # Add todos directly to store
        id1 = self.store.add_todo("Store todo 1")
        id2 = self.store.add_todo("Store todo 2")

        # View todos through service
        todos = self.service.get_all_todos()

        # Verify they match
        self.assertEqual(len(todos), 2)
        titles = [todo.title for todo in todos]
        self.assertIn("Store todo 1", titles)
        self.assertIn("Store todo 2", titles)


if __name__ == "__main__":
    unittest.main()