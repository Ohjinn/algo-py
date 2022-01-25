input_val = input()
input_num = input_val.split(" ")
hour = int(input_num[0])
minute = int(input_num[1])

if minute - 45 < 0:
    if hour - 1 < 0:
        hour = 24
    hour -= 1
    minute = 60 + minute - 45
else:
    minute -= 45



print(hour, minute)