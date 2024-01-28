M = int(input())

s = []

for i in range(M):
    cmd = input().split()
    
    if cmd[0] == 'add':
        if int(cmd[1]) not in s :
            s.append(int(cmd[1]))

    elif cmd[0] == 'remove':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
            
    elif cmd[0] == 'check':
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
            
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.append(int(cmd[1]))
            
    elif cmd[0] == 'all':
        s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
    elif cmd[0] == 'empty':
        s = []