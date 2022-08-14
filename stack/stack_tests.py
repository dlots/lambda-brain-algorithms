import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(1, 101):
            stack.push(i)
            self.assertEqual(stack.peek(), i)

    def test_pop(self):
        stack = Stack()
        for i in range(1, 101):
            stack.push(i)
        for i in reversed(range(1, 101)):
            top = stack.pop()
            self.assertEqual(top, i)

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        for i in range(1, 101):
            stack.push(i)
            self.assertEqual(stack.size(), i)
        for i in reversed(range(1, 101)):
            stack.pop()
            self.assertEqual(stack.size(), i - 1)

    def test_peek(self):
        stack = Stack()
        stack.push(0)
        for _ in range(100):
            top = stack.peek()
            self.assertEqual(stack.size(), 1)
            self.assertEqual(top, 0)



if __name__ == '__main__':
    unittest.main()
