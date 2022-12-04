def solution(n):
    pizza_count = 1
    while pizza_count * 6 % n != 0:
        pizza_count += 1
    return pizza_count