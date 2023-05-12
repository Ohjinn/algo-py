from collections import deque
# checking_table = [[0] * size_of_map for _ in range(size_of_map)]


def dfs(maps, deepest, size_of_map):
    if maps[size_of_map][size_of_map] != 1 and maps[size_of_map][size_of_map] < deepest:
        deepest = maps[size_of_map][size_of_map]

    return deepest


def bfs(maps, x, y):
    next_queue = deque()
    next_queue.append([x, y])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while next_queue:
        x, y = next_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    next_queue.append([nx, ny])

    return maps[-1][-1] if maps[-1][-1] > 1 else -1


def solution(maps):
    return bfs(maps, 0, 0)


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
