from collections import deque

def solution(queue1, queue2):
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    for _ in range(int(len(q1)*2.6)):
        if q1_sum > q2_sum:
            q1_sum -= q1[0]
            q2_sum += q1[0]
            q2.append(q1.popleft()) 
            cnt += 1
        elif q1_sum < q2_sum:
            q1_sum += q2[0]
            q2_sum -= q2[0]
            q1.append(q2.popleft())
            cnt += 1
        else:
            return cnt
    return -1
