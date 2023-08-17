def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        if len(cache) >= cacheSize:
            check = False
            for i, cache_city in enumerate(cache):
                if cache_city == city.lower():
                    cache.pop(i)
                    cache.insert(0, city.lower())
                    answer += 1
                    check = True
                    break
            if check == False:
                cache.insert(0, city.lower())
                cache.pop()
                answer += 5
        else:
            check = False
            for i, cache_city in enumerate(cache):
                if cache_city == city.lower():
                    answer += 1
                    cache.pop(i)
                    cache.insert(0, city.lower())
                    check = True
            if check == False:
                cache.insert(0, city.lower())
                answer += 5
    return answer

print(solution(2, ["a", "a", "a", "b", "b", "b", "c", "c", "c"]))