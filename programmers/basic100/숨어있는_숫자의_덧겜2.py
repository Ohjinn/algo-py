import re


def solution(my_string):
    return sum(map(int, re.sub("[a-zA-Z]", " ", my_string).split()))

print(solution("aAb1B2cC34oOp"))