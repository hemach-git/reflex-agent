from pathlib import Path
from reflex_agent.memory import Memory

def test_memory_starts_empty(tmp_path: Path):
    memory_file = tmp_path / "memory.json"

    memory = Memory(str(memory_file))

    assert memory.recall("name") is None


def test_remember_and_recall(tmp_path: Path):
    memory_file = tmp_path / "memory.json"

    memory = Memory(str(memory_file))

    memory.remember("name", "Hema")

    assert memory.recall("name") == "Hema"


def test_memory_persists_across_instances(tmp_path: Path):
    memory_file = tmp_path / "memory.json"

    memory = Memory(str(memory_file))

    memory.remember("name", "Hema")

    # Simulate a new agent process/session.
    new_memory = Memory(str(memory_file))

    assert new_memory.recall("name") == "Hema"


def test_memory_clear(tmp_path: Path):
    memory_file = tmp_path / "memory.json"

    memory = Memory(str(memory_file))

    memory.remember("name", "Hema")
    memory.clear()

    assert memory.recall("name") is None