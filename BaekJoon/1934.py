def gcd(m,n):
    if m<n:
        m,n=n,m
    if n==0:
        return m
    
    if m%n ==0:
        return n
    else:
        return gcd(n,m%n)

T = int(input())

result = []

for _ in range(T):
    a ,b = map(int, input().split())
    c = gcd(a,b)
    x = a*b/c
    
    result.append(int(x))
    
for k in result:
    print(k)