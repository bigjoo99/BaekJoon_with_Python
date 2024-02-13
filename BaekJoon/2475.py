x = list(map(int,input().split()))
sum=0

for i in x:
    sum+=(i**2)
    
print(sum%10)