list = input()

stack = []
cnt = 0

for i in range(len(list)):
    if list[i] == '(':
        stack.append(list[i])
    else:
        if list[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        
        else:
            stack.pop()
            cnt += 1
            
print(cnt)    