import unittest
from dictionary import NativeDictionary


class TestDictionary(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.size = 5
        super(TestDictionary, self).__init__(*args, **kwargs)

    def assert_size(self, dictionary, expected_size):
        length_keys = len([key for key in dictionary.slots if key is not None])
        length_values = len([value for value in dictionary.values if value is not None])
        self.assertEqual(length_keys, length_values)
        self.assertEqual(length_keys, expected_size)

    def test_put(self):
        dictionary = NativeDictionary(self.size)
        keys = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe']
        for i, key in enumerate(keys):
            dictionary.put(key, 0)
            self.assert_size(dictionary, i + 1)
            self.assertEqual(dictionary.get(key), 0)
        existing_key = 'abc'
        dictionary.put(existing_key, 1)
        self.assert_size(dictionary, 5)
        self.assertEqual(dictionary.get(existing_key), 1)

    def test_is_key(self):
        dictionary = NativeDictionary(self.size)
        keys = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe']
        for i, key in enumerate(keys):
            dictionary.put(key, 0)
            self.assertTrue(dictionary.is_key(key))
        self.assertFalse(dictionary.is_key('123'))

    def test_get(self):
        dictionary = NativeDictionary(self.size)
        keys = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe']
        for i, key in enumerate(keys):
            dictionary.put(key, 0)
            self.assertEqual(dictionary.get(key), 0)
        self.assertIsNone(dictionary.get('123'))


if __name__ == '__main__':
    unittest.main()
