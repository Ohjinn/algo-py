import heapq
def solution(k, score):
    answer = []
    top_rankers = []
    for day_score in score:
        top_rankers.append(day_score)
        top_rankers.sort(reverse=True)
        if len(answer) >= k:
            top_rankers.pop()
            answer.append(top_rankers[k - 1])
        else:
            answer.append(top_rankers[len(answer)])
    return answer


def solution2(k, score):
    answer = []
    top_rankers = []
    for day_score in score:
        top_rankers.append(day_score)
        if len(top_rankers) > k:
            top_rankers.remove(min(top_rankers))
        answer.append(min(top_rankers))
    return answer


def solution3(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])


print(solution2(3, [10, 100, 20, 150, 1, 100, 200]))
