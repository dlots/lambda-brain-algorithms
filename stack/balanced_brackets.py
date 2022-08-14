from stack import Stack


def brackets_are_balanced(brackets_string):
    stack = Stack()
    for ch in brackets_string:
        if ch == '(':
            stack.push(ch)
            continue
        top = stack.pop()
        if top is None:
            return False
    if stack.size() > 0:
        return False
    return True
