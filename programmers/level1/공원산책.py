def check_avail(park, now, direction, count):
    width, height = len(park[0]), len(park)
    x, y = now[0], now[1]
    if direction == 'E':
        for _ in range(count):
            x += 1
            if x >= width or park[y][x] == 'X':
                return False
    elif direction == 'S':
        for _ in range(count):
            y += 1
            if y >= height or park[y][x] == 'X':
                return False
    elif direction == 'W':
        for _ in range(count):
            x -= 1
            if x < 0 or park[y][x] == 'X':
                return False
    elif direction == 'N':
        for _ in range(count):
            y -= 1
            if y < 0 or park[y][x] == 'X':
                return False
    return True


def solution(park, routes):
    answer = []
    # park_array = [[j for j in i] for i in park]
    park_array = []
    for i, width in enumerate(park):
        park_array.append([])
        for j, element in enumerate(width):
            park_array[i].append(element)
            if element == 'S':
                answer.append(int(j))
                answer.append(int(i))
    for route in routes:
        direction, count = route.split(" ")
        count = int(count)
        if check_avail(park, answer, direction, count):
            if direction == 'E':
                answer[0] += count
            elif direction == 'S':
                answer[1] += count
            elif direction == 'W':
                answer[0] -= count
            elif direction == 'N':
                answer[1] -= count
            print(answer)

    return [answer[1], answer[0]]

print(solution(["SOO","OXX","OOO"],	["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
