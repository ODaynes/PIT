"""
VectorMaths.py should include all methods used to create and manipulate vectors
during the process of calculating the cosine similarity between documents.

Designed and created by Owen Daynes.

"""

import math

from TextProcessing import calculate_idf

"""
Takes two vectors
Returns dot product of vectors
"""


def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return None

    result = 0
    for i in range(0, len(vector1)):
        result += vector1[i] * vector2[i]
    return result


"""
Takes a vector as a parameter
Returns the euclidean norm of the vector
"""


def calculate_norm(vector):

    norm = 0
    for element in vector:
        norm += element**2
    return math.sqrt(norm)


"""
Takes two document vectors
Returns cosine similarity between vectors
"""


def cosine_similarity(document1, document2):
    dot = dot_product(document1, document2)

    d1 = math.sqrt(dot_product(document1, document1))
    d2 = math.sqrt(dot_product(document2, document2))

    denom = d1 * d2

    return dot / denom
