def solution(n):
    answer = 0
    front = 0
    sum_of = 0
    for i in range(1, n + 1):
        sum_of += i
        while sum_of > n:
            sum_of -= front
            front += 1
        if sum_of == n:
            answer += 1
    return answer