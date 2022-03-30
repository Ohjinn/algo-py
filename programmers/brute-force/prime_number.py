import math

global count
count = 0


def solution(numbers):
    answer = 0
    numbers_list = list(map(str, str(numbers)))
    used = [0 for _ in range(len(numbers_list))]
    generate(numbers_list, [], used)
    print(count)
    return answer


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def generate(numbers, chosen, used):
    print(chosen)
    temp = ''
    for i in range(len(chosen)):
        temp += chosen[i]

    if temp != '' and temp != '1' and temp != '0':
        if is_prime(int(temp)) == True:
            print(temp)
            global count
            count += 1

    if len(chosen) == len(numbers):
        return

    for i in range(len(numbers)):
        if not used[i]:
            chosen.append(numbers[i])
            used[i] = 1
            generate(numbers, chosen, used)
            used[i] = 0
            chosen.pop()


solution('011')
