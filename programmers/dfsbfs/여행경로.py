# 나는 바본가
# def solution(tickets):
#     answer = []
#     now_key = 'ICN'
#     dict_tickets = dict(tickets)
#     sorted(dict_tickets.items(), key=lambda item: item[1])
#     while len(dict_tickets) > 0:
#         temp = now_key
#         now_key = dict_tickets[now_key]
#         answer.append(temp)
#         if len(dict_tickets) == 1:
#             answer.append(dict_tickets[temp])
#         dict_tickets.pop(temp)
#
#     return answer

def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

    for r in routes.keys():
        routes[r].sort(reverse=True)

    st = ["ICN"]
    path = []

    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    answer = path[::-1]
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
