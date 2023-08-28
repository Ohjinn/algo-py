def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + format(number, 'b'))
        zero_location = ''.join(bin_number).rfind('0')
        bin_number[zero_location] = '1'

        if number % 2 == 1:
            bin_number[zero_location + 1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer