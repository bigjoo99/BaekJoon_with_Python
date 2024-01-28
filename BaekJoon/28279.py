import sys
from collections import deque

d = deque()

N = int(sys.stdin.readline())

list = []

for i in range(N):
    
    prompt = sys.stdin.readline().split()
    
    if prompt[0] == '1':
        d.appendleft(prompt[1])    

    elif prompt[0] == '2':
        d.append(prompt[1])

    elif prompt[0] == '3':
        if len(d) != 0:
            pop = d.popleft()
            list.append(pop)
        else:
            list.append('-1')
    
    elif prompt[0] == '4':
        if len(d) != 0:
            pop = d.pop()
            list.append(pop)
        else:
            list.append('-1')
    
    elif prompt[0] == '5':
        list.append(len(d))
        
    elif prompt[0] == '6':
        if len(d) ==0:
            list.append('1')
        else:
            list.append('0')
    
    elif prompt[0] == '7':
        if len(d) != 0:
            pop = d.popleft()
            d.appendleft(pop)
            list.append(pop)
        else:
            list.append('-1')
    
    elif prompt[0] == '8':
        if len(d) != 0:
            pop = d.pop()
            d.append(pop)
            list.append(pop)
        else:
            list.append('-1')
for _ in list:
    print(_)