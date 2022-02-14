import sys

n = int(sys.stdin.readline())

quad = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue, white = 0, 0

def divide(x, y, n):
    global white, blue
    start = quad[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != quad[i][j]:
                for a in range(2):
                    for b in range(2):
                        divide(x + n//2*a, y+n//2*b, n//2)
                return
    if quad[x][y] == 0:
        white += 1
    else:
        blue += 1

divide(0, 0, n)
print(white)
print(blue)

