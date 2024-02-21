n = int(input())

arr = []
cnt = 0 

for i in range(n):
    arr.append(int(input()))
    
for i in range(n-1,0,-1):
    if arr[i-1] >= arr[i]:
        cnt += arr[i-1] - arr[i] + 1
        arr[i-1] = arr[i] - 1 
        
print(cnt)