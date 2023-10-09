def solution(survey, choices):
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    mid = 4
    list1 = ['R','T','C','F','J','M','A','N']
    list2 = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
    answer = ''
    
    for i in range(len(choices)):
        if mid < choices[i]:
            list2[list1.index(survey[i][1])] += score[choices[i]]
        elif mid > choices[i]:
            list2[list1.index(survey[i][0])] += score[choices[i]]
        else:
            continue
            
    for i in range(0, 8, 2):
        if list2[i] < list2[i+1]:
            answer += list1[i+1]
        else:
            answer += list1[i]
    return answer
