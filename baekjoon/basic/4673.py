self_number = [0] * 10000
for i in range(1, 10000):
    if self_number[i] == 0:
        print(i)

    numbers_sum = 0
    temp = i
    while temp > 0:
        numbers_sum += temp % 10
        temp //= 10
    numbers_sum += i
    if numbers_sum < 10000:
        self_number[numbers_sum] = 1

