import math

H, W, N, M = list(map(int, input().split()))

x = math.ceil(H/(M+1))
y = math.ceil(W/(N+1))

print(x*y)