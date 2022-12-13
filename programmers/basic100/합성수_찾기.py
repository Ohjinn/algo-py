def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if is_mixed(i):
            answer += 1

    return answer


def is_mixed(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False


print(solution(10))