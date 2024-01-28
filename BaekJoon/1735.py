def gcd(m,n):
    if m<n:
        m,n=n,m
    if n==0:
        return m
    
    if m%n ==0:
        return n
    else:
        return gcd(n,m%n)
    
arr_X = list(map(int, input().split()))
arr_Y = list(map(int, input().split()))

A = arr_X[0]*arr_Y[1] + arr_Y[0]*arr_X[1]
B = arr_X[1]*arr_Y[1]

C = gcd(A,B)

print(int(A/C), int(B/C), end=' ')