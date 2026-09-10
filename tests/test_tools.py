from reflex_agent.tools.calculator import (
    add,
    subtract,
    multiply,
    divide,
)

def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(10, 5) == 2

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True

from reflex_agent.tools.clock import get_current_time

def test_get_current_time():
    result = get_current_time()

    assert isinstance(result, str)
    assert len(result) == 19

from reflex_agent.tools.registry import ToolRegistry
from reflex_agent.tools.calculator import add, multiply
from reflex_agent.tools.clock import get_current_time

def test_register_and_list_tools():
    registry = ToolRegistry()

    registry.register("add", add)
    registry.register("multiply", multiply)

    tools = registry.list_tools()

    assert "add" in tools
    assert "multiply" in tools

def test_execute_tool():
    registry = ToolRegistry()

    registry.register("add", add)

    result = registry.execute("add", 10, 20)

    assert result == 30

def test_execute_current_time_tool():
    registry = ToolRegistry()

    registry.register("get_current_time", get_current_time)

    result = registry.execute("get_current_time")

    assert isinstance(result, str)

def test_unknown_tool():
    registry = ToolRegistry()

    try:
        registry.execute("unknown_tool")
        assert False
    except ValueError as error:
        assert "not registered" in str(error)

## V0.2.0 Updates to configure Tools Abstraction

def test_tool_metadata():
    registry = ToolRegistry()

    registry.register(
        "add",
        "Add two numbers.",
        add,
    )

    tool = registry.get_tool("add")

    assert tool.name == "add"
    assert tool.description == "Add two numbers."

def test_describe_tools():
    registry = ToolRegistry()

    registry.register(
        "add",
        "Add two numbers.",
        add,
    )

    registry.register(
        "multiply",
        "Multiply two numbers.",
        multiply,
    )

    tools = registry.describe_tools()

    assert {
        "name": "add",
        "description": "Add two numbers.",
    } in tools

    assert {
        "name": "multiply",
        "description": "Multiply two numbers.",
    } in tools