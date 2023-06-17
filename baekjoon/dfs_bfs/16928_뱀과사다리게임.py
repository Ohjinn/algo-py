import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([1])
    while queue:
        current_location = queue.popleft()
        if current_location == 100:
            return visited[100]
        for possible_way in (1, 2, 3, 4, 5, 6):
            target_location = current_location + possible_way
            if target_location <= 100 and not visited[target_location]:
                if target_location in ladder_snake.keys():
                    jumped_location = ladder_snake[target_location]
                    if not visited[jumped_location]:
                        visited[jumped_location] = visited[current_location] + 1
                        queue.append(jumped_location)
                else:
                    visited[target_location] = visited[current_location] + 1
                    queue.append(target_location)


ladder_snake = dict()
N, M = map(int, input().split())
for _ in range(N + M):
    x, y = map(int, input().split())
    ladder_snake[x] = y
visited = [0] * 101

print(bfs())
