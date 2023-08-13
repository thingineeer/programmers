s = "a B z"
n = 25
result = []
for i in s:
    if i == ' ':
        result.append(' ')
    elif i.isupper():
        a = ord(i) + n
        if 65 <= a <= 90:
            result.append(chr(a))
        else:
            result.append(chr(a-26))
    elif i.islower():
        a = ord(i) + n
        if 97 <= a <= 122:
            result.append(chr(a))
        else:
            result.append(chr(a-26))
print(''.join(result))