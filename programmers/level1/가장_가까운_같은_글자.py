def solution(s):
    answer = []
    dict_index = {}
    for index, alpha in enumerate(s):
        if alpha in dict_index:
            answer.append(s[dict_index[alpha] + 1:index + 1].find(alpha) + 1)
            dict_index[alpha] = s[dict_index[alpha] + 1:index + 1].find(alpha)
        else:
            answer.append(-1)
            dict_index[alpha] = s[0:index + 1].find(alpha)
    return answer


def solution2(s):
    answer = []
    dict_index = {}
    for i in range(len(s)):
        if s[i] not in dict_index:
            answer.append(-1)
        else:
            answer.append(i - dict_index[s[i]])
        dict_index[s[i]] = i
    return answer


print(solution2("abcda"))
