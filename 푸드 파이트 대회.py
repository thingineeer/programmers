def solution(food):
    result = ""
  
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            result += str(i)
    result += '0'
    for i in range(len(food)-1, 0, -1):
        for j in range(food[i] // 2):
            result += str(i)

    return result
