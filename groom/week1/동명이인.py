# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
i, name = user_input.split(' ')
times = 0

for j in range(int(i)):
    if name in input():
        times += 1

print(times)