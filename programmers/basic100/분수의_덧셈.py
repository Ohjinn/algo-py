import math


def solution(denum1, num1, denum2, num2):
    num3, denum3 = denum1 * num2 + num1 * denum2, denum1 * denum2
    print(num3, denum3)
    gcd = math.gcd(max(denum1, denum2), min(denum1, denum2))
    answer = [num3 // gcd, denum3 // gcd]
    return answer


print(solution(1, 2, 3, 4))


'''
유클리드 호제법
a와 b의 최대공약수는 b와 나머지 r의 최대공약수와 같다

122와 22의 최대 공약수를 구하려면
122를 22로 나눈 나머지 -> 12
22를 12로 나눈 나머지 -> 10
12를 10으로 나눈 나머지 -> 2
10은 2로 나눠지므로 최대공약수는 2
'''