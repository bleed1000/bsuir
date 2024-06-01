import unittest

from lab import *

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix()

    def test_initial_matrix_creation(self):
        expected_matrix = [
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        ]
        self.assertEqual(self.matrix.matrix, expected_matrix)

    def test_load_element(self):
        self.assertEqual(self.matrix.load_element(0, 0), 1)
        self.assertEqual(self.matrix.load_element(1, 1), 1)
        self.assertEqual(self.matrix.load_element(2, 2), 0)
        self.assertEqual(self.matrix.load_element(3, 3), 1)

    def test_change_element(self):
        self.matrix.change_element(0, 0, 0)
        self.assertEqual(self.matrix.load_element(0, 0), 0)
        self.matrix.change_element(1, 1, 0)
        self.assertEqual(self.matrix.load_element(1, 1), 0)

    def test_word_from_matrix(self):
        self.assertEqual(self.matrix.word_from_matrix(0), '1111100001110000')
        self.assertEqual(self.matrix.word_from_matrix(1), '1100101010110010')
        self.assertEqual(self.matrix.word_from_matrix(15), '0010110101010011')

    def test_adres_row_from_matrix(self):
        self.assertEqual(self.matrix.adres_row_from_matrix(0), '1101110000001000')
        self.assertEqual(self.matrix.adres_row_from_matrix(1), '1111011111100010')

    def test_make_word(self):
        self.matrix.make_word(0, '1111111111111111')
        self.assertEqual(self.matrix.word_from_matrix(0), '1111111111111111')

    def test_locate_string_position(self):
        self.assertEqual(self.matrix.locate_string_position('1010101010101010', True), 1)
        self.assertEqual(self.matrix.locate_string_position('0000000000000000', True), 13)
        self.assertEqual(self.matrix.locate_string_position('1111111111111111', False), 0)

    def test_conjuction(self):
        self.assertEqual(self.matrix.conjuction('1010', '1100'), '1000')
        self.assertEqual(self.matrix.conjuction('1111', '1111'), '1111')

    def test_not_conjuction(self):
        self.assertEqual(self.matrix.not_conjuction('1010', '1100'), '0111')
        self.assertEqual(self.matrix.not_conjuction('1111', '1111'), '0000')

    def test_act(self):
        self.assertEqual(self.matrix.act('1010', '1100'), '1010')

    def test_not_act(self):
        self.assertEqual(self.matrix.not_act('1010', '1100'), '0101')

    def test_aggregate(self):
        self.assertEqual(self.matrix.aggregate('111'), '1111100001101111')

if __name__ == '__main__':
    unittest.main()
