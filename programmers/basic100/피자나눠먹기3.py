from math import ceil
def solution(slice, n):
    if slice >= n:
        return 1
    return ceil(n / slice)