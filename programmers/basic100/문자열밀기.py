from collections import deque


def solution(A, B):
    dq_a = deque(A)
    dq_b = deque(B)
    for i in A:
        if ''.join(dq_a) == ''.join(dq_b):
            return i + 1
        dq_a.appendleft(dq_a.pop())
    return -1


print(solution("apple", "elppa"))
