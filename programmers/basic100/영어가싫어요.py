def solution(numbers):
    answer = ''
    word = ''
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for alpha in numbers:
        word += alpha
        for index, number_string in enumerate(number_list):
            if word == number_string:
                answer += str(index)
                word = ''

    return int(answer)


def solution2(numbers):
    number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 0
    for word in number_list:
        numbers = numbers.replace(word, str(i))
        i += 1
    return int(numbers)

print(solution2("onetwothreefourfivesixseveneightnine"))