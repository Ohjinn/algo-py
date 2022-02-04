num1 = int(input())
num2 = int(input())

mul_sum = 0

for i in range(3):
    temp_num = num2 % 10
    num2 //= 10

    print(temp_num * num1)
    mul_sum += (temp_num * num1 * (10 ** i))


print(mul_sum)
