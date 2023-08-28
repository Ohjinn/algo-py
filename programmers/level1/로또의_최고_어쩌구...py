def solution(lottos, win_nums):
    counter = 0
    num_of_zero = 0

    for i in lottos:
        if i == 0:
            num_of_zero += 1
        for j in win_nums:
            if i == j:
                counter += 1

    return [7 - max(counter + num_of_zero, 1), 7 - max(counter, 1)]


print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))
