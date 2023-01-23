def solution(price, money, count):
    calculated_price = price * count * (count + 1) / 2
    if calculated_price > money:
        return calculated_price - money
    else:
        return 0
