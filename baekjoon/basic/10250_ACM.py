for _ in range(int(input())):
    H, W, N = map(int, input().split())
    a = N % H * 100
    b = N // H + 1
    if a == 0:
        a = H * 100
        b -= 1
    print(a + b)
