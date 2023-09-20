def solution(brown, yellow):
    
    d = []
    n = brown + yellow # n : 전체 블럭의 수
    for i in range(1, int(n**(1/2)) + 1): # 약수 모음
        if (n % i == 0):
            d.append(i) 
            if ( (i**2) != n) : 
                d.append(n // i)
    d.sort()
    
    for i in range(len(d)-1, 0, -1):
        x = d[i]
        y = n / x
        if (x-2)*(y-2) == yellow:
            return [x, y]
