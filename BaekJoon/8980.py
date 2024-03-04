n, c = map(int, input().split())
m = int(input())
arr = []

for _ in range(m):
    arr.append(tuple(map(int,input().split())))

arr.sort(key=lambda x: x[1])

truck = [0]*n
result = 0

for s, e, box in arr:
    x = box
    for i in range(s,e):
        if truck[i-1] + x > c:
            x = c- truck[i-1]
    for i in range(s,e):
        truck[i-1] += x
    result += x

print(result)