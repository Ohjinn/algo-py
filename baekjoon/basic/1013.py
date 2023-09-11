import re

t = int(input())
compiled_regex = re.compile('(100+1+|01)+')

for i in range(t):
    a = input()
    if compiled_regex.fullmatch(a):
        print('YES')
    else:
        print('NO')


