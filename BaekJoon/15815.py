s = input()

number = []

for i in range(len(s)):
    if s[i] == '+':
        a = number.pop()
        b = number.pop()
        number.append(a+b)
    elif s[i] == '-':
        a = number.pop()
        b = number.pop()
        number.append(b-a)
    elif s[i] == '*':
        a = number.pop()
        b = number.pop()
        number.append(a*b)
    elif s[i] == '/':
        a = number.pop()
        b = number.pop()
        number.append(b//a)
    else:
        number.append(int(s[i]))

print(*number)