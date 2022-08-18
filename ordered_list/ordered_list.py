class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.__length = 0
        self.find_steps = 0

    def compare(self, v1, v2):
        result = -1
        if v1 == v2:
            result = 0
        elif v1 > v2:
            result = 1
        return result

    def add(self, value):
        new_node = Node(value)
        self.__length += 1
        if self.__length == 1:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node is not None:
            comparison_result = self.compare(value, node.value)
            if (self.__ascending and comparison_result == 1) or (not self.__ascending and comparison_result == -1):
                node = node.next
                continue
            if node.prev is not None:
                new_node.prev = node.prev
                new_node.prev.next = new_node
            new_node.next = node
            node.prev = new_node
            if self.head == node:
                self.head = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def find(self, val):
        self.find_steps = 0
        node = self.head
        while node is not None:
            self.find_steps += 1
            comparison_result = self.compare(val, node.value)
            if (self.__ascending and comparison_result == 1) or (not self.__ascending and comparison_result == -1):
                node = node.next
                continue
            elif (self.__ascending and comparison_result == -1) or (not self.__ascending and comparison_result == 1):
                return None
            break
        return node

    def delete(self, val):
        node = self.head
        while node is not None:
            comparison_result = self.compare(val, node.value)
            if (self.__ascending and comparison_result == 1) or (not self.__ascending and comparison_result == -1):
                node = node.next
                continue
            elif (self.__ascending and comparison_result == -1) or (not self.__ascending and comparison_result == 1):
                return
            if node.value != val:
                node = node.next
                continue
            self.__length -= 1
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
            return

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.__length = 0
        self.find_steps = 0

    def len(self):
        return self.__length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super(OrderedStringList, self).compare(v1.strip(), v2.strip())
