import datetime


def solution(a, b):
    date = datetime.date(2016, a, b)
    day_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    no = date.weekday()
    return day_of_week[no]


print(solution(5, 24))
