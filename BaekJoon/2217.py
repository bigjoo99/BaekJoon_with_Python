import sys

input = sys.stdin.readline

n = int(input())
arr = []
result = []
for i in range(n):
    arr.append(int(input()))
    
arr.sort()

for i in arr:
    result.append(i*n)
    n -=1
    
print(max(result))