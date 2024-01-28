L, C = map(int, input().split())

arr = sorted(input().split())

x = []
y = []

for i in arr:
    if i == 'a' or i =='e' or i=='i' or i=='o' or i=='u':
        x.append(i)
    else:
        y.append(i)
        
x.sort()
y.sort()
arr.sort()


