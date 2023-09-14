import re

s = input()
while s != '#':
    findall = re.findall(r'[aeiouAEIOU]', s)
    print(len(findall))
    s = input()
