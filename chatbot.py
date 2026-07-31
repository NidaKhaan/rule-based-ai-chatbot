"""
Rule-Based AI Chatbot
A deterministic chatbot using dictionary-based intent matching.
Author: Nida Sheraz
"""

def get_response(user_input, knowledge_base):
    """Look up intent in knowledge base, return fallback if not found."""
    return knowledge_base.get(user_input, "I do not understand. Could you rephrase that?")


def sanitize_input(raw_input):
    """Normalize input: lowercase, strip whitespace."""
    return raw_input.lower().strip()


def main():
    knowledge_base = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What's on your mind?",
        "how are you": "I'm just code, but I'm running smoothly! And you?",
        "what is your name": "I'm a rule-based chatbot, built as Project 1 at DecodeLabs.",
        "help": "Try saying: hello, how are you, what is your name, or bye.",
        "bye": "Goodbye! Have a great day.",
    }

    exit_commands = {"bye", "exit", "quit"}

    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize_input(raw_input_text)

        if clean_input in exit_commands:
            print("Chatbot:", knowledge_base.get("bye", "Goodbye!"))
            break

        reply = get_response(clean_input, knowledge_base)
        print("Chatbot:", reply)


if __name__ == "__main__":
    main()