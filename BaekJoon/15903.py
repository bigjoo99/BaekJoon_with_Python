n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    arr.sort()
    x = arr[0]
    y = arr[1]
    arr[0] = x+y
    arr[1] = x+y
    
sum = 0
for i in arr:
    sum += i
    
print(sum)