arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rectangle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
max_value = [1, 4, 2, 3, 5, 4, 5]
# print(list(filter(lambda x: max_value[x] == max(max_value), range(len(max_value)))))

n = 4

new_90 = [[0] * n for _ in range(n)]
print(new_90)

for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
print(new_90)

new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n - i - 1][n - j - 1] = arr[i][j]
print(new_180)

arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sx, sy = 2, 2
length = 3

for y in range(sy, sy + length):
    for x in range(sx, sx + length):
        ox, oy = x - sx, y - sy
        rx, ry = length - oy - 1, ox
        new_arr[sy + ry][sx + rx] = arr[y][x]

for y in range(sy, sy + length):
    for x in range(sx, sx + length):
        arr[y][x] = new_arr[y][x]
print(arr)

visited = [0] * len(arr)

def permutations(n, new_arr):
    arr = [1, 2, 3, 4]
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

permutations(2, [])