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
    for target_number in phone_book:
        for loop_number in phone_book:
            if target_number != loop_number:
                if target_number.startswith(loop_number):
                    return False
    return True


print(solution2(["123", "456", "789"]))
