sugar = int(input())
answer = 0

max5 = sugar // 5
ck = False
for i in range(max5, 0, -1):
    if ((sugar - (5 * i)) % 3) == 0:
        ck = True
        break

if ck:
    k5left = sugar - (5 * i)
    k3 = k5left / 3
    print(int(i + k3))
else:
    if sugar % 3 == 0:
        print(int(sugar / 3))
    else:
        print(-1)
