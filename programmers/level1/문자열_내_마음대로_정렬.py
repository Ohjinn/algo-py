# 중복해결 불가능
def solution(strings, n):
    strings_nth = [i[n] for i in strings]
    string_dict = dict(zip(strings_nth, strings))
    sorted_string = sorted(string_dict.items(), key=lambda key: (key[0], key[1]))
    return [i[1] for i in sorted_string]


def solution_2(strings, n):
    answer = []
    strings_nth = [i[n] for i in strings]
    string_dict = dict(zip(strings, strings_nth))
    sorted_string = sorted(string_dict.items(), key=lambda key: (key[1], key[0]))
    for string in sorted_string:
        num_of_string = strings.count(string[0])
        if num_of_string != 0:
            for i in range(num_of_string):
                answer.append(string[0])
        else:
            answer.append(string[0])
    return answer

print(solution_2(["abce", "abcd", "cdx"], 2))
