
def decimal_to_ternary(decimal):
    ternary = ''
    while decimal != 1:
        ternary = str(decimal % 3) + ternary
        decimal //= 3
    return '1' + ternary


def ternary_to_decimal(ternary):
    decimal = 0
    mul = 1
    while ternary and int(ternary):
        decimal = decimal + int(ternary[-1]) * mul
        ternary = ternary[0:-1]
        mul *= 3
    return decimal


def solution(n):
    reversed_ternary = decimal_to_ternary(n)[::-1]
    return ternary_to_decimal(reversed_ternary)


def solution(n):
    answer = ''

    while n > 0:
        n, re = divmod(n, 3)
        answer += str(re)
    return int(answer, 3)


print(solution(125))
