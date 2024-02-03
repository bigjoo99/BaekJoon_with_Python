import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

result = []

for i in range(n,0,-1):
    x = arr[n-i]
    result.insert(x,i)

for i in result:
    print(i, end=' ')