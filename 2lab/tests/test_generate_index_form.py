import unittest
from generate_index_form import generate_index_form

class TestGenerateIndexForm(unittest.TestCase):
    def test_single_row(self):
        truth_table = [[0, 1]]
        self.assertEqual(generate_index_form(truth_table), 1)

    def test_multiple_rows(self):
        truth_table = [[0, 1], [1, 0], [1, 1]]
        self.assertEqual(generate_index_form(truth_table), 5) 

    def test_empty_table(self):
        truth_table = []
        self.assertEqual(generate_index_form(truth_table), 0)

    def test_single_column(self):
        truth_table = [[0], [1], [0]]
        self.assertEqual(generate_index_form(truth_table), 2)

