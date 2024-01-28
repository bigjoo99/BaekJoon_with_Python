import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

T = int(input())

arr = []
for _ in range(T):
    x = int(input())
    while True:
        if is_prime(x):
            arr.append(x)
            break
        else:
            x += 1
            
for i in arr:
    print(i)