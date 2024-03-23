# 2022 KAKAO TECH INTERNSHIP
# level 4
from collections import deque

def solution(rc, operations):
    
    rc = deque([deque(i) for i in rc])
    firsts = deque()
    lasts = deque()
    
    for i in rc:
        firsts.append(i.popleft())
        lasts.append(i.pop())
        
    for op in operations:
        if op == "Rotate":
            rc[0].appendleft(firsts.popleft())
            lasts.appendleft(rc[0].pop())
            rc[-1].append(lasts.pop())
            firsts.append(rc[-1].popleft())
        else:
            firsts.appendleft(firsts.pop())
            rc.appendleft(rc.pop())
            lasts.appendleft(lasts.pop())
    
    for i in rc:
        i.appendleft(firsts.popleft())
        i.append(lasts.popleft())
            
    return [list(i) for i in rc]
