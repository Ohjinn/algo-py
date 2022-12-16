def solution(my_string):
    sum = 0
    storage = ''
    for num in my_string.split():
        if num == 'Z':
            sum -= int(storage)
        else:
            sum += int(num)
            storage = num

    return sum


print(solution("10 20 30 40"))
