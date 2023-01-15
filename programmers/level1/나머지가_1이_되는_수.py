def solution(n):
    for i in range(1, (n // 2) + 1):
        if n % i == 1:
            return i

    return n - 1

print(solution(12))
