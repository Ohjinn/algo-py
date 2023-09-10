from collections import deque


def solution(food):
    answer = ''
    food_sequence = deque([0])
    for i in range(len(food) - 1, 0, -1):
        num_of_food = food[i]
        while num_of_food > 1:
            food_sequence.append(i)
            food_sequence.appendleft(i)
            num_of_food -= 2
    return ''.join([str(val) for val in food_sequence])


print(solution([1, 7, 1, 2]))
