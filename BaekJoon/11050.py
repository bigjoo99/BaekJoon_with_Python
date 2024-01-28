N, K = map(int,input().split())

A = 1
for i in range(1, N+1):
    A *= i
    
B = 1
for j in range(1, K+1):
    B *= j
    
for k in range(1, N-K+1):
    B *= k
    
print(int(A/B))