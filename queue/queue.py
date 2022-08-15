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

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.length += 1

    def delete(self, val, all=False):
        parent = None
        node = self.head
        while node is not None:
            if node.value != val:
                parent = node
                node = node.next
                continue
            self.length -= 1
            if node is self.tail:
                self.tail = parent
            if node is self.head:
                self.head = node.next
            elif parent is not None:
                parent.next = node.next
            if not all:
                return
            node = node.next


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    # complexity = O(1)
    def enqueue(self, item):
        self.queue.add_in_tail(Node(item))

    # complexity = O(1)
    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            top = self.queue.head.value
            self.queue.delete(top)
            return top

    def size(self):
        return len(self.queue)
