def solution(a, b, n):
    q = 0
    m = 0
    answer = 0
    
    while n >= a:
        q = n // a
        m = n % a
        n = q*b + m
        answer += q*b
    
    return answer
