# 숫자 문자열과 영단어

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    x = ''
    result = ''
    for i in s:
        if i.isalpha():
            x += i
            if x in words:
                result += str(words.index(x))
                x = ''
        else:
            result += i

    return int(result)