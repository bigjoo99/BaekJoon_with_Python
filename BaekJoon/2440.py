x = int(input())

for i in range(x,0,-1):
    for _ in range(i):
        print('*', end='')
    print()