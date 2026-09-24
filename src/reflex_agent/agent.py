from reflex_agent.context import AgentContext
from reflex_agent.tools.calculator import (
    add,
    subtract,
    multiply,
    divide,
)
from reflex_agent.tools.clock import get_current_time
from reflex_agent.tools.registry import ToolRegistry
from reflex_agent.context_resolver import ContextResolver

class ReflexAgent:
    """
    A simple tool-using reflex agent.

    The agent observes user input, determines whether
    a registered tool is required, executes the tool,
    and returns the result.
    """

    def __init__(self):
        self.tools = ToolRegistry()
        self.context = AgentContext()
        self.context_resolver = ContextResolver(self.context)

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

        if "that" in message:
            response = self._handle_contextual_operation(message)

            if response is not None:
                return response

        # Current time
        if "time" in message:
            result = self.tools.execute("get_current_time")

            self.context.update(
                tool_name="get_current_time",
                result=result,
                operation="current_time",
                user_input=user_input,
                arguments=(),
                )

            return f"The current time is {result}."

        # Teach the Agent to resolve "that"
        if "multiply that by" in message:
            parts = message.split("multiply that by")

            if len(parts) == 2:
                try:
                    b = float(parts[1].strip())

                    if self.context.last_result is None:
                        return "I don't have a previous result to use."

                    a = self.context.last_result

                    result = self.tools.execute("multiply", a, b)

                    self.context.update(
                        tool_name="multiply",
                        result=result,
                        operation="multiplication",
                        user_input=user_input,
                        arguments=(a, b),
                        )

                    return f"The answer is {result:g}."

                except ValueError:
                    return "I couldn't understand the number."

        # Multiplication
        if "*" in message:
            parts = message.split("*")

            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())

                    result = self.tools.execute("multiply", a, b)

                    self.context.update(
                        tool_name="multiply",
                        result=result,
                        operation="multiplication",
                        user_input=user_input,
                        arguments=(a, b),
                        )
                    
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

                    self.context.update(
                        tool_name="add",
                        result=result,
                        operation="addition",
                        user_input=user_input,
                        arguments=(a, b),
                        )

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

                    self.context.update(
                        tool_name="subtract",
                        result=result,
                        operation="subtraction",
                        user_input=user_input,
                        arguments=(a, b),
                        )

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

                    self.context.update(
                        tool_name="divide",
                        result=result,
                        operation="division",
                        user_input=user_input,
                        arguments=(a, b),
                        )

                    return f"The answer is {result:g}."

                except ValueError as error:
                    return str(error)

        # Default
        return "I don't understand that request yet."

    def get_context(self) -> dict:
        """
        Return the current agent context.
        """

        return {
            "last_tool": self.context.last_tool,
            "last_result": self.context.last_result,
            "last_operation": self.context.last_operation,
            "history": self.context.get_history(),
            }

# v0.30 Add a general contextual operation handler  

    def _handle_contextual_operation(self, message: str):
        """
        Handle operations that reference the previous result.
        """

        if self.context.last_result is None:
            return "I don't have a previous result to use."

        previous_result = self.context_resolver.resolve_reference("that")

        # --------------------------------------------------
        # Multiply: "multiply that by 10"
        # --------------------------------------------------

        if "multiply that by" in message:
            value = message.split("multiply that by", 1)[1].strip()
            try:
                number = float(value)
            except ValueError:
                return "I couldn't understand the number."
            result = self.tools.execute(
                "multiply",
                previous_result,
                number,
                )

            self.context.update(
                tool_name="multiply",
                result=result,
                operation="multiplication",
                user_input=message,
                arguments=(previous_result, number),
                )

            return f"The answer is {result:g}."

        # --------------------------------------------------
        # Add: "add 10 to that"
        # --------------------------------------------------

        if message.startswith("add ") and " to that" in message:
            value = message[len("add "):]
            value = value.split(" to that", 1)[0].strip()
            try:
                number = float(value)
            except ValueError:
                return "I couldn't understand the number."

            result = self.tools.execute(
                "add",
                previous_result,
                number,
                )

            self.context.update(
                tool_name="add",
                result=result,
                operation="addition",
                user_input=message,
                arguments=(previous_result, number),
                )

            return f"The answer is {result:g}."

        # --------------------------------------------------
        # Subtract: "subtract 5 from that"
        # --------------------------------------------------
        
        if message.startswith("subtract ") and " from that" in message:
            value = message[len("subtract "):]
            value = value.split(" from that", 1)[0].strip()
            try:
                number = float(value)
            except ValueError:
                return "I couldn't understand the number."

            result = self.tools.execute(
                "subtract",
                previous_result,
                number,
                )

            self.context.update(
                tool_name="subtract",
                result=result,
                operation="subtraction",
                user_input=message,
                arguments=(previous_result, number),
                )

            return f"The answer is {result:g}."

        # --------------------------------------------------
        # Divide: "divide that by 2"
        # --------------------------------------------------
        if "divide that by" in message:
            value = message.split("divide that by", 1)[1].strip()
            try:
                number = float(value)
            except ValueError:
                return "I couldn't understand the number."

            result = self.tools.execute(
                "divide",
                previous_result,
                number,
                )

            self.context.update(
                tool_name="divide",
                result=result,
                operation="division",
                user_input=message,
                arguments=(previous_result, number),
                )
            return f"The answer is {result:g}."
        return None