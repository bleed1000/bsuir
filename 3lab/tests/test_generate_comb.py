from generate_comb import *
import unittest

class TestGenerateCombinations(unittest.TestCase):
    def test_length_0(self):
        result = generate_combinations(0)
        expected = [[]]
        self.assertEqual(result, expected)

    def test_length_1(self):
        result = generate_combinations(1)
        expected = [[0], [1]]
        self.assertEqual(result, expected)

    def test_length_2(self):
        result = generate_combinations(2)
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(result, expected)

    def test_length_3(self):
        result = generate_combinations(3)
        expected = [
            [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
            [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
        ]
        self.assertEqual(result, expected)

    def test_length_4(self):
        result = generate_combinations(4)
        expected = [
            [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
            [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
            [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
            [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]
        ]
        self.assertEqual(result, expected)