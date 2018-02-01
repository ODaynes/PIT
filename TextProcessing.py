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


