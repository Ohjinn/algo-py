<<<<<<< HEAD
# 신고 당한놈이 아니라 신고한놈이 전리품으로 메일을 가져감
def solution(id_list, report, k):
    answer = []
    report_cnt_dict = {}

    report = list(set(report))
    for id in id_list:
        report_cnt_dict[id] = 0

    for a_report in report:
        a_report = a_report.split(' ')
        report_cnt_dict[a_report[1]] += 1
    print(report_cnt_dict)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
=======
def solution(id_list, report, k):
    answer = [0 for i in id_list]
    # id_list의 이름별 index를 저장
    # 예) id_list = [muji, frodo] -> indexer = {'muji': 0, 'frodo': 1}
    indexer = {string: i for i, string in enumerate(id_list)}

    # 중복을 제거하고 신고한 사람에게 신고당한 사람의 index를 저장
    # 예) counter = {'muji': [1, 2]} -> 무지는 1, 2번 사람을 신고함
    report_counter = {string: [] for string in id_list}

    reported_counter = {string: 0 for string in id_list}

    for case in report:
        reporter, reported = case.split()
        if indexer[reported] not in report_counter[reporter]:
            report_counter[reporter].append(indexer[reported])
            reported_counter[reported] += 1

    for i, name in enumerate(id_list):
        if reported_counter[name] >= k:
            for key, value in report_counter.items():
                if i in value:
                    answer[indexer[key]] += 1

    return answer
>>>>>>> 57e10baa77ebdc5c5b67e534385d5db93da760b5
