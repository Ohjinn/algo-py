# 특정 시간부터는 무조건 True이기 때문에 시간에 대한 이분탐색을 시행하면 된다.

def solution(a, b, g, s, w, t):
    l, r = 1, 4 * (10 ** 14)
    n = len(g)

    while l <= r:
        T = (l + r) // 2
        W, G, S = 0, 0, 0
        for town in range(n):
            if T < t[town]:
                continue
            X = w[town] + ((T - t[town]) // (t[town] * 2)) * w[town]  # 시간당 운반량
            G += min(X, g[town])  # 시간당 금
            S += min(X, s[town])  # 시간당 은
            W += min(X, g[town] + s[town])

        if G >= a and S >= b and W >= (a + b):
            r = T - 1
        else:
            l = T + 1

    return l