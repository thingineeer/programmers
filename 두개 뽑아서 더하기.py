def solution(numbers):
    result = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            if a not in result:
                result.append(a)
            
    return sorted(result)
