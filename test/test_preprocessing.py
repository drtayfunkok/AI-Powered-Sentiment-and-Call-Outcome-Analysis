import unittest
from src.preprocessing import extract_customer_responses

class TestPreprocessing(unittest.TestCase):
    def test_extract_customer_responses(self):
        transcript = "Agent: Hello, how can I assist? \nMember: I need help with my claim.\nAgent: Sure!"
        expected_output = "I need help with my claim."
        self.assertEqual(extract_customer_responses(transcript), expected_output)

if __name__ == '__main__':
    unittest.main()
