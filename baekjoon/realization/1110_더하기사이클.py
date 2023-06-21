
n = int(input())
m = n
count = 0

while True:
    a = m // 10
    b = m % 10
    c = (a + b) % 10
    m = (b * 10) + c

    count += 1
    if(m == n):
        break

print(count)
