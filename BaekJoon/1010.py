def nCk(N,K):
    A = 1
    for i in range(1, N+1):
        A *= i
    
    B = 1
    for j in range(1, K+1):
        B *= j
    
    for k in range(1, N-K+1):
        B *= k
    
    return int(A/B)

T = int(input())
result = []
for _ in range(T):
    n,m = map(int, input().split())
    x = nCk(m,n)
    result.append(x)
    
for i in result:
    print(i)