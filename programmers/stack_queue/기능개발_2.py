
def solution(progresses, speeds):
    from collections import deque
    progresses, speeds = deque(progresses), deque(speeds)

    answer = []
    time = 0
    temp = 0
    while progresses:
        if progresses[0] + (time * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            temp += 1
        else:
            if temp > 0:
                answer.append(temp)
                temp = 0
            time += 1
    answer.append(temp)
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))

