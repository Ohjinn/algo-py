def solution(cipher, code):
    answer = ''
    for i, alphabet in enumerate(cipher):
        if int(i % code) + 1 == code:
            answer += alphabet

    return answer

def solution2(cipher, code):
    answer = cipher[code-1::code]
    return answer

print(solution2("dfjardstddetckdaccccdegk", 4))