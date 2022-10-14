# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input().split()
inputs = [int(x) for x in user_input]

inputs.sort()

a = inputs[0] - inputs[3]
b = inputs[1] - inputs[2]

print(abs(a) + abs(b))