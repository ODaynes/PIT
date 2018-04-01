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

    def test_get_vocabulary(self):
        NUMBER_UNIQUE_TERMS = 6
        documents = [["Computer", "Science"], ["Natural", "Language", "Engineering"], ["Computer", "Science", "Natural", "Language", "Processing"]]
        vocabulary = TextProcessing.get_vocabulary(documents)
        assert len(vocabulary) == NUMBER_UNIQUE_TERMS

    def test_calculate_idf(self):
        term = "computer"
        documents = [["computer", "science"], ["computer", "engineering"], ["electronic", "engineering"]]
        idf = TextProcessing.calculate_idf(term, documents)
        assert idf > 1.0

    def test_create_dense_vectors(self):
        assert True

    def test_get_named_entities(self):
        assert True
