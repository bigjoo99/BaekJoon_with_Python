import sys

stack = []
list = []

n = int(sys.stdin.readline())

for i in range(n):
    
    prompt = sys.stdin.readline().split()
    
    if prompt[0] == '1':
        stack.append(prompt[1])    
    
    elif prompt[0] == '2':
        if len(stack) ==0:
            list.append('-1')

        else:
            list.append(stack.pop())
    
    elif prompt[0] == '3':
        list.append(len(stack))
    
    elif prompt[0] == '4':
        if len(stack) ==0:
            list.append('1')
        else:
            list.append('0')
    
    elif prompt[0] == '5':
        if len(stack) ==0:
            list.append('-1')
        else:
            list.append(stack[-1])
            
for _ in list:
    print(_)