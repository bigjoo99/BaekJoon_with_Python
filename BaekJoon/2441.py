n = int(input())
cnt = 0

for i in range(n):    
    for j in range(cnt):
        print(' ', end='')
    
    for k in range(n-i):
        print('*', end='')
    print()
    cnt+=1