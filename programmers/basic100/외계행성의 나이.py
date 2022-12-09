from string import ascii_lowercase


def solution(age):
    answer = ''
    alphabet = list(ascii_lowercase)
    while age / 10 > 0:
        answer = alphabet[age % 10] + answer
        age //= 10

    return answer


print(solution(100))
