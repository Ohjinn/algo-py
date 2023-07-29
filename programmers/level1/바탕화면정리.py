def solution(wallpaper):
    answer = [-1 for i in range(4)]
    for index, element in enumerate(wallpaper):
        lx = element.find('#')
        rx = element.rfind('#')

        if answer[1] == -1 or answer[3] == -1:
            answer[1] = lx
            answer[3] = rx
            answer[0] = index

        if lx != -1 and lx < answer[1]:
            answer[1] = lx

        if rx != -1 and rx > answer[3]:
            answer[3] = rx

        if lx != -1 or rx != -1:
            answer[2] = index

    answer[2] += 1
    answer[3] += 1
    return answer