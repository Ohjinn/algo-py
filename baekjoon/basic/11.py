t = int(input())

for i in range(t):
    arr = [input()]
    top = arr.pop()
    a = 0
    end = 0
    for c in range(len(top)):
        if top[c] == '(':
            a += 1
        else:
            a -= 1
            if a < 0:
                end = 1
    if a == 0 and end == 0:
        print("YES")
    else:
        print("NO")
