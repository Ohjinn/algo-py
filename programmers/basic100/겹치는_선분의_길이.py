def solution(lines):
    answer = 0
    min_of_line = 101
    max_of_line = -101
    now_checked = 0
    for point in lines:
        if point[0] < min_of_line:
            min_of_line = point[0]
        if point[1] > max_of_line:
            max_of_line = point[1]

    for i in range(min_of_line, max_of_line + 1):
        # 두 개 이상 겹쳐있으면 answer += 1
        if now_checked >= 2:
            answer += 1

        # 겹치는 갯수 측정
        for points in lines:
            if points[0] == i:
                now_checked += 1
            if points[1] == i:
                now_checked -= 1
    return answer

print(solution([[0, 5], [3, 9], [1, 10]]))
