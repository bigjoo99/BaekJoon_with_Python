import sys
input = sys.stdin.readline

arr = input()
T = int(input())
q = []
result = []

for _ in range(T):
    q.append(list(map(str, input().split())))
    
prefix = [0]*(len(arr))
prefix[0] = arr[0]

for x in range(1,len(arr)):
    prefix[x] = prefix[x-1] + arr[x]

for i in range(T):
    s, l, r = q[i][0], int(q[i][1]), int(q[i][2])
    x = arr[l:r+1]
    print(x.count(s))