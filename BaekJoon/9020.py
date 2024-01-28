def is_prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False 
    return True

for i in range(int(input())):
    n = int(input())
    max_a = 0;
    a = 0
    b = n
    
    for k in range(2,n//2+1):
        if is_prime_number(k) and is_prime_number(n-k):
            a = k
            b = n-k
            if max_a < a:
                max_a=a            
                
    print(max_a,n-max_a, end = ' ')
    print()