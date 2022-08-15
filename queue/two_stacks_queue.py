from stack.stack import Stack


class StackBasedQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def size(self):
        return self.push_stack.size() + self.pop_stack.size()

    def enqueue(self, item):
        self.push_stack.push(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        if self.pop_stack.size() == 0:
            while self.push_stack.size() > 0:
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()
