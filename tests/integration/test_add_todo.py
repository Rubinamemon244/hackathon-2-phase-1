"""
Integration tests for the add todo flow.
"""
import unittest
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService


class TestAddTodoIntegration(unittest.TestCase):
    """
    Integration tests for the add todo flow.
    """

    def setUp(self):
        """Set up a fresh service for each test."""
        self.store = InMemoryStore()
        self.service = TodoService(self.store)

    def test_add_todo_integration_flow(self):
        """Test the complete add todo flow from service to store."""
        # Add a todo using the service
        todo_id = self.service.add_todo("Integration test todo")

        # Verify the todo was added with correct ID
        self.assertEqual(todo_id, 1)

        # Verify the todo exists in the store
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 1)

        # Verify the todo has correct properties
        todo = todos[0]
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Integration test todo")
        self.assertEqual(todo.status, "pending")

    def test_add_multiple_todos_integration_flow(self):
        """Test adding multiple todos through the service."""
        # Add multiple todos
        id1 = self.service.add_todo("First todo")
        id2 = self.service.add_todo("Second todo")
        id3 = self.service.add_todo("Third todo")

        # Verify IDs are sequential
        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(id3, 3)

        # Verify all todos exist in the store
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 3)

        # Verify each todo has correct properties
        self.assertEqual(todos[0].title, "First todo")
        self.assertEqual(todos[1].title, "Second todo")
        self.assertEqual(todos[2].title, "Third todo")

    def test_add_todo_with_empty_title_fails(self):
        """Test that adding a todo with empty title raises an error."""
        with self.assertRaises(ValueError):
            self.service.add_todo("")

    def test_add_todo_with_whitespace_only_title_fails(self):
        """Test that adding a todo with whitespace-only title raises an error."""
        with self.assertRaises(ValueError):
            self.service.add_todo("   ")

    def test_add_todo_then_retrieve_it(self):
        """Test adding a todo and retrieving it through the service."""
        # Add a todo
        todo_id = self.service.add_todo("Test todo for retrieval")

        # Retrieve all todos
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 1)

        # Verify the retrieved todo matches what was added
        retrieved_todo = todos[0]
        self.assertEqual(retrieved_todo.id, todo_id)
        self.assertEqual(retrieved_todo.title, "Test todo for retrieval")
        self.assertEqual(retrieved_todo.status, "pending")


if __name__ == "__main__":
    unittest.main()