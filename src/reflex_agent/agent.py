from reflex_agent.tools.calculator import (
    add,
    subtract,
    multiply,
    divide,
)
from reflex_agent.tools.clock import get_current_time
from reflex_agent.tools.registry import ToolRegistry


class ReflexAgent:
    """
    A simple tool-using reflex agent.

    The agent observes user input, determines whether
    a registered tool is required, executes the tool,
    and returns the result.
    """

    def __init__(self):
        self.tools = ToolRegistry()

        self._register_tools()

    def _register_tools(self):
        """Register available tools with the agent."""
        
        self.tools.register(
                "add",
                "Add two numbers.",
                add,
            )
    
        self.tools.register(
                "subtract",
                "Subtract one number from another.",
                subtract,
            )
    
        self.tools.register(
                "multiply",
                "Multiply two numbers.",
                multiply,
            )
    
        self.tools.register(
                "divide",
                "Divide one number by another.",
                divide,
            )
    
        self.tools.register(
                "get_current_time",
                "Return the current local time.",
                get_current_time,
            )

    def respond(self, user_input: str) -> str:
        """
        Observe the input, select a tool when appropriate,
        execute the tool, and return a response.
        """

        message = user_input.lower().strip()

        # Greeting
        if "hello" in message or "hi" in message:
            return "Hello! How can I help you?"

        # Help
        if "help" in message:
            return (
                "I can handle greetings, help requests, "
                "basic calculations, and current time."
            )

        # Goodbye
        if "bye" in message or "goodbye" in message:
            return "Goodbye! Have a great day."

        # Current time
        if "time" in message:
            result = self.tools.execute("get_current_time")

            return f"The current time is {result}."

        # Multiplication
        if "*" in message:
            parts = message.split("*")

            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())

                    result = self.tools.execute("multiply", a, b)

                    return f"The answer is {result:g}."

                except ValueError:
                    return "I couldn't understand those numbers."

        # Addition
        if "+" in message:
            parts = message.split("+")

            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())

                    result = self.tools.execute("add", a, b)

                    return f"The answer is {result:g}."

                except ValueError:
                    return "I couldn't understand those numbers."

        # Subtraction
        if "-" in message:
            parts = message.split("-")

            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())

                    result = self.tools.execute("subtract", a, b)

                    return f"The answer is {result:g}."

                except ValueError:
                    return "I couldn't understand those numbers."

        # Division
        if "/" in message:
            parts = message.split("/")

            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())

                    result = self.tools.execute("divide", a, b)

                    return f"The answer is {result:g}."

                except ValueError as error:
                    return str(error)

        # Default
        return "I don't understand that request yet."