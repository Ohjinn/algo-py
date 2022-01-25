import math

A, B, V = map(int, (input().split(' ')))

count = math.ceil((V - B) / (A - B))

print(count)