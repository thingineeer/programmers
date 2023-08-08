def solution(ingredient):
    result = 0
    stack = []
    for i in ingredient:
        stack.append(i)

        # 스택이 [1, 2, 3, 1] 패턴과 일치하는 경우
        if stack[-4:] == [1, 2, 3, 1]:
            result += 1
            del stack[-4:]
    return result
