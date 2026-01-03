"""
Main entry point for the Todo Application.
"""
from src.store.in_memory_store import InMemoryStore
from src.services.todo_service import TodoService
from src.cli.cli_controller import CLIController


def main():
    """
    Main function to run the Todo Application.
    """
    print("Welcome to the Todo Application!")
    print("Type 'help' for instructions or select an option from the menu.")

    # Initialize the application components
    store = InMemoryStore()
    service = TodoService(store)
    controller = CLIController(service)

    # Main application loop
    while True:
        controller.display_menu()
        try:
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == "1":
                controller.handle_add_todo()
            elif choice == "2":
                controller.handle_view_todos()
            elif choice == "3":
                controller.handle_update_todo()
            elif choice == "4":
                controller.handle_delete_todo()
            elif choice == "5":
                controller.handle_mark_complete()
            elif choice == "6":
                controller.handle_help()
            elif choice == "7":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                controller.handle_invalid_command(choice)
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nEnd of input. Goodbye!")
            break


if __name__ == "__main__":
    main()