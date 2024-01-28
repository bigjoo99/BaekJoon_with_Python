def gcd(m,n):
    if m<n:
        m,n=n,m
    if n==0:
        return m
    
    if m%n ==0:
        return n
    else:
        return gcd(n,m%n)
    
A ,B = map(int,input().split())
C = gcd(A,B)

print(int(A*B/C))

