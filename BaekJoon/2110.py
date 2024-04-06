n, c = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
start = 1
end = arr[-1] - arr[0]

result = 0

while(start<=end):
    distance = []
    distance.append(arr[0])
    
    mid = (start+end)//2
    
    for x in arr:
        if x - distance[-1] >= mid:
            distance.append(x)
        
    if len(distance) < c:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        
print(result)