def solution(priorities, location):
    answer = 0
    length = len(priorities)
    check = [0 for i in range(length)]
    j = 0

    while check[location] == 0:
        max = 0
        num_of_max = 0
        print(check)
        print(priorities)
        for i in range(length):
            if priorities[i] > max and check[i] == 0:
                max = priorities[i]

        for i in range(length):
            if priorities[i] == max:
                num_of_max += 1
        print(max)
        print("nom", num_of_max)

        for j in range(j, length):
            print("j = ", j)
            if priorities[j] >= max and check[j] == 0:
                check[j] = 1
                answer += 1
                num_of_max -= 1
                print(answer)
                print("nom", num_of_max)
                if num_of_max == 0:
                    break

            if check[location] == 1:
                return answer
        if j == length - 1:
            j = 0

    print(check)
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))

