
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


def solution2(phone_book):
    answer = True
    map = {}
    for number in phone_book:
        map[number] = 1
    for number in phone_book:
        temp = ''
        for detail in number:
            if temp in map and temp != number:
                answer = False

    return answer

print(solution2(["119", "97674223", "1195524421"]))