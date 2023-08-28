# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(S):
    deq = deque(S)
    count = 0
    for i in range(len(deq)):
        if deq[0] == deq[-1]:
            count += 1
        deq.rotate(-1)

    return count

print(solution('abab'))
