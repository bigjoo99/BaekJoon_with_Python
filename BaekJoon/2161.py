from collections import deque

n = int(input())
d = deque()
result = []

for i in range(1, n+1):
    d.append(i)

for i in range(len(d)-1):
    result.append(d.popleft())
    d.append(d.popleft())
    
result.append(d.pop())

print(*result)
