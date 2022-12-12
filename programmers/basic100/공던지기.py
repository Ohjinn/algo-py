def solution(numbers, k):
    answer = int((k - 1) * 2 % len(numbers))
    return numbers[answer]

print(solution([1, 2, 3, 4], 2))