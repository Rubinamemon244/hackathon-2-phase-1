"""
Unit tests for the Todo model.
"""
import unittest
from src.models.todo import Todo


class TestTodoModel(unittest.TestCase):
    """
    Unit tests for the Todo model class.
    """

    def test_todo_creation_with_valid_data(self):
        """Test creating a Todo with valid data."""
        todo = Todo(id=1, title="Test todo", status="pending")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test todo")
        self.assertEqual(todo.status, "pending")

    def test_todo_creation_with_default_status(self):
        """Test creating a Todo with default status."""
        todo = Todo(id=1, title="Test todo")
        self.assertEqual(todo.status, "pending")

    def test_todo_creation_with_completed_status(self):
        """Test creating a Todo with completed status."""
        todo = Todo(id=1, title="Test todo", status="completed")
        self.assertEqual(todo.status, "completed")

    def test_todo_creation_with_empty_title_raises_error(self):
        """Test that creating a Todo with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            Todo(id=1, title="", status="pending")

    def test_todo_creation_with_whitespace_only_title_raises_error(self):
        """Test that creating a Todo with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            Todo(id=1, title="   ", status="pending")

    def test_todo_creation_with_invalid_status_raises_error(self):
        """Test that creating a Todo with invalid status raises ValueError."""
        with self.assertRaises(ValueError):
            Todo(id=1, title="Test todo", status="invalid")

    def test_todo_complete_method(self):
        """Test that the complete method changes status to completed."""
        todo = Todo(id=1, title="Test todo", status="pending")
        todo.complete()
        self.assertEqual(todo.status, "completed")

    def test_todo_to_dict_method(self):
        """Test that the to_dict method returns correct dictionary."""
        todo = Todo(id=1, title="Test todo", status="pending")
        expected_dict = {
            "id": 1,
            "title": "Test todo",
            "status": "pending"
        }
        self.assertEqual(todo.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()