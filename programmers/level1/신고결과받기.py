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
