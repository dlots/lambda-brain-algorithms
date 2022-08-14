class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def delete(self, val, all=False):
        parent = None
        node = self.head
        while node is not None:
            if node.value == val:
                self.length -= 1
                if node is self.tail:
                    self.tail = parent
                if node is self.head:
                    self.head = node.next
                elif parent is not None:
                    parent.next = node.next
                if not all:
                    return
            else:
                parent = node
            node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
        self.length += 1
        if newNode.next is None:
            self.tail = newNode


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return len(self.stack)

    # complexity - O(1)
    def pop(self):
        if self.size() == 0:
            return None
        else:
            top = self.stack.head.value
            self.stack.delete(top)
            return top

    # complexity - O(1)
    def push(self, value):
        self.stack.insert(None, Node(value))

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.head.value
