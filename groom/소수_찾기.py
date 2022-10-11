def prime_list():
    n = 100000
    list = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if list[i]:
            for j in range(i + i, n + 1, i):
                list[j] = False

    return [i for i in range(2, n + 1) if list[i]]


primes = prime_list()
input()
user_input = input().split()

sum = 0
for i in user_input:
    if int(i) in primes:
        sum += int(i)
print(sum)