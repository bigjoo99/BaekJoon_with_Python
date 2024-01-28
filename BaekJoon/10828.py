import sys

n = int(sys.stdin.readline())
    
stack = []

for i in range(n):
    act = sys.stdin.readline().split()
    
    if act[0] =='push':
        stack.append(act[1])
        
    elif act[0] =='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        
    elif act[0] == 'size':
        print(len(stack))
        
    elif act[0] =='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
            
    elif act[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
                    