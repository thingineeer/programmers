def solution(str1, str2):
            
    a = []

    for i in range(len(str1)-1):
        pair = str1[i:i+2]
        if pair.isalpha():
            a.append(pair.lower())
            
    b = []
    for i in range(len(str2)-1):
        pair = str2[i:i+2]
        if pair.isalpha():
            b.append(pair.lower())

    intersect = []      
    union_result = a.copy()
    a_temp = a.copy()
    a_temp2 = a.copy()
    
    for i in b:
        if i not in a_temp:
            union_result.append(i)
        else:
            a_temp.remove(i)
            
    for i in b:
        if i in a_temp2:
            a_temp2.remove(i)
            intersect.append(i)
            
    if len(intersect) == 0 or len(union_result) == 0:
        return 65536
    else:
        j =  len(intersect) / len(union_result)
        answer = int(j * 65536)
        return answer