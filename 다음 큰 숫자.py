# 별다른 insight는 없어서 1씩올려서 비교해보는 걸로 

def solution(n):
    A = list(bin(n)[2:]).count('1')
    
    while True:
        n += 1
        B = list(bin(n)[2:]).count('1')
        if A == B:
            break
            
    return n
