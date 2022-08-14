import string
import operator
from stack import Stack


def calculate_postfix_expression(expression):
    left = Stack()
    right = Stack()
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    for ch in reversed(expression):
        left.push(ch)
    while left.size() > 0:
        token = left.pop()
        if token in string.digits:
            right.push(int(token))
            continue
        elif token in operations:
            second = right.pop()
            first = right.pop()
            right.push(operations[token](first, second))
        elif token == "=":
            return right.pop()
    # if landed here, the expression is ill-formed
    return None
