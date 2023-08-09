def solution(s):
    sp = s.split(' ')
    answer = ''
    for i in sp:
        if i == '':
            answer += ' '
            continue
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
        
    # 마지막에 공백이 n개인경우 n개로 만들어 줘야함
    # 이 처리 안해주면 결과 마지막 문자열에 공백이 하나 더 생긴다.
    l = len(s)
    answer = answer.rstrip()
    for i in range(l-len(answer)):
        answer += ' '
    return answer
