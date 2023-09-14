import re
from collections import deque
from itertools import permutations


def operate(e, a, b):
    if e == '+':
        return a + b
    if e == '-':
        return a - b
    if e == '*':
        return a * b


def solution(expression):
    result = []
    basic_operations = ['+', '-', '*']

    operations = re.findall(r'[^0-9]+', expression)
    check = re.split("([^0-9])", expression)

    for ops in basic_operations:
        if ops not in operations:
            basic_operations.remove(ops)

    primary = permutations(basic_operations)

    for op_list in primary:
        exp = check
        for op in op_list:
            s = []
            for e in exp:
                if s and s[-1] == op:
                    operation = s.pop()
                    s[-1] = operate(operation, int(s[-1]), int(e))
                else:
                    s.append(e)
            exp = s
        result.append(abs(exp[0]))

    return max(result)