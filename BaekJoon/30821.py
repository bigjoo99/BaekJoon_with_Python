n = int(input())

a = 1

for i in range(n,n-5,-1):
    a *= i
    
print(int(a/120))