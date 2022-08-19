import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.size = 21
        self.step = 3
        super(TestHashTable, self).__init__(*args, **kwargs)

    def test_hash_function(self):
        table = HashTable(self.size, self.step)
        data = {
            "abc": 0,
            "cba": 0,
            "abd": 1,
            "bda": 1,
            "abe": 2,
            "eab": 2,
            "gwghnwegioghweig": 12,
            "gwghnwegioghw": 18
        }
        for string in data:
            self.assertEqual(table.hash_fun(string), data[string])

    def test_seek_slot(self):
        table = HashTable(self.size, self.step)
        strings = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc',
                   'abc', 'abc', 'abc', 'abc', ]
        for i, string in enumerate(strings):
            slot = table.seek_slot(string)
            if i < 9:
                self.assertIsNotNone(slot)
            else:
                self.assertIsNone(slot)
            table.put(string)

    def test_put(self):
        table = HashTable(self.size, self.step)
        strings = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe', 'abc', 'abc', 'abc', 'abc', 'abc', 'abc',
                   'abc', 'abc', 'abc', 'abc', ]
        for i, string in enumerate(strings):
            slot = table.put(string)
            length = len([value for value in table.slots if value is not None])
            if i < 9:
                self.assertIsNotNone(slot)
                self.assertEqual(length, i + 1)
            else:
                self.assertIsNone(slot)
                self.assertEqual(length, 9)

    def test_find(self):
        table = HashTable(self.size, self.step)
        strings = ['abc', 'afqewf', 'adsggqw', 'wghweghehw', 'qwgqewgqgqe']
        missing_strings = ["12412", "231363", "351215", "2312425"]
        for string in strings:
            table.put(string)
        for string in strings:
            self.assertIsNotNone(table.find(string))
        for string in missing_strings:
            self.assertIsNone(table.find(string))


if __name__ == '__main__':
    unittest.main()


