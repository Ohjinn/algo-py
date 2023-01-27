def caesar_cipher(char, n):
    if 64 < ord(char) < 91 or 96 < ord(char) < 123:
        target_ascii = ord(char) + n
        if (ord(char) < 91 and target_ascii >= 91) or (ord(char) < 123 and target_ascii >= 123):
            return chr(target_ascii - 26)
        else:
            return chr(target_ascii)
    return char


def solution(s, n):
    answer = ''
    for i in s:
        answer += caesar_cipher(i, n)
    return answer


print(solution("AB", 1))
