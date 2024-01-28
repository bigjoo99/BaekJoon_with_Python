import sys

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

P.sort()

x = 0
sum_arr = []

for i in range(N):
    x += P[i]
    sum_arr.append(x)
    
print(sum(sum_arr))