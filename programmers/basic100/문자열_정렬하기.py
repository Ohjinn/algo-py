import re


def solution(my_string):
    return sorted(map(int, re.sub("\D", '', my_string)))


print(solution("hi12392"))
