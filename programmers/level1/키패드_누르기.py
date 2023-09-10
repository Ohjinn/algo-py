def check_position(number):
    num_pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    for i_index, i in enumerate(num_pad):
        for j_index, j in enumerate(i):
            if number == j:
                return [i_index, j_index]


def distance_checker(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def solution(numbers, hand):
    answer = ''

    left_posi = '*'
    right_posi = '#'
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_posi = str(i)
        elif i in [3, 6, 9]:
            answer += 'R'
            right_posi = str(i)
        else:
            # 왼손, 오른손, 누를 숫자의 위치 확인
            left_point = check_position(left_posi)
            right_point = check_position(right_posi)
            target_point = check_position(str(i))

            # 왼손과 타겟, 오른손과 타겟의 거리 계산
            left_distance = distance_checker(left_point, target_point)
            right_distance = distance_checker(right_point, target_point)

            # 거리에 따른 양 손의 최근 위치 변경, answer 에 추가
            if left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    right_posi = str(i)
                else:
                    answer += 'L'
                    left_posi = str(i)
            elif left_distance > right_distance:
                answer += 'R'
                right_posi = str(i)
            else:
                answer += 'L'
                left_posi = str(i)

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))