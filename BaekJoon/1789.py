S = int(input())

n = 1

while True:
    if n*(n+1) <=2*S:
        n+=1
    else:
        break
    
print(n-1)