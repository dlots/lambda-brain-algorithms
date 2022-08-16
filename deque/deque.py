class BaseNode:
    def __init__(self):
        self.prev = None
        self.next = None


class DummyNode(BaseNode):
    pass


class Node(BaseNode):
    def __init__(self, v):
        super().__init__()
        self.value = v


class DoublyLinkedList:
    def __init__(self):
        # Create dummy nodes and make them private to hide them from user
        self.__head = DummyNode()
        self.__tail = DummyNode()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__length = 0

    def __len__(self):
        return self.__length

    def get_head(self):
        return self.__head.next

    def get_tail(self):
        return self.__tail.prev

    def add_in_head(self, newNode):
        self.__length += 1
        newNode.next = self.__head.next
        newNode.next.prev = newNode
        newNode.prev = self.__head
        newNode.prev.next = newNode

    def add_in_tail(self, newNode):
        self.__length += 1
        self.__tail.prev.next = newNode
        newNode.prev = self.__tail.prev
        self.__tail.prev = newNode
        newNode.next = self.__tail

    def delete_start_with_head(self, val, all=False):
        node = self.__head.next
        while node is not self.__tail:
            if node.value != val:
                node = node.next
                continue
            self.__length -= 1
            node.prev.next = node.next
            node.next.prev = node.prev
            if not all:
                return
            node = node.next

    def delete_start_with_tail(self, val, all=False):
        node = self.__tail.prev
        while node is not self.__head:
            if node.value != val:
                node = node.prev
                continue
            self.__length -= 1
            node.prev.next = node.next
            node.next.prev = node.prev
            if not all:
                return
            node = node.prev


class Deque:
    def __init__(self):
        self.deque = DoublyLinkedList()

    def addFront(self, item):
        self.deque.add_in_head(Node(item))

    def addTail(self, item):
        self.deque.add_in_tail(Node(item))

    def removeFront(self):
        if self.size() == 0:
            return None
        top = self.deque.get_head().value
        self.deque.delete_start_with_head(top)
        return top

    def removeTail(self):
        if self.size() == 0:
            return None
        bottom = self.deque.get_tail().value
        self.deque.delete_start_with_tail(bottom)
        return bottom

    def size(self):
        return len(self.deque)
