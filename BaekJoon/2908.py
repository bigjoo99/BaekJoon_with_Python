a,b = map(int, input().split())

reverse_a= a//100+(a//10)%10*10+(a%10)*100
reverse_b= b//100+(b//10)%10*10+(b%10)*100

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)    
