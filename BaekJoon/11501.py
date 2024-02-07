import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    
    have_stock = 0
    money = 0 
    x = stock[-1]
    
    for i in range(N-1,-1,-1):
        if x >= stock[i]:
            money += x -stock[i]
        else:
            x = stock[i]
            
    result.append(money)

for x in result:
    print(x)