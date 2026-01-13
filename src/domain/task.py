"""Task entity for the Todo application.

This module defines the Task dataclass representing a single todo item.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique numeric identifier (positive integer, auto-incremented)
        description: Text describing what needs to be done (non-empty string)
        is_complete: Completion status (True=complete, False=incomplete)
    """
    id: int
    description: str
    is_complete: bool = False
