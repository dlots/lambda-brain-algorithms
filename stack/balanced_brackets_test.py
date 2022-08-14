import unittest
from balanced_brackets import brackets_are_balanced


class BracketsTest(unittest.TestCase):
    def test_brackets_are_balanced_function(self):
        test_data = {
            "())(": False,
            "))((": False,
            "((())": False,
            "(()()())": True,
            "((()(()())))": True,
            "((((((((((((()))((())))))(((())))))(()))))))": True,
            "()()()()()()(((())))(()))))(())(": False
        }
        for string in test_data:
            self.assertEqual(brackets_are_balanced(string), test_data[string])


if __name__ == '__main__':
    unittest.main()
