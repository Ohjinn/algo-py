import re


def solution(files):
    answer = []

    separated = [re.split(r"([0-9]+)", file) for file in files]

    sort = sorted(separated, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]