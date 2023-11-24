def judge(start, end):
    keypad = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }
 
    start_distance = keypad[start]
    end_distance = keypad[end]
 
    distance = abs(start_distance[0] - end_distance[0]) + abs(start_distance[1] - end_distance[1])
    return distance
 
 
def solution(numbers, hand):
    
    l = "*"
    r = "#"
    l_pad = ["1", "4", "7"]
    r_pad = ["3", "6", "9"]
    numbers = list(map(str, numbers))
    result = []
    
    for number in numbers:
        if number in l_pad:
            result.append("L")
            l = number
        elif number in r_pad:
            result.append("R")
            r = number
        else:
            left_distance = judge(l, number)
            right_distance = judge(r, number)
            if left_distance == right_distance:
                if hand == "left":
                    result.append("L")
                    l = number
                elif hand == "right":
                    result.append("R")
                    r = number
            elif left_distance > right_distance:
                    result.append("R")
                    r = number
            else:
                result.append("L")
                l = number
    
    return ''.join(result)
