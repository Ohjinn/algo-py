bruteforce = int(input())

cnt = 0
result = 0
while cnt != bruteforce:
    result += 1
    str_result = str(result)
    if '666' in str_result:
        cnt += 1

print(result)

