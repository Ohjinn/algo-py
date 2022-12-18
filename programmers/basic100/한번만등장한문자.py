def solution(s):
    answer = ''
    alphabet_dict = {}
    for char in s:
        if char in alphabet_dict:
            alphabet_dict[char] += 1
        else:
            alphabet_dict[char] = 0

    for key, value in alphabet_dict.items():
        if value == 0:
            answer += key

    return ''.join(sorted(answer))


def solution2(s):
    answer = ''
    for c in "abcdefghijklmnopqrstuvwxyz":
        if s.count(c) == 1:
            answer += c
    return answer

print(solution("abcabcadc"))