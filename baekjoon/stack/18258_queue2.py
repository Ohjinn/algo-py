import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()


def push(x):
    queue.append(x)


def pop():
    if queue:
        print(queue.popleft())
    else:
        print(-1)


def size():
    print(len(queue))


def empty():
    if queue:
        print(0)
    else:
        print(1)


def front():
    if queue:
        print(queue[0])
    else:
        print(-1)


def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)


for _ in range(n):
    line = input().split()
    if line[0] == 'push':
        push(line[1])
    elif line[0] == 'pop':
        pop()
    elif line[0] == 'size':
        size()
    elif line[0] == 'empty':
        empty()
    elif line[0] == 'front':
        front()
    elif line[0] == 'back':
        back()

