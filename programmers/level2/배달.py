import heapq


def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [cost + c, n])


def solution(N, road, K):
    shortest_way = [float('inf')] * (N + 1)
    shortest_way[1] = 0

    adj = [[] for _ in range(N + 1)]

    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    print(adj)
    dijkstra(shortest_way, adj)
    return len([i for i in shortest_way if i <= K])


solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)