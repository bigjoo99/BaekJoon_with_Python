n , l = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
cnt = 1
x = arr[0]

for i in arr[1:]:
    if (i + 0.5) - (x-0.5) > l:
        cnt += 1
        x = i
        
print(cnt)