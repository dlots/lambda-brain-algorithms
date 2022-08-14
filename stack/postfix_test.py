import unittest
from postfix import calculate_postfix_expression


class PostfixTest(unittest.TestCase):
    def test_calculate_postfix_expression(self):
        expressions = {
            "1 2 + 3 * =": 9,
            "8 2 + 5 * 9 + =": 59,
            "8 2 + 5 * 9 + 2 / =": 29.5,
            "8 2 + 5 * 9 + 9 - =": 50
        }
        for expression in expressions:
            self.assertEqual(calculate_postfix_expression(expression), expressions[expression])


if __name__ == '__main__':
    unittest.main()
