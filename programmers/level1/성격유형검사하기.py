def solution(survey, choices):
    answer = ''
    point_of_statics = {'RT': 0, 'CF': 0,
                        'JM': 0, 'AN': 0}
    same_points_first = {'RT': 'R', 'CF': 'C',
                         'JM': 'J', 'AN': 'A'}
    point_array = [-3, -2, -1, 0, 1, 2, 3]

    for idx, element in enumerate(survey):
        if element in point_of_statics:
            point_of_statics[element] -= point_array[choices[idx] - 1]
        else:
            point_of_statics[element[::-1]] += point_array[choices[idx] - 1]

    for key, value in point_of_statics.items():
        if value == 0:
            answer += same_points_first[key]
        elif value > 0:
            answer += key[0]
        else:
            answer += key[1]

    return answer