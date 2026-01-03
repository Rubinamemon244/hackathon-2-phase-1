# Quickstart Guide: Console Todo App

## Prerequisites
- Python 3.13 or higher
- No external dependencies required

## Setup
1. Clone or create the project directory
2. Ensure Python 3.13+ is installed and accessible
3. No installation required - the application runs directly

## Running the Application
```bash
cd src
python main.py
```

## Basic Usage
Once the application starts, you will see a menu with the following options:
1. Add a new todo
2. View all todos
3. Update a todo
4. Delete a todo
5. Mark a todo as complete
6. Exit

### Available Commands
- **Add**: Enter description when prompted
- **View**: Displays all todos with their status and IDs
- **Update**: Enter ID and new description
- **Delete**: Enter ID of the todo to remove
- **Mark Complete**: Enter ID of the todo to mark as completed

## Example Workflow
1. Start the application: `python main.py`
2. Choose option 1 to add a todo: "Buy groceries"
3. Choose option 2 to view your list
4. Choose option 5 to mark the todo as complete
5. Choose option 2 again to see the updated status
6. Choose option 6 to exit

## Error Handling
The application provides clear error messages for:
- Invalid menu selections
- Non-existent todo IDs
- Empty or invalid input
- Other input errors