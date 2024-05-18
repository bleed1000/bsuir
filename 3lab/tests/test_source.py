import unittest
from sources import truth_table, count_entries, find_vars

class TestFunctions(unittest.TestCase):

    def test_truth_table(self):
        self.assertEqual(truth_table(1), [(False,), (True,)])
        self.assertEqual(truth_table(2), [(False, False), (False, True), (True, False), (True, True)])
        self.assertEqual(truth_table(3), [
            (False, False, False), (False, False, True), (False, True, False), (False, True, True),
            (True, False, False), (True, False, True), (True, True, False), (True, True, True)
        ])

    def test_count_entries(self):
        constituents = [
            ['   ✦    ', '   ✦    ', '     '],
            ['     ', '   ✦    ', '   ✦    '],
            ['   ✦    ', '     ', '     ']
        ]
        expected_output = {0: 2, 1: 2, 2: 1}
        self.assertEqual(count_entries(constituents), expected_output)
        
        constituents = [
            ['     ', '     ', '     '],
            ['   ✦    ', '   ✦    ', '   ✦    '],
            ['     ', '     ', '     ']
        ]
        expected_output = {0: 0, 1: 3, 2: 0}
        self.assertEqual(count_entries(constituents), expected_output)
        
        constituents = [
            ['   ✦    '],
            ['   ✦    '],
            ['   ✦    ']
        ]
        expected_output = {0: 1, 1: 1, 2: 1}
        self.assertEqual(count_entries(constituents), expected_output)

    def test_find_vars(self):
        self.assertEqual(find_vars('a & b'), ['a', 'b'])
        self.assertEqual(find_vars('!a | b & c'), ['a', 'b', 'c'])
        self.assertEqual(find_vars('x & y & z'), ['x', 'y', 'z'])
        self.assertEqual(find_vars(''), [])
        self.assertEqual(find_vars('a & a'), ['a'])

if __name__ == '__main__':
    unittest.main()
