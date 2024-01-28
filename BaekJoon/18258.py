from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

queue = deque([])

for _ in range(n):
    x = input().split()
    
    if x[0] =='push':
        queue.append(x[1])
    elif x[0] =='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)  
    elif x[0] =='size':
        print(len(queue))
    elif x[0] =='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif x[0] =='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x[0] =='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)