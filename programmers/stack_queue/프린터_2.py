from collections import deque


def solution(priorities, location):
    answer = 0
    deq = deque((n, i) for i, n in enumerate(priorities))
    while len(deq):
        temp = deq.popleft()
        if deq and max(deq)[0] > temp[0]:
            deq.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer


print(solution([2, 1, 3, 2], 2))

