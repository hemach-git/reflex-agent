from dataclasses import dataclass
from typing import Callable


@dataclass
class Tool:
    """
    Represents a capability available to the agent.
    """

    name: str
    description: str
    function: Callable

    def execute(self, *args, **kwargs):
        """Execute the underlying tool function."""
        return self.function(*args, **kwargs)


class ToolRegistry:
    """
    Registry for discovering and executing agent tools.
    """

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(
        self,
        name: str,
        description: str,
        function: Callable,
    ) -> None:
        """Register a tool with the registry."""

        tool = Tool(
            name=name,
            description=description,
            function=function,
        )

        self._tools[name] = tool

    def get_tool(self, name: str) -> Tool:
        """Return a registered tool by name."""

        if name not in self._tools:
            raise ValueError(f"Tool '{name}' is not registered.")

        return self._tools[name]

    def execute(self, name: str, *args, **kwargs):
        """Execute a registered tool and display a basic execution trace."""

        tool = self.get_tool(name)

        print(f"[TOOL] {tool.name}")
        print(f"[ARGS] {args}")

        result = tool.execute(*args, **kwargs)

        print(f"[RESULT] {result}")

        return result

    def list_tools(self) -> list[str]:
        """Return the names of all registered tools."""

        return list(self._tools.keys())

    def describe_tools(self) -> list[dict]:
        """Return metadata describing available tools."""

        return [
            {
                "name": tool.name,
                "description": tool.description,
            }
            for tool in self._tools.values()
        ]