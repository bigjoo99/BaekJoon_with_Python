S = input()
bomb = input()
stack = []

for i in S:
    stack.append(i)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

s = ''.join(stack)
if len(s) == 0:
    print('FRULA')
else:
    print(s)