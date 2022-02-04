import sys

n = int(sys.stdin.readline())

stack = []

def push(x):
    stack.append(x)

def pop():
    if pop:
        stack.pop()
    else:
        return -1

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        pop()
    else:
        push(temp)

print(sum(stack))