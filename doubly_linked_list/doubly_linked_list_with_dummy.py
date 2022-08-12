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


class DummyLinkedList:
    def __init__(self):
        # Create dummy nodes and make them private to hide them from user
        self.__head = DummyNode()
        self.__tail = DummyNode()
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

    def find(self, val):
        node = self.__head.next
        while node is not self.__tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found = []
        node = self.__head.next
        while node is not self.__tail:
            if node.value == val:
                found.append(node)
            node = node.next
        return found

    def delete(self, val, all=False):
        node = self.__head.next
        while node is not self.__tail:
            if node.value == val:
                self.__length -= 1
                node.prev.next = node.next
                node.next.prev = node.prev
            if not all:
                return
            node = node.next

    def clean(self):
        self.__length = 0
        self.__head = DummyNode()
        self.__tail = DummyNode()

    def insert(self, afterNode, newNode):
        if afterNode is None and self.__head is None:
            self.add_in_head(newNode)
            return
        elif afterNode is None and self.__head is not None:
            self.add_in_tail(newNode)
            return
        self.__length += 1
        newNode.next = afterNode.next
        newNode.next.prev = newNode
        newNode.prev = afterNode
        afterNode.next = newNode
