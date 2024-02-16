n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(i+1)

result = []
cnt = 0

for i in range(n):
    cnt += k-1
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    result.append(str(arr.pop(cnt)))

print("<",", ".join(result)[:],">", sep='')