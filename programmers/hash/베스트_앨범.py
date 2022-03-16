

def solution(genres, plays):
    answer = []
    genre_dic = {}
    genre_count = {}

    for i in range(len(genres)):
        if genres[i] in genre_dic.keys():
            genre_dic[genres[i]].append(plays[i])
        else:
            genre_dic[genres[i]] = [plays[i]]

    for genre in genre_dic.keys():
        genre_dic[genre].sort(reverse=True)
        genre_count[genre] = [sum(genre_dic[genre])]

    genre_count = dict(sorted(genre_count.items(), key=lambda item: item[1], reverse=True))

    for genre in genre_count.keys():
        instant = genre_dic[genre]
        for i in range(2):
            answer.append(plays.index(instant[i]))

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

