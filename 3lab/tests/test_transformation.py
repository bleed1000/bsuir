import unittest
from unittest.mock import patch
from transformation import *

class TestTransformFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=["!ab", "a!b", ""])
    def test_transform(self, mock_input):
        sdnf = [["1", "0"], ["0", "1"]]
        expected_output = [['1', '0'], ['0', '1'], ['0', '1'], ['1', '0']]
        self.assertEqual(transform(sdnf), expected_output)

    def test_transform_sknf(self):
        sdnf = "(a|b)&(!a|c)"
        expected_output = [['0', '0'], ['1', '0']]
        self.assertEqual(transform_sknf(sdnf), expected_output)

    def test_transform_sdnf(self):
        sdnf = "(a&b)|(!a&c)"
        expected_output = [['1', '1', '1'], ['0', '1', '1']]
        self.assertEqual(transform_sdnf(sdnf), expected_output)
        
if __name__ == '__main__':
    unittest.main()
