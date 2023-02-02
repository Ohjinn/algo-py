from itertools import combinations


# 문제 잘못 이해
def solution(t, p):
    answer = 0
    permute = combinations(t, len(p))
    for tuple in list(permute):
        word_sum = ''.join(tuple)
        print(word_sum)
    return answer


def solution2(t, p):
    answer = 0
    p_length = len(p)
    for i in range(0, len(t) - p_length + 1):
        if p >= t[i:i + p_length]:
            answer += 1
    return answer


print(solution2("3141592", "271"))
print(solution2("500220839878", "7"))
