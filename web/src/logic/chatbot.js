// Rule-Based AI Chatbot — Core Logic
// JavaScript port of the Python chatbot.py logic

export const KNOWLEDGE_BASE = {
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
};

export const EXIT_COMMANDS = new Set(["bye", "exit", "quit"]);

/**
 * Normalize input: lowercase, trim whitespace.
 */
export function sanitizeInput(rawInput) {
  return rawInput.toLowerCase().trim();
}

/**
 * Look up intent in knowledge base, return fallback if not found.
 */
export function getResponse(userInput, knowledgeBase = KNOWLEDGE_BASE) {
  if (!userInput) {
    return "You didn't say anything — try 'help' to see what I can do.";
  }
  return knowledgeBase[userInput] || "I do not understand. Type 'help' to see what I can respond to.";
}

/**
 * Check if input is an exit command.
 */
export function isExitCommand(cleanInput) {
  return EXIT_COMMANDS.has(cleanInput);
}