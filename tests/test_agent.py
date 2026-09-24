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

## V 0.3.0 tests
def test_context_after_addition():
    agent = ReflexAgent()

    agent.respond("25 + 30")

    context = agent.get_context()

    assert context["last_tool"] == "add"
    assert context["last_result"] == 55
    assert context["last_operation"] == "addition"

def test_context_after_multiplication():
    agent = ReflexAgent()

    agent.respond("10 * 5")

    context = agent.get_context()

    assert context["last_tool"] == "multiply"
    assert context["last_result"] == 50
    assert context["last_operation"] == "multiplication"

def test_contextual_multiplication():
    agent = ReflexAgent()

    agent.respond("25 + 30")

    response = agent.respond("multiply that by 10")

    assert response == "The answer is 550."


def test_contextual_addition():
    agent = ReflexAgent()

    agent.respond("100 / 4")

    response = agent.respond("add 10 to that")

    assert response == "The answer is 35."


def test_contextual_subtraction():
    agent = ReflexAgent()

    agent.respond("100 - 20")

    response = agent.respond("subtract 5 from that")

    assert response == "The answer is 75."


def test_contextual_division():
    agent = ReflexAgent()

    agent.respond("100 + 20")

    response = agent.respond("divide that by 4")

    assert response == "The answer is 30."