import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

sum = 1

for i in range(n):
    if sum < arr[i]:
        break
    sum += arr[i]
    
print(sum)