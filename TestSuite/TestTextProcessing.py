import unittest
import TextProcessing

from nltk.stem import snowball


class TestTextProcessing(unittest.TestCase):

    def test_remove_punctuation(self):
        raw = "Hello, world!"
        expected_processed = "Hello world"
        actual_processed = TextProcessing.remove_punctuation(raw)

        assert expected_processed == actual_processed

    def test_word_bag(self):
        before = "This is is an example text"
        after = TextProcessing.word_bag(before)

        assert len(after) == 5

    def test_stem_document(self):
        before = ["Computer", "Science"]
        after = TextProcessing.stem_document(before, snowball.EnglishStemmer())
        assert after[0] == "comput" and after[1] == "scienc"