from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    # 중복 제거된 신고 대상 정보 저장
    report_count = defaultdict(int)
    for i in set(report):
        report_count[i.split()[1]] += 1
    
    print(report_count)
    # k 이상으로 신고된 대상 필터링
    filtered_set = {key for key, value in report_count.items() if value >= k}
    
    print(filtered_set)
    # 각 유저가 어떤 유저에게 신고했는지 저장
    result_dict = defaultdict(list)
    for i in ser(report):
        a, b = i.split()
        result_dict[a].append(b)
    print(result_dict)

    # 필터링된 대상에 해당하는 유저들을 카운팅
    for i, user in enumerate(id_list):
        answer[i] = sum(1 for target in result_dict[user] if target in filtered_set)

    return answer
            
