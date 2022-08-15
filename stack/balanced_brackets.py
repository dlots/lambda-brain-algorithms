from stack import Stack


def brackets_are_balanced(brackets_string):
    stack = Stack()
    for ch in brackets_string:
        if ch == '(':
            stack.push(ch)
            continue
        if stack.size() == 0:
            return False
        stack.pop()
    return stack.size() == 0
