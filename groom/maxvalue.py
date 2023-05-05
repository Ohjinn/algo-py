max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    a = i
    b = j
    max_value = a * b
    print(a)
    print(b)
    print(max_value)
    if max_value > (a + 1) * (b - 1):
        break

print("알빠노 {}".format(a, b, max_value))
