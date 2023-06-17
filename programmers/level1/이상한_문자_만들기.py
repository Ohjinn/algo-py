def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        result = ''
        for idx, char in enumerate(i, 1):
            if idx % 2 == 1:
                result += char.upper()
            else:
                result += char.lower()
        answer.append(result)
    return ' '.join(answer)


print(solution("try hello world"))
