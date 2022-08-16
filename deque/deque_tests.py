import unittest
from deque import Deque


class TestDeque(unittest.TestCase):
    def test_addFront(self):
        deque = Deque()
        for i in range(1, 101):
            deque.addFront(i)
            self.assertEqual(deque.size(), i)
            self.assertEqual(deque.removeFront(), i)
            deque.addFront(i)
            self.assertEqual(deque.removeTail(), 1)
            deque.addTail(1)

    def test_addTail(self):
        deque = Deque()
        for i in range(1, 101):
            deque.addTail(i)
            self.assertEqual(deque.size(), i)
            self.assertEqual(deque.removeTail(), i)
            deque.addTail(i)
            self.assertEqual(deque.removeFront(), 1)
            deque.addFront(1)

    def test_removeFront(self):
        deque = Deque()
        for i in range(1, 101):
            deque.addTail(i)
        for i in range(1, 101):
            self.assertEqual(deque.removeFront(), i)
            self.assertEqual(deque.size(), 100 - i)

    def test_removeTail(self):
        deque = Deque()
        for i in range(1, 101):
            deque.addFront(i)
        for i in range(1, 101):
            self.assertEqual(deque.removeTail(), i)
            self.assertEqual(deque.size(), 100 - i)


if __name__ == '__main__':
    unittest.main()
