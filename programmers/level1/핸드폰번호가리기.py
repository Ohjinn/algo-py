def solution(phone_number):
    return ''.join(['*' for i in range(len(phone_number) - 4)]) + phone_number[len(phone_number) - 4:len(phone_number)]


def solution2(phone_number):
    return (len(phone_number) - 4) * '*' + phone_number[-4:]


print(solution2("01033334444"))
