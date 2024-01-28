from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

d = deque()

for i in range(t):
    s = input().split()

    if s[0] == 'push_front':
        d.appendleft(s[1])
    elif s[0] == 'push_back':
        d.append(s[1])
    elif s[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(d))
    elif s[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)