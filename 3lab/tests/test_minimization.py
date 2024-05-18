import unittest
from minimization import Minimization, MinimizationDNF  # Импортируем классы из вашего файла

# Mocking the find_vars and count_entries for testing purposes
# def mock_find_vars(term):
#     return set(filter(str.isalpha, term))

# def mock_count_entries(constituents):
#     return [sum(1 for cell in row if cell.strip() == '✦') for row in constituents]

# # Patching the original functions with mocks
# Minimization.find_vars = staticmethod(mock_find_vars)
# Minimization.count_entries = staticmethod(mock_count_entries)
# MinimizationDNF.find_vars = staticmethod(mock_find_vars)
# MinimizationDNF.count_entries = staticmethod(mock_count_entries)

class TestMinimization(unittest.TestCase):
    
    def set_up(self):
        def mock_find_vars(term):
            return set(filter(str.isalpha, term))

        def mock_count_entries(constituents):
            return [sum(1 for cell in row if cell.strip() == '✦') for row in constituents]
        Minimization.find_vars = staticmethod(mock_find_vars)
        Minimization.count_entries = staticmethod(mock_count_entries)
        MinimizationDNF.find_vars = staticmethod(mock_find_vars)
        MinimizationDNF.count_entries = staticmethod(mock_count_entries)

    def test_minimize_sknf_simple(self):
        sknf = "(a|b)&(!a|b)&(a|!b)"
        expected = "(a)&(b)"
        result = Minimization.minimize_sknf(sknf)
        self.assertEqual(result, expected)

    def test_minimize_sknf_complex(self):
        sknf = "(a|b|c)&(!a|b|c)&(a|!b|c)&(a|b|!c)&(!a|!b|c)"
        expected = "(c)&(a|b)"
        result = Minimization.minimize_sknf(sknf)
        self.assertEqual(result, expected)

class TestMinimizationDNF(unittest.TestCase):

    def test_minimize_dnf_simple(self):
        dnf = "(a&b)|(!a&b)|(a&!b)"
        expected = "(a)|(b)"
        result = MinimizationDNF.minimize_dnf(dnf)
        self.assertEqual(result, expected)

    def test_minimize_dnf_complex(self):
        dnf = "(a&b&c)|(!a&b&c)|(a&!b&c)|(a&b&!c)|(!a&!b&c)"
        expected = "(c)|(a&b)"
        result = MinimizationDNF.minimize_dnf(dnf)
        self.assertEqual(result, expected)
