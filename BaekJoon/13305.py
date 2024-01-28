import sys 

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
x = cost[0]

for i in range(N-1):
    if cost[i] < x:
        x = cost[i]
    result += x*road[i]
    
print(result)