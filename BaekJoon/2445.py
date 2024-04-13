x = int(input())

for i in range(1, x+1):
    print('*' * i + ' ' * (x-i) + ' ' * (x-i)+'*' * i)
for i in range(x-1,0 ,-1):
    print('*' * i + ' ' * (x-i) + ' ' * (x-i) + '*' * i)