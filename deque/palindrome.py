from deque import Deque


def check_palindrome(string):
    deque = Deque()
    for ch in string:
        deque.addTail(ch)
    while deque.size() > 1:
        if deque.removeTail() != deque.removeFront():
            return False
    return True
