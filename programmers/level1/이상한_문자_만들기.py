def solution(s):
    answer = ''
    for idx, char in enumerate(s, 1):
        if idx % 2 == 1:
            answer += char.upper()
        else:
            answer += char.lower()
    return answer


print(solution("try hello world"))
