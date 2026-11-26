import json
from pathlib import Path
from typing import Any

class Memory:
    """
    Persistent memory for the agent.

    Memory is stored on disk so it survives
    across agent sessions.
    """

    def __init__(self, file_path: str = "data/memory.json"):
        self.file_path = Path(file_path)
        self.data: dict[str, Any] = {}

        self.load()

    def remember(self, key: str, value: Any) -> None:
        """Store a value in persistent memory."""

        self.data[key] = value
        self.save()

    def recall(self, key: str) -> Any:
        """Retrieve a value from persistent memory."""

        return self.data.get(key)

    def save(self) -> None:
        """Persist memory to disk."""

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                self.data,
                file,
                indent=2,
            )

    def load(self) -> None:
        """Load memory from disk."""

        if not self.file_path.exists():
            self.data = {}
            return

        with self.file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            self.data = json.load(file)

    def clear(self) -> None:
        """Clear all persistent memory."""

        self.data = {}
        self.save()