"""
Todo model representing a single todo item.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, title, and status.

    Attributes:
        id: Unique identifier for the todo
        title: Description of the task
        status: Status of the todo ('pending' or 'completed')
    """
    id: int
    title: str
    status: str = "pending"  # Default status is 'pending'

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Todo title cannot be empty or whitespace-only")
        if self.status not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")

    def complete(self):
        """Mark the todo as completed."""
        self.status = "completed"

    def to_dict(self) -> dict:
        """Convert the todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }