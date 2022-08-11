class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.length += 1

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
        node = self.head
        while node is not None:
            if node.value != val:
                node = node.next
                continue
            self.length -= 1
            if node is self.tail and node is self.head:
                self.tail = None
                self.head = None
            elif node is self.tail:
                self.tail = node.prev
                node.prev.next = node.next
            elif node is self.head:
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next
            if not all:
                return

    def clean(self):
        self.length = 0
        self.head = None
        self.tail = None

    def len(self):
        return self.length

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.add_in_head(newNode)
            return
        elif afterNode is None and self.head is not None:
            self.add_in_tail(newNode)
            return
        self.length += 1
        newNode.next = afterNode.next
        if newNode.next is not None:
            newNode.next.prev = newNode
        newNode.prev = afterNode
        afterNode.next = newNode
        if afterNode is self.tail:
            self.tail = newNode

    def add_in_head(self, newNode):
        self.length += 1
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

