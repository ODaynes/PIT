import unittest
import TextProcessing


class TestTextProcessing(unittest.TestCase):

    def test_remove_punctuation(self):
        raw = "Hello, world!"
        expected_processed = "Hello world"
        actual_processed = TextProcessing.remove_punctuation(raw)

        assert expected_processed == actual_processed