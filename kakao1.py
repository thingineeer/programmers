# 신규 아이디 추천

def solution(new_id):
    temp = ''
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i not in '~!@#$%^&*()=+[{]}:?,<>/':
            temp += i
    new_id = temp

    temp = ''

    # 3
    if len(new_id) == 0:
        return 'aaa'
    else:
        cnt = 0
        for i in new_id:
            if i == '.':
                cnt += 1
                if cnt < 2:
                    temp += i
            else:
                temp += i
                cnt = 0

        # 4
        new_id = list(temp)
        temp = ''

        if new_id[0] == '.':
            if len(new_id) >= 2:
                new_id = new_id[1:]
            else:
                new_id = '.'

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    temp = list(new_id)

    # 5
    if len(temp) == 0:
        return 'aaa'

    # 6
    while len(temp) >= 16:
        temp.pop()
    if temp[-1] == '.':
        temp.pop()
    while (temp[-1] == '.'):
        temp.pop()

    new_id = list(temp)

    # 7
    while (len(new_id) <= 2):
        new_id.append(new_id[-1])

    for i in new_id:
        answer += i

    return answer
