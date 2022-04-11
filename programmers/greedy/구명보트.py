from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    data = deque(people)
    while data:
        if len(data) == 1:
            answer += 1
            break
        left = data.popleft()
        right = data.pop()
        sum = left + right
        if sum <= limit:
            answer += 1
        elif sum > limit:
            answer += 1
            data.appendleft(left)

    return answer


print(solution([70, 80, 50], 100))

