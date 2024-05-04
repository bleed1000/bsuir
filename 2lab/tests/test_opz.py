import unittest
from opz import *

class TestInfixToRPN(unittest.TestCase):
    def test_infix_to_rpn(self):
        expression = "A & B | ( C > D )"
        variables = set()
        result = infix_to_rpn(expression, variables)
        self.assertEqual(result, "A B & C D > |")
        
class TestEvaluateRPN(unittest.TestCase):
    def test_evaluate_rpn(self):
        expression = "A B & C D > |"
        truth_table = [
            [True, True, True, True],
            [True, False, True, False],
            [False, True, False, True],
            [False, False, True, True]
        ]
        result = evaluate_rpn(expression, truth_table)
        self.assertEqual(result, [True, False, True, True])