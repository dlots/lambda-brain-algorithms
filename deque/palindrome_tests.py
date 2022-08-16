import unittest
from palindrome import check_palindrome


class TestPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        data = {
            "redivider": True,
            "deified": True,
            "civic": True,
            "radar": True,
            "python": False,
            "console": False,
            "qiopfghqujikfgbegbf": False
        }
        for string in data:
            self.assertEqual(check_palindrome(string), data[string])


if __name__ == '__main__':
    unittest.main()
