def solution(my_string):
    answer = ''
    dictionary = {}
    for word in my_string:
        if dictionary.get(word):
            continue
        else:
            dictionary[word] = True
            answer += word

    return answer


print(solution("people"))