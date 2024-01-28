N,M = map(int, input().split())

arr = []
for x in range(N):
    arr.append(x+1)

for _ in range(M):
    i, j = map(int,input().split())
    x = arr[i-1]
    y = arr[j-1]
    arr[i-1] = y
    arr[j-1] = x

for x in arr:
    print(x, end=' ')