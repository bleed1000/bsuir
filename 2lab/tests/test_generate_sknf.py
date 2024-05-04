import unittest
from generate_sknf import generate_sknf

class TestGenerateSKNF(unittest.TestCase):
    def test_generate_sknf_single_clause(self):
        variables = ['A', 'B']
        truth_table = [[0, 0, 0], [0, 1, 1], [1, 0, 0], [1, 1, 0]]
        result = generate_sknf(variables, truth_table)
        self.assertEqual(result, "(A\/B)/\(!A\/B)/\(!A\/!B)")

    def test_generate_sknf_multiple_clauses(self):
        variables = ['A', 'B', 'C']
        truth_table = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 1, 1, 0]]
        result = generate_sknf(variables, truth_table)
        self.assertEqual(result, "(A\/B\/C)/\(A\/!B\/!C)/\(!A\/B\/!C)/\(!A\/!B\/!C)")

