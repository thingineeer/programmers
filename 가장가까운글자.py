def solution(s):
    result = []
    stack = []
    for i in s:
        # 없으면 그냥 집어 넣기
        if i not in stack:
            stack.append(i)
            result.append(-1)
        else:
        # 있으면 논리 적용
            result.append(stack[::-1].index(i)+1)
            stack.append(i)
    return result
