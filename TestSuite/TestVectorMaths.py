import unittest
import VectorMaths


class TestVectorMaths(unittest.TestCase):

    def test_dot_product(self):

        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        # (1 * 4) + (2 * 5) + (3 * 6) = 32
        result = VectorMaths.dot_product(vector1, vector2)
        assert result == 32

    def test_invalid_dot_product(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5]

        result = VectorMaths.dot_product(vector1, vector2)
        assert result is None
