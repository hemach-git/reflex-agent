import pytest

from reflex_agent.context import AgentContext
from reflex_agent.context_resolver import ContextResolver

def test_resolve_previous_result():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
    )

    resolver = ContextResolver(context)

    result = resolver.resolve_reference("that")

    assert result == 55

def test_resolve_without_previous_result():
    context = AgentContext()

    resolver = ContextResolver(context)

    with pytest.raises(ValueError):
        resolver.resolve_reference("that")


def test_unknown_reference():
    context = AgentContext()

    context.update(
        tool_name="add",
        result=55,
        operation="addition",
    )

    resolver = ContextResolver(context)

    with pytest.raises(ValueError):
        resolver.resolve_reference("something")
