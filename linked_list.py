class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.length += 1

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found = []
        node = self.head
        while node is not None:
            if node.value == val:
                found.append(node)
            node = node.next
        return found

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

    def clean(self):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

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
