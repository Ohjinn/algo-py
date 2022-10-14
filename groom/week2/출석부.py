import sys
input = sys.stdin.readline

length, sequence = map(int, input().split())

attendance = {}
# for i in range(length):
#     name, height = input().split()
#     attendance[name] = height
#
# print(sorted(attendance.items(), key=lambda a: (a[0], a[1])))

for i in range(length):
    name, height = input().split()
    if name in attendance:
        attendance[name].append(float(height))
    else:
        attendance[name] = [float(height)]

idx = 0
while idx < (length - sequence + 1):
    dic = attendance.popitem()
    if len(dic[1]) > 1:
        for i in sorted(dic[1]):
            idx += 1
    idx += 1
    print(dic[0], dic[1][0])

