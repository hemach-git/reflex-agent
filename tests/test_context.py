from reflex_agent.context import AgentContext

def test_context_initial_state():
    context = AgentContext()

    assert context.last_tool is None
    assert context.last_result is None
    assert context.last_operation is None

def test_context_update():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
    )

    assert context.last_tool == "add"
    assert context.last_result == 55
    assert context.last_operation == "addition"

def test_context_clear():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
    )

    context.clear()

    assert context.last_tool is None
    assert context.last_result is None
    assert context.last_operation is None

def test_context_records_interaction():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
        user_input="25 + 30",
        arguments=(25, 30),
    )

    history = context.get_history()

    assert len(history) == 1

    interaction = history[0]

    assert interaction.user_input == "25 + 30"
    assert interaction.tool_name == "add"
    assert interaction.arguments == (25, 30)
    assert interaction.result == 55
    assert interaction.operation == "addition"


def test_context_records_multiple_interactions():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
        user_input="25 + 30",
        arguments=(25, 30),
    )

    context.update(
        tool_name="multiply",
        result=550,
        operation="multiplication",
        user_input="multiply that by 10",
        arguments=(55, 10),
    )

    history = context.get_history()

    assert len(history) == 2
    assert history[0].result == 55
    assert history[1].result == 550
    assert history[1].tool_name == "multiply"


def test_clear_removes_history():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
    )

    context.clear()

    assert context.get_history() == []
    assert context.last_result is None
