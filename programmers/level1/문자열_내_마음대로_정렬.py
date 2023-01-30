def solution(strings, n):
    answer = []
    string_dict = dict(zip(strings, strings[n]))
    print(string_dict)
    return answer


print(solution(["sun", "bed", "car"], 1))
