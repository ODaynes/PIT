"""
TextProcessing.py should include all methods used to process
and otherwise manipulate text.

Designed and created by Owen Daynes.

NLTK (natural language tool kit) is a library with a variety of
different natural language processing utilities.
More information can be found here: http://www.nltk.org/
"""

from nltk.tag import pos_tag
from nltk import word_tokenize, ne_chunk
from string import punctuation
from math import log

"""
Takes a string representation of a document as the parameter
Returns a string representation of a document with all punctuation removed
"""


def remove_punctuation(document):
    return document.translate(str.maketrans("", "", punctuation))


"""
Takes a string representation of a document as the parameter
Returns a list containing each unique word in the provided document 
"""


def word_bag(document):
    bag = []
    tokens = word_tokenize(document)
    for token in tokens:
        if token.lower() not in bag and token.lower() not in punctuation:
            bag.append(token.lower())
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


"""
Takes a term and a list of tokenised documents as the parameters
Returns the inverse document frequency of the term
"""


def calculate_idf(term, documents):
    documents_containing_term = 0
    for document in documents:
        if term.lower() in document:
            documents_containing_term += 1

    if documents_containing_term > 0:
        return 1.0 + log(float(len(documents)) / documents_containing_term)
    else:
        return 1.0


"""
Takes a FileContainer object as a parameter
Uses term frequencies and other text processing functions 
to create vector representing document
"""


def create_document_vector(container_obj):
    vector = []

    for term, frequency in container_obj.term_frequencies.items():
        tf_idf = frequency * container_obj.inverse_document_frequencies[term]
        vector.append(tf_idf)

    return vector


"""
Takes two container objects as parameters
Creates and returns two dense vectors containing 
tf-idfs for all shared terms.
"""


def create_dense_vectors(container_x, container_y):
    shared_vocabulary = list(set(container_x.normalised).union(set(container_y.normalised)))
    new_x, new_y = list(), list()

    for term in shared_vocabulary:
        new_x.append(container_x.term_frequencies[term] * container_x.inverse_document_frequencies[term])
        new_y.append(container_y.term_frequencies[term] * container_y.inverse_document_frequencies[term])

    return new_x, new_y


"""
Takes raw text string as parameter
Returns list of entities found within text
"""


def get_named_entities(document_text):
    tagged_tokens = pos_tag(word_tokenize(document_text))
    tree = ne_chunk(tagged_tokens, binary=True)

    entities = list()

    for node in tree.subtrees():
        if node.label() == "NE":
            words, _ = zip(*node)
            entities.append(" ".join(words))

    return entities
