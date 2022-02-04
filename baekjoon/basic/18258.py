lines = int(input())
queue = []
location = 0

for _ in range(lines):
    N = list(input().split(' '))

    if N[0] == 'push':
        queue.append(N[1])
    elif N[0] == 'pop':
        if len(queue)-location == 0:
            print(-1)
        else:
            print(queue[location])
            location += 1
    elif N[0] == 'size':
        print(len(queue) - location)
    elif N[0] == 'empty':
        if len(queue) - location == 0:
            print(1)
        else:
            print(0)
    elif N[0] == 'front':
        if len(queue) - location == 0:
            print(-1)
        else:
            print(queue[location])
    elif N[0] == 'back':
        if len(queue) - location == 0:
            print(-1)
        else:
            print(queue[-1])

