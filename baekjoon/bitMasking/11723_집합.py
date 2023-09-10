import sys
input = sys.stdin.readline

null_set = set()

line_count = int(input())

for i in range(line_count):
    instructions = input().split(' ')

    if len(instructions) == 1:
        if instructions[0] == 'empty':
            null_set = set()
        else:
            null_set = set([i for i in range(1, 21)])

    else:
        number = int(instructions[1])
        if instructions[0] == 'add':
            null_set.add(number)
        elif instructions[0] == 'remove':
            null_set.remove(number)
        elif instructions[0] == 'check':
            print(1 if number in null_set else 0)
        elif instructions[0] == 'toggle':
            if number in null_set:
                null_set.discard(number)
            else:
                null_set.add(number)