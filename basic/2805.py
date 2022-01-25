N, M = map(int, input().split())
Trees = list(map(int, input().split()))


def cutter(n, m, trees):
    bottom = 0
    top = max(trees)

    while top >= bottom:
        tree_sum = 0
        mid = (top + bottom) // 2

        print(mid)
        print()
        for tree in trees:
            if tree - mid > 0:
                tree_sum += (tree - mid)

        if tree_sum >= m:
            bottom = mid + 1
        else:
            top = mid - 1

        print(bottom)
        print(top)
    return top


print(cutter(N, M, Trees))

