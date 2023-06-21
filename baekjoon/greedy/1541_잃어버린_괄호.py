import re

expression = input()
expressions = re.split(r'[+-]', expression)
plus_minus = re.findall(r'[+-]', expression)
result = int(expressions[0])
flag = False

for i, value in enumerate(plus_minus):
    if value == '-':
        flag = True

    if flag is False:
        result += int(expressions[i + 1])
    else:
        result -= int(expressions[i + 1])

print(result)