import math


def solution(fees, records):
    default = 1439  # 23:59
    result = {}
    answer = []

    # 차 번호순으로 정렬후 뒤집어 정렬
    lst = reversed(sorted(records, key=lambda x: int(x.split()[1])))
    for l in lst:
        i, j, k = l.split()

        m = int(i[:2]) * 60 + int(i[3:])  # 시각 -> 분

        if k == 'OUT' and not (j in result.keys()):  # 처음 들어오는 경우
            result[j] = m
        elif k == 'OUT':  # 한번이라도 들어온경우
            result[j] += m
        elif k == 'IN' and not (j in result.keys()):  # 처음 들어오는경우 (출차가 없는경우)
            result[j] = default - m
        else:  # 이미 있는 경우
            result[j] -= m

    for i, j in result.items():
        if j < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((j - fees[0]) / fees[2]) * fees[3])

    answer = list(reversed(answer))

    return answer
