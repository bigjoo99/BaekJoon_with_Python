T = int(input())

result =[]

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    result.append(arr[-3])

for x in result:
    print(x)