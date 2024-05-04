import unittest
from generate_sdnf import generate_sdnf

class TestGenerateSDNF(unittest.TestCase):
    def test_generate_sdnf_single_clause(self):
        variables = ['A', 'B']
        truth_table = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        result = generate_sdnf(variables, truth_table)
        self.assertEqual(result, "(!A!B\/AB)")

    def test_generate_sdnf_multiple_clauses(self):
        variables = ['A', 'B', 'C']
        truth_table = [[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0]]
        result = generate_sdnf(variables, truth_table)
        self.assertEqual(result, "(!A!BC\/!AB!C\/A!B!C)")

    def test_generate_sdnf_no_clauses(self):
        variables = ['A', 'B']
        truth_table = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
        result = generate_sdnf(variables, truth_table)
        self.assertEqual(result, "()")

if __name__ == '__main__':
    unittest.main()

