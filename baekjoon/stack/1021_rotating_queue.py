import sys
from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))
queue = [i for i in range(1, n + 1)]
cnt = 0
for i in range(m):
    queue_len = len(queue)
    queue_index = queue.index(arr[i])
    if queue_index < queue_len - queue_index:
        while True:
            if queue[0] == arr[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                cnt += 1
    else:
        while True:
            if queue[0] == arr[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                cnt += 1
print(cnt)
# 시간 복잡도가 O(n)
# deque는 O(1)이 걸림
