"""
Unit tests for the InMemoryStore.
"""
import unittest
from src.store.in_memory_store import InMemoryStore


class TestInMemoryStore(unittest.TestCase):
    """
    Unit tests for the InMemoryStore class.
    """

    def setUp(self):
        """Set up a fresh store for each test."""
        self.store = InMemoryStore()

    def test_add_todo_success(self):
        """Test adding a todo successfully."""
        todo_id = self.store.add_todo("Test todo")
        self.assertEqual(todo_id, 1)
        todos = self.store.get_all_todos()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].id, 1)
        self.assertEqual(todos[0].title, "Test todo")
        self.assertEqual(todos[0].status, "pending")

    def test_add_todo_with_empty_title_raises_error(self):
        """Test that adding a todo with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            self.store.add_todo("")

    def test_add_todo_with_whitespace_only_title_raises_error(self):
        """Test that adding a todo with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            self.store.add_todo("   ")

    def test_add_multiple_todos_have_sequential_ids(self):
        """Test that multiple todos get sequential IDs."""
        id1 = self.store.add_todo("First todo")
        id2 = self.store.add_todo("Second todo")
        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)

    def test_get_all_todos_empty_store(self):
        """Test getting all todos from an empty store."""
        todos = self.store.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_get_all_todos_with_todos(self):
        """Test getting all todos from a store with todos."""
        self.store.add_todo("First todo")
        self.store.add_todo("Second todo")
        todos = self.store.get_all_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].title, "First todo")
        self.assertEqual(todos[1].title, "Second todo")

    def test_get_todo_by_id_existing(self):
        """Test getting a todo by its ID when it exists."""
        todo_id = self.store.add_todo("Test todo")
        todo = self.store.get_todo_by_id(todo_id)
        self.assertIsNotNone(todo)
        self.assertEqual(todo.id, todo_id)
        self.assertEqual(todo.title, "Test todo")

    def test_get_todo_by_id_non_existing(self):
        """Test getting a todo by its ID when it doesn't exist."""
        todo = self.store.get_todo_by_id(999)
        self.assertIsNone(todo)

    def test_update_todo_success(self):
        """Test updating a todo successfully."""
        todo_id = self.store.add_todo("Original todo")
        result = self.store.update_todo(todo_id, "Updated todo")
        self.assertTrue(result)

        todos = self.store.get_all_todos()
        self.assertEqual(todos[0].title, "Updated todo")

    def test_update_todo_non_existing(self):
        """Test updating a non-existing todo returns False."""
        result = self.store.update_todo(999, "Updated todo")
        self.assertFalse(result)

    def test_update_todo_with_empty_title_returns_false(self):
        """Test updating a todo with empty title returns False."""
        todo_id = self.store.add_todo("Original todo")
        result = self.store.update_todo(todo_id, "")
        self.assertFalse(result)

    def test_update_todo_with_whitespace_only_title_returns_false(self):
        """Test updating a todo with whitespace-only title returns False."""
        todo_id = self.store.add_todo("Original todo")
        result = self.store.update_todo(todo_id, "   ")
        self.assertFalse(result)

    def test_delete_todo_success(self):
        """Test deleting a todo successfully."""
        todo_id = self.store.add_todo("Test todo")
        result = self.store.delete_todo(todo_id)
        self.assertTrue(result)

        todos = self.store.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_delete_todo_non_existing(self):
        """Test deleting a non-existing todo returns False."""
        result = self.store.delete_todo(999)
        self.assertFalse(result)

    def test_mark_complete_success(self):
        """Test marking a todo as complete successfully."""
        todo_id = self.store.add_todo("Test todo")
        result = self.store.mark_complete(todo_id)
        self.assertTrue(result)

        todo = self.store.get_todo_by_id(todo_id)
        self.assertEqual(todo.status, "completed")

    def test_mark_complete_non_existing(self):
        """Test marking a non-existing todo as complete returns False."""
        result = self.store.mark_complete(999)
        self.assertFalse(result)

    def test_clear_all(self):
        """Test clearing all todos from the store."""
        self.store.add_todo("First todo")
        self.store.add_todo("Second todo")
        self.assertEqual(len(self.store.get_all_todos()), 2)

        self.store.clear_all()
        self.assertEqual(len(self.store.get_all_todos()), 0)


if __name__ == "__main__":
    unittest.main()