def solution(id_pw, db):
    answer = 'fail'
    for db_id_pw in db:
        if db_id_pw[0] == id_pw[0] and db_id_pw[1] == id_pw[1]:
            return 'login'
        elif db_id_pw[0] == id_pw[0]:
            answer = 'wrong pw'
    return answer


print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
