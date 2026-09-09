from reflex_agent.agent import ReflexAgent

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