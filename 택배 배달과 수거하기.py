def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()
        
    while deliveries or pickups:
        a, b = cap, cap
            
        answer += max(len(deliveries), len(pickups)) * 2

        while len(deliveries) and a >= 0:
            deli = deliveries.pop()
            if deli <= a:
                a -= deli
            else:
                deliveries.append(deli - a)
                break
                
        while len(pickups) and b >= 0:
            pick = pickups.pop()
            if pick <= b:
                b -= pick
            else:
                pickups.append(pick - b)
                break

    return answer
