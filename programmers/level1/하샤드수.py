def solution(x):
    add = 0
    for i in str(x):
        add += int(i)
    if x % add == 0:
        return True
    return False

print(solution(10))
