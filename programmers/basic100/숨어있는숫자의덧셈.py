import re


def solution(my_string):
    return sum(list(map(int, re.sub("\D", '', my_string))))


print(solution("aAb1B2cC34oOp"))
