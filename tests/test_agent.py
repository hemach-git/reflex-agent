from reflex_agent.agent import ReflexAgent

## V 0.1.0 tests

def test_greeting():
    agent = ReflexAgent()

    response = agent.respond("hello")

    assert response == "Hello! How can I help you?"

def test_greeting_case_insensitive():
    agent = ReflexAgent()

    response = agent.respond("HELLO")

    assert response == "Hello! How can I help you?"

def test_goodbye():
    agent = ReflexAgent()

    response = agent.respond("goodbye")

    assert response == "Goodbye! Have a great day."

def test_help():
    agent = ReflexAgent()

    response = agent.respond("help")

    assert "greetings" in response

def test_unknown_input():
    agent = ReflexAgent()

    response = agent.respond("What is quantum computing?")

    assert response == "I don't understand that request yet."


## V 0.2.0 tests
def test_multiplication_tool():
    agent = ReflexAgent()

    response = agent.respond("25 * 4")

    assert response == "The answer is 100."

def test_addition_tool():
    agent = ReflexAgent()

    response = agent.respond("25 + 5")

    assert response == "The answer is 30."

def test_subtraction_tool():
    agent = ReflexAgent()

    response = agent.respond("25 - 5")

    assert response == "The answer is 20."

def test_division_tool():
    agent = ReflexAgent()

    response = agent.respond("20 / 4")

    assert response == "The answer is 5."

def test_time_tool():
    agent = ReflexAgent()

    response = agent.respond("What time is it?")

    assert response.startswith("The current time is ")    