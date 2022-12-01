import math


def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b

# 더 나눠질 수 있는 분수가 답으로 나오는 문제
def solution(denum1, num1, denum2, num2):
    denum3, num3 = denum1 * num2 + num1 * denum2, num1 * num2
    gcd = math.gcd(num2, num1)
    answer = [denum3 // gcd, num3 // gcd]

    a, b = answer[0], answer[1]

    return answer

# 1, 2, 1, 2 -> 2/2로 해결 불가능
def solution2(denum1, num1, denum2, num2):
    denum3, num3 = denum1 * num2 + num1 * denum2, num1 * num2
    m = 1
    for i in range(1, denum3):
        if denum3 % i == 0 and num3 % i == 0:
            m = i
    ml = gcd(denum3 / m, num3 / m)


    return [(int)(denum3 / ml), (int)(num3 / ml)]

print(solution2(1, 2, 1, 2))


'''
유클리드 호제법
a와 b의 최대공약수는 b와 나머지 r의 최대공약수와 같다

122와 22의 최대 공약수를 구하려면
122를 22로 나눈 나머지 -> 12
22를 12로 나눈 나머지 -> 10
12를 10으로 나눈 나머지 -> 2
10은 2로 나눠지므로 최대공약수는 2
'''