answer = 0


def dfs(numbers, depth, sum_of, target):
    global answer
    if depth == len(numbers):
        if sum_of == target:
            answer += 1
    else:
        dfs(numbers, depth + 1, sum_of + numbers[depth], target)
        dfs(numbers, depth + 1, sum_of - numbers[depth], target)


def solution(numbers, target):
    global answer
    depth, sum_of = 0, 0

    dfs(numbers, depth, sum_of, target)
    return answer