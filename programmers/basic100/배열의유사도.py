def solution(s1, s2):
    answer = 0
    dictionary = {string: True for string in s1}
    for i in s2:
        if dictionary.get(i):
            answer += 1
    return answer


def solution2(s1, s2):
    return len(set(s1) & set(s2))


print(solution2(["a", "b", "c"], ["com", "b", "d", "p", "c"]))