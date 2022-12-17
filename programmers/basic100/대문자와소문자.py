def solution(my_string):
    answer = ''
    for character in my_string:
        if ord(character) > 96:
            answer += chr(ord(character) - 32)
        else:
            answer += chr(ord(character) + 32)
    return answer


print(solution("cccCCC"))