n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = []

for i in range(n//2):
    a = arr[i]
    b = arr[-1-i]
    result.append(a+b)
    
print(min(result))