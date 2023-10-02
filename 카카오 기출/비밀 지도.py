def solution(n, arr1, arr2):
    
    answers = [bin(arr1[i] | arr2[i])[2:] for i in range(n)]
    
    for i, answer in enumerate(answers):
        if len(answer) < n:
            answers[i] = '0'*(n - len(answer)) + answer
    result = []

    for i in answers:
        i = i.replace('1','#')
        i = i.replace('0',' ')
        result.append(i)

    return result
