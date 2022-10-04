user_input = input()
print("Hello Goorm! Your input is " + user_input)

inputArray = user_input.split(' ')
init = 1
for i in inputArray:
    init *= int(i)
print(init)