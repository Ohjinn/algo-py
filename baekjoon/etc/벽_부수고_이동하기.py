import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([n])
    while queue:
        front = queue.popleft()
        if front == k:
            return visited[front]
        for possible_way in (front - 1, front + 1, front * 2):
            if 0 <= possible_way < max_location and not visited[possible_way]:
                visited[possible_way] = visited[front] + 1
                queue.append(possible_way)


max_location = 100001
n, ㅡ = map(int, input().split())
visited = [0] * max_location
print(bfs())
