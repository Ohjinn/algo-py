def solution(n):
    answer = []
    for i in range(2, n + 1):
        count = 0
        while n % i == 0:
            n /= i
            if count == 0:
                answer.append(i)
                count += 1
    return answer

print(solution(12))