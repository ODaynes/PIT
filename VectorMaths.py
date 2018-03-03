"""
VectorMaths.py should include all methods used to create and manipulate vectors
during the process of calculating the cosine similarity between documents.

Designed and created by Owen Daynes.

"""

"""
Takes two vectors
Returns dot product of vectors
"""


def dot_product(document1, document2):
    result = 0
    for i in range(0, len(document1)):
        result += document1[i] * document2[i]
    return result
