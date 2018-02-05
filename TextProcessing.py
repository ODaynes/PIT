"""
TextProcessing.py should include all methods used to process
and otherwise manipulate text.

Designed and created by Owen Daynes.

NLTK (natural language tool kit) is a library with a variety of
different natural language processing utilities.
More information can be found here: http://www.nltk.org/
"""

from nltk import word_tokenize
from string import punctuation

"""
Takes a string representation of a document as the parameter
Returns a string representation of a document with all punctuation removed
"""


def remove_punctuation(document):
    return

"""
Takes a string representation of a document as the parameter
Returns a list containing each unique word in the provided document 
"""


def word_bag(document):
    bag = []
    tokens = word_tokenize(document)
    for token in tokens:
        if token not in bag and token not in punctuation:
            bag.append(token)
    return bag


"""
Takes a list representation of a document and either the Snowball or Porter stemmer as the parameters
Returns a list containing each word from the original document stemmed
"""


def stem_document(document, stemmer):
    result = [stemmer.stem(word) for word in document]
    return result


"""
Takes a list of document-lists as the parameter
Returns a list of each unique word representing the entire vocabulary of all input documents
"""


def get_vocabulary(documents):
    result = []
    for document in documents:
        for word in document:
            if word not in result:
                result.append(word)

    return result
