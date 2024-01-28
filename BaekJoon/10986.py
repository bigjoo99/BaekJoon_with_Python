import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,input().split()))

prefix = [0 for _ in range(N+1)]

for x in range(N):
    prefix[x] = prefix[x-1] + arr[x]

cnt = 0

for i in range(1,N+1):
    for j in range(i, N+1):
        x = prefix[j] - prefix[i-1]
        if x % M ==0:
            cnt+=1

print(cnt)