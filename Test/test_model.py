import unittest
from src.model import analyze_transcript

class TestModel(unittest.TestCase):
    def test_sentiment_analysis(self):
        transcript = "I am very unhappy with the service."
        sentiment, _, outcome, _ = analyze_transcript(transcript)
        self.assertEqual(sentiment, "Negative")

    def test_call_outcome(self):
        transcript = "Thanks, my issue is now resolved."
        _, _, outcome, _ = analyze_transcript(transcript)
        self.assertEqual(outcome, "Issue Resolved")

if __name__ == '__main__':
    unittest.main()

