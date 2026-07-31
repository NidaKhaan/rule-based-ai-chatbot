"""
Rule-Based AI Chatbot
A deterministic chatbot using dictionary-based intent matching.
Author: Nida Sheraz
"""

KNOWLEDGE_BASE = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "hey": "Hey! Good to see you.",
    "how are you": "I'm just code, but I'm running smoothly! And you?",
    "what is your name": "I'm a rule-based chatbot, Project 1 at DecodeLabs.",
    "who made you": "I was built by Nida Sheraz as part of an AI engineering track.",
    "what can you do": "Right now, I respond to a fixed set of rules. No learning, no guessing — pure logic.",
    "help": "Try: hello, how are you, what is your name, what can you do, or bye.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
    "bye": "Goodbye! Have a great day.",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}


def sanitize_input(raw_input: str) -> str:
    """Normalize input: lowercase, strip leading/trailing whitespace."""
    return raw_input.lower().strip()


def get_response(user_input: str, knowledge_base: dict) -> str:
    """Return matched response, or a fallback if the intent is unknown."""
    if not user_input:
        return "You didn't say anything — try 'help' to see what I can do."
    return knowledge_base.get(user_input, "I do not understand. Type 'help' to see what I can respond to.")


def run_chat():
    """Main conversation loop. Runs until an exit command or interrupt."""
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        try:
            raw_input_text = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session interrupted. Goodbye!")
            break

        clean_input = sanitize_input(raw_input_text)

        if clean_input in EXIT_COMMANDS:
            print("Chatbot:", KNOWLEDGE_BASE.get("bye", "Goodbye!"))
            break

        reply = get_response(clean_input, KNOWLEDGE_BASE)
        print("Chatbot:", reply)


if __name__ == "__main__":
    run_chat()