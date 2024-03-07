n = int(input())

arr = [] 
cnt = 0

for i in range(n):
    x = input().rstrip()
    stack = []
    
    for j in range(len(x)):
        if len(stack) != 0:
            if x[j] == stack[-1]:
                stack.pop()
            else:
                stack.append(x[j])
        else:
            stack.append(x[j])
    
    if len(stack) == 0:
        cnt += 1

print(cnt)