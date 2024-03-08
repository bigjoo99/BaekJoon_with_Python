n = int(input())
top = list(map(int,input().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack:
        if top[stack[-1][0]]<top[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0]+1
            break
    stack.append((i,top[i]))
    
print(*result)