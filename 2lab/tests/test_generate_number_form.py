import unittest
from generate_numeric_form import generate_number_form

class TestGenerateNumberForm(unittest.TestCase):
    def test_generate_number_form(self):
        truth_table = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        sknf_num_form, sdnf_num_form = generate_number_form(truth_table)
        self.assertEqual(sknf_num_form, [1, 2])
        self.assertEqual(sdnf_num_form, [0, 3])

    def test_generate_number_form_empty(self):
        truth_table = []
        sknf_num_form, sdnf_num_form = generate_number_form(truth_table)
        self.assertEqual(sknf_num_form, [])
        self.assertEqual(sdnf_num_form, [])

if __name__ == '__main__':
    unittest.main()
