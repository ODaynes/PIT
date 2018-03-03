"""
VectorMaths.py should include all methods used to create and manipulate vectors
during the process of calculating the cosine similarity between documents.

Designed and created by Owen Daynes.

"""

import math

"""
Takes two vectors
Returns dot product of vectors
"""


def dot_product(document1, document2):
    result = 0
    for i in range(0, len(document1)):
        result += document1[i] * document2[i]
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

    d1 = calculate_norm(document1)
    d2 = calculate_norm(document2)

    return dot * (d1 / d2)