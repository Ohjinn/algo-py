import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
x_traverse = [0, 0, 1, -1]
y_traverse = [1, -1, 0, 0]


def dijkstra(i, count, cave, djk):
    queue = []
    heapq.heappush(queue, (cave[0][0], 0, 0))
    djk[0][0] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == size - 1 and y == size - 1:
            print(f'Problem {count}: {djk[x][y]}')
            break

        for i in range(4):
            new_x = x + x_traverse[i]
            new_y = y + y_traverse[i]

            if 0 <= new_x < size and 0 <= new_y < size:
                new_cost = cost + cave[new_x][new_y]

                if new_cost < djk[new_x][new_y]:
                    djk[new_x][new_y] = new_cost
                    heapq.heappush(queue, (new_cost, new_x, new_y))


count = 1
size = int(input())
while size != 0:
    cave = [list(map(int, input().split())) for _ in range(size)]
    djk = [[INF] * size for _ in range(size)]

    dijkstra(size, count, cave, djk)

    size = int(input())
    count += 1


