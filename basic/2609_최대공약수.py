import math

num1, num2 = map(int, input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))

# 유클리드 호제법, a를 b로 나눈 나머지와 b의 최대공약수는 a와 b의 최대공약수와 같다.
# math에 최대, 최소공약수가 구현되어 있지만 직접 코딩한다면

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)