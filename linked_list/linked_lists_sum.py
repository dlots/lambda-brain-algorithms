from linked_list import LinkedList, Node


def linked_lists_sum(list1, list2):
    if list1.len() != list2.len():
        return None

    resulting_list = LinkedList()
    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        resulting_list.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next
    return resulting_list
