"""
CLI controller for handling user input and displaying output.
"""
from typing import Optional
from src.services.todo_service import TodoService


class CLIController:
    """
    Controller that handles user input, validates commands, and displays results.
    """
    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI controller with a todo service.

        Args:
            todo_service: The service to handle todo operations
        """
        self.todo_service = todo_service

    def display_menu(self):
        """Display the main menu with available options."""
        print("\n" + "="*30)
        print("       TODO APPLICATION")
        print("="*30)
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Update a todo")
        print("4. Delete a todo")
        print("5. Mark a todo as complete")
        print("6. Help")
        print("7. Exit")
        print("="*30)

    def handle_add_todo(self):
        """Handle the add todo command."""
        try:
            title = input("Enter todo description: ").strip()
            if not title:
                print("❌ Error: Todo description cannot be empty.")
                return

            todo_id = self.todo_service.add_todo(title)
            print(f"✅ Todo added successfully with ID: {todo_id}")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error adding todo: {e}")

    def handle_view_todos(self):
        """Handle the view todos command."""
        try:
            todos = self.todo_service.get_all_todos()
            if not todos:
                print("📋 No todos found.")
                return

            print("\n📋 TODO LIST")
            print("-" * 40)
            for todo in todos:
                status_symbol = "✅" if todo.status == "completed" else "⏳"
                print(f"{status_symbol} [{todo.id:2d}] {todo.title}")
            print("-" * 40)
            print(f"Total: {len(todos)} todos")
        except Exception as e:
            print(f"❌ Error viewing todos: {e}")

    def handle_update_todo(self):
        """Handle the update todo command."""
        try:
            todo_id_str = input("Enter todo ID to update: ").strip()
            if not todo_id_str or not todo_id_str.isdigit():
                print("❌ Error: Invalid todo ID. Please enter a number.")
                return

            todo_id = int(todo_id_str)
            new_title = input("Enter new description: ").strip()
            if not new_title:
                print("❌ Error: New description cannot be empty.")
                return

            if self.todo_service.update_todo(todo_id, new_title):
                print(f"✅ Todo {todo_id} updated successfully.")
            else:
                print(f"❌ Error: Todo with ID {todo_id} not found.")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error updating todo: {e}")

    def handle_delete_todo(self):
        """Handle the delete todo command."""
        try:
            todo_id_str = input("Enter todo ID to delete: ").strip()
            if not todo_id_str or not todo_id_str.isdigit():
                print("❌ Error: Invalid todo ID. Please enter a number.")
                return

            todo_id = int(todo_id_str)
            if self.todo_service.delete_todo(todo_id):
                print(f"✅ Todo {todo_id} deleted successfully.")
            else:
                print(f"❌ Error: Todo with ID {todo_id} not found.")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error deleting todo: {e}")

    def handle_mark_complete(self):
        """Handle the mark complete command."""
        try:
            todo_id_str = input("Enter todo ID to mark complete: ").strip()
            if not todo_id_str or not todo_id_str.isdigit():
                print("❌ Error: Invalid todo ID. Please enter a number.")
                return

            todo_id = int(todo_id_str)
            if self.todo_service.mark_complete(todo_id):
                print(f"✅ Todo {todo_id} marked as complete.")
            else:
                print(f"❌ Error: Todo with ID {todo_id} not found.")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error marking complete: {e}")

    def handle_help(self):
        """Display help information."""
        print("\n" + "="*40)
        print("              HELP")
        print("="*40)
        print("1. Add a new todo: Add a new task to your list")
        print("2. View all todos: Display all your tasks with their status")
        print("3. Update a todo: Change the description of an existing task")
        print("4. Delete a todo: Remove a task from your list")
        print("5. Mark a todo as complete: Mark a task as finished")
        print("6. Help: Show this help message")
        print("7. Exit: Close the application")
        print("="*40)

    def handle_invalid_command(self, command: str):
        """Handle invalid commands."""
        print(f"❌ Invalid command: '{command}'. Please enter a valid option (1-7).")

    def validate_todo_id(self, todo_id_str: str) -> Optional[int]:
        """
        Validate a todo ID string.

        Args:
            todo_id_str: The string representation of the todo ID

        Returns:
            The integer ID if valid, None otherwise
        """
        if not todo_id_str or not todo_id_str.isdigit():
            return None
        return int(todo_id_str)