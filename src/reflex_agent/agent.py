class ReflexAgent:
    """
    A simple rule-based reflex agent.

    The agent observes the current user's input,
    evaluates predefined rules/conditions, (matches it against them) 
    and returns an approriate response (performs the corresponding action.)
    """

    def respond(self, user_input: str) -> str:
        """
        Observe the input, match a condition, 
        ans Generate a response based on the user's input.
        """

        message = user_input.lower().strip()

        # Rule 1: Greeting
        if "hello" in message or "hi" in message:
            return "Hello! How can I help you?"

        # Rule 2: Goodbye        
        if "bye" in message or "goodbye" in message:
            return "Goodbye! Have a great day."

        # Rule 3: Help request
        if "help" in message:
            return "I can respond to greetings, help requests, and goodbyes."

        # Default action
        return "I don't understand that request yet."