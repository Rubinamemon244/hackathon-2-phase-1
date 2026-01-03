"""
Quick validation script to test all functionality of the Todo App.
"""
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService
from src.models.todo import Todo


def test_all_functionality():
    """Test all functionality of the Todo App."""
    print("Testing all functionality of the Todo App...")

    # Initialize the application components
    store = InMemoryStore()
    service = TodoService(store)

    # Test 1: Add todos
    print("\n1. Testing ADD functionality...")
    id1 = service.add_todo("First todo item")
    id2 = service.add_todo("Second todo item")
    print(f"   Added todos with IDs: {id1}, {id2}")

    # Test 2: View todos
    print("\n2. Testing VIEW functionality...")
    todos = service.get_all_todos()
    print(f"   Retrieved {len(todos)} todos:")
    for todo in todos:
        print(f"   - [{todo.id}] {todo.title} ({todo.status})")

    # Test 3: Update a todo
    print("\n3. Testing UPDATE functionality...")
    update_result = service.update_todo(id1, "Updated first todo")
    print(f"   Update result: {update_result}")
    if update_result:
        todos = service.get_all_todos()
        updated_todo = next(t for t in todos if t.id == id1)
        print(f"   Updated todo: [{updated_todo.id}] {updated_todo.title}")

    # Test 4: Mark a todo as complete
    print("\n4. Testing MARK COMPLETE functionality...")
    complete_result = service.mark_complete(id2)
    print(f"   Mark complete result: {complete_result}")
    if complete_result:
        todos = service.get_all_todos()
        completed_todo = next(t for t in todos if t.id == id2)
        print(f"   Completed todo: [{completed_todo.id}] {completed_todo.title} ({completed_todo.status})")

    # Test 5: Delete a todo
    print("\n5. Testing DELETE functionality...")
    delete_result = service.delete_todo(id1)
    print(f"   Delete result: {delete_result}")
    if delete_result:
        todos = service.get_all_todos()
        print(f"   Remaining todos after deletion: {len(todos)}")
        for todo in todos:
            print(f"   - [{todo.id}] {todo.title} ({todo.status})")

    # Test 6: Try operations on non-existing todo
    print("\n6. Testing operations on non-existing todo...")
    non_exist_result = service.update_todo(999, "This won't work")
    print(f"   Update non-existing todo: {non_exist_result}")

    non_exist_result = service.delete_todo(999)
    print(f"   Delete non-existing todo: {non_exist_result}")

    non_exist_result = service.mark_complete(999)
    print(f"   Mark complete non-existing todo: {non_exist_result}")

    print("\n✅ All functionality tests completed successfully!")

    # Final view to confirm state
    print("\n7. Final view of remaining todos...")
    final_todos = service.get_all_todos()
    print(f"   Final count: {len(final_todos)} todos")
    for todo in final_todos:
        print(f"   - [{todo.id}] {todo.title} ({todo.status})")


if __name__ == "__main__":
    test_all_functionality()