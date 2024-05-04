import unittest
from generate_truth_table import generate_combinations

class TestGenerateCombinations(unittest.TestCase):
    def test_generate_combinations_length_1(self):
        result = generate_combinations(1)
        self.assertEqual(result, [[0], [1]])

    def test_generate_combinations_length_2(self):
        result = generate_combinations(2)
        self.assertEqual(result, [[0, 0], [0, 1], [1, 0], [1, 1]])

    def test_generate_combinations_length_3(self):
        result = generate_combinations(3)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
                                   [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

    def test_generate_combinations_length_0(self):
        result = generate_combinations(0)
        self.assertEqual(result, [[]])