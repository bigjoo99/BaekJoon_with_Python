import sys
input = sys.stdin.readline

N = int(input())

ls = [int(input()) for _ in range(N)]
ls.sort()

minus = list()

for i in range(N):
    for j in range(i+1, N):
        minus.append(abs(ls[i]- ls[j]))

minus.sort()
ans = [minus[0]]

for i in range(2, minus[0]):
    if minus[0] % i == 0:
        ans.append(i)

ans.sort()

print(*ans)