# Data Model: Console Todo App

## Todo Entity

### Fields
- **id**: Integer (Auto-generated, unique identifier)
- **title**: String (Required, task description)
- **status**: String (Enum: "pending" or "completed", default: "pending")

### Validation Rules
- Title must not be empty or whitespace-only
- ID must be unique within the application session
- Status must be either "pending" or "completed"

### State Transitions
- Default state: "pending"
- Transition to "completed": When user marks task as complete
- No reverse transition (completed tasks remain completed)

## Todo List (Collection)

### Properties
- Collection of Todo entities
- Maintains order of insertion
- Provides lookup by ID

### Constraints
- No duplicate IDs allowed
- All operations happen in-memory only
- Data is lost when application terminates