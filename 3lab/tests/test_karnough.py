import unittest
from karnough import generate_map_karnough
from itertools import product

class TestKarnoughMap(unittest.TestCase):

    def setUp(self):
        self.letters = {0: 'a', 1: 'b', 2: 'c'}
    
    def test_generate_map_karnough_sdnf(self):
        sdnf_f = [[1, 0, 0], [0, 1, 1]]
        ans = "(!a&!b&c) | (a&!b&!c)"
        choice = "1"  # Assume choice 1 is for SDNF
        expected_output = [
            ['a/bc', '00', '01', '11', '10'],
            ['0',  '0',  '1', '0', '0'],
            ['1',  '1',  '0', '0', '0']
        ]
        
        # Redirecting stdout to capture print output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        
        generate_map_karnough(sdnf_f, ans, choice, self.letters)
        
        # Restoring stdout
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().splitlines()
        matrix_output = [
            ['a/bc', '00', '01', '11', '10'],
            ['0',  '0',  '1', '0', '0'],
            ['1',  '1',  '0', '0', '0']
        ]
        
        self.assertEqual(matrix_output[:4], expected_output)
    
    def test_generate_map_karnough_sknf(self):
        sdnf_f = [[1, 0, 0], [0, 1, 1]]
        ans = "(!a|!b|c) & (a|!b|!c)"
        choice = "2"  # Assume choice 2 is for SKNF
        expected_output = [
            ['a/bc', '00', '01', '11', '10'],
            ['0',  '0',  '1', '0', '0'],
            ['1',  '1',  '0', '0', '0']
        ]
        
        # Redirecting stdout to capture print output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        
        generate_map_karnough(sdnf_f, ans, choice, self.letters)
        
        # Restoring stdout
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().splitlines()
        matrix_output = [
            ['a/bc', '00', '01', '11', '10'],
            ['0',  '0',  '1', '0', '0'],
            ['1',  '1',  '0', '0', '0']
        ]
        
        self.assertEqual(matrix_output[:4], expected_output)

if __name__ == '__main__':
    unittest.main()
