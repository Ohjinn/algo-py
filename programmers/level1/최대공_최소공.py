def solution(n, m):
    return [gcd(n, m), lcm(n, m)]


def gcd(x, y):

   while(y):
       x, y = y, x % y
   return x


def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

print(solution(3, 12))