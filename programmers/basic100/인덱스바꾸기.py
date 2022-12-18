def solution(my_string, num1, num2):
    char1 = my_string[num1]
    char2 = my_string[num2]
    my_string = my_string[:num1] + char2 + my_string[num1 + 1:]
    my_string = my_string[:num2] + char1 + my_string[num2 + 1:]

    return my_string


print(solution("hello", 1, 2))