n = int(input())

arr = list(map(int, input().split()))

x = sorted(arr)
y = sorted(arr, reverse=True)
result = []

for i in range(n):
    result.append(x[i]+y[i])
    
print(min(result))