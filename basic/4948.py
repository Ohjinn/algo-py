
def prime_list(n):
    prime = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime[i]:
            for j in range(i + i, n, i):
                prime[j] = False

    return [i for i in range(2, n) if prime[i]]

while True:
    n = int(input())

    if n == 0:
        break
    p_list = prime_list(2 * n + 1)
    a_list = [num for num in p_list if num > n]
    print(len(a_list))