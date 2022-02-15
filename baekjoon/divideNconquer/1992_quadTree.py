import sys

n = int(sys.stdin.readline())

quad = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def divide(x, y, n):
    start = quad[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != quad[i][j]:
                print('(', end='')
                for a in range(2):
                    for b in range(2):
                        divide(x + n//2*a, y+n//2*b, n//2)
                print(')', end='')
                return

    if quad[x][y] == 0:
        print('0', end='')
    else:
        print('1', end='')

divide(0, 0, n)

