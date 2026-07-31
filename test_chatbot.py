import unittest
from chatbot import get_response, sanitize_input, KNOWLEDGE_BASE


class TestChatbot(unittest.TestCase):

    def test_sanitize_lowercases_and_strips(self):
        self.assertEqual(sanitize_input("  Hello  "), "hello")

    def test_known_intent_returns_correct_response(self):
        self.assertEqual(get_response("hello", KNOWLEDGE_BASE), KNOWLEDGE_BASE["hello"])

    def test_unknown_intent_returns_fallback(self):
        result = get_response("asdkjfh", KNOWLEDGE_BASE)
        self.assertIn("do not understand", result)

    def test_empty_input_handled(self):
        result = get_response("", KNOWLEDGE_BASE)
        self.assertIn("help", result.lower())


if __name__ == "__main__":
    unittest.main()