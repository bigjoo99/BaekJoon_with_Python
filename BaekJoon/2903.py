n = int(input())

x = 2

for i in range(n):
    x_n = (x+(2**i))**2
    x += (2**i)
    
print(x_n)