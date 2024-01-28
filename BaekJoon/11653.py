n = int(input())

arr = []

num = 2;

while n != 1:    
    if n%num == 0:
        n = n//num
        arr.append(num)
        num = 2
    else:
        num = num+1


arr.sort()

for i in arr:
    print(i)