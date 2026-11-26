from pathlib import Path
import sys

# Support direct execution from a source checkout without installation.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reflex_agent.agent import ReflexAgent

def main():
    agent = ReflexAgent()

    print("================================")
    print("Reflex Agent V0.1.0")
    print("================================")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "quit":
            print("Agent: Goodbye!")
            break

        response = agent.respond(user_input)

        print(f"Agent: {response}")

if __name__ == "__main__":
    main()