from dataclasses import dataclass
from typing import Any


@dataclass
class Interaction:
    """Represents one agent interaction."""

    user_input: str
    tool_name: str | None
    arguments: tuple[Any, ...]
    result: Any
    operation: str | None


class AgentContext:
    """
    Stores contextual information for the current interaction.
    """

    def __init__(self):
        self.last_tool = None
        self.last_result = None
        self.last_operation = None

        self.history: list[Interaction] = []

    def update(
        self,
        tool_name: str,
        result: Any,
        operation: str | None = None,
        user_input: str = "",
        arguments: tuple[Any, ...] = (),
    ) -> None:
        """Update current context and record the interaction."""

        self.last_tool = tool_name
        self.last_result = result
        self.last_operation = operation

        interaction = Interaction(
            user_input=user_input,
            tool_name=tool_name,
            arguments=arguments,
            result=result,
            operation=operation,
        )

        self.history.append(interaction)

    def get_history(self) -> list[Interaction]:
        """Return the interaction history."""

        return self.history

    def clear(self) -> None:
        """Clear the current interaction context and history."""

        self.last_tool = None
        self.last_result = None
        self.last_operation = None
        self.history.clear()