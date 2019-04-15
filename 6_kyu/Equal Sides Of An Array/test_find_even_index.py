import unittest
from find_even_index import find_even_index


class TextFindEvenIndex(unittest.TestCase):
    def test_find_even_index(self):
        assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
        assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
        assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
        assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
        assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
        assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
        assert find_even_index(range(1, 100)) == -1
        assert find_even_index([0, 0, 0, 0, 0]) == 0
        assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
        assert find_even_index(range(-100, -1)), -1


if __name__ == '__main__':
    unittest.main()
